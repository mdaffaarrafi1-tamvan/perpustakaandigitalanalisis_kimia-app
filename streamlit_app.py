import streamlit as st
import pandas as pd
from PyPDF2 import PdfReader

# ======================================================
# KONFIGURASI HALAMAN
# ======================================================
st.set_page_config(
    page_title="ChemLib Hybrid Digital",
    page_icon="🧪",
    layout="wide"
)

# ======================================================
# DATABASE INTERNAL
# ======================================================
data_panduan = {
    "Gravimetri": {
        "Judul": "Penentuan Kadar Sulfat sebagai BaSO4",
        "Prosedur": "1. Pengendapan\n2. Penyaringan\n3. Pemijaran",
        "Ref": "Modul Praktikum"
    }
}

# ======================================================
# SIDEBAR
# ======================================================
menu = st.sidebar.selectbox(
    "Pilih Menu",
    ["Dashboard", "Cari MSDS"]
)

# ======================================================
# DASHBOARD
# ======================================================
if menu == "Dashboard":

    st.title("🧪 ChemLib Digital")
    st.write("Perpustakaan Digital Laboratorium")

# ======================================================
# CARI MSDS
# ======================================================
elif menu == "Cari MSDS":

    st.header("📄 Upload PDF MSDS")

    uploaded_file = st.file_uploader(
        "Upload file PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        st.success(f"File berhasil diupload: {uploaded_file.name}")

        try:

            # membaca PDF
            pdf_reader = PdfReader(uploaded_file)

            jumlah_halaman = len(pdf_reader.pages)

            st.write(f"Jumlah halaman: {jumlah_halaman}")

            # ambil teks
            all_text = ""

            for page in pdf_reader.pages:

                text = page.extract_text()

                if text:
                    all_text += text

            # tampilkan teks
            st.text_area(
                "Isi PDF",
                all_text,
                height=400
            )

        except Exception as e:

            st.error(f"Terjadi error: {e}")
