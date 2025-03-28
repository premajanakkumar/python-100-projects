with open('example.txt','r') as file:
    text = file.read()

words = text.split()
reversed_list = []
for word in words:
    reversed_word = word[::-1]
    reversed_list.append(reversed_word)
reversed_string = " ".join(reversed_list)
with open('example-reversed.txt','w') as f1:
    f1.write(reversed_string)