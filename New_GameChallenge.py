#!/bin/python

"""
Ram and Hari fed up with FIFA so they invented a new game. The rules of the game are as follows.

At first they have a set of N distinct integers. The players make moves in turns. Each turn, the player whose turn it is chooses two distinct integers x and y from the set, such that the set does not contain their absolute difference |x - y|. The integer |x - y| is added to the set, increasing its size by one.

If the current player has no valid move, he loses the game. Your task is to find the player who wins the game, knowing that both the players play optimally and Ram always makes the first move.

Example

For N = 2 and A = [2, 3], the output should be
New_Game(N, A) = "RAM".

Since there're just two numbers in the initial set, Ram has to take them. The set changes to [1, 2, 3], and Hari ends up with no valid move to make, so Ram is the winner.

Input/Output

[time limit] 4000ms (py)
[input] integer N

Set size.

Constraints:
2 ≤ N ≤ 100.

[input] array.integer A

Array of N distinct integers.

Constraints:
A.length = N,
1 ≤ A[i] ≤ 109.

[output] string

The winner name, either "RAM" or "HARI".

"""

def New_Game(N, A):
    if N in range(2,101):
        counter = 0
        while True:
            numbers = random.sample(A, 2)
            if abs(numbers[0] - numbers[1]) in A:
                break
            else:
                A.add(abs(numbers[0] - numbers[1]))
                counter += 1
    return counter

if __name__ == "__main__":
    
    N = int(raw_input())
    A = raw_input().split()
    A = [int(a) for a in A]
    A = set(A)
    counter = New_Game(N, A)
    print counter
    if counter % 2 == 0:
        print "HARI"
    else:
        print "RAM"
