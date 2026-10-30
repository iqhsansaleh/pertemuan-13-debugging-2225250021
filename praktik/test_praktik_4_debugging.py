import unittest

from praktik_4_debugging import hitung_rata_rata, nilai_tertinggi, status


class TestPemrosesanNilai(unittest.TestCase):
    def test_t1_rata_rata_empat_nilai(self):
        self.assertEqual(hitung_rata_rata([80, 60, 90, 70]), 75.0)

    def test_t2_rata_rata_dua_nilai(self):
        self.assertEqual(hitung_rata_rata([100, 80]), 90.0)

    def test_t3_status_nilai_60(self):
        self.assertEqual(status(60), "Lulus")

    def test_t4_status_nilai_59(self):
        self.assertEqual(status(59), "Tidak lulus")

    def test_t5_nilai_tertinggi(self):
        self.assertEqual(nilai_tertinggi([80, 60, 90, 70]), 90)

    def test_t6_nilai_tertinggi_semua_negatif(self):
        self.assertEqual(nilai_tertinggi([-8, -2, -5]), -2)


if __name__ == "__main__":
    unittest.main()