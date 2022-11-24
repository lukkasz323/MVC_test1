class View:
    def __init__(self) -> None:
        self.view_data: dict[str, str] = dict()
    
    
    def get_view(self) -> str:
        return f"MOTD: {self.view_data['motd']}"