import streamlit as st
import os
import base64

# =========================
# DATABASE MSDS
# =========================
database_msds = {
    "Asam Klorida (HCl)": "Ikan.pdf",
    "Natrium Hidroksida (NaOH)": "NaOH.pdf",
    "Asam Sulfat (H2SO4)": "H2SO4.pdf",
}

# =========================
# SETUP HALAMAN
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
    ["Home", "MSDS & Safety", "SNI & ISO", "Kalibrasi Alat", "Panduan Analisis", "K3L & Limbah"]
)

# =========================
# HOME
# =========================
if menu == "Home":
    st.title("🧪 Perpustakaan Digital Analisis Kimia")
    st.write("Sistem database MSDS, standar, dan metode analisis laboratorium.")

    col1, col2, col3 = st.columns(3)
    col1.metric("MSDS", f"{len(database_msds)} File")
    col2.metric("Standar SNI", "12 Dokumen")
    col3.metric("Metode Analisis", "24 Prosedur")

# =========================
# MSDS & SAFETY
# =========================
elif menu == "MSDS & Safety":
    st.header("🗃️ Database MSDS & Safety")

    # 🔥 RELATIVE PATH (WAJIB UNTUK STREAMLIT CLOUD)
    folder_path = os.path.join(os.path.dirname(__file__), "PDF_ANJING")

    # DEBUG (boleh dimatikan nanti)
    st.subheader("🔧 Debug Info")
    st.write("Folder Path:", folder_path)
    st.write("Folder Exists:", os.path.exists(folder_path))

    if os.path.exists(folder_path):
        st.write("Isi Folder:", os.listdir(folder_path))
    else:
        st.error("❌ Folder PDF_ANJING tidak ditemukan di project!")
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

    # =========================
    # TAMPILKAN PDF
    # =========================
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            pdf_data = f.read()

        # DOWNLOAD
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
        st.error("❌ File PDF tidak ditemukan. Pastikan file ada di folder PDF_ANJING.")

# =========================
# SNI & ISO
# =========================
elif menu == "SNI & ISO":
    st.header("📜 Standar SNI & ISO")
    st.write("Contoh standar: SNI air minum, ISO 17025, dll.")

# =========================
# KALIBRASI
# =========================
elif menu == "Kalibrasi Alat":
    st.header("⚖️ Kalibrasi Alat Laboratorium")
    st.write("Panduan dasar kalibrasi alat kimia.")

# =========================
# ANALISIS
# =========================
elif menu == "Panduan Analisis":
    st.header("🔬 Metode Analisis")

    metode = st.radio("Pilih Metode:", ["Gravimetri", "Titrimetri"])

    if metode == "Gravimetri":
        st.code("Pengendapan → Filtrasi → Pengeringan → Penimbangan")
    else:
        st.code("Pipet → Titrasi → Endpoint → Perhitungan")

# =========================
# K3L
# =========================
elif menu == "K3L & Limbah":
    st.header("🛡️ K3L & Limbah")
    st.checkbox("Limbah Logam Berat")
    st.checkbox("Limbah Organik")
    st.checkbox("APD Wajib Digunakan")
