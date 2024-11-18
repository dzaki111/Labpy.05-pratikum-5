kontak = {
    "Ari": "081267888",
    "Dina": "087677776"
}

print(f"Kontak Ari: {kontak['Ari']}")

kontak["Ari"] = "087654544"
print("\nKontak baru ditambahkan: Ari - 087654544")

kontak["Dina"] = "088999776"
print("\nKontak Dina diperbarui: Dina - 088999776")

print("\nDaftar Nama:")
for nama in kontak.keys():
    print(nama)

print("\nDaftar Nomor:")
for nomor in kontak.values():
    print(nomor)

print("\nDaftar Nama dan Nomor:")
print("=" * 30)
print(f"{'Nama':<10} | {'Nomor':<15}")
print("=" * 30)
for nama, nomor in kontak.items():
    print(f"{nama:<10} | {nomor:<15}")
print("=" * 30)

del kontak["Dina"]
print("\nKontak Dina berhasil dihapus.")

print("\nDaftar Nama dan Nomor (Setelah Penghapusan):")
print("=" * 30)
print(f"{'Nama':<10} | {'Nomor':<10}")
print("=" * 30)
for nama, nomor in kontak.items():
    print(f"{nama:<10} | {nomor:<10}")
print("=" * 30)
