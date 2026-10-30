"""Kasus 1: menentukan status kelulusan pada batas nilai 60."""

import unittest


def status_lulus(nilai):
	if nilai >= 60:
		return "Lulus"
	return "Tidak lulus"


class TestStatusLulus(unittest.TestCase):
	def test_nilai_di_bawah_batas(self):
		self.assertEqual(status_lulus(59), "Tidak lulus")

	def test_nilai_tepat_di_batas(self):
		self.assertEqual(status_lulus(60), "Lulus")

	def test_nilai_di_atas_batas(self):
		self.assertEqual(status_lulus(61), "Lulus")


if __name__ == "__main__":
	unittest.main()
