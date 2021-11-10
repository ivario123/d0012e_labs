$
T(n) =   O(k^2)\text{~if~}n <= k\\
           c1+2\cdot T(⌊(n/2)⌋) + O(n)\text{~if~} n > k
$

number of times the recursion happens if the loop ends at $k = 1$ is
$
\lim_{n\rightarrow \infty} \frac{n}{2^n} \rightarrow log(n)
$
since it ends at k the actual number of function calls will be
$
log(n)- \lim_{k→∞} \frac{k}{2^k} = log(n)-log(k) = log\left(\frac{n}{k}\right)
$
