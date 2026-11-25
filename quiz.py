from turtle import Screen

import pgzrun

TITLE="quiz game"
WIDTH=870
HEIGHT=650

marquee_box=Rect(0,10,880,80)
question_box=Rect(20,100,650,150)
timer_box=Rect(700,100,150,150)
skip_box=Rect(700,270,150,330)
ans_box1=Rect(20,270,300,150)
ans_box2=Rect(370,270,300,150)
ans_box3=Rect(20,450,300,150)
ans_box4=Rect(370,450,300,150)

score=0
time_left=10
question_file_name="questions.txt"
marquee_message=""
is_game_over=False
answer_boxes=[ans_box1,ans_box2,ans_box3,ans_box4]
questions=[]
question_count=0
question_index=0

def draw():
    global marquee_message
    screen.clear()
    screen.fill(color="black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "navy blue")
    screen.draw.filled_rect(timer_box, "navy blue")
    screen.draw.filled_rect(skip_box, "red")

    for i in answer_boxes:
        screen.draw.filled_rect(i, "green")

    marquee_message= "Welcome To Quiz Master  "+f"Q: {question_index} of {question_count}"

    screen.draw.textbox(marquee_message,marquee_box,color="white")
    screen.draw.textbox("skip",skip_box,color="red",angle=-90)
    screen.draw.textbox(str(time_left),timer_box,shadow=(0.5,0.5),scolor="black")
    screen.draw.textbox(question[0].strip(),question_box,color="navy blue",shadow=(0.5,0.5),scolor="black")

    index=1
    for i in answer_boxes:
        screen.draw.textbox(question[index].strip(),i,color="black")
        index= index+1

    
def move_marquee():
    marquee_box.x=marquee_box.x-2
    if marquee_box.right<0:
        marquee.box.left=WIDTH
    










pgzrun.go()
