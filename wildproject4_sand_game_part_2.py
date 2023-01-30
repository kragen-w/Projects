"""
    This program allows the user to click and hold their mouse on the dudraw canvas, and if they click 
    the "s" key, sand falls randomly around the curser, and will continue falling until it hits the bottom 
    of the canvas or the top of a sand pile. If the user clicks "r", for rain, then rain will fall in a similar 
    fashion. If the user clicks "f," for floor, then the user can draw lines that both the water and sand will 
    interact with. The sand will fall in dunes when it falls above water, and act as wet sand when below water. 
    When q is typed, the program ends. The user can costomize how large the rain drops and sand chunks are that fall,
    and how far spread apart they are from the curser. 
    Filename: wildproject3_sand_game_part_1.py
    Author: Kragen Wild
    Date: 1-22-23
    Course: Programming II
    Assignment: Project SandGame - Part 1
    Collaborators: nada
    Internet Source: nada
"""
from random import randint
import dudraw


#this sets the canvas scale and size of the 2d list
size = 101

dudraw.set_x_scale(0,size-1)
dudraw.set_y_scale(0,size-1)
dudraw.set_canvas_size(800,800)


#i got confused on what number was what, so i made it so empty pixels are 0, sand is 1, floors are 2, and water is 3
empty = 0
sand = 1
floor = 2
water = 3
#these are the buffers for when placing sand and water
x_buffer = 50
y_buffer = 1
#this sets the thickness of the floor when drawn
floor_thick = 1
sand_thick = 2
water_thick = 2

#creates and returns 2d list
def create_list(size: int):
    """
    This function creates a 2d list filled with "0"s that has the same number of rows and colums as the size variable
    parameters: size: int
    return: The aformentioned 2d list
    """
    #2d list is made
    dlist = []
    #nested for loop to append "0"s for all values of 2d list, which size has been predetermined my the size variable
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        dlist.append(row)
    return dlist

#takes the list and draws it
def draw_list(dlist: list)->None:
    """
    This function transverses a 2d list and draws sand, water, or floor depending on the value being looked at
    in the 2d list
    parameters: dlist: list
    return: None
    """
    #nested for loop that looks at every value in the 2d list
    for i in range(len(dlist)):
        for j in range(len(dlist[i])):
            #if the current value being looked at is sand, then the color changes to a sand color
            if dlist[i][j] == sand:
                dudraw.set_pen_color_rgb(235,203,163)
            #if the current value being looked at is floor, then the color changes to a black color    
            if dlist[i][j] == floor:
                dudraw.set_pen_color_rgb(0,0,0)
            #if the current value being looked at is water, then the color changes to a water color    
            if dlist[i][j] == water:
                dudraw.set_pen_color_rgb(98,189,201)
            #if the current value being looked at isn't empty, then a square with 1/2 the radius of the canvas size is
            #drawn at the coordinate of the 2d list
            if dlist[i][j] != empty:
                dudraw.filled_square(j -1/2 ,size-i -1/2 ,1/2)  

#updates the presence of sand
def sand_drawer(dlist: list, sand_thick)->None:
    """
    This function draws sand in random areas around the curser when the mouse is pressed
    parameters: dlist: list
    return: None
    """
    #if the mouse is pressed:
    if dudraw.mouse_is_pressed():
        #the x and y position of the mouse press is stored in variables
        mouse_x = int(dudraw.mouse_x())
        mouse_y = int(dudraw.mouse_y())
        #the actual position of where the sand will be drawn is changed by a random buffer
        #this buffer will change the x and y position slightly
        #the y position is size - mouse_y because the coordinates of duddraw are typical x and y, 
        #but the loop that reads the 2d list reads from top to bottom, so the y axis is inverted
        x_position = mouse_x + randint(-x_buffer,x_buffer)
        y_position = size-mouse_y + randint(-y_buffer,y_buffer)
        #if the y position is within the canvas
        if y_position < size and y_position > 0:
            #if the x position is within the canvas
            if x_position < size and x_position > 0:
                #if there isnt already sand or water there
                if dlist[y_position][x_position] != floor and dlist[y_position][x_position] != water:
                    #this loops creates a square around the cursur, and fills changes each value in that square to floor
                    #this sets up how many rows are in the square
                    for i in range(-sand_thick,sand_thick+1):
                        #this is how many colums are in the square
                        for j in range(-sand_thick,sand_thick+1):
                            #in order for any part of the square to be drawn, it cannot be outside the canvas
                            if y_position + i < size and y_position + i > 0 and x_position + j < size and x_position + j > 0:
                                #the position of that spot in the 2d list is changed to sand
                                dlist[y_position + i][x_position + j] = sand

