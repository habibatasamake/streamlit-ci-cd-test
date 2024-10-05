import streamlit as st
import pandas as pd

def main():
    st.title("Hello, World!")
    st.write("Ceci est une application Streamlit déployée via CI/CD avec GitHub Actions.")
    # Créer un DataFrame simple
    data = {
        'Column A': [1, 2, 3, 4],
        'Column B': [10, 20, 30, 40]
    }
    df = pd.DataFrame(data)

    # Afficher le DataFrame dans l'application Streamlit
    st.write("Voici un DataFrame simple:")
    st.dataframe(df)

if __name__ == "__main__":
    main()
    