# Prediction of Readmission of Diabetic Patients from 1999-2008

This repository is to store classification models to predict hospital readmissions regarding patients with diabetes. The data set chosen was provided by Virginia Commonwealth University and downloaded from [kaggle](https://www.kaggle.com/brandao/diabetes).

## Business Problem
Determining treatment effectiveness within diabetic pateints is an ardous process. Therefore, predicting readmission possibility of patients would allow care-providers to determine treatment qaulity, effectiveness, and prepare further treatment plans if necessary. Also, classifying high risk patients would determine ineffective or errorneous treatments, reducing treatment risks in the future. This prediction model will provide insight to treatment effecitiveness, cost reduction method, and reduced medical risks to careproviders. Hospitals and insurance angency can utilize this model to increase logistical and financial support for highly effective treatments and high risk patients.

## Methods

1. Clean data set by creating dummy variables for categorical data
    1A. Diagnosis categorized per ICD9 code group defined by related study refere to decription.pdf page 5 table 2.
    2A. Dropped irrelevant or largely missing data columns such as pateint ID and weight.
2. Perform EDA on cleaned data to gain understanding of statistical significance for feature engineering. Also create data visualizatoin of statistically signifiant features.
3. Create baseline models for iterative improvements using recall as the scoring metric.
4. Select best perfomring model and crate final prediction for model performance analysis.

## Repository Structure
    .
    ├── src                             # source code for custom functions
    ├── data                             # source code for custom functions
    ├── notebooks                         # contained matplotlib plots  
        ├── reddit_scrape_praw.ipynb        # notebook for analysis
    └── README.md