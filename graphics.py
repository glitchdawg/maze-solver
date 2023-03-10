from tkinter import Tk, BOTH, Canvas

#create a Window class
class Window:
    #The constructor should take a width and height. This will be the size of the new window we create in pixels.
    def __init__(self, width, height):
        #It should create a new root widget using Tk() and save it as a data member
        self.__root=Tk()
        #Set the title property of the root widget
        self.__root.title("Maze solver")
        #Create a Canvas and save it as a data member.
        self.__canvas=Canvas(self.__root, bg="white", height=height, width=width)
        #Pack the canvas so that it's ready to be drawn
        self.__canvas.pack(fill=BOTH,expand=1)
        #Create a data member to represent that the window is "running", and set it to False
        self.__running=False
        #we also need to add another line to constructor to call the protocol method on the root widget, to connect your close method to the "delete window" action.
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    #The redraw() method on the window class should simply call the root widget's update_idletasks() and update() methods. Each time this is called, the window will redraw itself.
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        #This method should set the data member we created to track the "running" state of the window to True
        self.__running = True
        #it should call self.redraw() over and over as long as the running state remains True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running=False
    
    def draw_line(self,line,fill_color="black"):
        line.draw(self.__canvas,fill_color)
        
class Point:
    def __init__(self,x,y):
        #x - the x-coordinate (horizontal) in pixels of the point
        self.x=x
        #y - the y-coordinate (vertical) in pixels of the point
        self.y=y


class Line:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

    def draw(self,canvas,fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y,self.p2.x,self.p2.y, fill=fill_color,width=2
        )
        #Finally, pack the canvas again
        canvas.pack(fill=BOTH, expand=1)



    
        
