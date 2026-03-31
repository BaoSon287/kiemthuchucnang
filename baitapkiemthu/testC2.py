import unittest
from calculator import validate_score, round_band, calculate_overall


class TestC2(unittest.TestCase):

    # ===== validate_score =====
    def test_validate_score_invalid_type(self):
        # không phải số → False
        self.assertFalse(validate_score("A"))

    def test_validate_score_out_of_range(self):
        # ngoài khoảng 0–9 → False
        self.assertFalse(validate_score(10))

    def test_validate_score_not_multiple_0_5(self):
        # không phải bội 0.5 → False
        self.assertFalse(validate_score(2.7))

    def test_validate_score_valid(self):
        # hợp lệ → True
        self.assertTrue(validate_score(6.5))


    # ===== round_band =====
    def test_round_band_down(self):
        # < 0.25 → làm tròn xuống
        self.assertEqual(round_band(6.15), 6)

    def test_round_band_half(self):
        # 0.25 ≤ x < 0.75 → .5
        self.assertEqual(round_band(7.64), 7.5)

    def test_round_band_up(self):
        # ≥ 0.75 → lên 1
        self.assertEqual(round_band(5.93), 6.0)


    # ===== calculate_overall =====
    def test_calculate_overall_invalid(self):
        # có phần tử invalid → return sớm
        self.assertEqual(calculate_overall("A", 5, 6, 7), "Invalid input")

    def test_calculate_overall_valid(self):
        # tất cả hợp lệ → tính avg và làm tròn
        # avg = (4+5+6+7)/4 = 5.5 → round_band = 5.5
        self.assertEqual(calculate_overall(4, 5, 6, 7), 5.5)


if __name__ == '__main__':
    unittest.main()