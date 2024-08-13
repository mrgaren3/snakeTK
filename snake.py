from tkinter import *
import random
GAME_WIDTH,GAME_HEIGHT,SPEED,SPACE_SIZE,BODY_PARTS=800,800,70,35,3
SNAKE_COLOR,FOOD_COLOR,BACKGROUND_COLOR='green','red','black'

class Snake:
    def __init__(self):
        self.bodysize=BODY_PARTS
        self.coordinate=[]
        self.sqaures=[]
        for i in range(BODY_PARTS):
            self.coordinate.append([0,0])
        for x,y in self.coordinate:
            square=canvs.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
            self.sqaures.append(square)
class Food:
    def __init__(self):
        x=random.randint(0,int(GAME_WIDTH/SPACE_SIZE)-1)*SPACE_SIZE
        y=random.randint(0,int(GAME_HEIGHT/SPACE_SIZE)-1)*SPACE_SIZE
        self.coordinate=[x,y]
        canvs.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag='food')
def game_over():
    canvs.delete(ALL)
    canvs.create_text(canvs.winfo_width()/2,canvs.winfo_height()/2,font=('ink',70),
                      text="game over NOOB",tag='gaveover',fill='red')
def change_direction(new_direction):
    global direct
    if new_direction == 'left':
        if direct !='right':
            direct=new_direction
    elif new_direction == 'right':
        if direct !='left':
            direct=new_direction
    elif new_direction == 'up':
        if direct !='down':
            direct=new_direction
    elif new_direction == 'down':
        if direct !='up':
            direct=new_direction
def next_turn(snake,food):
    x,y=snake.coordinate[0]
    if direct =='up':
        y-=SPACE_SIZE
    elif direct =='down':
        y+=SPACE_SIZE
    elif direct == 'right':
        x+=SPACE_SIZE
    elif direct=='left':
        x-=SPACE_SIZE
    snake.coordinate.insert(0,(x,y))
    square=canvs.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)
    snake.sqaures.insert(0,square)
    if  x == food.coordinate[0] and  y == food.coordinate[1]:
        global  score,SPEED
        score+=1
        if score >=45:
            SPEED=35
        elif score >=30:
            SPEED=55
        label.config(text=f"Score : {score}")
        canvs.delete('food')
        food=Food()
    else:
        del snake.coordinate[-1]
        canvs.delete(snake.sqaures[-1])
        del snake.sqaures[-1]
    if check_collign(snake):
        game_over()
    else:
        window.after(SPEED,next_turn,snake,food)
def check_collign(snake):
    x,y=snake.coordinate[0]
    if x<0 or x>=GAME_WIDTH:
        return True
    elif y<0 or y>=GAME_HEIGHT:
        return True
    for body_parts in snake.coordinate[1:]:
        if x== body_parts[0] and y==body_parts[1]:
            return True
    return False
window=Tk()
window.title('snake_game')
window.resizable(False,False)
score=0
direct='down'
label=Label(window,font=('consolas',30),text=f'Score :{score}')
label.pack()
canvs=Canvas(window,bg=BACKGROUND_COLOR,width=GAME_WIDTH,height=GAME_HEIGHT)
canvs.pack()

window.update()

window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
x=int((screen_width/2)-(window_width/2))
y=int((screen_height/2)-(window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>',lambda  event:change_direction('left'))
window.bind('<Right>',lambda  event:change_direction('right'))
window.bind('<Up>',lambda  event:change_direction('up'))
window.bind('<Down>',lambda  event:change_direction('down'))

snake=Snake()
food=Food()
next_turn(snake,food)
window.mainloop()