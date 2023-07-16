# Amyzing's Battleships
Amyzing's Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku  
Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each battleship occupies one square on the board. Goodluck!!  

[Here](https://project3-battleships-36d94044604b.herokuapp.com/) is the live version of my project.  
![Capture](https://github.com/Amyz1ng/Project3-battleships/assets/124196828/dbf1cf04-cbf7-49ab-a20f-87f922c150b9)


# How to play  
The player enters their name and two boards are randomly generated.
The player can see where their ships are, indicated by an * sign, but cannot see where the computer's ships are. Guesses are marked on the board with an X. Hits are indicated by @ .
The player and the computer then take it in turns to make guesses and try to sink each other's battleships.
The winner is the player who sinks all of their opponent's battleships first.   

Key notes:  
"*"  - Player Battleships  
"@"  - Destroyed Battleships  
"X"  - Guessed Locations
# Features
## Existing Features
- Random board generation  
- Ships are randomly placed on both the player and computer boards  
- The player cannot see where the computer's ships are   
## Future Features
- Give user ability to set amount of turns allowed
- Allow own placement of battleships
- Allow one battleship to take over multiple blocks
# Testing  
I have manually tested this project by doing the following:  
- Passed the code through a PEP8 linter and confirmed there are no problems  
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, dupliace inputs 
- Tested in my local terminal and the Code Institute Heroku terminal  
# Bugs
## Solved Bugs  
- Game would pop up error messages if incorrect input was entered, but would still count the turn and move on. I've fixed this to not continue until a valid value is given.
## Remaining Bugs  
No bugs remaining  
## Validator Testing  
- PEP8  
- No errors were returned from https://pep8ci.herokuapp.com/
![PEP](https://github.com/Amyz1ng/Project3-battleships/assets/124196828/8b1c8881-3dc6-47dc-84a9-207990dce92f)

# Deployment  
This project was deployed using Code Institute's mock terminal for Heroku.  
# Steps for deployment:  
- Fork or clone this repository  
- Create a new Heroku app  
- Set the build backs to Python and NodeJS in that order
- Add config var to include Key: Port Value: 8000
- Link the Heroku app to the repository  
- Click on Deploy  
# Credits  
- Code Institute for the deployment terminal  
- Code Institute's Project Scope video
