print('deleting all my book library')

import os

filepath = '/users/NAME/Desktop/Books/minibooks'
dir_list = os.listdir(filepath)
count = 0
books = filepath

#naming files
print("Those are the current books in my folder", filepath, " :") 
print(dir_list)

#counting all files
for path in os.listdir(filepath):
    if os.path.isfile(os.path.join(filepath, path)):
        count += 1
print("Right now, the file count in Books folder is: ", count)

print(books)
print('getting close')

#deleting books
if os.path.isdir(books):
    i = 0
    number_of_files = len(dir_list)
    while i < number_of_files:
        file_path2 = dir_list[i]

        #print(filepath + '/' +file_path2)
        print(os.path.join(filepath, file_path2))
        os.remove(filepath + '/' + file_path2)
        
        i += 1
        
    print('gg you are getting there now!')
else:
    print('aha, try againnn')
