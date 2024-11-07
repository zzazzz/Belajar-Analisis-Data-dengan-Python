import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
@st.cache_data
def load_data():
    day_df = pd.read_csv('/data/day.csv')
    hour_df = pd.read_csv('/data/hour.csv')
    return day_df, hour_df

day_df, hour_df = load_data()

# Sidebar navigation
st.sidebar.header("Navigasi")
menu = st.sidebar.selectbox("Pilih Halaman", options=["Visualisasi", "Dataframe"])
selected_year = st.sidebar.selectbox("Pilih Tahun", options=["2011", "2012", "2011-2012"])

# Filter data sesuai dengan tahun yang dipilih
if selected_year == "2011":
    filtered_day_df = day_df[day_df['yr'] == 0]
    filtered_hour_df = hour_df[hour_df['yr'] == 0]
elif selected_year == "2012":
    filtered_day_df = day_df[day_df['yr'] == 1]
    filtered_hour_df = hour_df[hour_df['yr'] == 1]
else:
    filtered_day_df = day_df  # Semua data untuk 2011-2012
    filtered_hour_df = hour_df

# Metadata dan Dataframe (halaman terpisah)
if menu == "Dataframe":
    st.title("Dataset Penyewaan Sepeda")

    st.write("## Dataset Characteristics")
    st.markdown(
        """
        ### Dataset characteristics
        Both `hour.csv` and `day.csv` have the following fields, except `hr` which is not available in `day.csv`:
        
        - **instant**: record index
        - **dteday**: date
        - **season**: season (1: spring, 2: summer, 3: fall, 4: winter)
        - **yr**: year (0: 2011, 1: 2012)
        - **mnth**: month (1 to 12)
        - **hr**: hour (0 to 23, only in `hour.csv`)
        - **holiday**: whether day is holiday (extracted from the official DC holiday schedule)
        - **weekday**: day of the week
        - **workingday**: 1 if day is neither weekend nor holiday, else 0
        - **weathersit**:
            - 1: Clear, Few clouds, Partly cloudy
            - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
            - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds
            - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
        - **temp**: Normalized temperature in Celsius (divided by 41)
        - **atemp**: Normalized feeling temperature in Celsius (divided by 50)
        - **hum**: Normalized humidity (divided by 100)
        - **windspeed**: Normalized wind speed (divided by 67)
        - **casual**: count of casual users
        - **registered**: count of registered users
        - **cnt**: total count of bike rentals (casual + registered)
        """
    )

    st.write("### Data Penyewaan Sepeda (Daily)")
    st.dataframe(filtered_day_df)

# Visualisasi (halaman utama)
else:
    st.title("Dashboard Penyewaan Sepeda Interaktif")

    # 1. Penyewaan Sepeda pada Hari Kerja vs Hari Libur
    st.write("### Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x='workingday', y='cnt', data=filtered_day_df, ax=ax)
    ax.set_title('Penyewaan Sepeda pada Hari Kerja vs Hari Libur')
    ax.set_xlabel('Jenis Hari')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticklabels(['Hari Libur', 'Hari Kerja'])
    st.pyplot(fig)

    # 2. Tren Penyewaan Sepeda Bulanan
    st.write("### Tren Penyewaan Sepeda Bulanan")
    fig, ax = plt.subplots(figsize=(14, 7))
    sns.lineplot(x='mnth', y='cnt', data=filtered_day_df, marker="o", label=f"Tahun {selected_year}")
    if selected_year != "2011-2012":
        prev_year = "2011" if selected_year == "2012" else "2012"
        prev_year_data = day_df[day_df['yr'] == (0 if prev_year == "2011" else 1)]
        sns.lineplot(x='mnth', y='cnt', data=prev_year_data, marker="o", label=f"Tahun {prev_year}")
    ax.set_title(f'Tren Penyewaan Sepeda Bulanan {selected_year}')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.legend(title='Tahun')
    st.pyplot(fig)

    # 3. Penyewaan Sepeda Berdasarkan Jenis Pengguna
    st.write("### Penyewaan Sepeda Berdasarkan Jenis Pengguna")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(filtered_hour_df['casual'], bins=30, kde=True, color="blue", label="Casual Users", ax=ax)
    sns.histplot(filtered_hour_df['registered'], bins=30, kde=True, color="orange", label="Registered Users", ax=ax)
    ax.set_title('Distribusi Penyewaan Sepeda (Casual vs Registered)')
    ax.set_xlabel('Jumlah Penyewaan')
    ax.set_ylabel('Frekuensi')
    ax.legend()
    st.pyplot(fig)

    # 4. Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu
    st.write("### Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
    fig, ax = plt.subplots(figsize=(14, 7))
    sns.lineplot(x='weekday', y='cnt', data=filtered_day_df, marker="o", color='orange', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
    ax.set_xlabel('Hari dalam Minggu')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticks(range(0, 7))
    ax.set_xticklabels(['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
    st.pyplot(fig)

    # 5. Distribusi Penyewaan Berdasarkan Musim
    st.write("### Distribusi Penyewaan Sepeda Berdasarkan Musim")
    fig, ax = plt.subplots(figsize=(14, 7))
    sns.boxplot(x='season', y='cnt', data=filtered_day_df, ax=ax)
    ax.set_title('Distribusi Penyewaan Sepeda Berdasarkan Musim')
    ax.set_xlabel('Musim')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
    st.pyplot(fig)
