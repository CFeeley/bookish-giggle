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
    fileDir = os.path.dirname(os.path.realpath('__file__'))

    # For accessing the file in the same folder
    #file_upload = "test.txt"

    chosen_file = input('What is the name of the file you want to upload')

    # For accessing the file in a folder contained in the current folder
    file_upload = os.path.join(fileDir, 'test_folder/' + chosen_file)

    # For accessing the file in the parent folder of the current folder
    #filename = os.path.join(fileDir, '../same.txt')
    # readFile(filename)

    # For accessing the file inside a sibling folder.
    # filename = os.path.join(fileDir, '../sibling_test_folder/test.txt')
    # filename = os.path.abspath(os.path.realpath(filename))

    return file_upload

def getfile_pull():
    filename = input('Which directory is the file you want to pull in?')
    return filename

def main():
    FTP_Library.fileUpload(getfile_upload(), getserver_address(), getserver_username(), getserver_password())
    FTP_Library.fileDelete(getfile_upload(), getserver_address(), getserver_username(), getserver_password())
    FTP_Library.filePull(getfile_pull(), getserver_address(), getserver_username(), getserver_password())
