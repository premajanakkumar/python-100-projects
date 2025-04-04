import os
from datetime import datetime


directory = 'files'
filenames = os.listdir(directory)
print(filenames)
for filename in filenames:
    filepath = os.path.join(directory,filename)
    day = datetime.now().strftime("%A")
    with open(filepath,'r') as file:
        content = file.read()
        words = content.split()
        words_count = len(words)
        print(words_count)
    new_file_name = f'{filename[:-4]}-{words_count}-{day}.txt'
    new_file_path = os.path.join(directory,new_file_name)
    os.rename(filepath,new_file_path)
