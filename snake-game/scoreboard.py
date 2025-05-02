from  turtle import  Turtle
ALIGNMENT="center"
FONT=('Courier', 24, 'bold')
class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score=0
		self.color("White")
		self.penup()
		self.goto(x=0, y=265)
		self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
		self.hideturtle()

	def game_over(self):
		self.goto(0,0)
		self.write("Game Over.", align=ALIGNMENT, font=FONT)
	def update_score(self):
		self.score+=1
		self.clear()
		self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)