class Plateau():
  def __init__(self,coords):
    
    self.__length = int(coords.split(" ")[0])
    self.__width = int(coords.split(" ")[1])
    self.__rovers = []


  def getlength(self):
    return self.__length

  def getwidth(self):
    return self.__width

  def display(self,r):
    rx = r.getx()
    ry = r.gety()
    grid = []
    for i in range(0,self.__length):
      grid.append([])
      for j in range(0,self.__width):
        if i == self.__length-(ry) and j == rx-1:
          grid[i].append("R")
        else:
          grid[i].append("")


    for i in range(0,self.__length):
      print(grid[i])

  def addrover(self,rover):
    self.__rovers.append(rover)

  def getrover(self,i):
    return self.__rovers[i]
    
    

    
class Rover():
  def __init__(self):
    self.__Direction = Direction()
    self.__x = None
    self.__y = None
    self.placerover()

  def getx(self):
    return self.__x

  def gety(self):
    return self.__y
  
  def rotateright(self):
    self.__Direction.right()

  def rotateleft(self):
    self.__Direction.left()

  def placerover(self):
    print("Enter the x coordinate of the rover")
    x = int(input())
    while x > p.getwidth() or x < 1:
      print("Error, rover not on Plateau")
      x = int(input())
    self.__x = x
    print("Enter the y coordinate of the rover")
    y = int(input())
    while y > p.getlength() or y < 1:
      print("Error, rover not on Plateau")
      y = int(input())
    self.__y = y

  def move(self):
    if self.__Direction.getdirection() == "N":
      self.checkmove(1,"Height")
      print("N")
    elif self.__Direction.getdirection() == "S":
      self.checkmove(-1,"Height")
      print("S")
    elif self.__Direction.getdirection() == "E":
      self.checkmove(1,"Width")
      print("E")
    elif self.__Direction.getdirection() == "W":
      self.checkmove(-1,"Width")
      print("W")
    else:
      print("Error")

  def checkmove(self,move,direction):
    if direction == "Height":
      if self.__y + move > p.getlength() or self.__y + move < 1:
        print("Error, rover unable to move")
      else:
        self.__y += move
    else:
      if self.__x + move > p.getwidth() or self.__x + move < 1:
        print("Error, rover unable to move")
      else:
        self.__x += move

  def processString(self,string):
    string = string.upper()
    for i in range(0,len(string)):
      if string[i] == "M":
        self.move()
      elif string[i] == "L":
        self.rotateleft()
      elif string[i] == "R":
        self.rotateright()
      else:
        pass
         
class Direction():
  def __init__(self):
    self.__values = ["N","E","S","W"]
    self.__pointer = self.setdirection()

  def setdirection(self):
    self.__pointer = 0
    print("Enter the direction to face the rover, first letter of the direction")
    d = input()
    if d.upper() == "N":
      self.__pointer = 0
    elif d.upper() == "E":
      self.__pointer = 1
    elif d.upper() == "S":
      self.__pointer = 2
    elif d.upper() == "W":
      self.__pointer = 3
    else:
      print("Error!")
    return self.__pointer
    
  def left(self):
    if self.__pointer - 1 < 0:
      self.__pointer = 3
    else: 
      self.__pointer += -1
  
    
  def right(self):
    if self.__pointer + 1 > 3:
      self.__pointer = 0
    else: 
      self.__pointer += 1

  def getdirection(self):
    try:
      return self.__values[self.__pointer]
    except:
      print(self.__pointer)


print("Enter the top right coordinates of the plateau.")
print("Length then width, with a space in between e.g 7 7:")
coords = input()
p = Plateau(coords)

r = Rover()

p.display(r)

print("Enter commands")
string = input()
while string != "X":
  r.processString(string)
  p.display(r)
  string = input()
