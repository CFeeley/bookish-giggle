#!/usr/bin/python3
from ftplib import FTP

def fileDelete(filename, SERVER, USERNAME, PASSWORD):
    ftp = FTP(SERVER)
    ftp.login(USERNAME, PASSWORD)
    ftp.cwd('/data/')
    ftp.delete(filename)
    ftp.retrlines('LIST')
    ftp.quit()
    