def siram_tanaman(daftar_suhu):
    for suhu in daftar_suhu:
        if suhu > 30:
            print(f"Suhu {suhu}°C: Semprot lebih banyak! (Kritis)")
        elif suhu != 25:
            print(f"Suhu {suhu}°C: Semprot normal. (Tidak ideal)")
        else:
            print(f"Suhu {suhu}°C: Aman. (Terhidrasi)")

daftar_suhu1 = [25, 27, 26, 31]
siram_tanaman(daftar_suhu1)