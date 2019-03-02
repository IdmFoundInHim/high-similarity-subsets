# High-Similarity-Subsets

_Note: A "Subset(s)" of a multiset is assumed to be a_
_[submultiset](https://en.wiktionary.org/wiki/submultiset#English)._

## Summary
Sorts a [multiset](https://en.wikipedia.org/wiki/Multiset) _K_ into
subsets with each subset having equal (or nearly equal) sum and equal
cardinality (number of elements).




## The Official Problem

For a given multiset _K_ and positive integer (not 0) _r_,
where \#_K_ % _r_ = 0, produce set _R_ containing only subsets of _K_
that are equal in cardinality and equal, or as close to equal as
possible, in sum. Every element in _K_ must be placed into a
sub-multiset in _R_ once and only once. 

Constraints:
* _r_ ≠ 0, _r_ ∈ **N**
* \#_K_ [%](https://en.wikipedia.org/wiki/Modulo_operation) _r_ = 0
* 

Mathmatically,

(See the list at the bottom if your viewer supports LaTeX in Markdown)

* (#_K_) / _n_ = (#_K<sub>x</sub>_) where 0 ≤ _x_ ≤ _n_
* ∑ _K<sub>0</sub>_ ≊ ∑ _K<sub>1</sub>_ ≊ ∑ _K<sub>2</sub>_ ≊...
  * Preferably = rather than ≈

If you have LaTeX support, 
* $$\frac{\#K}{n} = \#K_x, 0 \le x \le n$$
* $$\sum{K_0} \approxeq \sum{K_1} \approxeq \sum{K_2} \approxeq ...$$
    * Preferably $=$ rather than $\approx$


