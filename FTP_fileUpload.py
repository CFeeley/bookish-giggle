#!/usr/bin/python3
from ftplib import FTP

def fileUpload(filename, SERVER, USERNAME, PASSWORD):
    ftp = FTP(SERVER)
    ftp.login(USERNAME, PASSWORD)
    ftp.cwd('/data/')
    filehandle = open(filename, 'rb')
    ftp.storlines('STOR test.txt', filehandle)
    filehandle.close()
    ftp.retrlines('LIST')
    ftp.quit()
