#!/usr/bin/python3
import FTP_fileUpload
import FTP_fileDelete

SERVER = ""
USERNAME = ""
PASSWORD = ""
filename = ""

FTP_fileUpload.fileUpload(filename, SERVER, USERNAME, PASSWORD)
FTP_fileDelete.fileDelete(filename, SERVER, USERNAME, PASSWORD)

