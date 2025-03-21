"""
This is a sample program to learn drawing

"""

#import the arcade libary
import arcade

#open a window
arcade.open_window(600, 600, "Drawing Example")

#set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

#Get ready to draw
arcade.start_render()

#Drawing code goes here
#draw a rectangle
#left of 0, right of 599,
#top of 300, bottom of 0
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.color.GREEN)
arcade.draw_line(0, 0, 100, 100, arcade.color.AERO_BLUE)
#Finish drawing
arcade.finish_render()
#Keep the window open
arcade.run()
print("done")