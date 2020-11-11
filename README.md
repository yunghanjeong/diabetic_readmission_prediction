# Prediction of Readmission of Diabetic Patients from 1999-2008
**Authors** <br>
[Yung Han Jeong](https://github.com/yunghanjeong)<br>
[Malcolm Katzenbach](https://github.com/malcolm206)<br>

## Overview
This project will create classification models to predict hospital readmissions regarding patients with diabetes through data provided by Virginia Commonwealth University (downloaded from [kaggle](https://www.kaggle.com/brandao/diabetes)) from 1999-2008 with 130 U.S. hospitals. Predicting high risk patients will provide valuable information to the careproviders to better prepare future care needs of diabetic patients. 

## Business Problem
Determining treatment effectiveness within diabetic pateints is an ardous process. Therefore, predicting readmission possibility of patients would allow care-providers to determine treatment qaulity, effectiveness, and prepare further treatment plans if necessary. Also, classifying high risk patients would determine ineffective or errorneous treatments, reducing treatment risks in the future. This prediction model will provide insight to treatment effecitiveness, cost reduction method, and reduced medical risks to careproviders. Hospitals and insurance angency can utilize this model to increase logistical and financial support for highly effective treatments and high risk patients.

## Data
The data provided by Virginia Commonwealth University collected from 130 U.S. hospitals over the years of 1999-2008 on diabetic pateints. The data is separated by unique patient ID and provides features such as number of medications, hospital stays, and sex. The readmission status was defined as "No", no readmission in that year, "<30", readmitted within 30 days of last visit, and ">30", readmitted after 30 days period. 

A supporting documetion, description.pdf, Impatct of HbA1c Measurement on Hospital Readmission Rates: Analysis of 70,000 Clinical Databse Patient Records was also provided as reference. 

## Methods

1. Clean data set by creating dummy variables for categorical data 
    - Diagnosis categorized per ICD9 code group defined by related study refere to decription.pdf page 5 table 2.
    - Dropped irrelevant or largely missing data columns such as pateint ID and weight.
2. Perform EDA on cleaned data to gain understanding of statistical significance for feature engineering. Also create data visualizatoin of statistically signifiant features.
3. Create baseline models for iterative improvements using recall as the scoring metric.
4. Select best perfomring model and crate final prediction for model performance analysis.
5. Compare feature weights and ranks among the best performing model to determine significant indicators of readmission prediction. 

## Exploratory Data Analysis

The predictant, readmitted, displays class imbalance with no readmission dominating the class, followed by greater 30 days, then less than 30 days. 

**some graph about data spread**

The age category of patients were skewed towards the older (>50) patients. 

![age_graph](https://github.com/yunghanjeong/diabetic_readmission_prediction/blob/main/image/Age_Readmiited.png?raw=true)

Some of the significant features of readmission predictions were following: 

The probability of readmission was directly related to the number of diagnoses of the patient during the visit. 

![num_diag](https://github.com/yunghanjeong/diabetic_readmission_prediction/blob/main/image/Percentage_NoD_Readmitted.png?raw=true)

The number of inpatient visits were a significant factor in determining readmission possibilities. 

![inpatient](https://github.com/yunghanjeong/diabetic_readmission_prediction/blob/main/image/num_inpatient_violin.png?raw=true)

## Model Evaluation

## Summary

## Future Steps



## Repository Structure
    .
    ├── data                                    # contains all data used
    |    ├── ICM9_reference                     # ICM9 code for reference
    ├── image                                   # contains all visualization and local images
    ├── model                                   # conatain all final models and feature info
    ├── notebooks                               # contains all work notebooks
    |    ├── data_preparation.ipynb             # data clean and feature engineering
    |    ├── diabetes_readmission_model.ipynb   # model building and tuning
    |    ├── diabetes_readmission_eda.ipynb     # EDA and visulization
    ├── final.ipynb                             # EDA and visulization
    └── README.md
