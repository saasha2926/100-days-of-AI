import streamlit as st
import pandas as pd
from eda_agent import EDAAgent

def main():
    st.title("CSV File Upload and EDA")

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        # Read the CSV file
        df = pd.read_csv(uploaded_file)
        agent = EDAAgent(df)

        # Display the dataframe
        st.write("Data Preview:")
        st.dataframe(df)

        # User input for analysis
        user_query = st.text_input("What analysis would you like to perform?")

        if user_query.lower() == 'summary':
            st.write(agent.summarize_data())
        elif user_query.lower().startswith('visualize'):
            column_name = user_query.split()[-1]
            agent.visualize_data(column_name)
        elif user_query.lower() == 'missing':
            agent.visualize_missing_data()
        else:
            st.write("Unknown command")

if __name__ == "__main__":
    main()
