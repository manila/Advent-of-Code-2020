raw_data = []
with open("data.txt") as lines:
    for line in lines:
        raw_data.append(line.rstrip())

parsed_data = []
for line in raw_data:
    parsed_data.append(line.split())
    parsed_data[-1][0] = [int(num)-1 for num in line.split()[0].split("-")]
    parsed_data[-1][1] = parsed_data[-1][1][0]

proper_passwords = 0
for line in parsed_data:
    first_index, second_index = line[0][0],line[0][1]
    password = line[2]
    char = line[1]
    if (password[first_index] == char) or (password[second_index] == char):
        if not ((password[first_index] == char) and (password[second_index] == char)):
            proper_passwords+=1

print(proper_passwords)
