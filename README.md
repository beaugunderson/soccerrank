# soccerrank

This is a command-line application that calculates the ranking table for a soccer league.

## Input/output
The input and output are text. 
The main script (soccer.py) parses the input.txt file passed by name on the command line. 
It outputs the result via stdout to the console.

The input contains results of games, one per line. 
The output orders from most to least points, following the format 'rank. team, 0 pts'.


## The rules
In this league, a tie is worth 1 point and a win is worth 3 points. A loss is worth 0 points. 
If two or more teams have the same number of points, they should have the same rank and be printed in alphabetical order.