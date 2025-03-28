import os
from datetime import datetime

directory = 'files'
filenames = os.listdir(directory)
for filename in filenames: 
    filepath = os.path.join(directory,filename)
    with open(filepath,'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        day = datetime.now().strftime('%A')
        
    new_file_name = f'{filename[:1]}.txt'
    new_file_path = os.path.join(directory,new_file_name)
    os.rename(filepath,new_file_path) 