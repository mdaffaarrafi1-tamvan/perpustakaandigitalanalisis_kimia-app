import streamlit as st
import os
import base64  # Diperlukan untuk mengubah PDF menjadi format yang bisa dibaca browser

# --- DATABASE LINK & NAMA FILE MSDS ---
# Menghubungkan nama bahan dengan nama file PDF yang ada di folder 'pdf_msds'
database_msds = {
    "Asam Klorida (HCl)": "Ikan.pdf.pdf",
    "Asam Nitrat (HNO3)": "MSDS Nitric Acid.PDF",
    "Asam Sulfat (H2SO4)": "H2SO4.pdf",
}

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Library Analisis Kimia", page_icon="🧪", layout="wide")

# --- SIDEBAR NAVIGASI ---
st.sidebar.title("📚 Navigasi")
menu = st.sidebar.radio(
    "Pilih Kategori:",
    ["Home", "MSDS & Safety", "SNI & ISO", "Kalibrasi Alat", "Panduan Analisis (Gravi/Titri)", "K3L & Limbah"]
)

# --- HALAMAN HOME ---
if menu == "Home":
    st.title("🧪 Perpustakaan Digital Analisis Kimia")
    st.subheader("Selamat Datang, Analis!")
    st.write("Silakan pilih kategori di samping untuk memulai pencarian data.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Database MSDS", f"{len(database_msds)}+ Bahan")
    col2.metric("Standar SNI", "12 Dokumen")
    col3.metric("Metode Uji", "24 Prosedur")

# --- HALAMAN MSDS (TAMPILKAN & DOWNLOAD PDF) ---
elif menu == "MSDS & Safety":
    st.header("🗃️ Database MSDS & Simbol Bahaya")
    st.write("Silakan pilih bahan untuk melihat pratinjau dan mengunduh dokumen PDF MSDS.")
    
    pilihan_bahan = st.selectbox("Pilih atau Cari Bahan Kimia:", list(database_msds.keys()))
    nama_file_pdf = database_msds[pilihan_bahan]
    
    # Jalur menuju file PDF di dalam folder 'pdf_msds'
    path_file = os.path.join("pdf_msds", nama_file_pdf)
    
    st.info(f"Anda memilih: **{pilihan_bahan}**")
    
    # Cek apakah file PDF-nya beneran ada di dalam folder
    if os.path.exists(path_file):
        # 1. LOGIKA TOMBOL DOWNLOAD
        with open(path_file, "rb") as file_pdf:
            konten_pdf = file_pdf.read()
            
            st.download_button(
                label=f"📥 Download File PDF {nama_file_pdf}",
                data=konten_pdf,
                file_name=nama_file_pdf,
                mime="application/pdf",
                use_container_width=True
            )
        
        # 2. LOGIKA MENAMPILKAN PREVIEW PDF DI LAYAR
        st.subheader(f"📄 Pratinjau Dokumen: {nama_file_pdf}")
        
        # Mengubah PDF ke format base64 agar bisa ditempel di komponen bawaan web
        base64_pdf = base64.b64encode(konten_pdf).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
        
        # Menampilkan iframe PDF ke dalam Streamlit secara aman
        st.markdown(pdf_display, unsafe_allow_html=True)
        
    else:
        st.error(f"⚠️ File '{nama_file_pdf}' belum dimasukkan ke dalam folder 'pdf_msds'. Silakan salin file PDF Anda ke folder tersebut terlebih dahulu.")

# --- HALAMAN LAINNYA (TETAP AMAN) ---
elif menu == "SNI & ISO":
    st.header("📜 Standar SNI & ISO 17025")
    st.write("1. **SNI 01-3553-2006:** Air minum dalam kemasan.")

elif menu == "Kalibrasi Alat":
    st.header("⚖️ Panduan Kalibrasi Instrumen")
    st.write("1. Pastikan waterpass berada di tengah.")

elif menu == "Panduan Analisis (Gravi/Titri)":
    st.header("🔬 Metode Analisis Konvensional")
    metode = st.radio("Pilih Metode:", ["Gravimetri", "Titrimetri"], horizontal=True)
    if metode == "Gravimetri":
        st.code("Pengendapan -> Penyaringan -> Pencucian -> Pengeringan -> Penimbangan")

elif menu == "K3L & Limbah":
    st.header("🛡️ Manajemen K3L & Limbah")
    st.checkbox("Limbah Logam Berat (Wadah Biru)")
