from decimal import ROUND_05UP, Rounded
from distutils.cmd import Command
from tkinter import * 
from tkinter import colorchooser
from turtle import width
import math
from tkinter import simpledialog
import pickle
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw
import PIL.ImageGrab as ImageGrab
import tkinter.messagebox as messagebox





class paintBrush:
    def __init__(self,width,height,title):
        self.screen = Tk()
        self.screen.title(title)
        self.screen.geometry(str(width)+'x'+str(height))
        self.brush_color = 'black'
        self.eraser_color = 'white'
        self.last_x,self.last_y = None,None
        self.shape_id = None
        self.select_start = None
        self.select_end = None
        self.scale = 1.1
        self.fill_color = None
        self.level = 100 
        self.scale1 = 1.2 
        self.bezier_mode = False
        self.control_points = []





        #buttons
        self.button_area = Frame(self.screen,width=width,height=100,bg="teal")
        self.button_area.pack()
        #create canvas
        self.canvas = Canvas(self.screen,width=width,height=height,bg="white")
        self.canvas.pack()
   
        #select color button
        self.select_color_button = Button(self.button_area,text="Select Color",
                             command= self.select_color,bg="grey",width = 19, height = 1)
        self.select_color_button.place(x=300,y=60)
        #clear button
        self.clear_button = Button(self.button_area,text="Clear",
                             command= self.clear_canvas,bg="yellow",width = 4, height = 1)
        self.clear_button.place(x=5,y=5)
        #Brush buton
        self.select_color_button = Button(self.button_area,text="b\nr\nu\ns\nh",
                             command= self.on_BrushButton_pressed,bg="grey",width = 3, height = 5)
        self.select_color_button.place(x=474,y=6)
        #Eraser buton
        self.select_eraser_button = Button(self.button_area,text="Eraser",
                             command= self.on_EraserButton_pressed,bg="orange",width = 5, height = 1)
        self.select_eraser_button.place(x=5,y=38)
        #multiple Eraser buton
        self.select_eraser2_button = Button(self.button_area,text="Multiple Color Eraser",
                             command= self.set_eraser_color,bg="turquoise",width = 15, height = 1)
        self.select_eraser2_button.place(x=5,y=68)
       #width 7 buton
        self.select_width7_button = Button(self.button_area,text="Brush Width 7",
                             command= self.on_width7Button_pressed,bg="medium purple",width = 11, height = 1)
        self.select_width7_button.place(x=510,y=5)
       #width 10 buton
        self.select_width10_button = Button(self.button_area,text="Brush Width 10",
                             command= self.on_width10Button_pressed,bg="medium sea green",width = 11, height = 1)
        self.select_width10_button.place(x=510,y=37)
        #width 13 buton
        self.select_width13_button = Button(self.button_area,text="Brush Width 13",
                             command= self.on_width13Button_pressed,bg="dark goldenrod",width = 11, height = 1)
        self.select_width13_button.place(x=510,y=67)
        #Select Area: Select a given area in a rectangle which can be treated as a single unit.
        self.select_area_button = Button(self.button_area, text="Select Area", 
                                         command = self.on_selectAreaButton_pressed,
                                        bg="salmon", width=8, height=1)
        self.select_area_button.place(x=55, y=38)
        #magnifier
        # Zoom in button
        self.zoom_in_button = Button(self.button_area, text="Zoom In", command=self.zoom_in, bg="light grey", width=7, height=1)
        self.zoom_in_button.place(x=48, y=5)
        # Zoom out button
        self.zoom_out_button = Button(self.button_area, text="Zoom Out", command=self.zoom_out, bg="light grey", width=7, height=1)
        self.zoom_out_button.place(x=112, y=4)
        # Color Picker button
        self.color_picker_button = Button(self.screen, text="Color Picker", 
                                          command=self.pick_color)
        self.color_picker_button.pack()
        #fileed region button
        self.fill_region_button = Button(self.button_area, text="Fill\nRegion",
                        command=self.on_fill_region_button_pressed,bg="orchid",width=5, height=3)
        self.fill_region_button.place(x=125, y=37)
        #load button
        self.load_button = Button(self.button_area, text="load canvas", command=self.load_canvas
                                  , bg="yellow green",width=10, height=1)
        self.load_button.place(x=180,y=5)
        # save button
        self.save_button = Button(self.button_area, text="save canvas", command=self.save_canvas
                                  , bg="yellow green",width=10, height=1)
        self.save_button.place(x=180,y=37)
        # Help button
        self.Help_button = Button(self.button_area, text="H\nE\nL\nP", command=self.display_help
                                  , bg="medium purple",width=2, height=5)
        self.Help_button.place(x=447,y=6)
        # Text button
        self.Text_button = Button(self.button_area, text="T\nE\nX\nT", command=self.on_text_button_pressed
                                  , bg="pink",width=2, height=5)
        self.Text_button.place(x=270,y=5)
        # bezier button
        self.bezier_button = tk.Button(self.button_area, text="Bezier", command=self.on_bezier_button_pressed, bg="salmon",width=10, height=1)
        self.bezier_button.place(x=180, y=67)

        










        #color button
        #red
        self.red_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("red") ,bg="red",width = 2, height = 1)
        self.red_button.place(x=300,y=5)
        #yellow
        self.yellow_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("yellow") ,bg="yellow",width = 2, height = 1)
        self.yellow_button.place(x=320,y=5)
        #orange
        self.orange_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("orange") ,bg="orange",width = 2, height = 1)
        self.orange_button.place(x=340,y=5)
        #green
        self.green_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("green") ,bg="green",width = 2, height = 1)
        self.green_button.place(x=360,y=5)
        #blue
        self.blue_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("blue") ,bg="blue",width = 2, height = 1)
        self.blue_button.place(x=380,y=5)
        #grey
        self.grey_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("grey") ,bg="grey",width = 2, height = 1)
        self.grey_button.place(x=400,y=5)
        #purple
        self.purple_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("purple") ,bg="purple",width = 2, height = 1)
        self.purple_button.place(x=420,y=5)
        #pink
        self.pink_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("pink") ,bg="pink",width = 2, height = 1)
        self.pink_button.place(x=300,y=30)
        #brown
        self.brown_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("brown") ,bg="brown",width = 2, height = 1)
        self.brown_button.place(x=320,y=30)
        #magenta
        self.magenta_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("magenta") ,bg="magenta",width = 2, height = 1)
        self.magenta_button.place(x=340,y=30)
        #black 
        self.black_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("black") ,bg="black",width = 2, height = 1)
        self.black_button.place(x=360,y=30)
        #white 
        self.white_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("white") ,bg="white",width = 2, height = 1)
        self.white_button.place(x=380,y=30)
        #darkorchid 
        self.darkorchid_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("darkorchid") ,bg="darkorchid",width = 2, height = 1)
        self.darkorchid_button.place(x=400,y=30)
        #yellow green 
        self.yellow_green_button = Button(self.button_area,text="",
                             command=lambda:self.sel_col_but("yellow green") ,bg="yellow green",width = 2, height = 1)
        self.yellow_green_button.place(x=420,y=30)
        












        #filled color button
        self.filled_button = Button(self.button_area,text="Filled Color Shapes",
                             command = self.on_CircleButton_pressed,bg="dark khaki",width = 38, height = 1)
        self.filled_button.place(x=610,y=67)
         #circle button
        self.circle2_button = Button(self.button_area,text="Circle",
                             command = self.on_CircleButton2_pressed,bg="salmon",width = 5, height = 1)
        self.circle2_button.place(x=840,y=5)
         # Rectangle button
        self.rectangle2_button = Button(self.button_area, text="Rectangle", 
                             command=self.on_RectangleButton2_pressed, bg="salmon",width=8, height=1)
        self.rectangle2_button.place(x=772, y=5)
        # Oval button
        self.oval2_button = Button(self.button_area, text="Oval", 
                             command=self.on_OvalButton2_pressed, bg="salmon",width=4, height=1)
        self.oval2_button.place(x=727, y=5)
        # square button
        self.square2_button = Button(self.button_area, text="Square", 
                             command=self.on_SquareButton2_pressed, bg="salmon",width=5, height=1)
        self.square2_button.place(x=613, y=5)
        # straightLine button
        self.straightLine_button = Button(self.button_area, text="Line", 
                             command=self.on_StraightLineButton_pressed, bg="salmon",width=5, height=1)
        self.straightLine_button.place(x=840, y=37)
        # Triangle button
        self.Triangle2_button = Button(self.button_area, text="Triangle", 
                             command=self.on_TriangleButton2_pressed, bg="salmon",width=5, height=1)
        self.Triangle2_button.place(x=613, y=37)
        #Star button
        self.Star2_button = Button(self.button_area, text="star", 
                             command=self.on_StarButton2_pressed, bg="salmon",width=5, height=1)
        self.Star2_button.place(x=725, y=37)
        #Pentagon button
        self.pentagon2_button = Button(self.button_area, text="pentagon", 
                             command=self.on_pentagonButton2_pressed, bg="salmon",width=7, height=1)
        self.pentagon2_button.place(x=775, y=37)
        #Hexagon button
        self.hexagon2_button = Button(self.button_area, text="Hexagon", 
                             command=self.on_hexagonButton2_pressed, bg="salmon",width=6, height=1)
        self.hexagon2_button.place(x=667, y=37)
        # n points polygon button
        self.n_polygon2_button = Button(self.button_area, text="n polygon", 
                             command=self.on_n_polygonButton2_pressed, bg="salmon",width=7, height=1)
        self.n_polygon2_button.place(x=662, y=5)











        #un filled color button
        self.unfilled_button = Button(self.button_area,text="Un Filled Color Shapes",
                             command = self.on_CircleButton_pressed,bg="dark khaki",width = 38, height = 1)
        self.unfilled_button.place(x=910,y=67)
        
        #circle button
        self.circle_button = Button(self.button_area,text="Circle",
                             command = self.on_CircleButton_pressed,bg="salmon",width = 5, height = 1)
        self.circle_button.place(x=910,y=5)
        # Rectangle button
        self.rectangle_button = Button(self.button_area, text="Rectangle", 
                             command=self.on_RectangleButton_pressed, bg="salmon",width=8, height=1)
        self.rectangle_button.place(x=910, y=37)
        # Oval button
        self.oval_button = Button(self.button_area, text="Oval", 
                             command=self.on_OvalButton_pressed, bg="salmon",width=5, height=1)
        self.oval_button.place(x=985, y=37)
        # square button
        self.square_button = Button(self.button_area, text="Square", 
                             command=self.on_SquareButton_pressed, bg="salmon",width=5, height=1)
        self.square_button.place(x=1039, y=37)
        # straightLine button
        self.straightLine_button = Button(self.button_area, text="Line", 
                             command=self.on_StraightLineButton_pressed, bg="salmon",width=5, height=1)
        self.straightLine_button.place(x=1090, y=37)
        # Triangle button
        self.Triangle_button = Button(self.button_area, text="Triangle", 
                             command=self.on_TriangleButton_pressed, bg="salmon",width=5, height=1)
        self.Triangle_button.place(x=960, y=5)
        #Star button
        self.Star_button = Button(self.button_area, text="star", 
                             command=self.on_StarButton_pressed, bg="salmon",width=5, height=1)
        self.Star_button.place(x=1143, y=37)
        #Pentagon button
        self.pentagon_button = Button(self.button_area, text="pentagon", 
                             command=self.on_pentagonButton_pressed, bg="salmon",width=7, height=1)
        self.pentagon_button.place(x=1010, y=5)
        ##Hexagon button
        self.hexagon_button = Button(self.button_area, text="Hexagon", 
                             command=self.on_hexagonButton_pressed, bg="salmon",width=6, height=1)
        self.hexagon_button.place(x=1073, y=5)
        # n points polygon button
        self.n_polygon_button = Button(self.button_area, text="n polygon", 
                             command=self.on_n_polygonButton_pressed, bg="salmon",width=7, height=1)
        self.n_polygon_button.place(x=1130, y=5)
       








        #bind
        self.canvas.bind("<B1-Motion>",self.brush_draw)
        self.canvas.bind("<ButtonRelease-1>",self.brush_draw_end)
        # bind mouse click event for color picker tool
        self.canvas.bind("<Button-1>", self.get_color)
        # for filled region
        self.canvas.bind("<Button-1>", self.on_canvas_region_click)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)








    def on_bezier_button_pressed(self):
        self.bezier_mode = not self.bezier_mode
        if self.bezier_mode:
            self.bezier_button.config(relief="sunken")
        else:
            self.bezier_button.config(relief="raised")

    def on_canvas_click(self, event):
        if self.bezier_mode:
            self.control_points.append((event.x, event.y))

    def on_canvas_drag(self, event):
        if self.bezier_mode and len(self.control_points) == 3:
            self.control_points.append((event.x, event.y))
            self.canvas.delete("current_curve")
            self.canvas.create_line(self.control_points, smooth=True, fill="black", tags="current_curve")

    def on_canvas_release(self, event):
        if self.bezier_mode and len(self.control_points) == 4:
            self.control_points.append((event.x, event.y))
            self.canvas.create_line(self.control_points, smooth=True, fill="black")
            self.control_points = []






    #text
    def on_text_button_pressed(self):
        text = simpledialog.askstring("Text Input", "Enter your text:")
        if text:
            x = self.canvas.winfo_width() // 2
            y = self.canvas.winfo_height() // 2
            self.canvas.create_text(x, y, text=text, fill="black",font = ("Arial",80))
    #help button
    def display_help(self):
        messagebox.showinfo("Help", "Help information for Paint Brush.\n1: Tool Description\n2: Keyboard shortcuts\n3: Usage instructions\n4: Troubleshooting\n5: About")
    #save
    def save_canvas(self):
        #file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        #if file_path:
        #    ImageGrab.grab().save(file_path)
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if file_path:
            # Calculate the bounding box of the canvas
            x = self.canvas.winfo_rootx() + self.canvas.winfo_x()
            y = self.canvas.winfo_rooty() + self.canvas.winfo_y()
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()

            # Take a screenshot of the canvas area only
            image = ImageGrab.grab(bbox=(x-5, y-101, x + width, y + height-101))
            #resized_image = image.resize((width // 5, height // 5))
            # Set the DPI value to match the screen's DPI
            image.save(file_path)

    #load
    def load_canvas(self):
        file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        if file_path:
            self.canvas.delete("all")
            self.canvas.image = PhotoImage(file=file_path)
            self.canvas.create_image(0, 0, anchor="nw", image=self.canvas.image)
              

    #filled region 
    def on_fill_region_button_pressed(self):
        color = colorchooser.askcolor(title="Select Fill Color")
        if color:
            self.fill_color = color[1]

    def on_canvas_region_click(self, event):
        shape_id = self.canvas.find_closest(event.x, event.y)
        self.fill_area(shape_id)

    def fill_area(self, shape_id):
        self.canvas.itemconfig(shape_id, fill=self.fill_color)
    #color picker
    def pick_color(self):
        color = colorchooser.askcolor(title="Pick a color")
        if color:
            self.canvas.config(bg=color[1])

    def get_color(self, event):
        x = event.x
        y = event.y
        items = self.canvas.find_closest(x, y)
        if items:
            item = items[-1]
            color = self.canvas.itemcget(item, "fill")
            print("Selected color:", color)

 



    #magnifier
    def zoom_in(self):
         self.level *= self.scale1
         self.canvas.scale("all", 0, 0, self.scale1, self.scale1)

    def zoom_out(self):
        self.level /= self.scale1
        self.canvas.scale("all", 0, 0, 1 / self.scale1, 1 / self.scale1)

    def apply_canvas_scale(self):
        self.canvas.scale("all", 0.2, 0.2, self.scale, self.scale)
    
    #select area
    def on_selectAreaButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<ButtonPress-1>", self.on_sel_Area_Press)
        self.canvas.bind("<B1-Motion>", self.on_Sel_Area_Move)
        self.canvas.bind("<ButtonRelease-1>", self.on_Sel_Area_rel)

    def on_sel_Area_Press(self, event):
        self.select_start = (event.x, event.y)

    def on_Sel_Area_Move(self, event):
        if self.select_start is not None:
            self.select_end = (event.x, event.y)
            self.update_sel_area()

    def on_Sel_Area_rel(self, event):
        if self.select_start is not None:
            self.select_end = (event.x, event.y)
            self.update_sel_area()
            #self.process_selected_area()

    def update_sel_area(self):
        self.canvas.delete("selected_part")

        if self.select_start is not None and self.select_end is not None:
            x1, y1 = self.select_start
            x2, y2 = self.select_end
            self.canvas.create_rectangle(x1, y1, x2, y2, outline="blue", width=3,
                                        tags="selected_part")
    
    #def process_selected_area(self):
    #    x1, y1 = self.select_start
    #    x2, y2 = self.select_end
    #    print("Selected area coordinates:", x1, y1, x2, y2)




    #on eraser button preseed
    def on_EraserButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_eraser)
        self.canvas.bind("<ButtonRelease-1>",self.draw_eraser_end)
    def draw_eraser(self,event):
        x = event.x
        y = event.y
        self.canvas.create_rectangle(x-10,y-10,x+10,y+10,
                                     fill = self.eraser_color ,outline = '' )

    def draw_eraser_end(self,event):
         self.last_x,self.last_y = None,None
    def set_eraser_color(self):
        color = colorchooser.askcolor()[1] 
        if color:
            self.eraser_color = color
    
    #width 
    # width 7
    def on_width7Button_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_width7brush)
        self.canvas.bind("<ButtonRelease-1>",self.draw_width7brush_end)
    def draw_width7brush(self,event):
        if self.last_x == None:
            self.last_x,self.last_y = event.x,event.y
            return
        self.canvas.create_line(self.last_x,self.last_y, event.x,event.y,
                               width=7,capstyle=ROUND,fill = self.brush_color)
        self.last_x,self.last_y = event.x,event.y
    def draw_width7brush_end(self,event):
        self.last_x,self.last_y = None,None
    # width 10
    def on_width10Button_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_width10brush)
        self.canvas.bind("<ButtonRelease-1>",self.draw_width10brush_end)
    def draw_width10brush(self,event):
        if self.last_x == None:
            self.last_x,self.last_y = event.x,event.y
            return
        self.canvas.create_line(self.last_x,self.last_y, event.x,event.y,
                               width=10,capstyle=ROUND,fill = self.brush_color)
        self.last_x,self.last_y = event.x,event.y
    def draw_width10brush_end(self,event):
        self.last_x,self.last_y = None,None
    # width 13
    def on_width13Button_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_width13brush)
        self.canvas.bind("<ButtonRelease-1>",self.draw_width13brush_end)
    def draw_width13brush(self,event):
        if self.last_x == None:
            self.last_x,self.last_y = event.x,event.y
            return
        self.canvas.create_line(self.last_x,self.last_y, event.x,event.y,
                               width=13,capstyle=ROUND,fill = self.brush_color)
        self.last_x,self.last_y = event.x,event.y
    def draw_width13brush_end(self,event):
        self.last_x,self.last_y = None,None


















    #filled color button
    #on circle button pressed
    def on_CircleButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_circle2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_circle2_end)
    #on rectnagle button pressed
    def on_RectangleButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_rectangle2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_rectangle2_end)
    #on oval button pressed
    def on_OvalButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_Oval2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_Oval2_end)
    #on Square button pressed
    def on_SquareButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_square2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_square2_end)
    #on Triangle button pressed
    def on_TriangleButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_triangle2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_triangle2_end)
    #on Star button pressed
    def on_StarButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_star2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_star2_end)
    #on pentagon button pressed
    def on_pentagonButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_pentagon2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_pentagon2_end)
    #on Hexagon button pressed
    def on_hexagonButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_hexagon2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_hexagon2_end)
    #on n polygon button pressed
    def on_n_polygonButton2_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>") 
        self.canvas.bind("<B1-Motion>",self.draw_n_polygon2)
        self.canvas.bind("<ButtonRelease-1>",self.draw_n_polyon2_end)















    #un filled color button
    #on brush button pressed
    def on_BrushButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.brush_draw)
        self.canvas.bind("<ButtonRelease-1>",self.brush_draw_end)
    #on circle button pressed
    def on_CircleButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_circle)
        self.canvas.bind("<ButtonRelease-1>",self.draw_circle_end)
    #on rectnagle button pressed
    def on_RectangleButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>",self.draw_rectangle_end)
    #on oval button pressed
    def on_OvalButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_Oval)
        self.canvas.bind("<ButtonRelease-1>",self.draw_Oval_end)
    #on Square button pressed
    def on_SquareButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_square)
        self.canvas.bind("<ButtonRelease-1>",self.draw_square_end)
    #on Straight line button pressed
    def on_StraightLineButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_line)
        self.canvas.bind("<ButtonRelease-1>",self.draw_line_end)
    #on Triangle button pressed
    def on_TriangleButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_triangle)
        self.canvas.bind("<ButtonRelease-1>",self.draw_triangle_end)
    #on Star button pressed
    def on_StarButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_star)
        self.canvas.bind("<ButtonRelease-1>",self.draw_star_end)
    #on pentagon button pressed
    def on_pentagonButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_pentagon)
        self.canvas.bind("<ButtonRelease-1>",self.draw_pentagon_end)
    #on Hexagon button pressed
    def on_hexagonButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>",self.draw_hexagon)
        self.canvas.bind("<ButtonRelease-1>",self.draw_hexagon_end)
    #on n polygon button pressed
    def on_n_polygonButton_pressed(self):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>") 
        self.canvas.bind("<B1-Motion>",self.draw_n_polygon)
        self.canvas.bind("<ButtonRelease-1>",self.draw_n_polyon_end)







    # filled color button
    #circle
    def draw_circle2(self,event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x,self.last_y = event.x,event.y
            return
        radius = abs(self.last_x - event.x) + abs(self.last_y - event.y)
        x1,y1 = (self.last_x - radius),(self.last_y - radius)
        x2,y2 = (self.last_x + radius),(self.last_y + radius)
        self.shape_id = self.canvas.create_oval(x1,y1,x2,y2,outline=self.brush_color,
                                   fill = self.brush_color,width = 5)
    def draw_circle2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # rectangle
    def draw_rectangle2(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        self.shape_id = self.canvas.create_rectangle(self.last_x, self.last_y, event.x, event.y,
                                                     fill=self.brush_color,outline=self.brush_color, width=5)
    def draw_rectangle2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # Oval
    def draw_Oval2(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        self.shape_id = self.canvas.create_oval(self.last_x, self.last_y, event.x, event.y,
                                 fill=self.brush_color,outline=self.brush_color, width=5)
    def draw_Oval2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # Square
    def draw_square2(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        side_length = min(abs(x2 - x1), abs(y2 - y1))

        if x2 < x1:
            x1 -= side_length
        if y2 < y1:
            y1 -= side_length

        self.shape_id = self.canvas.create_rectangle(x1, y1, x1 + side_length, y1 + side_length,
                                     fill=self.brush_color,outline=self.brush_color, width=5)

    def draw_square2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    #Triangle
    def draw_triangle2(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y

        cx = (self.last_x + event.x) // 2  
        cy = (self.last_y + event.y) // 2  
        x3 = cx - (y2 - cy)  
        y3 = cy + (x2 - cx)  

        self.shape_id = self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, x1, y1,
                                 fill = self.brush_color,outline=self.brush_color, width=5)

    def draw_triangle2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
     # Star
    def draw_star2(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        radius = abs(self.last_x - event.x) / 2
        angle = math.pi / 5  
        points = []
        for i in range(10):
            theta = i * 2 * angle - math.pi / 2
            if i % 2 == 0:
                x = cx + radius * math.cos(theta)
                y = cy + radius * math.sin(theta)
            #else:
            #    x = cx + (radius / 2) * math.cos(theta)
            #    y = cy + (radius / 2) * math.sin(theta)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color,
                                                fill=self.brush_color, width=5)

    def draw_star2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # pentagon
    def draw_pentagon2(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        radius = abs(self.last_x - event.x) / 2
        angle = 2 * math.pi / 5  
        points = []
        for i in range(5):
            theta = i * angle - math.pi / 2
            x = cx + radius * math.cos(theta)
            y = cy + radius * math.sin(theta)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color,
                                                  fill=self.brush_color,width=5)
    def draw_pentagon2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # Hexagon
    def draw_hexagon2(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        radius = abs(self.last_x - event.x) / 2
        angle = 2 * math.pi / 6  
        points = []
        for i in range(6):
            theta = i * angle
            x = cx + radius * math.cos(theta)
            y = cy + radius * math.sin(theta)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color,
                                                  fill=self.brush_color,width=5)

    def draw_hexagon2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # n polygon
    def draw_n_polygon2(self, event):
        sides = simpledialog.askinteger("Enter Sides", 
           "Enter the number of sides for the polygon:", minvalue=3)
        distance = simpledialog.askfloat("Enter Distance", 
              "Enter the distance or width of the shape:")

        if sides is None:
            return
        if self.shape_id is None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        radius = distance / 2
        angle = 2 * math.pi / sides
        points = []
        for i in range(sides):
            theta = i * angle
            x = cx + radius * math.cos(theta)
            y = cy + radius * math.sin(theta)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color,
                                                  width=5, fill=self.brush_color)

    def draw_n_polyon2_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None   

















    #un filled color button
    #circle
    def draw_circle(self,event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
        if self.last_x is None:
            self.last_x,self.last_y = event.x,event.y
            return
        radius = abs(self.last_x - event.x) + abs(self.last_y - event.y)
        x1,y1 = (self.last_x - radius),(self.last_y - radius)
        x2,y2 = (self.last_x + radius),(self.last_y + radius)
        self.shape_id = self.canvas.create_oval(x1,y1,x2,y2,
                                   outline = self.brush_color,width = 5)
    def draw_circle_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None

    # rectangle
    
    def draw_rectangle(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        self.shape_id = self.canvas.create_rectangle(self.last_x, self.last_y, event.x, event.y,
                                                     outline=self.brush_color, width=5)
    def draw_rectangle_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # Oval
    def draw_Oval(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        self.shape_id = self.canvas.create_oval(self.last_x, self.last_y, event.x, event.y,
                                                     outline=self.brush_color, width=5)
    def draw_Oval_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # Square
    def draw_square(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y
        side_length = min(abs(x2 - x1), abs(y2 - y1))

        if x2 < x1:
            x1 -= side_length
        if y2 < y1:
            y1 -= side_length

        self.shape_id = self.canvas.create_rectangle(x1, y1, x1 + side_length, y1 + side_length,
                                                 outline=self.brush_color, width=5)

    def draw_square_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # Straight Line
    def draw_line(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        self.shape_id = self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                                     fill = self.brush_color, width=5)
    def draw_line_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # Triangle
    def draw_triangle(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        x1, y1 = self.last_x, self.last_y
        x2, y2 = event.x, event.y

        cx = (self.last_x + event.x) // 2  
        cy = (self.last_y + event.y) // 2  
        x3 = cx - (y2 - cy)  
        y3 = cy + (x2 - cx)  

        self.shape_id = self.canvas.create_line(x1, y1, x2, y2, x3, y3, x1, y1,
                                            fill=self.brush_color, width=5)

    def draw_triangle_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    
    # Star
    def draw_star(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        radius = abs(self.last_x - event.x) / 2
        angle = math.pi / 5  
        points = []
        for i in range(10):
            theta = i * 2 * angle - math.pi / 2
            if i % 2 == 0:
                x = cx + radius * math.cos(theta)
                y = cy + radius * math.sin(theta)
            #else:
            #    x = cx + (radius / 2) * math.cos(theta)
            #    y = cy + (radius / 2) * math.sin(theta)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color, width=5, fill='')

    def draw_star_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # pentagon
    def draw_pentagon(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return

        cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        radius = abs(self.last_x - event.x) / 2
        angle = 2 * math.pi / 5  
        points = []
        for i in range(5):
            theta = i * angle - math.pi / 2
            x = cx + radius * math.cos(theta)
            y = cy + radius * math.sin(theta)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color, width=5, fill='')
    def draw_pentagon_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None
    # Hexagon
    def draw_hexagon(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        radius = abs(self.last_x - event.x) / 2
        angle = 2 * math.pi / 6  
        points = []
        for i in range(6):
            theta = i * angle
            x = cx + radius * math.cos(theta)
            y = cy + radius * math.sin(theta)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color, width=5, fill='')

    def draw_hexagon_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None

    # n polygon
    def draw_n_polygon(self, event):
        sides = simpledialog.askinteger("Enter Sides", 
           "Enter the number of sides for the polygon:", minvalue=3)
        distance = simpledialog.askfloat("Enter Distance", 
              "Enter the distance or width of the shape:")

        if sides is None:
            return
        if self.shape_id is None:
            self.canvas.delete(self.shape_id)

        if self.last_x is None:
            self.last_x, self.last_y = event.x, event.y
            return
        cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        radius = distance / 2
        angle = 2 * math.pi / sides
        points = []
        for i in range(sides):
            theta = i * angle
            x = cx + radius * math.cos(theta)
            y = cy + radius * math.sin(theta)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color, width=5, fill='')
        #n = int(input("Enter Number of sides: "))
        #sides = int(input("Enter Number of sides: "))
     
        #cx, cy = (self.last_x + event.x) / 2, (self.last_y + event.y) / 2
        #radius = min(abs(self.last_x - event.x), abs(self.last_y - event.y)) / 2
        #radius = math.hypot(event.x - self.last_x, event.y - self.last_y) / 2
        #angle = 2 * math.pi / sides
        #points = []
        #for i in range(sides):
        #   theta = i * angle
        #   x = cx + radius * math.cos(theta)
        #   y = cy + radius * math.sin(theta)
        #   points.append(x)
        #   points.append(y)

        #self.shape_id = self.canvas.create_polygon(points, outline=self.brush_color, width=5 , fill='')

    def draw_n_polyon_end(self,event):
        self.last_x,self.last_y = None,None
        self.shape_id = None









    


    #select color
    def sel_col_but(self,col):
        self.brush_color = col;
    #color 
    def select_color(self):
        selected_color = colorchooser.askcolor()
        if selected_color[1] is not None:
            self.brush_color = selected_color[1]
        #self.brush_color = selected_color[1]
        #if(selected_color[1]==None):

    # clear
    def clear_canvas(self):
        self.canvas.delete("all")
    def run(self):
        self.screen.mainloop()

    def brush_draw(self,event):
        if self.last_x == None:
            self.last_x,self.last_y = event.x,event.y
            return
        self.canvas.create_line(self.last_x,self.last_y, event.x,event.y,
                               width=5,capstyle=ROUND,fill = self.brush_color)
        self.last_x,self.last_y = event.x,event.y
    def brush_draw_end(self,event):
        self.last_x,self.last_y = None,None

paintBrush(1200,600,"Paint Brush").run()
 

