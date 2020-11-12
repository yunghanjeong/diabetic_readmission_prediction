import os
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 200) #set to show all columns
pd.set_option('display.max_rows', 200) 
import numpy as np

%matplotlib inline

# Load dataset
df = pd.read_csv("../data/diabetic_data.csv")

def create_dummy_columns(columns, dataframe):
    for column in columns:
        dummies = pd.get_dummies(dataframe[column], drop_first=True, prefix=column)
        dataframe = pd.concat([dataframe, dummies], axis=1)
        dataframe.drop(columns=column, inplace = True)
    return dataframe

def create_dummy_drugs(columns, dataframe):
    for drug_column in columns:
        if "No" not in dataframe[drug_column].unique(): 
            dummies = pd.get_dummies(dataframe[drug_column], prefix=drug_column)
        else:
            dummies = pd.get_dummies(dataframe[drug_column], prefix=drug_column)
            column_name = "_".join([drug_column, "No"])
            dummies.drop(columns=column_name, inplace=True)
        dataframe = pd.concat([dataframe, dummies], axis=1)
        dataframe.drop(columns=drug_column, inplace = True)
    return dataframe

def create_dummy_bloodtest(columns, dataframe):
    for blood_test in columns:
        dummies = pd.get_dummies(dataframe[blood_test],  prefix=blood_test)
        column_name = "_".join([blood_test, "None"])
        dummies.drop(columns=column_name, inplace=True)
        dataframe = pd.concat([dataframe, dummies], axis=1)
        dataframe.drop(columns=blood_test, inplace = True)
    return dataframe

def diagnosis_clean(value):
    # input: diagnosis code
    # output: diagnosis group based on code in the pdf
    if value in circulatory_list:
        return "circulatory"
    elif value in respiratory_list:
        return "respiratory"
    elif value in digestive_list:
        return "digestive"
    elif value in diabetes_list:
        return "diabetes"
    elif value in injury_list:
        return "injury"
    elif value in muscle_list:
        return "musculoskeletal"
    elif value in genit_list:
        return "genitourinary"
    elif value in neo_list:
        return "neoplasms"
    else:
        return "other"

def diagnosis_binning(dataframe):
    # get all diabetest diagnosis
    diab_diag_1 = list(df.diag_1.apply(lambda x: x if x[:3]=="250" else np.nan).dropna().unique())
    diab_diag_2 = list(df.diag_2.apply(lambda x: x if x[:3]=="250" else np.nan).dropna().unique())
    diab_diag_3 = list(df.diag_3.apply(lambda x: x if x[:3]=="250" else np.nan).dropna().unique())
    
    # get string value of all diagnosis code
    circulatory_list = [str(code) for code in range(390, 460, 1)] + ["785"]
    respiratory_list = [str(code) for code in range(460, 520, 1)] + ["786"]
    digestive_list = [str(code) for code in range(520, 580, 1)] + ["787"]
    diabetes_list = set(diab_diag_1 + diab_diag_2 + diab_diag_3)
    injury_list = [str(code) for code in range(800, 1000, 1)]
    muscle_list = [str(code) for code in range(710, 740, 1)]
    genit_list = [str(code) for code in range(580, 629, 1)] + ["788"]
    neo_list = [str(code) for code in range(140, 240, 1)]
    
    # replace diagnosis code with diagnosis group 
    dataframe.diag_1 = dataframe.diag_1.apply(diagnosis_clean)
    dataframe.diag_2 = dataframe.diag_2.apply(diagnosis_clean)
    dataframe.diag_3 = dataframe.diag_3.apply(diagnosis_clean)
    
    return dataframe

def create_dummy_diagnosis(columns, dataframe):
    for diag_col in columns:
        dummies = pd.get_dummies(dataframe[diag_col], prefix=diag_col)
        drop_col = "_".join([diag_col, "other"]) #dropped "other" diagnosis as reference column
        dummies.drop(columns=drop_col, inplace=True)
        dataframe = pd.concat([dataframe, dummies], axis=1)
        dataframe.drop(columns=diag_col, inplace=True)
    return dataframe

def clean_data(dataframe):
    # Drop columns with large missing values or had insignificant amount of data
    # Create list of columns needing to be dropped
    bad_columns = ['encounter_id', 'patient_nbr', 'payer_code', 'weight', 
               'medical_specialty', 'acetohexamide', 'tolbutamide',
              'troglitazone', 'examide', 'citoglipton', 'glipizide-metformin',
              'glimepiride-pioglitazone', 'metformin-rosiglitazone',
              'metformin-pioglitazone']
    
    # Drop columns from the bad_columns list
    df.drop(columns=bad_columns, inplace=True)
    
    # Drop index with missing gender information
    df.drop(index = df[df.gender == "Unknown/Invalid"].index, inplace=True)
    # update to numeric, male = 0 female = 1
    df.gender = df.gender.apply(lambda x: 0 if x == "Male" else 1)
    
    # list of columns to get dummy variables for
    dummy_columns = ["admission_type_id", "discharge_disposition_id", "admission_source_id", 
                 "age", "race"]
    # create dummy columns from column list
    df = create_dummy_columns(dummy_columns, df)

    # list of drug columns
    dummy_drug_columns =  ["metformin", "repaglinide", "nateglinide", "chlorpropamide", 
                     "glimepiride", "glipizide", "glyburide", "pioglitazone", "rosiglitazone", 
                     "acarbose", "miglitol", "tolazamide", "insulin", "glyburide-metformin"]
    # create dummy columns for drugs
    df = create_dummy_drugs(dummy_drug_columns, df)

    # list of blood tests
    blood_test_columns = ["max_glu_serum", "A1Cresult"]
    # create dummy columns for blood tests
    df = create_dummy_bloodtests(blood_test_columns, df)
    
    # bin diagnosis codes
    df = diagnosis_binning(df)
    # list diagnosis columns
    diagnosis_columns = ["diag_1", "diag_2", "diag_3"]
    # create dummy columns for diagnosis bins
    df = create_dummy_diagnosis(diagnosis_columns, df)
    
    clean_df = df
    return clean_df
    
    
    
    
    
    
    
    



