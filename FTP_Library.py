#!/usr/bin/python3
from ftplib import FTP

def fileUpload(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    while True:
        try:
            file_dir = input('Which directory do you want to upload the file to?')
            if file_dir == 'quit':
                quit()
            ftp.cwd(file_dir)
        except ftp.all_errors:
            print('Directory not found.')
        else:
            break
    # opening file to upload
    with open(filename, 'r')as f:
    # storlines stores the file
        ftp.storlines('STOR %s' % filename, f)
    # shows contents in current directory
    # ftp.retrlines('LIST')
    # closes connection to ftp
    ftp.quit()

def fileDelete(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    while True:
        try:
            file_dir = input('Which directory is the file you want to pull in?')
            if file_dir == 'quit':
                quit()
            ftp.cwd(file_dir)
        except ftp.all_errors:
            print('Directory not found.')
        else:
            break
    # delete the specified filename
    while True:
        try:
            if filename == 'quit':
                quit()
            ftp.delete(filename)
        except ftp.all_errors:
            print('File not found.')
            filename = input('Which is the file you want to delete named?')
        else:
            break
    # shows contents in current directory
    # ftp.retrlines('LIST')
    # closes connection to ftp
    ftp.quit()

def filePull(filename, SERVER, USERNAME, PASSWORD):
    # connection to server
    ftp = FTP(SERVER)
    # server login credentials
    ftp.login(USERNAME, PASSWORD)
    # change directory
    while True:
        try:
            file_dir = input('Which directory is the file you want to pull in?')
            if file_dir == 'quit':
                quit()
            ftp.cwd(file_dir)
        except ftp.all_errors:
            print('Directory not found.')
        else:
            break
    # opening filename to download
    while True:
       try:
           if filename == 'quit':
               quit()
       # retreive the specified filename
           with open(filename, 'ab') as f:
               ftp.retrbinary('RETR %s' % filename, lambda data: f.write(data))
       except ftp.all_errors:
            filename = input('File not found. What is the full file name?')
       else:
           break
    # shows contents in current directory
    #ftp.retrlines('LIST')
    # closes connection to ftp
    ftp.quit()
