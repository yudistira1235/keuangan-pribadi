import csv
from datetime import datetime
from collections import defaultdict

FILE_NAME = 'transaksi.csv'

def read_data():
    try:
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def write_data(data):
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ['Tanggal', 'Jenis', 'Kategori', 'Jumlah', 'Keterangan']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def add_transaction():
    tanggal = input('Tanggal (YYYY-MM-DD): ')
    jenis = input('Jenis (Pemasukan/Pengeluaran): ')
    kategori = input('Kategori: ')
    jumlah = input('Jumlah: ')
    keterangan = input('Keterangan: ')
    data = read_data()
    data.append({'Tanggal': tanggal, 'Jenis': jenis, 'Kategori': kategori, 'Jumlah': jumlah, 'Keterangan': keterangan})
    write_data(data)
    print('Data berhasil ditambahkan.')

def view_transactions():
    data = read_data()
    for idx, row in enumerate(data):
        print(f"{idx+1}. {row}")

def report_bulanan_tahunan():
    data = read_data()
    tahun = input('Masukkan tahun (YYYY): ')
    bulan = input('Masukkan bulan (MM), kosongkan jika ingin laporan tahunan: ')
    total_pemasukan = 0
    total_pengeluaran = 0
    for row in data:
        tanggal = datetime.strptime(row['Tanggal'], '%Y-%m-%d')
        if tanggal.year == int(tahun) and (bulan == '' or tanggal.month == int(bulan)):
            if row['Jenis'].lower() == 'pemasukan':
                total_pemasukan += int(row['Jumlah'])
            elif row['Jenis'].lower() == 'pengeluaran':
                total_pengeluaran += int(row['Jumlah'])
    print(f"Total Pemasukan: {total_pemasukan}")
    print(f"Total Pengeluaran: {total_pengeluaran}")
    print(f"Saldo: {total_pemasukan - total_pengeluaran}")

def laporan_kategori_pengeluaran():
    data = read_data()
    kategori_pengeluaran = defaultdict(int)
    for row in data:
        if row['Jenis'].lower() == 'pengeluaran':
            kategori_pengeluaran[row['Kategori']] += int(row['Jumlah'])
    print('Laporan Pengeluaran per Kategori:')
    for kategori, jumlah in kategori_pengeluaran.items():
        print(f"{kategori}: {jumlah}")

def menu():
    while True:
        print('\nMenu Manajemen Keuangan Pribadi')
        print('1. Tambah Catatan Pemasukan/Pengeluaran')
        print('2. Lihat Semua Catatan')
        print('3. Laporan Bulanan/Tahunan')
        print('4. Laporan Kategori Pengeluaran')
        print('5. Keluar')
        pilihan = input('Pilih menu: ')

        if pilihan == '1':
            add_transaction()
        elif pilihan == '2':
            view_transactions()
        elif pilihan == '3':
            report_bulanan_tahunan()
        elif pilihan == '4':
            laporan_kategori_pengeluaran()
        elif pilihan == '5':
            print('Terima kasih telah menggunakan aplikasi.')
            break
        else:
            print('Pilihan tidak valid.')

if __name__ == '__main__':
    menu()