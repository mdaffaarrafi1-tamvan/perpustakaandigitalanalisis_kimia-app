import streamlit as st
import os
import base64
import streamlit.components.v1 as components
from streamlit_pdf_viewer import pdf_viewer
from streamlit_option_menu import option_menu

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
    "SNI-06-6989.3-2004_TSS-Secara-Gravimetri": "SNI-06-6989.3-2004-TSS-Secara-Gravimetri.pdf",
    "SNI-6989-72_2009_Cara-Uji-Kebutuhan-BOD": "SNI-6989-72_2009-Cara-Uji-Kebutuhan-BOD.pdf",
    "SNI-1971-2011_Cara-Uji-Kadar-Air-Total-Agregat-Dengan-Pengeringan": "SNI-1971-2011-Cara-Uji-Kadar-Air-Total-Agregat-Dengan-Pengeringan.pdf",
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
    "ISO-45001-2018 Occupational health and safety management systems ": "ISO-45001-2018.pdf",
}

# =========================
# DATABASE FILE Kalibrasi
# =========================
database_kalibrasi = {
    "HPLC": "hplc-method-dev-guide-br6818en-mk.pdf",
    "GCMS": "Shimadzu-QP-2020-NX-GCMS-training-manual.pdf",
    "pH Meter": "INE-PH200E_OPR_VER2.pdf",
    "Spectro-X4PC": "Spectro-X4PC_OPR.pdf",
    "Neraca Analitik": "shimadzu-analytical-balance-aux-Manual.pdf",
}

