# import libraries
import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px


st.set_page_config(layout='wide',
                    page_title='Car Price Predict',
                    page_icon='🚗',)

def run():
    # def run():
    # untuk menjalankan streamlit di terminal tulis
    # streamlit run <nama script>.py

    # Title and Header
    st.title('Prediksi Harga Mobil Bekas 🚗')

    st.image('https://imgsrv2.voi.id/suLydjR6Ej95G4wMRLvCcHvpboT70PfLeYrWDjtN4iI/auto/1200/675/sm/1/bG9jYWw6Ly8vcHVibGlzaGVycy8zMjE0MDQvMjAyMzEwMTkxNjIzLW1haW4uanBn.jpg')

    st.markdown('''
    ## Tentang
    Aplikasi ini dibuat untuk memprediksi harga mobil bekas berdasarkan fitur-fitur penting seperti tipe mobil,
                kapasitas mesin, jenis bahan bakar, dan lainnya.
                Model telah dilatih menggunakan algoritma Machine Learning untuk memberikan prediksi yang akurat.
    ''')

    st.write('# Introduction')

    '''
    ### Latar Belakang
    Pada pasar otomotif, menentukan harga jual mobil bekas sering menjadi tantangan bagi penjual dan pembeli.
    Harga mobil bekas dipengaruhi oleh berbagai faktor seperti merek, model, tahun pembuatan,
    kilometer yang telah ditempuh, kapasitas mesin, dan lainnya. Penilaian harga yang tidak akurat dapat menyebabkan.
    Dalam pasar mobil bekas, penentuan harga seringkali bersifat subjektif dan bergantung pada pengalaman atau penilaian pribadi.
    Hal ini dapat menyebabkan:
    - Harga jual yang tidak kompetitif.
    - Ketidakadilan dalam transaksi.
    - Kurangnya transparansi dalam proses negosiasi.
    - Maka, diperlukan sistem prediksi yang objektif untuk menentukan harga berdasarkan data historis dan spesifikasi kendaraan.

    ### Problem Statement
    Bagaimana membangun model prediksi yang akurat untuk menentukan harga jual mobil bekas menggunakan data historis
    dan spesifikasi teknis kendaraan, sehingga dapat meningkatkan kepercayaan dan efisiensi dalam proses jual-beli?.
    '''


    st.write('# Dataset')

    df = pd.read_csv('CarPrice_Assignment.csv')
    df['Type'] = df['CarName'].str.split(pat=' ', n=1).str[1]  # Ekstrak Type Mobil
    df['Brand'] = df['CarName'].str.split(pat=' ', n=1).str[0]  # Ekstrak Brand
    # Masukkan kolom Merek dan Jenis sesuai urutan yang diinginkan
    df.insert(1, 'Type', df.pop('Type'))
    df.insert(1, 'Brand', df.pop('Brand'))

    def fix_brand(df, old_name, new_name):
        df['Brand'] = df['Brand'].replace(old_name, new_name)

        # Memanggil fungsi perbaikan
        fix_brand(df, 'maxda', 'mazda')
        fix_brand(df, 'nissan', 'Nissan')
        fix_brand(df, 'porcshce', 'porsche')
        fix_brand(df, 'toyouta', 'toyota')
        fix_brand(df, 'vokswagen', 'volkswagen')
        fix_brand(df, 'vw', 'volkswagen')

    def fix_type(df, old_name, new_name):
        df['Type'] = df['Type'].replace(old_name, new_name)
        # Memanggil fungsi perbaikan
        fix_type(df, '100ls', '100 Ls')

    df.drop(['car_ID','CarName','symboling'], axis=1, inplace=True)
    df.loc[138, 'Type'] = 'Dl'   # Missing value pertama diisi dengan 'Subaru Dl'
    df.loc[141, 'Type'] = 'Brz'  # Missing value kedua diisi dengan 'Brz'

    st.dataframe(df, hide_index=True)

    st.write('# Exploratory Data Analysis')

    cat_cols = ['fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel',
                'enginelocation', 'enginetype', 'cylindernumber', 'fuelsystem']

    # Define kolom Numerik untuk dianalisis
    num_cols = ['wheelbase', 'carlength', 'carwidth', 'carheight', 'curbweight',
                'enginesize', 'boreratio', 'stroke', 'compressionratio', 'horsepower',
                'peakrpm', 'citympg', 'highwaympg', 'price']

    # visualisasi data
    st.write('### Distribusi Harga Mobil')
    fig = plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x='price', bins=20, kde=True)
    st.pyplot(fig)

    '''- Mobil bekas dengan harga yang lebih murah lebih umum dalam dataset, Sesuai dengan pola pasar di mana mobil dengan harga terjangkau lebih mudah dijual.
    - Harga tinggi merupakan outlier tetapi dalam data set ini mencerminkan mobil mewah sport dan tidak akan di handling outliers karena kolom `price` adalah __Target__.'''

    # Scatter plot
    fig = px.scatter(data_frame=df, x='enginesize', y='price', 
                    hover_data=['carbody', 'drivewheel'])
    st.plotly_chart(fig)

    # Selectbox for columns
    selected_col = st.selectbox('Pilih Kolom untuk Visualisasi', options=df.columns[2:24])
    st.write(f'### Distribusi Kolom: {selected_col}')
    fig = plt.figure(figsize=(10, 5))
    sns.histplot(data=df, x=selected_col, bins=20, hue='price')