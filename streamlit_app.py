import streamlit as st
import os
import base64

# --- DATABASE MSDS ---
database_msds = {
    "Asam Klorida (HCl)": "Ikan.pdf",
    "Natrium Hidroksida (NaOH)": "NaOH.pdf",
    "Asam Sulfat (H2SO4)": "H2SO4.pdf",
}

# --- SETTING HALAMAN ---
st.set_page_config(page_title="Library Analisis Kimia", page_icon="🧪", layout="wide")

# --- SIDEBAR ---
st.sidebar.title("📚 Navigasi")
menu = st.sidebar.radio(
    "Pilih Menu:",
    ["Home", "MSDS & Safety", "SNI & ISO", "Kalibrasi Alat", "Panduan Analisis", "K3L & Limbah"]
)

# --- HOME ---
if menu == "Home":
    st.title("🧪 Perpustakaan Digital Analisis Kimia")
    st.write("Selamat datang di sistem database laboratorium.")

    col1, col2, col3 = st.columns(3)
    col1.metric("MSDS", "3 File")
    col2.metric("SNI", "12 Dokumen")
    col3.metric("Metode", "24 Prosedur")

# --- MSDS ---
elif menu == "MSDS & Safety":
    st.header("🗃️ Database MSDS & Safety")

    # 🔥 PATH FIX SESUAI LAPTOP KAMU
    folder_path = r"C:\Users\ASUS\OneDrive\Desktop\PDF_ANJING"

    st.subheader("🔧 Debug Info (hapus nanti kalau sudah normal)")
    st.write("Folder Path:", folder_path)
    st.write("Folder Exists:", os.path.exists(folder_path))

    if os.path.exists(folder_path):
        st.write("Isi Folder:", os.listdir(folder_path))
    else:
        st.error("Folder PDF_ANJING tidak ditemukan!")
        st.stop()

    # PILIH BAHAN
    pilihan = st.selectbox(
        "Pilih Bahan Kimia:",
        list(database_msds.keys())
    )

    nama_file = database_msds[pilihan]
    file_path = os.path.join(folder_path, nama_file)

    st.info(f"File dipilih: {nama_file}")
    st.write("Full Path:", file_path)
    st.write("File Exists:", os.path.exists(file_path))

    # CEK FILE
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            pdf_data = f.read()

        # DOWNLOAD BUTTON
        st.download_button(
            label="📥 Download MSDS",
            data=pdf_data,
            file_name=nama_file,
            mime="application/pdf"
        )

        # PREVIEW PDF
        base64_pdf = base64.b64encode(pdf_data).decode("utf-8")

        pdf_display = f"""
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" 
            height="700">
        </iframe>
        """

        st.components.v1.html(pdf_display, height=750)

    else:
        st.error("❌ File PDF tidak ditemukan. Cek nama file di folder PDF_ANJING.")

# --- SNI & ISO ---
elif menu == "SNI & ISO":
    st.header("📜 Standar SNI & ISO")
    st.write("Contoh: SNI Air Minum, ISO 17025, dll.")

# --- KALIBRASI ---
elif menu == "Kalibrasi Alat":
    st.header("⚖️ Kalibrasi Alat Laboratorium")
    st.write("Panduan kalibrasi dasar alat kimia.")

# --- ANALISIS ---
elif menu == "Panduan Analisis":
    st.header("🔬 Metode Analisis")

    metode = st.radio("Pilih Metode:", ["Gravimetri", "Titrimetri"])

    if metode == "Gravimetri":
        st.code("Pengendapan → Filtrasi → Pengeringan → Penimbangan")
    else:
        st.code("Pipet → Titrasi → Endpoint → Perhitungan")

# --- K3L ---
elif menu == "K3L & Limbah":
    st.header("🛡️ K3L & Limbah")
    st.checkbox("Limbah Logam Berat")
    st.checkbox("Limbah Organik")
    st.checkbox("APD Wajib Digunakan")
