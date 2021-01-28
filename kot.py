import pygame
from monster import Monster
from die import Die
from button import Button
from card import Card
from random import seed
from random import randint

BLACK = (0, 0, 0)
GREEN = (0, 204, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 247, 120)
CYAN = (150, 255, 255)
 
pygame.init()
size = (900, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("")
done = False
clock = pygame.time.Clock()
seed(30)

purple_x = 190
purple_y = 320

red_x = 340
red_y = 370

green_x = 490
green_y = 370

blue_x = 640
blue_y = 320


# Declare Sprites
purple_sprite = pygame.image.load('data/purple.png').convert_alpha()
red_sprite = pygame.image.load('data/red.png').convert_alpha()
green_sprite = pygame.image.load('data/green.png').convert_alpha()
blue_sprite = pygame.image.load('data/blue.png').convert_alpha()
claw_sprite = pygame.image.load('data/claw.png').convert_alpha()
die_heart_sprite = pygame.image.load('data/die_heart.png').convert_alpha()
lightning_sprite = pygame.image.load('data/lightning.png').convert_alpha()
vp_sprite = pygame.image.load('data/vp.png').convert_alpha()
health_sprite = pygame.image.load('data/heart.png').convert_alpha()
energy_sprite = pygame.image.load('data/energy.png').convert_alpha()


# Make some monsters
monsters = [Monster("purple", 10, 0, 0, purple_sprite, purple_x, purple_y, BLACK, True, False), 
Monster("red", 10, 0, 0, red_sprite, red_x, red_y, RED, True, False),
Monster("green", 10, 0, 0, green_sprite, green_x, green_y, GREEN, True, False),
Monster("blue", 10, 0, 0, blue_sprite, blue_x, blue_y, BLUE, True, False)]

# Fonts
myfont = pygame.font.Font("data/8bitfont.ttf", 15)
my_big_font = pygame.font.Font("data/8bitfont.ttf", 20)

# Title text
kot_title = my_big_font.render('King of Tokyo', False, (0, 0, 0))

# Test function
def say_hi():
    print("Hi")


# Important variables
rolls = 0
allowed_rolls = 3
num_dice = 6
tokyo_index = 3
num_players = 0
res = True

for monster in monsters:
    if monster.alive:
        num_players += 1


def roll():
    global rolls, allowed_rolls, num_dice, dice

    if rolls >= allowed_rolls:
        for i in range(6):
            if not dice[i].kept:
                dice[i].flipDie()
            
        return

    for i in range(num_dice):
        num = randint(1, 6)
        if num == 1:
            dice[i].updateLabel("1")
        elif num == 2:
            dice[i].updateLabel("2")
        elif num == 3:
            dice[i].updateLabel("3")
        elif num == 4:
            dice[i].updateLabel("<3")
        elif num == 5:
            dice[i].updateLabel("!")
        else:
            dice[i].updateLabel("*")
    
    rolls += 1

    if rolls == allowed_rolls:
        resolve()
        

def resolve():
    global end_turn_button, dice, rolls, allowed_rolls, res

    if end_turn_button.text is "Resolve":
        if rolls == 0:
            return

        rolls = allowed_rolls
        res = False

        for i in range(6):
            if not dice[i].kept:
                dice[i].flipDie()

        end_turn_button.updateLabel("Done")
    else:


        rolls = 0
        res = True

        for i in range(6):
            dice[i].flipDie()

        handleTurn()
        
        end_turn_button.updateLabel("Resolve")

def handleTurn():
    print("turn handled!")

def updatePositions():
    global tokyo_index, num_players, monsters

    if num_players is 4:
        if tokyo_index == 0:
            # Purple in tokyo
            monsters[0].x = 420
            monsters[0].y = 120

            monsters[1].x = 220
            monsters[1].y = 290

            monsters[2].x = 420
            monsters[2].y = 340

            monsters[3].x = 610
            monsters[3].y = 290
        elif tokyo_index == 1:
            # Red in tokyo
            monsters[1].x = 420
            monsters[1].y = 120

            monsters[0].x = 220
            monsters[0].y = 290

            monsters[2].x = 420
            monsters[2].y = 340

            monsters[3].x = 610
            monsters[3].y = 290
        elif tokyo_index == 2:
            # Green in tokyo
            monsters[2].x = 420
            monsters[2].y = 120

            monsters[0].x = 220
            monsters[0].y = 290

            monsters[1].x = 420
            monsters[1].y = 340

            monsters[3].x = 610
            monsters[3].y = 290
        else:
            # Blue in tokyo
            monsters[3].x = 420
            monsters[3].y = 120

            monsters[0].x = 220
            monsters[0].y = 290

            monsters[1].x = 420
            monsters[1].y = 340

            monsters[2].x = 610
            monsters[2].y = 290

    # still need for num_players < 4

            

updatePositions()
    

# Make some dice!
dice = [Die("?", myfont, BLACK, (190, 504, 70, 70), GREEN, CYAN, None),
Die("?", myfont, BLACK, (280, 504, 70, 70), GREEN, CYAN, None),
Die("?", myfont, BLACK, (370, 504, 70, 70), GREEN, CYAN, None),
Die("?", myfont, BLACK, (460, 504, 70, 70), GREEN, CYAN, None),
Die("?", myfont, BLACK, (550, 504, 70, 70), GREEN, CYAN, None),
Die("?", myfont, BLACK, (640, 504, 70, 70), GREEN, CYAN, None),
# Die("?", myfont, BLACK, (725, 504, 70, 70), GREEN, CYAN, say_hi),
# Die("?", myfont, BLACK, (815, 504, 70, 70), GREEN, CYAN, say_hi)
]

roll_button = Button("Roll!", myfont, BLACK, (20, 504, 110, 70), GREEN, CYAN, roll)
end_turn_button = Button("Resolve", myfont, BLACK, (770, 504, 110, 70), GREEN, CYAN, resolve)

cards = [Card("-*-", "card1", 0, 0, 0, 0, myfont, BLACK, (10, 10, 80, 120), YELLOW, CYAN, say_hi, False),
Card("-*-",  "card2", 0, 0, 0, 0, myfont, BLACK, (10, 140, 80, 120), YELLOW, CYAN, say_hi, False),
Card("-*-",  "card3", 0, 0, 0, 0, myfont, BLACK, (10, 270, 80, 120), YELLOW, CYAN, say_hi, False)]
 
# Game loop
while not done:

    # Mouse position
    pos = pygame.mouse.get_pos()

    # Update game elements

    for die in dice:
        die.update(pos)

    for card in cards:
        card.update(pos)

    roll_button.update(pos)
    end_turn_button.update(pos)


    # Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tokyo_index = 0
                updatePositions()
            elif event.key == pygame.K_2:
                tokyo_index = 1
                updatePositions()
            elif event.key == pygame.K_3:
                tokyo_index = 2
                updatePositions()
            elif event.key == pygame.K_4:
                tokyo_index = 3
                updatePositions()

        if rolls and res:
            for die in dice:
                die.get_event(event)
        

        for card in cards:
            card.get_event(event)

        roll_button.get_event(event)
        end_turn_button.get_event(event)

 

    # Draw elements on the screen
    screen.fill(WHITE)

    # Draw title
    screen.blit(kot_title,(360,25))

    pygame.draw.line(screen, BLACK, [0, 480], [900, 480], 4)
    pygame.draw.line(screen, BLACK, [0, 597], [900, 597], 4)
    pygame.draw.line(screen, BLACK, [1, 480], [1, 600], 4)
    pygame.draw.line(screen, BLACK, [897, 480], [897, 600], 4)
    pygame.draw.line(screen, BLACK, [150, 480], [150, 600], 4)
    pygame.draw.line(screen, BLACK, [750, 480], [750, 600], 4)
    
    for monster in monsters:
        monster.draw(screen)
    
    for die in dice:
        die.draw(screen)

    for card in cards:
        card.draw(screen)

    roll_button.draw(screen)
    end_turn_button.draw(screen)
 
    pygame.display.flip()
     
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()