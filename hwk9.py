# https://www.geeksforgeeks.org/python/python-convert-list-characters-string/

import csv     

def greedy1(map:dict) -> dict:
    """ Generates a color mapping given a map/graph in the form of a dictionary
    
    """
    colors_used = {1}  # Track the colors used
    current_color = 1  # Track the most recent color added
    color_mapping = {} # Dictionary of mapping to return

    # Iterate through states
    for key in map.keys():
        print(key)
        # Put neighbor colors into a set
        neighbor_colors = set()
        # Iterate through neighbors
        for n in map[key]['Neighbors']:
            # If the neighbors is colored (it's in color mapping), Add the color to the set
            if n in color_mapping.keys():
                neighbor_colors.add(color_mapping[n])
        # Take set difference of neighbor colors and colors used
        print(f'colors_used : {colors_used}')
        print(f'neighbor_colors : {neighbor_colors}')
        available_colors = colors_used - neighbor_colors
        print(available_colors)
        # If colors_used == neighbor_colors, Add a new color
        if available_colors == set():
            current_color += 1
            colors_used.add(current_color)
            color_mapping[key] = current_color
        # Else, use the first item in available colors
        else:
            color_mapping[key] = list(available_colors)[0]
    return color_mapping

def as_list(neighbors: str) -> list :
    """ Parse neighbors string into a list of strings
    """
    # Create an array to store neighbors
    slots = 1
    for i in neighbors:
        if i == ',':
            slots += 1
    neighbors_arr = [0] * slots
    # Turn list of chars into full strings
    word = ''
    index = 0
    for i in neighbors:
        if not i == ',' and not i == ' ':
            word += i
        if i == ',':
            neighbors_arr[index] = word
            index += 1
            word = ''
    neighbors_arr[index] = word
    return neighbors_arr

def main():
    # Turn csv into a dictionary
    map = dict()
    with open('color-US-states.csv') as csv_file:    
        csv_reader = csv.reader(csv_file, delimiter=',')
        header = csv_reader.__next__()
        for row in csv_reader:
            key = row[0]
            map[key] = {
                        'Neighbors' : as_list(row[1]),
                        'Num_n' : int(row[2])
                        }    
    # Greedy 1
    print(greedy1(map))
main()