#updates the presence of floor
def floor_drawer(dlist: list, floor_thick: int)->None:
    """
    This function draws floor in a square around the curser, who's radius
    is determined by the floor_thick variable, around the curser when the mouse is pressed
    parameters: dlist: list, floor_thick: int
    return: None
    """
    #if the mouse is pressed:
    if dudraw.mouse_is_pressed():
        #the x and y position of the mouse press is stored in variables
        mouse_x = int(dudraw.mouse_x())
        mouse_y = int(dudraw.mouse_y())
        #the y position is size - mouse_y because the coordinates of duddraw are typical x and y, 
        #but the loop that reads the 2d list reads from top to bottom, so the y axis is inverted
        x_position = mouse_x
        y_position = size-mouse_y
        if y_position < size and y_position > 0:
            #if the x position is within the canvas
            if x_position < size and x_position > 0:
                #if there isnt already sand or water there
                if dlist[y_position][x_position] != sand and dlist[y_position][x_position] != water:
                    #this loops creates a square around the cursur, and fills changes each value in that square to floor
                    #this sets up how many rows are in the square
                    for i in range(-floor_thick,floor_thick+1):
                        #this is how many colums are in the square
                        for j in range(-floor_thick,floor_thick+1):
                            #in order for any part of the square to be drawn, it cannot be outside the canvas
                            if y_position + i < size and y_position + i > 0 and x_position + j < size and x_position + j > 0:
                                #the position of that spot in the 2d list is changed to sand
                                dlist[y_position + i][x_position + j] = floor

#updates the presence of water
def water_drawer(dlist: list, water_thick)->None:
    """
    This function draws water in random areas around the curser when the mouse is pressed
    parameters: dlist: list
    return: None
    """
    #if the mouse is pressed:
    if dudraw.mouse_is_pressed():
        #the x and y position of the mouse press is stored in variables
        mouse_x = int(dudraw.mouse_x())
        mouse_y = int(dudraw.mouse_y())
        #the actual position of where the sand will be drawn is changed by a random buffer
        #this buffer will change the x and y position slightly
        #the y position is size - mouse_y because the coordinates of duddraw are typical x and y, 
        #but the loop that reads the 2d list reads from top to bottom, so the y axis is inverted
        x_position = mouse_x + randint(-x_buffer,x_buffer)
        y_position = size-mouse_y + randint(-y_buffer,y_buffer)
        #if the y position is within the canvas
        if y_position < size and y_position > 0:
            #if the x position is within the canvas
            if x_position < size and x_position > 0:
                #if there isnt already sand or water there
                if dlist[y_position][x_position] != floor and dlist[y_position][x_position] != sand:
                    #this loops creates a square around the cursur, and fills changes each value in that square to floor
                    #this sets up how many rows are in the square
                    for i in range(-water_thick,water_thick+1):
                        #this is how many colums are in the square
                        for j in range(-water_thick,water_thick+1):
                            #in order for any part of the square to be drawn, it cannot be outside the canvas
                            if y_position + i < size and y_position + i > 0 and x_position + j < size and x_position + j > 0:
                                #the position of that spot in the 2d list is changed to sand
                                dlist[y_position + i][x_position + j] = water

