from rich.console import Console
from rich.theme import Theme
import time

console = Console(color_system="truecolor")
console.rule("[bold red]Make America Great Again!")
console.print('[bold blue]BY BUILDING A FUCKING WALL[/bold blue]', justify='center') 
print(console._detect_color_system())

with console.status("Building...", spinner='aesthetic'):
    pass

theme = Theme({

}
)

class Main():
    
    def __init__(self, console_color, meters, building):
        self.original_color = console_color
        self.console_color = console_color
        self.meters = meters
        self.building = building
    
    def built_so_far(self):
        """shows how much you've built when you exit the program"""
        self.console_color = self.original_color
        self.building = False
        console.print(f'\nBuilt so far: {self.meters}')

    def building_wall(self):
        console.print('Building Wall, press CTRL+C to stop...')
        time.sleep(1)
        