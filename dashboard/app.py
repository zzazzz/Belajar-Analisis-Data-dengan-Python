import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load datasets
@st.cache_data
def load_data():
    day_df = pd.read_csv('data/day.csv')
    hour_df = pd.read_csv('data/hour.csv')
    return day_df, hour_df

day_df, hour_df = load_data()

# Sidebar navigation
st.sidebar.header("Navigasi")
menu = st.sidebar.radio("Pilih Pertanyaan", options=[
    "Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3", "Pertanyaan 4", "Pertanyaan 5"
])

# Filter data untuk rentang tahun 2011-2012
filtered_day_df = day_df
filtered_hour_df = hour_df

# Pertanyaan 1: Distribusi jumlah penyewaan sepeda per hari (daily) vs per jam (hourly)
if menu == "Pertanyaan 1":
    st.title("Distribusi Jumlah Penyewaan Sepeda per Hari dan per Jam")
    st.write("Bagaimana distribusi jumlah penyewaan sepeda per hari (daily) dibandingkan dengan penyewaan sepeda per jam (hourly)? Apakah ada pola yang menunjukkan perbedaan signifikan antara keduanya?")
    
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    sns.histplot(filtered_day_df['cnt'], bins=30, kde=True, ax=ax[0])
    ax[0].set_title('Distribusi Total Penyewaan Sepeda (Daily)')
    ax[0].set_xlabel('Jumlah Penyewaan')
    ax[0].set_ylabel('Frekuensi')

    sns.histplot(filtered_hour_df['cnt'], bins=30, kde=True, ax=ax[1])
    ax[1].set_title('Distribusi Total Penyewaan Sepeda (Hourly)')
    ax[1].set_xlabel('Jumlah Penyewaan')
    ax[1].set_ylabel('Frekuensi')
    st.pyplot(fig)

    # Insight dan Kesimpulan
    st.subheader("Insight")
    st.write("- Distribusi total penyewaan sepeda (Daily) terbanyak pada interval 4000 sampai 4100-an penyewaan sepeda dengan frekuensi sebesar 50.")
    st.write("- Distribusi total penyewaan sepeda (Hourly) terbanyak pada interval 0 sampai 30-an penyewaan sepeda dengan frekuensi sebesar 4000.")
    
    st.subheader("Conclusion")
    st.write("Distribusi jumlah penyewaan sepeda per hari menunjukkan bahwa sebagian besar jumlah penyewaan berkisar antara 4000 hingga 4100 penyewaan per hari dengan frekuensi tertinggi sekitar 50 kali. Sementara itu, pada penyewaan per jam, sebagian besar terjadi pada interval 0 hingga 30 penyewaan dengan frekuensi sekitar 4000 kali. Ini menunjukkan bahwa secara harian, jumlah penyewaan lebih konsisten pada kisaran tertentu, sedangkan pada tingkat per jam, ada lebih banyak fluktuasi dengan frekuensi penyewaan rendah yang lebih sering terjadi.")

# Pertanyaan 2: Penyewaan sepeda pada hari kerja vs hari libur
elif menu == "Pertanyaan 2":
    st.title("Penyewaan Sepeda pada Hari Kerja vs Hari Libur")
    st.write("Apakah ada perbedaan yang signifikan dalam jumlah penyewaan sepeda antara hari kerja dan hari libur? Kapan penyewaan sepeda cenderung lebih tinggi?")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x='workingday', y='cnt', data=filtered_day_df, ax=ax)
    ax.set_title('Penyewaan Sepeda pada Hari Kerja vs Hari Libur')
    ax.set_xlabel('Jenis Hari')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticklabels(['Hari Libur', 'Hari Kerja'])
    st.pyplot(fig)

    # Insight dan Kesimpulan
    st.subheader("Insight")
    st.write("- Penyewaan sepeda pada hari kerja vs hari libur paling banyak terjadi pada hari libur dan paling sedikit pada hari kerja sesuai dengan box-plot yang disajikan.")
    
    st.subheader("Conclusion")
    st.write("Penyewaan sepeda cenderung lebih tinggi pada hari libur dibandingkan hari kerja, seperti yang terlihat pada box-plot. Hal ini mungkin disebabkan oleh waktu luang yang lebih banyak pada hari libur, memungkinkan orang untuk lebih sering menyewa sepeda. Penyewaan sepeda lebih sedikit terjadi pada hari kerja, kemungkinan karena keterbatasan waktu yang disebabkan oleh kegiatan rutin seperti bekerja atau bersekolah.")

