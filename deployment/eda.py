import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO

def run():
    left, center, right = st.columns([1, 15, 1])

    with center:
        st.markdown("<h1 style='text-align: center;'>📊 Exploratory Data Analysis (EDA)</h1>", unsafe_allow_html=True)

        try:
            df = pd.read_csv("data_clean.csv")
        except FileNotFoundError:
            st.error("❌ Dataset file `data_clean.csv` not found.")
            return

        st.markdown(
        "<p style='text-align: center;'>This page presents an overview of the data used in the used car price prediction model.</p><hr>", 
        unsafe_allow_html=True
    )

        # Filter interaktif
        brand_filter = st.multiselect("🔎 Car Brand Filter:", options=sorted(df["Brand"].unique()), default=sorted(df["Brand"].unique()))
        filtered_df = df[df["Brand"].isin(brand_filter)]

        st.subheader("🔍 Dataset Overview")
        st.dataframe(filtered_df.head())

        st.subheader("📈 Descriptive Statistics")
        st.dataframe(filtered_df.describe())

        # Distribusi Harga
        st.subheader("💰 Used Car Price Distribution")
        fig, ax = plt.subplots(figsize=(16, 8))
        sns.histplot(filtered_df["price"], bins=30, kde=True, ax=ax, color='skyblue')
        st.pyplot(fig)

        # Korelasi Spearman
        st.subheader("🔗 Correlation Between Numerical Features (Spearman)")
        corr = filtered_df.select_dtypes(include='number').corr(method='spearman')
        fig, ax = plt.subplots(figsize=(16, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
        st.pyplot(fig)

        # Distribusi Brand
        st.subheader("🏷️ Total Car Brands")
        fig, ax = plt.subplots(figsize=(16, 8))
        brand_counts = filtered_df["Brand"].value_counts()
        sns.barplot(x=brand_counts.values, y=brand_counts.index, ax=ax)
        ax.set_xlabel("Amount")
        ax.set_ylabel("Brand")
        st.pyplot(fig)

        # Harga Rata-rata per Brand (Top 10)
        st.subheader("💵 Top 10 Brands By Average Price")
        mean_prices = filtered_df.groupby("Brand")["price"].mean().sort_values(ascending=False).head(10)
        fig, ax = plt.subplots(figsize=(16, 8))
        sns.barplot(x=mean_prices.values, y=mean_prices.index, ax=ax)
        ax.set_xlabel("Average Price")
        ax.set_ylabel("Brand")
        for i, v in enumerate(mean_prices.values):
            ax.text(v + 200, i, f"{int(v):,}", va="center")
        st.pyplot(fig)

        # Distribusi Tipe Mobil
        st.subheader("🚘 Car Type Distribution")
        fig, ax = plt.subplots(figsize=(16, 8))
        sns.countplot(data=filtered_df, x='carbody', order=filtered_df['carbody'].value_counts().index, ax=ax)
        st.pyplot(fig)

        # Distribusi Drive Wheel
        st.subheader("⚙️ Drive Wheel Distribution")
        fig, ax = plt.subplots(figsize=(16, 8))
        sns.countplot(data=filtered_df, x='drivewheel', order=filtered_df['drivewheel'].value_counts().index, ax=ax)
        st.pyplot(fig)

        # Tombol Download Data
        st.markdown("### 📥 Download Dataset")
        csv = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="data_clean_filtered.csv",
            mime="text/csv"
        )

        st.info("📌 This EDA helps to understand the features that affect the price of a used car.")