from calculator import calculate_overall

def run_test(tc, actual, expected):
    if actual == expected:
        print(f"{tc}: PASS")
    else:
        print(f"{tc}: FAIL (Expected {expected}, Got {actual})")


def test_boundary():
    print("\n=== Boundary Value Test ===\n")

    # ===== Nominal =====
    run_test("TC01", calculate_overall(6,6,6,6), 6.0)

    # ===== Listening =====
    run_test("TC02", calculate_overall(0,6,6,6), 4.5)
    run_test("TC03", calculate_overall(0.5,6,6,6), 4.5)
    run_test("TC04", calculate_overall(8.5,6,6,6), 6.5)
    run_test("TC05", calculate_overall(9,6,6,6), 6.5)

    # ===== Reading =====
    run_test("TC06", calculate_overall(6,0,6,6), 4.5)
    run_test("TC07", calculate_overall(6,0.5,6,6), 4.5)
    run_test("TC08", calculate_overall(6,8.5,6,6), 6.5)
    run_test("TC09", calculate_overall(6,9,6,6), 6.5)

    # ===== Writing =====
    run_test("TC10", calculate_overall(6,6,0,6), 4.5)
    run_test("TC11", calculate_overall(6,6,0.5,6), 4.5)
    run_test("TC12", calculate_overall(6,6,8.5,6), 6.5)
    run_test("TC13", calculate_overall(6,6,9,6), 6.5)

    # ===== Speaking =====
    run_test("TC14", calculate_overall(6,6,6,0), 4.5)
    run_test("TC15", calculate_overall(6,6,6,0.5), 4.5)
    run_test("TC16", calculate_overall(6,6,6,8.5), 6.5)
    run_test("TC17", calculate_overall(6,6,6,9), 6.5)


if __name__ == "__main__":
    test_boundary()