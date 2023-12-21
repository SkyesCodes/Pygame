# Fruit Slicer!
### It is your final phase of chef training, you must make a fruit salad as your estranged instructor sends the fruit flying your way! Careful to avoid the bombs he mixed in! You will have 3 lives to score as many points as you can, good luck!
---
## Initial Wireframe
![Initial Wireframe](https://imgur.com/1SPFvSo.png)

---
## Game Description
- The objective of this game is to click fruits as they fly across the screen and near your character, timing and accuracy are the name of the game here.
- Clicking fruit will score you points
- Clicking bombs will lose a life 
- You have 3 lives to score as many points as possible
- You will have 5 minutes to score as many points as possible
- there is no win condition, only loss and time out conditions, the objective is to score as high as possible and try to beat it on later attempts.
---
## User Stories
- AAU I want to click start and have the game begin
- AAU I want to be able to play the game have it tracking my points and lives correctly
- AAU I want to play the game to beat my own highscore
---
## MVP
- A working pygame, including a start screen
- render a character on the screen 
- render fruits and bombs to move across the screen
- make either the area the fruit is in, or the fruit themselves clickable, as well as bombs. 
- Game will track score
- Will track lives, ending the game when you run out of them.



## Stretch goals
- Include normal and hard difficulties, which will make the game both more accesible and have a higher ceiling 
- Focus on visual styling hopefully including animations and sounds
- attach to a database to have scores globally tracked on deployment
- Create a highscore display on start screen
- alter the loss condition to make accuracy more important, missing fruit will also lose a life.
- create combo tracking to further reward accuracy and highscore opportunities. (alternative to the altered loss condition)

## Sprint Plan:
- Wednesday
    - Continue learning to use pygame through reading, videos, and hands on testing
- Thursday
    - Begin initial barebones of the game visuals so I can add logic to them and see it work
- Friday
    - Work on the game logic (this is expected to take the longest)
- Weekend
    - Finish game logic
- Monday
    - If game logic is not complete, complete it. If it is, move on to stretch goals
- Tuesday
    -hopefully stretch goals
- Wednesday
    -hopefully stretch goals
- Thursday
    -Present!
---
## Technologies used
- Virtual Studio Code
- python
- pygame

## GAME UPDATE
- I decided to take a slightly different direction with the game. Instead of 3 seperate lanes I randomly spawn fruit all over the window, starting slow and picking up over time. I kept the concpet of bombs but made the same change to them. Instead of clicking on fruit the objective of the game is now to collect fruit with your character and avoid bombs the best you can. Fruits are worth varrying amounts of points, and bombs will take away 1 of your 3 lives. When 3 lives are lost the game is over and the window will close. Score as many points as you can before you run out of lives!

## Screenshots
![Start Screen](https://imgur.com/t9CpBhW.png)
![Gameplay](https://imgur.com/0vGLzSe.png)
![Game Over](https://imgur.com/Elvohrr.png)


