import numpy as np
import matplotlib.pyplot as plt

# =====================================
# 1. Data Pengukuran
# =====================================
# Waktu pengamatan (detik)
waktu = np.array([0, 1, 2, 3, 4])

# Kecepatan kendaraan hasil pengukuran (m/s)
kecepatan = np.array([0, 5, 12, 20, 29])

# Selang waktu
dt = waktu[1] - waktu[0]


# =====================================
# 2. Fungsi Turunan Numerik
# =====================================
def beda_maju(data, delta):
    """
    Turunan numerik metode beda maju
    """
    return np.diff(data) / delta


def beda_tengah(data, delta):
    """
    Turunan numerik metode beda tengah
    """
    return (data[2:] - data[:-2]) / (2 * delta)


# =====================================
# 3. Turunan Analitik (Ground Truth)
# =====================================
# Asumsi model kecepatan v(t) ≈ t^2 + 4t
# Maka percepatan analitik a(t) = dv/dt = 2t + 4
def percepatan_analitik(t):
    return 2 * t + 4


# =====================================
# 4. Perhitungan Turunan
# =====================================
a_maju = beda_maju(kecepatan, dt)
a_tengah = beda_tengah(kecepatan, dt)

t_maju = waktu[:-1]
t_tengah = waktu[1:-1]

a_analitik_maju = percepatan_analitik(t_maju)
a_analitik_tengah = percepatan_analitik(t_tengah)


# =====================================
# 5. Analisis Error
# =====================================
error_maju = np.abs(a_analitik_maju - a_maju)
error_tengah = np.abs(a_analitik_tengah - a_tengah)

mae_maju = np.mean(error_maju)
mae_tengah = np.mean(error_tengah)


# =====================================
# 6. Output Numerik
# =====================================
print("=== HASIL ESTIMASI PERCEPATAN KENDARAAN ===\n")

print("Metode Beda Maju")
print("Percepatan:", a_maju)
print("MAE:", round(mae_maju, 3), "m/s²\n")

print("Metode Beda Tengah")
print("Percepatan:", a_tengah)
print("MAE:", round(mae_tengah, 3), "m/s²\n")

print("Kesimpulan:")
if mae_tengah < mae_maju:
    print("Metode beda tengah lebih akurat dibandingkan beda maju.")
else:
    print("Metode beda maju cukup baik namun kurang akurat dibandingkan beda tengah.")


# =====================================
# 7. Visualisasi
# =====================================
plt.figure(figsize=(9, 8))

# Grafik Kecepatan
plt.subplot(3, 1, 1)
plt.plot(waktu, kecepatan, marker='o', label="Kecepatan")
plt.xlabel("Waktu (detik)")
plt.ylabel("Kecepatan (m/s)")
plt.title("Data Kecepatan Kendaraan")
plt.grid(True)
plt.legend()

# Grafik Percepatan
plt.subplot(3, 1, 2)
plt.plot(t_maju, a_maju, 'o-', label="Beda Maju")
plt.plot(t_tengah, a_tengah, 's-', label="Beda Tengah")
plt.plot(waktu, percepatan_analitik(waktu), '--', label="Analitik")
plt.xlabel("Waktu (detik)")
plt.ylabel("Percepatan (m/s²)")
plt.title("Perbandingan Metode Turunan Numerik")
plt.grid(True)
plt.legend()

# Grafik Error
plt.subplot(3, 1, 3)
plt.plot(t_maju, error_maju, 'o-', label="Error Beda Maju")
plt.plot(t_tengah, error_tengah, 's-', label="Error Beda Tengah")
plt.xlabel("Waktu (detik)")
plt.ylabel("Error (m/s²)")
plt.title("Perbandingan Error Metode Turunan Numerik")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
