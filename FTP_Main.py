#!/usr/bin/python3
import FTP_fileUpload
import FTP_fileDelete
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
    fileDir = os.path.dirname(os.path.realpath('__file__'))

    # For accessing the file in the same folder
    filename = "test.txt"

    # For accessing the file in a folder contained in the current folder
    # filename = os.path.join(fileDir, 'test_folder/test.txt')

    # For accessing the file in the parent folder of the current folder
    # filename = os.path.join(fileDir, '../same.txt')
    # readFile(filename)

    # For accessing the file inside a sibling folder.
    # filename = os.path.join(fileDir, '../sibling_test_folder/test.txt')
    # filename = os.path.abspath(os.path.realpath(filename))
    
    return filename


FTP_fileUpload.fileUpload(getfile_upload(), getserver_address(), getserver_username(), getserver_password())
FTP_fileDelete.fileDelete(getfile_upload(), getserver_address(), getserver_username(), getserver_password())
