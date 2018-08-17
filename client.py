from ftplib import FTP
from sys import argv
import time
import os

# Constants for messages used
RMSG = "Input file name to retrieve"
UMSG = "Input file to updload"
CHOICE = "\nWould you like to upload a file or retrieve\n Enter (U) for upload\n Enter (R) for retrieve\n Enter (Q) to quit"
CONT = "Would you like to continue the connection\n Enter (0) for no\n Enter (1) for yes"

# Will handle calling the start functions and continue functions
def conn_loop(ftp):
    cont = 1

    while cont:
        cont = start(ftp)
        if(cont):
            cont = contDec(cont)

        
# Will determine if the user would like to continue or close the ftp connection
def contDec(cont):
    
    cont = int(input(CONT + ": "))

    while(cont != 0 and cont != 1):
        print("\nIncrrect response\n")
        time.sleep(.2)
        cont = int(input(CONT + ": "))
    if(cont == 0):
        print("\nQuitting")
    return cont

# Will handle the starting logic
def start(ftp):
    nextDecision = 1
    ans = input(CHOICE + ": ").capitalize()
    
    time.sleep(.2)
    while ans != 'R' and ans != 'U' and ans != 'Q':
        print("\nIncorrect response\n")
        time.sleep(.2)
        ans = input(CHOICE + ": ").capitalize()
    if(ans == 'R'):
        grabFile(ftp)
    elif(ans == 'U'):
        uploadFile(ftp)
    elif(ans == 'Q'):
        print("\nQuitting")
        nextDecision = 0

    return nextDecision

# Lists files in server directory and requests form user which file to be received
def grabFile(ftp):

    print("\nFiles to choose from:\n")
    ftp.retrlines('LIST')

    directory = "Files Received"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    fileName = input('\n' + RMSG + ": ")

    localFile = open(directory + "/" + fileName, 'wb')
    ftp.retrbinary('RETR ' + fileName, localFile.write, 1024)
    localFile.close()

    time.sleep(.2)
    print("\nFile received\n")

# Lists files in client directory and requests from user which file to upload
def uploadFile(ftp):

    print("\nFiles to choose from:\n")
    dirs = os.listdir("/Workspace/Coding/ftpclient")
    for file in dirs:
        print(file)
    
    fileName = input('\n' + UMSG + ": ")

    ftp.storbinary('STOR ' + fileName, open(fileName, 'rb'))

    time.sleep(.2)
    print("\nFile uploaded\n")

def main():
    IP = input("Input IP Address for connection: ")
    # Creates the FTP connection
    ftp = FTP('')
    ftp.connect(IP, 5173)

    # Connects after receiving the username and password
    username = input("Username: ")
    password = input("Password: ")
    msg = ftp.login(user=username,passwd=password)

    code = int(msg[0:3])

    print("\n" + msg)

    if(code == 230):
        conn_loop(ftp)

    ftp.quit()

if __name__ == "__main__":
    main()