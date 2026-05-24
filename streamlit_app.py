import streamlit as st
import pandas as pd

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="ChemLib Hybrid Digital", page_icon="🧪", layout="wide")

# --- DATA MANUAL (DATABASE INTERNAL) ---
# Ini adalah bagian di mana Anda memasukkan data jurnal/panduan secara manual
data_panduan = {
    "Gravimetri": {
        "Judul": "Penentuan Kadar Sulfat sebagai BaSO4",
        "Prosedur": "1. Pengendapan dengan BaCl2\n2. Digesti\n3. Penyaringan\n4. Pemijaran",
        "Ref": "Modul Praktikum Kimia Analitik"
    },
    "Titrimetri": {
        "Judul": "Standarisasi NaOH dengan Asam Oksalat",
        "Prosedur": "1. Pembuatan larutan baku primer\n2. Titrasi menggunakan indikator PP",
        "Ref": "SNI 06-6989.11-2004"
    }
}

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("📚 Navigasi Perpustakaan")
menu = st.sidebar.selectbox(
    "Pilih Layanan:",
    ["Dashboard", "Cari MSDS (Otomatis)", "Panduan Praktikum (Manual)", "K3L & Kalibrasi"]
)

# --- HALAMAN 1: DASHBOARD ---
if menu == "Dashboard":
    st.title("🧪 ChemLib: Perpustakaan Digital Analisis Kimia")
    st.write("Selamat datang di sistem manajemen data laboratorium berbasis Hybrid.")
    
    # Statistik Sederhana
    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **Metode Manual:** Digunakan untuk prosedur internal yang spesifik.")
    with col2:
        st.success("🌐 **Metode Otomatis:** Terhubung ke database global untuk data bahan kimia.")

# --- HALAMAN 2: CARI MSDS (OTOMATIS VIA LINK) ---
elif menu == "Cari MSDS (Otomatis)":
    st.header("🌐 Pencarian MSDS Global")
    st.write("Masukkan nama bahan untuk mencari data keamanan secara langsung di PubChem.")
    
    nama_bahan = st.text_input("Ketik Nama Bahan Kimia (Inggris):", placeholder="Contoh: Sulfuric Acid")
    
    if nama_bahan:
        # Teknik Hybrid: Membuat link pencarian otomatis berdasarkan input user
        st.subheader(f"Hasil Pencarian untuk: {nama_bahan}")
        url_pubchem = f"https://pubchem.ncbi.nlm.nih.gov/#query={nama_bahan.replace(' ', '%20')}"
        
        st.write(f"Sistem telah menyiapkan data untuk **{nama_bahan}**.")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Placeholder jika ingin ada video tutorial
        
        st.markdown(f"""
            <a href="{url_pubchem}" target="_blank">
                <button style="padding:10px; border-radius:5px; background-color:#F04444; color:white; border:none; cursor:pointer;">
                    Klik di Sini untuk Buka MSDS Resmi {nama_bahan}
                </button>
            </a>
        """, unsafe_allow_html=True)
        st.caption("Link di atas akan membawa Anda ke database eksternal PubChem secara otomatis.")

# --- HALAMAN 3: PANDUAN (MANUAL) ---
elif menu == "Panduan Praktikum (Manual)":
    st.header("📖 Panduan Analisis Internal")
    pilihan = st.selectbox("Pilih Metode:", list(data_panduan.keys()))
    
    konten = data_panduan[pilihan]
    st.subheader(konten["Judul"])
    st.text_area("Langkah Kerja:", konten["Prosedur"], height=150)
    st.markdown(f"**Referensi:** *{konten['Ref']}*")
    
    # Fitur Upload Jurnal (Otomatis Tersimpan di Web Selama Sesi Berjalan)
    st.divider()
    st.subheader("📤 Upload Jurnal/SNI Baru")
    uploaded_file = st.file_uploader("Tambahkan file PDF jurnal ke perpustakaan", type="pdf")
    if uploaded_file is not None:
        st.success(f"File '{uploaded_file.name}' berhasil diunggah ke database sementara.")

# --- HALAMAN 4: K3L & KALIBRASI ---
elif menu == "K3L & Kalibrasi":
    st.header("🛡️ Keselamatan Kerja & Perawatan Alat")
    
    with st.expander("Lihat Jadwal Kalibrasi Neraca"):
        df_kalibrasi = pd.DataFrame({
            "Alat": ["Neraca 01", "Neraca 02", "pH Meter"],
            "Status": ["Terkalibrasi", "Perlu Kalibrasi", "Terkalibrasi"],
            "Tanggal": ["2024-05-01", "2024-06-15", "2024-04-20"]
        })
        st.table(df_kalibrasi)
        
    with st.expander("Prosedur Limbah B3"):
        st.warning("Pastikan limbah cair asam dinetralkan sebelum masuk ke penampungan.")
