# 2-levelShortestPathTest

## How to run the code
To run the project simply run the main.py, It will ask for inputs step by step.

## About the Algorithm
We used a dynamic programming algorithm similar to djikstra.
we started backward recursion from one side and forward recursion from the other.
First we consider any house and shop as vertexes and created weighed edges 
between them.

For the more crowded side of the river we just created edges between buildings (Houses or Shops) and nearest connectors 
(Bridges and Boat-ports) but for the other side we had to create edges between any port/bridge to any of destinations.
so we have (Count of Ports and Bridges) x (Count of Shops) edges on the right side.

| ![dividing graph levels](https://github.com/Shaghafr/2-levelShortestPath/blob/master/images/Image3.png) |
|:--:| 
| *Classic Shortest-path search space* |


<br>
<br>


| ![dividing graph levels](https://github.com/Shaghafr/2-levelShortestPath/blob/master/images/Image2.png) |
|:--:| 
| *Omitting Edges from the **Wrong** side (with less nodes)*| 

<br>
<br>

| ![dividing graph levels](https://github.com/Shaghafr/2-levelShortestPath/blob/master/images/Image1.png) |
|:--:| 
| *Omitting Edges from the **Correct** side (with more nodes)* |

<br>
<br>

On the other side we have (Count of Houses) x (1 to 6) edges.
We used the more crowded side of river in the narrower matrix.
In the next step we store all the path length information to use them in next steps.

Therefore by calculating minimum of sum of two path lengths, we can have already calculated and stored
left and right side edges we achieve the minimum path.



### Complexity
The solution is based on 2 sub graphs and their corresponding
adjancy matrixes, and considering that in the worst case one of matrixes size 
is;
```math
A = (Count of Houses) x 6 
A[i][j] = distance from House[i] to nearest ports or bridges 
```
Calculating each of these distances will take **O(1)**.
<br>
<br>

And the other side's adjancy matrix would be;
```math
B = (Count of Ports) x (Count of Shops)
B[i][j] = distance from Port[i]to Shop[j]
```
similar to the above we have;

```math
C = (Count of Bridges) x (Count of Shops)
C[i[j] = distance from Bridgeᵢ[i] to Shop[j]
```
In order to get the result we should pick a row from **A** and a column 
from **B** after calculating 6 x [Shop Count] sums, we have to find the minimum which will
have a time complexity of **O(log n)**.

Finally we have to create a new matrix to store the results
```math
D[i][j] = shortest distance between Home[i] and Shop[j]
```
We will fill this matrix and each component of the matrix will take 
**O(log(6 x ShopCount))**

<br>
So finnaly for the worst case we can have:

```math
O(n^2.log(n))
```

## About the Implementation
The algorithm is implemented using python 3.8.

Considering DRY principals, some inherited classes are used to avoid unnecessary code duplication and 
also this enabled us to use these two Shop and House classes as alternatives based on the graph structure.
Also a polymorphic method is used to calculate different values of 
path length according to port(boat + walking) or bridge(bicycle) usage in order to consider different
speeds of these two travel method.

## Next Steps:
1. I will create a random input generator, which will help to test the algorithm better.
2. I will create a unit test for testing results and comparing them with a classic djikstra algorithm to ensure the 
correctness of the results.
3. I will try to use better data structures which may help to achieve to a better performance.
4. I will try to create a simple visualization to illustrate the problem and the solution results.

## References:
* Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). Introduction to algorithms. Single-Source Shortest Paths. (pp. 643-683). MIT press.(pp)
* Rachmawati, D., & Gustin, L. (2020, June). Analysis of Dijkstra’s Algorithm and A* Algorithm in Shortest Path Problem. In Journal of Physics: Conference Series (Vol. 1566, No. 1, p. 012061). IOP Publishing.
* Zwick, U. (2002). All pairs shortest paths using bridging sets and rectangular matrix multiplication. Journal of the ACM (JACM), 49(3), 289-317.
* MIT 6.006 Introduction to Algorithms, Fall 2011: [Single-Source Shortest Paths Problem](https://www.youtube.com/watch?v=Aa2sqUhIn-E)  
* MIT 6.006 Introduction to Algorithms, Fall 2011: [Dynamic Programming I: Fibonacci, Shortest Paths](https://www.youtube.com/watch?v=OQ5jsbhAv_M)

