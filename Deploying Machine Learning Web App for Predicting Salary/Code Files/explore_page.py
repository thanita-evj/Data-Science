import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Others" # combine the small number of countries into Others
    return categorical_map

def clean_experience(x):
    if x == "More than 50 years":
        return 50
    if x == "Less than 1 year":
        return 0.5
    return float(x)

def clean_education(x):
    if "Bachelor’s degree (B.A., B.S., B.Eng., etc.)" in x:
        return "Bachelor's degree"
    if "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)" in x:
        return "Master's degree"
    if "Professional degree (JD, MD, etc.)" in x or "Other doctoral degree (Ph.D., Ed.D., etc.)" in x:
        return "Post grad"
    return "Less than a Bachelors"

# data transformation
@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel","YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly": "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["Salary"] <= 300000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Others"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Engineer Salaries")

    st.write("""### Stack Overflow Developer Survey 2022""")

    # plot 1 - number of data
    st.write("#### Number of Data from Different Countries")
    data = df["Country"].value_counts()
    st.bar_chart(data)

    # plot 2 - mean salary based on country
    st.write("""#### Mean Annual Salary Based on Countries""")

    data2 = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data2)
   
   # plot 3 - mean salary based on experience
    st.write("""#### Mean Annual Salary Based on Years of Experiences""")

    data3 = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data3)