from tkinter import *
import Combination_generator
import all_factors
import math
import bisect
import time


class Eggsorter:

    def __init__(self, root, n, r):

        self.n = n
        self.r = r
        self.eggcups = []  # all n possible egg positions represented as tkinter oval objects on canvas
        self.columns, self.rows = self.grid_setup(self.n)

        # Tkinter initiation
        self.container = Frame(root)
        self.container.pack()
        self.canvas = self.eggbox()

    def grid_setup(self, n):
        """ Returns closest factors of n which, when multiplied, equal n, e.g. n = 20: returns 5 x 4, n = 30: returns 6 x 5, n = 21: returns 3 x 7"""
        """ These define width and height of grid"""
        if math.sqrt(n) % 1 == 0:  # check if n has perfect square
            # print("dfdsf")
            (columns, rows) = (math.sqrt(n), math.sqrt(n))

        else:

            factors = all_factors.main(n)

            w = bisect.bisect_right(factors, math.sqrt(n))  # returns index pos of nearest factor greater than root n
            #  slice factors list into 2 sublists, above and below sqrt of  n, e.g. for n = 30:  [2,3,5]  < 5.47 < [6,10,15,30]
            fac_below = factors[:w]  # [2,3,5]
            fac_above = factors[w:]  # [6,10,15,30]

            columns = fac_above[0]  # 6
            rows = fac_below[-1]  # 5

        return columns, rows

    def eggbox(self):
        """Setup empty eggbox as tkinter oval objects per rows, columns"""

        w = 1500  # tk window width
        h = 800  # tk window height

        d = 100  # "egg" diameter

        #  resize to prevent eggcups overlapping and going off screen edge
        if d*self.columns > w:
            d = w/self.columns
        if d*self.rows > h:
            d = h/self.rows

        canvas = Canvas(self.container, bg="black", width=w, height=h)
        canvas.pack()

        # setup red outined ovals for col x rows and append to eggcups list
        for j in range(20, h, int(h/self.rows)):
            for i in range(20, w, int(w / self.columns)):

                eggcup = canvas.create_oval(i, j, i+d, j+d, outline="red")
                self.eggcups.append(eggcup)

        return canvas

    def sorteggs(self):
        """ Loops through all combinations of ncr and displays this shit on the tkinter canvas"""
        allseq = Combination_generator.main(self.n, self.r)  # Generator yields each combination in turn

        # seq = (1,3,5,8)
        # for i in seq:
        #     self.canvas.itemconfig(self.eggcups[i - 1], fill="red")

        for seq in allseq:
            for i in seq:
                self.canvas.itemconfig(self.eggcups[i-1], fill="red")  # display current sequence by applying red fill (show egg init)
            self.container.after(250, self.canvas.update())  # loop every 0.25 seconds

            for i in seq:
                self.canvas.itemconfig(self.eggcups[i-1], fill="black")  # reset before displaying next sequence


if __name__ == '__main__':
    n = int(input("Enter n: "))
    r = int(input("Enter r: "))

    root = Tk()
    eggsorter = Eggsorter(root, n, r)
    eggsorter.sorteggs()
    root.mainloop()
