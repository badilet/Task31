# Напишите функцию которая подсчитает количество строк, слов и букв в текстовом файле.
def counter():
    text = input("Enter a large text: ")
    print("Number of lines: ", len(text.split('.')))
    print("Number of words: ", len(text.split())+1)
    print("Number of letters: ", len(text))


counter()
