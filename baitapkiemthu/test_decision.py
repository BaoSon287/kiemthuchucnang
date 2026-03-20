from calculator import calculate_overall


def run_test(tc, actual, expected):
    """
    Compare actual result with expected result and print test status.
    
    Parameters:
    - tc (str): Test case ID
    - actual: Result returned from function
    - expected: Expected result
    
    Output:
    - PASS if actual == expected
    - FAIL with details otherwise
    """
    if actual == expected:
        print(f"{tc}: PASS")
    else:
        print(f"{tc}: FAIL (Expected {expected}, Got {actual})")


def test_decision_table():
    """
    Decision Table Testing for IELTS overall score rounding.

    This test suite verifies the rounding logic based on the decimal
    part of the average score, according to IELTS rules:

    - Decimal < 0.25       → round down to nearest integer (.0)
    - 0.25 ≤ Decimal < 0.75 → round to .5
    - Decimal ≥ 0.75       → round up to next integer

    All input scores are valid IELTS scores (multiples of 0.5).
    """

    print("\n=== Decision Table Test (Rounding IELTS) ===\n")

    # TC01: Decimal < 0.25 → round down
    # Average = (6 + 6 + 6 + 6.5) / 4 = 6.125 → 6.0
    run_test("TC01", calculate_overall(6, 6, 6, 6.5), 6.0)

    # TC02: Decimal = 0.25 → round to .5
    # Average = 6.25 → 6.5
    run_test("TC02", calculate_overall(6, 6, 6, 7), 6.5)

    # TC03: Decimal in [0.25, 0.75) → round to .5
    # Average = 6.5 → 6.5
    run_test("TC03", calculate_overall(6, 6, 6, 8), 6.5)

    # TC04: Decimal < 0.75 → still round to .5
    # Average = 6.625 → 6.5
    run_test("TC04", calculate_overall(6, 6, 6, 8.5), 6.5)

    # TC05: Decimal = 0.75 → round up
    # Average = 6.75 → 7.0
    run_test("TC05", calculate_overall(6, 6, 6, 9), 7.0)


if __name__ == "__main__":
    test_decision_table()