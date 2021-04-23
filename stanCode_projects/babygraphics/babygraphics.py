"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + ((width-GRAPH_MARGIN_SIZE*2)/len(YEARS))*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # UPPER LINE
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # LOWER LINE
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT- GRAPH_MARGIN_SIZE)
    # DRAW EVERY VERTICAL LINE AND YEAR.
    for x in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, x), GRAPH_MARGIN_SIZE, get_x_coordinate(CANVAS_WIDTH, x), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE/2)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, x)+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[x], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # COUNT HOW MANY NAMES USER TYPE IN IT.
    # IF THERE'S MISSING DATA, ASSUMING THEIR RANKS ARE OUT OF 1000.
    # IF THE DATA ARE ALL COMPLETED, FIND THEIR RANKS IN DICT.
    # LAST BUT NOT LEAST, DRAW THE LINE WITH THEIR YEARS AND RANKS.
    len_lookup_name = len(lookup_names)
    for i in range(len_lookup_name):
        for j in range(len(YEARS)-1):
            name = lookup_names[i]
            if str(YEARS[j]) not in name_data[name]:
                # can't work
                # name_data[name] = str(YEARS[j])
                # name[str(YEARS[j])] = 1000
                # can work
                name_data[name][str(YEARS[j])] = 1000
                rank = name_data[name][str(YEARS[j])]
                # name_data[name] = {str(YEARS[j]): 1000}
                # rank = name_data[name][str(YEARS[j])]
            else:
                rank = name_data[name][str(YEARS[j])]
            if str(YEARS[j+1]) not in name_data[name]:
                # name_data[name] = str(YEARS[j+1])
                # name[str(YEARS[j+1])] = 1000
                name_data[name][str(YEARS[j+1])] = 1000
                rank_next = name_data[name][str(YEARS[j+1])]
                # name_data[name] = {str(YEARS[j+1]): 1000}
                # rank_next = name_data[name][str(YEARS[j+1])]
            # IF RANKS BEYOND 1000, ASSUMING THEIR ARE 1000.
            else:
                rank_next = name_data[name][str(YEARS[j+1])]
            if int(rank) > 1000:
                rank = 1000
            if int(rank_next) > 1000:
                rank_next = 1000
            canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j), GRAPH_MARGIN_SIZE+int(rank)*(56/100),
                               get_x_coordinate(CANVAS_WIDTH, j+1), GRAPH_MARGIN_SIZE+int(rank_next)*56/100, width=LINE_WIDTH, fill=COLORS[i])
            if rank == 1000:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j), GRAPH_MARGIN_SIZE + int(rank) * (56 / 100),
                                   text=f"{name}: * ", anchor=tkinter.SW)
                if (YEARS[j+1]) == 2010:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1), GRAPH_MARGIN_SIZE + int(rank_next) * (56 / 100),
                                       text=f"{name}: * ", anchor=tkinter.SW)
            else:
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j), GRAPH_MARGIN_SIZE+int(rank)*(56/100),
                                   text=f'{name}: {rank}', anchor=tkinter.SW)
                if (YEARS[j+1]) == 2010:
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j+1), GRAPH_MARGIN_SIZE + int(rank_next) * (56 / 100),
                                       text=f"{name}: {rank_next} ", anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
