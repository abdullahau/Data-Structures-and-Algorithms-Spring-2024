# Description

Here you can find all my practice notes from University of Helsinki's [Data Structures and Algorithms](https://studies.helsinki.fi/courses/course-implementation/otm-f36af785-3311-4b6f-bfd3-2aa6add9d2f9), spring 2024 open online course.

The exercises and examples are entirely implemented in Python 3.

Currently, this repo is a work-in-progress and shall be updated regularly.

So far, there are no requirements for external packages and/or libraries except Python's standard library. You can run the notebooks and Python scripts on VSCode or any other editor/IDE you feel comfortable with.

Please feel free to message me for any questions or suggestions.

## References

- Course Website: [Data Structures and Algorithms, spring 2024](https://tira.mooc.fi/spring-2024/)
- Exercise Website: [Exercises on Code Submission Evaluation System](https://cses.fi/dsa24k/list/)

## Repo Structure

```bash
|-- 0. General Algorithms.py
|-- 1. Introduction.ipynb
|-- 2. List.ipynb
|-- 2a. Adding elements to list.ipynb
|-- 3. Efficient algorithms.ipynb    
|-- 4. Hashing.ipynb
|-- 4a. Hash table.ipynb  
|-- 4b. Slow hashing.ipynb
|-- 5. Sorting.ipynb      
|-- 5a. Insertion sort.ipynb
|-- 5b. Merge sort.ipynb    
|-- 5c. Sorting lower bound.ipynb
|-- 6. Own data structures.ipynb
|-- 7. Trees and recursion.ipynb
|-- CSES Problem Set
|   |-- 0 - Introductory Problems
|   |   |-- 0 - Weird Algorithm.ipynb
|   |   |-- 1 - Missing Number.ipynb
|   |   |-- 10 - Coin Piles.ipynb
|   |   |-- 11 - Palindrome Reorder.ipynb
|   |   |-- 12 - Gray Code.ipynb
|   |   |-- 13 - Tower of Hanoi.ipynb
|   |   |-- 2 - Repetitions.ipynb
|   |   |-- 3 - Increasing Array.ipynb
|   |   |-- 4 - Permutations.ipynb
|   |   |-- 5 - Number Spiral.ipynb
|   |   |-- 6 - Two Knights.ipynb
|   |   |-- 7 - Two Sets.ipynb
|   |   |-- 8 - Bit Strings.ipynb
|   |   |-- 9 - Trailing Zeros.ipynb
|   |   |-- bitstrings.py
|   |   |-- graycode.py
|   |   |-- hanoi.py
|   |   |-- increasingarray.py
|   |   |-- knights.py
|   |   |-- missing.py
|   |   |-- palindrome.py
|   |   |-- permutations.py
|   |   |-- repetitions.py
|   |   |-- spiral.py
|   |   |-- trailingzeros.py
|   |   |-- twosets.py
|   |   `-- weird.py
|   |-- Antti Laaksonen - Guide to Competitive Programming - Learning and Improving Algorithms Through Contests.pdf
|   |-- Competitive Programmer's Handbook.pdf
|   `-- Introduction.md
|-- Exercises
|   |-- Week 1
|   |   |-- 1 - Candies.ipynb
|   |   |-- 2 - Inversions.ipynb
|   |   |-- 3 - Same bits.ipynb
|   |   |-- 4 - Repeat.ipynb
|   |   |-- 5 - Efficiency test.ipynb
|   |   |-- 6 - Sequence of numbers.ipynb
|   |   |-- 7 - Time complexities.ipynb
|   |   |-- 8 - Rectangles.ipynb
|   |   |-- candies.py
|   |   |-- inversions.py
|   |   |-- rectangles.py
|   |   |-- repeat.py
|   |   |-- samebits.py
|   |   `-- sequence.py
|   |-- Week 2
|   |   |-- 10 - List efficiency II.ipynb
|   |   |-- 11 - List incrementing.ipynb
|   |   |-- 12 - Different sums.ipynb
|   |   |-- 13 - Circle game.ipynb
|   |   |-- 14 - Two lists.ipynb
|   |   |-- 15 - Nested list.ipynb
|   |   |-- 16 - Inversions again.ipynb
|   |   |-- 9 - List efficiency I.ipynb
|   |   |-- againinv.py
|   |   |-- circlegame.py
|   |   |-- listadd.py
|   |   |-- nestedlist.py
|   |   |-- sumdiff.py
|   |   `-- twolists.py
|   |-- Week 3
|   |   |-- 17 - Same bit.ipynb
|   |   |-- 18 - Same character.ipynb
|   |   |-- 19 - Forbidden character.ipynb
|   |   |-- 20 - Lone number.ipynb
|   |   |-- 21 - List split.ipynb
|   |   |-- 22 - Tira sequences.ipynb
|   |   |-- 23 - Last number.ipynb
|   |   |-- 24 - Stock trading.ipynb
|   |   |-- forbidden.py
|   |   |-- lastnumber.py
|   |   |-- listsplit.py
|   |   |-- onlyone.py
|   |   |-- samebit.py
|   |   |-- samechar.py
|   |   |-- sequences.py
|   |   `-- trading.py
|   |-- Week 4
|   |   |-- 25 - Robot route.ipynb
|   |   |-- 26 - No pair.ipynb
|   |   |-- 27 - Same distance.ipynb
|   |   |-- 28 - Play lists.ipynb
|   |   |-- 29 - Big win.ipynb
|   |   |-- 30 - Same hash.ipynb
|   |   |-- 31 - Sublists.ipynb
|   |   |-- 32 - Long route.ipynb
|   |   |-- bigwin.py
|   |   |-- longroute.py
|   |   |-- nopair.py
|   |   |-- playlists.py
|   |   |-- robot.py
|   |   |-- samedist.py
|   |   |-- samehash.py
|   |   |-- sublists.py
|   |   `-- words.txt
|   |-- Week 5
|   |   |-- 33 - Packing.ipynb
|   |   |-- 34 - Contiguous numbers.ipynb
|   |   |-- 35 - Sorting algorithms.ipynb
|   |   |-- 36 - Binary search.ipynb
|   |   |-- 37 - Largest distance.ipynb
|   |   |-- 38 - Restaurant.ipynb
|   |   |-- 39 - Semisorting.ipynb
|   |   |-- 40 - Swap and move.ipynb
|   |   |-- distance.py
|   |   |-- interval.py
|   |   |-- packbox.py
|   |   |-- restaurant.py
|   |   |-- semisort.py
|   |   `-- swapmove.py
|   |-- Week 6
|   |   |-- 41 - Max list.ipynb
|   |   |-- 42 - Repeat list.ipynb
|   |   |-- 43 - Fast mode.ipynb
|   |   |-- 44 - Mex numbers.ipynb
|   |   |-- 45 - Quick list.ipynb
|   |   |-- 46 - Different repeats.ipynb
|   |   |-- 47 - Sum of squares.ipynb
|   |   |-- 48 - Near list.ipynb
|   |   |-- fastmode.py
|   |   |-- maxlist.py
|   |   |-- mex.py
|   |   |-- nearlist.py
|   |   |-- quicklist.py
|   |   |-- repeatlist.py
|   |   |-- squaresum.py
|   |   `-- trackrepeat.py
|   `-- Week 7
|       |-- 49 - Leaves.ipynb
|       |-- 50 - No branch.ipynb
|       |-- 51 - Children.ipynb
|       |-- 52 - Depths.ipynb
|       |-- 53 - Same depth.ipynb
|       |-- 54 - Subtrees.ipynb
|       |-- 55 - Queens.ipynb
|       |-- 56 - All Trees.ipynb
|       |-- alltree.py
|       |-- depths.py
|       |-- leaves.py
|       |-- maxchild.py
|       |-- nobranch.py
|       |-- queens.py
|       |-- samedepth.py
|       `-- subtrees.py
|-- README.md
`-- Resources
    |-- Backtracking.ipynb
    |-- Binary Tree.ipynb
    |-- Input & Output file txt in Bash.md
    |-- Jupyter-Shortcuts.md
    |-- Recursion for Beginners_ A Beginner's Guide to Recursion.pdf
    |-- Recursion for Beginners_ A Beginner's Guide to Recursion.pptx
    |-- Recursion.ipynb
    |-- TimeComplexity - Python Wiki.md
    |-- memoryallocation.py

12 directories, 165 files
```
