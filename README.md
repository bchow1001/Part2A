# Part2A

1. How to use Heap Sort (n \log n)This algorithm is used whenever you have a "messy" list of numbers and you want to put them in order from smallest to largest.The Steps:
- Copy the Code: Paste the heap_sort and heapify functions into your Python file.
-Create a List: Define a variable containing a list of numbers you want to sort.
- Call the Function: Run heap_sort(your_list_name). Note that this algorithm sorts the list "in-place," meaning it changes your original list directly.

Example Implementation:
# 1. Define your messy list
my_numbers = [45, 2, 89, 12, 0, 7]

# 2. Call the algorithm
heap_sort(my_numbers)

# 3. See the result
print("My Sorted Numbers:", my_numbers)
# Output: [0, 2, 7, 12, 45, 89]
What's happening? When you call heap_sort, the code first rearranges your list into a "Heap" (a tree where the biggest number is at the top). It then swaps that biggest number to the end of the list and repeats the process until everything is sorted.


2. How to use Towers of Hanoi (O(2^n))This code doesn't "sort" data; instead, it provides you with a step-by-step instruction manual on how to solve the classic puzzle.
The Steps:
-Copy the Code: Paste the towers_of_hanoi function into your Python file.

-Set the Disks: Decide how many disks you want to move (start with 3).

-Name the Pegs: You need to tell the computer the names of your three pegs (e.g., 'A', 'B', and 'C').

-Call the Function: Use towers_of_hanoi(disks, start, end, helper).
# 1. Choose number of disks
Example Implementation:
disks = 3

# 2. Run the instructions
# We want to move 'disks' from Peg A to Peg C, using Peg B as a helper.
towers_of_hanoi(disks, 'Source Peg', 'Destination Peg', 'Auxiliary Peg')

What's happening? The code will print out a list of moves like this:

Move disk 1 from Source Peg to Destination Peg

Move disk 2 from Source Peg to Auxiliary Peg

...and so on.

A Quick Warning: Because this is an exponential algorithm, be careful with the number of disks!

3 disks = 7 lines of instructions.

10 disks = 1,023 lines of instructions.

30 disks = Over 1 billion lines of instructions! Your computer might freeze if you try a number too high.
