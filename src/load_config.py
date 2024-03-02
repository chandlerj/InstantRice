from rich import print
import os


class systemConfig:
    """
    Class which checks for presence of configuration files for programs
    instant rice is compatible with. Additionally, loads the user's configuration
    file for instant rice.
    """
    
    i3_config = ""
    i3_lock_image = ""
    polybar_config = ""
    wallpaper_directory = ""
    rofi_config = ""
    username = ""
    rice_config = ""
    
    #instant rice configuration settings
    use_dmenu = False
    generate_i3_lock = False

    def __init__(self):
        print('[bold green]Loading configuration files')
        
        #Grab username to find configuration files
        self.username = os.getlogin()
        
        # check if config files present and make accessible to instantrice
        # if file not present do nothing. On user to initialize files
        if os.path.exists(f'/home/{self.username}/.config/i3/'):
            self.i3_config = f'/home/{self.username}/.config/i3/config'
            self.i3_lock_image = f'/home/{self.username}/.config/i3/lock.png'
        if os.path.exists(f'/home/{self.username}/.config/polybar/'):
            self.polybar_config = f'/home/{self.username}/.config/polybar/config.ini'
        if os.path.exists(f'/home/{self.username}/.config/rofi/config.rasi'):
            self.rofi_config = f'/home/{self.username}/.config/rofi/config.rasi'
        if os.path.exists(f'/home/{self.username}/.config/instantrice/'):
            self.rice_config = f'/home/{self.username}/.config/instantrice/config.rice'
            self.get_user_preferences()
        else:
            print(f'[bold red]InstantRice configuration not present.\nDrop default configuration file at /home/{self.username}/.config/InstantRice/config.rice?')
            response = input('(a)ccept (d)ecline> ')
            if response == "a":
                self.rice_config = f'/home/{self.username}/.config/instantrice/config.rice'
                self.copy_rice_config()

    def copy_rice_config(self):

        print(f'Creating instant rice configuration directory')
        os.makedirs(f'/home/{self.username}/.config/instantrice')

        with open('../data/default_config.rice') as file:
            data = file.readlines()
        with open(f'{self.rice_config}', 'w') as file:
            file.writelines(data)
    
    def get_user_preferences(self):

        with open(self.rice_config) as file:
            data = file.readlines()
        
        for i, line in enumerate(data):
            if "use_dmenu" in line:
                match = line.split(' ')
                self.use_dmenu = True if match[2] == 'True' else False
            if "generate_i3_lock" in line:
                match = line.split(' ')
                self.generate_i3_lock = True if match[2] == 'True' else False
            if "wallpaper_directory"  in line:
                match = line.split(' ')
                self.wallpaper_directory = match[2]
