import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="Smart Energy Dashboard", layout="wide")

st.title("⚡ Smart Energy Monitoring Dashboard")

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/dataset.csv")

# ---------------- DATA CLEANING ----------------
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df["Global_active_power"] = pd.to_numeric(df["Global_active_power"], errors="coerce")
df["Voltage"] = pd.to_numeric(df["Voltage"], errors="coerce")
df["Global_intensity"] = pd.to_numeric(df["Global_intensity"], errors="coerce")

df["Sub_metering_1"] = pd.to_numeric(df["Sub_metering_1"], errors="coerce")
df["Sub_metering_2"] = pd.to_numeric(df["Sub_metering_2"], errors="coerce")
df["Sub_metering_3"] = pd.to_numeric(df["Sub_metering_3"], errors="coerce")

df = df.dropna()
df = df.reset_index(drop=True)

# ---------------- DATA PREVIEW ----------------
st.subheader("📊 Dataset Preview")
st.dataframe(df.head())

# ---------------- STATISTICS ----------------
st.subheader("📈 Statistics")
st.write(df.describe())

# ---------------- INSIGHTS ----------------
st.subheader("⚡ Energy Insights")

st.write("Average Power Usage:", df["Global_active_power"].mean())
st.write("Maximum Power Usage:", df["Global_active_power"].max())
st.write("Minimum Power Usage:", df["Global_active_power"].min())

# ---------------- POWER CONSUMPTION ----------------
st.subheader("⚡ Power Consumption Over Time")

fig1 = px.line(
    df,
    x="Date",
    y="Global_active_power",
    title="Power Consumption Trend"
)
st.plotly_chart(fig1)

# ---------------- VOLTAGE ----------------
st.subheader("🔋 Voltage Over Time")

fig2 = px.line(
    df,
    x="Date",
    y="Voltage",
    title="Voltage Trend"
)
st.plotly_chart(fig2)

# ---------------- CURRENT ----------------
st.subheader("⚙️ Current Over Time")

fig3 = px.line(
    df,
    x="Date",
    y="Global_intensity",
    title="Current Trend"
)
st.plotly_chart(fig3)

# ---------------- SUB METERING ----------------
st.subheader("🏠 Sub Metering Comparison")

fig4 = px.line(
    df,
    x="Date",
    y="Sub_metering_1",
    title="Sub Metering 1"
)
st.plotly_chart(fig4)

fig5 = px.line(
    df,
    x="Date",
    y="Sub_metering_2",
    title="Sub Metering 2"
)
st.plotly_chart(fig5)

fig6 = px.line(
    df,
    x="Date",
    y="Sub_metering_3",
    title="Sub Metering 3"
)
st.plotly_chart(fig6)