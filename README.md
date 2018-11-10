# Tic-Tac-Toe
### A Guide to Collaboration
When working on any sort of project, it is almost always easier to have a helping hand. Coding is only a small part of *the development process*; collaborating with other programmers is a skill that is often overlooked, but equally as valuable. How good is a teammate in a group project if they can't work with anyone else? Hint: not very good. This project will teach you the basics of *version control* and how to work with multiple people on the same project.

### The Game
We all know how Tic Tac Toe works, but here are the rules anyway:
1. A **3 x 3 game board** is set up with every space empty.
1. Two players alternate turns; each player has a marker (X and O).
1. On their turn, the player may choose an **empty space** to place their marker.
1. If any player completes a sequence of 3 markers in the game board, they win! Players can complete a sequence in these 3 ways:
	1. **Horizontally**
	1. **Vertically**
	2. **Diagonally**
1. Continue playing until a player wins, or there are no more empty spaces left on the game board.

### Tasks
Just like any other problem that needs solving, the game of Tic Tac Toe can be broken down into several smaller problems, typically refered to as **subtasks**.
Solving many subtasks is often much easier to do than solving one large task. For example: your task is to `solve 14 * 4`. This looks pretty difficult, so let's break it up into subtasks. We know that `4 + 10 = 14`, so we can break up the large task into the combination of two subtasks: `4 * 4 = 24`, and `10 * 4 = 40`. Now, our large task (`14 * 4`) can be rewritten into `(4 * 4) + (10 * 4)`. We already know how to solve the subtasks: `4 * 4 = 16` and `10 * 4 = 40`. Great! We have all the pieces we need to solve our initial task! `14 * 4 = (4 * 4) + (10 * 4) = 16 + 40 = 56` And just like that, we have our answer: **56**.

## Our Tasks
No, Tic Tac Toe is not an extremely advanced game. But just like any other problem that needs solving, it is easier to solve subtasks, and two (or more) heads are better than one. Each table group will be working together on a task of their choice. To avoid any confusion between groups, each task has a set of rules / codes / **style guides** that must be followed. The list of tasks is as follows:
* **Create Game Board**: Initialize a 3 x 3 game board in the form of a 2 dimensional list.
	* *Rule*: Store game board in variable called `game_board`.
* **User Input**: Get input from player X and player O: store player marker (X or O) and where they are playing on the board in variables, then place marker in game board.
	* *Rule*: Placed move variable will be called `move_index` and current player will be called `current_player`.
* **Win Cases (3)**: If `current_player` has won the game,end program.
	* **Horizontal**: Check if `current_player` has occupied an entire row.
	* **Vertical**: Check if `current_player` has occupied an entire column.
	* **Diagonal**: Check if `current_player` has made a diagonal sequence from corner to opposite corner.
* **Display Current Game Board**: Print out `game_board` to user(s), and make it look pretty!
* **Keep the Game Going**: Loop until either a player has won the game or the game ends in a tie.

# Workflow
Each table will pick one person to **fork** this repository (`bm20894/Tic-Tac-Toe`). Their tablemates will work on *that forked repository* together. Because we won't be writing a boatload of code, you really only need one person in your table typing. Each table should follow this process for working:
1. Fork **this repository**. This will create a "copy" of the current repository in your GitHub account. It will look something like this: `mshunt/Tic-Tac-Toe`
1. Work together in your teams to write some code that solves your subtask. Each team has a section outlined in the main file, `tictactoe.py`. Add your code in your section. When you think it looks good, brace yourselves; a storm's a comin'.
1. Click on the `Upload Files` button. **Drag and Drop** your file into the box to add it to your commit.
1. Commit your changes to the `master` branch in your forked repository. This updates the code you just wrote from your computer to your team's repository on GitHub.
1. If everything looks good and fits the styleguide, submit a **Pull Request** to to the *real* repository: `bm20894/Tic-Tac-Toe`. Add a brief description of what your team did to solve your subtask, and contribute to the larger project.
1. If you got to this point, congrats! You can sit back and relax until the host of the repository (Miles) accepts your **Pull Request**, adding your code to the larger project.

## Questions
If you have any questions, don't be afraid to ask! As the saying goes, Rome wasn't built in a day, and it sure wasn't founded by just one person (it was founded by two). If your tablemates don't know the answer right now, they will in a minute if you ask someone who does! 