# =========================
# KONFIGURASI HALAMAN
# =========================
st.markdown("""
<div class="main-title">
🧪 PERPUSTAKAAN DIGITAL ANALISIS KIMIA
</div>

<div class="sub-title">
MSDS • SNI • ISO • Metode Analisis Laboratorium
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* ==========================================
   BACKGROUND ANIMASI
========================================== */

[data-testid="stAppViewContainer"]{
    background: linear-gradient(
        -45deg,
        #0f172a,
        #1e3a8a,
        #0f766e,
        #4338ca,
        #0f172a
    );

    background-size: 500% 500%;

    animation: animateBG 10s ease infinite;
}

@keyframes animateBG{
    0%{
        background-position:0% 50%;
    }

    50%{
        background-position:100% 50%;
    }

    100%{
        background-position:0% 50%;
    }
}

/* ==========================================
   CONTAINER UTAMA
========================================== */

.main .block-container{

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(15px);

    border-radius:25px;

    padding:2rem;

    margin-top:15px;

    box-shadow:
        0px 10px 40px rgba(0,0,0,0.25);
}

/* ==========================================
   SIDEBAR MODERN
========================================== */

section[data-testid="stSidebar"]{

    background: rgba(15,23,42,0.92);

    backdrop-filter: blur(20px);

    border-right:1px solid rgba(255,255,255,0.15);
}

/* Semua tulisan sidebar */

section[data-testid="stSidebar"] *{

    color:white !important;
}

/* ==========================================
   RADIO MENU
========================================== */

div[role="radiogroup"] label{

    background: rgba(255,255,255,0.08);

    padding:12px;

    border-radius:15px;

    margin-bottom:8px;

    transition:0.3s;
}

div[role="radiogroup"] label:hover{

    background: rgba(56,189,248,0.25);

    transform:translateX(5px);
}

/* ==========================================
   JUDUL
========================================== */

.main-title{

    text-align:center;

    font-size:3rem;

    font-weight:bold;

    color:white;

    text-shadow:
        0 0 10px rgba(56,189,248,0.7);
}

.sub-title{

    text-align:center;

    color:#e2e8f0;

    margin-bottom:40px;
}

/* ==========================================
   CARD
========================================== */

.card{

    background: rgba(255,255,255,0.12);

    backdrop-filter: blur(12px);

    border-radius:25px;

    padding:30px;

    text-align:center;

    border:1px solid rgba(255,255,255,0.15);

    transition:0.3s;
}

.card:hover{

    transform:
        translateY(-8px)
        scale(1.03);

    box-shadow:
        0 0 25px rgba(56,189,248,0.35);
}

.card-number{

    font-size:3rem;

    font-weight:bold;

    color:#38bdf8;
}

.card-title{

    color:white;
}

/* ==========================================
   BUTTON MODERN
========================================== */

.stButton > button{

    width:100%;

    border:none;

    border-radius:15px;

    padding:12px;

    font-weight:bold;

    color:white;

    background: linear-gradient(
        135deg,
        #2563eb,
        #06b6d4
    );

    transition:0.3s;

    box-shadow:
        0 0 15px rgba(6,182,212,0.25);
}

.stButton > button:hover{

    transform:
        translateY(-3px)
        scale(1.02);

    box-shadow:
        0 0 25px rgba(6,182,212,0.5);
}

/* ==========================================
   DOWNLOAD BUTTON
========================================== */

.stDownloadButton > button{

    width:100%;

    border:none;

    border-radius:15px;

    font-weight:bold;

    color:white;

    background: linear-gradient(
        135deg,
        #10b981,
        #06b6d4
    );

    box-shadow:
        0 0 15px rgba(16,185,129,0.3);
}

/* ==========================================
   INPUT
========================================== */

.stTextInput input{

    border-radius:15px !important;

    border:1px solid rgba(255,255,255,0.3);
}

.stSelectbox > div > div{

    border-radius:15px !important;
}

/* ==========================================
   HEADER TEXT
========================================== */

h1,h2,h3,h4,h5,h6{

    color:white !important;
}

p,label{

    color:white !important;
}

li{

    color:#ADD8E6 !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================


with st.sidebar:
    
    menu = option_menu(
        menu_title=" Navigasi",
        options=[
            "Home",
            "MSDS & Safety",
            "SNI & ISO",
            "Kalibrasi Alat",
            "Panduan Analisis",
        ],
        icons=[
            "house-fill",
            "exclamation-triangle-fill",
            "file-earmark-text-fill",
            "tools",
            "clipboard-data-fill",
        ],
        menu_icon="mortarboard-fill",
        default_index=0,
        styles={
            "container": {
                "padding": "10px",
                "background-color": "#0f172a",
                "border-radius": "15px"
            },

            "icon": {
                "color": "#38bdf8",
                "font-size": "18px"
            },

            "menu-title": {
                "color": "white",
                "font-size": "20px",
                "font-weight": "bold"
            },

            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "padding": "12px",
                "margin": "5px",
                "border-radius": "12px",
                "--hover-color": "#1e293b",
            },

            "nav-link-selected": {
                "background": "linear-gradient(135deg,#2563eb,#06b6d4)",
                "color": "white",
                "font-weight": "bold",
            },
        }
    )

# =========================
# HALAMAN HOME
# =========================
if menu == "Home":
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <div class="card-number">{len(database_msds)}</div>
            <div class="card-title">Database MSDS</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <div class="card-number">{len(database_kalibrasi)}</div>
            <div class="card-title">Database Kalibrasi</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="card">
            <div class="card-number">{len(database_SNI)}</div>
            <div class="card-title">Database SNI/ISO</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.info("""
    📚 Fitur yang tersedia:
    - Database MSDS bahan kimia, SNI, ISO, Kalibrasi Instrumen
    - Download dokumen MSDS, SNI, ISO, Kalibrasi Instrumen
    - Panduan analisis gravimetri dan titrimetri
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
        placeholder="Ketik Nama Bahan Kimia Yang Ingin Dicari..."
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
        placeholder="Ketik SNI/ISO Yang Ingin Dicari..."
    )

    if pilihan_bahan is None:
        st.info("Silakan cari dan pilih SNI.")
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

    pilihan_bahan = st.selectbox(
        "🔍 Cari Kalibrasi",
        options=sorted(database_kalibrasi.keys()),
        index=None,
        placeholder="Ketik Instrumen Yang Ingin Dikalibrasi..."
    )

    if pilihan_bahan is None:
        st.info("Silakan cari dan pilih Instrumen.")
        st.stop()

    nAma_file_pdf = database_kalibrasi[pilihan_bahan]
    
     # Folder PDF
    fOlder_pdf = "pdf_kalibrasi"

    # Gabungkan path
    Path_file = os.path.join(fOlder_pdf, nAma_file_pdf)

    st.info(f"📄 File dipilih: {nAma_file_pdf}")

    # =========================
    # CEK FILE ADA / TIDAK
    # =========================
    if os.path.exists(Path_file):

        # Baca PDF
        with open(Path_file, "rb") as file_pdf:
            kOnten_pdf = file_pdf.read()

        # =========================
        # TOMBOL DOWNLOAD
        # =========================
        st.download_button(
            label="📥 Download PDF",
            data=kOnten_pdf,
            file_name=nAma_file_pdf,
            mime="application/pdf",
            use_container_width=True
        )

        st.success("✅ File PDF berhasil dimuat")

        # =========================
        # PREVIEW PDF
        # =========================
        st.subheader("📄 Preview PDF")       
        pdf_viewer(kOnten_pdf)
        
