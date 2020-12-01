# they call me a brute when i use force
data = []
with open("day1_data.txt") as numbers:
    for number in numbers:
        data.append(int(number.rstrip()))

for num1 in data:
    for num2 in data:
        for num3 in data:
            if num1+num2+num3==2020:
                print(num1*num2*num3)
                exit()