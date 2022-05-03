""""
Imports tkinter librry , coming with all inbuilt methods/functions.
Don't have to override object of widgets

messagebox is used to display message boxes
"""
from tkinter import *
from tkinter import messagebox


# Frame uses rectangular areas to organize the layout and improve widgets
class Checkers(Frame):
    # Initialize the attributes
    def __init__(self, doc, coord, z, moves, illegal, rad, num, moved, red_crown, blk_crown):
        # Calls frame to initialize the attributes inherited from frame
        Frame.__init__(self, doc)
        self.doc = doc

        # Used to keep track of the overlapping locations
        self.coord = coord  # Used to keep track of coordinates of pieces
        self.z = z
        self.moves = moves
        self.illegal = illegal  # Used to determine if a move is illegal
        # Rad and num are used to keep track of the players pieces
        self.rad = rad  # White pieces
        self.num = num  # Red pieces

        self.moved = moved
        self.red_crown = red_crown
        self.blk_crown = blk_crown

        self.step()

    def step(self):
        # organized widgets in blocks before placing
        # fill=both, determines to fil extra space, both means horizon and vertical
        # expand=True widget expands to fill any space not used
        self.pack(fill=BOTH, expand=TRUE)

        # Makes the background color
        canvas = Canvas(self, bg="gray")

        data = {"x": 0, "y": 0, "item": None}
        inpt = {"x": 0, "y": 0, "item": None}
        final_coord = [0, 0]

        # Creates the board create_rectangle(x0, y0, x1, y1, option, ...)
        re1 = canvas.create_rectangle(40, 30, 90, 80, outline="red", fill="red", tags="red")
        bl2 = canvas.create_rectangle(40, 80, 90, 130, outline="black", fill="black", tags="black")
        re3 = canvas.create_rectangle(40, 130, 90, 180, outline="red", fill="red", tags="red")
        bl4 = canvas.create_rectangle(40, 180, 90, 230, outline="black", fill="black", tags="black")
        re5 = canvas.create_rectangle(40, 230, 90, 280, outline="red", fill="red", tags="red")
        bl6 = canvas.create_rectangle(40, 280, 90, 330, outline="black", fill="black", tags="black")
        re7 = canvas.create_rectangle(40, 330, 90, 380, outline="red", fill="red", tags="red")
        bl8 = canvas.create_rectangle(40, 380, 90, 430, outline="black", fill="black", tags="black")
        bl9 = canvas.create_rectangle(90, 30, 140, 80, outline="black", fill="black", tags="black")
        re10 = canvas.create_rectangle(90, 80, 140, 130, outline="red", fill="red", tags="red")
        bl11 = canvas.create_rectangle(90, 130, 140, 180, outline="black", fill="black", tags="black")
        re12 = canvas.create_rectangle(90, 180, 140, 230, outline="red", fill="red", tags="red")
        bl13 = canvas.create_rectangle(90, 230, 140, 280, outline="black", fill="black", tags="black")
        re14 = canvas.create_rectangle(90, 280, 140, 330, outline="red", fill="red", tags="red")
        bl15 = canvas.create_rectangle(90, 330, 140, 380, outline="black", fill="black", tags="black")
        re16 = canvas.create_rectangle(90, 380, 140, 430, outline="red", fill="red", tags="red")
        re17 = canvas.create_rectangle(140, 30, 190, 80, outline="red", fill="red", tags="red")
        bl18 = canvas.create_rectangle(140, 80, 190, 130, outline="black", fill="black", tags="black")
        re19 = canvas.create_rectangle(140, 130, 190, 180, outline="red", fill="red", tags="red")
        bl20 = canvas.create_rectangle(140, 180, 190, 230, outline="black", fill="black", tags="black")
        re21 = canvas.create_rectangle(140, 230, 190, 280, outline="red", fill="red", tags="red")
        bl22 = canvas.create_rectangle(140, 280, 190, 330, outline="black", fill="black", tags="black")
        re23 = canvas.create_rectangle(140, 330, 190, 380, outline="red", fill="red", tags="red")
        bl24 = canvas.create_rectangle(140, 380, 190, 430, outline="black", fill="black", tags="black")
        bl25 = canvas.create_rectangle(190, 30, 240, 80, outline="black", fill="black", tags="black")
        re26 = canvas.create_rectangle(190, 80, 240, 130, outline="red", fill="red", tags="red")
        bl27 = canvas.create_rectangle(190, 130, 240, 180, outline="black", fill="black", tags="black")
        re28 = canvas.create_rectangle(190, 180, 240, 230, outline="red", fill="red", tags="red")
        bl29 = canvas.create_rectangle(190, 230, 240, 280, outline="black", fill="black", tags="black")
        re30 = canvas.create_rectangle(190, 280, 240, 330, outline="red", fill="red", tags="red")
        bl31 = canvas.create_rectangle(190, 330, 240, 380, outline="black", fill="black", tags="black")
        re32 = canvas.create_rectangle(190, 380, 240, 430, outline="red", fill="red", tags="red")
        re33 = canvas.create_rectangle(240, 30, 290, 80, outline="red", fill="red", tags="red")
        bl34 = canvas.create_rectangle(240, 80, 290, 130, outline="black", fill="black", tags="black")
        re35 = canvas.create_rectangle(240, 130, 290, 180, outline="red", fill="red", tags="red")
        bl36 = canvas.create_rectangle(240, 180, 290, 230, outline="black", fill="black", tags="black")
        re37 = canvas.create_rectangle(240, 230, 290, 280, outline="red", fill="red", tags="red")
        bl38 = canvas.create_rectangle(240, 280, 290, 330, outline="black", fill="black", tags="black")
        re39 = canvas.create_rectangle(240, 330, 290, 380, outline="red", fill="red", tags="red")
        bl40 = canvas.create_rectangle(240, 380, 290, 430, outline="black", fill="black", tags="black")
        bl41 = canvas.create_rectangle(290, 30, 340, 80, outline="black", fill="black", tags="black")
        re42 = canvas.create_rectangle(290, 80, 340, 130, outline="red", fill="red", tags="red")
        bl43 = canvas.create_rectangle(290, 130, 340, 180, outline="black", fill="black", tags="black")
        re44 = canvas.create_rectangle(290, 180, 340, 230, outline="red", fill="red", tags="red")
        bl45 = canvas.create_rectangle(290, 230, 340, 280, outline="black", fill="black", tags="black")
        re46 = canvas.create_rectangle(290, 280, 340, 330, outline="red", fill="red", tags="red")
        bl47 = canvas.create_rectangle(290, 330, 340, 380, outline="black", fill="black", tags="black")
        re48 = canvas.create_rectangle(290, 380, 340, 430, outline="red", fill="red", tags="red")
        re49 = canvas.create_rectangle(340, 30, 390, 80, outline="red", fill="red", tags="red")
        bl50 = canvas.create_rectangle(340, 80, 390, 130, outline="black", fill="black", tags="black")
        re51 = canvas.create_rectangle(340, 130, 390, 180, outline="red", fill="red", tags="red")
        bl52 = canvas.create_rectangle(340, 180, 390, 230, outline="black", fill="black", tags="black")
        re53 = canvas.create_rectangle(340, 230, 390, 280, outline="red", fill="red", tags="red")
        bl54 = canvas.create_rectangle(340, 280, 390, 330, outline="black", fill="black", tags="black")
        re55 = canvas.create_rectangle(340, 330, 390, 380, outline="red", fill="red", tags="red")
        bl56 = canvas.create_rectangle(340, 380, 390, 430, outline="black", fill="black", tags="black")
        bl57 = canvas.create_rectangle(390, 30, 440, 80, outline="black", fill="black", tags="black")
        re58 = canvas.create_rectangle(390, 80, 440, 130, outline="red", fill="red", tags="red")
        bl59 = canvas.create_rectangle(390, 130, 440, 180, outline="black", fill="black", tags="black")
        re60 = canvas.create_rectangle(390, 180, 440, 230, outline="red", fill="red", tags="red")
        bl61 = canvas.create_rectangle(390, 230, 440, 280, outline="black", fill="black", tags="black")
        re62 = canvas.create_rectangle(390, 280, 440, 330, outline="red", fill="red", tags="red")
        bl63 = canvas.create_rectangle(390, 330, 440, 380, outline="black", fill="black", tags="black")
        re64 = canvas.create_rectangle(390, 380, 440, 430, outline="red", fill="red", tags="red")
        """
        The variable sit is used to keep track of the location of the piece
        when clicked upon. Data is used to keep track of the player pieces when
        clicked and moved around
        """

        # For the clicking on pieces
        def button_press(sit):
            # returns information containing the object id of the object closest to point
            # records the object, plus its location
            data["item"] = canvas.find_closest(sit.x, sit.y)[0]
            data["x"] = sit.x
            data["y"] = sit.y

            inpt["item"] = data["item"]
            inpt["x"] = data["x"]
            inpt["y"] = data["y"]

            # shares the location of objects that are touching
            item_below = canvas.find_overlapping(sit.x, sit.y, sit.x, sit.y)[0]
            self.coord = coordinates(item_below)

        # For the letting go of pieces
        def button_release(sit):
            # Resets clicking information (mouse)
            data["item"] = None
            data["x"] = 0
            data["y"] = 0

        def moving(sit):

            # Define how far the obj moved
            coord_x = sit.x - data["x"]
            coord_y = sit.y - data["y"]
            # Move that distance
            canvas.move(data["item"], coord_x, coord_y)
            # New position
            data["x"] = sit.x
            data["y"] = sit.y

        # Gets information from item_below
        # Uses the coordinates to keep track of the movement
        def coordinates(identification):
            coord = []
            # Making column coords
            if 0 < identification < 9:
                coord.append(1)
            elif 9 <= identification < 17:
                coord.append(2)
            elif 17 <= identification < 25:
                coord.append(3)
            elif 25 <= identification < 33:
                coord.append(4)
            elif 33 <= identification < 41:
                coord.append(5)
            elif 41 <= identification < 49:
                coord.append(6)
            elif 49 <= identification < 57:
                coord.append(7)
            else:
                coord.append(8)

            # Making row coords
            if identification % 8 == 0:
                coord.append(8)
            elif identification % 8 == 1:
                coord.append(1)
            elif identification % 8 == 2:
                coord.append(2)
            elif identification % 8 == 3:
                coord.append(3)
            elif identification % 8 == 4:
                coord.append(4)
            elif identification % 8 == 5:
                coord.append(5)
            elif identification % 8 == 6:
                coord.append(6)
            elif identification % 8 == 7:
                coord.append(7)

            return coord

        """
        Keeps the pieces from moving multiple spaces across the board. 
        calculates where the piece is being placed and tells if its not allowed to be there.
        Also uses the coordinates to tell if the piece is being jumped over. thus telling
        if the piece needs to go away

        """

        def stan(coords):
            dims = []
            coord1 = 0
            coord2 = 0
            coord_1 = 0
            coord_2 = 0
            i = 1

            # configuring the x-coords
            while i < 9:
                if coords[0] == i:
                    if i == 1:
                        coord1 = 40
                        coord2 = 90
                    elif i == 2:
                        coord1 = 90
                        coord2 = 140
                    elif i == 3:
                        coord1 = 140
                        coord2 = 190
                    elif i == 4:
                        coord1 = 190
                        coord2 = 240
                    elif i == 5:
                        coord1 = 240
                        coord2 = 290
                    elif i == 6:
                        coord1 = 290
                        coord2 = 340
                    elif i == 7:
                        coord1 = 340
                        coord2 = 390
                    elif i == 8:
                        coord1 = 390
                        coord2 = 440

                # configuring y coords
                if coords[1] == i:
                    if i == 1:
                        coord_1 = 30
                        coord_2 = 80
                    elif i == 2:
                        coord_1 = 80
                        coord_2 = 130
                    elif i == 3:
                        coord_1 = 130
                        coord_2 = 180
                    elif i == 4:
                        coord_1 = 180
                        coord_2 = 230
                    elif i == 5:
                        coord_1 = 230
                        coord_2 = 280
                    elif i == 6:
                        coord_1 = 280
                        coord_2 = 330
                    elif i == 7:
                        coord_1 = 330
                        coord_2 = 380
                    elif i == 8:
                        coord_1 = 380
                        coord_2 = 430
                i += 1

            dims.append(coord1)
            dims.append(coord_1)
            dims.append(coord2)
            dims.append(coord_2)

            return dims

        # Making the pieces oval = canvas.create_oval(x0, y0, x1, y1, options)
        w1 = canvas.create_oval(50, 90, 80, 120, outline="white", fill="white", tags="oval")
        w2 = canvas.create_oval(50, 190, 80, 220, outline="white", fill="white", tags="oval")
        w3 = canvas.create_oval(50, 290, 80, 320, outline="white", fill="white", tags="oval")
        w4 = canvas.create_oval(50, 390, 80, 420, outline="white", fill="white", tags="oval")
        g5 = canvas.create_oval(100, 40, 130, 70, outline="white", fill="white", tags="oval")
        w6 = canvas.create_oval(100, 140, 130, 170, outline="white", fill="white", tags="oval")
        w7 = canvas.create_oval(100, 240, 130, 270, outline="white", fill="white", tags="oval")
        w8 = canvas.create_oval(100, 340, 130, 370, outline="white", fill="white", tags="oval")
        w9 = canvas.create_oval(150, 90, 180, 120, outline="white", fill="white", tags="oval")
        w10 = canvas.create_oval(150, 190, 180, 220, outline="white", fill="white", tags="oval")
        w11 = canvas.create_oval(150, 290, 180, 320, outline="white", fill="white", tags="oval")
        w12 = canvas.create_oval(150, 390, 180, 420, outline="white", fill="white", tags="oval")
        r1 = canvas.create_oval(300, 40, 330, 70, outline="maroon", fill="maroon", tags="oval")
        r2 = canvas.create_oval(300, 140, 330, 170, outline="maroon", fill="maroon", tags="oval")
        r3 = canvas.create_oval(300, 240, 330, 270, outline="maroon", fill="maroon", tags="oval")
        r4 = canvas.create_oval(300, 340, 330, 370, outline="maroon", fill="maroon", tags="oval")
        r5 = canvas.create_oval(350, 90, 380, 120, outline="maroon", fill="maroon", tags="oval")
        r6 = canvas.create_oval(350, 190, 380, 220, outline="maroon", fill="maroon", tags="oval")
        r7 = canvas.create_oval(350, 290, 380, 320, outline="maroon", fill="maroon", tags="oval")
        r8 = canvas.create_oval(350, 390, 380, 420, outline="maroon", fill="maroon", tags="oval")
        r9 = canvas.create_oval(400, 40, 430, 70, outline="maroon", fill="maroon", tags="oval")
        r10 = canvas.create_oval(400, 140, 430, 170, outline="maroon", fill="maroon", tags="oval")
        r11 = canvas.create_oval(400, 240, 430, 270, outline="maroon", fill="maroon", tags="oval")
        r12 = canvas.create_oval(400, 340, 430, 370, outline="maroon", fill="maroon", tags="oval")

        def logc(sit):
            if self.moved:
                self.moved = False

            button_release(sit)
            bl_tags = canvas.find_withtag("black")  # Returns a list of the objects ID
            # cur_itm helps with keeping track of the pieces and decidng whos turn it is
            cur_itm = canvas.find_closest(sit.x, sit.y)[0]  # Returns ID of the closest object
            # Returns ID of object sharing a point
            item_below = canvas.find_overlapping(sit.x, sit.y, sit.x, sit.y)[0]
            itm_tuple = canvas.find_overlapping(sit.x, sit.y, sit.x, sit.y)
            # has a variable equal function coordinates
            final_coord = coordinates(item_below)

            # Finds the difference for the row and col
            row_diff = abs(final_coord[1] - self.coord[1])
            col_diff = abs(final_coord[0] - self.coord[0])

            # Keeps the players pieces from moving where ever
            # The player has to move the piece diagonally and has to stay on the black tiles
            # Can only move multiple spaces when jumping a player
            colour = False
            if ((64 < self.z < 77) and (64 < cur_itm < 77)) and self.illegal != True:
                # colour = True
                if not self.moved:
                    coord_x = inpt["x"] - sit.x
                    coord_y = inpt["y"] - sit.y
                    canvas.move(inpt["item"], coord_x, coord_y)
                    self.moved = True

            elif ((76 < self.z < 90) and (76 < cur_itm < 90)) and self.illegal != True:
                # colour = True
                if not self.moved:
                    coord_x = inpt["x"] - sit.x
                    coord_y = inpt["y"] - sit.y
                    canvas.move(inpt["item"], coord_x, coord_y)
                    self.moved = True

            # Used for when a players piece reaches the end and becomes a king
            # The piece can now move in any direction
            for item in bl_tags:
                if item == item_below and len(itm_tuple) == 2 and row_diff > 0 and col_diff > 0:
                    sq_dims = stan(final_coord)
                    self.moves += 1
                    if final_coord[0] == 1 and cur_itm > 76 and colour != True:
                        canvas.itemconfig(cur_itm, fill="Orange", outline="Orange")
                        self.red_crown.append(cur_itm)
                    elif final_coord[0] == 8 and cur_itm < 77 and colour != True:
                        canvas.itemconfig(cur_itm, fill="gray", outline="gray")
                        self.blk_crown.append(cur_itm)

                    gcrn_itm = 0
                    for i in self.blk_crown:
                        if i == cur_itm and colour != True:
                            gcrn_itm = i
                            break

                    ocrn_itm = 0
                    for i in self.red_crown:
                        if i == cur_itm and colour != True:
                            ocrn_itm = i
                            break

                    if col_diff == 2 and row_diff == 2 and self.moves > 1:
                        man_coord = []
                        # column = 0
                        # rows = 0
                        self.z = cur_itm
                        if final_coord[0] > self.coord[0] and final_coord[1] > self.coord[1]:
                            if cur_itm < 77 or ocrn_itm == cur_itm:
                                column = self.coord[0] + 1
                                rows = self.coord[1] + 1
                                man_coord.append(column)
                                man_coord.append(rows)
                            else:
                                self.illegal = True
                                coord_x = inpt["x"] - sit.x
                                coord_y = inpt["y"] - sit.y
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break
                        elif final_coord[0] > self.coord[0] and final_coord[1] < self.coord[1]:
                            if cur_itm < 77 or ocrn_itm == cur_itm:
                                column = self.coord[0] + 1
                                rows = self.coord[1] - 1
                                man_coord.append(column)
                                man_coord.append(rows)
                            else:
                                self.illegal = True
                                coord_x = inpt["x"] - sit.x
                                coord_y = inpt["y"] - sit.y
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break
                        elif final_coord[0] < self.coord[0] and final_coord[1] > self.coord[1]:
                            if cur_itm > 76 or gcrn_itm == cur_itm:
                                column = self.coord[0] - 1
                                rows = self.coord[1] + 1
                                man_coord.append(column)
                                man_coord.append(rows)
                            else:
                                self.illegal = True
                                coord_x = inpt["x"] - sit.x
                                coord_y = inpt["y"] - sit.y
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break
                        elif final_coord[0] < self.coord[0] and final_coord[1] < self.coord[1]:
                            if cur_itm > 76 or gcrn_itm == cur_itm:
                                column = self.coord[0] - 1
                                rows = self.coord[1] - 1
                                man_coord.append(column)
                                man_coord.append(rows)
                            else:
                                self.illegal = True
                                coord_x = inpt["x"] - sit.x
                                coord_y = inpt["y"] - sit.y
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break

                        if len(man_coord) != 0 and colour != True:
                            dims = stan(man_coord)
                            man = canvas.find_enclosed(dims[0], dims[1], dims[2], dims[3])
                            if len(man) == 0:
                                coord_x = inpt["x"] - sit.x
                                coord_y = inpt["y"] - sit.y
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break
                            else:
                                if (cur_itm < 77 and man[0] > 76) or (cur_itm > 76 and man[0] < 77):
                                    canvas.delete(man)  # Deletes a players piece when jumped
                                    if man[0] < 77:
                                        self.rad -= 1
                                    else:
                                        self.num -= 1
                                    # Sends a game over message if either of the payers lose all their pieces
                                    if self.rad == 0 or self.num == 0:
                                        if self.rad > self.num:
                                            messagebox.showinfo(title=None, message="Game Over, white Wins")
                                        else:
                                            messagebox.showinfo(title=None, message="Game Over, Red Wins")
                                else:
                                    coord_x = inpt["x"] - sit.x
                                    coord_y = inpt["y"] - sit.y
                                    canvas.move(inpt["item"], coord_x, coord_y)
                                    self.z = 0
                        break

                    elif col_diff == 1 and row_diff == 1:
                        if (64 < cur_itm < 77) and cur_itm != gcrn_itm:
                            if final_coord[0] < self.coord[0]:
                                continue
                        elif (76 < cur_itm < 90) and cur_itm != ocrn_itm:
                            if final_coord[0] > self.coord[0]:
                                continue

                        self.z = cur_itm
                        break

            else:
                if not colour:
                    coord_x = inpt["x"] - sit.x
                    coord_y = inpt["y"] - sit.y
                    canvas.move(inpt["item"], coord_x, coord_y)

        # Allows for the moving, and clicking of the pieces
        # Binds the pieces to the functions
        canvas.tag_bind("oval", "<ButtonPress>", button_press)
        canvas.tag_bind("oval", "<Motion>", moving)
        canvas.tag_bind("oval", "<ButtonRelease>", logc)
        # Displays the pieces and the board
        canvas.pack(fill=BOTH, expand=1)


roooot = Tk()
red = False
white = False
count = 0
kount = 0
Checkers(roooot, [], 0, 0, False, 12, 12, False, [], [])
roooot.geometry("480x460+500+200")  # Sets size of the window screen
roooot.mainloop()

