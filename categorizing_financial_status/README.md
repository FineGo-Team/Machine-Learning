# Categorizing Financial Status

This folder contains files related to the classification model for financial status based on income, expenses, and other factors. The dataset used for this model was created using authentic data from the **Badan Pusat Statistik (BPS)** (Indonesian Statistics Agency) on the Regional Minimum Wage (UMR) for each province in Indonesia in 2020, further enhanced using Python for training and testing purposes.

## **Folder Contents**
- `categorizing_financial_health_model.ipynb`: A Jupyter Notebook containing the code for data preprocessing, model training, and evaluation of the financial status classification model.
- `categorizing_financial_health_model.h5`: A trained model file in H5 format, ready for deployment or inference.
- `categorizing_financial_health_model.keras`: A trained model file saved in Keras format.
- `categorizing_financial_health_model.py`: A standalone Python script for training and evaluating the model.
- `financial_data_indonesia.csv`: A developed dataset used for training the model.

## **About the Dataset**
The dataset used in this project was developed based on authentic data on the Regional Minimum Wage (UMR) for each province in Indonesia in 2020, published by the **Badan Pusat Statistik (BPS)**.  
- **Original source:** UMR 2020 data from BPS.  
- **Development process:**  
  The dataset was enhanced using Python by adding several new columns, such as expenses for basic needs (food, transportation, housing), monthly bills (water, electricity, internet), debts, savings, and financial status determined based on the ratio of income to expenses.

This dataset serves as simulated data for training the classification model, categorizing financial health into three categories: **Sehat**, **Kurang Sehat**, and **Tidak Sehat**.

## **Usage**
1. Run the `categorizing_financial_health_model.ipynb` file to train and evaluate the model.
2. Use the trained model files (`.h5` or `.keras`) for deployment.
3. The dataset (`financial_data_indonesia.csv`) can be used for further experimentation or model validation.

## **License**
This dataset was created for educational and machine learning model development purposes. The original data comes from the **Badan Pusat Statistik (BPS)**, and further development was conducted independently. Please respect copyright and data policies when using this information.
