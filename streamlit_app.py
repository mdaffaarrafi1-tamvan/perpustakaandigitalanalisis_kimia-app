import streamlit as st
import pandas as pd
from streamlit_pdf_viewer import pdf_viewer

# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="ChemLib Hybrid Digital",
    page_icon="🧪",
    layout="wide"
)

# =========================================================
# DATABASE INTERNAL
# =========================================================
data_panduan = {

    "Gravimetri": {

        "Judul": "Penentuan Kadar Sulfat sebagai BaSO4",

        "Prosedur":
        "1. Pengendapan dengan BaCl2\n"
        "2. Digesti\n"
        "3. Penyaringan\n"
        "4. Pemijaran",

        "Ref": "Modul Praktikum Kimia Analitik"
    },

    "Titrimetri": {

        "Judul": "Standarisasi NaOH dengan Asam Oksalat",

        "Prosedur":
        "1. Pembuatan larutan baku primer\n"
        "2. Titrasi menggunakan indikator PP",

        "Ref": "SNI 06-6989.11-2004"
    }
}

# =========================================================
# DATABASE MSDS
# =========================================================
daftar_msds = {

    "Crystal Violet":
    "msds/crystal_violet.pdf"

    # Tambahkan file lain di sini
    # "Asam Sulfat": "msds/asam_sulfat.pdf"
}

# =========================================================
# SIDEBAR
# =========================================================
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

    st.write(
        "Sistem informasi perpustakaan digital laboratorium kimia berbasis hybrid."
    )

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "📘 Menyediakan panduan praktikum internal laboratorium."
        )

    with col2:

        st.success(
            "📄 Menyediakan database MSDS yang dapat dilihat dan diunduh."
        )

# =========================================================
# CARI MSDS
# =========================================================
elif menu == "Cari MSDS":

    st.header("📄 Database MSDS Laboratorium")

    st.write(
        "Pilih bahan kimia untuk melihat dokumen MSDS."
    )

    # =====================================================
    # PILIH BAHAN
    # =====================================================
    pilihan = st.selectbox(

        "Pilih bahan kimia:",

        list(daftar_msds.keys())
    )

    # path file
    file_path = daftar_msds[pilihan]

    # =====================================================
    # BUKA FILE PDF
    # =====================================================
    with open(file_path, "rb") as pdf_file:

        PDFbyte = pdf_file.read()

        st.subheader(f"📘 MSDS {pilihan}")

        # tombol download
        st.download_button(

            label="⬇️ Download MSDS",

            data=PDFbyte,

            file_name=f"{pilihan}.pdf",

            mime="application/pdf"
        )

        st.divider()

        # tampilkan PDF
        pdf_viewer(PDFbyte)

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

    st.markdown(
        f"**Referensi:** {konten['Ref']}"
    )

# =========================================================
# K3L & KALIBRASI
# =========================================================
elif menu == "K3L & Kalibrasi":

    st.header("🛡️ K3L dan Kalibrasi")

    with st.expander("Jadwal Kalibrasi"):

        df = pd.DataFrame({

            "Alat": [
                "Neraca 01",
                "Neraca 02",
                "pH Meter"
            ],

            "Status": [
                "Terkalibrasi",
                "Perlu Kalibrasi",
                "Terkalibrasi"
            ],

            "Tanggal": [
                "2024-05-01",
                "2024-06-15",
                "2024-04-20"
            ]
        })

        st.table(df)

    with st.expander("Prosedur Limbah B3"):

        st.warning(
            "Pastikan limbah cair asam dinetralkan sebelum dibuang."
        )
