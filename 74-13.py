stroka = input()
opens = stroka.find('(')
closes = stroka.find(')')
if opens != -1 and closes != -1:
    result = stroka[opens+1:closes]
    print(result)
else:
    print('Скобки введи да')