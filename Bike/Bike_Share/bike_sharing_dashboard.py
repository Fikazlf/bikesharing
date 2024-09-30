import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Fungsi untuk memplot jumlah pengguna sepeda berdasarkan kondisi cuaca
def plot_bike_rentals_by_weather():
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weathersit', y='cnt', data=day_df)
    plt.title('Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Pengguna Sepeda')
    st.pyplot(plt)

# Fungsi untuk memplot jumlah total sepeda yang disewakan berdasarkan bulan dan tahun
def plot_monthly_trends():
    monthly_counts = day_df.groupby(by=["mnth", "yr"]).agg({"cnt": "sum"}).reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=monthly_counts, x="mnth", y="cnt", hue="yr", palette="rocket", marker="o")
    plt.title("Jumlah total sepeda yang disewakan berdasarkan Bulan dan tahun")
    plt.xlabel(None)
    plt.ylabel(None)
    plt.legend(title="Tahun", loc="upper right")
    st.pyplot(plt)

# Fungsi untuk memplot perbandingan penyewaan antara pengguna terdaftar dan tidak terdaftar
def plot_user_type_comparison():
    total_registered = day_df['registered'].sum()
    total_casual = day_df['casual'].sum()
    
    labels = ['Pengguna Terdaftar', 'Pengguna Tidak Terdaftar']
    values = [total_registered, total_casual]

    plt.bar(labels, values, color=['blue', 'orange'])
    plt.title('Perbandingan Penyewaan Sepeda')
    plt.ylabel('Jumlah Penyewaan')
    st.pyplot(plt)

# Membaca data dari path relatif
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Memproses data
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['yr'] = day_df['yr'].astype('category')
day_df['mnth'] = day_df['mnth'].map({
    1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
    7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
}).astype('category')
day_df['weathersit'] = day_df['weathersit'].map({
    1: 'Clear', 2: 'Mist', 3: 'Light Snow', 4: 'Heavy Rain'
}).astype('category')

# Memulai dashboard
st.title("Bike Sharing Dashboard")

# Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca
st.header("1. Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca")
st.write(
    "Grafik ini menunjukkan jumlah pengguna sepeda yang menyewa berdasarkan kondisi cuaca. "
    "Kondisi cuaca dibagi menjadi empat kategori: Clear, Mist, Light Snow, dan Heavy Rain. "
    "Ini membantu kita memahami bagaimana cuaca mempengaruhi penggunaan sepeda."
)
plot_bike_rentals_by_weather()

# Jumlah total sepeda yang disewakan berdasarkan Bulan dan Tahun
st.header("2. Jumlah total sepeda yang disewakan berdasarkan Bulan dan tahun")
st.write(
    "Grafik ini menunjukkan jumlah total sepeda yang disewakan berdasarkan bulan dan tahun. "
    "Ini memberikan wawasan tentang tren sewa sepeda selama beberapa tahun terakhir dan "
    "bagaimana penggunaan sepeda bervariasi di setiap bulan."
)
plot_monthly_trends()

# Perbandingan Penyewaan antara Pengguna Terdaftar dan Tidak Terdaftar
st.header("3. Perbandingan Penyewaan antara Pengguna Terdaftar dan Tidak Terdaftar")
st.write(
    "Grafik ini menunjukkan perbandingan jumlah penyewaan sepeda antara pengguna terdaftar dan tidak terdaftar. "
    "Data ini penting untuk memahami perilaku pengguna dan bisa membantu dalam strategi pemasaran serta pengembangan layanan."
)
plot_user_type_comparison()
