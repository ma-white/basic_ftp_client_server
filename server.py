from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user("Michael", "Michael7", "/Users/Mike/Documents/Workspace_Mike/FTP", perm="elradfmw")
    #authorizer.add_anonymous("/Users/Mike/Documents/Workspace_Mike/FTP", perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer(('', 5173), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()