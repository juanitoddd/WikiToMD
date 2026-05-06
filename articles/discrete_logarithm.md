[![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Discrete_logarithm_mod_5.svg/250px-Discrete_logarithm_mod_5.svg.png)](/wiki/File:Discrete_logarithm_mod_5.svg)Discrete logarithm modulo 5, with base 2.

---


In [mathematics](/wiki/Mathematics), for given [real numbers](/wiki/Real_number) ${\displaystyle a}$ and ${\displaystyle b}$, the [logarithm](/wiki/Logarithm) ${\displaystyle \log _{b}(a)}$ is a number ${\displaystyle x}$ such that ${\displaystyle b^{x}=a}$. The **discrete logarithm** generalizes this concept to a [cyclic group](/wiki/Cyclic_group). A simple example is the group of [integers](/wiki/Integer) [modulo a prime number](/wiki/Modular_arithmetic) (such as 5) under [modular multiplication](/wiki/Modular_multiplication) of nonzero elements.

For instance, take ${\displaystyle b=2}$ in the multiplicative group modulo 5, whose elements are ${\displaystyle {1,2,3,4}}$. Then:
${\displaystyle 2^{1}=2,\quad 2^{2}=4,\quad 2^{3}=8\equiv 3{\pmod {5}},\quad 2^{4}=16\equiv 1{\pmod {5}}.}$
The powers of 2 modulo 5 cycle through all nonzero elements, so discrete logarithms exist and are given by:
${\displaystyle \log _{2}1=4,\quad \log _{2}2=1,\quad \log _{2}3=3,\quad \log _{2}4=2.}$

More generally, in any [group](/wiki/Group_(mathematics)) ${\displaystyle G}$, powers ${\displaystyle b^{k}}$ can be defined for all [integers](/wiki/Integer) ${\displaystyle k}$, and the **discrete logarithm** ${\displaystyle \log _{b}(a)}$ is an integer ${\displaystyle k}$ such that ${\displaystyle b^{k}=a}$. In [arithmetic modulo](/wiki/Modular_arithmetic) an integer ${\displaystyle m}$, the more commonly used term is **index**: One can write ${\displaystyle k=\mathbb {ind} _{b}a{\pmod {m}}}$ (read "the index of ${\displaystyle a}$ to the base ${\displaystyle b}$ modulo ${\displaystyle m}$") for ${\displaystyle b^{k}\equiv a{\pmod {m}}}$ if ${\displaystyle b}$ is a [primitive root](/wiki/Primitive_root_modulo_n) of ${\displaystyle m}$ and ${\displaystyle \gcd(a,m)=1}$.

