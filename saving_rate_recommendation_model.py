# -*- coding: utf-8 -*-
"""recomendations_financial_health_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qBFZi95pfmijBYb3F-zzRcjHStzt5K9I

# **Import Library**
"""

import tensorflow as tf
import pandas as pd
import numpy as np

"""# **Loading Dataset**

"""

from google.colab import files

# Mengupload file financial_data_indonesia_recomendation.csv
uploaded = files.upload()

df = pd.read_csv("financial_data_indonesia_recommendation.csv")


# Sample preview of the data
df.head()

"""## **EDA**"""

df.info()

df.describe()

df.isnull().all()

"""# **Preparing Data**

**Encoding Category Column**
"""

from sklearn.preprocessing import LabelEncoder

# Create a LabelEncoder object for the 'location' feature
label_encoder_location = LabelEncoder()

# Encode the 'location' column in the dataframe using the label encoder
df['location'] = label_encoder_location.fit_transform(df['location'])

# Display the unique classes/labels for the 'location' feature after encoding
print("Classes for 'location':", label_encoder_location.classes_)

# Display the first few rows of the dataframe after encoding the 'location' feature
print(df.head())

"""**Split Data**"""

from sklearn.model_selection import train_test_split

# Define the input features and target variable
features = ['location', 'age', 'income', 'food_expenses', 'transport_expenses', 'housing_cost', 'water_bill',
            'electricity_bill', 'internet_cost', 'debt', 'savings']
targets = ['r_saving_rate']

# Separate the features (X) and target (y) from the dataset
X = df[features]  # Input features
y = df[targets]  # Target variable (saving rate recommendation)

# Split the dataset into training set (80%) and temporary set (20%)
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)

# Split the temporary set into validation (50%) and test (50%) sets
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

print(f"X_train shape: {X_train.shape}")
print(f"X_val shape: {X_val.shape}")
print(f"X_test shape: {X_test.shape}")

"""**Scaling Some Column**"""

from sklearn.preprocessing import StandardScaler

# Initialize the StandardScaler for both features and target
feature_scaler = StandardScaler()
target_scaler = StandardScaler()

# Define the features to scale
features_to_scale = [
    'income', 'food_expenses', 'transport_expenses',
    'housing_cost', 'water_bill', 'electricity_bill',
    'internet_cost', 'debt', 'savings'
]

# Create copies of the datasets to avoid altering the original data
X_train_scaled = X_train.copy()
X_val_scaled = X_val.copy()
X_test_scaled = X_test.copy()

y_train_scaled = y_train.copy()
y_val_scaled = y_val.copy()
y_test_scaled = y_test.copy()

# Scale the features in the training, validation, and test datasets
X_train_scaled[features_to_scale] = feature_scaler.fit_transform(X_train[features_to_scale])
X_val_scaled[features_to_scale] = feature_scaler.transform(X_val[features_to_scale])
X_test_scaled[features_to_scale] = feature_scaler.transform(X_test[features_to_scale])

# Scale the target values
y_train_scaled[targets] = target_scaler.fit_transform(y_train[targets].values.reshape(-1, 1))
y_val_scaled[targets] = target_scaler.transform(y_val[targets].values.reshape(-1, 1))
y_test_scaled[targets] = target_scaler.transform(y_test[targets].values.reshape(-1, 1))

# Display the first few rows of the scaled features and targets in the training set
print("Scaled Features (Training):")
print(X_train_scaled[features_to_scale].head())

print("\nScaled Targets (Training):")
print(y_train_scaled[targets].head())

# Display the first few rows of the scaled training data
print(X_train.head())

"""# **Modelling**"""

from tensorflow.keras import Sequential, layers
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import regularizers

# Function to build a Sequential model
def build_model(input_shape, dropout_rate=0.5, l2_reg=0.001, learning_rate=0.00001):
    model = Sequential([
        Dense(256, activation='relu', kernel_regularizer=regularizers.l2(l2_reg), input_shape=(input_shape,)),
        Dropout(dropout_rate),  # Dropout layer to prevent overfitting
        Dense(128, activation='relu', kernel_regularizer=regularizers.l2(l2_reg)),
        Dropout(dropout_rate),
        Dense(64, activation='relu', kernel_regularizer=regularizers.l2(l2_reg)),
        Dropout(dropout_rate),
        Dense(1, activation='linear')  # Output layer for 1 target recommendation
    ])
    # Compile the model with Adam optimizer, MSE loss, and MAE metric
    model.compile(optimizer=Adam(learning_rate=learning_rate),
                  loss='mean_squared_error',
                  metrics=['mae'])
    return model

# Function to train the model
def train_model(model, X_train, y_train, X_val, y_val, epochs=50, batch_size=32, patience=10):
    # Early stopping to monitor validation loss and stop training if it doesn't improve
    early_stopping = EarlyStopping(monitor='val_loss', patience=patience, restore_best_weights=True)
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(X_val, y_val),  # Using validation data to monitor performance
        callbacks=[early_stopping]  # Stop training early if the validation loss stops improving
    )
    return history

