# ProSetSolver

(https://www.ocf.berkeley.edu/~dadams/proset/)
Projective Set solver designed for EXPERT mode



## Usage

The console will prompt the user to input the color data of the seven cards.

For each of the seven cards, input the active colors by listing the first letters of each active color.

##For example...

<img width="118" alt="Screen Shot 2022-10-09 at 10 20 44 AM" src="https://user-images.githubusercontent.com/57467707/194764985-fbbee4e8-f94b-4b42-8411-1c0f68269115.png">

For this image, the user will enter in "ryp" for the active red, yellow, and purple spots.


**Note that the order in which the user enters the cards does not matter, though it will affect how the program returns the sequence of correct cards.
###For example...
The program may return (1,3,5) as a possible sequence. The "1" represents the first card the user entered, "3" for the third, and "5" for the fifth.

##



#Dependencies
None - only uses the built-in itertools library
