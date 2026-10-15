
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Performance Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Performance Analyzer")
st.write("Analyze student marks and academic performance.")

# Sample student dataset
data = {
    "Name": ["Anu", "Balu", "Charan", "Divya", "Esha"],
    "Python": [85, 72, 45, 92, 65],
    "Java": [78, 68, 38, 88, 70],
    "DBMS": [90, 75, 42, 95, 60]
}

df = pd.DataFrame(data)
subjects = ["Python", "Java", "DBMS"]

df["Average"] = df[subjects].mean(axis=1).round(2)
df["Result"] = df[subjects].ge(40).all(axis=1).map(
    {True: "Pass", False: "Fail"}
)

topper = df.loc[df["Average"].idxmax()]

# Summary metrics
c1, c2, c3 = st.columns(3)

c1.metric("Total Students", len(df))
c2.metric("Class Average", round(df["Average"].mean(), 2))
c3.metric("Topper", topper["Name"])

st.subheader("Student Performance Report")
st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("Subject-wise Marks")
st.bar_chart(df.set_index("Name")[subjects])

st.subheader("Average Marks by Student")
st.bar_chart(df.set_index("Name")["Average"])

st.subheader("Pass / Fail Summary")
counts = df["Result"].value_counts()
st.bar_chart(counts)

st.success(
    f"Top Performer: {topper['Name']} "
    f"with an average of {topper['Average']} marks."
)

csv_data = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download Student Report",
    data=csv_data,
    file_name="student_report.csv",
    mime="text/csv"
)

st.caption("Built with Python, Pandas and Streamlit.")
