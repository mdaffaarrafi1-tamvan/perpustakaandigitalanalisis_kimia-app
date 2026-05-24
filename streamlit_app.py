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

# --- SIDEBAR ---
st.sidebar.title("📚 Navigasi")
menu = st.sidebar.radio(
    "Pilih Kategori:",
    ["Home", "MSDS & Safety", "SNI & ISO", "Kalibrasi Alat", "Panduan Analisis (Gravi/Titri)", "K3L & Limbah"]
)

# --- HOME ---
if menu == "Home":
    st.title("🧪 Perpustakaan Digital Analisis Kimia")

# --- MSDS ---
elif menu == "MSDS & Safety":
    st.header("🗃️ Database MSDS & Simbol Bahaya")

    pilihan_bahan = st.selectbox(
        "Pilih Bahan Kimia:",
        list(database_msds.keys())
    )

    nama_file_pdf = database_msds[pilihan_bahan]

    # 🔥 PATH SUDAH DIUBAH KE PDF_ANJING
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    path_file = os.path.join(BASE_DIR, "PDF_ANJING", nama_file_pdf)

    st.info(f"Anda memilih: **{pilihan_bahan}**")

    # DEBUG (boleh dihapus nanti)
    st.write("Path file:", path_file)
    st.write("File ada?", os.path.exists(path_file))

    if os.path.exists(path_file):
        with open(path_file, "rb") as file_pdf:
            konten_pdf = file_pdf.read()

        st.download_button(
            label=f"📥 Download {nama_file_pdf}",
            data=konten_pdf,
            file_name=nama_file_pdf,
            mime="application/pdf"
        )

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
        st.error("File tidak ditemukan! Cek folder 'PDF_ANJING' dan nama file.")
