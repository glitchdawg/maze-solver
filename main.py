from graphics import Window , Line, Point
def main():
    win=Window(800,600)
    l=Line(Point(50,50),Point(400,400))
    print("running...")
    win.draw_line(l,"black")

    win.wait_for_close()
    print("closing...")
main()