Discrete logarithms are quickly computable in a few special cases. However, no efficient method is known for computing them in general. In cryptography, the computational complexity of the discrete logarithm problem, along with its application, was first proposed in the [Diffie–Hellman problem](/wiki/Diffie%E2%80%93Hellman_problem). Several important [algorithms](/wiki/Algorithm) in [public-key cryptography](/wiki/Public-key_cryptography), such as [ElGamal](/wiki/ElGamal_cryptosystem), base their security on the [hardness assumption](/wiki/Computational_hardness_assumption) that the discrete logarithm problem (DLP) over carefully chosen groups has no efficient solution,[[1]](#cite_note-1) and in a general [black box](/wiki/Black_box) group lacks a [subexponential solution](/wiki/Subexponential_time) at all.[[2]](#cite_note-2)




## Definition


Let ${\displaystyle G}$ be any group. Denote its [group operation](/wiki/Group_operation) by multiplication and its [identity element](/wiki/Identity_element) by ${\displaystyle 1}$. Let ${\displaystyle b}$ be any element of ${\displaystyle G}$. For any positive integer ${\displaystyle k}$, the expression ${\displaystyle b^{k}}$ denotes the product of ${\displaystyle b}$ with itself ${\displaystyle k}$ times:[[3]](#cite_note-:0-3)


${\displaystyle b^{k}=\underbrace {b\cdot b\cdot \ldots \cdot b} _{k\;{\text{factors}}}.}$
Similarly, let ${\displaystyle b^{-k}}$ denote the product of ${\displaystyle b^{-1}}$ with itself ${\displaystyle k}$ times. For ${\displaystyle k=0}$, the ${\displaystyle k}$th power is the identity: ${\displaystyle b^{0}=1}$.

Let ${\displaystyle a}$ also be an element of ${\displaystyle G}$. An integer ${\displaystyle k}$ that solves the equation ${\displaystyle b^{k}=a}$ is termed a **discrete logarithm** (or simply **logarithm**, in this context) of ${\displaystyle a}$ to the base ${\displaystyle b}$. One writes ${\displaystyle k=\log _{b}a}$.



## Examples



### Powers of 10


The [powers of 10](/wiki/Power_of_10) are


${\displaystyle \ldots ,0.001,0.01,0.1,1,10,100,1000,\ldots .}$
For any number ${\displaystyle a}$ in this list, one can compute ${\displaystyle \log _{10}a}$. For example, ${\displaystyle \log _{10}{10000}=4}$, and ${\displaystyle \log _{10}{0.001}=-3}$. These are instances of the discrete logarithm problem.

Other base-10 logarithms in the real numbers are not instances of the discrete logarithm problem, because they involve non-integer exponents. For example, the equation ${\displaystyle \log _{10}{53}=1.724276\ldots }$ means that ${\displaystyle 10^{1.724276\ldots }}$. While integer exponents can be defined in any group using products and inverses, arbitrary real exponents, such as this 1.724276…, require other concepts such as the [exponential function](/wiki/Exponential_function).

In [group-theoretic](/wiki/Group-theoretic) terms, the powers of 10 form a [cyclic group](/wiki/Cyclic_group) ${\displaystyle G}$ under multiplication, and 10 is a [generator](/wiki/Cyclic_group) for this group. The discrete logarithm ${\displaystyle \log _{10}a}$ is defined for any ${\displaystyle a}$ in ${\displaystyle G}$.



### Powers of a fixed real number


A similar example holds for any non-zero real number ${\displaystyle b}$. The powers form a multiplicative [subgroup](/wiki/Subgroup) ${\displaystyle G=\{\ldots ,b^{-2},b^{-1},1,b^{1},b^{2},\ldots \}}$ of the non-zero real numbers. For any element ${\displaystyle a}$ of ${\displaystyle G}$, one can compute ${\displaystyle \log _{b}a}$.



### Modular arithmetic


One of the simplest settings for discrete logarithms is the group [**Z***p*×](/wiki/Multiplicative_group_of_integers_modulo_n). This is the group of multiplication [modulo](/wiki/Modular_arithmetic) the [prime](/wiki/Prime_number) ${\displaystyle p}$. Its elements are non-zero [congruence classes](/wiki/Modular_arithmetic#Congruence_class) modulo ${\displaystyle p}$, and the group product of two elements may be obtained by ordinary integer multiplication of the elements followed by reduction modulo ${\displaystyle p}$.

The ${\displaystyle k}$th [power](/wiki/Exponentiation) of one of the numbers in this group may be computed by finding its '${\displaystyle k}$th power as an integer and then finding the remainder after division by ${\displaystyle p}$. When the numbers involved are large, it is more efficient to reduce modulo ${\displaystyle p}$ multiple times during the computation. Regardless of the specific algorithm used, this operation is called [modular exponentiation](/wiki/Modular_exponentiation). For example, consider **Z**17×. To compute ${\displaystyle 3^{4}}$ in this group, compute ${\displaystyle 3^{4}=81}$, and then divide ${\displaystyle 81}$ by ${\displaystyle 17}$, obtaining a remainder of ${\displaystyle 13}$. Thus ${\displaystyle 3^{4}=13}$ in the group **Z**17×.

The discrete logarithm is just the inverse operation. For example, consider the equation ${\displaystyle 3^{k}\equiv 13{\pmod {17}}}$. From the example above, one solution is ${\displaystyle k=4}$, but it is not the only solution. Since ${\displaystyle 3^{16}\equiv 1{\pmod {17}}}$ —as follows from [Fermat's little theorem](/wiki/Fermat%27s_little_theorem)— it also follows that if ${\displaystyle n}$ is an integer then ${\displaystyle 3^{4+16n}\equiv 3^{4}\cdot (3^{16})^{n}\equiv 3^{4}\cdot 1^{n}\equiv 3^{4}\equiv 13{\pmod {17}}}$. Hence the equation has infinitely many solutions of the form ${\displaystyle 4+16n}$. Moreover, because ${\displaystyle 16}$ is the smallest positive integer ${\displaystyle m}$ satisfying ${\displaystyle 3^{m}\equiv 1{\pmod {17}}}$, these are the only solutions. Equivalently, the set of all possible solutions can be expressed by the constraint that ${\displaystyle k\equiv 4{\pmod {16}}}$.



### Powers of the identity


In the special case where ${\displaystyle b}$ is the identity element ${\displaystyle 1}$ of the group ${\displaystyle G}$, the discrete logarithm ${\displaystyle \log _{b}a}$ is undefined for ${\displaystyle a}$ other than ${\displaystyle 1}$, and every integer ${\displaystyle k}$ is a discrete logarithm for ${\displaystyle a=1}$.



## Properties


Powers obey the usual algebraic identity ${\displaystyle b^{k+l}=b^{k}\cdot b^{l}}$.[[3]](#cite_note-:0-3) In other words, the [function](/wiki/Function_(mathematics))


${\displaystyle f\colon \mathbf {Z} \to G}$
defined by ${\displaystyle f(k)=b^{k}}$ is a [group homomorphism](/wiki/Group_homomorphism) from the group of integers ${\displaystyle \mathbf {Z} }$ under addition [onto](/wiki/Surjection) the [subgroup](/wiki/Subgroup) ${\displaystyle H}$ of ${\displaystyle G}$ [generated](/wiki/Generating_set_of_a_group) by ${\displaystyle b}$. For all ${\displaystyle a}$ in ${\displaystyle H}$, ${\displaystyle \log _{b}a}$ exists. [Conversely](/wiki/Converse_(logic)), ${\displaystyle \log _{b}a}$ does not exist for ${\displaystyle a}$ that are not in ${\displaystyle H}$.

If ${\displaystyle H}$ is [infinite](/wiki/Infinite_group), then ${\displaystyle \log _{b}a}$ is also unique, and the discrete logarithm amounts to a [group isomorphism](/wiki/Group_isomorphism)


${\displaystyle \log _{b}\colon H\to \mathbf {Z} .}$
On the other hand, if ${\displaystyle H}$ is [finite](/wiki/Finite_group) of [order](/wiki/Order_of_a_group) ${\displaystyle n}$, then ${\displaystyle \log _{b}a}$ is 0 unique only up to [congruence modulo](/wiki/Modular_arithmetic) ${\displaystyle n}$, and the discrete logarithm amounts to a group isomorphism


${\displaystyle \log _{b}\colon H\to \mathbf {Z} _{n},}$
where ${\displaystyle \mathbf {Z} _{n}}$ denotes the additive group of integers modulo ${\displaystyle n}$.

The familiar base change formula for ordinary logarithms remains valid: If ${\displaystyle c}$ is another generator of ${\displaystyle H}$, then


${\displaystyle \log _{c}a=\log _{c}b\cdot \log _{b}a.}$

## Algorithms





The discrete logarithm problem is considered to be computationally intractable. For a classical (e.g., non-[quantum](/wiki/Quantum_computing)) computer, no efficient ([polynomial](/wiki/P_(complexity))-time) algorithm is yet known for computing discrete logarithms in general.

A general algorithm for computing ${\displaystyle \log _{b}a}$ in finite groups ${\displaystyle G}$ is to raise ${\displaystyle b}$ to larger and larger powers ${\displaystyle k}$ until the desired ${\displaystyle a}$ is found. This algorithm is sometimes called *trial multiplication*. It requires [running time](/wiki/Running_time) [linear](/wiki/Linear_time) in the size of the group ${\displaystyle G}$ and thus [exponential](/wiki/Exponential_time) in the number of digits in the size of the group. Therefore, it is an exponential-time algorithm, practical only for small groups ${\displaystyle G}$.

More sophisticated algorithms exist, usually inspired by similar algorithms for [integer factorization](/wiki/Integer_factorization). These algorithms run faster than the naïve algorithm, some of them proportional to the [square root](/wiki/Square_root) of the size of the group, and thus exponential in half the number of digits in the size of the group. However, none of them runs in [polynomial time](/wiki/Polynomial_time) (in the number of digits in the size of the group).


- [Baby-step giant-step](/wiki/Baby-step_giant-step)
- [Function field sieve](/wiki/Function_field_sieve)
- [Index calculus algorithm](/wiki/Index_calculus_algorithm)
- [Number field sieve](/wiki/General_number_field_sieve)
- [Pohlig–Hellman algorithm](/wiki/Pohlig%E2%80%93Hellman_algorithm)
- [Pollard's rho algorithm for logarithms](/wiki/Pollard%27s_rho_algorithm_for_logarithms)
- [Pollard's kangaroo algorithm](/wiki/Pollard%27s_kangaroo_algorithm) (aka Pollard's lambda algorithm)


There is an efficient [quantum algorithm](/wiki/Shor%27s_algorithm) due to [Peter Shor](/wiki/Peter_Shor).[[4]](#cite_note-4)

Efficient classical algorithms also exist in certain special cases. For example, in the group of the integers modulo ${\displaystyle p}$ under addition, the power ${\displaystyle b^{k}}$ becomes a product ${\displaystyle b\cdot k}$, and equality means congruence modulo ${\displaystyle p}$ in the integers. The [extended Euclidean algorithm](/wiki/Extended_Euclidean_algorithm) finds ${\displaystyle k}$ quickly.

With [Diffie–Hellman](/wiki/Diffie%E2%80%93Hellman_key_exchange), a cyclic group modulo a prime ${\displaystyle p}$ is used, allowing an efficient computation of the discrete logarithm with Pohlig–Hellman if the order of the group (being ${\displaystyle p-1}$) is sufficiently [smooth](/wiki/Smooth_number), i.e. has no large [prime factors](/wiki/Prime_factor).



## Comparison with integer factorization


While computing discrete logarithms and integer factorization are distinct problems, they share some properties:


- both are special cases of the [hidden subgroup problem](/wiki/Hidden_subgroup_problem) for [finite abelian groups](/wiki/Finite_abelian_group),
- both problems seem to be difficult (no efficient algorithms are known for non-[quantum computers](/wiki/Quantum_computer)),
- for both problems efficient algorithms on quantum computers are known,
- algorithms from one problem are often adapted to the other, and
- the difficulty of both problems has been used to construct various [cryptographic](/wiki/Cryptographic) systems.



## Cryptography


There exist groups for which computing discrete logarithms is apparently difficult.  In some cases (e.g. large prime order subgroups of  groups ${\displaystyle \mathbf {Z} _{p}^{\times }}$) there is not only no efficient algorithm known for the worst case, but the [average-case complexity](/wiki/Average-case_complexity) can be shown to be about as hard as the worst case using [random self-reducibility](/wiki/Random_self-reducibility).[[5]](#cite_note-5)

At the same time, the inverse problem of discrete exponentiation is not difficult (it can be computed efficiently using [exponentiation by squaring](/wiki/Exponentiation_by_squaring), for example).  This asymmetry is analogous to the one between integer factorization and integer multiplication. Both asymmetries (and other possibly [one-way functions](/wiki/One-way_function)) have been exploited in the construction of cryptographic systems.

Popular choices for the group ${\displaystyle G}$ in discrete logarithm cryptography (DLC) are the cyclic groups ${\displaystyle \mathbf {Z} _{p}^{\times }}$ (e.g. [ElGamal encryption](/wiki/ElGamal_encryption), [Diffie–Hellman key exchange](/wiki/Diffie%E2%80%93Hellman_key_exchange), and the [Digital Signature Algorithm](/wiki/Digital_Signature_Algorithm)) and cyclic subgroups of [elliptic curves](/wiki/Elliptic_curve) over [finite fields](/wiki/Finite_field) (*see* [Elliptic curve cryptography](/wiki/Elliptic_curve_cryptography)).

While there is no publicly known algorithm for solving the discrete logarithm problem in general, the first three steps of the [number field sieve](/wiki/General_number_field_sieve) algorithm only depend on the group ${\displaystyle G}$, not on the specific elements of ${\displaystyle G}$ whose finite ${\displaystyle \log }$ is desired. By [precomputing](/wiki/Precomputing) these three steps for a specific group, one need only carry out the last step, which is much less computationally expensive than the first three, to obtain a specific logarithm in that group.[[6]](#cite_note-imperfectfs-6)

It turns out that much [internet](/wiki/Internet) traffic uses one of a handful of groups that are of order 1024 bits or less, e.g. cyclic groups with order of the Oakley primes specified in RFC 2409.[[7]](#cite_note-7) The [Logjam](/wiki/Logjam_(computer_security)) attack used this vulnerability to compromise a variety of internet services that allowed the use of groups whose order was a 512-bit prime number, so called [export grade](/wiki/Export_of_cryptography).[[6]](#cite_note-imperfectfs-6)

The authors of the Logjam attack estimate that the much more difficult precomputation needed to solve the discrete log problem for a 1024-bit prime would be within the budget of a large national [intelligence agency](/wiki/Intelligence_agency) such as the U.S. [National Security Agency](/wiki/National_Security_Agency) (NSA). The Logjam authors speculate that precomputation against widely reused 1024 DH primes is behind claims in [leaked NSA documents](/wiki/Global_surveillance_disclosures_(2013%E2%80%93present)) that NSA is able to break much of current cryptography.[[6]](#cite_note-imperfectfs-6)



## See also


- [A. W. Faber Model 366](/wiki/A._W._Faber_Model_366)
- [Percy Ludgate](/wiki/Percy_Ludgate) and [Irish logarithm](/wiki/Irish_logarithm)



## References



1. **[^](#cite_ref-1)** Menezes, Alfred J.; van Oorschot, Paul C.; Vanstone, Scott A. (1996). ["Public-Key Encryption"](https://cacr.uwaterloo.ca/hac/about/chap8.pdf) (PDF). [*Handbook of Applied Cryptography*](https://www.taylorfrancis.com/books/9780429881329) (1 ed.). CRC Press. p. 294. [doi](/wiki/Doi_(identifier)):[10.1201/9780429466335](https://doi.org/10.1201%2F9780429466335). [ISBN](/wiki/ISBN_(identifier)) [978-0-429-46633-5](/wiki/Special:BookSources/978-0-429-46633-5).
2. **[^](#cite_ref-2)** Shoup...
3. ^ [***a***](#cite_ref-:0_3-0) [***b***](#cite_ref-:0_3-1) Lam, Kwok-Yan; Shparlinski, Igor; Wang, Huaxiong; Xing, Chaoping, eds. (2001). [*Cryptography and Computational Number Theory*](https://link.springer.com/10.1007/978-3-0348-8295-8). Basel: Birkhäuser Basel. pp. 54–56. [doi](/wiki/Doi_(identifier)):[10.1007/978-3-0348-8295-8](https://doi.org/10.1007%2F978-3-0348-8295-8). [eISSN](/wiki/EISSN_(identifier)) [2297-0584](https://search.worldcat.org/issn/2297-0584). [ISBN](/wiki/ISBN_(identifier)) [978-3-0348-9507-1](/wiki/Special:BookSources/978-3-0348-9507-1). [ISSN](/wiki/ISSN_(identifier)) [2297-0576](https://search.worldcat.org/issn/2297-0576).
4. **[^](#cite_ref-4)** Shor, Peter (1997). "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer". *SIAM Journal on Computing*. **26** (5): 1484–1509. [arXiv](/wiki/ArXiv_(identifier)):[quant-ph/9508027](https://arxiv.org/abs/quant-ph/9508027). [doi](/wiki/Doi_(identifier)):[10.1137/s0097539795293172](https://doi.org/10.1137%2Fs0097539795293172). [MR](/wiki/MR_(identifier)) [1471990](https://mathscinet.ams.org/mathscinet-getitem?mr=1471990). [S2CID](/wiki/S2CID_(identifier)) [2337707](https://api.semanticscholar.org/CorpusID:2337707).
5. **[^](#cite_ref-5)** Blake, Ian F.; Garefalakis, Theo (2004-04-01). ["On the complexity of the discrete logarithm and Diffie–Hellman problems"](https://doi.org/10.1016%2Fj.jco.2004.01.002). *Journal of Complexity*. Festschrift for Harald Niederreiter, Special Issue on Coding and Cryptography. **20** (2): 148–170. [doi](/wiki/Doi_(identifier)):[10.1016/j.jco.2004.01.002](https://doi.org/10.1016%2Fj.jco.2004.01.002). [ISSN](/wiki/ISSN_(identifier)) [0885-064X](https://search.worldcat.org/issn/0885-064X).
6. ^ [***a***](#cite_ref-imperfectfs_6-0) [***b***](#cite_ref-imperfectfs_6-1) [***c***](#cite_ref-imperfectfs_6-2) Adrian, David; Bhargavan, Karthikeyan; Durumeric, Zakir; Gaudry, Pierrick; Green, Matthew; Halderman, J. Alex; [Heninger, Nadia](/wiki/Nadia_Heninger); Springall, Drew; Thomé, Emmanuel; Valenta, Luke; VanderSloot, Benjamin; Wustrow, Eric; Zanella-Béguelin, Santiago; Zimmermann, Paul (2015-10-12). ["Imperfect Forward Secrecy: How Diffie-Hellman Fails in Practice"](https://dl.acm.org/doi/10.1145/2810103.2813707). *Proceedings of the 22nd ACM SIGSAC Conference on Computer and Communications Security*. ACM. pp. 5–17. [doi](/wiki/Doi_(identifier)):[10.1145/2810103.2813707](https://doi.org/10.1145%2F2810103.2813707). [ISBN](/wiki/ISBN_(identifier)) [978-1-4503-3832-5](/wiki/Special:BookSources/978-1-4503-3832-5).
7. **[^](#cite_ref-7)** Harkins, D.; Carrel, D. (November 1998). [The Internet Key Exchange (IKE)](https://www.rfc-editor.org/info/rfc2409) (Report). RFC Editor. [doi](/wiki/Doi_(identifier)):[10.17487/rfc2409](https://doi.org/10.17487%2Frfc2409).



- Rosen, Kenneth H. (2011). *Elementary Number Theory and Its Application* (6 ed.). Pearson. p. 368. [ISBN](/wiki/ISBN_(identifier)) [978-0321500311](/wiki/Special:BookSources/978-0321500311).
- Weisstein, Eric W. ["Discrete Logarithm"](http://mathworld.wolfram.com/DiscreteLogarithm.html). *MathWorld*. Wolfram Web. Retrieved 2019-01-01.




## Further reading


- [Richard Crandall](/wiki/Richard_Crandall); [Carl Pomerance](/wiki/Carl_Pomerance). Chapter 5, *Prime Numbers: A computational perspective*, 2nd ed., Springer.
- Stinson, Douglas Robert (2006). *Cryptography: Theory and Practice* (3 ed.). London, UK: [CRC Press](/wiki/CRC_Press). [ISBN](/wiki/ISBN_(identifier)) [978-1-58488-508-5](/wiki/Special:BookSources/978-1-58488-508-5).


- [v](/wiki/Template:Number-theoretic_algorithms)
- [t](/wiki/Template_talk:Number-theoretic_algorithms)
- [e](/wiki/Special:EditPage/Template:Number-theoretic_algorithms)

[Number-theoretic](/wiki/Number_theory) [algorithms](/wiki/Algorithm)[Primality tests](/wiki/Primality_test)
- [AKS](/wiki/AKS_primality_test)
- [APR](/wiki/Adleman%E2%80%93Pomerance%E2%80%93Rumely_primality_test)
- [Baillie–PSW](/wiki/Baillie%E2%80%93PSW_primality_test)
- [Elliptic curve](/wiki/Elliptic_curve_primality)
- [Pocklington](/wiki/Pocklington_primality_test)
- [Fermat](/wiki/Fermat_primality_test)
- [Lucas](/wiki/Lucas_primality_test)
- *[Lucas–Lehmer](/wiki/Lucas%E2%80%93Lehmer_primality_test)*
- *[Lucas–Lehmer–Riesel](/wiki/Lucas%E2%80%93Lehmer%E2%80%93Riesel_test)*
- *[Proth's theorem](/wiki/Proth%27s_theorem)*
- *[Pépin's](/wiki/P%C3%A9pin%27s_test)*
- [Quadratic Frobenius](/wiki/Quadratic_Frobenius_test)
- [Solovay–Strassen](/wiki/Solovay%E2%80%93Strassen_primality_test)
- [Miller–Rabin](/wiki/Miller%E2%80%93Rabin_primality_test)


[Prime-generating](/wiki/Generating_primes)
- [Sieve of Atkin](/wiki/Sieve_of_Atkin)
- [Sieve of Eratosthenes](/wiki/Sieve_of_Eratosthenes)
- [Sieve of Pritchard](/wiki/Sieve_of_Pritchard)
- [Sieve of Sundaram](/wiki/Sieve_of_Sundaram)
- [Wheel factorization](/wiki/Wheel_factorization)


[Integer factorization](/wiki/Integer_factorization)
- [Continued fraction (CFRAC)](/wiki/Continued_fraction_factorization)
- [Dixon's](/wiki/Dixon%27s_factorization_method)
- [Lenstra elliptic curve (ECM)](/wiki/Lenstra_elliptic-curve_factorization)
- [Euler's](/wiki/Euler%27s_factorization_method)
- [Pollard's rho](/wiki/Pollard%27s_rho_algorithm)
- [*p* − 1](/wiki/Pollard%27s_p_%E2%88%92_1_algorithm)
- [*p* + 1](/wiki/Williams%27s_p_%2B_1_algorithm)
- [Quadratic sieve (QS)](/wiki/Quadratic_sieve)
- [General number field sieve (GNFS)](/wiki/General_number_field_sieve)
- *[Special number field sieve (SNFS)](/wiki/Special_number_field_sieve)*
- [Rational sieve](/wiki/Rational_sieve)
- [Fermat's](/wiki/Fermat%27s_factorization_method)
- [Shanks's square forms](/wiki/Shanks%27s_square_forms_factorization)
- [Trial division](/wiki/Trial_division)
- [Shor's](/wiki/Shor%27s_algorithm)


[Multiplication](/wiki/Multiplication_algorithm)
- [Ancient Egyptian](/wiki/Ancient_Egyptian_multiplication)
- [Long](/wiki/Long_multiplication)
- [Karatsuba](/wiki/Karatsuba_algorithm)
- [Toom–Cook](/wiki/Toom%E2%80%93Cook_multiplication)
- [Schönhage–Strassen](/wiki/Sch%C3%B6nhage%E2%80%93Strassen_algorithm)
- [Fürer's](/wiki/F%C3%BCrer%27s_algorithm)


[Euclidean](/wiki/Euclidean_division) [division](/wiki/Division_algorithm)
- [Binary](/wiki/Binary_division)
- [Chunking](/wiki/Chunking_(division))
- [Fourier](/wiki/Fourier_division)
- [Goldschmidt](/wiki/Goldschmidt_division)
- [Newton-Raphson](/wiki/Newton%E2%80%93Raphson_division)
- [Long](/wiki/Long_division)
- [Short](/wiki/Short_division)
- [SRT](/wiki/SRT_division)


Discrete logarithm
- [Baby-step giant-step](/wiki/Baby-step_giant-step)
- [Pollard rho](/wiki/Pollard%27s_rho_algorithm_for_logarithms)
- [Pollard kangaroo](/wiki/Pollard%27s_kangaroo_algorithm)
- [Pohlig–Hellman](/wiki/Pohlig%E2%80%93Hellman_algorithm)
- [Index calculus](/wiki/Index_calculus_algorithm)
- [Function field sieve](/wiki/Function_field_sieve)


[Greatest common divisor](/wiki/Greatest_common_divisor)
- [Binary](/wiki/Binary_GCD_algorithm)
- [Euclidean](/wiki/Euclidean_algorithm)
- [Extended Euclidean](/wiki/Extended_Euclidean_algorithm)
- [Lehmer's](/wiki/Lehmer%27s_GCD_algorithm)


[Modular square root](/wiki/Quadratic_residue)
- [Cipolla](/wiki/Cipolla%27s_algorithm)
- [Pocklington's](/wiki/Pocklington%27s_algorithm)
- [Tonelli–Shanks](/wiki/Tonelli%E2%80%93Shanks_algorithm)
- [Berlekamp](/wiki/Berlekamp%E2%80%93Rabin_algorithm)


Other algorithms
- [Chakravala](/wiki/Chakravala_method)
- [Cornacchia](/wiki/Cornacchia%27s_algorithm)
- [Exponentiation by squaring](/wiki/Exponentiation_by_squaring)
- [Integer square root](/wiki/Integer_square_root)
- [Integer relation](/wiki/Integer_relation_algorithm) ([LLL](/wiki/Lenstra%E2%80%93Lenstra%E2%80%93Lov%C3%A1sz_lattice_basis_reduction_algorithm); [KZ](/wiki/Korkine%E2%80%93Zolotarev_lattice_basis_reduction_algorithm))
- [Modular exponentiation](/wiki/Modular_exponentiation)
- [Montgomery reduction](/wiki/Montgomery_reduction)
- [Schoof](/wiki/Schoof%27s_algorithm)
- [Trachtenberg system](/wiki/Trachtenberg_system)



- *Italics* indicate that algorithm is for numbers of special forms



- [v](/wiki/Template:Cryptography_public-key)
- [t](/wiki/Template_talk:Cryptography_public-key)
- [e](/wiki/Special:EditPage/Template:Cryptography_public-key)

[Public-key cryptography](/wiki/Public-key_cryptography)Algorithms[Integer factorization](/wiki/Integer_factorization)
- [Benaloh](/wiki/Benaloh_cryptosystem)
- [Blum–Goldwasser](/wiki/Blum%E2%80%93Goldwasser_cryptosystem)
- [Cayley–Purser](/wiki/Cayley%E2%80%93Purser_algorithm)
- [Damgård–Jurik](/wiki/Damg%C3%A5rd%E2%80%93Jurik_cryptosystem)
- [GMR](/wiki/GMR_(cryptography))
- [Goldwasser–Micali](/wiki/Goldwasser%E2%80%93Micali_cryptosystem)
- [Naccache–Stern](/wiki/Naccache%E2%80%93Stern_cryptosystem)
- [Paillier](/wiki/Paillier_cryptosystem)
- [Rabin](/wiki/Rabin_signature)
- [RSA](/wiki/RSA_cryptosystem)
- [Okamoto–Uchiyama](/wiki/Okamoto%E2%80%93Uchiyama_cryptosystem)
- [Schmidt–Samoa](/wiki/Schmidt-Samoa_cryptosystem)


Discrete logarithm
- [BLS](/wiki/Boneh%E2%80%93Lynn%E2%80%93Shacham)
- [Cramer–Shoup](/wiki/Cramer%E2%80%93Shoup_cryptosystem)
- [DH](/wiki/Diffie%E2%80%93Hellman_key_exchange)
- [DSA](/wiki/Digital_Signature_Algorithm)
- [ECDH](/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)
- [X25519](/wiki/Curve25519)
- [X448](/wiki/Curve448)
- [ECDSA](/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- [EdDSA](/wiki/EdDSA)
- [Ed25519](/wiki/EdDSA#Ed25519)
- [Ed448](/wiki/EdDSA#Ed448)
- [ECMQV](/wiki/ECMQV)
- [EKE](/wiki/Encrypted_key_exchange)
- [ElGamal](/wiki/ElGamal_encryption)
- [signature scheme](/wiki/ElGamal_signature_scheme)
- [MQV](/wiki/MQV)
- [Schnorr](/wiki/Schnorr_signature)
- [SPEKE](/wiki/SPEKE)
- [SRP](/wiki/Secure_Remote_Password_protocol)
- [STS](/wiki/Station-to-Station_protocol)


[Lattice/SVP/CVP](/wiki/Lattice-based_cryptography)/[LWE](/wiki/Learning_with_errors)/[SIS](/wiki/Short_integer_solution_problem)
- [BLISS](/wiki/BLISS_signature_scheme)
- [Kyber](/wiki/Kyber)
- [NewHope](/wiki/NewHope)
- [NTRUEncrypt](/wiki/NTRUEncrypt)
- [NTRUSign](/wiki/NTRUSign)
- [RLWE-KEX](/wiki/RLWE-KEX)
- [RLWE-SIG](/wiki/RLWE-SIG)


Others
- [AE](/wiki/Algebraic_Eraser)
- [CEILIDH](/wiki/CEILIDH)
- [EPOC](/wiki/Efficient_Probabilistic_Public-Key_Encryption_Scheme)
- [HFE](/wiki/Hidden_Field_Equations)
- [IES](/wiki/Integrated_Encryption_Scheme)
- [Lamport](/wiki/Lamport_signature)
- [McEliece](/wiki/McEliece_cryptosystem)
- [Merkle–Hellman](/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem)
- [Naccache–Stern knapsack cryptosystem](/wiki/Naccache%E2%80%93Stern_knapsack_cryptosystem)
- [Three-pass protocol](/wiki/Three-pass_protocol)
- [XTR](/wiki/XTR)
- [SQIsign](/wiki/SQIsign)
- [SPHINCS+](/wiki/SPHINCS%2B)


Theory
- [Discrete logarithm cryptography](#Cryptography)
- [Elliptic-curve cryptography](/wiki/Elliptic-curve_cryptography)
- [Hash-based cryptography](/wiki/Hash-based_cryptography)
- [Non-commutative cryptography](/wiki/Non-commutative_cryptography)
- [RSA problem](/wiki/RSA_problem)
- [Trapdoor function](/wiki/Trapdoor_function)


Standardization
- [CRYPTREC](/wiki/CRYPTREC)
- [IEEE P1363](/wiki/IEEE_P1363)
- [NESSIE](/wiki/NESSIE)
- [NSA Suite B](/wiki/NSA_Suite_B_Cryptography)
- [CNSA](/wiki/Commercial_National_Security_Algorithm_Suite)
- [Post-Quantum Cryptography](/wiki/NIST_Post-Quantum_Cryptography_Standardization)


Topics
- [Digital signature](/wiki/Digital_signature)
- [OAEP](/wiki/Optimal_asymmetric_encryption_padding)
- [Fingerprint](/wiki/Public_key_fingerprint)
- [PKI](/wiki/Public_key_infrastructure)
- [Web of trust](/wiki/Web_of_trust)
- [Key size](/wiki/Key_size)
- [Identity-based cryptography](/wiki/Identity-based_cryptography)
- [Post-quantum cryptography](/wiki/Post-quantum_cryptography)
- [OpenPGP card](/wiki/OpenPGP_card)



- [v](/wiki/Template:Computational_hardness_assumptions)
- [t](/wiki/Template_talk:Computational_hardness_assumptions)
- [e](/wiki/Special:EditPage/Template:Computational_hardness_assumptions)

[Computational hardness assumptions](/wiki/Computational_hardness_assumption)Number theoretic
- [Integer factorization](/wiki/Integer_factorization)
- [Phi-hiding](/wiki/Phi-hiding_assumption)
- [RSA problem](/wiki/RSA_problem)
- [Strong RSA](/wiki/Strong_RSA_assumption)
- [Quadratic residuosity](/wiki/Quadratic_residuosity_problem)
- [Decisional composite residuosity](/wiki/Decisional_composite_residuosity_assumption)
- [Higher residuosity](/wiki/Higher_residuosity_problem)


Group theoretic
- [Discrete logarithm](#Cryptography)
- [Diffie-Hellman](/wiki/Diffie%E2%80%93Hellman_problem)
- [Decisional Diffie–Hellman](/wiki/Decisional_Diffie%E2%80%93Hellman_assumption)
- [Computational Diffie–Hellman](/wiki/Computational_Diffie%E2%80%93Hellman_assumption)


Pairings
- [External Diffie–Hellman](/wiki/XDH_assumption)
- [Sub-group hiding](/wiki/Sub-group_hiding)
- [Decision linear](/wiki/Decision_Linear_assumption)


Lattices
- [Shortest vector problem](/wiki/Lattice_problem#Shortest_vector_problem_(SVP)) ([gap](/wiki/Lattice_problem#GapSVP))
- [Closest vector problem](/wiki/Lattice_problem#Closest_vector_problem_(CVP)) ([gap](/wiki/Lattice_problem#GapCVP))
- [Learning with errors](/wiki/Learning_with_errors)
- [Ring learning with errors](/wiki/Ring_learning_with_errors)
- [Short integer solution](/wiki/Short_integer_solution_problem)


Non-cryptographic
- [Exponential time hypothesis](/wiki/Exponential_time_hypothesis)
- [Unique games conjecture](/wiki/Unique_games_conjecture)
- [Planted clique conjecture](/wiki/Planted_clique)



 
NewPP limit report
Parsed by mw‐web.eqiad.main‐669fff9b5‐95kdx
Cached time: 20260503023435
Cache expiry: 2592000
Cache expiry source: Module:Citation/CS1 (os.date(%Y))
Reduced expiry: false
Complications: [vary‐revision‐sha1, show‐toc]
CPU time usage: 0.319 seconds
Real time usage: 0.558 seconds
Preprocessor visited node count: 1793/1000000
Revision size: 18506/2097152 bytes
Post‐expand include size: 67957/2097152 bytes
Template argument size: 960/2097152 bytes
Highest expansion depth: 12/100
Expensive parser function count: 4/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 65292/5000000 bytes
Lua time usage: 0.142/10.000 seconds
Lua memory usage: 5682501/52428800 bytes
Number of Wikibase entities loaded: 0/500


Transclusion expansion time report (%,ms,calls,template)
100.00%  246.185      1 -total
 32.82%   80.797      1 Template:Reflist
 26.33%   64.821      5 Template:Cite_book
 23.06%   56.765      3 Template:Navbox
 22.85%   56.265      1 Template:Number_theoretic_algorithms
 17.47%   43.018      1 Template:Short_description
 11.09%   27.292      2 Template:Pagetype
  6.76%   16.645      1 Template:See_also
  3.74%    9.215      1 Template:Use_dmy_dates
  3.74%    9.203      4 Template:Main_other

 Render ID 9f7df492-4698-11f1-aebb-2598b00409d7 
 Saved in parser cache with key enwiki:pcache:181334:|#|:idhash:canonical and timestamp 20260503023435 and revision id 1323312909. Rendering was triggered because: page_view
 
![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

---


Retrieved from "[https://en.wikipedia.org/w/index.php?title=Discrete_logarithm&oldid=1323312909](https://en.wikipedia.org/w/index.php?title=Discrete_logarithm&oldid=1323312909)"