# Function to evaluate and save the model
def evaluate_and_save_model(model, X_test, y_test):
    # Evaluate the model on the test set
    test_loss, test_mae = model.evaluate(X_test, y_test)
    print(f"Test Loss: {test_loss}, Test MAE: {test_mae}")
    # Save the model in two formats: H5 and Keras
    model.save('saving_rate_recommendation_model.h5')
    print(f"Model saved to {'saving_rate_recommendation_model.h5'}")
    model.save('saving_rate_recommendation_model.keras')
    print(f"Model saved to {'saving_rate_recommendation_model.keras'}")

# Build the model
input_shape = X_train_scaled.shape[1]  # The number of features in the training data
model = build_model(input_shape)

# Train the model
history = train_model(model, X_train_scaled, y_train_scaled, X_test_scaled, y_test_scaled)

# Evaluate and save the model
evaluate_and_save_model(model, X_test_scaled, y_test_scaled)

from sklearn.metrics import mean_absolute_error, mean_squared_error

# Evaluation function for the model
def evaluate_model(model, X_test_scaled, y_test_scaled, target_scaler, targets):
    """
    Evaluates the model's performance on the test set and returns relevant metrics.
    Additionally, it returns the predicted values after transforming them back to the original scale.
    """
    # Check shapes of the input data
    print(f"Shape of X_test_scaled: {X_test_scaled.shape}")
    print(f"Shape of y_test_scaled: {y_test_scaled.shape}")

    # Ensure that X_test and y_test have the same number of samples
    if X_test_scaled.shape[0] != y_test_scaled.shape[0]:
        raise ValueError(f"Mismatch in the number of samples: {X_test_scaled.shape[0]} vs {y_test_scaled.shape[0]}")

    # Predict the target values for the test set (scaled)
    y_pred_scaled = model.predict(X_test_scaled)

    # Reshape the predictions to match the target shape (2D for inverse transformation)
    y_pred_scaled = y_pred_scaled.reshape(-1, 1)

    # Transform the predictions back to the original scale
    y_pred = target_scaler.inverse_transform(y_pred_scaled)

    # Ensure the target data is selected correctly (only the relevant column)
    y_true = target_scaler.inverse_transform(y_test_scaled[targets].to_numpy().reshape(-1, 1))

    # Check if the shapes of y_true and y_pred match
    print(f"Shape of y_true: {y_true.shape}")
    print(f"Shape of y_pred: {y_pred.shape}")

    # Calculate evaluation metrics
    mae = mean_absolute_error(y_true, y_pred)  # Mean Absolute Error
    mse = mean_squared_error(y_true, y_pred)  # Mean Squared Error
    rmse = np.sqrt(mse)  # Root Mean Squared Error

    # Print the evaluation metrics
    print("\nEvaluation Metrics on Test Set:")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Mean Squared Error (MSE): {mse:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

    # Return true values and predicted values for further analysis if needed
    return y_true, y_pred

# Calling the evaluation function with targets
y_true, y_pred = evaluate_model(model, X_test_scaled, y_test_scaled, target_scaler, targets)

# Displaying some sample predictions vs actual values
print("\nSample Predictions vs Actual:")
for i in range(5):
    print(f"Predicted: {y_pred[i][0]:.2f}, Actual: {y_true[i][0]:.2f}")

# Fit the Scaler on the Training Data (this should be done only once)
feature_scaler.fit(X_train[feature_names])  # Fit the scaler with the training data

# Function to get user input for each feature
def get_user_input(feature_names):
    user_data = []
    for feature in feature_names:
        if feature == 'location':  # For 'location', use LabelEncoder
            value = input(f"Please enter the location ({', '.join(label_encoder_location.classes_)}): ")
            value = label_encoder_location.transform([value])[0]  # Convert input to encoded label
        else:  # For other features, take numeric input
            value = float(input(f"Please enter the value for {feature}: "))
        user_data.append(value)
    return np.array([user_data])  # Return as numpy array for model input

# Function to predict recommendations based on user input
def predict_recommendations(model, user_input, feature_scaler):
    # Scale the user input
    user_input_scaled = feature_scaler.transform(user_input)  # Transform input with the scaler

    # Ensure reshaping for 2D input
    user_input_scaled = user_input_scaled.reshape(1, -1)  # Shape (1, num_features)

    # Predict the recommendation
    prediction = model.predict(user_input_scaled)
    return prediction[0]  # Return the first prediction

# Get user input for each feature
user_input = get_user_input(features)

# Reshape the input to match the model input shape (2D)
user_input_reshaped = np.reshape(user_input, (1, -1))

# Make the prediction and return it to the original scale
predicted_recommendations = predict_recommendations(model, user_input_reshaped, feature_scaler)

# Convert the predicted recommendations back to the original scale
predicted_r_saving_rate = target_scaler.inverse_transform(predicted_recommendations.reshape(-1, 1))

# Display the predicted result in the original scale, rounded to 2 decimal places
print(f"\nPredicted r_saving_rate (%): {predicted_r_saving_rate[0][0]:.2f}")
