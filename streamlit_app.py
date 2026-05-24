import streamlit as st
import os
import base64

# --- DATABASE MSDS ---
database_msds = {
    "Asam Klorida (HCl)": "Ikan.pdf",
    "Natrium Hidroksida (NaOH)": "NaOH.pdf",
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

# --- HOME ---
if menu == "Home":
    st.title("🧪 Perpustakaan Digital Analisis Kimia")
    st.subheader("Selamat Datang, Analis!")
    st.write("Silakan pilih kategori di samping untuk memulai.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Database MSDS", f"{len(database_msds)} Bahan")
    col2.metric("Standar SNI", "12 Dokumen")
    col3.metric("Metode Uji", "24 Prosedur")

# --- MSDS & SAFETY ---
elif menu == "MSDS & Safety":
    st.header("🗃️ Database MSDS & Simbol Bahaya")

    # 🔍 DEBUG SYSTEM (WAJIB UNTUK CEK ERROR)
    st.subheader("🔧 DEBUG INFO")

    st.write("Working Directory:", os.getcwd())
    st.write("File Script:", os.path.dirname(os.path.abspath(__file__)))

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    folder_path = os.path.join(BASE_DIR, "PDF_ANJING")

    st.write("Folder Path:", folder_path)
    st.write("Folder Exists:", os.path.exists(folder_path))

    if os.path.exists(folder_path):
        st.write("Isi Folder:", os.listdir(folder_path))
    else:
        st.error("Folder PDF_ANJING tidak ditemukan!")

    # --- PILIH BAHAN ---
    pilihan_bahan = st.selectbox(
        "Pilih atau Cari Bahan Kimia:",
        list(database_msds.keys())
    )

    nama_file_pdf = database_msds[pilihan_bahan]

    # --- PATH FILE PDF ---
    path_file = os.path.join(folder_path, nama_file_pdf)

    st.info(f"Anda memilih: **{pilihan_bahan}**")
    st.write("Path file PDF:", path_file)
    st.write("File Exists:", os.path.exists(path_file))

    # --- CEK FILE ---
    if os.path.exists(path_file):
        with open(path_file, "rb") as file_pdf:
            konten_pdf = file_pdf.read()

        # DOWNLOAD BUTTON
        st.download_button(
            label=f"📥 Download {nama_file_pdf}",
            data=konten_pdf,
            file_name=nama_file_pdf,
            mime="application/pdf"
        )

        # PREVIEW PDF
        base64_pdf = base64.b64encode(konten_pdf).decode("utf-8")

        pdf_display = f"""
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" 
            height="650">
        </iframe>
        """

        st.components.v1.html(pdf_display, height=700)

    else:
        st.error("❌ File PDF tidak ditemukan! Cek nama file & folder.")

# --- SNI & ISO ---
elif menu == "SNI & ISO":
    st.header("📜 Standar SNI & ISO 17025")
    st.write("1. SNI 01-3553-2006: Air minum dalam kemasan.")

# --- KALIBRASI ---
elif menu == "Kalibrasi Alat":
    st.header("⚖️ Panduan Kalibrasi Instrumen")
    st.write("Pastikan alat dalam kondisi siap pakai.")

# --- GRAVI / TITRI ---
elif menu == "Panduan Analisis (Gravi/Titri)":
    st.header("🔬 Metode Analisis Konvensional")

    metode = st.radio("Pilih Metode:", ["Gravimetri", "Titrimetri"], horizontal=True)

    if metode == "Gravimetri":
        st.code("Pengendapan → Penyaringan → Pengeringan → Penimbangan")
    else:
        st.code("Pipet → Titrasi → Endpoint → Perhitungan")

# --- K3L ---
elif menu == "K3L & Limbah":
    st.header("🛡️ Manajemen K3L & Limbah")
    st.checkbox("Limbah Logam Berat (Wadah Biru)")
    st.checkbox("Limbah Organik (Wadah Hijau)")
