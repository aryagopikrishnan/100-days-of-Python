#Reeborg's World 
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def first_turn():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def next_turns():
    turn_left()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
first_turn()
next_turns()
next_turns()
next_turns()
next_turns()
next_turns()


num_of_hurdles = 6
while num_of_hurdles > 0:
    jump()
    num_of_hurdles -= 1 


# Hurdle 2: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json


def turn_right():
    turn_left()
    turn_left()
    turn_left()
  
def first_turn():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
def next_turns():
    turn_left()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
first_turn()


while at_goal() != True:
    next_turns()
    

    


    


    




    

