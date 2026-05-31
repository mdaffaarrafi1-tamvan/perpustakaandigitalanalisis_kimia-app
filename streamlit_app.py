import streamlit as st
import os
import base64
import streamlit.components.v1 as components
from streamlit_pdf_viewer import pdf_viewer

# =========================
# DATABASE FILE MSDS
# =========================
database_msds = {
    "Asam Klorida (HCl)": "Ikan.pdf.pdf",
    "Natrium Hidroksida (NaOH)": "NaOH.pdf",
    "Asam Sulfat (H2SO4)": "H2SO4.pdf",
}

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Library Analisis Kimia",
    page_icon="🧪",
    layout="wide"
)

# =========================
# SIDEBAR
# =========================
st.sidebar.title("📚 Navigasi")

menu = st.sidebar.radio(
    "Pilih Menu:",
    [
        "Home",
        "MSDS & Safety",
        "SNI & ISO",
        "Kalibrasi Alat",
        "Panduan Analisis",
        "K3L & Limbah"
    ]
)

# =========================
# HALAMAN HOME
# =========================
if menu == "Home":

    st.title("🧪 Perpustakaan Digital Analisis Kimia")
    st.subheader("Selamat Datang, Analis Laboratorium")

    st.write("""
    Aplikasi ini digunakan untuk:
    - Melihat dokumen MSDS
    - Download PDF bahan kimia
    - Panduan analisis laboratorium
    - Standar SNI & ISO
    - Informasi K3L laboratorium
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Database MSDS", f"{len(database_msds)} File")
    col2.metric("Metode Analisis", "24+")
    col3.metric("Dokumen SNI", "12+")

# =========================
# HALAMAN MSDS
# =========================
elif menu == "MSDS & Safety":

    st.header("🗃️ Database MSDS & Safety")

    pilihan_bahan = st.selectbox(
        "Pilih Bahan Kimia:",
        list(database_msds.keys())
    )

    nama_file_pdf = database_msds[pilihan_bahan]

    # Folder PDF
    folder_pdf = "pdf_msds"

    # Gabungkan path
    path_file = os.path.join(folder_pdf, nama_file_pdf)

    st.info(f"📄 File dipilih: {nama_file_pdf}")

    # =========================
    # CEK FILE ADA / TIDAK
    # =========================
    if os.path.exists(path_file):

        # Baca PDF
        with open(path_file, "rb") as file_pdf:
            konten_pdf = file_pdf.read()

        # =========================
        # TOMBOL DOWNLOAD
        # =========================
        st.download_button(
            label="📥 Download PDF",
            data=konten_pdf,
            file_name=nama_file_pdf,
            mime="application/pdf",
            use_container_width=True
        )

        st.success("✅ File PDF berhasil dimuat")

        # =========================
        # PREVIEW PDF
        # =========================
        st.subheader("📄 Preview PDF")       
        pdf_viewer(konten_pdf)
# =========================
# HALAMAN SNI
# =========================
elif menu == "SNI & ISO":

    st.header("📜 Standar SNI & ISO")

    st.write("""
    1. SNI 01-3553-2006 — Air Minum Dalam Kemasan  
    2. ISO 17025 — Sistem Manajemen Laboratorium  
    3. SNI Analisis Kimia Lingkungan  
    """)

# =========================
# HALAMAN KALIBRASI
# =========================
elif menu == "Kalibrasi Alat":

    st.header("⚖️ Kalibrasi Instrumen")

    st.write("""
    ### Langkah Kalibrasi:
    1. Pastikan alat bersih
    2. Cek waterpass
    3. Gunakan anak timbangan standar
    4. Catat hasil kalibrasi
    """)

# =========================
# HALAMAN PANDUAN ANALISIS
# =========================
elif menu == "Panduan Analisis":

    st.header("🔬 Metode Analisis")

    metode = st.radio(
        "Pilih Metode:",
        ["Gravimetri", "Titrimetri"],
        horizontal=True
    )

    if metode == "Gravimetri":

        st.code("""
Pengendapan
↓
Penyaringan
↓
Pencucian
↓
Pengeringan
↓
Penimbangan
        """)

    elif metode == "Titrimetri":

        st.code("""
Persiapan Sampel
↓
Penambahan Indikator
↓
Titrasi
↓
Perubahan Warna
↓
Perhitungan Konsentrasi
        """)

# =========================
# HALAMAN K3L
# =========================
elif menu == "K3L & Limbah":

    st.header("🛡️ K3L & Limbah Laboratorium")

    st.checkbox("☣️ Limbah Logam Berat")
    st.checkbox("🧪 Limbah Asam Basa")
    st.checkbox("🔥 Limbah Mudah Terbakar")

    st.warning("Gunakan APD lengkap saat bekerja di laboratorium.")
