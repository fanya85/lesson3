# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв а в слове
word = 'Архангельск'.lower()
print(word.count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'.lower()
a = 0
for i in word:
    if i in 'аоеыие':
        a += 1
print(a)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
sen = sentence.split()
print(len(sen))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
sen = sentence.split()
for i in range(len(sen)):
    print(sen[i][0], end=" ")


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
sen = sentence.split()

#lenght_word = 0
#for i in sen:
#    lenght_word += len(i)

lenght_word = len(sentence.replace(' ', ''))

print(lenght_word / len(sen))