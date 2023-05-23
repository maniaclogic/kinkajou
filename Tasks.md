# Tasks

1) Setup Kivy ✔
2) Setup DB from file
   1) Values table with attributes: [value, answer, written, level=0]
   2) Levels table with attributes: [level, max, counter]
3) Create value class from DB
4) Display card on screen with value
5) On click display answer (flip animation would be cool)
6) Display success (✓ and 𐄂) buttons with answer
7) Update value based on success
   1) add to next level or first level
   2) increment counter for level in level table
8) Check level counter >= max 
   1) Read all from level (new variable: current_level)
   2) when level is empty set current_level to 1st level again
   3) Randomly select 10 new values from DB
   4) Throw error when not enough values to continue game
9) Implement token to support several users
10) 