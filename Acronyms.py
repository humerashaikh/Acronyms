user_input = str(input("Enter a Phrase: "))
text = user_input.split()
print(text)
a = " "
for phrase  in text:
    a = a+str(phrase[0]).upper()
print(f'Acronyms of {text} is {a}')
