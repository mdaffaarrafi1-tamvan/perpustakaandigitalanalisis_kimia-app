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
    "Asam Nitrat (HNO3)": "MSDS Nitric Acid.PDF",
    "Asam Sulfat (H2SO4)": "Asam sulfat.PDF",
    "Asam Asetat (H2SO4)": "asam asetat.PDF",
    "Asam Salisilat (H2SO4)": "MSDS Asam Salisilat - SAFC.PDF",
    "Asam Oksalat (H2SO4)": "MSDS ASAM OKSALAT.pdf",
    "Asam Flourida (H2SO4)": "MSDS Hydroflouric Acid.pdf",
    "Aseton (C3H6O)": "MSDS Aseton.PDF",
    "Benzena (C6H6)": "MSDS Benzena.PDF",
    "Boraks (Na2B4O7)": "MSDS Boraks.pdf",
    "Metanol (CH4O)": "methanol.pdf",
    "Etanol (C2H6O)": "MSDS Etanol.PDF",
    "Formaldehida (C2H4O)": "MSDS Formaldehida - Sigma Aldrich.pdf",
    "Kloroform (CHCl3)": "MSDS KLOROFORM.PDF",
    "NitroBenzen (C6H5NO2)": "MSDS NITROBENZENA.PDF",
    "Natrium Sianida (NaCN)": "MSDS SIANIDA.pdf",
    "Kalium Sianida (KCN)": "Potasium Sianida.pdf",
    "Natrium Hidroksida (NaOH)": "MSDS SODIUM HIDROKSIDA - SIGMA ALRICH.pdf",
    "Kalium Hidroksida (KOH)": "kalium hidroksida .PDF.pdf",
    "Kalsium Hidroksida (CaOH2)": "kalsium hidroksida .PDF.pdf",
    "Natrium Hidroksida (NaOH)": "MSDS SODIUM HIDROKSIDA - SIGMA ALRICH.pdf",
    "Amonia (NH3)": "Amonia.PDF",
    "Amonium Nitrat (NH4NO3)": "msds amonium nitrat.pdf",
    "Arsen (Ar)": "arsen.pdf",
    "Merkuri (Hg)": "merkuri.PDF",
    "Merkuri(II)sulfat (HgSO4)": "Mercury(II) sulfate.PDF",
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

     # Folder PDF
    Folder_pdf = "pdf_SNI"

    # Gabungkan path
    path_file = os.path.join(Folder_pdf, nama_file_pdf)

    st.info(f"📄 File dipilih: {nama_file_pdf}")

    # =========================
    # CEK FILE ADA / TIDAK
    # =========================
    if os.path.exists(path_file):

        # Baca PDF
        with open(path_file, "rb") as file_pdf:
            Konten_pdf = file_pdf.read()

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
        pdf_viewer(Konten_pdf)

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
