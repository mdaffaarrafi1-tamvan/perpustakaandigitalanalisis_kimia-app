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
    "Asam Asetat (CH3COOH)": "asam asetat.PDF",
    "Asam Salisilat (C2H6O3)": "MSDS Asam Salisilat - SAFC.PDF",
    "Asam Oksalat (H2C2O4)": "MSDS ASAM OKSALAT.pdf",
    "Asam Flourida (HF)": "MSDS Hydroflouric Acid.pdf",
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
    "Barium Sulfat (BaSO4)": "BaSO4.PDF",
    "Kalium Permanganat (KMnO4)": "KMnO4.PDF",
    "Barium Kloridia Dihidrat (BaCl2 · 2H2O)": "BaCl2 · 2H2O.PDF",
    "Natrium Sulfat (NaSO4)": "NaSO4.PDF",
    "Besi(III) (FeOH3)": "FeOH3.PDF",
    "Kalium Kromat (K2CrO4)": "K2CrO4.PDF",
    "Kalium Dikromat (K2Cr2O7)": "K2Cr2O7.PDF",
    "Natrium Karbonat (Na2CO3)": "Na2CO3.PDF",
    "Natrium Bikarbonat (NaHCO3)": "NaHCO3.PDF",
    "Natrium Tiosulfat (Na2S2O3)": "Na2S2O3.PDF",
    "Kalsium Sulfat Dihidrat (CaSO4 · 2H2O)": "CaSO4 · 2H2O.PDF",
    "Kalsium Karbonat (CaCO3)": "CaCO3.PDF",
    "Tembaga (II) Sulfat(CuSO4)": "CuSO4.PDF",
    "Propanol (C3H8O)": "C3H8O.PDF",
    "Butanol (C4H12O)": "C4H12O.PDF",
    "Fenol (C6H6O)": "C6H6O.PDF",
    "Xylena (C8H12)": "C8H12.PDF",
    "Asam Benzoat (C7H6O2)": "Asam Benzoat.PDF",
    "2-Aminopiridin-asam 3-karboksilat (C6H6N2O2)": "2-Aminopiridin-asam 3-karboksilat.PDF",
    "Asam Sitrat Monohidrat (C6H8O7 · H2O)": "Asam Sitrat.PDF",
    "Iodin (I2)": "Iodin.PDF",
    "Toluena (C7H8)": "Toluena.PDF",
    "EDTA (C10H12N2O8*4Na*4H2O )": "EDTA.PDF",
    "Timbal(II)Asetat Trihidrat(Pb(C2H3O2)2 · 3H2O)": "Pb Asetat.PDF",
    "Gt Anti-Rb IgG Fluorescein Conjugated Secondary (Fluorescein)": "Fluorescein.PDF",
}

# =========================
# DATABASE FILE SNI/ISO
# =========================
database_SNI = {
    "SNI-9063-2022_Air&Limbah Mikrobiologi": "SNI-9063-2022_Air&Limbah Mikrobiologi.pdf",
    "SNI-8990-2021_Air Limbah Fisika_Kimia": "SNI-8990-2021_Air Limbah Fisika_Kimia.pdf",
    "SNI-7119-3-2017_Udara Ambien (TSP)": "SNI-7119-3-2017_Udara Ambien (TSP).pdf",
    "SNI-6989-59-2008_Sampling Air Limbah": "SNI-6989-59-2008_Sampling Air Limbah.pdf",
    "SNI-6989-58-2008_Sampling Air Tanah": "SNI-6989-58-2008_Sampling Air Tanah.pdf",
    "SNI 19-7119.9-2005_Sampling Udara Ambien": "SNI 19-7119.9-2005_Sampling Udara Ambien.pdf",
    "SNI 19-7119.2-2005_Sampling Udara Emisi": "SNI 19-7119.2-2005_Sampling Udara Emisi.pdf",
    "SNI 19-0429-1989_Sampling Cairan": "SNI 19-0429-1989_Sampling Cairan.pdf",
    "SNI 19-0428-1998_Sampling Padatan": "SNI 19-0428-1998_Sampling Padatan.pdf",
    "SNI 03-6802-2002_Sampling Tanah ": "SNI 03-6802-2002_Sampling Tanah .pdf",
    "SNI 19-0428-1998_Sampling Padatan": "SNI 19-0428-1998_Sampling Padatan.pdf",
    "ISO-10381-1-2002 Soil Quality": "ISO-10381-1-2002.pdf",
    "ISO-10381-2-2002 Soil Quality": "ISO-10381-2-2002.pdf",
    "ISO-10381-3-2001 SOil Quality": "ISO-10381-3-2001.pdf",
    "ISO-10381-4-2003 Soil Quality": "ISO-10381-4-2003.pdf",
    "ISO-10381-5-2005 Soil Quality": "ISO-10381-5-2005.pdf",
    "ISO-10381-6-2009 Soil Quality": "ISO-10381-6-2009.pdf",
    "ISO_IEC_17025_2017_ID Pengujian dan Kalibrasi": "ISO_IEC_17025_2017_ID.pdf",
    "ISO_IEC_17025_2017_ENG Pengujian dan Kalibrasi": "ISO_IEC_17025_2017_ENG.pdf",
    "ISO_5667_1_2023_ENG Water Quality": "ISO_5667_1_2023_ENG.pdf",
    "ISO_5667_1_2020_ENG Water Quality": "ISO_5667_1_2020_ENG.pdf",
}

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
page_title="Perpustakaan Digital Analisis Kimia",
    page_icon="🧪",
    layout="wide"
)
    
