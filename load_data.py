import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def load_data(dataframe_path):
    """_summary_
    load the data 
    Args:
        dataframe_path (_type_): dataframe_path
    """
    df = pd.read_csv(dataframe_path)
    return df

def construct_hist_for_column(dataframe,column_name):
    """_summary_
    Generate a histogram for a column from a dataframe
    Args:
        dataframe (_type_): _description_
        column_name (_type_): _description_
    """
    # Création de l'histogramme sans définir de bins
    fig, ax = plt.subplots()
    sns.histplot(dataframe[column_name], kde=False, ax=ax)

    # Définir les titres et labels
    ax.set_title(f"Répartition de {column_name}")
    ax.set_xlabel(column_name)
    ax.set_ylabel('Fréquence')

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)