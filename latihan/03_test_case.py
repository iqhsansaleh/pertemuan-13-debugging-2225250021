"""Test batas kelulusan, termasuk nilai tepat pada ambang batas."""

import unittest


def status_lulus(nilai):
	if nilai >= 60:
		return "Lulus"
	return "Tidak lulus"


class TestStatusLulus(unittest.TestCase):
	def test_nilai_59_tidak_lulus(self):
		self.assertEqual(status_lulus(59), "Tidak lulus")

	def test_nilai_60_lulus(self):
		self.assertEqual(status_lulus(60), "Lulus")

	def test_nilai_61_lulus(self):
		self.assertEqual(status_lulus(61), "Lulus")


if __name__ == "__main__":
	unittest.main()
