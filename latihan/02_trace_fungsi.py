"""Latihan menelusuri parameter dan nilai return dengan debugger.

Pasang breakpoint pada baris pemanggilan hitung_diskon di bawah, lalu pilih
Step Into untuk mengamati total, persen, diskon, dan nilai return.
"""


def hitung_diskon(total, persen):
	diskon = total * persen / 100
	return total - diskon


hasil = hitung_diskon(200000, 10)
print(hasil)
