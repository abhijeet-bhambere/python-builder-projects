import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Streamlit Data Streamer", layout="wide")
st.title("Sample data streamer")

# sample_df = pd.DataFrame({"vals":sample_vals})
sample_df = pd.DataFrame(columns=["vals"])

# Defining 2 columns:
c1, c2 = st.columns(2)
with c1:
    st.subheader("Live Line Chart")
    chart_placeholder = st.empty()
with c2:
    st.subheader("Live Data Table")
    table_placeholder = st.empty()

total_iterations = 10
chunk_size = 8

for i in range(total_iterations):
    # Create the new chunk
    # Creating a df of random integer values
    sample_vals = np.round(np.random.normal(28,3.0,size=chunk_size),2)
    # sample_vals = [20,23,22,25,26,24,23,22,24,27,28,26,25,24,23,24,25,20,23,22,25,26,24,23,22,24,27,28,26,25,24,23,24,25,20,23,22,25,26,24,23,22,24,27,28,26,25,24,23,24,25]
    
    new_chunk = pd.DataFrame({"vals": sample_vals})
    
    # Append to master_df using concat (the modern way)
    master_df = pd.concat([sample_df, new_chunk], ignore_index=True)
    
    # Update the placeholders
    chart_placeholder.line_chart(master_df["vals"])
    table_placeholder.dataframe(master_df) # Use .dataframe instead of .table for better performance
    
    time.sleep(0.2)


st.success("Data stream completed!")