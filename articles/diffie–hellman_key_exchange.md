[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/DiffieHellman.png/500px-DiffieHellman.png)](//en.wikipedia.org/wiki/File:DiffieHellman.png)With Diffie–Hellman key exchange, two parties arrive at a common secret key, without passing the common secret key across the public channel.

---


**Diffie–Hellman** (**DH**) **key exchange**[[nb 1]](#cite_note-1) is a mathematical method of securely generating a symmetric [cryptographic key](//en.wikipedia.org/wiki/Cryptographic_key) over a public channel and was one of the first [protocols](//en.wikipedia.org/wiki/Public-key_cryptography) as conceived by [Ralph Merkle](//en.wikipedia.org/wiki/Ralph_Merkle) and named after [Whitfield Diffie](//en.wikipedia.org/wiki/Whitfield_Diffie) and [Martin Hellman](//en.wikipedia.org/wiki/Martin_Hellman).[[1]](#cite_note-Merkle_1978-2) DH is one of the earliest practical examples of public key exchange implemented within the field of cryptography. Published in 1976 by Diffie and Hellman, this is the earliest publicly known work that proposed the idea of a private key and a corresponding public key.

Traditionally, secure encrypted communication between two parties required that they first exchange keys by some secure physical means, such as paper key lists transported by a trusted [courier](//en.wikipedia.org/wiki/Courier). The Diffie–Hellman key exchange method allows two parties that have no prior knowledge of each other to jointly establish a [shared secret](//en.wikipedia.org/wiki/Shared_secret) key over an [insecure channel](//en.wikipedia.org/wiki/Insecure_channel). This key can then be used to encrypt subsequent communications using a [symmetric-key](//en.wikipedia.org/wiki/Symmetric-key_algorithm) [cipher](//en.wikipedia.org/wiki/Cipher).

Diffie–Hellman is used to secure a variety of [Internet](//en.wikipedia.org/wiki/Internet) services. However, research published in October 2015 suggests that the parameters in use for many DH Internet applications at that time were not strong enough to prevent compromise by very well-funded attackers, such as the security services of some countries.[[2]](#cite_note-imperfectfs-3)

The scheme was published by Whitfield Diffie and Martin Hellman in 1976,[[3]](#cite_note-Diffie_1976-4) but in 1997 it was revealed that [James H. Ellis](//en.wikipedia.org/wiki/James_H._Ellis),[[4]](#cite_note-5) [Clifford Cocks](//en.wikipedia.org/wiki/Clifford_Cocks), and [Malcolm J. Williamson](//en.wikipedia.org/wiki/Malcolm_J._Williamson) of [GCHQ](//en.wikipedia.org/wiki/Government_Communications_Headquarters), the British signals intelligence agency, had previously shown in 1969[[5]](#cite_note-6) how public-key cryptography could be achieved.[[6]](#cite_note-7)

Although Diffie–Hellman key exchange itself is a non-authenticated [key-agreement protocol](//en.wikipedia.org/wiki/Key-agreement_protocol), it provides the basis for a variety of authenticated protocols, and is used to provide [forward secrecy](//en.wikipedia.org/wiki/Forward_secrecy) in [Transport Layer Security](//en.wikipedia.org/wiki/Transport_Layer_Security)'s [ephemeral](//en.wikipedia.org/wiki/Ephemeral_key) modes (referred to as EDH or DHE depending on the cipher suite).  Forward secrecy results from the use of ephemeral keys: the private keys are discarded once key agreement is complete, making them safe from later compromise.   Ephemeral keys are practical because it is computationally cheap to create public-private key pairs suitable for use with Diffie-Hellman exchange.

The method was followed shortly after by the [RSA cryptosystem](//en.wikipedia.org/wiki/RSA_cryptosystem), an implementation of public-key cryptography using asymmetric algorithms.

Expired US patent 4200770[[7]](#cite_note-8) from 1977 describes the now public-domain algorithm. It credits Hellman, Diffie, and Merkle as inventors.




## Name


In 2006, Hellman suggested the algorithm be called **Diffie–Hellman–Merkle key exchange** in recognition of [Ralph Merkle](//en.wikipedia.org/wiki/Ralph_Merkle)'s contribution to the invention of [public-key cryptography](//en.wikipedia.org/wiki/Public-key_cryptography) (Hellman, 2006), writing:


The system ... has since become known as Diffie–Hellman key exchange. While that system was first described in a paper by Diffie and me, it is a public key distribution system, a concept developed by Merkle, and hence should be called 'Diffie–Hellman–Merkle key exchange' if names are to be associated with it. I hope this small pulpit might help in that endeavor to recognize Merkle's equal contribution to the invention of public key cryptography.[[8]](#cite_note-Hellman2002-9)



## Description



### General overview



[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Diffie-Hellman_Key_Exchange.svg/250px-Diffie-Hellman_Key_Exchange.svg.png)](//en.wikipedia.org/wiki/File:Diffie-Hellman_Key_Exchange.svg)Illustration of the concept behind Diffie–Hellman key exchange

---


Diffie–Hellman key exchange establishes a shared secret between two parties that can be used for secret communication for exchanging data over a public network. An analogy illustrates the concept of public key exchange by using colors instead of very large numbers:

The process begins by having the two parties, [Alice and Bob](//en.wikipedia.org/wiki/Alice_and_Bob), publicly agree on an arbitrary starting color that does not need to be kept secret. In this example, the color is yellow. Each person also selects a secret color that they keep to themselves – in this case, red and cyan. The crucial part of the process is that Alice and Bob each mix their own secret color together with their mutually shared color, resulting in orange-tan and light-blue mixtures respectively, and then publicly exchange the two mixed colors. Finally, each of them mixes the color they received from the partner with their own private color. The result is a final color mixture (yellow-brown in this case) that is identical to their partner's final color mixture.

If a third party listened to the exchange, they would only know the common color (yellow) and the first mixed colors (orange-tan and light-blue), but it would be very hard for them to find out the final secret color (yellow-brown). Bringing the analogy back to a [real-life](//en.wikipedia.org/wiki/Real-life) exchange using large numbers rather than colors, this determination is computationally expensive; it is impossible to compute in a practical amount of time even for modern [supercomputers](//en.wikipedia.org/wiki/Supercomputer).



### Cryptographic explanation


The simplest and the original implementation,[[3]](#cite_note-Diffie_1976-4) later formalized as **Finite Field Diffie–Hellman** in RFC 7919,[[9]](#cite_note-10) of the protocol uses the [multiplicative group of integers modulo](//en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n) *p*, where *p* is [prime](//en.wikipedia.org/wiki/Prime_number), and *g* is a [primitive root modulo](//en.wikipedia.org/wiki/Primitive_root_modulo_n) *p*. To guard against potential vulnerabilities, it is recommended to use prime numbers of at least 2048 bits in length. This increases the difficulty for an adversary attempting to compute the discrete logarithm and compromise the shared secret. These two values are chosen in this way to ensure that the resulting shared secret can take on any value from 1 to *p* − 1. Here is an example of the protocol, with non-secret values in blue, and secret values in **red**.


1. [Alice and Bob](//en.wikipedia.org/wiki/Alice_and_Bob) publicly agree to use a modulus *p* = 23 and base *g* = 5 (which is a primitive root modulo 23).
2. Alice chooses a secret integer ***a*** = 4, then sends Bob *A* = *g**a*** mod *p*
- *A* = 5**4** mod 23 = 4 (in this example both *A* and ***a*** have the same value 4, but this is usually not the case)
3. Bob chooses a secret integer ***b*** = 3, then sends Alice *B* = *g**b*** mod *p*
- *B* = 5**3** mod 23 = 10
4. Alice computes ***s*** = *B**a*** mod *p*
- ***s*** = 10**4** mod 23 = **18**
5. Bob computes ***s*** = *A**b*** mod *p*
- ***s*** = 4**3** mod 23 = **18**
6. Alice and Bob now share a secret (the number 18).


Both Alice and Bob have arrived at the same values because under mod *p*,


${\displaystyle {\color {Blue}A}^{\color {Red}{\boldsymbol {b}}}{\bmod {\color {Blue}p}}={\color {Blue}g}^{\color {Red}{\boldsymbol {ab}}}{\bmod {\color {Blue}p}}={\color {Blue}g}^{\color {Red}{\boldsymbol {ba}}}{\bmod {\color {Blue}p}}={\color {Blue}B}^{\color {Red}{\boldsymbol {a}}}{\bmod {\color {Blue}p}}}$
More specifically,


${\displaystyle ({\color {Blue}g}^{\color {Red}{\boldsymbol {a}}}{\bmod {\color {Blue}p}})^{\color {Red}{\boldsymbol {b}}}{\bmod {\color {Blue}p}}=({\color {Blue}g}^{\color {Red}{\boldsymbol {b}}}{\bmod {\color {Blue}p}})^{\color {Red}{\boldsymbol {a}}}{\bmod {\color {Blue}p}}}$
Only *a* and *b* are kept secret. All the other values – *p*, *g*, *ga* mod *p*, and *gb* mod *p* – are sent in the clear. The strength of the scheme comes from the fact that *gab* mod *p* = *gba* mod *p* take extremely long times to compute by any known classical algorithm just from the knowledge of *p*, *g*, *ga* mod *p*, and *gb* mod *p*. Such a function that is easy to compute but hard to invert is called a [one-way function](//en.wikipedia.org/wiki/One-way_function). Once Alice and Bob compute the shared secret they can use it as an encryption key, known only to them, for sending messages across the same open communications channel.

Of course, much larger values of *a*, *b*, and *p* would be needed to make this example secure, since there are only 23 possible results of *n* mod 23. However, if *p* is a prime of at least 600 digits, then even the fastest modern computers using the fastest known algorithm cannot find *a* given only *g*, *p* and *ga* mod *p*.[*[citation needed](//en.wikipedia.org/wiki/Wikipedia:Citation_needed)*] Such a problem is called the [discrete logarithm problem](//en.wikipedia.org/wiki/Discrete_logarithm_problem).[[2]](#cite_note-imperfectfs-3) The computation of *ga* mod *p* is known as [modular exponentiation](//en.wikipedia.org/wiki/Modular_exponentiation) and can be done efficiently even for large numbers.
Note that *g* need not be large at all, and in practice is usually a small integer (like 2, 3, ...).



### Secrecy chart


The chart below depicts who knows what, again with non-secret values in blue, and secret values in **red**. Here [Eve](//en.wikipedia.org/wiki/Alice_and_Bob#Cast_of_characters) is an [eavesdropper](//en.wikipedia.org/wiki/Eavesdropping#Network_attacks) – she watches what is sent between Alice and Bob, but she does not alter the contents of their communications.


- *g*, public (primitive root) base, known to Alice, Bob, and Eve. *g* = 5
- *p*, public (prime) modulus, known to Alice, Bob, and Eve. *p* = 23
- ***a***, Alice's private key, known only to Alice. ***a*** = **6**
- ***b***, Bob's private key known only to Bob. ***b*** = **15**
- *A*, Alice's public key, known to Alice, Bob, and Eve. *A* = *g**a*** mod *p* = 8
- *B*, Bob's public key, known to Alice, Bob, and Eve. *B* = *g**b*** mod *p* = 19






Alice


Known

Unknown


*p* = 23




*g* = 5




***a*** = **6**

***b***


*A* = 5***a*** mod 23




*A* = 5**6** mod 23 = 8




*B* = 19




***s*** = B***a*** mod 23




***s*** = 19**6** mod 23 = **2**






Bob


Known

Unknown


*p* = 23




*g* = 5




***b*** = **15**

***a***


*B* = 5***b*** mod 23




*B* = 5**15** mod 23 = 19




*A* = 8




***s*** = A***b*** mod 23




***s*** = 8**15** mod 23 = **2**






Eve


Known

Unknown


*p* = 23




*g* = 5






***a***, ***b***


 

 


 

 


*A* = 8, *B* = 19




 

 




***s***


Now ***s*** is the shared secret key and it is known to both Alice and Bob, but *not* to Eve. Note that it is not helpful for Eve to compute *AB*, which equals *g****a***+***b*** mod p.

Note: It should be difficult for Alice to solve for Bob's private key or for Bob to solve for Alice's private key. If it is not difficult for Alice to solve for Bob's private key (or vice versa), then an eavesdropper, [Eve](//en.wikipedia.org/wiki/Alice_and_Bob#Cast_of_characters), may simply substitute her own private / public key pair, plug Bob's public key into her private key, produce a fake shared secret key, and solve for Bob's private key (and use that to solve for the shared secret key). [Eve](//en.wikipedia.org/wiki/Alice_and_Bob#Cast_of_characters) may attempt to choose a public / private key pair that will make it easy for her to solve for Bob's private key.



### Generalization to finite cyclic groups


Here is a more general description of the protocol:[[10]](#cite_note-11)


1. Alice and Bob agree on a natural number *n* and a [generating](//en.wikipedia.org/wiki/Generating_set_of_a_group) element *g* in the finite [cyclic group](//en.wikipedia.org/wiki/Cyclic_group) *G* of order *n*. (This is usually done long before the rest of the protocol; *g* and *n* are assumed to be known by all attackers.) The group *G* is written multiplicatively.
2. Alice picks a random [natural number](//en.wikipedia.org/wiki/Natural_number) *a* with 1 < *a* < *n*, and sends the element *ga* of *G* to Bob.
3. Bob picks a random natural number *b* with 1 < *b* < *n*, and sends the element *gb* of *G* to Alice.
4. Alice computes the element (*gb*)*a* = *gba* of G.
5. Bob computes the element (*ga*)*b* = *gab* of G.


Both Alice and Bob are now in possession of the group element *gab* = *gba*, which can serve as the shared secret key. The group *G* satisfies the requisite condition for [secure communication](//en.wikipedia.org/wiki/Secure_communication) as long as there is no efficient algorithm for determining *gab* given *g*, *ga*, and *gb*.

For example, the [elliptic curve Diffie–Hellman](//en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman) protocol is a variant that represents an element of G as a point on an elliptic curve instead of as an integer modulo n. Variants using [hyperelliptic curves](//en.wikipedia.org/wiki/Hyperelliptic_curve_cryptography) have also been proposed. The [supersingular isogeny key exchange](//en.wikipedia.org/wiki/Supersingular_isogeny_key_exchange) is a Diffie–Hellman variant that was designed to be secure against [quantum computers](//en.wikipedia.org/wiki/Quantum_computers), but it was broken in July 2022.[[11]](#cite_note-castryckdecru2023-12)



## Ephemeral and/or static keys


The used keys can either be ephemeral or static (long term) key, but could even be mixed, so called semi-static DH. These variants have different properties and hence different use cases. An overview over many variants and some also discussions can for example be found in NIST SP 800-56A.[[12]](#cite_note-13) A basic list:


1. ephemeral, ephemeral: Usually used for key agreement. Provides [forward secrecy](//en.wikipedia.org/wiki/Forward_secrecy), but no [authenticity](//en.wikipedia.org/wiki/Authentication).
2. static, static: Would generate a long term shared secret. Does not provide forward secrecy, but implicit authenticity. Since the keys are static it would for example not protect against [replay-attacks](//en.wikipedia.org/wiki/Replay_attack).
3. ephemeral, static: For example, used in [ElGamal encryption](//en.wikipedia.org/wiki/ElGamal_encryption) or [Integrated Encryption Scheme (IES)](//en.wikipedia.org/wiki/Integrated_Encryption_Scheme). If used in key agreement it could provide implicit one-sided authenticity (the ephemeral side could verify the authenticity of the static side). No forward secrecy is provided.


It is possible to use ephemeral and static keys in one key agreement to provide more security as for example shown in NIST SP 800-56A, but it is also possible to combine those in a single DH key exchange, which is then called triple DH (3-DH).



### Triple Diffie–Hellman (3-DH)


In 1997 a kind of triple DH was proposed by Simon Blake-Wilson, Don Johnson and Alfred Menezes,[[13]](#cite_note-14) which was improved by C. Kudla and K. G. Paterson in 2005[[14]](#cite_note-15) and shown to be secure.

The long term secret keys of Alice and Bob are denoted by *a* and *b* respectively, with public keys *A* and *B*, as well as the ephemeral key pairs (*x*, *X*) and (*y*, *Y*). Then protocol is:



Triple Diffie–Hellman (3-DH) protocol


Alice (${\displaystyle A=g^{a}}$)



Bob (${\displaystyle B=g^{b}}$)


${\displaystyle X=g^{x}}$

${\displaystyle X\rightarrow {}}$






${\displaystyle {}\leftarrow Y}$

${\displaystyle Y=g^{y}}$


${\displaystyle K=\operatorname {KDF} \left(Y^{x},\,B^{x},\,Y^{a},\,X,\,Y,\,A,\,B\right)}$



${\displaystyle K=\operatorname {KDF} \left(X^{y},\,X^{b},\,A^{y},\,X,\,Y,\,A,\,B\right)}$

The long term public keys need to be transferred somehow. That can be done beforehand in a separate, trusted channel, or the public keys can be encrypted using some partial key agreement to preserve anonymity. For more of such details as well as other improvements like [side channel protection](//en.wikipedia.org/wiki/Side-channel_attack) or explicit [key confirmation](//en.wikipedia.org/wiki/Key_(cryptography)), as well as early messages and additional password authentication, see e.g. US patent "Advanced modular handshake for key agreement and optional authentication".[[15]](#cite_note-16)



### Extended Triple Diffie–Hellman (X3DH)


X3DH was initially proposed as part of the [Double Ratchet Algorithm](//en.wikipedia.org/wiki/Double_Ratchet_Algorithm) used in the [Signal Protocol](//en.wikipedia.org/wiki/Signal_Protocol). The protocol offers forward secrecy and cryptographic deniability. It operates on an elliptic curve.[[16]](#cite_note-x3dh-17)

The protocol uses five public keys. Alice has an identity key IKA and an ephemeral key EKA. Bob has an identity key IKB, a signed prekey SPKB, and a one-time prekey OPKB.[[16]](#cite_note-x3dh-17) Bob first publishes his three keys to a server, which Alice downloads and verifies the signature on. Alice then initiates the exchange to Bob.[[16]](#cite_note-x3dh-17) The OPK is optional.[[16]](#cite_note-x3dh-17)



## Operation with more than two parties


Diffie–Hellman key agreement is not limited to negotiating a key shared by only two participants. Any number of users can take part in an agreement by performing iterations of the agreement protocol and exchanging intermediate data (which does not itself need to be kept secret). For example, Alice, Bob, and Carol could participate in a Diffie–Hellman agreement as follows, with all operations taken to be modulo *p*:


1. The parties agree on the algorithm parameters *p* and *g*.
2. The parties generate their private keys, named *a*, *b*, and *c*.
3. Alice computes ga mod p and sends it to Bob.
4. Bob computes (ga)b mod p = gab mod p and sends it to Carol.
5. Carol computes (gab)c mod p = gabc mod p and uses it as her secret.
6. Bob computes gb mod p and sends it to Carol.
7. Carol computes (gb)c mod p = gbc mod p and sends it to Alice.
8. Alice computes (gbc)a mod p = gbca mod p = gabc mod p and uses it as her secret.
9. Carol computes gc mod p and sends it to Alice.
10. Alice computes (gc)a mod p = gca mod p and sends it to Bob.
11. Bob computes (gca)b mod p = gcab mod p = gabc mod p and uses it as his secret.


An eavesdropper has been able to see ga mod p, gb mod p, gc mod p, gab mod p, gac mod p, and gbc mod p, but cannot use any combination of these to efficiently reproduce gabc mod p.

To extend this mechanism to larger groups, two basic principles must be followed:


- Starting with an "empty" key consisting only of *g*, the secret is made by raising the current value to every participant's private exponent once, in any order (the first such exponentiation yields the participant's own public key).
- Any intermediate value (having up to *N*−1 exponents applied, where *N* is the number of participants in the group) may be revealed publicly, but the final value (having had all *N* exponents applied) constitutes the shared secret and hence must never be revealed publicly. Thus, each user must obtain their copy of the secret by applying their own private key last (otherwise there would be no way for the last contributor to communicate the final key to its recipient, as that last contributor would have turned the key into the very secret the group wished to protect).


These principles leave open various options for choosing in which order participants contribute to keys. The simplest and most obvious solution is to arrange the *N* participants in a circle and have *N* keys rotate around the circle, until eventually every key has been contributed to by all *N* participants (ending with its owner) and each participant has contributed to *N* keys (ending with their own). However, this requires that every participant perform *N* modular exponentiations.

By choosing a more desirable order, and relying on the fact that keys can be duplicated, it is possible to reduce the number of modular exponentiations performed by each participant to log2(*N*) + 1 using a [divide-and-conquer-style](//en.wikipedia.org/wiki/Divide_and_conquer_algorithms) approach, given here for eight participants:


1. Participants A, B, C, and D each perform one exponentiation, yielding gabcd; this value is sent to E, F, G, and H. In return, participants A, B, C, and D receive gefgh.
2. Participants A and B each perform one exponentiation, yielding gefghab, which they send to C and D, while C and D do the same, yielding gefghcd, which they send to A and B.
3. Participant A performs an exponentiation, yielding gefghcda, which it sends to B; similarly, B sends gefghcdb to A. C and D do similarly.
4. Participant A performs one final exponentiation, yielding the secret gefghcdba = gabcdefgh, while B does the same to get gefghcdab = gabcdefgh; again, C and D do similarly.
5. Participants E through H simultaneously perform the same operations using gabcd as their starting point.


Once this operation has been completed all participants will possess the secret gabcdefgh, but each participant will have performed only four modular exponentiations, rather than the eight implied by a simple circular arrangement.



## Security and practical considerations


The protocol is considered secure against eavesdroppers if *G* and *g* are chosen properly. In particular, the order of the group G must be large, particularly if the same group is used for large amounts of traffic. The eavesdropper has to solve the [Diffie–Hellman problem](//en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_problem) to obtain *g**ab*. This is currently considered difficult for groups whose order is large enough. An efficient algorithm to solve the [discrete logarithm problem](//en.wikipedia.org/wiki/Discrete_logarithm_problem) would make it easy to compute *a* or *b* and solve the Diffie–Hellman problem, making this and many other public key cryptosystems insecure. Fields of small characteristic may be less secure.[[17]](#cite_note-18)

The [order](//en.wikipedia.org/wiki/Order_(group_theory)) of *G* should have a large prime factor to prevent use of the [Pohlig–Hellman algorithm](//en.wikipedia.org/wiki/Pohlig%E2%80%93Hellman_algorithm) to obtain *a* or *b*. For this reason, a [Sophie Germain prime](//en.wikipedia.org/wiki/Sophie_Germain_prime) *q* is sometimes used to calculate *p* = 2*q* + 1, called a [safe prime](//en.wikipedia.org/wiki/Safe_prime), since the order of *G* is then only divisible by 2 and *q*. Sometimes *g* is chosen to generate the order *q* subgroup of *G*, rather than *G*, so that the [Legendre symbol](//en.wikipedia.org/wiki/Legendre_symbol) of *ga* never reveals the low order bit of *a*. A protocol using such a choice is for example [IKEv2](//en.wikipedia.org/wiki/Internet_Key_Exchange).[[18]](#cite_note-19)

The generator *g* is often a small integer such as 2. Because of the [random self-reducibility](//en.wikipedia.org/wiki/Random_self-reducibility) of the discrete logarithm problem a small *g* is equally secure as any other generator of the same group.

If Alice and Bob use [random number generators](//en.wikipedia.org/wiki/Random_number_generator) whose outputs are not completely random and can be predicted to some extent, then it is much easier to eavesdrop.

In the original description, the Diffie–Hellman exchange by itself does not provide [authentication](//en.wikipedia.org/wiki/Authentication) of the communicating parties and can be vulnerable to a [man-in-the-middle attack](//en.wikipedia.org/wiki/Man-in-the-middle_attack).
Mallory (an active attacker executing the man-in-the-middle attack) may establish two distinct key exchanges, one with Alice and the other with Bob, effectively masquerading as Alice to Bob, and vice versa, allowing her to decrypt, then re-encrypt, the messages passed between them. Note that Mallory must be in the middle from the beginning and continuing to be so, actively decrypting and re-encrypting messages every time Alice and Bob communicate. If she arrives after the keys have been generated and the encrypted conversation between Alice and Bob has already begun, the attack cannot succeed. If she is ever absent, her previous presence is then revealed to Alice and Bob. They will know that all of their private conversations had been intercepted and decoded by someone in the channel. In most cases it will not help them get Mallory's private key, even if she used the same key for both exchanges.

A method to authenticate the communicating parties to each other is generally needed to prevent this type of attack. Variants of Diffie–Hellman, such as [STS protocol](//en.wikipedia.org/wiki/Station-to-Station_protocol), may be used instead to avoid these types of attacks.



### Denial-of-service attack


A [CVE](//en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures) released in 2021 (*[CVE-2002-20001](https://nvd.nist.gov/vuln/detail/CVE-2002-20001)*) disclosed a [denial-of-service attack](//en.wikipedia.org/wiki/Denial-of-service_attack) (DoS) against the protocol variants using ephemeral keys, called D(HE)at attack.[[19]](#cite_note-dheatattack-20) The attack exploits that the Diffie–Hellman key exchange allows attackers to send arbitrary numbers that are actually not public keys, triggering expensive modular exponentiation calculations on the victim's side. Another CVEs release disclosed that the Diffie–Hellman key exchange implementations may use long private exponents  (*[CVE-2022-40735](https://nvd.nist.gov/vuln/detail/CVE-2022-40735)*) that arguably make modular exponentiation calculations unnecessarily expensive[[20]](#cite_note-Oorschot_Wiener_1996-21) or may unnecessarily check a peer's public key (*[CVE-2024-41996](https://nvd.nist.gov/vuln/detail/CVE-2024-41996)*) which has similar resource requirement as key calculation using a long exponent.[[21]](#cite_note-22) An attacker can exploit both vulnerabilities together.



### Practical attacks on Internet traffic


The [number field sieve](//en.wikipedia.org/wiki/General_number_field_sieve) algorithm, which is generally the most effective in solving the [discrete logarithm problem](//en.wikipedia.org/wiki/Discrete_logarithm_problem), consists of four computational steps. The first three steps only depend on the order of the group G, not on the specific number whose finite log is desired.[[22]](#cite_note-23) It turns out that much Internet traffic uses one of a handful of groups that are of order 1024 bits or less.[[2]](#cite_note-imperfectfs-3) By [precomputing](//en.wikipedia.org/wiki/Precomputing) the first three steps of the number field sieve for the most common groups, an attacker need only carry out the last step, which is much less computationally expensive than the first three steps, to obtain a specific logarithm. The [Logjam](//en.wikipedia.org/wiki/Logjam_(computer_security)) attack used this vulnerability to compromise a variety of Internet services that allowed the use of groups whose order was a 512-bit prime number, so called [export grade](//en.wikipedia.org/wiki/Export_of_cryptography). The authors needed several thousand CPU cores for a week to precompute data for a single 512-bit prime. Once that was done, individual logarithms could be solved in about a minute using two 18-core Intel Xeon CPUs.[[2]](#cite_note-imperfectfs-3)

As estimated by the authors behind the Logjam attack, the much more difficult precomputation needed to solve the discrete log problem for a 1024-bit prime would cost on the order of $100 million, well within the budget of a large national [intelligence agency](//en.wikipedia.org/wiki/Intelligence_agency) such as the U.S. [National Security Agency](//en.wikipedia.org/wiki/National_Security_Agency) (NSA). The Logjam authors speculate that precomputation against widely reused 1024-bit DH primes is behind claims in [leaked NSA documents](//en.wikipedia.org/wiki/2010s_global_surveillance_disclosures) that NSA is able to break much of current cryptography.[[2]](#cite_note-imperfectfs-3)

To avoid these vulnerabilities, the Logjam authors recommend use of [elliptic curve cryptography](//en.wikipedia.org/wiki/Elliptic_curve_cryptography), for which no similar attack is known. Failing that, they recommend that the order, *p*, of the Diffie–Hellman group should be at least 2048 bits. They estimate that the pre-computation required for a 2048-bit prime is 109 times more difficult than for 1024-bit primes.[[2]](#cite_note-imperfectfs-3)



### Security against quantum computers


[Quantum computers](//en.wikipedia.org/wiki/Quantum_computing) can break public-key cryptographic schemes, such as RSA, finite-field DH and elliptic-curve DH key-exchange protocols, using [Shor's algorithm](//en.wikipedia.org/wiki/Shor%27s_algorithm) for solving the [factoring problem](//en.wikipedia.org/wiki/Integer_factorization), the [discrete logarithm problem](//en.wikipedia.org/wiki/Discrete_logarithm), and the period-finding problem. A [post-quantum variant of Diffie-Hellman algorithm](//en.wikipedia.org/wiki/Post-Quantum_Extended_Diffie%E2%80%93Hellman) was proposed in 2023, and relies on a combination of the quantum-resistant CRYSTALS-Kyber protocol, as well as the old elliptic curve [X25519](//en.wikipedia.org/wiki/X25519) protocol.



## Other uses



### Encryption


Public key encryption schemes based on the Diffie–Hellman key exchange have been proposed. The first such scheme is the [ElGamal encryption](//en.wikipedia.org/wiki/ElGamal_encryption). A more modern variant is the [Integrated Encryption Scheme](//en.wikipedia.org/wiki/Integrated_Encryption_Scheme).



### Forward secrecy


Protocols that achieve [forward secrecy](//en.wikipedia.org/wiki/Forward_secrecy) generate new key pairs for each [session](//en.wikipedia.org/wiki/Session_(computer_science)) and discard them at the end of the session. The Diffie–Hellman key exchange is a frequent choice for such protocols, because of its fast key generation.



### Password-authenticated key agreement


When Alice and Bob share a password, they may use a [password-authenticated key agreement](//en.wikipedia.org/wiki/Password-authenticated_key_agreement) (PK) form of Diffie–Hellman to prevent man-in-the-middle attacks. One simple scheme is to compare the [hash](//en.wikipedia.org/wiki/Cryptographic_hash_function) of **s** concatenated with the password calculated independently on both ends of channel. A feature of these schemes is that an attacker can only test one specific password on each iteration with the other party, and so the system provides good security with relatively weak passwords. This approach is described in [ITU-T](//en.wikipedia.org/wiki/ITU-T) Recommendation [X.1035](//en.wikipedia.org/wiki/X.1035), which is used by the [G.hn](//en.wikipedia.org/wiki/G.hn) home networking standard.

An example of such a protocol is the [Secure Remote Password protocol](//en.wikipedia.org/wiki/Secure_Remote_Password_protocol).



### Public key


It is also possible to use Diffie–Hellman as part of a [public key infrastructure](//en.wikipedia.org/wiki/Public_key_infrastructure), allowing Bob to encrypt a message so that only Alice will be able to decrypt it, with no prior communication between them other than Bob having trusted knowledge of Alice's public key. Alice's public key is ${\displaystyle (g^{a}{\bmod {p}},g,p)}$. To send her a message, Bob chooses a random *b* and then sends Alice ${\displaystyle g^{b}{\bmod {p}}}$ (unencrypted) together with the message encrypted with symmetric key ${\displaystyle (g^{a})^{b}{\bmod {p}}}$. Only Alice can determine the symmetric key and hence decrypt the message because only she has *a* (the private key). A pre-shared public key also prevents man-in-the-middle attacks.

In practice, Diffie–Hellman is not used in this way, with [RSA](//en.wikipedia.org/wiki/RSA_(cryptosystem)) being the dominant public key algorithm. This is largely for historical and commercial reasons,[*[citation needed](//en.wikipedia.org/wiki/Wikipedia:Citation_needed)*] namely that [RSA Security](//en.wikipedia.org/wiki/RSA_(security_firm)) created a [certificate authority](//en.wikipedia.org/wiki/Certificate_authority) for key signing that became [Verisign](//en.wikipedia.org/wiki/Verisign). Diffie–Hellman, as elaborated above, cannot directly be used to sign certificates. However, the [ElGamal](//en.wikipedia.org/wiki/ElGamal_signature_scheme) and [DSA](//en.wikipedia.org/wiki/Digital_Signature_Algorithm) signature algorithms are mathematically related to it, as well as [MQV](//en.wikipedia.org/wiki/MQV), [STS](//en.wikipedia.org/wiki/Station-to-Station_protocol) and the [IKE](//en.wikipedia.org/wiki/Internet_Key_Exchange) component of the [IPsec](//en.wikipedia.org/wiki/IPsec) protocol suite for securing [Internet Protocol](//en.wikipedia.org/wiki/Internet_Protocol) communications.



## See also


- [Elliptic-curve Diffie–Hellman](//en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman) key exchange
- [Supersingular isogeny key exchange](//en.wikipedia.org/wiki/Supersingular_isogeny_key_exchange)
- [Forward secrecy](//en.wikipedia.org/wiki/Forward_secrecy)
- [Diffie–Hellman problem](//en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_problem)
- [Modular exponentiation](//en.wikipedia.org/wiki/Modular_exponentiation)
- [Denial-of-service attack](//en.wikipedia.org/wiki/Denial-of-service_attack)
- [Post-Quantum Extended Diffie–Hellman](//en.wikipedia.org/wiki/Post-Quantum_Extended_Diffie%E2%80%93Hellman)
- [Accumulator (cryptography)](//en.wikipedia.org/wiki/Accumulator_(cryptography))



## Notes



1. **[^](#cite_ref-1)** Synonyms of Diffie–Hellman key exchange include:
- Diffie–Hellman–Merkle key exchange
- Diffie–Hellman key agreement
- Diffie–Hellman key establishment
- Diffie–Hellman key negotiation
- Exponential key exchange
- Diffie–Hellman protocol
- Diffie–Hellman handshake



## References



1. **[^](#cite_ref-Merkle_1978_2-0)** Merkle, Ralph C. (April 1978). "Secure Communications Over Insecure Channels". *[Communications of the ACM](//en.wikipedia.org/wiki/Communications_of_the_ACM)*. **21** (4): 294–299. [CiteSeerX](//en.wikipedia.org/wiki/CiteSeerX_(identifier)) [10.1.1.364.5157](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.364.5157). [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.1145/359460.359473](https://doi.org/10.1145%2F359460.359473). [S2CID](//en.wikipedia.org/wiki/S2CID_(identifier)) [6967714](https://api.semanticscholar.org/CorpusID:6967714). Received August, 1975; revised September 1977
2. ^ [***a***](#cite_ref-imperfectfs_3-0) [***b***](#cite_ref-imperfectfs_3-1) [***c***](#cite_ref-imperfectfs_3-2) [***d***](#cite_ref-imperfectfs_3-3) [***e***](#cite_ref-imperfectfs_3-4) [***f***](#cite_ref-imperfectfs_3-5) Adrian, David; et al. (October 2015). ["Imperfect Forward Secrecy: How Diffie–Hellman Fails in Practice"](https://weakdh.org/imperfect-forward-secrecy-ccs15.pdf) (PDF). [Archived](https://web.archive.org/web/20150906213656/https://weakdh.org/imperfect-forward-secrecy-ccs15.pdf) (PDF) from the original on 2015-09-06.
3. ^ [***a***](#cite_ref-Diffie_1976_4-0) [***b***](#cite_ref-Diffie_1976_4-1) [Diffie, Whitfield](//en.wikipedia.org/wiki/Whitfield_Diffie); [Hellman, Martin E.](//en.wikipedia.org/wiki/Martin_Hellman) (November 1976). ["New Directions in Cryptography"](http://ee.stanford.edu/%7Ehellman/publications/24.pdf) (PDF). *[IEEE Transactions on Information Theory](//en.wikipedia.org/wiki/IEEE_Transactions_on_Information_Theory)*. **22** (6): 644–654. [Bibcode](//en.wikipedia.org/wiki/Bibcode_(identifier)):[1976ITIT...22..644D](https://ui.adsabs.harvard.edu/abs/1976ITIT...22..644D). [CiteSeerX](//en.wikipedia.org/wiki/CiteSeerX_(identifier)) [10.1.1.37.9720](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.37.9720). [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.1109/TIT.1976.1055638](https://doi.org/10.1109%2FTIT.1976.1055638). [Archived](https://web.archive.org/web/20141129035850/https://ee.stanford.edu/%7Ehellman/publications/24.pdf) (PDF) from the original on 2014-11-29.
4. **[^](#cite_ref-5)** [Ellis, J. H.](//en.wikipedia.org/wiki/James_H._Ellis) (January 1970). ["The possibility of Non-Secret digital encryption"](https://web.archive.org/web/20141030210530/https://cryptocellar.web.cern.ch/cryptocellar/cesg/possnse.pdf) (PDF). *CESG Research Report*. Archived from [the original](http://cryptocellar.web.cern.ch/cryptocellar/cesg/possnse.pdf) (PDF) on 2014-10-30. Retrieved 2015-08-28.
5. **[^](#cite_ref-6)** ["The Possibility of Secure Secret Digital Encryption"](https://www.gchq.gov.uk/sites/default/files/document_files/CESG_Research_Report_No_3006_0.pdf) (PDF). [Archived](https://web.archive.org/web/20170216051636/https://www.gchq.gov.uk/sites/default/files/document_files/CESG_Research_Report_No_3006_0.pdf) (PDF) from the original on 2017-02-16. Retrieved 2017-07-08.
6. **[^](#cite_ref-7)** ["GCHQ trio recognised for key to secure shopping online"](https://www.bbc.co.uk/news/uk-england-gloucestershire-11475101). *[BBC News](//en.wikipedia.org/wiki/BBC_News)*. 5 October 2010. [Archived](https://web.archive.org/web/20140810044800/http://www.bbc.co.uk/news/uk-england-gloucestershire-11475101) from the original on 10 August 2014. Retrieved 5 August 2014.
7. **[^](#cite_ref-8)** [US patent 4200770](https://worldwide.espacenet.com/textdoc?DB=EPODOC&IDX=US4200770)
8. **[^](#cite_ref-Hellman2002_9-0)** Hellman, Martin E. (May 2002), ["An overview of public key cryptography"](http://www-ee.stanford.edu/~hellman/publications/31.pdf) (PDF), *IEEE Communications Magazine*, **40** (5): 42–49, [Bibcode](//en.wikipedia.org/wiki/Bibcode_(identifier)):[2002IComM..40e..42H](https://ui.adsabs.harvard.edu/abs/2002IComM..40e..42H), [CiteSeerX](//en.wikipedia.org/wiki/CiteSeerX_(identifier)) [10.1.1.127.2652](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.127.2652), [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.1109/MCOM.2002.1006971](https://doi.org/10.1109%2FMCOM.2002.1006971), [S2CID](//en.wikipedia.org/wiki/S2CID_(identifier)) [9504647](https://api.semanticscholar.org/CorpusID:9504647), [archived](https://web.archive.org/web/20160402093741/http://www-ee.stanford.edu/%7Ehellman/publications/31.pdf) (PDF) from the original on 2016-04-02
9. **[^](#cite_ref-10)** Wong, David (2021). "Key exchange standards". [*Real World Cryptography*](https://books.google.com/books?id=Qd5CEAAAQBAJ). Manning. [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [9781617296710](//en.wikipedia.org/wiki/Special:BookSources/9781617296710) – via Google Books.`{{[cite book](//en.wikipedia.org/wiki/Template:Cite_book)}}`:  CS1 maint: deprecated archival service ([link](//en.wikipedia.org/wiki/Category:CS1_maint:_deprecated_archival_service))
10. **[^](#cite_ref-11)** Buchmann, Johannes A. (2013). [*Introduction to Cryptography*](https://books.google.com/books?id=BuQlBQAAQBAJ&pg=PA190) (Second ed.). Springer Science+Business Media. pp. 190–191. [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [978-1-4419-9003-7](//en.wikipedia.org/wiki/Special:BookSources/978-1-4419-9003-7).
11. **[^](#cite_ref-castryckdecru2023_12-0)** Castryck, Wouter; Decru, Thomas (April 2023). ["An efficient key recovery attack on SIDH"](https://web.archive.org/web/20240926174200/https://eprint.iacr.org/2022/975.pdf) (PDF). *Annual International Conference on the Theory and Applications of Cryptographic Techniques*: 423–447. Archived from [the original](https://eprint.iacr.org/2022/975.pdf) (PDF) on 2024-09-26.
12. **[^](#cite_ref-13)** Barker, Elaine; Chen, Lily; Roginsky, Allen; Vassilev, Apostol; Davis, Richard (2018-04-16). [Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography](https://csrc.nist.gov/Pubs/sp/800/56/a/r3/Final) (Report). National Institute of Standards and Technology.
13. **[^](#cite_ref-14)** Blake-Wilson, Simon; Johnson, Don; Menezes, Alfred (1997), "Key Agreement Protocols and their Security Analysis", *Crytography and Coding*, Lecture Notes in Computer Science, vol. 1355, pp. 30–45, [CiteSeerX](//en.wikipedia.org/wiki/CiteSeerX_(identifier)) [10.1.1.25.387](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.25.387), [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/BFb0024447](https://doi.org/10.1007%2FBFb0024447), [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-540-63927-5](//en.wikipedia.org/wiki/Special:BookSources/978-3-540-63927-5)
14. **[^](#cite_ref-15)** Kudla, Caroline; Paterson, Kenneth G. (2005). "Modular Security Proofs for Key Agreement Protocols". In Roy, Bimal (ed.). [*Advances in Cryptology - ASIACRYPT 2005*](https://iacr.org/archive/asiacrypt2005/546/546.pdf) (PDF). Lecture Notes in Computer Science. Vol. 3788. Berlin, Heidelberg: Springer. pp. 549–565. [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/11593447_30](https://doi.org/10.1007%2F11593447_30). [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-540-32267-2](//en.wikipedia.org/wiki/Special:BookSources/978-3-540-32267-2).
15. **[^](#cite_ref-16)** [US11025421B2](https://patents.google.com/patent/US11025421B2/en?oq=11025421), Fay, Bjorn, "Advanced modular handshake for key agreement and optional authentication", issued 2021-06-01
16. ^ [***a***](#cite_ref-x3dh_17-0) [***b***](#cite_ref-x3dh_17-1) [***c***](#cite_ref-x3dh_17-2) [***d***](#cite_ref-x3dh_17-3) ["Specifications >> The X3DH Key Agreement Protocol"](https://www.signal.org/docs/specifications/x3dh/). *Signal Messenger*.
17. **[^](#cite_ref-18)** Barbulescu, Razvan; Gaudry, Pierrick; Joux, Antoine; Thomé, Emmanuel (2014). ["A Heuristic Quasi-Polynomial Algorithm for Discrete Logarithm in Finite Fields of Small Characteristic"](http://hal.inria.fr/docs/00/90/90/87/PDF/article.pdf) (PDF). *Advances in Cryptology – EUROCRYPT 2014*. Proceedings 33rd Annual International Conference on the Theory and Applications of Cryptographic Techniques. Lecture Notes in Computer Science. Vol. 8441. Copenhagen, Denmark. pp. 1–16. [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/978-3-642-55220-5_1](https://doi.org/10.1007%2F978-3-642-55220-5_1). [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-642-55220-5](//en.wikipedia.org/wiki/Special:BookSources/978-3-642-55220-5). [Archived](https://web.archive.org/web/20200322030320/https://hal.inria.fr/docs/00/90/90/87/PDF/article.pdf) (PDF) from the original on 2020-03-22.
18. **[^](#cite_ref-19)** "RFC 4306 Internet Key Exchange (IKEv2) Protocol". Internet Engineeringrg/web/20150107073645/[http://www.ietf.org/rfc/rfc4306.txt](http://www.ietf.org/rfc/rfc4306.txt).
19. **[^](#cite_ref-dheatattack_20-0)** Pfeiffer, Szilárd; Tihanyi, Norbert (25 December 2023). ["D(HE)at: A Practical Denial-of-Service Attack on the Finite Field Diffie-Hellman Key Exchange"](https://doi.org/10.1109%2FACCESS.2023.3347422). *[IEEE Access](//en.wikipedia.org/wiki/IEEE_Access)*. **12**: 957–980. [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.1109/ACCESS.2023.3347422](https://doi.org/10.1109%2FACCESS.2023.3347422).
20. **[^](#cite_ref-Oorschot_Wiener_1996_21-0)** van Oorschot, P.C.; Wiener, M.J. (1996). ["On Diffie-Hellman Key Agreement with Short Exponents"](https://link.springer.com/chapter/10.1007/3-540-68339-9_29). *Advances in Cryptology — EUROCRYPT '96*. Lecture Notes in Computer Science. Vol. 1070. Springer, Berlin, Heidelberg (published 2001). pp. 332–343. [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.1007/3-540-68339-9_29](https://doi.org/10.1007%2F3-540-68339-9_29). [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [978-3-540-61186-8](//en.wikipedia.org/wiki/Special:BookSources/978-3-540-61186-8). [Archived](https://web.archive.org/web/20230219191210/https://link.springer.com/chapter/10.1007/3-540-68339-9_29) from the original on 2023-02-19.
21. **[^](#cite_ref-22)** Elaine, Barker; Lily, Chen; Allen, Roginsky; Apostol, Vassilev; Richard, Davis (2018). ["Recommendation for Pair-Wise Key-Establishment Schemes Using Discrete Logarithm Cryptography"](https://csrc.nist.gov/pubs/sp/800/56/a/r3/final). National Institute of Standards and Technology. [doi](//en.wikipedia.org/wiki/Doi_(identifier)):[10.6028/NIST.SP.800-56Ar3](https://doi.org/10.6028%2FNIST.SP.800-56Ar3).
22. **[^](#cite_ref-23)** Whitfield Diffie, Paul C. Van Oorschot, and Michael J. Wiener "Authentication and Authenticated Key Exchanges", in Designs, Codes and Cryptography, 2, 107–125 (1992), Section 5.2, available as Appendix B to [U.S. patent 5,724,425](https://patents.google.com/patent/US5724425)



### General references


- Gollman, Dieter (2011). *Computer Security* (2nd ed.). West Sussex, England: John Wiley & Sons, Ltd. [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [978-0470741153](//en.wikipedia.org/wiki/Special:BookSources/978-0470741153).
- Williamson, Malcolm J. (January 21, 1974). [*Non-secret encryption using a finite field*](https://www.gchq.gov.uk/sites/default/files/document_files/nonsecret_encryption_finite_field_0.pdf) (PDF) (Technical report). Communications Electronics Security Group. [Archived](https://web.archive.org/web/20170323052715/https://www.gchq.gov.uk/sites/default/files/document_files/nonsecret_encryption_finite_field_0.pdf) (PDF) from the original on 2017-03-23. Retrieved 2017-03-22.
- Williamson, Malcolm J. (August 10, 1976). [*Thoughts on Cheaper Non-Secret Encryption*](http://www.fi.muni.cz/usr/matyas/lecture/paper3.pdf) (PDF) (Technical report). Communications Electronics Security Group. [Archived](https://web.archive.org/web/20040719085349/http://www.fi.muni.cz/usr/matyas/lecture/paper3.pdf) (PDF) from the original on 2004-07-19. Retrieved 2015-08-25.
- [The History of Non-Secret Encryption](https://web.archive.org/web/20130404174201/https://cryptocellar.web.cern.ch/cryptocellar/cesg/ellis.pdf) [JH Ellis](//en.wikipedia.org/wiki/James_H._Ellis) 1987 (28K PDF file) ([HTML version](https://web.archive.org/web/20040808040209/http://jya.com/ellisdoc.htm))
- [The First Ten Years of Public-Key Cryptography](http://cr.yp.to/bib/1988/diffie.pdf) Whitfield Diffie, Proceedings of the IEEE, vol. 76, no. 5, May 1988, pp: 560–577 (1.9MB PDF file)
- [Menezes, Alfred](//en.wikipedia.org/wiki/Alfred_Menezes); [van Oorschot, Paul](//en.wikipedia.org/wiki/Paul_van_Oorschot); [Vanstone, Scott](//en.wikipedia.org/wiki/Scott_Vanstone) (1997). *[Handbook of Applied Cryptography](//en.wikipedia.org/w/index.php?title=Handbook_of_Applied_Cryptography&action=edit&redlink=1)* Boca Raton, Florida: CRC Press. [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [0-8493-8523-7](//en.wikipedia.org/wiki/Special:BookSources/0-8493-8523-7). ([Available online](http://www.cacr.math.uwaterloo.ca/hac/))
- [Singh, Simon](//en.wikipedia.org/wiki/Simon_Singh) (1999) *[The Code Book: the evolution of secrecy from Mary Queen of Scots to quantum cryptography](//en.wikipedia.org/wiki/The_Code_Book:_the_evolution_of_secrecy_from_Mary_Queen_of_Scots_to_quantum_cryptography)* New York: Doubleday [ISBN](//en.wikipedia.org/wiki/ISBN_(identifier)) [0-385-49531-5](//en.wikipedia.org/wiki/Special:BookSources/0-385-49531-5)
- [An Overview of Public Key Cryptography](https://dx.doi.org/10.1109/MCOM.2002.1006971) Martin E. Hellman, IEEE Communications Magazine, May 2002, pp. 42–49. (123kB PDF file)



## External links


- [Oral history interview with Martin Hellman](https://conservancy.umn.edu/handle/11299/107353), [Charles Babbage Institute](//en.wikipedia.org/wiki/Charles_Babbage_Institute), University of Minnesota. Leading cryptography scholar Martin Hellman discusses the circumstances and fundamental insights of his invention of public key cryptography with collaborators Whitfield Diffie and Ralph Merkle at [Stanford University](//en.wikipedia.org/wiki/Stanford_University) in the mid-1970s.
- RFC [2631](https://www.rfc-editor.org/rfc/rfc2631) – *Diffie–Hellman Key Agreement Method*. E. Rescorla. June 1999.
- RFC [3526](https://www.rfc-editor.org/rfc/rfc3526) – *More Modular Exponential (MODP) Diffie–Hellman groups for Internet Key Exchange (IKE)*. T. Kivinen, M. Kojo, SSH Communications Security. May 2003.





- [v](//en.wikipedia.org/wiki/Template:Cryptography_public-key)
- [t](//en.wikipedia.org/wiki/Template_talk:Cryptography_public-key)
- [e](//en.wikipedia.org/wiki/Special:EditPage/Template:Cryptography_public-key)

[Public-key cryptography](//en.wikipedia.org/wiki/Public-key_cryptography)Algorithms[Integer factorization](//en.wikipedia.org/wiki/Integer_factorization)
- [Benaloh](//en.wikipedia.org/wiki/Benaloh_cryptosystem)
- [Blum–Goldwasser](//en.wikipedia.org/wiki/Blum%E2%80%93Goldwasser_cryptosystem)
- [Cayley–Purser](//en.wikipedia.org/wiki/Cayley%E2%80%93Purser_algorithm)
- [Damgård–Jurik](//en.wikipedia.org/wiki/Damg%C3%A5rd%E2%80%93Jurik_cryptosystem)
- [GMR](//en.wikipedia.org/wiki/GMR_(cryptography))
- [Goldwasser–Micali](//en.wikipedia.org/wiki/Goldwasser%E2%80%93Micali_cryptosystem)
- [Naccache–Stern](//en.wikipedia.org/wiki/Naccache%E2%80%93Stern_cryptosystem)
- [Paillier](//en.wikipedia.org/wiki/Paillier_cryptosystem)
- [Rabin](//en.wikipedia.org/wiki/Rabin_signature)
- [RSA](//en.wikipedia.org/wiki/RSA_cryptosystem)
- [Okamoto–Uchiyama](//en.wikipedia.org/wiki/Okamoto%E2%80%93Uchiyama_cryptosystem)
- [Schmidt–Samoa](//en.wikipedia.org/wiki/Schmidt-Samoa_cryptosystem)


[Discrete logarithm](//en.wikipedia.org/wiki/Discrete_logarithm)
- [BLS](//en.wikipedia.org/wiki/Boneh%E2%80%93Lynn%E2%80%93Shacham)
- [Cramer–Shoup](//en.wikipedia.org/wiki/Cramer%E2%80%93Shoup_cryptosystem)
- DH
- [DSA](//en.wikipedia.org/wiki/Digital_Signature_Algorithm)
- [ECDH](//en.wikipedia.org/wiki/Elliptic-curve_Diffie%E2%80%93Hellman)
- [X25519](//en.wikipedia.org/wiki/Curve25519)
- [X448](//en.wikipedia.org/wiki/Curve448)
- [ECDSA](//en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- [EdDSA](//en.wikipedia.org/wiki/EdDSA)
- [Ed25519](//en.wikipedia.org/wiki/EdDSA#Ed25519)
- [Ed448](//en.wikipedia.org/wiki/EdDSA#Ed448)
- [ECMQV](//en.wikipedia.org/wiki/ECMQV)
- [EKE](//en.wikipedia.org/wiki/Encrypted_key_exchange)
- [ElGamal](//en.wikipedia.org/wiki/ElGamal_encryption)
- [signature scheme](//en.wikipedia.org/wiki/ElGamal_signature_scheme)
- [MQV](//en.wikipedia.org/wiki/MQV)
- [Schnorr](//en.wikipedia.org/wiki/Schnorr_signature)
- [SPEKE](//en.wikipedia.org/wiki/SPEKE)
- [SRP](//en.wikipedia.org/wiki/Secure_Remote_Password_protocol)
- [STS](//en.wikipedia.org/wiki/Station-to-Station_protocol)


[Lattice/SVP/CVP](//en.wikipedia.org/wiki/Lattice-based_cryptography)/[LWE](//en.wikipedia.org/wiki/Learning_with_errors)/[SIS](//en.wikipedia.org/wiki/Short_integer_solution_problem)
- [BLISS](//en.wikipedia.org/wiki/BLISS_signature_scheme)
- [Kyber](//en.wikipedia.org/wiki/Kyber)
- [NewHope](//en.wikipedia.org/wiki/NewHope)
- [NTRUEncrypt](//en.wikipedia.org/wiki/NTRUEncrypt)
- [NTRUSign](//en.wikipedia.org/wiki/NTRUSign)
- [RLWE-KEX](//en.wikipedia.org/wiki/RLWE-KEX)
- [RLWE-SIG](//en.wikipedia.org/wiki/RLWE-SIG)


Others
- [AE](//en.wikipedia.org/wiki/Algebraic_Eraser)
- [CEILIDH](//en.wikipedia.org/wiki/CEILIDH)
- [EPOC](//en.wikipedia.org/wiki/Efficient_Probabilistic_Public-Key_Encryption_Scheme)
- [HFE](//en.wikipedia.org/wiki/Hidden_Field_Equations)
- [IES](//en.wikipedia.org/wiki/Integrated_Encryption_Scheme)
- [Lamport](//en.wikipedia.org/wiki/Lamport_signature)
- [McEliece](//en.wikipedia.org/wiki/McEliece_cryptosystem)
- [Merkle–Hellman](//en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem)
- [Naccache–Stern knapsack cryptosystem](//en.wikipedia.org/wiki/Naccache%E2%80%93Stern_knapsack_cryptosystem)
- [Three-pass protocol](//en.wikipedia.org/wiki/Three-pass_protocol)
- [XTR](//en.wikipedia.org/wiki/XTR)
- [SQIsign](//en.wikipedia.org/wiki/SQIsign)
- [SPHINCS+](//en.wikipedia.org/wiki/SPHINCS%2B)


Theory
- [Discrete logarithm cryptography](//en.wikipedia.org/wiki/Discrete_logarithm#Cryptography)
- [Elliptic-curve cryptography](//en.wikipedia.org/wiki/Elliptic-curve_cryptography)
- [Hash-based cryptography](//en.wikipedia.org/wiki/Hash-based_cryptography)
- [Non-commutative cryptography](//en.wikipedia.org/wiki/Non-commutative_cryptography)
- [RSA problem](//en.wikipedia.org/wiki/RSA_problem)
- [Trapdoor function](//en.wikipedia.org/wiki/Trapdoor_function)


Standardization
- [CRYPTREC](//en.wikipedia.org/wiki/CRYPTREC)
- [IEEE P1363](//en.wikipedia.org/wiki/IEEE_P1363)
- [NESSIE](//en.wikipedia.org/wiki/NESSIE)
- [NSA Suite B](//en.wikipedia.org/wiki/NSA_Suite_B_Cryptography)
- [CNSA](//en.wikipedia.org/wiki/Commercial_National_Security_Algorithm_Suite)
- [Post-Quantum Cryptography](//en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization)


Topics
- [Digital signature](//en.wikipedia.org/wiki/Digital_signature)
- [OAEP](//en.wikipedia.org/wiki/Optimal_asymmetric_encryption_padding)
- [Fingerprint](//en.wikipedia.org/wiki/Public_key_fingerprint)
- [PKI](//en.wikipedia.org/wiki/Public_key_infrastructure)
- [Web of trust](//en.wikipedia.org/wiki/Web_of_trust)
- [Key size](//en.wikipedia.org/wiki/Key_size)
- [Identity-based cryptography](//en.wikipedia.org/wiki/Identity-based_cryptography)
- [Post-quantum cryptography](//en.wikipedia.org/wiki/Post-quantum_cryptography)
- [OpenPGP card](//en.wikipedia.org/wiki/OpenPGP_card)


- [v](//en.wikipedia.org/wiki/Template:Cryptography)
- [t](//en.wikipedia.org/wiki/Template_talk:Cryptography)
- [e](//en.wikipedia.org/wiki/Special:EditPage/Template:Cryptography)

[Cryptography](//en.wikipedia.org/wiki/Cryptography)General
- [History of cryptography](//en.wikipedia.org/wiki/History_of_cryptography)
- [Outline of cryptography](//en.wikipedia.org/wiki/Outline_of_cryptography)
- [Classical cipher](//en.wikipedia.org/wiki/Classical_cipher)
- [Cryptographic protocol](//en.wikipedia.org/wiki/Cryptographic_protocol)
- [Authentication protocol](//en.wikipedia.org/wiki/Authentication_protocol)
- [Cryptographic primitive](//en.wikipedia.org/wiki/Cryptographic_primitive)
- [Cryptanalysis](//en.wikipedia.org/wiki/Cryptanalysis)
- [Cryptocurrency](//en.wikipedia.org/wiki/Cryptocurrency)
- [Cryptosystem](//en.wikipedia.org/wiki/Cryptosystem)
- [Cryptographic nonce](//en.wikipedia.org/wiki/Cryptographic_nonce)
- [Cryptovirology](//en.wikipedia.org/wiki/Cryptovirology)
- [Hash function](//en.wikipedia.org/wiki/Hash_function)
- [Cryptographic hash function](//en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Key derivation function](//en.wikipedia.org/wiki/Key_derivation_function)
- [Secure Hash Algorithms](//en.wikipedia.org/wiki/Secure_Hash_Algorithms)
- [Digital signature](//en.wikipedia.org/wiki/Digital_signature)
- [Kleptography](//en.wikipedia.org/wiki/Kleptography)
- [Key (cryptography)](//en.wikipedia.org/wiki/Key_(cryptography))
- [Key exchange](//en.wikipedia.org/wiki/Key_exchange)
- [Key generator](//en.wikipedia.org/wiki/Key_generator)
- [Key schedule](//en.wikipedia.org/wiki/Key_schedule)
- [Key stretching](//en.wikipedia.org/wiki/Key_stretching)
- [Keygen](//en.wikipedia.org/wiki/Keygen)
- [Machines](//en.wikipedia.org/wiki/Template:Cryptography_machines)
- [Ransomware](//en.wikipedia.org/wiki/Ransomware)
- [Random number generation](//en.wikipedia.org/wiki/Random_number_generation)
- [Cryptographically secure pseudorandom number generator](//en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator) (CSPRNG)
- [Pseudorandom noise](//en.wikipedia.org/wiki/Pseudorandom_noise) (PRN)
- [Secure channel](//en.wikipedia.org/wiki/Secure_channel)
- [Insecure channel](//en.wikipedia.org/wiki/Insecure_channel)
- [Subliminal channel](//en.wikipedia.org/wiki/Subliminal_channel)
- [Encryption](//en.wikipedia.org/wiki/Encryption)
- [Decryption](//en.wikipedia.org/wiki/Decryption)
- [End-to-end encryption](//en.wikipedia.org/wiki/End-to-end_encryption)
- [Harvest now, decrypt later](//en.wikipedia.org/wiki/Harvest_now,_decrypt_later)
- [Information-theoretic security](//en.wikipedia.org/wiki/Information-theoretic_security)
- [Plaintext](//en.wikipedia.org/wiki/Plaintext)
- [Codetext](//en.wikipedia.org/wiki/Codetext)
- [Ciphertext](//en.wikipedia.org/wiki/Ciphertext)
- [Shared secret](//en.wikipedia.org/wiki/Shared_secret)
- [Trapdoor function](//en.wikipedia.org/wiki/Trapdoor_function)
- [Trusted timestamping](//en.wikipedia.org/wiki/Trusted_timestamping)
- [Key-based routing](//en.wikipedia.org/wiki/Key-based_routing)
- [Onion routing](//en.wikipedia.org/wiki/Onion_routing)
- [Garlic routing](//en.wikipedia.org/wiki/Garlic_routing)
- [Kademlia](//en.wikipedia.org/wiki/Kademlia)
- [Mix network](//en.wikipedia.org/wiki/Mix_network)


Mathematics
- [Cryptographic hash function](//en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Block cipher](//en.wikipedia.org/wiki/Block_cipher)
- [Stream cipher](//en.wikipedia.org/wiki/Stream_cipher)
- [Symmetric-key algorithm](//en.wikipedia.org/wiki/Symmetric-key_algorithm)
- [Authenticated encryption](//en.wikipedia.org/wiki/Authenticated_encryption)
- [Public-key cryptography](//en.wikipedia.org/wiki/Public-key_cryptography)
- [Quantum key distribution](//en.wikipedia.org/wiki/Quantum_key_distribution)
- [Quantum cryptography](//en.wikipedia.org/wiki/Quantum_cryptography)
- [Post-quantum cryptography](//en.wikipedia.org/wiki/Post-quantum_cryptography)
- [Message authentication code](//en.wikipedia.org/wiki/Message_authentication_code)
- [Random numbers](//en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator)
- [Steganography](//en.wikipedia.org/wiki/Steganography)



- ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png)

---

 [Category](//en.wikipedia.org/wiki/Category:Cryptography)



 
NewPP limit report
Parsed by mw‐api‐int.eqiad.main‐84b4c4f9fc‐94hpt
Cached time: 20260503041611
Cache expiry: 2592000
Cache expiry source: Module:Citation/CS1 (os.date(%Y))
Reduced expiry: false
Complications: [vary‐revision‐sha1, prevent‐selective‐update, show‐toc]
CPU time usage: 0.862 seconds
Real time usage: 1.194 seconds
Preprocessor visited node count: 6202/1000000
Revision size: 46984/2097152 bytes
Post‐expand include size: 154117/2097152 bytes
Template argument size: 10074/2097152 bytes
Highest expansion depth: 13/100
Expensive parser function count: 7/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 186215/5000000 bytes
Lua time usage: 0.454/10.000 seconds
Lua memory usage: 6248263/52428800 bytes
Number of Wikibase entities loaded: 0/500


Transclusion expansion time report (%,ms,calls,template)
100.00%  951.451      1 -total
 38.15%  363.020      2 Template:Reflist
 25.70%  244.514      4 Template:Navbox
 15.68%  149.157      4 Template:Cite_journal
 15.65%  148.882      1 Template:Cryptography_navbox
 13.15%  125.150      1 Template:Short_description
  8.63%   82.139      1 Template:Cryptography_public-key
  7.72%   73.412      2 Template:Pagetype
  6.56%   62.372      1 Template:Pp-pc
  6.20%   59.026      1 Template:Cn

 Render ID d1965309-46a6-11f1-8076-3dc37daffd0a 
 Saved in parser cache with key enwiki:pcache:7903:|#|:idhash:canonical and timestamp 20260503041611 and revision id 1352263080. Rendering was triggered because: api-parseSaved in parser cache with key enwiki:stable-pcache:7903:|#|:idhash:canonical and timestamp 20260503041611 and revision id 1352263080. Rendering was triggered because: unknown
 

Post‐processing cache key enwiki:stable‐pcache‐postproc:7903:|#|:idhash:injectTOC=0!postproc=1!skin=vector‐2022, generated at 20260503041644
![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

---


Retrieved from "[https://en.wikipedia.org/w/index.php?title=Diffie–Hellman_key_exchange&oldid=1352263080](https://en.wikipedia.org/w/index.php?title=Diffie–Hellman_key_exchange&oldid=1352263080)"
