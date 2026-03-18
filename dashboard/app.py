import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('/data/website_data.csv')

# Classification
def classify_site(row):
    if row['bounce_rate'] > 65:
        return "Needs Optimization"
    elif row['seo_score'] > 85:
        return "High Performer"
    else:
        return "Average"

df['category'] = df.apply(classify_site, axis=1)

# Title
st.title("📊 Website Performance & SEO Dashboard")

# KPIs
st.subheader("Key Metrics")

col1, col2, col3 = st.columns(3)
col1.metric("Average Load Time", round(df['load_time'].mean(), 2))
col2.metric("Average SEO Score", round(df['seo_score'].mean(), 2))
col3.metric("Average Bounce Rate", round(df['bounce_rate'].mean(), 2))

# Filter
st.subheader("Filter by Category")
category = st.selectbox("Select category", df['category'].unique())
filtered_df = df[df['category'] == category]

# Table
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Charts
st.subheader("SEO Score Distribution")
st.bar_chart(df['seo_score'])

st.subheader("Load Time vs Bounce Rate")
st.scatter_chart(df[['load_time', 'bounce_rate']])
