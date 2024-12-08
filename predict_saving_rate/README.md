# Predict Saving Rate

This folder contains files related to the regression model for predicting the recommended saving rate based on users' income, expenses, and other financial factors. The dataset used for this model was created using authentic data from the **Badan Pusat Statistik (BPS)** (Indonesian Statistics Agency) on the Regional Minimum Wage (UMR) for each province in Indonesia in 2020, further enhanced using Python to generate additional features.

## **Folder Contents**
- `saving_rate_recommendation_model.ipynb`: A Jupyter Notebook containing the code for data preprocessing, model training, and evaluation for predicting saving rates.
- `saving_rate_recommendation_model.h5`: A trained model file in H5 format, ready for deployment or inference.
- `saving_rate_recommendation_model.keras`: A trained model file saved in Keras format.
- `saving_rate_recommendation_model.py`: A standalone Python script for training and evaluating the regression model.
- `financial_data_indonesia_recommendation.csv`: A developed dataset used for training the model.

## **About the Dataset**
The dataset used in this project was developed based on authentic data on the Regional Minimum Wage (UMR) for each province in Indonesia in 2020, published by the **Badan Pusat Statistik (BPS)**.  
- **Original source:** UMR 2020 data from BPS.  
- **Development process:**  
  Using Python, the dataset was enhanced by adding various columns, such as income, expenses (food, transportation, housing, water bills, electricity bills, and internet bills), debts, savings, and the recommended saving rate. The saving rate recommendations were calculated based on financial data, taking into account common financial planning principles.

This dataset serves as simulated data for training the regression model, predicting a personalized recommended saving rate to help users improve their financial management.

## **Usage**
1. Run the `saving_rate_recommendation_model.ipynb` file to train and evaluate the regression model.
2. Use the trained model files (`.h5` or `.keras`) for deployment or inference.
3. The dataset (`financial_data_indonesia_recommendation.csv`) can be used for further experimentation or testing.

## **License**
This dataset was created for educational and machine learning model development purposes. The original data comes from the **Badan Pusat Statistik (BPS)**, and further development was conducted independently. Please respect copyright and data policies when using this information.

