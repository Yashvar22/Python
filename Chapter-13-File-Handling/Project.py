from pathlib import Path;
import os; 

def readFileandFolder():
   path=Path('')
   items=list(path.rglob('*'))
   for i,items in enumerate(items):
      print(f"{i+1}: {items}")
   
def createFile():
    try:
       readFileandFolder()
       name=input("please tell your file name:- ")
       p=Path(name)
       if not p.exists():
           with open(p,'w') as fs:
              data=input("what you want to write:-");
              fs.write(data)
 
           print(f"File created successfully")

       else:
         print("this file alread exists")

    except Exception as err:
       print(f"An err occures as {err}")


def readFile():
     try: 
         readFileandFolder();
         name=input("which file you want to read:-")
         p=Path(name);
    
         if p.exists() and p.is_file():
            with open(p,'r') as fs:
              data =fs.read();
              print(data);
       
            print("file read successfully");
    
         else:
             print("file does not exists")

     except Exception as err:
       print(f"An err occures as {err}")

def updateFile():
   try:
      readFileandFolder();
      name=input("which file you want to update:-")
      p=Path(name);
      
      if p.exists() and p.is_file():
         print("Press 1 for changing name of file:- ")
         print("Press 2 for overriding the data of your file:- ")
         print("Press 3 for appending some content in your file:- ")

         res=int(input("tell your response:- "))

         if res == 1:
            name2=input("tell your new file name:-")
            p2=Path(name2);
            p.rename(p2)

         if res == 2:
           with open(p,'w') as fs:
              data= input("tell what you want to write this will override the data:- ")
              fs.write(data)

         if res == 3:
            with open(p,'a') as fs:
              data= input("tell what you want to append:- ")
              fs.write(" " + data)       
   except Exception as err:
         print(f"an error occured as {err}")

def deleteFile():
    try:
       readFileandFolder();
       name=input("which file you want to delete:- ");
       p=Path(name)

       if p.exists() and p.is_file():
          os.remove(p);
          print("file deleted succesfullt");
       else:
          print("no such file exists")
    except Exception as err:
       print(f"An err occured as {err}")

print("pres 1 for creating a file")
print("pres 2 for reading a file")
print("pres 3 for updating a file")
print("pres 4 for deletion a file")


check=int(input("Please tell your response:- "))

if check==1:
   createFile()

if check==2:
    readFile()

if check == 3:
   updateFile()

if check== 4:
   deleteFile()