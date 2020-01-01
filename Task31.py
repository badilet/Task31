# Напишите функцию которая подсчитает количество строк, слов и букв в текстовом файле.

file = open("Task31.txt", "r")
data = file.read()
words = data.split()
num_lines = sum(1 for line in open('Task31.txt'))

print('Number of lines in text: ', num_lines)
print('Number of words in text: ', len(words))
print('Number of letters inn text: ', len(data))
