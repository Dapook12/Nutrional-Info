import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# Load dataset bunga Iris
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Siapkan model klasifikasi
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Judul aplikasi
st.title("Klasifikasi Bunga Iris")

# Input ciri-ciri bunga
sepal_length = st.number_input("Panjang Sepal (cm):")
sepal_width = st.number_input("Lebar Sepal (cm):")
petal_length = st.number_input("Panjang Kelopak (cm):")
petal_width = st.number_input("Lebar Kelopak (cm):")

# Prediksi jenis bunga
if st.button("Klasifikasi"):
    prediksi = knn.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    if prediksi == 0:
        hasil = "Iris Setosa"
    elif prediksi == 1:
        hasil = "Iris Versicolor"
    else:
        hasil = "Iris Virginica"
    st.write("Jenis bunga: ", hasil)

# Tampilkan informasi tentang bunga Iris
st.write("Informasi Bunga Iris")
with st.expander("Deskripsi"):
    st.write(
        """
        Bunga Iris memiliki tiga spesies yang umum ditemukan: Iris Setosa, Iris Versicolor, dan Iris Virginica.
        Masing-masing spesies memiliki ciri-ciri fisik yang berbeda, seperti panjang dan lebar sepal dan kelopak.
        """
    )
with st.expander("Data Set"):
    st.dataframe(data.data, columns=data.feature_names)

# Visualisasi data
st.write("Visualisasi Data")
st.bar_chart(
    X.groupby("species")[["sepal_length", "sepal_width", "petal_length", "petal_width"]].mean()
)

# CSS untuk styling
with open("style.css") as f:
    style = f.read()
st.write(f"<style>{style}</style>", unsafe_allow_html=True)
