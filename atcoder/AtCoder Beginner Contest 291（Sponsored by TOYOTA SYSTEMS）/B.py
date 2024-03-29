'''
Problem Statement
Takahashi is participating in a gymnastic competition.
In the competition, each of
5N judges grades Takahashi's performance, and his score is determined as follows:

Invalidate the grades given by the
N judges who gave the highest grades.
Invalidate the grades given by the
N judges who gave the lowest grades.
Takahashi's score is defined as the average of the remaining
3N judges' grades.
More formally, Takahashi's score is obtained by performing the following procedure on the multiset of the judges' grades
S (
∣S∣=5N):

Repeat the following operation
N times: choose the maximum element (if there are multiple such elements, choose one of them) and remove it from
S.
Repeat the following operation
N times: choose the minimum element (if there are multiple such elements, choose one of them) and remove it from
S.
Takahashi's score is defined as the average of the
3N elements remaining in
S.
The
i-th
(1≤i≤5N) judge's grade for Takahashi's performance was
X
i
​
  points. Find Takahashi's score.

Constraints
1≤N≤100
0≤X
i
​
 ≤100
All values in the input are integers.
Input
The input is given from Standard Input in the following format:

N
X
1
​

X
2
​

…
X
5N
​

Output
Print Takahashi's score.
Your answer will be considered correct if the absolute or relative error from the true value is at most
10
−5
 .

Sample Input 1
Copy
1
10 100 20 50 30
Sample Output 1
Copy
33.333333333333336
Since
N=1, the grade given by one judge who gave the highest grade, and one with the lowest, are invalidated.
The
2-nd judge gave the highest grade (
100 points), which is invalidated.
Additionally, the
1-st judge gave the lowest grade (
10 points), which is also invalidated.
Thus, the average is
3
20+50+30
​
 =33.333⋯.

Note that the output will be considered correct if the absolute or relative error from the true value is at most
10
−5
 .

Sample Input 2
Copy
2
3 3 3 4 5 6 7 8 99 100
Sample Output 2
Copy
5.500000000000000
Since
N=2, the grades given by the two judges who gave the highest grades, and two with the lowest, are invalidated.
The
10-th and
9-th judges gave the highest grades (
100 and
99 points, respectively), which are invalidated.
Three judges, the
1-st,
2-nd, and
3-rd, gave the lowest grade (
3 points), so two of them are invalidated.
Thus, the average is
6
3+4+5+6+7+8
​
 =5.5.

Note that the choice of the two invalidated judges from the three with the lowest grades does not affect the answer.
'''