#the gravity function, which allows blocks to fall straight down or diaginally
def gravity(dlist: list)->None:
    """
    This function identifies floor and sand on the 2d list and makes them fall either stright down or diagonally
    parameters: dlist: list
    return: None
    """
    #allows blocks to fall straight down, and takes
    def straight_down(row, colum, material, undernieth, dlist)->None:
        """
        This makes the material variable fall straight down, and what ever is the underneith variable switches spots with it
        parameters: row: int, colum: int, material: int, underneith: int, dlist: list
        return: None
        """
        #if the current position of the dlist is the specified material, and the block undernieth is also
        #the specified material, then those two materials switch
        if dlist[row][colum] == material and dlist[row + 1][colum] == undernieth:
            dlist[row + 1][colum] = material
            dlist[row][colum] = undernieth
         
    def diagonally_right(row, colum, material, dlist)->None:
        """
        This makes the material variable diagonally to the right, and what ever is variable is diagonally to the rightswitches spots with it
        parameters: row: int, colum: int, material: int, dlist: list
        return: None
        """
        #if the block to the right and diagonal right to the specified material is another specified material
        if dlist[row][colum] == material and dlist[row + 1][colum] != empty and dlist[row + 1][colum + 1]== empty and dlist[row][colum + 1]==empty:
            #then those materials switch
            dlist[row][colum] = empty
            dlist[row + 1][colum + 1] = material

    def diagonally_left(row, colum, material, dlist)->None:
        """
        This makes the material variable diagonally to the left, and what ever is variable is diagonally to the left switches spots with it
        parameters: row: int, colum: int, material: int, dlist: list
        return: None
        """
        #if the block to the left and diagonal left to the specified material is another specified material
        if dlist[row][colum] == material and dlist[row + 1][colum] != empty and dlist[row + 1][colum - 1]== empty and dlist[row][colum - 1]==empty:
            #then those materials switch
            dlist[row][colum] = empty
            dlist[row+ 1 ][colum - 1] = material
            return True
        else:
            return False
    #this looks at every row in the 2dlist but backwards from the end of the list
    for row in range(size,0, -1):
        #looks at every number in the colum
        for colum in range(size):
            #if the row being looked at is not the floor, which is the size of the canvas -1
            if row < size - 1:
                
                #sand will fall straight down if water and air are beneath it
                #water will fall straight down only if air is beneath it
                straight_down(row, colum, sand, empty, dlist)
                straight_down(row, colum, water, empty, dlist)
                straight_down(row, colum, sand, water, dlist)                

                #if the colum position of the number in the 2d list being looked at is not either the left or right edge of the canvas
                if colum < size-1 and colum > 1: 
                    #sand and water will fall diagonally right through air
                    diagonally_right(row, colum, sand, dlist)
                    diagonally_left(row, colum, sand, dlist)

                    diagonally_right(row, colum, water, dlist)
                    diagonally_left(row, colum, water, dlist)
                    
                    
                    x = randint(0,1)
                    if x == 0:
                        #if the current value is water and there is an empty block to the right, then the water moves to the right
                        if dlist[row][colum] == water and dlist[row][colum + 1] == empty:
                            dlist[row][colum + 1] = water
                            dlist[row][colum] = empty 
                    else:
                        #if the current value is water and there is an empty block to the left, then the water moves to the left
                        if dlist[row][colum] == water and dlist[row][colum - 1] == empty:
                            dlist[row][colum - 1] = water
                            dlist[row][colum] = empty
                #if the colum of the current value is the far right edge of the canvas, then those blocks will move diagonally left
                #if the value is water or sand
                if colum == size -1:
                    diagonally_left(row, colum, sand, dlist)
                    diagonally_left(row, colum, water, dlist)
                #if the colum of the current value is the far left edge of the canvas, then those blocks will move diagonally right
                #if the value is water or sand
                if colum == 1:
                    diagonally_right(row, colum, sand, dlist)
                    diagonally_right(row, colum, water, dlist)




#the 2list is created                   
liist = create_list(size)
#the key variable is created, which tracks what material is to be drawn
#it starts by drawing sand
key = "s"
#this is the animation while loop, and it stops when the user presses "q"
while key != "q":
    
    #this changes "key" to the key that is typed
    if dudraw.has_next_key_typed():
        key = dudraw.next_key_typed()
    #the list is drawn
    draw_list(liist)
    #if the key is s, then sand is drawn
    if key == "s":
        sand_drawer(liist, sand_thick)
    #if the key is f, then floor is drawn
    elif key == "f":
        floor_drawer(liist, floor_thick)
    #if the key is r, then rain is drawn
    elif key == "r":
        water_drawer(liist, water_thick)
    #the gravity function updates the position of the values in the list to fall down, diagonally, etc
    gravity(liist)
    #the canvas is shown for 10 milisenconds
    dudraw.show(10)
    #the canvas is cleared
    dudraw.clear()
