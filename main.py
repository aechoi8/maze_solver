from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        #Create root widget
        self.__root = Tk()
        #set window title
        self.__root.title("My Window")
        #Create canvas with specified width and height
        self.__canvas = Canvas(self.__root, width = width, height = height)
        #Pack canvas to make it visible
        self.__canvas.pack(fill=BOTH, expand=True)
        #Initialize running state
        self.__running = False
        # Connect close method to window close button
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        # Update and redraw the window
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        #Set running state to True and keep redrawing until closed:
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        #Set running state to False to stop the loop
        self.__running = False
    
def main():
    #Create window instance and wait for it to close
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()