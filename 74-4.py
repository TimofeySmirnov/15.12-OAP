stroka = input()
count = 0
for i in stroka:
    if i == '*' or i == ';' or i == ':':
        count += 1

print(count)
        