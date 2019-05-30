with open ('C:\\projects\\lesson3\\referat.txt', 'r', encoding='utf-8') as referat:
    content = referat.read()
    print(len(content))

    content_word = content.split()
    print(len(content_word))

    content_sign = content.replace('.', '!')

with open('referat2.txt', 'w') as referat2:
    referat2.write(content_sign)


