from pathlib import Path
import os

def readfileandfolder():
  path = Path('')
  items = list(path.rglob('*'))
  for i, items in enumerate(items):
    print(f"{i+1} : {items}")

def createfile():
  try:
    readfileandfolder()
    name = input("Please tell your file name:-")
    p = Path(name)
    if not p.exists() and p.is_file():
      with open(p, "w") as fs:
        data = input("What you want to write in this file: ")
        fs.write(data)

      print("Your file is created successfully!")
    else:
      print("Your file already exist")

  except Exception as err:
    print(f"An error occured: {err}")


def readfile():
  try:
    readfileandfolder()
    name = input("Which file you want to read")
    p = Path(name)
    if p.exists() and p.is_file():
      with open(p, "r") as fs:
        data = fs.read()
        print(data)

      print("Your file is read successfully!")
    else:
      print("Your file does not exist")
  except Exception as err:
    print(f"An error occured as: {err}")


def updatefile():
  try:
    readfileandfolder()
    name = input("tell which file you want to update")
    p = Path(name)
    if p.exists() and p.is_file():
      print("Press 1 for changing the name of your file:-")
      print("Press 2 for changing the content / data of your file:-")
      print("Press 3 for appending some content in your file")
      
      res = int(input("Please tell your response:-"))

      if res==1:
        name2 = input("tell your new filename:-")
        p2 = Path(name2)
        if not p2.exists():
          p.rename(p2)
          print("Your file is renamed successfully")
        else:
          print("Your file already exist")
      
      if res==2:
        with open(p, "w") as fs:
          data = input("Tell What you want to write in this file: ")
          fs.write(data)
        print("Your file is updated successfully!")

      if res==3:
        with open(p, "a") as fs:
          data = input("Tell What you want to append in this file: ")
          fs.write(data)
        print("Your file is updated successfully!")
    
  except Exception as err:
    print(f"An error occured as: {err}")


def deletefile():
  try:
    readfileandfolder()
    name = input("tell which file you want to delete")
    p = Path(name)
    if p.exists() and p.is_file():
      os.remove(p)
      # p.unlink()
      print("Your file is deleted successfully!")
    else:
      print("no such file exist")
  except Exception as err:
    print(f"An error occured as: {err}")




print("Press 1 for creating the file")
print("Press 2 for reading the file")
print("Press 3 for updating the file")
print("Press 4 for deleting the file")

check = int(input("Please tell your response:-"))

if check==1:
  createfile()

if check==2:
  readfile()

if check==3:
  updatefile()

if check==4:
  deletefile()
