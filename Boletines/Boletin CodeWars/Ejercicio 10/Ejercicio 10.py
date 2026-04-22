def get_grade(s1, s2, s3):
    promedio = (s1 + s2 + s3) / 3
    if 0 <= promedio <= 100:
        if 90 <= promedio <= 100:
            return "A"
        elif 80 <= promedio <= 90:
            return "B"
        elif 70 <= promedio <= 80:
            return "C"
        elif 60 <= promedio <= 70:
            return "D"
        elif 0 <= promedio <= 60:
            return "F"
    return None

print(get_grade(95, 90, 93))
