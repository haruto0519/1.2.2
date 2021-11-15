#-----import statements-----
import random as rand
import turtle as trtl
import leaderboard as lb
spot = trtl.Turtle()
import turtle as score_writer
counter=trtl.Turtle()
wn=trtl.Screen()
spot.showturtle()
spot.shape("circle")
spot.color("red")
spot.speed(10)
score = 0
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input ("Please enter your name:")

counter.pencolor("white")
score_writer.pencolor("white")
font_setup = ("Helvetica", 20, "normal")
different_sizes = [.5, .7, .9, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3]
differnet_colors = ["white", "pink", "blue", "red", "orange", "yellow"]

def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) <= 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

def clicked(x, y):
    colors = rand.randint(0,5)
    spot.color(differnet_colors[colors])
    size = rand.randint(0,12)
    spot.shapesize(different_sizes[size])
    global score
    score += 1
    new_xpo = rand.randint(-380,380)
    new_ypo = rand.randint(-280,280)
    spot.penup()
    spot.goto(new_xpo, new_ypo) 
    #update_score
    score_writer.clear()
    score_writer.goto(-300,200)
    score_writer.write("score: ", font=font_setup)
    score_writer.goto(-220,200)
    score_writer.write(score, font=font_setup)
    
def countdown():
  global timer, timer_up
  counter.clear()
  counter.penup()
  counter.hideturtle()
  counter.goto(150,200)
  if timer <= 0:
    counter.write("times up",font=font_setup)
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

spot.onclick(clicked)


#timer shower(was on textbook)
score_writer.penup()
timer = 10
counter_interval = 1000   
timer_up = False
score_writer.penup()
score_writer.hideturtle()

wn.bgcolor("black")
wn.ontimer(countdown, counter_interval)
wn = trtl.Screen()
wn.mainloop()