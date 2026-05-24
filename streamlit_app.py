# =========================================================
# CARI MSDS
# =========================================================
elif menu == "Cari MSDS":

    st.header("📄 Upload dan Analisis MSDS")

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
        pdf_reader = PdfReader(uploaded_file)

        jumlah_halaman = len(pdf_reader.pages)

        st.write(f"Jumlah halaman PDF: {jumlah_halaman}")

        # mengambil teks seluruh halaman
        all_text = ""

        for page in pdf_reader.pages:

            text = page.extract_text()

            if text:
                all_text += text

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

            st.error(
                f"Bahan memiliki indikasi bahaya: {', '.join(hasil_bahaya)}"
            )

        else:

            st.success("Tidak ditemukan kata kunci bahaya.")
