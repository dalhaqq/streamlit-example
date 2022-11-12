import streamlit as st

Data_Produk = {
    101:"BERAS PUTIH",
    102:"GULA PASIR",
    103:"GULA JAWA",
    104:"MIE INSTANT",
    105:"TELUR AYAM",
    106:"MINYAK GORENG",
    107:"SUSU BUBUK",
    108:"SUSU KENTAL",
    109:"SUSU UHT",
    110:"TEPUNG TERIGU",
    111:"TEPUNG MAIZENA",
    112:"TEPUNG TAPIOKA",
    113:"TEPUNG BERAS",
    114:"TEPUNG KETAN",
    115:"KOPI HITAM",
    116:"KECAP MANIS",
    117:"KECAP ASIN",
    118:"SAUS TOMAT",
    119:"SAUS PEDAS",
    120:"SAUS TIRAM",
}
Data_Harga = {
    101:"250000",
    102:"120000",
    103:"160000",
    104:"48000",
    105:"250000",
    106:"252000",
    107:"420000",
    108:"180000",
    109:"96000",
    110:"450000",
    111:"425000",
    112:"180000",
    113:"144000",
    114:"228000",
    115:"120000",
    116:"156000",
    117:"156000",
    118:"204000",
    119:"204000",
    120:"132000"
}
Data_Netto = {
    101:"25 kg/karung ",
    102:"10 kg/karung",
    103:"10 kg/karung",
    104:"1 kardus",
    105:"1 peti",
    106:"1 kardus",
    107:"1 kardus",
    108:"1 Kardus",
    109:"1 Kardus",
    110:"1 karung",
    111:"1 karung",
    112:"1 karung",
    113:"1 karung",
    114:"1 karung",
    115:"1 kardus",
    116:"1 kardus",
    117:"1 kardus",
    118:"1 kardus",
    119:"1 kardus",
    120:"1 kardus"
}


st.title('TOKO SEDERHANA')
st.write('OLEH KELOMPOK 2 AKUNTANSI C 2021')
st.image('https://kemensos.go.id/uploads/topics/15816644489183.jpg')
Barang = ({
       'NAMA PRODUK': Data_Produk,
       'HARGA PRODUK': Data_Harga,
       'PER': Data_Netto
       })

st.table(Barang)

Produk = st.selectbox(
    'PILIH ID PRODUK',
    (Data_Produk))
Keterangan = st.write('*PRODUK DENGAN ID', Produk, 'ADALAH', Data_Produk[Produk])
Jumlah = st.number_input('JUMLAH PESANAN', min_value=0)
Total_Harga = st.write(Jumlah, 'x', Data_Harga[Produk], '=', int(Jumlah)*int(Data_Harga[Produk]))
Nama = st.text_input('NAMA PEMBELI')
Alamat = st.text_input('ALAMAT PEMBELI')
No_HP = st.text_input('NOMOR HP')
Ekspedisi = st.radio(
    "EKSPEDISI PENGIRIMAN",
    ('JNE', 'JNT', 'SiCepat Halu', 'Anteraja'))

Data_Metode = {
    1:"BRI",
    2:"BCA",
    3:"BNI",
    4:"DANA",
    5:"OVO",
    6:"LINK AJA",
    7:"SHOOPE"
}
Data_Nomor = {
    1: "000701029624534 a.n Adinda  Maulidia Sari",
    2: "5515007277 a.n Nur Kana Rahmawati",
    3: "1382052514 a.n Karaniya",
    4: "083147851179 a.n Wishty Sabrina ",
    5: "08990336249 a.n Fajar Prasetyo",
    6: "08990336249 a.n Adinda Maulidia Sari",
    7: "08532145627 a.n Karaniya", 
}

Pembayaran = ({
    'METODE PEMBAYARAN':Data_Metode
    })
st.table(Pembayaran)
Metode = st.selectbox(
    'METODE PEMBAYARAN', (Data_Metode))
st.write('*ANDA MEMILIH METODE PEMBAYARAN', Data_Metode[Metode])

Hasil = st.button('Selesai')

if Hasil:
    if Nama == '' or Alamat == '' or No_HP == '' or Ekspedisi == '' :
        st.warning('ISIAN TIDAK BOLEH KOSONG')
    else:
        pembeli = ({
                'NAMA PEMBELI': [Nama],
                'ALAMAT PEMBELI': [Alamat],
                'NOMOR HP': [No_HP],
                'EKSPEDISI': [Ekspedisi],
                'BARANG YANG DIBELI': [Data_Produk[Produk]],
                'JUMLAH PESANAN': [Jumlah],
                'JUMLAH TAGIHAN (Rp.)': [int(Jumlah)*int(Data_Harga[Produk])]
                })
        st.table(pembeli)
        
        st.write('METODE PEMBAYARAN', Data_Metode[Metode], 'DENGAN NOMOR TUJUAN', Data_Nomor[Metode])

        st.info('SILAHKAN LAKUKAN TRANSAKSI PEMBAYARAN KURANG DARI 1X24 JAM')

        st.write('*Mohon lakukan konfirmasi pembayaran ke No.WA 08990336249 dengan format:')
        st.write('Nama_Kode Barang_Metode pembayaran')
