import streamlit as st

# Kelas untuk konversi mata uang
class KonversiMataUang:
    def __init__(self):
        # Inisialisasi nilai tukar mata uangs
        self.nilai_tukar = {
            "USD": 1.0,      # Dolar AS
            "EUR": 0.96,     # Euro
            "IDR": 16200.92, # Rupiah Indonesia
            "JPY": 157.43,   # Yen Jepang
            "GBP": 0.80,     # Pound Sterling
            "AUD": 1.60,     # Dolar Australia
            "CAD": 1.44,     # Dolar Kanada
            "MYR": 4.47,     # Ringgit Malaysia
            "THB": 34.22,    # Baht Thailand
            "SGD": 1.36,     # Dolar Singapura
            "PHP": 58.09,    # Peso Filipina
            "VND": 25425.00, # Dong Vietnam
            "KWD": 0.31,     # Dinar Kuwait
            "BHD": 0.38      # Dinar Bahrain
        }

    def konversi(self, jumlah, mata_uang_dasar, mata_uang_tujuan):
        # Menghitung nilai tukar
        if mata_uang_dasar in self.nilai_tukar and mata_uang_tujuan in self.nilai_tukar:
            # Menghitung jumlah terkonversi
            jumlah_terkonversi = (jumlah / self.nilai_tukar[mata_uang_dasar]) * self.nilai_tukar[mata_uang_tujuan]
            return jumlah_terkonversi
        else:
            return None

def kalkulator_pajak(jumlah, persentase_pajak):
    pajak = jumlah * (persentase_pajak / 100)
    total_setelah_pajak = jumlah + pajak
    return pajak, total_setelah_pajak

def konversi_mata_uang_app():
    st.header("Konversi Mata Uang")

    mata_uang_dasar = st.selectbox("Pilih mata uang dasar", ["USD", "EUR", "IDR", "JPY", "GBP", "AUD", "CAD", "MYR", "THB", "SGD", "PHP", "VND", "KWD", "BHD"])
    mata_uang_tujuan = st.selectbox("Pilih mata uang tujuan", ["USD", "EUR", "IDR", "JPY", "GBP", "AUD", "CAD", "MYR", "THB", "SGD", "PHP", "VND", "KWD", "BHD"])

    konversi_mata_uang = KonversiMataUang()

    if mata_uang_dasar == mata_uang_tujuan:
        st.error("Mata uang dasar dan tujuan tidak boleh sama. Silahkan pilih mata uang yang berbeda.")
    else :
        jumlah = st.number_input("Masukkan jumlah mata uang yang ingin dikonversi", min_value=0.0)
        if st.button("Konversi"):
            jumlah_terkonversi = konversi_mata_uang.konversi(jumlah, mata_uang_dasar, mata_uang_tujuan)
            if jumlah_terkonversi is not None:
                st.success(f"{jumlah} {mata_uang_dasar} = {jumlah_terkonversi:.2f} {mata_uang_tujuan}")
                if "riwayat_konversi" not in st.session_state:
                    st.session_state.riwayat_konversi = []
                st.session_state.riwayat_konversi.append(f"{jumlah} {mata_uang_dasar} = {jumlah_terkonversi:.2f} {mata_uang_tujuan}")
            else:
                st.error("Mata uang tidak ditemukan. Silahkan coba lagi.")

def kalkulator_pajak_app():
    st.header("Kalkulator Pajak")

    mata_uang = st.selectbox("Pilih mata uang", ["USD", "EUR", "IDR", "JPY", "GBP", "AUD", "CAD", "MYR", "THB", "SGD", "PHP", "VND", "KWD", "BHD"])
    jumlah = st.number_input(f"Masukkan jumlah dalam {mata_uang} yang ingin dihitung pajaknya", min_value=0.0)
    persentase_pajak = st.number_input("Masukkan persentase pajak", min_value=0.0)

    if st.button("Hitung Pajak"):
        pajak, total_setelah_pajak = kalkulator_pajak(jumlah, persentase_pajak)
        st.success(f"Pajak: {pajak:.2f} {mata_uang}, Total setelah pajak: {total_setelah_pajak:.2f} {mata_uang}")
        if "riwayat_pajak" not in st.session_state:
            st.session_state.riwayat_pajak = []
        st.session_state.riwayat_pajak.append(f"Pajak: {pajak:.2f} {mata_uang}, Total setelah pajak: {total_setelah_pajak:.2f} {mata_uang}")

