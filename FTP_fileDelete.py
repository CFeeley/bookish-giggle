#!/usr/bin/python3
from ftplib import FTP

def fileDelete(filename):
    ftp = FTP("SERVER")
    ftp.login("USERNAME", "PASSWORD")
    ftp.cwd('/data/')
    #ftp.retrlines('LIST')
    ftp.delete("filename")
    ftp.quit()

fileDelete(filename)
