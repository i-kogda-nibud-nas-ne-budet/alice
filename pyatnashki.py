from play import *
from random import shuffle
class Card():
    def __init__(self, x , y , number) -> None:
        self.x = x
        self.y = y
        self.number = number
        self.box = new_box(color = 'cyan', width = 240 , height = 240,
                           x = self.x, y = self.y, border_color= 'orange',
                           border_width = 5)
        self.text = new_text(color = 'black', words= str(self.number),
                             x= self.x, y= self.y)

    def check_empty(self, empty):
        return abs(self.x - empty.x + self.y - empty.y) == 250

    def change_coor(self, empty):
        if self.check_empty(empty):
            self.x,empty.x = empty.x,self.x
            self.y, empty.y = empty.y, self.y
            self.update()
            self.check_position()
            empty.update()

    def update(self):
        self.box.x = self.x
        self.text.x = self.x
        self.box.y = self.y
        self.text.y = self.y

    def check_position(self):
        self.box.color = 'cyan'
        for i in range(4):
            for j in range(4):
                if int(self.text.words) == j+4*i+1 and self.x == -350 + 250*j and self.y == 370 - 250*i:
                    self.box.color = 'lime'

class Empty():
    def __init__(self, x , y) -> None:
        self.x = x
        self.y = y
        self.box = new_box(color = 'black', width = 240 , height = 240,
                           x = self.x, y = self.y, border_color= 'black',
                           border_width = 5)
    def update(self):
        self.box.x = self.x
        self.box.y = self.y


set_backdrop('black')
cards = []
card_shuffle = [i for i in range(1,15+1)]
shuffle(card_shuffle)
for i in range(4):
    for j in range(4):
        if not(i==j==3):
            card = Card(x = -350 + 250*j, y = 370 - 250*i, number=card_shuffle[j+4*i])
            card.check_position()
            cards.append(card)
        else:
            empty = Empty(x = -350 + 250*j, y = 370 - 250*i)



@repeat_forever
def game():
    lime_num = 0
    for card in cards:
        if card.box.color == 'lime':
            lime_num += 1
        if card.box.is_clicked:
            card.change_coor(empty)
    if lime_num == 15:
        for card in cards:
            card.box.start_physics()
start_program()