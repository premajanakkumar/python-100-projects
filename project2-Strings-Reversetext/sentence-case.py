with open('snowwhite.txt','r') as f1:
    text = f1.read()

#conver the the string to a list
sentences =  text.split(". ")

sentence_list = []
for sentence in sentences:
    
    sentence = sentence.capitalize()
    sentence_list.append(sentence)

capi_string = ". ".join(sentence_list)
print(capi_string)
    
with open('snowwhite-caps.txt','w') as f1:
    f1.write(capi_string)

    