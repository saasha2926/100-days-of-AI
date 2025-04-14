import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sweetviz as scv
import missingno as msno
import streamlit as st

class EDAAgent:
    def __init__(self,dataframe):
        self.df = dataframe

    def summarize_data(self):
        return self.df.describe()

    def visualize_data(self,column_name):
        plt.figure(figsize=(10,6))
        sns.histplot(self.df[column_name],kde=True)
        plt.title(f'Distribution of {column_name}')
        st.pyplot(plt)
        plt.clf


    def visualize_missing_data(self):
        msno.matrix(self.df)
        st.pyplot(plt)
        plt.clf()
