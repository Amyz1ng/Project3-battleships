# Amyzing's Battleships
Amyzing's Battleships is a Python terminal game, which runs in the Code Institute mock terminal on Heroku
Users can try to beat the computer by finding all of the computer's battleships before the computer finds theirs. Each battleship occupies one square on the board.  

[Here](https://project3-battleships-36d94044604b.herokuapp.com/) is the live version of my project.

# How to play  
The player enters their name and two boards are randomly generated.
The player can see where their ships are, indicated by an * sign, but cannot see where the computer's ships are. Guesses are marked on the board with an X. Hits are indicated by @ .
The player and the computer then take it in turns to make guesses and try to sink each other's battleships.
The winner is the player who sinks all of their opponent's battleships first.
# Features
## Existing Features
- Random board generation  
- Ships are randomly placed on both the player and computer boards  
- The player cannot see where the computer's ships are   
## Future Features
- Allow player to select the board size and number of ships  
- Allow player to position ships themselves  
- Have ships larger than 1x1  

# Testing  
I have manually tested this project by doing the following:  
- Passed the code through a PEP8 linter and confirmed there are no problems  
- Given invalid inputs: strings when numbers are expected, out of bounds inputs, same input twice  
- Tested in my local terminal and the Code Institute Heroku terminal  
# Bugs
## Solved Bugs  
- When I wrote the project, I was getting index errors because I had forgotten that the lists are zero indexed. I fixed this by adding size - 1 where necessary  
- My validate_coordinates function was returning false positives because I hadn't structured the if statement properly  
## Remaining Bugs  
No bugs remaining  
## Validator Testing  
- PEP8  
- No errors were returned from [PEP8online.com](https://pep8ci.herokuapp.com/)
![PEP](https://github.com/Amyz1ng/Project3-battleships/assets/124196828/8b1c8881-3dc6-47dc-84a9-207990dce92f)

# Deployment  
This project was deployed using Code Institute's mock terminal for Heroku.  
# Steps for deployment:  
- Fork or clone this repository  
- Create a new Heroku app  
- Set the build backs to Python and NodeJS in that order  
- Link the Heroku app to the repository  
- Click on Deploy  
# Credits  
- Code Institute for the deployment terminal  
- Wikipedia for the details of the Battleships game  
