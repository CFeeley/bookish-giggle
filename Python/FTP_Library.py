#!/usr/bin/python3

from ftplib import FTP

def fileUpload(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    ftp.cwd('/data/')
    # opening file to upload
    filehandle = open(filename, 'rb')
    # storlines stores the file
    ftp.storlines('STOR test.txt', filehandle)
    # closes file
    filehandle.close()
    # shows contents in current directory
    ftp.retrlines('LIST')
    # closes connection to ftp
    ftp.quit()

def fileDelete(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    ftp.cwd('/data/')
    # delete the specified filename
    ftp.delete(filename)
    # shows contents in current directory
    ftp.retrlines('LIST')
    # closes connection to ftp
    ftp.quit()

def filePull(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    ftp.cwd(file_dir())
    # opening filename to download
    with open(filename, 'wb') as f:
        # delete the specified filename
        ftp.retrbinary('RETR %s' % filename, lambda data: f.write(data))
    # shows contents in current directory
    ftp.retrlines('LIST')
    # closes connection to ftp
    ftp.quit()

def file_dir():
    file_dir = ''
    file_dir = input('Which directory is the file you want to pull in?')
    if (file_dir == 'current'):
        return '/data/'
    else:
        return file_dir