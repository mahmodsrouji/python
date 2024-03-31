print("""
Welcome to my island!
 _;~)                  (~;_
(   |                  |   )
 ~', ',    ,''~'',   ,' ,'~
     ', ','       ',' ,'
       ',: {'} {'} :,'
         ;   /^\   ;
          ~\  ~  /~
        ,' ,~~~~~, ',
      ,' ,' ;~~~; ', ',
    ,' ,'    '''    ', ',
  (~  ;               ;  ~)
   -;_)               (_;-

There are two doors in front of you. 🚪 a red door, and 🚪 a blue door.
""")
door = input("Which door do you want to open? \n").lower()
if door == "red":
    print("Great! now you entered a room.")
    gift = input("You found three boxes: 🎁 white, 🎁 black, 🎁 green. \n").lower()
    if gift == "white":
        print("Oops! you opened a box filled with snakes 🐍🐍🐍")
    elif gift == "black":
        print("Oops! you opened a door filled with spiders 🕷️🕸️🕷️🕸️🕷️🕸️")
    elif gift == "green":
        print("Congratulations! You found the treasure! 💰💰💰")
    else: 
        print("invalid choice 🤷‍♂️🤷‍♂️🤷‍♂️")
elif door == "blue":
    print("""
    Oops! You chose the crocodile door.
    Game over! 🐊🐊🐊
    """)
else:
    print("invalid choice 🤷‍♂️🤷‍♂️🤷‍♂️")