from BackEnd.server import Server
from FrontEnd.client import Client


def main():
    server = Server()
    client = Client()
    
    client.connect(server)


if __name__ == '__main__':
    main()