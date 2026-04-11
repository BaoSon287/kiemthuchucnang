from calculator import validate_score, round_band, calculate_overall


def run_test(tc, actual, expected):
    if actual == expected:
        print(f"{tc}: PASS")
    else:
        print(f"{tc}: FAIL (Expected {expected}, Got {actual})")


def test_all_uses():
    print("\n=== All-Uses (Data Flow Testing) ===\n")

    # ===== validate_score =====
    # Bao phủ: type check, range check, step check, valid path

    run_test("TC01", validate_score(10), False)      # ngoài range (p-use)
    run_test("TC02", validate_score("A"), False)     # sai kiểu (p-use)
    run_test("TC03", validate_score(5.75), False)    # không phải bội 0.5 (c-use)
    run_test("TC04", validate_score(5.5), True)      # hợp lệ (c-use)

    # ===== round_band =====
    # Bao phủ các nhánh sử dụng biến decimal part

    run_test("TC05", round_band(5.1), 5.0)           # < 0.25
    run_test("TC06", round_band(5.6), 5.5)           # < 0.75
    run_test("TC07", round_band(5.5), 5.5)           # = 0.5 (đi nhánh giữa)
    run_test("TC08", round_band(5.9), 6.0)           # ≥ 0.75

    # ===== calculate_overall =====
    # Bao phủ DU của scores + validate + vòng lặp

    run_test("TC09", calculate_overall(4, 5, 6, 7), 5.5)
    # valid → đi qua loop → dùng score (c-use)

    run_test("TC10", calculate_overall("A", "B", "C", "D"), "Invalid input")
    # tất cả invalid → dừng sớm (p-use)

    run_test("TC11", calculate_overall("A", 5, 6, 7), "Invalid input")
    # invalid 1 phần → break giữa chừng (p-use)


if __name__ == "__main__":
    test_all_uses()