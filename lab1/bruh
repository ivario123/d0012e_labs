
## These calculations assume that the time complexity of merge is linear and that the constanst are negligible.


$
  T(n) =   O(k^2)\text{~if~}n <= k\\
           c1+2\cdot T(⌊(n/2)⌋) + O(n)\text{~if~} n > k
$

$
  T(n) = c1 + 2\cdot T(⌊(n/2)⌋) + O(n)
$
since $T(⌊(n/2)⌋)$ is unknow, we pass n/2 as n to $T(n)$

$
  T(n/2) = c1 + 2\cdot T(⌊(n/4)⌋) + n/2
$
Passing it back into $T(n)$
$
  T(n) = c1 + 2\cdot\{ c1 + 2\cdot T(⌊\frac{n}{2^2}⌋) + n/2\}  + n =  \\
  =\{c = \text{all constants} \} =\\
  = c + 2^2\cdot T(⌊\frac{n}{2^2}⌋) + 2 \cdot n
$
Since $T(n/4)$ is unknow, we pass n/4 as n to $T(n)$
$
  T(n/2^2) = c1 + 2\cdot T(⌊\frac{n}{2^3}⌋) + n/2^2 = \\ 
$
passing it back into $T(n)$
$
  T(n) = c + 2^2\cdot \{c1 + 2\cdot T(⌊\frac{n}{2^3}⌋) + n/2^2\} + 2 \cdot n = \\
  = c + 2^3\cdot T(⌊\frac{n}{2^3}⌋) + 3 \cdot n
$
We can see a repeating pattern in the above equations.
$
  T(n)_i = c + 2^i\cdot T(⌊\frac{n}{2^i}⌋) + i \cdot n
$
Where $_i$ represents the number of times we have to pass the input to $T(n)$


To find out how many times we need to pass the input to $T(n)$ we can use the end condition
$
  T(k) = O(k^2)
$
so when $n=k$ we return a constant time

To find out when n is equal to k we can use the following equation:
$
  \frac{n}{2^i} = k → n = 2^i\cdot k→ log_2(n) = log_2(2^i\cdot k)→ log_2(n) = log(2^i) + log(k) →\\→ log(n) = i⋅log(2) + log(k) → i =log(n)-log(k) → i = log(n/k) 
$

So the time complexity of $T(n)$ is :
$
T(n) = c + n/k\cdot T(k) + log(n/k)\cdot n = c + \frac{n\cdot T(k)}{k} + (log(n)-log(k))\cdot n
$

Final formula:
$
  T(n) = c + \frac{n\cdot T(k)}{k} + (log(n)-log(k))\cdot n
$

Optimal K value dependent on $T(k)$ since if $T(k)<log(k)\cdot k$ then $k=n$ is optimal but if $T(k)>log(k)\cdot k$ then we need to solve:

$
 \frac{n\cdot T(k)}{k} < (log(n)-log(k))\cdot n\\
 \text{where~} k < n \text{~and~} T(k) > log(k)\cdot k\\
 T(k) < (log(n)-log(k))\cdot k\\
$
For insertion sort the $T(k)$ is $O(k^2)$ so:
$
  O(k^2) < (log(n)-log(k))\cdot k\\
  k < log(n)-log(k)\\
  k + log(k) < log(n)\\
  2^k +k < n\\
$
For bSort the $T(k)$ is $O(n⋅log(n))$ so:
$
  O(k⋅log(k)) < (log(n)-log(k))\cdot k\\
  log(k) < log(n)-log(k)\\
  log(k)+log(k) < log(n)\\
  log(k^2) < log(n)\\
  k <  sqrt(n)\\
$
