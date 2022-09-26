def time2millis(days, hours, minutes, seconds):
    millis = days * 24 * 60 * 60 * 1000
    millis += hours * 60 * 60 * 1000
    millis += minutes * 60 * 1000
    millis += seconds * 1000
    return millis

print(time2millis(0, 1, 20, 3))
