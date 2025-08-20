import pandas as pd
import streamlit as st
import numpy as np

filenames = []

st.title("Data Cleaner!")

with st.form(key='datacleaner'):
    uploaded_files = st.file_uploader("Choose CSV files", type="csv", accept_multiple_files=True)

    if uploaded_files is not None:
        
        st.write('Choose your options')
        
        remove_emp = st.checkbox('Remove empty rows ')
        remove_dup = st.checkbox('Remove duplicate rows')
        
        dataframes = []
        for i,file in enumerate(uploaded_files):
            try:
                df = pd.read_csv(file)
                dataframes.append(df)
                st.write("filename:", file.name)
                filenames.append(file.name)
            except pd.errors.EmptyDataError:
                st.error('Something wrong with your file, try again!')
        
        if dataframes:
            dataframe = pd.concat(dataframes, axis=0, ignore_index=True)
                 
        submit = st.form_submit_button(label='Submit')
        
        if submit and dataframes:
            if remove_emp:
                dataframe = dataframe.replace(r'^\s*$', np.nan, regex=True)
                dataframe = dataframe.dropna(axis=1)
            if remove_dup:
                dataframe = dataframe.drop_duplicates()
            st.dataframe(dataframe)
                
            
            
if dataframes: 
           
    csv = dataframe.to_csv(index=False).encode('utf-8')             
    option = st.selectbox(
        "Choose the name", filenames,
        )
        
            
    st.download_button(
                label="Download CSV",
                data=csv,
                file_name=f"{option}",
                mime="text/csv",
                icon=":material/download:",
            )
                
        