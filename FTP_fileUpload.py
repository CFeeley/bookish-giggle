#!/usr/bin/python3
from ftplib import FTP
import os

def fileUpload(filename):
    ftp = FTP("server")
    ftp.login("username", "pass")
    ftp.cwd('/data/')
    #ftp.retrlines('LIST')
    filehandle = open(filename, 'rb')
    ftp.storlines('STOR test.txt', filehandle)
    filehandle.close()
    ftp.quit()

fileDir = os.path.dirname(os.path.realpath('__file__'))

#For accessing the file in the same folder
filename = "test.txt"

#For accessing the file in a folder contained in the current folder
#filename = os.path.join(fileDir, 'test_folder/test.txt')

#For accessing the file in the parent folder of the current folder
#filename = os.path.join(fileDir, '../same.txt')
#readFile(filename)

#For accessing the file inside a sibling folder.
#filename = os.path.join(fileDir, '../sibling_test_folder/test.txt')
#filename = os.path.abspath(os.path.realpath(filename))

fileUpload(filename)