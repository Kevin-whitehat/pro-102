import os
import shutil

from__dir="C:/Users/ASUS/Downloads"
to_dir="D:/downloads/downloads3"
list_of_files=os.listdir(from__dir)
print(list_of_files)
for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
   

    if extension=="":
        continue
    if extension in[".txt",".doc",".docx",".pdf"]:
        path1=from__dir+'/'+file_name
        path2=to_dir+'/'+"document_files"
        path3=to_dir+'/'+"document_files"+'/'+file_name
        print(path1)
        print(path3)

        if os.path.exists(path2):
            print("moving"+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
    elif extension in[".gif",".png",".jpg",".jpeg",".jfif"]:
        path1=from__dir+'/'+file_name
        path2=to_dir+'/'+"image_files"
        path3=to_dir+'/'+"image_files"+'/'+file_name
        print(path1)
        print(path3)

        if os.path.exists(path2):
            print("moving"+file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)