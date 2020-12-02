raw_data = []
with open("data.txt") as lines:
    for line in lines:
        raw_data.append(line.rstrip())

parsed_data = []
for line in raw_data:
    parsed_data.append(line.split())
    parsed_data[-1][0] = [int(num) for num in line.split()[0].split("-")]
    parsed_data[-1][1] = parsed_data[-1][1][0]

proper_passwords = 0
for line in parsed_data:
    min_char, max_char = line[0][0],line[0][1]
    password = line[2]
    char = line[1]
    char_count = password.count(char)
    if min_char <= char_count <= max_char:
        proper_passwords+=1
        
print(proper_passwords)
