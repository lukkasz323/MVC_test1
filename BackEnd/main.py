import http.server
from controller.controller import Controller
from model.model import Model
from view.view import View


def main():
    print('[BackEnd]')
    
    server = http.server.HTTPServer(server_address=('', 0), RequestHandlerClass=http.server.SimpleHTTPRequestHandler)
    print(server.get_request())
    
    controller = Controller(Model(), View())


if __name__ == '__main__':
    main()