def is_leap(num):
    return num % 4 == 0 and (num % 400 == 0 or num % 100 != 0)


year = int(input())
print(str(is_leap(year)))

