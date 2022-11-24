from prints import print_client

class Client:
    def __init__(self) -> None:
        pass
    
    
    def connect(self, server) -> None:
        self.handle_request(server, 'get_motd', '')
        while True:  
            data = input('Update MOTD: ')
            self.handle_request(server, 'set_motd', data)
        
        
    def handle_request(self, server, path: str, data) -> None:
        response = server.request(path, data)
        print_client(response)