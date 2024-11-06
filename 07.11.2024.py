def task_206():
    exp = 64**150 + 4**300 - 32
    
    count_7 = 0
    while exp != 0:
        if exp % 8 == 7:
            count_7 += 1
        exp //= 8
    
    return count_7

def task_210():
    res = 36**10 + 6**25 - 15
    
    count_0 = 0
    while res != 0:
        if res % 6 == 0:
            count_0 += 1
        res //= 6
    return count_0

def task_216():
    bases = [4, 5, 6, 7, 8, 9, 10]
    for base in bases:
        if (
            int("12", base)
            * int("13", base)
        ) == int("211", base):
            return base

# answer: 198
print("№ 206:", task_206())

# answer: 5
print("№ 210:", task_210())

# answer: 5
print("№ 216:", task_216())
