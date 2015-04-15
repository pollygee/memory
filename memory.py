# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, click, state
    cards = 2*(range(0, 8))
    print cards
    random.shuffle(cards)
    exposed = [False] * len(cards)
    click = 0
    label.set_text("Turns = 0")
    state = 0
    
# define event handlers
def mouseclick(pos):
    global click, exposed, click_card, cards
    click += 1
    label.set_text("Turns = " + str(click // 2))
    click_card = pos[0] // 50
    if exposed[click_card] == False:
        exposed[click_card] = True
    else:
        return
    global state, card1, card2, match
    if state == 0:
        state = 1
        card1 = click_card
    elif state == 1:
        state = 2
        card2 = click_card
        if cards[card1] == cards[card2]:
            match = True
        else:
            match = False
    else:
        if match == True:
            exposed[click_card] = True
            exposed[card1] = True
        elif match == False:
            exposed[card1] = False
            exposed[card2] = False
        card1 = click_card
        state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, click_card
    #canvas_pos = [card_pos * 50 + 15, 55]
    for (card_pos, value) in enumerate(cards):
        if exposed[card_pos] == True:
            canvas_pos = [card_pos * 50 + 15, 55]
            canvas.draw_text(str(value), canvas_pos, 35, "white")
            canvas_pos[0] += (800 // 16)
        else: 
            canvas.draw_polygon([[card_pos * 50, 0], [((card_pos * 50) + 50), 0], [((card_pos * 50) + 50), 100], [(card_pos * 50), 100]], 1, "Red", "Green")
    


# frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
