#
# Sample Labyrinth class to preesent a simple Manhathan map search
#
import copy

MOVES = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# ---------------------------------------------------------------------
# Sample Labyrinth class to preesent a simple Manhathan map search
# ---------------------------------------------------------------------
class Labyrinth():

    def __init__(self, width, height):

        self.width = width          # Width of the labyrinth
        self.height = height        # Height of the labyrinth
        self.cellsPath = {}         # Dictionary to store the paths from origin
        self.walls = set()          # Set of coordinates with a wall
        self.entry = (0,0)          # Entry point to the labyrinth
        self.exit = (0,0)           # Exit point from the Labyrinth

    # ---------------------------------------------------------------------
    # Loads the maze in the class
    # ---------------------------------------------------------------------
    def loadMaze(self, lines):

        for r in range(len(lines)):
            for c in range(len(lines[r])):
                if lines[r][c] == "x":              # 'x' means there is a wall
                    l.walls.add((r, c))
                elif lines[r][c] == "I":            # 'I' indicates the entry cell to the labyrinth
                    l.entry = (r, c)
                elif lines[r][c] == "O":            # 'O' indicates the exit cell to the labyrinth
                    l.exit = (r, c)


    # ---------------------------------------------------------------------
    # Calculates all the paths from the requested point of origin inside the maze to all the valid coordinates
    # Returns False if the origin is not a valid cell
    # ---------------------------------------------------------------------
    def allPaths (self, origin):

        if not 0 <= origin[0] < self.height or not 0 <= origin[1] < self.width or origin in self.walls:
            return False

        self.cellsPath = {}                     # Initializon variables
        visited = [origin]                      # List to keep track of the cells already visited adding the origin coordinate
        self.cellsPath[origin] = [0, [origin]]  # adding the path from origin to itself

        while len(visited) > 0:

            current = visited.pop(0)                                # poping an element from the visited
            for m in MOVES:                                         # looping on the possible moves (4 directionsin this case)
                newCell = (current[0] + m[0], current[1] + m[1])    # calculating new coordinates depending on the move
                if newCell not in self.walls:                       # if it is not a wall we proceed
                    if newCell in self.cellsPath.keys():            # if we were already here
                        if self.cellsPath[newCell][0] > self.cellsPath[current][0] + 1:             # check if the path stored is longer than the new one
                            self.cellsPath[newCell][0] = self.cellsPath[current][0] + 1             # in that case update the path length
                            self.cellsPath[newCell][1] = copy.deepcopy(self.cellsPath[current][1])  # copy the path
                            self.cellsPath[newCell][1].append(newCell)                              # and add the current cell

                    else:
                        self.cellsPath[newCell] = [self.cellsPath[current][0] + 1, []]              # initialize cellpath with length + 1
                        self.cellsPath[newCell][1] = copy.deepcopy(self.cellsPath[current][1])      # copy the path
                        self.cellsPath[newCell][1].append(newCell)                                  # and add the current cell
                        visited.append(newCell)                                                     # add the cell to the visited list

        return True

    #---------------------------------------------------------------------
    # Prints the path from an already calculated origin to a requested destination
    # ---------------------------------------------------------------------
    def printPath(self, destination):

        if destination in self.cellsPath.keys():
            print(self.cellsPath[destination])
        else:
            print("Destination not reachable")

    #---------------------------------------------------------------------
    # Calculates the paths from the requested origin to any point and
    # Prints the path from that origin to a requested destination
    # ---------------------------------------------------------------------
    def calculateAndPrintPath(self, origin, destination):
        result = l.allPaths(origin)
        if result:
            if destination in self.cellsPath.keys():
                print(self.cellsPath[destination])
            else:
                print("Destination not reachable")
        else:
            print("Origin not valid")


#--------------------------------------------------------------------------------------------
#--------------------------------------------- Main -----------------------------------------
#--------------------------------------------------------------------------------------------
fich = open(r"C:\Users\Sonia\PycharmProjects\Labyrinth\lab1.txt", "r")
w, h = [int(i) for i in fich.readline().split()]
l = Labyrinth(w,h)

lines = []                          # list of all the lines defining the maze
for r in range(h):
    lines.append(fich.readline())


# loads the maze details in the Labyrinth class
l.loadMaze(lines)

# Calculates all the paths from the given point (in this case the entry, but it could be any valid coordinate)
# Returns a boolean. False if the origin coordinates are not valild
result = l.allPaths (l.entry)

# prints the path from the origin to the given point (in this case the exit point) or an error message if not reachable
l.printPath(l.exit)

# Calculates all the paths and prints the one to the given destination
l.calculateAndPrintPath((1,1), (3,7))




