def save_game(current_level, tries_left):
    '''
        Saves game state to save_file.sv

        :param: current_level str
        :param: tries_left str
    '''
    savefile = open("/home/marek/Documents/Python projects/Portfolio/Number guessing game/save_file.sv", "w")
    savefile.write(f"{current_level}#{tries_left}")
    print("SAVING GAME...")
    savefile.close()

def load_game():
    '''
        Loads game state from save_file.sv

        :returns: int
    '''
    savefile = open("/home/marek/Documents/Python projects/Portfolio/Number guessing game/save_file.sv", "r")
    output = savefile.read()
    print("LOADING GAME...")
    output_list_raw = output.split("#")
    output_list = [int(output_list_raw[0]), int(output_list_raw[1])]
    savefile.close()
    return output_list
