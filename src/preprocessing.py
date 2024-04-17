import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def load_data(file_type):
    """
    Loads data from the specified type (train or test).

    Args:
    file_type (str): A string specifying the type of data to load ('train' or 'test').

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data.
    """
    # Define the base path depending on the type of data requested
    base_path = f'./data/{file_type}/'
    
    # Define the file name based on the provided type
    filename = 'train.csv' if file_type == 'train' else 'test.csv'

    # Construct the full file path
    file_path = f'{base_path}{filename}'
    
    # Load and return the data
    return pd.read_csv(file_path)

def preprocess_data(df):
    """
    Applies preprocessing steps to the given DataFrame.

    Args:
    df (DataFrame): A pandas DataFrame to preprocess.

    Returns:
    ndarray: The preprocessed data as a numpy array.
    """
    # Define numerical and categorical features
    numerical_features = ['Annual_Income', 'Num_Bank_Accounts', 'Num_Credit_Card', 'Age']
    categorical_features = ['Occupation', 'Education_Level']

    # Create transformers for numerical and categorical data
    transformers = [
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(), categorical_features)
    ]
    
    # Initialize and apply column transformer
    preprocessor = ColumnTransformer(transformers=transformers)
    return preprocessor.fit_transform(df)
