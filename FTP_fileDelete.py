#!/usr/bin/python3
from ftplib import FTP

def fileDelete():
    ftp = FTP("SERVER")
    ftp.login("USERNAME", "PASSWORD")
    ftp.cwd('/data/')
    #ftp.retrlines('LIST')
    ftp.delete("test.txt")
    ftp.quit()

fileDelete()
