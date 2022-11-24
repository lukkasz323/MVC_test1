from prints import print_server
from BackEnd.controller.controller import Controller
from BackEnd.model.model import Model
from BackEnd.view.view import View


class Server:
    def __init__(self) -> None:
        self.model = Model()
        self.view = View()
        self.controller = Controller(self.model, self.view)
        
    def request(self, path: str, data: str):
        print_server(f'Processing request of path `{path}` and data `{data}`.')
        self.controller.process_request(path, data)
        return self.view.get_view()