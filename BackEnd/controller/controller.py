from prints import print_server

from BackEnd.model.model import Model
from BackEnd.view.view import View


class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        
        self.update_view()
        
    def process_request(self, path: str, data: str) -> None:
        if path == 'get_motd':
            pass
        elif path == 'set_motd':
            if data:
                self.model.motd = data
                print_server(f"Controller updated Model's motd to `{data}`")
        else:
            raise ValueError('Unsupported argument')
        print_server(f'Updating view from: `{self.view.get_view()}`')
        self.update_view()
        print_server(f'View updated to `{self.view.get_view()}`')
        
        
    def update_view(self) -> None:
        self.view.view_data = {'motd': self.model.motd}