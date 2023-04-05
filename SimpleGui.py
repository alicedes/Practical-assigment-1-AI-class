import pygame

pygame.init()

WINDOWSIZE=(1000,800)
PURPLE=(186,85,211)
BLACK=(0,0,0)
WHITE=(255,255,255)

running=True
screen= pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("4x6 Checkers")
clock = pygame.time.Clock()
gui_font = pygame.font.SysFont("Arial", 20)

buttons = []
#https://pythonprogramming.altervista.org/buttons-in-pygame/
class Button:
	def __init__(self,text,width,height,pos,elevation):
		#Core attributes 
		self.pressed = False
		self.elevation = elevation
		self.dynamic_elecation = elevation
		self.original_y_pos = pos[1]
 
		# top rectangle 
		self.top_rect = pygame.Rect(pos,(width,height))
		self.top_color = '#475F77'
 
		# bottom rectangle 
		self.bottom_rect = pygame.Rect(pos,(width,height))
		self.bottom_color = '#354B5E'
		#text
		self.text = text
		self.text_surf = gui_font.render(text,True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
		buttons.append(self)
 
	def change_text(self, newtext):
		self.text_surf = gui_font.render(newtext, True,'#FFFFFF')
		self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
 
	def draw(self):
		# elevation logic 
		self.top_rect.y = self.original_y_pos - self.dynamic_elecation
		self.text_rect.center = self.top_rect.center 
 
		self.bottom_rect.midtop = self.top_rect.midtop
		self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
 
		pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
		pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
		screen.blit(self.text_surf, self.text_rect)
		self.check_click()
 
	def check_click(self):
		mouse_pos = pygame.mouse.get_pos()
		if self.top_rect.collidepoint(mouse_pos):
			self.top_color = '#D74B4B'
			if pygame.mouse.get_pressed()[0]:
				self.dynamic_elecation = 0
				self.pressed = True
				self.change_text(f"{self.text}")
			else:
				self.dynamic_elecation = self.elevation
				if self.pressed == True:
					print('click')
					self.pressed = False
					self.change_text(self.text)
		else:
			self.dynamic_elecation = self.elevation
			self.top_color = '#475F77'

button1 = Button('Start',400,80,(325,300),5)
button2 = Button('Help',400,80,(325,390),5)
button3 = Button('Quit',400,80,(325,480),5)

def buttons_draw():
	for b in buttons:
		b.draw()

#https://www.youtube.com/watch?v=vnd3RfeG3NM
#board


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False  
    screen.fill(PURPLE)
    buttons_draw()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
