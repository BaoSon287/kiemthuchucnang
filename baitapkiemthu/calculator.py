def validate_score(score):
    # phải là số
    if not isinstance(score, (int, float)):
        return False

    # trong khoảng 0–9
    if score < 0 or score > 9:
        return False

    # phải là bội của 0.5
    if (score * 2) % 1 != 0:
        return False

    return True


def round_band(score):
    integer_part = int(score)
    decimal_part = score - integer_part

    if decimal_part < 0.25:
        return integer_part
    elif decimal_part < 0.75:
        return integer_part + 0.5
    else:
        return integer_part + 1.0


def calculate_overall(l, r, w, s):
    scores = [l, r, w, s]
    i = 0
    while i < len(scores):  
        s = scores[i]
    
        if not validate_score(s):
           return "Invalid input"
        i += 1

    avg = sum(scores) / 4
    return round_band(avg)