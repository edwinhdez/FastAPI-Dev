

import turtle

turtle.shape("turtle")

# Draw the head
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(50)
 
# Draw the eyes 
turtle.penup() 
turtle.goto(-15, -25) 
turtle.pendown() 
turtle.circle(5) 
  
# Draw the other eye 
turtle.penup() 
turtle.goto(15, -25) 
turtle.pendown() 
turtle.circle(5)  

 # Draw the nose  
turtle.penup()  								   	    # Lift up the pen 	   	     # Move to the position of the nose  	    turtle.goto(0, 0)  	    turtle.pendown()  	    turtle.dot(10, "black")  

 # Draw the mouth   turtle.penup()     # Lift up the pen     # Move to the position of the mouth     turtle.goto(-20, -40)     turtle.pendown()     turtle.setheading(-45)     turtle.forward(40)