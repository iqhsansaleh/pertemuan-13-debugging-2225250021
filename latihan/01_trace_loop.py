"""Latihan tracing perulangan.

Prediksi sebelum menjalankan: nilai akhir total adalah 24.
"""

total = 1
print("i | total setelah total = total * i")
print("--+--------------------------------")

for i in range(1, 5):
	total = total * i
	print(f"{i} | {total}")

print(f"Output akhir: {total}")
