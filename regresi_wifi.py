import numpy as np
import matplotlib.pyplot as plt

# ===============================
# Data Pengukuran
# ===============================
jarak = np.array([1, 2, 3, 4, 5])

# Data ideal (teoritis, tanpa noise)
sinyal_ideal = np.array([-40, -45, -50, -55, -60])

# Data real (hasil pengukuran WiFi)
sinyal_real = np.array([-38, -42, -47, -53, -58])

# ===============================
# Regresi Linear (Data Real)
# ===============================
b, a = np.polyfit(jarak, sinyal_real, 1)
prediksi = a + b * jarak

# ===============================
# R² (Coefficient of Determination)
# ===============================
ss_res = np.sum((sinyal_real - prediksi) ** 2)               # Residual Sum of Squares
ss_tot = np.sum((sinyal_real - np.mean(sinyal_real)) ** 2)  # Total Sum of Squares
r2 = 1 - (ss_res / ss_tot)

# ===============================
# Error Analysis
# ===============================
error = np.abs(sinyal_real - prediksi)
mae = np.mean(error)

# ===============================
# Prediksi Jarak Baru
# ===============================
jarak_baru = 6
prediksi_baru = a + b * jarak_baru

# ===============================
# Output
# ===============================
print(f"Persamaan regresi: y = {a:.2f} + ({b:.2f})x")
print("Error tiap titik:", error)
print(f"Mean Absolute Error (MAE): {mae:.2f} dBm")
print(f"Nilai R²: {r2:.3f}")
print(f"Prediksi sinyal WiFi pada jarak 6 meter: {prediksi_baru:.2f} dBm")

# ===============================
# Visualisasi
# ===============================
plt.figure()
plt.scatter(jarak, sinyal_real, label="Data Real (Pengukuran)")
plt.plot(jarak, sinyal_ideal, linestyle='--', label="Data Ideal (Teoritis)")
plt.plot(jarak, prediksi, label=f"Regresi Linear (R²={r2:.2f})")
plt.scatter(jarak_baru, prediksi_baru, marker='x', s=120, label="Titik Prediksi (6 m)")

plt.title("Regresi Linear Jarak vs Kekuatan Sinyal WiFi")
plt.xlabel("Jarak (meter)")
plt.ylabel("Kekuatan Sinyal WiFi (dBm)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
