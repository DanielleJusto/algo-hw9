# Name:       - Danielle Justo
# Peers:      - Isabelle Wang
# References: - https://www.geeksforgeeks.org/python/python-convert-list-characters-string/
#               https://www.geeksforgeeks.org/r-language/create-a-choropleth-map-by-using-plotly-package-in-r/
#               https://statisticsglobe.com/state-name-abbreviation-r
#               https://plotly.com/python/map-configuration/

import csv  
import pandas   

def greedy1(map:dict) -> dict:
    """ Generates a color mapping given a map/graph in the form of a dictionary
    :param map: (dict) A map or in the form of a dictionary
    :return: (dict) A dictionary mapping map keys to colors
    >>> print(greedy1(map))
    {'Alabama': 1, 'Alaska': 1, 'Arizona': 1, 'Arkansas': 1, 'California': 2, 
    'Colorado': 2, 'Connecticut': 1, 'Delaware': 1, 'Florida': 2, 'Georgia': 3, 
    'Hawaii': 1, 'Idaho': 1, 'Illinois': 1, 'Indiana': 2, 'Iowa': 2, 'Kansas': 1, 
    'Kentucky': 3, 'Louisiana': 2, 'Maine': 1, 'Maryland': 2, 'Massachusetts': 2, 
    'Michigan': 3, 'Minnesota': 1, 'Mississippi': 3, 'Missouri': 4, 'Montana': 2, 
    'Nebraska': 3, 'Nevada': 3, 'New_Hampshire': 3, 'New_Jersey': 2, 'New_Mexico': 3, 
    'New_York': 3, 'North_Carolina': 1, 'North_Dakota': 3, 'Ohio': 1, 'Oklahoma': 5, 
    'Oregon': 4, 'Pennsylvania': 4, 'Rhode_Island': 4, 'South_Carolina': 2, 'South_Dakota': 4, 
    'Tennessee': 2, 'Texas': 4, 'Utah': 4, 'Vermont': 1, 'Virginia': 4, 'Washington': 2, 
    'West_Virginia': 5, 'Wisconsin': 4, 'Wyoming': 5}
    """
    colors_used = {1}  # Track the colors used
    current_color = 1  # Track the most recent color added
    color_mapping = {} # Dictionary of mapping to return
    num_ops = 0        # Keep track of operations for analysis

    # Iterate through states
    for key in map.keys():
        # Put neighbor colors into a set
        neighbor_colors = set()
        # Iterate through neighbors
        for n in map[key]['Neighbors']:
            # If the neighbors is colored (it's in color mapping), Add the color to the set
            if n in color_mapping.keys():
                neighbor_colors.add(color_mapping[n])
        # Take set difference of neighbor colors and colors used
        available_colors = colors_used - neighbor_colors
        # If colors_used == neighbor_colors, Add a new color
        if available_colors == set():
            current_color += 1
            colors_used.add(current_color)
            color_mapping[key] = current_color
        # Else, use the first item in available colors
        else:
            color_mapping[key] = list(available_colors)[0]
    return color_mapping

def greedy2(map:dict) -> dict:
    return {}

def as_list(neighbors: str) -> list :
    """ Parse neighbors string into a list of strings
    :param neighbors: (str) A list of neighboring states in the form of a string of chars
    :return: (list) The list of neighboring states parsed into a list of strings
    >>> list_as_str = 'Florida, Georgia, Mississippi, Tennessee'
    >>> print(as_list(list_as_str))
    ['Florida', 'Georgia', 'Mississippi', 'Tennessee']
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

def testHelper():
        filename = 'color-US-states.csv'
        with open(filename) as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = csv_reader.__next__()
            row = csv_reader.__next__()
        print(row[1])
        print(as_list(row[1]))

def main():
    map = dict()
    filename = 'color-US-states.csv'
    try: 
        print("Converting .csv into dictionary....")
        # Turn csv into a dictionary
        with open(filename) as csv_file:    
            csv_reader = csv.reader(csv_file, delimiter=',')
            header = csv_reader.__next__()
            for row in csv_reader:
                key = row[0]
                map[key] = {
                            'Neighbors' : as_list(row[1]),
                            'Num_n' : int(row[2])
                            }    
        print("csv successfully converted!")
        end_program = False
        while(end_program == False):
            try:
                print("Pick a greedy map coloring algorithm.\n(0) To quit the program\n(1) For greedy algorithm 1\n(2) For greedy algorithm 2")
                choice = int(input())
                if choice == 0:
                    end_program = True
                if choice == 1:
                    coloring1 = greedy1(map)
                    print(coloring1)
                    try:
                        with open("greedy1.csv", 'w') as file:
                            writer = csv.writer(file)
                            writer.writerow(coloring1.keys())
                            writer.writerow(coloring1.values())
                        print("Mapping saved to greedy1.csv.")
                    except FileNotFoundError:
                        print(f"Error writing to {file}")
                if choice == 2:
                    print(greedy2(map))
                elif not choice in [0,1,2]:
                    print("Pick a greedy map coloring algorithm.\n(0) To quit the program\n(1) For greedy algorithm 1\n(2) For greedy algorithm 2")
            except ValueError:
                print("Pick a greedy map coloring algorithm.\n(0) To quit the program\n(1) For greedy algorithm 1\n(2) For greedy algorithm 2")

    except FileNotFoundError:
        print(f"Error opening {filename}")

main()
# testHelper()