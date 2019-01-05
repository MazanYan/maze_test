import random
import math

class Maze:



    """
    Cell
    """
    class Cell:
        def __init__(self, type: "Void, Wall, Space", state: "op, cl" = " "):
            self.__state = " "
            self.__type = type
            if self.__type == "Wall":
                self.__state = state
            if self.__type == "Void":
                self.__state = "▣"

        def type(self):
            return self.__type

        def show_state(self):
            return self.__state

        def open(self):
            if self.__type == "Wall":
                self.__state = " "

        def close(self):
            if self.__type == "Wall":
                self.__state = "▣"

    def __init__(self, width, height):
        self.wall_rows = list(range(1, height, 2))
        self.wall_columns = list(range(1, width, 2))
        self.width = width
        self.height = height

        self.matrix = [[self.Cell("Void") if x%2 == 1 and y%2 == 1
                        else(self.Cell("Wall") if x%2 == 1 or y%2 == 1 else self.Cell("Space")) for x in range(width)]
                        for y in range(height)]

        self.generate_maze()

    def __str__(self):
         result = ""
         for i in self.matrix:
             for j in i:
                 result+=j.show_state() + " "
             result += "\n"
         return result[:-1]

    def generate_maze(self):

        def choose_random_row(start = 0,end = self.height-1):
            return random.choice([x for x in range(start, end,2)])

        def choose_random_column(start = 0, end = self.width-1):
            return random.choice([x for x in range(start, end,2)])

        def split(axis_to_split: "0x or 0y", row_column_to_close, start_pt, end_pt):
            if math.fabs(end_pt-start_pt)<=1:
                return
            if axis_to_split == "0x":
                row_to_close = row_column_to_close
                for i in range(start_pt, end_pt):
                    self.matrix[row_to_close][i].close()
            else:
                column_to_close = row_column_to_close
                for i in range(start_pt, end_pt):
                    self.matrix[i][column_to_close].close()

        def iteration_step(x_start, x_end, y_start,y_end):
            """
            A check-out to make recursion end
            :param x_start:
            :param x_end:
            :param y_start:
            :param y_end:
            :return:
            """
            if (math.fabs(x_start-x_end)<=2 or math.fabs(y_start-y_end)<=2):
                return

            row_to_close = choose_random_row(y_start, y_end)
            column_to_close = choose_random_column(x_start, x_end)

            row_in_open = choose_random_column(x_start-1, x_end)
            column_in_open = choose_random_row(y_start-1, y_end)

            split("0x", row_to_close, x_start, x_end)
            split("0y", column_to_close, y_start, y_end)

            self.matrix[row_to_close][row_in_open].open()
            self.matrix[column_in_open][column_to_close].open()

            #print(self, "\n\n\n")
            iteration_step(x_start,column_to_close,y_start,row_to_close)
            iteration_step(column_to_close,x_end,y_start,row_to_close)
            iteration_step(x_start,column_to_close,row_to_close, y_end)
            iteration_step(column_to_close, x_end, row_to_close, y_end)

        iteration_step(0,self.width,0,self.height)