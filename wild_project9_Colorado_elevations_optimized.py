"""
A program takes a bunch of elevation data from a file, reads it, puts it into a 2d string that
has each elevation value in it's proper location, determines a grayscale value for every elevation (higher = more
white, lower = more black), and then draws a pixel with that color in order to create a topigraphical map of Colorado.
and, zoe helped :). once the map is drawn, anytime the user clicks on a location on the map, the elevaton at that point is displayed,
and if the user clicks any key, the program ends

File Name: wild_project9_Colorado_elevations_better.py
Date: 11/14/22
Course: COMP1351
Assignment: Project 9
Collaborators: None
Internet Sources: None
"""


import dudraw

#creates an empty list that will eventually hold the values in a 2d list 
everything = []
#opens the file thats in the same folder as the python file
with open(f"projects/prog_9/CO_elevations_feet.txt", "r") as a_file:
    #reads the file one line at a time, and repeats following code for each line
    for line in a_file:
        #creates a variable row, and saves the heights in list form, split by spaces
        row = line.strip().split(" ")
        #the "everything" list made before the file was opened takes each row as a value,
        # and because each row is a list, "everything" becomes a list of lists, or a 2d list 
        everything.append(row)
print(f"{everything} <- all the data")

#this sets up the inital value of the maximum value in the entire 2d list, which has every height value
max = 0
#this loop repeats for every row in the 2d list
for i in range(len(everything)):
    #this loop repeats for every value in each row
    for j in range(len(everything[i])):
        #this checks each height in each row, and if the value of the specific height being checked is 
        # bigger max, that height value becomes the new max 
        if int(everything[i][j]) > int(max):
            max = everything[i][j]

#prints the max
print(f"The max height is {max} feet.")

#this sets the x scale of the canvas to be the same as the length of each row in the 2d list (760)
dudraw.set_x_scale(0,len(everything[0]))
#this sets the y scale of the canvas to be the same as the number of rows in the 2d list (560)
dudraw.set_y_scale(0,len(everything))
#this makes it so the size of the canvas lines up with the amount of pixels in the x and y scale
dudraw.set_canvas_size(760,560)
#this is the bool that will be set to false if a key is typed, ending the while loop
proceed = True
#this sets the variable that will become the elevation at the location of the mouse click
elevation = ""
#this loop repeats until a key is pressed, setting proceed to False



for i in range(len(everything)):
            #this loop repeats for every value in each row
            for j in range(len(everything[i])):
                #this line is a little complicated.
                # it sets the color of each height before it is drawn
                # it does this by taking the height value, casting it as an integr, and subtracting 3330, which is the minimum value
                # then, that value is divided by 10774, which is the maximum value - the minimum value (14104 - 3330)
                # then, a value between 0 and 1 is achieved, and that value is multiplied my 255, and then casted to an integer
                # the complexity comes from wanting the minimum height value to be 0, and the max to be 255
                # this gives the most detail in the map 
                color = int(((int(everything[i][j])-3330) / 10774) * 255)
                #this code sets the pen color to a greyscale value, determined by the line above
                dudraw.set_pen_color_rgb(color,color,color)
                #this code draws a square, or pixel
                #the coordinates of the pixel come from the i and j loop. when dealing with 2d lists,
                # the inside loop acts as the x value because it is the loop transversing each row,
                # and the outside loop transverses the y value becuase it looks at each row, going down the whole list.
                # because of this, j is the x coordinate because is is the inside list,
                # and i is the y corrdinate because it is the outside loop
                # (ill be honest this is really hard to describe in words so if further explanation is needed,
                # i can do it in person) 
                dudraw.filled_square(j,i,1)
                #this bit of code checks for a mouse click, and stores the coordinates of the mouse click to
                # elevation, which is found by putting the x and y coordinates into the "everything" 2d list
                # which finds the height value at that location (again, this is hard to put into words, i 
                # can explain this in person if needed) 
                
                #this code ends the for loop if any key is typed at all




while proceed:
    if dudraw.mouse_is_pressed():
        x = int((dudraw.mouse_x()))
        y = int((dudraw.mouse_y()))
        elevation = everything[y][x]
        #this loop repeats for every row in the 2d list
        for i in range(len(everything)):
            #this loop repeats for every value in each row
            for j in range(len(everything[i])):
                #this line is a little complicated.
                # it sets the color of each height before it is drawn
                # it does this by taking the height value, casting it as an integr, and subtracting 3330, which is the minimum value
                # then, that value is divided by 10774, which is the maximum value - the minimum value (14104 - 3330)
                # then, a value between 0 and 1 is achieved, and that value is multiplied my 255, and then casted to an integer
                # the complexity comes from wanting the minimum height value to be 0, and the max to be 255
                # this gives the most detail in the map 
                color = int(((int(everything[i][j])-3330) / 10774) * 255)
                #this code sets the pen color to a greyscale value, determined by the line above
                dudraw.set_pen_color_rgb(color,color,color)
                #this code draws a square, or pixel
                #the coordinates of the pixel come from the i and j loop. when dealing with 2d lists,
                # the inside loop acts as the x value because it is the loop transversing each row,
                # and the outside loop transverses the y value becuase it looks at each row, going down the whole list.
                # because of this, j is the x coordinate because is is the inside list,
                # and i is the y corrdinate because it is the outside loop
                # (ill be honest this is really hard to describe in words so if further explanation is needed,
                # i can do it in person) 
                dudraw.filled_square(j,i,1)
                #this bit of code checks for a mouse click, and stores the coordinates of the mouse click to
                # elevation, which is found by putting the x and y coordinates into the "everything" 2d list
                # which finds the height value at that location (again, this is hard to put into words, i 
                # can explain this in person if needed) 
                
                #this code ends the for loop if any key is typed at all
    if dudraw.has_next_key_typed():
        if dudraw.next_key_typed() == "q":
            proceed = False
    #sets the color of the text to bright red
    dudraw.set_pen_color_rgb(255,0,0)
    #sets the size of the font to 30
    dudraw.set_font_size(30)
    #sets the font to comic sans (lol)
    dudraw.set_font_family("Comic Sans")
    #prints the text at the bottom right side of the screen, 
    dudraw.text(700,20, elevation)
    #shows the map for half a second
    dudraw.show(500)





