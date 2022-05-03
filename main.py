""""
Noah Assam
Checkers
5.2.22
EECE 2140

Imports tkinter librry , coming with all inbuilt methods/functions.
Don't have to override object of widgets

messagebox is used to display message boxes
"""
from tkinter import messagebox
from tkinter import *


# Frame uses rectangular areas to organize the layout and improve widgets
class Checkers(Frame):
    # Initialize the attributes
    def __init__(self, doc, coord, z, moves, illegal, rad, num, moved, red_crown, blk_crown):
        # Calls frame to initialize the attributes inherited from frame
        Frame.__init__(self, doc)
        self.red_crown = red_crown
        self.blk_crown = blk_crown
        self.doc = doc
        self.illegal = illegal  # Used to determine if a move is illegal
        # Rad and num are used to keep track of the players pieces
        self.rad = rad  # White pieces
        self.num = num  # Red pieces
        # Used to keep track of the overlapping locations
        self.coord = coord  # Used to keep track of coordinates of pieces
        self.z = z
        self.moves = moves
        self.moved = moved

        self.step()

    def step(self):
        # organized widgets in blocks before placing
        # fill=both, determines to fil extra space, both means horizon and vertical
        # expand=True widget expands to fill any space not used
        self.pack(fill=BOTH, expand=TRUE)

        # Makes the background color
        canvas = Canvas(self, bg="gray")
        fin = [0, 0]
        data = {"x": 0, "y": 0, "item": None}
        inpt = {"x": 0, "y": 0, "item": None}

        # Creates the board create_rectangle(x0, y0, x1, y1, option, ...)
        red1 = canvas.create_rectangle(40, 30, 90, 80, outline="red", fill="red", tags="red")
        black2 = canvas.create_rectangle(40, 80, 90, 130, outline="black", fill="black", tags="black")
        red3 = canvas.create_rectangle(40, 130, 90, 180, outline="red", fill="red", tags="red")
        black4 = canvas.create_rectangle(40, 180, 90, 230, outline="black", fill="black", tags="black")
        red5 = canvas.create_rectangle(40, 230, 90, 280, outline="red", fill="red", tags="red")
        black6 = canvas.create_rectangle(40, 280, 90, 330, outline="black", fill="black", tags="black")
        red7 = canvas.create_rectangle(40, 330, 90, 380, outline="red", fill="red", tags="red")
        black8 = canvas.create_rectangle(40, 380, 90, 430, outline="black", fill="black", tags="black")
        black9 = canvas.create_rectangle(90, 30, 140, 80, outline="black", fill="black", tags="black")
        red10 = canvas.create_rectangle(90, 80, 140, 130, outline="red", fill="red", tags="red")
        black11 = canvas.create_rectangle(90, 130, 140, 180, outline="black", fill="black", tags="black")
        red12 = canvas.create_rectangle(90, 180, 140, 230, outline="red", fill="red", tags="red")
        black13 = canvas.create_rectangle(90, 230, 140, 280, outline="black", fill="black", tags="black")
        red14 = canvas.create_rectangle(90, 280, 140, 330, outline="red", fill="red", tags="red")
        black15 = canvas.create_rectangle(90, 330, 140, 380, outline="black", fill="black", tags="black")
        red16 = canvas.create_rectangle(90, 380, 140, 430, outline="red", fill="red", tags="red")
        red17 = canvas.create_rectangle(140, 30, 190, 80, outline="red", fill="red", tags="red")
        black18 = canvas.create_rectangle(140, 80, 190, 130, outline="black", fill="black", tags="black")
        red19 = canvas.create_rectangle(140, 130, 190, 180, outline="red", fill="red", tags="red")
        black20 = canvas.create_rectangle(140, 180, 190, 230, outline="black", fill="black", tags="black")
        red21 = canvas.create_rectangle(140, 230, 190, 280, outline="red", fill="red", tags="red")
        black22 = canvas.create_rectangle(140, 280, 190, 330, outline="black", fill="black", tags="black")
        red23 = canvas.create_rectangle(140, 330, 190, 380, outline="red", fill="red", tags="red")
        black24 = canvas.create_rectangle(140, 380, 190, 430, outline="black", fill="black", tags="black")
        black25 = canvas.create_rectangle(190, 30, 240, 80, outline="black", fill="black", tags="black")
        red26 = canvas.create_rectangle(190, 80, 240, 130, outline="red", fill="red", tags="red")
        black27 = canvas.create_rectangle(190, 130, 240, 180, outline="black", fill="black", tags="black")
        red28 = canvas.create_rectangle(190, 180, 240, 230, outline="red", fill="red", tags="red")
        black29 = canvas.create_rectangle(190, 230, 240, 280, outline="black", fill="black", tags="black")
        red30 = canvas.create_rectangle(190, 280, 240, 330, outline="red", fill="red", tags="red")
        black31 = canvas.create_rectangle(190, 330, 240, 380, outline="black", fill="black", tags="black")
        red32 = canvas.create_rectangle(190, 380, 240, 430, outline="red", fill="red", tags="red")
        red33 = canvas.create_rectangle(240, 30, 290, 80, outline="red", fill="red", tags="red")
        black34 = canvas.create_rectangle(240, 80, 290, 130, outline="black", fill="black", tags="black")
        red35 = canvas.create_rectangle(240, 130, 290, 180, outline="red", fill="red", tags="red")
        black36 = canvas.create_rectangle(240, 180, 290, 230, outline="black", fill="black", tags="black")
        red37 = canvas.create_rectangle(240, 230, 290, 280, outline="red", fill="red", tags="red")
        black38 = canvas.create_rectangle(240, 280, 290, 330, outline="black", fill="black", tags="black")
        red39 = canvas.create_rectangle(240, 330, 290, 380, outline="red", fill="red", tags="red")
        black40 = canvas.create_rectangle(240, 380, 290, 430, outline="black", fill="black", tags="black")
        black41 = canvas.create_rectangle(290, 30, 340, 80, outline="black", fill="black", tags="black")
        red42 = canvas.create_rectangle(290, 80, 340, 130, outline="red", fill="red", tags="red")
        black43 = canvas.create_rectangle(290, 130, 340, 180, outline="black", fill="black", tags="black")
        red44 = canvas.create_rectangle(290, 180, 340, 230, outline="red", fill="red", tags="red")
        black45 = canvas.create_rectangle(290, 230, 340, 280, outline="black", fill="black", tags="black")
        red46 = canvas.create_rectangle(290, 280, 340, 330, outline="red", fill="red", tags="red")
        black47 = canvas.create_rectangle(290, 330, 340, 380, outline="black", fill="black", tags="black")
        red48 = canvas.create_rectangle(290, 380, 340, 430, outline="red", fill="red", tags="red")
        red49 = canvas.create_rectangle(340, 30, 390, 80, outline="red", fill="red", tags="red")
        black50 = canvas.create_rectangle(340, 80, 390, 130, outline="black", fill="black", tags="black")
        red51 = canvas.create_rectangle(340, 130, 390, 180, outline="red", fill="red", tags="red")
        black52 = canvas.create_rectangle(340, 180, 390, 230, outline="black", fill="black", tags="black")
        red53 = canvas.create_rectangle(340, 230, 390, 280, outline="red", fill="red", tags="red")
        black54 = canvas.create_rectangle(340, 280, 390, 330, outline="black", fill="black", tags="black")
        red55 = canvas.create_rectangle(340, 330, 390, 380, outline="red", fill="red", tags="red")
        black56 = canvas.create_rectangle(340, 380, 390, 430, outline="black", fill="black", tags="black")
        black57 = canvas.create_rectangle(390, 30, 440, 80, outline="black", fill="black", tags="black")
        red58 = canvas.create_rectangle(390, 80, 440, 130, outline="red", fill="red", tags="red")
        black59 = canvas.create_rectangle(390, 130, 440, 180, outline="black", fill="black", tags="black")
        red60 = canvas.create_rectangle(390, 180, 440, 230, outline="red", fill="red", tags="red")
        black61 = canvas.create_rectangle(390, 230, 440, 280, outline="black", fill="black", tags="black")
        red62 = canvas.create_rectangle(390, 280, 440, 330, outline="red", fill="red", tags="red")
        black63 = canvas.create_rectangle(390, 330, 440, 380, outline="black", fill="black", tags="black")
        red64 = canvas.create_rectangle(390, 380, 440, 430, outline="red", fill="red", tags="red")
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
            inpt["x"] = data["x"]
            inpt["y"] = data["y"]
            inpt["item"] = data["item"]


            # shares the location of objects that are touching
            item_below = canvas.find_overlapping(sit.x, sit.y, sit.x, sit.y)[0]
            self.coord = coordinates(item_below)

        def moving(sit):

            # Define how far the obj moved
            coord_x = sit.x - data["x"]
            coord_y = sit.y - data["y"]
            # Move that distance
            canvas.move(data["item"], coord_x, coord_y)
            # New position
            data["y"] = sit.y
            data["x"] = sit.x

        # For the letting go of pieces
        def button_release(sit):
            # Resets clicking information (mouse)
            data["item"] = None
            data["x"] = 0
            data["y"] = 0



        # Gets information from item_below
        # Uses the coordinates to keep track of the movement
        def coordinates(taffy):
            coord = []


            # Making column coords
            if 0 < taffy < 9:
                coord.append(1)
            elif 9 <= taffy < 17:
                coord.append(2)
            elif 17 <= taffy < 25:
                coord.append(3)
            elif 25 <= taffy < 33:
                coord.append(4)
            elif 33 <= taffy < 41:
                coord.append(5)
            elif 41 <= taffy < 49:
                coord.append(6)
            elif 49 <= taffy < 57:
                coord.append(7)
            else:
                coord.append(8)

            # Making row coords
            if taffy % 8 == 0:
                coord.append(8)
            elif taffy % 8 == 1:
                coord.append(1)
            elif taffy % 8 == 2:
                coord.append(2)
            elif taffy % 8 == 3:
                coord.append(3)
            elif taffy % 8 == 4:
                coord.append(4)
            elif taffy % 8 == 5:
                coord.append(5)
            elif taffy % 8 == 6:
                coord.append(6)
            elif taffy % 8 == 7:
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
            k = 1

            # configuring the x-coords
            while k < 9:
                if coords[0] == k:
                    if k == 1:
                        coord1 = 40
                        coord2 = 90
                    elif k == 2:
                        coord1 = 90
                        coord2 = 140
                    elif k == 3:
                        coord1 = 140
                        coord2 = 190
                    elif k == 4:
                        coord1 = 190
                        coord2 = 240
                    elif k == 5:
                        coord1 = 240
                        coord2 = 290
                    elif k == 6:
                        coord1 = 290
                        coord2 = 340
                    elif k == 7:
                        coord1 = 340
                        coord2 = 390
                    elif k == 8:
                        coord1 = 390
                        coord2 = 440

                # configuring y coords
                if coords[1] == k:
                    if k == 1:
                        coord_1 = 30
                        coord_2 = 80
                    elif k == 2:
                        coord_1 = 80
                        coord_2 = 130
                    elif k == 3:
                        coord_1 = 130
                        coord_2 = 180
                    elif k == 4:
                        coord_1 = 180
                        coord_2 = 230
                    elif k == 5:
                        coord_1 = 230
                        coord_2 = 280
                    elif k == 6:
                        coord_1 = 280
                        coord_2 = 330
                    elif k == 7:
                        coord_1 = 330
                        coord_2 = 380
                    elif k == 8:
                        coord_1 = 380
                        coord_2 = 430
                k += 1

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
            # itm helps with keeping track of the pieces and decidng whos turn it is
            itm = canvas.find_closest(sit.x, sit.y)[0]  # Returns ID of the closest object
            # Returns ID of object sharing a point
            itm_tuple = canvas.find_overlapping(sit.x, sit.y, sit.x, sit.y)
            item_below = canvas.find_overlapping(sit.x, sit.y, sit.x, sit.y)[0]

            # has a variable equal function coordinates
            fin = coordinates(item_below)

            # Finds the difference for the row and col
            lol = abs(fin[0] - self.coord[0])
            row_diff = abs(fin[1] - self.coord[1])


            # Keeps the players pieces from moving where ever
            # The player has to move the piece diagonally and has to stay on the black tiles
            # Can only move multiple spaces when jumping a player
            colour = False
            if ((64 < self.z < 77) and (64 < itm < 77)) and self.illegal != True:
                colour = True
                if not self.moved:
                    coord_x = inpt["x"] - sit.x
                    coord_y = inpt["y"] - sit.y
                    canvas.move(inpt["item"], coord_x, coord_y)
                    self.moved = True

            elif ((76 < self.z < 90) and (76 < itm < 90)) and self.illegal != True:
                colour = True
                if not self.moved:
                    coord_x = inpt["x"] - sit.x
                    coord_y = inpt["y"] - sit.y
                    canvas.move(inpt["item"], coord_x, coord_y)
                    self.moved = True

            # Used for when a players piece reaches the end and becomes a king
            # The piece can now move in any direction
            for item in bl_tags:
                if item == item_below and len(itm_tuple) == 2 and row_diff > 0 and lol > 0:
                    sq_dims = stan(fin)
                    self.moves += 1
                    if fin[0] == 1 and itm > 76 and colour != True:
                        canvas.itemconfig(itm, fill="Orange", outline="Orange")
                        self.red_crown.append(itm)
                    elif fin[0] == 8 and itm < 77 and colour != True:
                        canvas.itemconfig(itm, fill="gray", outline="gray")
                        self.blk_crown.append(itm)

                    itm_1 = 0
                    for i in self.blk_crown:
                        if i == itm and colour != True:
                            itm_1 = i
                            break

                    itm_2 = 0
                    for i in self.red_crown:
                        if i == itm and colour != True:
                            itm_2 = i
                            break

                    if lol == 2 and row_diff == 2 and self.moves > 1:
                        man_coord = []
                        self.z = itm
                        if fin[0] > self.coord[0] and fin[1] > self.coord[1]:
                            if itm < 77 or itm_2 == itm:
                                column = self.coord[0] + 1
                                rows = self.coord[1] + 1
                                man_coord.append(column)
                                man_coord.append(rows)
                            else:
                                coord_x = inpt["x"] - sit.x
                                coord_y = inpt["y"] - sit.y
                                self.illegal = True

                                canvas.move(inpt["item"], coord_x, coord_y)
                                break
                        elif fin[0] > self.coord[0] and fin[1] < self.coord[1]:
                            if itm < 77 or itm_2 == itm:
                                rows = self.coord[1] - 1
                                column = self.coord[0] + 1
                                man_coord.append(column)
                                man_coord.append(rows)
                            else:
                                coord_x = inpt["x"] - sit.x
                                self.illegal = True
                                coord_y = inpt["y"] - sit.y
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break
                        elif fin[1] > self.coord[1] and fin[0] < self.coord[0]:
                            if itm > 76 or itm_1 == itm:
                                rows = self.coord[1] + 1
                                column = self.coord[0] - 1
                                man_coord.append(column)
                                man_coord.append(rows)
                            else:
                                coord_y = inpt["y"] - sit.y
                                self.illegal = True
                                coord_x = inpt["x"] - sit.x
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break
                        elif fin[0] < self.coord[0] and fin[1] < self.coord[1]:
                            if itm > 76 or itm_1 == itm:
                                rows = self.coord[1] - 1
                                column = self.coord[0] - 1
                                man_coord.append(column)
                                man_coord.append(rows)
                            else:
                                coord_y = inpt["y"] - sit.y
                                coord_x = inpt["x"] - sit.x
                                self.illegal = True
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break

                        if len(man_coord) != 0 and colour != True:
                            dims = stan(man_coord)
                            man = canvas.find_enclosed(dims[0], dims[1], dims[2], dims[3])
                            if len(man) == 0:
                                coord_y = inpt["y"] - sit.y
                                coord_x = inpt["x"] - sit.x
                                canvas.move(inpt["item"], coord_x, coord_y)
                                break
                            else:
                                if (itm > 76 and man[0] < 77) or (itm < 77 and man[0] > 76):
                                    canvas.delete(man)  # Deletes a players piece when jumped
                                    if man[0] < 77:
                                        self.rad -= 1
                                    else:
                                        self.num -= 1
                                    # Sends a game over message if either of the payers lose all their pieces
                                    if self.num == 0 or self.rad == 0:
                                        if self.rad > self.num:
                                            messagebox.showinfo(title=None, message="Game Over, white Wins")
                                        else:
                                            messagebox.showinfo(title=None, message="Game Over, Red Wins")
                                else:
                                    self.z = 0
                                    coord_y = inpt["y"] - sit.y
                                    coord_x = inpt["x"] - sit.x
                                    canvas.move(inpt["item"], coord_x, coord_y)
                        break

                    elif lol == 1 and row_diff == 1:
                        if itm != itm_1 and (64 < itm < 77):
                            if fin[0] < self.coord[0]:
                                continue
                        elif (76 < itm < 90) and itm != itm_2:
                            if fin[0] > self.coord[0]:
                                continue

                        self.z = itm
                        break

            else:
                if not colour:
                    coord_y = inpt["y"] - sit.y
                    coord_x = inpt["x"] - sit.x
                    canvas.move(inpt["item"], coord_x, coord_y)

        # Allows for the moving, and clicking of the pieces
        # Binds the pieces to the functions
        canvas.tag_bind("oval", "<Motion>", moving)
        canvas.tag_bind("oval", "<ButtonPress>", button_press)
        canvas.tag_bind("oval", "<ButtonRelease>", logc)
        # Displays the pieces and the board
        canvas.pack(fill=BOTH, expand=1)


roooot = Tk()
count = 0
kount = 0
red = False
white = False
Checkers(roooot, [], 0, 0, False, 12, 12, False, [], [])
roooot.geometry("480x460+500+200")  # Sets size of the window screen
roooot.mainloop()

