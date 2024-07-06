import streamlit as st
import requests
import cv2
import numpy as np

# Mendefinisikan URL API Azure Services
api_url = "https://YOUR_AZURE_API_URL"

# Menampilkan judul aplikasi
st.title("Aplikasi Pengenalan Gizi Makanan")

# Kolom untuk upload gambar
uploaded_file = st.file_uploader("Upload Gambar Makanan")

# Tombol untuk proses gambar
if st.button("Proses Gambar"):
    # Membaca gambar yang diupload
    if uploaded_file is not None:
        image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # Mengubah gambar menjadi format yang sesuai untuk API Azure
        encoded_image = cv2.imencode('.jpg', image)[1].tobytes()

        # Mengirimkan gambar ke API Azure dan mendapatkan hasil
        response = requests.post(api_url, data=encoded_image)
        data = response.json()

        # Menampilkan hasil pengenalan gizi
        if data['status'] == 'success':
            st.write("**Nama Makanan:**", data['nama_makanan'])
            st.write("**Kandungan Gizi:**")
            for nutrient in data['kandungan_gizi']:
                st.write(f"- {nutrient['nama']}: {nutrient['nilai']}")
        else:
            st.write("Gagal mengenali gambar makanan.")