st.markdown("""
<div class='main-title'>
🧪 Perpustakaan Digital Analisis Kimia
</div>

<div class='sub-title'>
Sistem Informasi Laboratorium dan Database MSDS
</div>
""", unsafe_allow_html=True)

/* =========================
   BACKGROUND RGB SOFT
========================= */

.stApp {
    background: linear-gradient(
        -45deg,
        #e8eef7,
        #dbeafe,
        #e0f2fe,
        #eef2ff,
        #f8fafc
    );

    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
}

/* Animasi Background */
@keyframes gradientBG {
    0% {
        background-position: 0% 50%;
    }

    50% {
        background-position: 100% 50%;
    }

    100% {
        background-position: 0% 50%;
    }
}

/* =========================
   SIDEBAR
========================= */

section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(15px);
    border-right: 1px solid rgba(255,255,255,0.3);
}

/* =========================
   JUDUL
========================= */

.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 700;
    color: #0f172a;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    font-size: 1.3rem;
    color: #475569;
    margin-bottom: 40px;
}

/* =========================
   CARD
========================= */

.card {

    background: rgba(255,255,255,0.65);

    backdrop-filter: blur(15px);

    border-radius: 25px;

    padding: 30px;

    text-align: center;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.08);

    transition: all 0.3s ease;
}

/* Hover 3D ringan */

.card:hover {

    transform:
        translateY(-8px)
        scale(1.02);

    box-shadow:
        0 15px 35px rgba(59,130,246,0.15);
}

/* Angka */

.card-number {

    font-size: 3rem;

    font-weight: bold;

    color: #2563eb;

    margin-bottom: 10px;
}

/* Judul Card */

.card-title {

    font-size: 1.1rem;

    color: #475569;
}

/* =========================
   BUTTON
========================= */

.stButton > button {

    border-radius: 12px;

    border: none;

    background: linear-gradient(
        135deg,
        #2563eb,
        #3b82f6
    );

    color: white;

    font-weight: 600;

    transition: 0.3s;
}

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 8px 20px rgba(59,130,246,0.25);
}

/* =========================
   INPUT
========================= */

.stTextInput input,
.stSelectbox div[data-baseweb="select"] {

    border-radius: 12px !important;

    background: rgba(255,255,255,0.8) !important;
}

/* =========================
   ALERT
========================= */

.stSuccess,
.stInfo,
.stWarning {

    border-radius: 15px;
}

/* =========================
   METRIC
========================= */

[data-testid="metric-container"] {

    background: rgba(255,255,255,0.7);

    border-radius: 15px;

    padding: 15px;

    box-shadow:
        0 5px 15px rgba(0,0,0,0.05);
}

</style>
""", unsafe_allow_html=True)

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

    st.markdown(
        '<div class="main-title">🧪 Perpustakaan Digital Analisis Kimia</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-title">Sistem Informasi Laboratorium dan Database MSDS</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
        <div class="card-number">{len(database_msds)}+</div>
        <div class="card-title">Database MSDS</div>
    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <div class="card-number">{len(database_msds)}+</div>
        <div class="card-title">Database MSDS</div>
    </div>
    """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="card">
        <div class="card-number">{len(database_SNI)}+</div>
        <div class="card-title">Database SNI/ISO</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.info("""
    📚 Fitur yang tersedia:
    
    - Database MSDS bahan kimia
    - Download dokumen keselamatan kerja
    - Panduan analisis gravimetri dan titrimetri
    - Referensi SNI dan ISO 17025
    - Panduan K3L laboratorium
    """)
# =========================
# HALAMAN MSDS
# =========================
elif menu == "MSDS & Safety":

    st.header("🗃️ Database MSDS & Safety")

    pilihan_bahan = st.selectbox(
        "🔍 Cari MSDS",
        options=sorted(database_msds.keys()),
        index=None,
        placeholder="Ketik nama bahan kimia..."
    )

    if pilihan_bahan is None:
        st.info("Silakan cari dan pilih bahan kimia.")
        st.stop()

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

    pilihan_bahan = st.selectbox(
        "🔍 Cari SNI/ISO",
        options=sorted(database_SNI.keys()),
        index=None,
        placeholder="Ketik nama bahan kimia..."
    )

    if pilihan_bahan is None:
        st.info("Silakan cari dan pilih bahan kimia.")
        st.stop()

    Nama_file_pdf = database_SNI[pilihan_bahan]
    
     # Folder PDF
    Folder_pdf = "pdf_SNI"

    # Gabungkan path
    Path_file = os.path.join(Folder_pdf, Nama_file_pdf)

    st.info(f"📄 File dipilih: {Nama_file_pdf}")

    # =========================
    # CEK FILE ADA / TIDAK
    # =========================
    if os.path.exists(Path_file):

        # Baca PDF
        with open(Path_file, "rb") as file_pdf:
            Konten_pdf = file_pdf.read()

        # =========================
        # TOMBOL DOWNLOAD
        # =========================
        st.download_button(
            label="📥 Download PDF",
            data=Konten_pdf,
            file_name=Nama_file_pdf,
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
