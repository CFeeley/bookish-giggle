#!/usr/bin/python3
import FTP_fileUpload
import FTP_fileDelete

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


filename = "test.txt"


FTP_fileUpload.fileUpload(filename, getserver_address(), getserver_username(), getserver_password())
FTP_fileDelete.fileDelete(filename, getserver_address(), getserver_username(), getserver_password())

