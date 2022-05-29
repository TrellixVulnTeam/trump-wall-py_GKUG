from rich.console import Console
import time

console = Console(color_system="truecolor")
console.rule("[bold red]Make America Great Again!")
console.print('[bold blue]BY BUILDING A FUCKING WALL[/bold blue]', justify='center') 
console.rule()

class MainClass():
    
    def __init__(self, console_color, meters, building=True):
        self.original_color = console_color
        self.console_color = console_color
        self.meters = meters
        self.building = building

    def building_wall(self):

        def built_so_far():
            """shows how much you've built when you exit the program"""
            self.console_color = self.original_color
            self.building = False
            console.print(f'\nBuilt so far: {self.meters}')

        console.print('[bold green]GIVE[/bold green] [bold white]UP[/bold white] [bold red]MEXICANS!!![/bold red]\n')
        time.sleep(1)

        c = self.console_color
        while self.building:
            try:
                console.print(f'[{c}]|¯¯¯¯[/{c}]')
                time.sleep(1)
                self.meters += 0.25
            except KeyboardInterrupt:
                built_so_far()
    
def help_menu():
        console.print('[bold black]Colors[/bold black]', justify='center')
        console.print('[bold red]-rw[/bold red] -> builds a red wall', justify='center')
        console.print('[bold blue]-bw[/bold blue] -> builds a blue wall', justify='center')
        console.print(' [bold green]-gw[/bold green] -> builds a green wall', justify='center')
        console.print('[bold magenta]-pw[/bold magenta] -> builds a pink wall', justify='center')
        console.print('none arguments -> build a white wall', justify='center')
        console.rule()

        
if __name__ == '__main__':
    console_color = 'bold white'
    try:
        if sys.argv[1] == '-rw':
            console_color = 'bold red'        
        elif sys.argv[1] == '-bw':
            console_color = 'bold blue'
        elif sys.argv[1] == '-gw':
            console_color = 'bold green'
        elif sys.argv[1] == '-pw':
            console_color = 'bold magenta'
        else:
            pass
    except:
        help_menu()

    trump = MainClass(console_color, 0.0)
    with console.status("Building Wall, press CTRL+C to stop...", spinner='aesthetic'):
        trump.building_wall()

        

        