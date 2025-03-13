stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
import random
fruits=['apple','banana','mango','orange','sapota','grapes']
lives=6
selected_fruit=random.choice(fruits)
display=[]
for i in selected_fruit:
    display+='_'
print(display)
game_over=False
while not game_over:
    guss_letter=input("guss a letter :").lower()
    for position in range(len(selected_fruit)):
        letter=selected_fruit[position]
         
        if letter==guss_letter:
            display[position]=guss_letter
    print(display)
    if guss_letter not in selected_fruit:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose the game")
    if '_' not in display:
        game_over=True
        print("you win")
    print(stages[lives])
            
    
 
    
        
    
    
    
 