def konversi_satuan_app():
    st.header("Kalkulator Konversi Satuan")
    
    # Pilihan satuan dasar
    satuan_dasar = st.selectbox("Pilih satuan dasar", ["Meter", "Kilometer", "Centimeter", "Milimeter", "Mile", "Inch", "Foot", "Yard"])
    satuan_tujuan = st.selectbox("Pilih satuan tujuan", ["Meter", "Kilometer", "Centimeter", "Milimeter", "Mile", "Inch", "Foot", "Yard"])

    # Input jumlah yang ingin dikonversi
    jumlah = st.number_input("Masukkan jumlah yang ingin dikonversi", min_value=0.0)

    # Tombol untuk melakukan konversi
    if st.button("Konversi"):
        hasil = None  # Inisialisasi hasil
        if satuan_dasar == "Meter":
            if satuan_tujuan == "Kilometer":
                hasil = jumlah / 1000
            elif satuan_tujuan == "Centimeter":
                hasil = jumlah * 100
            elif satuan_tujuan == "Milimeter":
                hasil = jumlah * 1000
            elif satuan_tujuan == "Mile":
                hasil = jumlah / 1609.34
            elif satuan_tujuan == "Inch":
                hasil = jumlah * 39.3701
            elif satuan_tujuan == "Foot":
                hasil = jumlah * 3.28084
            elif satuan_tujuan == "Yard":
                hasil = jumlah * 1.09361
        elif satuan_dasar == "Kilometer":
            if satuan_tujuan == "Meter":
                hasil = jumlah * 1000
            elif satuan_tujuan == "Centimeter":
                hasil = jumlah * 100000
            elif satuan_tujuan == "Milimeter":
                hasil = jumlah * 1000000
            elif satuan_tujuan == "Mile":
                hasil = jumlah / 1.60934
            elif satuan_tujuan == "Inch":
                hasil = jumlah * 39370.1
            elif satuan_tujuan == "Foot":
                hasil = jumlah * 3280.84
            elif satuan_tujuan == "Yard":
                hasil = jumlah * 1093.61
        elif satuan_dasar == "Centimeter":
            if satuan_tujuan == "Meter":
                hasil = jumlah / 100
            elif satuan_tujuan == "Kilometer":
                hasil = jumlah / 100000
            elif satuan_tujuan == "Milimeter":
                hasil = jumlah * 10
            elif satuan_tujuan == "Mile":
                hasil = jumlah / 160934
            elif satuan_tujuan == "Inch":
                hasil = jumlah / 2.54
            elif satuan_tujuan == "Foot":
                hasil = jumlah / 30.48
            elif satuan_tujuan == "Yard":
                hasil = jumlah / 91.44
        elif satuan_dasar == "Milimeter":
            if satuan_tujuan == "Meter":
                hasil = jumlah / 1000
            elif satuan_tujuan == "Kilometer":
                hasil = jumlah / 1000000
            elif satuan_tujuan == "Centimeter":
                hasil = jumlah / 10
            elif satuan_tujuan == "Mile":
                hasil = jumlah / 1609340
            elif satuan_tujuan == "Inch":
                hasil = jumlah / 25.4
            elif satuan_tujuan == "Foot":
                hasil = jumlah / 304.8
            elif satuan_tujuan == "Yard":
                hasil = jumlah / 914.4
        elif satuan_dasar == "Mile":
            if satuan_tujuan == "Meter":
                hasil = jumlah * 1609.34
            elif satuan_tujuan == "Kilometer":
                hasil = jumlah * 1.60934
            elif satuan_tujuan == "Centimeter":
                hasil = jumlah * 160934
            elif satuan_tujuan == "Milimeter":
                hasil = jumlah * 1609340
            elif satuan_tujuan == "Inch":
                hasil = jumlah * 63360
            elif satuan_tujuan == "Foot":
                hasil = jumlah * 5280
            elif satuan_tujuan == "Yard":
                hasil = jumlah * 1760
        elif satuan_dasar == "Inch":
            if satuan_tujuan == "Meter":
                hasil = jumlah / 39.3701
            elif satuan_tujuan == "Kilometer":
                hasil = jumlah / 39370.1
            elif satuan_tujuan == "Centimeter":
                hasil = jumlah * 2.54
            elif satuan_tujuan == "Milimeter":
                hasil = jumlah * 25.4
            elif satuan_tujuan == "Mile":
                hasil = jumlah / 63360
            elif satuan_tujuan == "Foot":
                hasil = jumlah / 12
            elif satuan_tujuan == "Yard":
                hasil = jumlah / 36
        elif satuan_dasar == "Foot":
            if satuan_tujuan == "Meter":
                hasil = jumlah / 3.28084
            elif satuan_tujuan == "Kilometer":
                hasil = jumlah / 3280.84
            elif satuan_tujuan == "Centimeter":
                hasil = jumlah * 30.48
            elif satuan_tujuan == "Milimeter":
                hasil = jumlah * 304.8
            elif satuan_tujuan == "Mile":
                hasil = jumlah / 5280
            elif satuan_tujuan == "Inch":
                hasil = jumlah * 12
            elif satuan_tujuan == "Yard":
                hasil = jumlah / 3
        elif satuan_dasar == "Yard":
            if satuan_tujuan == "Meter":
                hasil = jumlah / 1.09361
            elif satuan_tujuan == "Kilometer":
                hasil = jumlah / 1093.61
            elif satuan_tujuan == "Centimeter":
                hasil = jumlah * 91.44
            elif satuan_tujuan == "Milimeter":
                hasil = jumlah * 914.4
            elif satuan_tujuan == "Mile":
                hasil = jumlah / 1760
            elif satuan_tujuan == "Inch":
                hasil = jumlah * 36
            elif satuan_tujuan == "Foot":
                hasil = jumlah * 3

        # Menampilkan hasil konversi
        if hasil is not None:
            st.write(f"Hasil konversi: {hasil} {satuan_tujuan}")
        else:
            st.write("Satuan tidak dikenali.")

        st.success(f"{jumlah} {satuan_dasar} = {hasil:.2f} {satuan_tujuan}")
        if "riwayat_satuan" not in st.session_state:
            st.session_state.riwayat_satuan = []
        st.session_state.riwayat_satuan.append(f"{jumlah} {satuan_dasar} = {hasil:.2f} {satuan_tujuan}")

