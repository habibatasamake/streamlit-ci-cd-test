import pandas as pd 

def load_data(dataframe_path):
    """_summary_
    load the data 
    Args:
        dataframe_path (_type_): dataframe_path
    """
    df = pd.read_csv(dataframe_path)
    return df