# =========================
# HALAMAN PANDUAN ANALISIS
# =========================
elif menu == "Panduan Analisis":

    st.header("🔬 Metode Analisis Laboratorium")

    metode = st.radio(
        "Pilih Metode:",
        ["Gravimetri", "Titrimetri"],
        horizontal=True
    )

    # ==========================================
    # GRAVIMETRI
    # ==========================================
    if metode == "Gravimetri":

        sub_metode = st.selectbox(
            "Pilih Percobaan Gravimetri:",
            [
                "Penentuan Kadar Air",
                "Penentuan Kadar Abu",
                "Penentuan Kadar Sulfat Dalam Garam Glauber",
                "Penentuan Kadar Besi Dalam FAS",
                "Penentuan Kadar Barium Dalam Barium Klorida",
            ]
        )

        if sub_metode == "Penentuan Kadar Air":

            st.subheader("💧 Penentuan Kadar Air")

            st.markdown("""
### Cara Kerja

Timbang wadah kosong + tutup

⬇️

Panaskan dalam tanur ± 130˚C selama 1 jam

⬇️

Dinginkan ( Desikator ) selama 30 menit

⬇️

Timbang sebagai (W0)

⬇️

Timbang sampel teliti 2 gram ke wadah
dengan posisi tutup di bawah wadah, catat
sebagai (W1)

⬇️

Panaskan wadah berisi sampel dalam keadaan tidak
tertutup rapat, di tanur pada suhu ± 130˚C selama 1 jam

⬇️

Dinginkan ( Desikator ) selama 15 menit

⬇️

Timbang sebagai (W2)

⬇️

Hitung kadar air (%)
""")

        elif sub_metode == "Penentuan Kadar Abu":

            st.subheader("🔥 Penentuan Kadar Abu")

            st.markdown("""
### Cara Kerja

Masukkan cawan ke tanur, lalu panaskan dengan suhu
± 550˚C selama 1 jam

⬇️

Dinginkan ( Desikator ), lalu timbang bobot kosong 
sampai bobot tetap, catat sebagai (W0)

⬇️

Timbang sampel 3 s/d 5 gram ke cawan,
catat sebagai (W1)

⬇️

Sampel dalam cawan (W1) di arangkan diatas bunsen, abukan 
dengan melakukan pemijaran menggunakan maker

⬇️

Panaskan sampel dengan tanur pada suhu 
± 550˚C selama 1 jam, dinginkan ( Desikator )
selama 30 menit

⬇️

Ulangi step diatas hingga mendapatkan bobot konstan

⬇️

Timbang dan catat sebagai (W2)

⬇️

Menghitung Kadar Abu (%)
""")
        elif sub_metode == "Penentuan Kadar Sulfat Dalam Garam Glauber":

            st.subheader("🔥 Penentuan Kadar Sulfat Dalam Garam Glauber")

            st.markdown("""
### Cara Kerja

Timbang sampel garam glauber 
0,5 gram ke piala gelas 500 mL

⬇️

Larutkan dengan 250 mL air suling, lalu
diasamkan dengan 3 mL HCL 4N

⬇️

Dipanaskan sampai mendidih, dibubuhi barium klorida yang 
mendidih sambil diaduk, penambahan barium klorida harus
dilakukan dnegna cepat sambil diaduk

⬇️

Uji sempurna dengan setetes larutan barium

⬇️

Aging selama 1 jam dengan api yang kecil

⬇️

Endapan pada piala gelas di cuci dengan air panas, untuk menghilang kan Cl-

⬇️

Saring endapan menggunakan kertas saring dan corong kaca, 
lalu bilas hingga endapan bebas dari pengotor 

⬇️

Uji endapan dengan tetesan terakhir nya di beri ( Perak Nitrat dengan Asam Nitrat )

⬇️

jika sudah bebas pengotor, beri setetes asam sulfat, lalu masukkan ke cawan,
lalu keringkan diatas bunsen, lalu pijarkan menggunakan meker

⬇️

Panaskan dalam tanur pada suhu 750˚C hingga bobot tetap,
timbang sebagai (W2)

⬇️

Hitung kadar sulfat (%)

""")
        elif sub_metode == "Penentuan Kadar Besi Dalam FAS":

            st.subheader("🔥 Penentuan Kadar Fe dalam garam besi (II)")

            st.markdown("""
### Cara Kerja

Timbang 0,25 g smapel Ferro Ammonium Sulfat (FAS)

⬇️

Masukkan ke piala gelas 400 mL, larutkan 25 mL air suling.
tambahkan 1 tetes Asam Sulfat

⬇️

Letakkan diatas bunsen lalu tambahkan Asam Nitrat 20 tetes,
tambahkan air suling hingga tepat 200 mL, lalu panaskan

⬇️

Uji larutan dengan setetes ammonia untuk mengetahui 
besi (ll) sudah teroksidasi menjadi besi (lll)

⬇️

Jika oksidasi sudah sempurna, panaskan hingga sebelum mendidih

⬇️

Tambahkan ammonia 7 drop hingga terbentuk endapan, setelah itu diamkan
hingga mengendap

⬇️

Uji sempurna dengan setetes ammonia, jika tidak terbentuk endapan maka 
pengendapan sudah sempurna 

⬇️

Aging selama 30 sampai 40 menit dengan api kecil

⬇️

Cairan disaring menggunakan kertas saring whatman no 41
endapan dicuci dengan Ammonium Nitrat 1%, pencucian
dilakukan 3 sampai 4 kali hingga bersih

⬇️ 

Masukkan ke cawan porselen, lalu keringkan diatas bunsen,
kemudian dipijarkan menggunakan meker

⬇️ 

Masukkan kedalam tanur, desikator dan timbang bobot akhir 

⬇️ 

Hitung kadar Fe (%)
""")
        elif sub_metode == "Penentuan Kadar Barium Dalam Barium Klorida":

            st.subheader("🔥 Penentuan Kadar Barium")

            st.markdown("""
### Cara Kerja

Masukkan cawan ke tanur, lalu panaskan dengan suhu
± 550˚C selama 1 jam

⬇️

Dinginkan ( Desikator ), lalu timbang bobot kosong 
sampai bobot tetap, catat sebagai (W0)

⬇️

Timbang sampel 3 s/d 5 gram ke cawan,
catat sebagai (W1)

⬇️

Sampel dalam cawan (W1) di arangkan diatas bunsen, abukan 
dengan melakukan pemijaran menggunakan maker

⬇️

Panaskan sampel dengan tanur pada suhu 
± 550˚C selama 1 jam, dinginkan ( Desikator )
selama 30 menit

⬇️

Ulangi step diatas hingga mendapatkan bobot konstan

⬇️

Timbang dan catat sebagai (W2)

⬇️

Menghitung Kadar Abu (%)
""")
    # ==========================================
    # TITRIMETRI
    # ==========================================
    elif metode == "Titrimetri":

        sub_metode = st.selectbox(
            "Pilih Metode Titrimetri:",
            [
                "Standarisasi NaOH 0,1 N",
                "Standarisasi HCl 0,1 N",
                "Standarisasi KMnO₄ 0,1 N",
                "Standarisasi Na₂S₂O₃ 0,1 N",
                "Standarisasi EDTA 0,1 N"
            ]
        )

        if sub_metode == "Standarisasi NaOH 0,1 N":

            st.subheader("🧪 Standarisasi NaOH 0,1 N")

            st.markdown("""
### Cara Kerja

Timbang teliti ± 630 mg asam oksalat dengan kaca arloji

⬇️

Larutkan dalam labu takar 100 mL, lalu homogenkan

⬇️

Larutan dipipet sebanyak 25 mL ke dalam erlenmeyer 250 mL

⬇️

Tambahkan 2 tetes indikator fenolftalein ( PP )

⬇️

Titar dengan NaOH 0,1N 
tidak berwarna -> merah muda seulas 

⬇️

Catat volume, lalu hitung normalitas NaOH
""")

        elif sub_metode == "Standarisasi HCl 0,1 N":

            st.subheader("🧪 Standarisasi HCl 0,1 N")

            st.markdown("""
### Cara Kerja

Timbang teliti 1500 mg boraks dengan kaca arloji

⬇️

Larutkan dalam labu takar 100 mL, lalu homogenkan

⬇️

Larutan dipipet sebanyak 25 mL ke dalam erlenmeyer 250 mL

⬇️

Tambahkan 2 tetes indikator metil merah ( MM )

⬇️

Titar dengan HCl 0,1N 
kuning seulas -> merah muda seulas 

⬇️

Catat volume, lalu hitung normalitas HCl
""")

        elif sub_metode == "Standarisasi KMnO₄ 0,1 N":

            st.subheader("🧪 Standarisasi KMnO₄ 0,1 N")

            st.markdown("""
### Cara Kerja

Timbang teliti ± 630 mg asam oksalat dengan kaca arloji

⬇️

Larutkan dalam labu takar 100 mL, lalu homogenkan

⬇️

Larutan dipipet sebanyak 25 mL ke dalam erlenmeyer 250 mL
+ asam sulfat 25 mL, lalu panaskan sampai 70˚C

⬇️

Titar dengan KMnO4 
Tidak berwarna -> merah muda seulas 

⬇️

Catat volume, lalu hitung normalitas KMnO4
""")

        elif sub_metode == "Standarisasi Na₂S₂O₃ 0,1 N":

            st.subheader("🧪 Standarisasi Na₂S₂O₃ 0,1 N")

            st.markdown("""
### Cara Kerja

Timbang teliti 500 mg kalium dikromat

⬇️

Melarutkan dalam Aquades

⬇️

Menambahkan KI Berlebih

⬇️

Menambahkan HCl

⬇️

Membebaskan Iodin (I₂)

⬇️

Menitrasi dengan Na₂S₂O₃

⬇️

Menambahkan Indikator Amilum

⬇️

Titrasi hingga Larutan Tidak Berwarna

⬇️

Menghitung Normalitas Na₂S₂O₃
""")

        elif sub_metode == "Standarisasi EDTA 0,1 N":

            st.subheader("🧪 Standarisasi EDTA 0,1 N")

            st.markdown("""
### Cara Kerja

Menyiapkan Larutan Standar CaCO₃

⬇️

Melarutkan dalam Aquades

⬇️

Menambahkan Buffer pH 10

⬇️

Menambahkan Indikator Eriochrome Black T (EBT)

⬇️

Menitrasi dengan Larutan EDTA

⬇️

Perubahan Warna Merah Anggur Menjadi Biru

⬇️

Mencatat Volume EDTA

⬇️

Menghitung Konsentrasi EDTA
""")
