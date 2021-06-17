import tkinter as tk
import random


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    
    draw_sky(canvas)

    draw_ground(canvas)

    draw_grass(canvas)

    draw_clouds(canvas)
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    tree_center = scene_left + 500
    tree_top = scene_top + 200
    tree_height = 150
    draw_pine_tree(canvas, tree_center, tree_top, tree_height)

    tree_center2 = scene_left + 250
    tree_top2 = scene_top + 200
    tree_height2 = 150
    draw_pine_tree(canvas, tree_center2, tree_top2, tree_height2)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas):
    canvas.create_rectangle(0,0,799,499, fill='deepSkyBlue',outline='')

def draw_ground(canvas):
    canvas.create_rectangle(0,300,800,800, fill='tan4',outline='')

def draw_clouds(canvas):
    x1 = 50
    for _ in range (10):

        x1 = random.randint(50, 150)
        y1 = random.randint(75, 125)
        x2 = random.randint(150, 200)
        y2 = random.randint(125, 135)
        color = random.choice(['white','snow3','snow2'])
        canvas.create_oval(x1,y1,x2,y2, fill=f'{color}',outline='')

    for _ in range(10):
        x3 = random.randint(500, 545)
        y3 = random.randint(130, 155)
        x4 = random.randint(545, 600)
        y4 = random.randint(155, 165)
        color = random.choice(['white','snow3','snow2'])
        canvas.create_oval(x3,y3,x4,y4, fill=f'{color}',outline='')
    
    for _ in range(10):
        x5 = random.randint(300, 350)
        y5 = random.randint(130, 155)
        x6 = random.randint(350, 425)
        y6 = random.randint(155, 165)
        color = random.choice(['white','snow3','snow2'])
        canvas.create_oval(x5,y5,x6,y6, fill=f'{color}',outline='')
        

def draw_grass(canvas):
    i = 0
    x1 = 0
    for i in range (3000):
        x1 += random.randint(2,5)
        y1 = random.randint(449, 599)

        color = random.choice(['green', 'green3', 'green1'])
        canvas.create_rectangle(x1,y1,x1+4,y1-85, fill=f"{color}",outline='')

def draw_pine_tree(canvas, peak_x, peak_y, height):
    """Draw a single pine tree.
    Parameters
        canvas: The tkinter canvas where this
            function will draw a pine tree.
        peak_x, peak_y: The x and y location in pixels where
            this function will draw the top peak of a pine tree.
        height: The height in pixels of the pine tree that
            this function will draw.
    Return: nothing
    """
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")


    

# Call the main function so that
# this program will start executing.
main()