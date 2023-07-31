Added project https://github.com/users/maniaclogic/projects/1/views/1

# Tasks

1) Setup Kivy ✔
2) Setup DB and tables ✔
   - Levels table with attributes: [level, max, counter] ✔
3) Write add value option to app and insert to vocab table ✔
   - Values table with attributes: [value, answer, written, level=0] ✔
- Clear form after save
4) Create value class from DB
5) Display card on screen with value
6) On click display answer (flip animation would be cool)
7) Display success (✓ and 𐄂) buttons with answer
8) Update value based on success
   1) add to next level or first level
   2) increment counter for level in level table
9) Check level counter >= max 
   1) Read all from level (new variable: current_level)
   2) when level is empty set current_level to 1st level again
   3) Randomly select 10 new values from DB
   4) Throw error when not enough values to continue game
10) Add achievements (for fun!)
   1) Add daily mission of 30 new vocab
   2) Add counter == how many vocab practiced today
   3) How many vocabulary overall
   4) How many vocabulary in level 5

Will never happen: 11) Implement token to support several users

## Questions

- How to implement grammar structure?
     - Add sentence per vocab?
- How to add listening comprehension?
