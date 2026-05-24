import streamlit as st
import pandas as pd

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="ChemLib Hybrid Digital",
    page_icon="🧪",
    layout="wide"
)

# --- DATABASE INTERNAL ---
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

# --- SIDEBAR ---
st.sidebar.title("📚 Navigasi")
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Dashboard",
        "Cari MSDS",
        "Panduan Praktikum",
        "K3L & Kalibrasi"
    ]
)

# =========================================================
# DASHBOARD
# =========================================================
if menu == "Dashboard":

    st.title("🧪 ChemLib Digital")
    st.write("Sistem informasi laboratorium kimia berbasis hybrid.")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📘 Data Internal Laboratorium")

    with col2:
        st.success("🌐 Integrasi Database Global")

# =========================================================
# CARI MSDS
# =========================================================
elif menu == "Cari MSDS":

    st.header("🌐 Pencarian MSDS")

    nama_bahan = st.text_input(
        "Masukkan nama bahan kimia:",
        placeholder="Contoh: Crystal Violet"
    )

    if nama_bahan:

        st.subheader(f"Hasil pencarian: {nama_bahan}")

        # link otomatis ke PubChem
        url_pubchem = f"https://pubchem.ncbi.nlm.nih.gov/#query={nama_bahan.replace(' ', '%20')}"

        st.markdown(f"""
        [🔗 Buka Data PubChem]({url_pubchem})
        """)

    st.divider()

    # =====================================================
    # UPLOAD PDF SDS
    # =====================================================
    st.subheader("📄 Upload File SDS / MSDS")

    uploaded_file = st.file_uploader(
        "Upload file PDF SDS",
        type="pdf"
    )

    if uploaded_file is not None:

        st.success(f"File berhasil diupload: {uploaded_file.name}")

        # membaca PDF
        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        jumlah_halaman = len(pdf_reader.pages)

        st.write(f"Jumlah halaman PDF: {jumlah_halaman}")

        # mengambil teks seluruh halaman
        all_text = ""

        for page in pdf_reader.pages:
            all_text += page.extract_text()

        # tampilkan isi PDF
        st.subheader("📖 Isi Dokumen SDS")

        st.text_area(
            "Hasil ekstraksi teks:",
            all_text,
            height=400
        )

        # =================================================
        # PENCARIAN BAHAYA OTOMATIS
        # =================================================
        st.subheader("⚠️ Identifikasi Bahaya")

        keyword_bahaya = [
            "berbahaya",
            "karsinogen",
            "iritasi",
            "toksik",
            "flammable",
            "cancer"
        ]

        hasil_bahaya = []

        for kata in keyword_bahaya:
            if kata.lower() in all_text.lower():
                hasil_bahaya.append(kata)

        if hasil_bahaya:
            st.error(f"Bahan memiliki indikasi bahaya: {', '.join(hasil_bahaya)}")
        else:
            st.success("Tidak ditemukan kata kunci bahaya.")

# =========================================================
# PANDUAN PRAKTIKUM
# =========================================================
elif menu == "Panduan Praktikum":

    st.header("📘 Panduan Praktikum")

    pilihan = st.selectbox(
        "Pilih metode:",
        list(data_panduan.keys())
    )

    konten = data_panduan[pilihan]

    st.subheader(konten["Judul"])

    st.text_area(
        "Prosedur",
        konten["Prosedur"],
        height=200
    )

    st.markdown(f"**Referensi:** {konten['Ref']}")

# =========================================================
# K3L
# =========================================================
elif menu == "K3L & Kalibrasi":

    st.header("🛡️ K3L dan Kalibrasi")

    with st.expander("Jadwal Kalibrasi"):

        df = pd.DataFrame({
            "Alat": ["Neraca 01", "Neraca 02", "pH Meter"],
            "Status": ["Terkalibrasi", "Perlu Kalibrasi", "Terkalibrasi"],
            "Tanggal": ["2024-05-01", "2024-06-15", "2024-04-20"]
        })

        st.table(df)

    with st.expander("Limbah B3"):
        st.warning(
            "Pastikan limbah asam dinetralkan sebelum dibuang."
        )