# Pertanyaan 3: Distribusi penyewaan sepeda antara pengguna kasual dan terdaftar
elif menu == "Pertanyaan 3":
    st.title("Distribusi Penyewaan Sepeda Berdasarkan Jenis Pengguna")
    st.write("Bagaimana distribusi penyewaan sepeda antara pengguna kasual dan terdaftar? Apakah pengguna terdaftar lebih banyak menyewa sepeda dibandingkan pengguna kasual?")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(filtered_hour_df['casual'], bins=30, kde=True, color="blue", label="Casual Users", ax=ax)
    sns.histplot(filtered_hour_df['registered'], bins=30, kde=True, color="orange", label="Registered Users", ax=ax)
    ax.set_title('Distribusi Penyewaan Sepeda (Casual vs Registered)')
    ax.set_xlabel('Jumlah Penyewaan')
    ax.set_ylabel('Frekuensi')
    ax.legend()
    st.pyplot(fig)

    # Insight dan Kesimpulan
    st.subheader("Insight")
    st.write("- Distribusi penyewaan sepeda (Casual vs Registered) terjadi pada bins pertama dengan frekuensi registered users sebanyak 4000 dan casual users kurang dari 8000.")
    
    st.subheader("Conclusion")
    st.write("Distribusi penyewaan sepeda menunjukkan bahwa pengguna terdaftar (registered) menyewa sepeda dalam jumlah yang signifikan, meskipun jumlah penyewaan terbanyak tetap pada pengguna kasual (casual) di interval pertama. Ini mungkin mengindikasikan bahwa pengguna terdaftar menyewa sepeda secara lebih konsisten, sedangkan pengguna kasual cenderung menyewa dalam jumlah yang lebih bervariasi.")

# Pertanyaan 4: Tren penyewaan sepeda bulanan antara tahun 2011 dan 2012
elif menu == "Pertanyaan 4":
    st.title("Tren Penyewaan Sepeda Bulanan")
    st.write("Apakah ada perbedaan dalam tren penyewaan sepeda bulanan antara tahun 2011 dan 2012? Bulan mana yang menunjukkan penyewaan terbanyak dan apakah ada pola musiman?")
    
    fig, ax = plt.subplots(figsize=(14, 7))
    sns.lineplot(x='mnth', y='cnt', hue='yr', data=filtered_day_df, marker="o", ax=ax)
    ax.set_title('Tren Penyewaan Sepeda Bulanan 2011-2012')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.legend(title='Tahun', labels=['2011', '2012'])
    st.pyplot(fig)

    # Insight dan Kesimpulan
    st.subheader("Insight")
    st.write("- Tren penyewaan sepeda bulanan (2011 vs 2012) paling banyak terjadi pada tahun 2012 dengan frekuensi tertinggi pada bulan ke-9.")
    
    st.subheader("Conclusion")
    st.write("Tren penyewaan sepeda bulanan menunjukkan perbedaan signifikan antara tahun 2011 dan 2012, dengan jumlah penyewaan tertinggi terjadi pada bulan ke-9 di tahun 2012. Hal ini menunjukkan adanya peningkatan jumlah penyewaan sepeda di tahun 2012 dibandingkan tahun sebelumnya, kemungkinan terkait dengan perubahan musim atau cuaca, atau peningkatan popularitas sepeda sebagai moda transportasi.")

# Pertanyaan 5: Penyewaan sepeda tertinggi dalam seminggu
elif menu == "Pertanyaan 5":
    st.title("Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu")
    st.write("Hari apa yang menunjukkan jumlah penyewaan sepeda tertinggi dalam seminggu? Bagaimana pola penyewaan sepeda berdasarkan hari dalam seminggu?")
    
    fig, ax = plt.subplots(figsize=(14, 7))
    sns.lineplot(x='weekday', y='cnt', data=filtered_day_df, marker="o", color='orange', ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda Berdasarkan Hari dalam Seminggu')
    ax.set_xlabel('Hari dalam Minggu')
    ax.set_ylabel('Jumlah Penyewaan')
    ax.set_xticks(range(0, 7))
    ax.set_xticklabels(['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])
    st.pyplot(fig)

    # Insight dan Kesimpulan
    st.subheader("Insight")
    st.write("- Rata-rata penyewaan sepeda berdasarkan hari dalam seminggu terbanyak terjadi pada hari Jumat.")
    
    st.subheader("Conclusion")
    st.write("Berdasarkan hari dalam seminggu, penyewaan sepeda terbanyak terjadi pada hari Jumat. Pola ini mungkin disebabkan oleh banyaknya kegiatan sosial dan rekreasi yang dilakukan pada hari tersebut, terutama menjelang akhir pekan, sehingga mendorong lebih banyak orang untuk menyewa sepeda.")
