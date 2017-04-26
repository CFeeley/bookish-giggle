#!/usr/bin/python3
import FTP_Library
import os


def getserver_address():
    print("Enter the FTP server's url you want to connect to.")
    SERVER = input()
    return SERVER

def getserver_username():
    print("Enter the FTP's username.")
    USERNAME = input()
    return USERNAME

def getserver_password():
    print("Enter the FTP's password.")
    PASSWORD = input()
    return PASSWORD

def getfile_upload():
    while True:
        try:
            fileDir = os.path.dirname(os.path.realpath('__file__'))
            file_location = int(input('Where is the file located? If in current folder answer 1, if it is in a folder within the current folder answer 2, if it is in the parent folder of the current folder answer 3, if it is in a sibling folder answer 4.'))
            # For accessing the file in the same folder
            if file_location == 1:
                while True:
                    try:
                        chosen_file = input('What is the name of the file you want to upload')
                        f = open(chosen_file, 'r')
                    except IOError:
                        print('Could not locate file. Please type the full file name.')
                        continue
                    else:
                        f.close()
                        break
                return chosen_file
            # For accessing the file in a folder contained in the current folder
            elif file_location == 2:
                while True:
                    try:
                        folder_name = input('What is the exact name of the folder')
                        chosen_file = input('What is the name of the file you want to upload')
                        chosen_file = os.path.join(fileDir, ('%s/' % folder_name) + chosen_file)
                        f = open(chosen_file, 'r')
                    except IOError:
                        print('Could not locate file. Please type the full folder name and file name.')
                        continue
                    else:
                        f.close()
                        break
                return chosen_file
            # For accessing the file in the parent folder of the current folder
            elif file_location == 3:
                while True:
                    try:
                        chosen_file = input('What is the name of the file you want to upload')
                        chosen_file = os.path.join(fileDir, '../' + chosen_file)
                        f = open(chosen_file, 'r')
                    except IOError:
                        print('Could not locate file. Please type the full folder name and file name.')
                        continue
                    else:
                        f.close()
                        break
                return chosen_file
            # For accessing the file inside a sibling folder.
            elif file_location == 4:
                while True:
                    try:
                        sibling_foldername = input('What is the exact sibling folders name?')
                        chosen_file = input('What is the name of the file you want to upload')
                        chosen_file = os.path.join(fileDir, ('../%s/' % sibling_foldername) + chosen_file)
                        chosen_file = os.path.abspath(os.path.realpath(chosen_file))
                        f = open(chosen_file, 'r')
                    except IOError:
                        print('Could not locate file. Please type the full folder name and file name.')
                        continue
                    else:
                        f.close()
                        break
                return chosen_file
            elif file_location > 4:
                print("Incorrect value entered.")
                quit()
            elif file_location < 1:
                print("Incorrect value entered.")
                quit()
            else:
                print('Could not locate file. Please type the full folder name and file name.')
        except ValueError:
            print('I dont understand that.')
        else:
            break



def getfile_pull():
    filename = input('What is the full file name you want to pull?')
    return filename

def getfile_delete():
    filename = input('What is the file you want to delete named?')
    return filename

def main():
        FTP_Library.fileUpload(getfile_upload(), getserver_address(), getserver_username(), getserver_password())
        # FTP_Library.fileDelete(getfile_delete(), getserver_address(), getserver_username(), getserver_password())
        FTP_Library.filePull(getfile_pull(), getserver_address(), getserver_username(), getserver_password())

main()
