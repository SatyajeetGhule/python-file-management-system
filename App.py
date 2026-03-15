import os

# Create File :
def Create_File(fileName):
    try:
        with open(fileName, 'x') as file:
            print(f" File '{fileName}' Succesfully Created...")
    except FileExistsError:
        print("Error : File is already exist in that directory")
    except Exception as e:
        print("Error : ",e)


# Show all Files:
def viewAllFiles(path):
    try:
        files = os.listdir(path)
        if not files:
            print("Error : Directory is empty")
            return
        for file in files:
            print(file)
    except FileNotFoundError:
        print("Error : Path Not Found!")


# Read File :
def read_File(fileName):
    try:
        with open(fileName, 'r') as file:
            content = file.read()
            print(f"\nContent of '{fileName}':\n")
            print(content)
    except FileNotFoundError:
        print("Error : File Not Fond!")
    except Exception as e:
        print("Error : ",e)


# Edit File :
def editFile(fileName):
    try:
        with open(fileName, 'a') as file:
            content = input("Enter the the Data : ")
            file.write(content + "\n")
            print("Data Succesfully Added in that file.")
    except FileNotFoundError:
        print("Error : File Not Fond!")
    except Exception as e:
        print("Error : ",e)

# Delete File :
def deleteFile(fileName):
    try:
        os.remove(fileName)
        print("File Deleted Succesfully")
    except FileNotFoundError:
            print("Error : File Not Exist in that Directory")
    except Exception as e:
        print("Eroor : ",e)


# Show Menu :
def menu():
    print("---------------------------------------------------")
    print("----------- File MAnagement System ----------------")
    print("---------------------------------------------------")
    print()
    print("1 : Create File")
    print("2 : View All File")
    print("3 : Read File")
    print("4 : Delete File")
    print("5 : Edit File")
    print("6 : Exit File")

while True:
    menu()
    choice = input("Enter your Choice(1-6) : ")

    if choice == '1':
        Create_File(input("Enter the Filr Name for Create File: "))
    elif choice == '2':
        viewAllFiles(input("Enter the path of File for view all Files:"))
    elif choice == '3':
        read_File(input("Enter the File Name for Read File: "))
    elif choice == '4':
        deleteFile(input("Enter the File Name for Delete File:"))
    elif choice == '5':
        editFile(input("Enter the file name for Edit File : "))
    elif choice == '6':
        print("App Closing...\nThank you..")
        break
    else:
        print("Invalid Input!")
