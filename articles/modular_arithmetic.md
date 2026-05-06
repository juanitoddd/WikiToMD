[![icon](https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/60px-Question_book-new.svg.png)

---](/wiki/File:Question_book-new.svg)This article **needs additional citations for [verification](/wiki/Wikipedia:Verifiability)**. Please help [improve this article](/wiki/Special:EditPage/Modular_arithmetic) by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners). Unsourced material may be challenged and removed.*Find sources:* ["Modular arithmetic"](https://www.google.com/search?as_eq=wikipedia&q=%22Modular+arithmetic%22) – [news](https://www.google.com/search?tbm=nws&q=%22Modular+arithmetic%22+-wikipedia&tbs=ar:1) **·** [newspapers](https://www.google.com/search?&q=%22Modular+arithmetic%22&tbs=bkt:s&tbm=bks) **·** [books](https://www.google.com/search?tbs=bks:1&q=%22Modular+arithmetic%22+-wikipedia) **·** [scholar](https://scholar.google.com/scholar?q=%22Modular+arithmetic%22) **·** [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Modular+arithmetic%22&acc=on&wc=on) *(June 2025)**([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal))*




[![Left: Analog clock reading 9 o'clock. Right: After four hours have passed, the clock now reads 1 o'clock.](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Clock_group.svg/330px-Clock_group.svg.png)](/wiki/File:Clock_group.svg)Time-keeping on this clock uses arithmetic modulo 12. Adding 4 hours to 9 o'clock gives 1 o'clock, since 13 is congruent to 1 modulo 12.

---


In [mathematics](/wiki/Mathematics), **modular arithmetic** is a system of [arithmetic](/wiki/Arithmetic) operations for [integers](/wiki/Integer), differing from the usual ones in that numbers "wrap around" when reaching or exceeding a certain value, called the **modulus**. The modern approach to [number theory](/wiki/Number_theory) using modular arithmetic was developed by [Carl Friedrich Gauss](/wiki/Carl_Friedrich_Gauss) in his book *[Disquisitiones Arithmeticae](/wiki/Disquisitiones_Arithmeticae)*, published in 1801.[[1]](#cite_note-1)

*Modular arithmetic modulo* m consists of systematically replacing the results of additions, multiplications, and subtractions by the remainder of the division by m. A  remarkable property of modular arithmetic is that the result of a computation does not depend on whether the division by m is performed after each operation, only once at the end of the computation, or at the end of the computation and after some intermediate results—typically when an intermediate result becomes too large.




## Motivating example


A familiar setting exhibiting modular arithmetic is the [hour hand](/wiki/Hour_hand) on a [12-hour clock](/wiki/12-hour_clock). If the hour hand points to 7 now, then 8 hours later it will point to 3. Ordinary addition would result in 7 + 8 = 15, but  15 reads as 3 on the clock face. This is because the hour hand makes one rotation every 12 hours and the hour number starts over when the hour hand passes 12. We say that 15 is *congruent* to 3 modulo 12, and we write 15 ≡ 3 (mod 12), so 7 + 8 ≡ 3 (mod 12).

Similarly, if one waits 8 hours and then 8 more hours (thus 16 hours in total), the clock will show the same time change as if one waited 4 hours.  This is reflected by the identity 2 × 8 ≡ 4 (mod 12). After a wait of exactly 12 hours, the hour hand will be right where it started, so 12 acts as 0; one writes 12 ≡ 0 (mod 12).



## Congruence


Given an [integer](/wiki/Integer) *m* ≥ 1, called a **modulus**, two integers a and b are said to be **congruent** modulo m, if their difference *a* − *b* is an [integer multiple](/wiki/Integer_multiple) of m; that is, if there is an integer *k* such that


*a* − *b* = *km*.
Congruence modulo m is a [congruence relation](/wiki/Congruence_relation), meaning that it is an [equivalence relation](/wiki/Equivalence_relation) compatible with [addition](/wiki/Addition), [subtraction](/wiki/Subtraction), and [multiplication](/wiki/Multiplication). Congruence modulo m is denoted by


${\displaystyle a\equiv b{\pmod {m}}.}$
The parentheses mean that (mod *m*) applies to the entire equation, not just to the right-hand side (here, b).

This notation is not to be confused with the notation *b* mod *m* or (*b* mod *m*) (without parentheses immediately before "mod"), which refers to the remainder of *b* when divided by *m*, known as the [modulo](/wiki/Modulo) operation; that is, *b* mod *m* denotes the unique integer r such that 0 ≤ *r* < *m* and *r* ≡ *b* (mod *m*). So, the relation ${\displaystyle a\equiv b{\pmod {m}}}$ must be read ${\displaystyle (a\equiv b){\bmod {m}},}$  and is equivalent with ${\displaystyle a{\bmod {m}}=b{\bmod {m}}.}$

The congruence relation *a* ≡ *b* (mod *m*) may be rewritten as
${\displaystyle \exists k\in \mathbb {Z} \quad a=km+b,}$
explicitly showing its relationship with [Euclidean division](/wiki/Euclidean_division). However, the *b* here need not be the remainder in the division of *a* by *m*. Rather, *a* ≡ *b* (mod *m*) asserts that *a* and *b* have the same [remainder](/wiki/Remainder) when divided by *m*. That is,


*a* = *p m* + *r*,
*b* = *q m* + *r*,
where 0 ≤ *r* < *m* is the common remainder. We recover the previous relation (*a* − *b* = *k m*) by subtracting these two expressions and setting *k* = *p* − *q*.

Because the congruence modulo m is defined by the [divisibility](/wiki/Divisor#Further_notions_and_facts) by m and because −1 is a [unit](/wiki/Unit_(ring_theory)#Integer_ring) in the ring of integers, a number is divisible by −*m* exactly if it is divisible by m.
This means that every non-zero integer m may be taken as a modulus.



### Examples


In modulus 12, one can assert that:


38 ≡ 14 (mod 12)
because the difference is 38 − 14 = 24 = 2 × 12, a multiple of 12. Equivalently, 38 and 14 have the same remainder 2 when divided by 12.

The definition of congruence also applies to negative values. For example:


${\displaystyle {\begin{aligned}2&\equiv -3{\pmod {5}}\\-8&\equiv {\phantom {+}}7{\pmod {5}}\\-3&\equiv -8{\pmod {5}}.\end{aligned}}}$

## Basic properties


The congruence relation satisfies all the conditions of an [equivalence relation](/wiki/Equivalence_relation):


- Reflexivity: *a* ≡ *a* (mod *m*)
- Symmetry: *a* ≡ *b* (mod *m*) if and only if *b* ≡ *a* (mod *m*).
- Transitivity: If *a* ≡ *b* (mod *m*) and *b* ≡ *c* (mod *m*), then *a* ≡ *c* (mod *m*)


If *a*1 ≡ *b*1 (mod *m*) and *a*2 ≡ *b*2 (mod *m*), or if *a* ≡ *b* (mod *m*), then:[[2]](#cite_note-FOOTNOTELehoczkyRusczky2006-2)


- *a* + *k* ≡ *b* + *k* (mod *m*) for any integer *k* (compatibility with translation)
- *k a* ≡ *k b* (mod *m*) for any integer *k* (compatibility with scaling)
- *k a* ≡ *k b* (mod *k m*) for any integer *k*
- *a*1 + *a*2 ≡ *b*1 + *b*2 (mod *m*) (compatibility with addition)
- *a*1 − *a*2 ≡ *b*1 − *b*2 (mod *m*) (compatibility with subtraction)
- *a*1 *a*2 ≡ *b*1 *b*2 (mod *m*) (compatibility with multiplication)
- *a**k* ≡ *b**k* (mod *m*) for any non-negative integer *k* (compatibility with exponentiation)
- *p*(*a*) ≡ *p*(*b*) (mod *m*), for any [polynomial](/wiki/Polynomial) *p*(*x*) with integer coefficients (compatibility with polynomial evaluation)


If *a* ≡ *b* (mod *m*), then it is generally false that *ka* ≡ *kb* (mod *m*). However, the following is true:


- If *c* ≡ *d* (mod *φ*(*m*)), where *φ* is [Euler's totient function](/wiki/Euler%27s_totient_function), then *a**c* ≡ *a**d* (mod *m*)—provided that *a* is [coprime](/wiki/Coprime) with *m*.


If *a* ≡ *b* (mod *mn*), then *a* ≡ *b* (mod *m*) and *a* ≡ *b* (mod *n*).

For cancellation of common terms, we have the following rules:


- If *a* + *k* ≡ *b* + *k* (mod *m*), where *k* is any integer, then *a* ≡ *b* (mod *m*).
- If *k a* ≡ *k b* (mod *m*) and *k* is coprime with *m*, then *a* ≡ *b* (mod *m*).
- If *k a* ≡ *k b* (mod *k m*) and *k* ≠ 0, then *a* ≡ *b* (mod *m*).


The last rule can be used to move modular arithmetic into division. If *b* divides *a*, then (*a*/*b*) mod *m* = (*a* mod (*b m*)) / *b*.

The [modular multiplicative inverse](/wiki/Modular_multiplicative_inverse) is defined by the following rules:


- Existence: There exists an integer denoted *a*−1 such that *aa*−1 ≡ 1 (mod *m*) if and only if *a* is coprime with *m*. This integer *a*−1 is called a *modular multiplicative inverse* of a modulo *m*.
- If *a* ≡ *b* (mod *m*) and *a*−1 exists, then *a*−1 ≡ *b*−1 (mod *m*) (compatibility with multiplicative inverse, and, if *a* = *b*, uniqueness modulo *m*).
- If *ax* ≡ *b* (mod *m*) and *a* is coprime to *m*, then the solution to this linear congruence is given by *x* ≡ *a*−1*b* (mod *m*).


The multiplicative inverse *x* ≡ *a*−1 (mod *m*)  may be efficiently computed by solving [Bézout's equation](/wiki/B%C3%A9zout%27s_identity) *a x* + *m y* = 1 for *x*, *y*, by using the [Extended Euclidean algorithm](/wiki/Modular_multiplicative_inverse#Extended_Euclidean_algorithm).

In particular, if *p* is a prime number, then *a* is coprime with *p* for every *a* such that 0 < *a* < *p*; thus a multiplicative inverse exists for all *a* that is not congruent to zero modulo *p*.



## Advanced properties


Some of the more advanced properties of congruence relations are the following:


- [Fermat's little theorem](/wiki/Fermat%27s_little_theorem): If *p* is prime and does not divide *a*, then *a**p*−1 ≡ 1 (mod *p*).
- [Euler's theorem](/wiki/Euler%27s_theorem): If *a* and *m* are coprime, then *a**φ*(*m*) ≡ 1 (mod *m*), where *φ* is [Euler's totient function](/wiki/Euler%27s_totient_function).
- A simple consequence of Fermat's little theorem is that if *p* is prime, then *a*−1 ≡ *a**p*−2 (mod *p*) is the multiplicative inverse of 0 < *a* < *p*. More generally, from Euler's theorem, if *a* and *m* are coprime, then *a*−1 ≡ *a**φ*(*m*)−1 (mod *m*). Hence, if *ax* ≡ *1* (mod *m*), then *x* ≡ *a**φ*(*m*)−1 (mod *m*).
- Another simple consequence is that if *a* ≡ *b* (mod *φ*(*m*)), where *φ* is Euler's totient function, then *k**a* ≡ *k**b* (mod *m*) provided *k* is [coprime](/wiki/Coprime) with *m*.
- [Wilson's theorem](/wiki/Wilson%27s_theorem): *p* is prime if and only if (*p* − 1)! ≡ −1 (mod *p*).
- [Chinese remainder theorem](/wiki/Chinese_remainder_theorem): For any *a*, *b*  and coprime *m*, *n*, there exists a unique *x* (mod *mn*) such that *x* ≡ *a* (mod *m*) and *x* ≡ *b* (mod *n*). In fact,  *x* ≡ *b m**n*−1 *m* + *a n**m*−1 *n* (mod *mn*) where *m**n*−1 is the inverse of *m* modulo *n* and *n**m*−1 is the inverse of *n* modulo *m*.
- [Lagrange's theorem](/wiki/Lagrange%27s_theorem_(number_theory)): If *p* is prime and *f* (*x*) = *a*0 *x**d* + ... + *a**d* is a [polynomial](/wiki/Polynomial) with integer coefficients such that p is not a divisor of *a*0, then the congruence *f* (*x*) ≡ 0 (mod *p*)  has at most *d* non-congruent solutions.
- [Primitive root modulo *m*](/wiki/Primitive_root_modulo_n): A number *g* is a primitive root modulo *m* if, for every integer *a* coprime to *m*, there is an integer *k* such that *g**k* ≡ *a* (mod *m*). A primitive root modulo *m* exists if and only if *m* is equal to 2, 4, *p**k* or  2*p**k*, where *p* is an odd prime number and *k* is a positive integer. If a primitive root modulo *m* exists, then there are exactly *φ*(*φ*(*m*)) such primitive roots, where *φ* is the Euler's totient function.
- [Quadratic residue](/wiki/Quadratic_residue): An integer *a* is a quadratic residue modulo *m*, if there exists an integer *x* such that *x*2 ≡ *a* (mod *m*). [Euler's criterion](/wiki/Euler%27s_criterion) asserts that, if *p* is an odd prime, and a is not a multiple of p, then *a* is a quadratic residue modulo *p* if and only if
*a*(*p*−1)/2 ≡ 1 (mod *p*).



## Congruence classes


The congruence relation is an [equivalence relation](/wiki/Equivalence_relation). The [equivalence class](/wiki/Equivalence_class) modulo m of an integer *a* is the set of all integers of the form *a* + *k m*, where k is any integer. It is called the **congruence class** or **residue class** of *a* modulo *m*, and may be denoted (*a* mod *m*), or as *a* or [*a*] when the modulus *m* is known from the context.

Each residue class modulo *m* contains exactly one integer in the range ${\displaystyle 0,...,|m|-1}$. Thus, these ${\displaystyle |m|}$ integers are [representatives](/wiki/Representative_(mathematics)) of their respective residue classes.

It is generally easier to work with integers than sets of integers; that is, the representatives most often considered, rather than their residue classes.

Consequently, (*a* mod *m*) denotes generally the unique integer r such that 0 ≤ *r* < *m* and *r* ≡ *a* (mod *m*); it is called the **residue** of *a* modulo *m*.

In particular, (*a* mod *m*) = (*b* mod *m*) is equivalent to *a* ≡ *b* (mod *m*), and this explains why "=" is often used instead of "≡" in this context.



## Residue systems


Each residue class modulo *m* may be represented by any one of its members, although we usually represent each residue class by the smallest nonnegative integer which belongs to that class[[3]](#cite_note-FOOTNOTEWeisstein-3) (since this is the proper remainder which results from division). Any two members of different residue classes modulo *m* are incongruent modulo *m*. Furthermore, every integer belongs to one and only one residue class modulo *m*.[[4]](#cite_note-FOOTNOTEPettofrezzoByrkit197090-4)

The set of integers {0, 1, 2, ..., *m* − 1} is called the **least residue system modulo *m***. Any set of *m* integers, no two of which are congruent modulo *m*, is called a **complete residue system modulo *m***.

The least residue system is a complete residue system, and a complete residue system is simply a set containing precisely one [representative](/wiki/Representative_(mathematics)) of each residue class modulo *m*.[[5]](#cite_note-FOOTNOTELong197278-5) For example, the least residue system modulo 4 is {0, 1, 2, 3}. Some other complete residue systems modulo 4 include:


- {1, 2, 3, 4}
- {13, 14, 15, 16}
- {−2, −1, 0, 1}
- {−13, 4, 17, 18}
- {−5, 0, 6, 21}
- {27, 32, 37, 42}


Some sets that are *not* complete residue systems modulo 4 are:


- {−5, 0, 6, 22}, since 6 is congruent to 22 modulo 4.
- {5, 15}, since a complete residue system modulo 4 must have exactly 4 incongruent residue classes.



### Reduced residue systems



Given the [Euler's totient function](/wiki/Euler%27s_totient_function) *φ*(*m*), any set of *φ*(*m*) integers that are [relatively prime](/wiki/Coprime_integers) to *m* and mutually incongruent under modulus *m* is called a **reduced residue system modulo *m***.[[6]](#cite_note-FOOTNOTELong197285-6) The set {5, 15} from above, for example, is an instance of a reduced residue system modulo 4.



### Covering systems



Covering systems represent yet another type of residue system that may contain residues with varying moduli.



## Integers modulo *m*


In the context of this paragraph, the modulus *m* is almost always taken as positive.

The set of all [congruence classes](#Congruence_classes) modulo *m* is a [ring](/wiki/Ring_(mathematics)) called the **ring of integers modulo *m***, and is denoted ${\textstyle \mathbb {Z} /m\mathbb {Z} }$, ${\displaystyle \mathbb {Z} /(m)}$, ${\displaystyle \mathbb {Z} /m}$, or ${\displaystyle \mathbb {Z} _{m}}$.[[7]](#cite_note-FOOTNOTEDenton2013-7) The ring ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$ is fundamental to various branches of mathematics (see *[§ Applications](#Applications)* below).
(In some parts of [number theory](/wiki/Number_theory) the notation ${\displaystyle \mathbb {Z} _{m}}$ is avoided because it can be confused with the set of [*m*-adic integers](/wiki/P-adic_integer).)

For *m* > 0 one has


${\displaystyle \mathbb {Z} /m\mathbb {Z} =\left\{{\overline {a}}_{m}\mid a\in \mathbb {Z} \right\}=\left\{{\overline {0}}_{m},{\overline {1}}_{m},{\overline {2}}_{m},\ldots ,{\overline {m{-}1}}_{m}\right\}.}$
When *m* = 1, ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$ is the [zero ring](/wiki/Zero_ring); when *m* = 0, ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$ is not an [empty set](/wiki/Empty_set); rather, it is [isomorphic](/wiki/Isomorphism) to ${\displaystyle \mathbb {Z} }$, since *a*0 = {*a*}.

Addition, subtraction, and multiplication are defined on ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$ by the following rules:


- ${\displaystyle {\overline {a}}_{m}+{\overline {b}}_{m}={\overline {(a+b)}}_{m}}$
- ${\displaystyle {\overline {a}}_{m}-{\overline {b}}_{m}={\overline {(a-b)}}_{m}}$
- ${\displaystyle {\overline {a}}_{m}{\overline {b}}_{m}={\overline {(ab)}}_{m}.}$


The properties given before imply that, with these operations, ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$ is a [commutative ring](/wiki/Commutative_ring). For example, in the ring ${\displaystyle \mathbb {Z} /24\mathbb {Z} }$, one has


${\displaystyle {\overline {12}}_{24}+{\overline {21}}_{24}={\overline {33}}_{24}={\overline {9}}_{24}}$
as in the arithmetic for the 24-hour clock.

The notation ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$ is used because this ring is the [quotient ring](/wiki/Quotient_ring) of ${\displaystyle \mathbb {Z} }$ by the [ideal](/wiki/Ideal_(ring_theory)) ${\displaystyle m\mathbb {Z} }$, the set formed by all multiples of *m*, that is, all numbers *k m* with ${\displaystyle k\in \mathbb {Z} .}$

Under addition, ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$ is a [cyclic group](/wiki/Cyclic_group).  All finite cyclic groups are isomorphic with ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$ for some m.[[8]](#cite_note-8)

The ring of integers modulo *m* is a [field](/wiki/Field_(mathematics)); that is, every nonzero element has a [multiplicative inverse](/wiki/Modular_multiplicative_inverse), if and only if *m* is [prime](/wiki/Prime_number). If *m* = *p**k* is a [prime power](/wiki/Prime_power) with *k* > 1, there exists a unique (up to isomorphism) finite field ${\displaystyle \mathrm {GF} (m)=\mathbb {F} _{m}}$ with *m* elements, which is *not* isomorphic to ${\displaystyle \mathbb {Z} /m\mathbb {Z} }$, which fails to be a field because it has [zero-divisors](/wiki/Zero-divisor).

If *m* > 1, ${\displaystyle (\mathbb {Z} /m\mathbb {Z} )^{\times }}$ denotes the [multiplicative group of the integers modulo *m*](/wiki/Multiplicative_group_of_integers_modulo_n) that are invertible. It consists of the congruence classes *a**m*, where *a* [is coprime](/wiki/Coprime_integers) to *m*; these are precisely the classes possessing a multiplicative inverse. They form an [abelian group](/wiki/Abelian_group) under multiplication; its order is *φ*(*m*), where φ is [Euler's totient function](/wiki/Euler%27s_totient_function).



## Applications


In pure mathematics, modular arithmetic is one of the foundations of [number theory](/wiki/Number_theory), touching on almost every aspect of its study, and it is also used extensively in [group theory](/wiki/Group_theory), [ring theory](/wiki/Ring_theory), [knot theory](/wiki/Knot_theory), and [abstract algebra](/wiki/Abstract_algebra). In applied mathematics, it is used in [computer algebra](/wiki/Computer_algebra), [cryptography](/wiki/Cryptography), [computer science](/wiki/Computer_science), [chemistry](/wiki/Chemistry) and the [visual](/wiki/Visual_arts) and [musical](/wiki/Music) arts.

A very practical application is to calculate checksums within serial number identifiers. For example, [International Standard Book Number](/wiki/International_Standard_Book_Number) (ISBN) uses modulo 11 (for 10-digit ISBN) or modulo 10 (for 13-digit ISBN) arithmetic for error detection. Likewise, [International Bank Account Numbers](/wiki/International_Bank_Account_Number) (IBANs) use modulo 97 arithmetic to spot user input errors in bank account numbers. In chemistry, the last digit of the [CAS registry number](/wiki/CAS_registry_number) (a unique identifying number for each chemical compound) is a [check digit](/wiki/Check_digit), which is calculated by taking the last digit of the first two parts of the CAS registry number times 1, the previous digit times 2, the previous digit times 3 etc., adding all these up and computing the sum modulo 10.

In cryptography, modular arithmetic directly underpins [public key](/wiki/Public-key_cryptography) systems such as [RSA](/wiki/RSA_(algorithm)) and [Diffie–Hellman](/wiki/Diffie%E2%80%93Hellman_key_exchange), and provides [finite fields](/wiki/Finite_field) which underlie [elliptic curves](/wiki/Elliptic_curve), and is used in a variety of [symmetric key algorithms](/wiki/Symmetric_key_algorithm) including [Advanced Encryption Standard](/wiki/Advanced_Encryption_Standard) (AES), [International Data Encryption Algorithm](/wiki/International_Data_Encryption_Algorithm) (IDEA), and [RC4](/wiki/RC4). RSA and Diffie–Hellman use [modular exponentiation](/wiki/Modular_exponentiation).

In computer algebra, modular arithmetic is commonly used to limit the size of integer coefficients in intermediate calculations and data. It is used in [polynomial factorization](/wiki/Polynomial_factorization), a problem for which all known efficient algorithms use modular arithmetic. It is used by the most efficient implementations of [polynomial greatest common divisor](/wiki/Polynomial_greatest_common_divisor), exact [linear algebra](/wiki/Linear_algebra) and [Gröbner basis](/wiki/Gr%C3%B6bner_basis) algorithms over the integers and the rational numbers. As posted on [Fidonet](/wiki/Fidonet) in the 1980s and archived at [Rosetta Code](/wiki/Rosetta_Code), modular arithmetic was used to disprove [Euler's sum of powers conjecture](/wiki/Euler%27s_sum_of_powers_conjecture) on a [Sinclair QL](/wiki/Sinclair_QL) [microcomputer](/wiki/Microcomputer) using just one-fourth of the integer precision used by a [CDC 6600](/wiki/CDC_6600) [supercomputer](/wiki/Supercomputer) to disprove it two decades earlier via a [brute force search](/wiki/Brute_force_search).[[9]](#cite_note-9)

In computer science, modular arithmetic is often applied in [bitwise operations](/wiki/Bitwise_operation) and other operations involving fixed-width, cyclic [data structures](/wiki/Data_structure). The modulo operation, as implemented in many [programming languages](/wiki/Programming_language) and [calculators](/wiki/Calculator), is an application of modular arithmetic that is often used in this context. The logical operator [XOR](/wiki/XOR) sums 2 bits, modulo 2.

The use of [long division](/wiki/Long_division) to turn a fraction into a [repeating decimal](/wiki/Repeating_decimal) in any base *b* is equivalent to modular multiplication of *b* modulo the denominator. For example, for decimal, *b* = 10.

In music, arithmetic modulo 12 is used in the consideration of the system of [twelve-tone equal temperament](/wiki/Twelve-tone_equal_temperament), where [octave](/wiki/Octave) and [enharmonic](/wiki/Enharmonic) equivalency occurs (that is, pitches in a 1:2 or 2:1 ratio are equivalent, and C-[sharp](/wiki/Sharp_(music)) is considered the same as D-[flat](/wiki/Flat_(music))).

The method of [casting out nines](/wiki/Casting_out_nines) offers a quick check of decimal arithmetic computations performed by hand. It is based on modular arithmetic modulo 9, and specifically on the crucial property that 10 ≡ 1 (mod 9).

Arithmetic modulo 7 is used in algorithms that determine the day of the week for a given date. In particular, [Zeller's congruence](/wiki/Zeller%27s_congruence) and the [Doomsday algorithm](/wiki/Doomsday_algorithm) make heavy use of modulo-7 arithmetic.

More generally, modular arithmetic also has application in disciplines such as [politics](/wiki/Politics) (for example, [apportionment](/wiki/Apportionment_(politics))), [economics](/wiki/Economics) (for example, [game theory](/wiki/Game_theory)) and other areas of the [social sciences](/wiki/Social_science), where [proportional](/wiki/Proportional_(fair_division)) division and allocation of resources plays a central part of the analysis.



## Computational complexity


Since modular arithmetic has such a wide range of applications, it is important to know how hard it is to solve a system of congruences. A linear system of congruences can be solved in [polynomial time](/wiki/Polynomial_time) with a form of [Gaussian elimination](/wiki/Gaussian_elimination), for details see [linear congruence theorem](/wiki/Linear_congruence_theorem). Algorithms, such as [Montgomery reduction](/wiki/Montgomery_reduction), also exist to allow simple arithmetic operations, such as multiplication and [exponentiation modulo *m*](/wiki/Modular_exponentiation), to be performed efficiently on large numbers.

Some operations, like finding a [discrete logarithm](/wiki/Discrete_logarithm) or a [quadratic congruence](/wiki/Quadratic_congruences) appear to be as hard as [integer factorization](/wiki/Integer_factorization) and thus are a starting point for [cryptographic algorithms](/wiki/Cryptography) and [encryption](/wiki/Encryption). These problems might be [NP-intermediate](/wiki/NP-intermediate).

Solving a system of non-linear modular arithmetic equations is [NP-complete](/wiki/NP-complete).[[10]](#cite_note-FOOTNOTEGareyJohnson1979-10)



## See also



- [Boolean ring](/wiki/Boolean_ring)
- [Circular buffer](/wiki/Circular_buffer)
- [Division (mathematics)](/wiki/Division_(mathematics))
- [Finite field](/wiki/Finite_field)
- [Legendre symbol](/wiki/Legendre_symbol)
- [Modular exponentiation](/wiki/Modular_exponentiation)
- [Modulo (mathematics)](/wiki/Modulo_(mathematics))
- [Multiplicative group of integers modulo n](/wiki/Multiplicative_group_of_integers_modulo_n)
- [Pisano period](/wiki/Pisano_period) (Fibonacci sequences modulo *n*)
- [Primitive root modulo n](/wiki/Primitive_root_modulo_n)
- [Quadratic reciprocity](/wiki/Quadratic_reciprocity)
- [Quadratic residue](/wiki/Quadratic_residue)
- [Rational reconstruction (mathematics)](/wiki/Rational_reconstruction_(mathematics))
- [Reduced residue system](/wiki/Reduced_residue_system)
- [Serial number arithmetic](/wiki/Serial_number_arithmetic) (a special case of modular arithmetic)
- [Two-element Boolean algebra](/wiki/Two-element_Boolean_algebra)
- Topics relating to the group theory behind modular arithmetic:
- [Cyclic group](/wiki/Cyclic_group)
- [Multiplicative group of integers modulo n](/wiki/Multiplicative_group_of_integers_modulo_n)
- Other important theorems relating to modular arithmetic:
- [Carmichael's theorem](/wiki/Carmichael_function)
- [Chinese remainder theorem](/wiki/Chinese_remainder_theorem)
- [Euler's theorem](/wiki/Euler%27s_theorem)
- [Fermat's little theorem](/wiki/Fermat%27s_little_theorem) (a special case of Euler's theorem)
- [Lagrange's theorem](/wiki/Lagrange%27s_theorem_(group_theory))
- [Thue's lemma](/wiki/Thue%27s_lemma)




## Notes


1. **[^](#cite_ref-1)** [Gray, Jeremy](/wiki/Jeremy_Gray_(mathematician)). *A History of Abstract Algebra: From Algebraic Equations to Modern Algebra*. Germany, Springer International Publishing, 2018. 143.
2. **[^](#cite_ref-FOOTNOTELehoczkyRusczky2006_2-0)** [Lehoczky & Rusczky 2006](#CITEREFLehoczkyRusczky2006).
3. **[^](#cite_ref-FOOTNOTEWeisstein_3-0)** [Weisstein](#CITEREFWeisstein).
4. **[^](#cite_ref-FOOTNOTEPettofrezzoByrkit197090_4-0)** [Pettofrezzo & Byrkit 1970](#CITEREFPettofrezzoByrkit1970), p. 90.
5. **[^](#cite_ref-FOOTNOTELong197278_5-0)** [Long 1972](#CITEREFLong1972), p. 78.
6. **[^](#cite_ref-FOOTNOTELong197285_6-0)** [Long 1972](#CITEREFLong1972), p. 85.
7. **[^](#cite_ref-FOOTNOTEDenton2013_7-0)** [Denton 2013](#CITEREFDenton2013).
8. **[^](#cite_ref-8)** Sengadir T., *[Discrete Mathematics and Combinatorics](https://books.google.com/books?id=nglisrt9IewC&pg=PA293&dq=%22Zn+is+generated+by+1%22)*, p. 293, at [Google Books](/wiki/Google_Books)
9. **[^](#cite_ref-9)** ["Euler's sum of powers conjecture"](https://rosettacode.org/wiki/Euler%27s_sum_of_powers_conjecture#QL_SuperBASIC). *rosettacode.org*. [Archived](https://web.archive.org/web/20230326025754/https://rosettacode.org/wiki/Euler%27s_sum_of_powers_conjecture#QL_SuperBASIC) from the original on 26 March 2023. Retrieved 11 November 2020.
10. **[^](#cite_ref-FOOTNOTEGareyJohnson1979_10-0)** [Garey & Johnson 1979](#CITEREFGareyJohnson1979).



## References



- [Apostol, Tom M.](/wiki/Tom_M._Apostol) (1976), *Introduction to analytic number theory*, Undergraduate Texts in Mathematics, New York-Heidelberg: Springer-Verlag, [ISBN](/wiki/ISBN_(identifier)) [978-0-387-90163-3](/wiki/Special:BookSources/978-0-387-90163-3), [MR](/wiki/MR_(identifier)) [0434929](https://mathscinet.ams.org/mathscinet-getitem?mr=0434929), [Zbl](/wiki/Zbl_(identifier)) [0335.10001](https://zbmath.org/?format=complete&q=an:0335.10001). See in particular chapters 5 and 6 for a review of basic modular arithmetic.


- Berggren, John L. ["Modular arithmetic"](https://www.britannica.com/EBchecked/topic/920687/modular-arithmetic). *[Encyclopædia Britannica](/wiki/Encyclop%C3%A6dia_Britannica)*.


- Bullynck, Maarten. ["Modular Arithmetic before C. F. Gauss: Systematisations and discussions on remainder problems in 18th-century Germany"](https://web.archive.org/web/20131102014013/http://www.kuttaka.org/Gauss_Modular.pdf) (PDF). Archived from [the original](http://www.kuttaka.org/Gauss_Modular.pdf) (PDF) on 2 November 2013. Retrieved 3 February 2018.


- [Cormen, Thomas H.](/wiki/Thomas_H._Cormen); [Leiserson, Charles E.](/wiki/Charles_E._Leiserson); [Rivest, Ronald L.](/wiki/Ronald_L._Rivest); [Stein, Clifford](/wiki/Clifford_Stein) (2001). "31.3: Modular arithmetic". *[Introduction to Algorithms](/wiki/Introduction_to_Algorithms)* (2nd ed.). MIT Press and McGraw-Hill. pp. 862–868. [ISBN](/wiki/ISBN_(identifier)) [0-262-03293-7](/wiki/Special:BookSources/0-262-03293-7).


- Denton, Tom (16 November 2013). ["2.3: Integers Modulo n"](https://math.libretexts.org/Bookshelves/Abstract_and_Geometric_Algebra/Book%3A_Introduction_to_Algebraic_Structures_(Denton)/02%3A_Groups_I/2.03%3A_Integers_Modulo_n). *Mathematics LibreTexts*. [Archived](https://web.archive.org/web/20210419035455/https://math.libretexts.org/Bookshelves/Abstract_and_Geometric_Algebra/Book%3A_Introduction_to_Algebraic_Structures_(Denton)/02%3A_Groups_I/2.03%3A_Integers_Modulo_n) from the original on 19 April 2021. Retrieved 12 August 2020.


- Garey, M. R.; Johnson, D. S. (1979). [*Computers and Intractability, a Guide to the Theory of NP-Completeness*](https://archive.org/details/computersintract0000gare). W. H. Freeman. [ISBN](/wiki/ISBN_(identifier)) [0716710447](/wiki/Special:BookSources/0716710447).


- Gioia, Anthony (2001). [*Number Theory: An Introduction*](http://genealogy.math.ndsu.nodak.edu/id.php?id=3545) (Reprint ed.). Dover. [ISBN](/wiki/ISBN_(identifier)) [0-486-41449-3](/wiki/Special:BookSources/0-486-41449-3).


- Lehoczky, Sandor; [Rusczky, Richard](/wiki/Richard_Rusczyk) (2006). Patrick, David (ed.). *The Art of Problem Solving*. Vol. 1 (7 ed.). AoPS Incorporated. p. 44. [ISBN](/wiki/ISBN_(identifier)) [0977304566](/wiki/Special:BookSources/0977304566).


- Long, Calvin T. (1972). *Elementary Introduction to Number Theory* (2nd ed.). Lexington: [D. C. Heath and Company](/wiki/D._C._Heath_and_Company). [LCCN](/wiki/LCCN_(identifier)) [77171950](https://lccn.loc.gov/77171950).


- Pettofrezzo, Anthony J.; Byrkit, Donald R. (1970). [*Elements of Number Theory*](https://archive.org/details/elementsofnumber0000pett). Englewood Cliffs: [Prentice Hall](/wiki/Prentice_Hall). [ISBN](/wiki/ISBN_(identifier)) [9780132683005](/wiki/Special:BookSources/9780132683005). [LCCN](/wiki/LCCN_(identifier)) [71081766](https://lccn.loc.gov/71081766).


- Sengadir, T. (2009). *Discrete Mathematics and Combinatorics*. Chennai, India: Pearson Education India. [ISBN](/wiki/ISBN_(identifier)) [978-81-317-1405-8](/wiki/Special:BookSources/978-81-317-1405-8). [OCLC](/wiki/OCLC_(identifier)) [778356123](https://search.worldcat.org/oclc/778356123).


- Weisstein, Eric W. ["Modular Arithmetic"](https://mathworld.wolfram.com/ModularArithmetic.html). *Wolfram MathWorld*. [Archived](https://web.archive.org/web/20230714132828/https://mathworld.wolfram.com/ModularArithmetic.html) from the original on 14 July 2023. Retrieved 12 August 2020.




## External links


- ["Congruence"](https://www.encyclopediaofmath.org/index.php?title=Congruence), *[Encyclopedia of Mathematics](/wiki/Encyclopedia_of_Mathematics)*, [EMS Press](/wiki/European_Mathematical_Society), 2001 [1994]
- In this [modular art](https://web.archive.org/web/20060101075602/http://britton.disted.camosun.bc.ca/modart/jbmodart.htm) article, one can learn more about applications of modular arithmetic in art.
- An [article](https://web.archive.org/web/20160220061222/http://mersennewiki.org/index.php/Modular_arithmetic) on modular arithmetic on the GIMPS wiki
- [Modular Arithmetic and patterns in addition and multiplication tables](http://www.cut-the-knot.org/blue/Modulo.shtml)


- [v](/wiki/Template:Number_theory)
- [t](/wiki/Template_talk:Number_theory)
- [e](/wiki/Special:EditPage/Template:Number_theory)

[Number theory](/wiki/Number_theory)Fields
- [Algebraic number theory](/wiki/Algebraic_number_theory) ([class field theory](/wiki/Class_field_theory), [non-abelian class field theory](/wiki/Non-abelian_class_field_theory), [Iwasawa theory](/wiki/Iwasawa_theory), [Tate's thesis](/wiki/Tate%27s_thesis), [Kummer theory](/wiki/Kummer_theory))
- [Analytic number theory](/wiki/Analytic_number_theory) ([analytic theory of L-functions](/wiki/L-function), [probabilistic number theory](/wiki/Probabilistic_number_theory), [sieve theory](/wiki/Sieve_theory))
- [Geometric number theory](/wiki/Geometry_of_numbers)
- [Computational number theory](/wiki/Computational_number_theory)
- [Transcendental number theory](/wiki/Transcendental_number_theory)
- [Diophantine geometry](/wiki/Diophantine_geometry) ([Arakelov theory](/wiki/Arakelov_theory), [Hodge–Arakelov theory](/wiki/Hodge%E2%80%93Arakelov_theory))
- [Arithmetic combinatorics](/wiki/Arithmetic_combinatorics) ([additive number theory](/wiki/Additive_number_theory))
- [Arithmetic geometry](/wiki/Arithmetic_geometry) ([anabelian geometry](/wiki/Anabelian_geometry), [p-adic Hodge theory](/wiki/P-adic_Hodge_theory))
- [Arithmetic topology](/wiki/Arithmetic_topology)
- [Arithmetic dynamics](/wiki/Arithmetic_dynamics)


Key concepts
- [Numbers](/wiki/Number)
- [Zero](/wiki/0)
- [Natural numbers](/wiki/Natural_number)
- [Unity](/wiki/1)
- [Prime numbers](/wiki/Prime_number)
- [Composite numbers](/wiki/Composite_number)
- [Rational numbers](/wiki/Rational_number)
- [Irrational numbers](/wiki/Irrational_number)
- [Algebraic numbers](/wiki/Algebraic_number)
- [Transcendental numbers](/wiki/Transcendental_number)
- [p-adic numbers](/wiki/P-adic_number) ([p-adic analysis](/wiki/P-adic_analysis))
- [Arithmetic](/wiki/Arithmetic)
- Modular arithmetic
- [Chinese remainder theorem](/wiki/Chinese_remainder_theorem)
- [Arithmetic functions](/wiki/Arithmetic_function)


Advanced concepts
- [Quadratic forms](/wiki/Quadratic_form)
- [Modular forms](/wiki/Modular_form)
- [L-functions](/wiki/L-function)
- [Diophantine equations](/wiki/Diophantine_equation)
- [Diophantine approximation](/wiki/Diophantine_approximation)
- [Irrationality measure](/wiki/Irrationality_measure)
- [Simple continued fractions](/wiki/Simple_continued_fraction)



- ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png)

---

 [Category](/wiki/Category:Number_theory)
- ![](https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Symbol_list_class.svg/20px-Symbol_list_class.svg.png)

---

 [List of topics](/wiki/List_of_number_theory_topics)
- ![](https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Symbol_list_class.svg/20px-Symbol_list_class.svg.png)

---

 [List of recreational topics](/wiki/List_of_recreational_number_theory_topics)
- [![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Wikibooks-logo.svg/20px-Wikibooks-logo.svg.png)

---](/wiki/File:Wikibooks-logo.svg) [Wikibook](https://en.wikibooks.org/wiki/Number_Theory)
- [![](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/20px-Wikiversity_logo_2017.svg.png)

---](/wiki/File:Wikiversity_logo_2017.svg) [Wikiversity](https://en.wikiversity.org/wiki/Number_Theory)



 
NewPP limit report
Parsed by mw‐api‐int.eqiad.main‐6f7dd49c68‐4q4rm
Cached time: 20260502212546
Cache expiry: 2592000
Cache expiry source: Module:Citation/CS1 (os.date(%Y))
Reduced expiry: false
Complications: [vary‐revision‐sha1, prevent‐selective‐update, show‐toc]
CPU time usage: 1.093 seconds
Real time usage: 1.461 seconds
Preprocessor visited node count: 13303/1000000
Revision size: 32118/2097152 bytes
Post‐expand include size: 102179/2097152 bytes
Template argument size: 21189/2097152 bytes
Highest expansion depth: 12/100
Expensive parser function count: 6/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 51314/5000000 bytes
Lua time usage: 0.573/10.000 seconds
Lua memory usage: 9421005/52428800 bytes
Number of Wikibase entities loaded: 0/500


Transclusion expansion time report (%,ms,calls,template)
100.00% 1162.298      1 -total
 29.80%  346.370    242 Template:Math
 13.77%  160.093      1 Template:Reflist
 12.38%  143.850      4 Template:Cite_web
  9.87%  114.674      1 Template:Short_description
  9.48%  110.214      1 Template:Number_theory
  9.23%  107.275      1 Template:Navbox
  7.47%   86.774      1 Template:More_citations_needed
  7.24%   84.120    255 Template:Main_other
  6.73%   78.225      1 Template:Ambox

 Render ID 7b58f856-466d-11f1-8940-07f8e6474150 
 Saved in parser cache with key enwiki:pcache:20087:|#|:idhash:canonical and timestamp 20260502212546 and revision id 1352218723. Rendering was triggered because: api-parse
 
![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

---


Retrieved from "[https://en.wikipedia.org/w/index.php?title=Modular_arithmetic&oldid=1352218723](https://en.wikipedia.org/w/index.php?title=Modular_arithmetic&oldid=1352218723)"
