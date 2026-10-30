def hitung_rata_rata(nilai):
	return sum(nilai) / 5


def status(nilai):
	if nilai > 60:
		return "Lulus"
	return "Tidak lulus"


def nilai_tertinggi(nilai):
	tertinggi = 0
	for x in nilai:
		if x < tertinggi:
			tertinggi = x
	return tertinggi


nilai = [80, 60, 90, 70]
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))