def about_us():
    st.header("About Us")
    st.write("""
        Anggota kelompok: 
        
        1. Muhammad Alfarel Putra (0110224071)
        2. Latif Wibowo (0110224065)
        3. Umar Al Faruq (0110224093)
        4. Angeliq Mexgaputri (0110224217)

        Penjelasan Aplikasi:

        Aplikasi ini dirancang untuk membantu pengguna dalam melakukan konversi mata uang, 
        menghitung pajak, dan melakukan konversi satuan panjang, serta menyediakan riwayat semua fitur.
        Kami berkomitmen untuk memberikan kemudahan dan keakuratan dalam setiap perhitungan.
    """)

def riwayat_fitur():
    st.header("Riwayat")
    
    # Menampilkan riwayat konversi
    if 'riwayat_konversi' in st.session_state:
        st.subheader("Riwayat Konversi Mata Uang")
        for item in st.session_state.riwayat_konversi:
            st.write(item)
    else:
        st.write("Belum ada riwayat konversi mata uang.")

    # Menampilkan riwayat pajak
    if 'riwayat_pajak' in st.session_state:
        st.subheader("Riwayat Pajak")
        for item in st.session_state.riwayat_pajak:
            st.write(item)
    else:
        st.write("Belum ada riwayat pajak.")
    
    if 'riwayat_satuan' in st.session_state:
        st.subheader("Riwayat Satuan")
        for item in st.session_state.riwayat_satuan:
            st.write(item)
    else:
        st.write("Belum ada riwayat satuan.")


def main():
    st.title("Aplikasi Konversi Mata Uang dan Lain-lainnya")

    pilihan = st.sidebar.selectbox("Pilihan Fitur:", ["About Us","Konversi Mata Uang", "Kalkulator Pajak","Konversi Satuan", "Riwayat Fitur"])
    if pilihan == "About Us":
        about_us()
    elif pilihan == "Konversi Mata Uang":
        konversi_mata_uang_app()
    elif pilihan == "Kalkulator Pajak":
        kalkulator_pajak_app()
    elif pilihan == "Konversi Satuan":
        konversi_satuan_app()
    elif pilihan == "Riwayat Fitur":
        riwayat_fitur()

if __name__ == "__main__":
    main()