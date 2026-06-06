from ai_analyzer import analyze_log_ai
from analyzer import analyze_log
import pandas as pd
import streamlit as st

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("AI SOC Analyst Assistant")
st.write("Upload Excel file containing SOC logs")

# --------------------------------------------------
# Upload Excel File
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload Excel File",
    type=["xlsx"]
)

# --------------------------------------------------
# Read Uploaded File
# --------------------------------------------------
if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    st.success("Logs received successfully")

    st.write("### Uploaded Logs")
    st.dataframe(df)

    # --------------------------------------------------
    # Analyze Button
    # --------------------------------------------------
    if st.button("Analyze Logs"):

        st.write("## AI Analysis Results")

    # Analyze only first 5 logs
    for index, row in df.head(5).iterrows():

        log_data = row["log"]

        st.write(f"### Log {index + 1}")
        st.code(log_data)

        with st.spinner("Analyzing..."):

            result = analyze_log_ai(log_data)

        st.write(result)

        st.divider()
