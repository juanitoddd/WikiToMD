[![Alice signs a message—"Hello Bob!"—by appending a signature which is computed from the message and her private key. Bob receives the message, including the signature, and using Alice's public key, verifies the authenticity of the signed message.](https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Private_key_signing.svg/250px-Private_key_signing.svg.png)](/wiki/File:Private_key_signing.svg)Alice signs a message—"Hello Bob!"—by appending a signature which is computed from the message and her private key.  Bob receives both the message and signature. He uses Alice's public key to verify the authenticity of the signed message.

---


A **digital signature** is a [mathematical](/wiki/Mathematics) scheme for verifying the authenticity of digital messages or documents. A valid digital signature on a message gives a recipient confidence that the message came from a sender known to the recipient.[[1]](#cite_note-bellare-goldwasser2008digsigs-1)[[2]](#cite_note-katz-lindell2007digsigs-2)

Digital signatures are a type of [public-key cryptography](/wiki/Public-key_cryptography), and are commonly used for [software distribution](/wiki/Software_distribution),[[3]](#cite_note-boneh-shoup-3)[[4]](#cite_note-debian-package-signing-4)[[5]](#cite_note-apple-code-distribution-5)
financial transactions,[*[citation needed](/wiki/Wikipedia:Citation_needed)*] [contract management software](/wiki/Contract_management_software),[*[citation needed](/wiki/Wikipedia:Citation_needed)*] and in other cases where it is important to detect forgery or [tampering](/wiki/Tampering_(crime)).

A digital signature on a message or document is similar to a [handwritten signature](/wiki/Signature) on paper, but it is not restricted to a physical medium like paper—any [bitstring](/wiki/Bitstring) can be digitally signed—and while a handwritten signature on paper could be copied onto other paper in a [forgery](/wiki/Forgery), a digital signature on a message is mathematically bound to the *content* of the message so that it is infeasible for anyone to forge a valid digital signature on any other message.[[6]](#cite_note-stinson3e2006digsigs-6)

Digital signatures are often used to implement [electronic signatures](/wiki/Electronic_signature), which include any electronic data that carries the intent of a signature,[[7]](#cite_note-cEMCl-7) but not all electronic signatures use digital signatures.[[8]](#cite_note-6TaHP-8)[[9]](#cite_note-uExGJ-9)




## Definition


A digital signature scheme consists of three algorithms:[[6]](#cite_note-stinson3e2006digsigs-6)[[10]](#cite_note-galbraith2012mathpkcbook-kemdem-10)


- A **[key generation](/wiki/Key_generation)** algorithm that selects a **private key** at random from a set of possible private keys. The algorithm outputs the private key and a corresponding **public key**.
- A **signing** algorithm that, given a message and a private key, produces a signature.
- A **signature verifying** algorithm that, given the message, public key and signature, either accepts or rejects the message's claim to authenticity.


Two main properties are required:


1. *Correctness*:  Signatures produced by the signing algorithm with a private key pass the verification algorithm with the corresponding public key.
2. *Security* ([existential unforgeability under chosen-message attack](/wiki/Digital_signature_forgery), or EUF-CMA):  It should be computationally infeasible to generate a valid signature for a party without knowing that party's private key.


Formally, a digital signature scheme is a triple of [probabilistic polynomial-time](/wiki/Probabilistic_polynomial-time) algorithms, (*G*, *S*, *V*), satisfying:


- *G* (key-generator) generates a public key (*pk*), and a corresponding private key (*sk*), on input 1*n*, where *n* is the security parameter.
- *S* (signing) returns a tag, *t*, on the inputs: the private key (*sk*), and a string (*x*).
- *V* (verifying) outputs *accepted* or *rejected* on the inputs: the public key (*pk*), a string (*x*), and a tag (*t*).


Here 1*n* refers to a [unary number](/wiki/Unary_numeral_system) in the formalism of [computational complexity theory](/wiki/Computational_complexity_theory).

For *correctness*, *S* and *V* must satisfy


Pr [(*pk*, *sk*) ← *G*(1*n*), *V*(*pk*, *x*, *S*(*sk*, *x*)) = *accepted*] = 1.[[11]](#cite_note-IjhTrs-11)
A digital signature scheme is *secure* if for every non-uniform probabilistic polynomial time [adversary](/wiki/Adversary_(cryptography)) *A*,


Pr [(*pk*, *sk*) ← *G*(1*n*), (*x*, *t*) ← *A**S*(*sk*, · )(*pk*, 1*n*), *x* ∉ *Q*, *V*(*pk*, *x*, *t*) = *accepted*] < [negl](/wiki/Negligible_function)(*n*),
where *A**S*(*sk*, · ) denotes that *A* has access to the [oracle](/wiki/Oracle_machine), *S*(*sk*, · ), *Q* denotes the set of the queries on *S* made by *A*, which knows the public key, *pk*, and the security parameter, *n*, and *x* ∉ *Q* denotes that the adversary may not directly query the string, *x*, on *S*.[[11]](#cite_note-IjhTrs-11)[[12]](#cite_note-nOvvy-12)



## History


In 1976, [Whitfield Diffie](/wiki/Whitfield_Diffie) and [Martin Hellman](/wiki/Martin_Hellman) first described the notion of a digital signature scheme, although they only conjectured that such schemes existed based on functions that are trapdoor one-way permutations.[[13]](#cite_note-ikWoF-13)[[14]](#cite_note-lysythesis-14)  Soon afterwards, [Ronald Rivest](/wiki/Ronald_Rivest), [Adi Shamir](/wiki/Adi_Shamir), and [Len Adleman](/wiki/Len_Adleman) invented the [RSA](/wiki/RSA_(algorithm)) algorithm, which could be used to produce primitive digital signatures[[15]](#cite_note-rsa-15) (although only as a proof-of-concept – "plain" RSA signatures are not secure[[16]](#cite_note-7aSJZ-16)). The first widely marketed software package to offer digital signature was [Lotus Notes](/wiki/Lotus_Notes) 1.0, released in 1989, which used the RSA algorithm.[[17]](#cite_note-CKgyC-17)

Other digital signature schemes were soon developed after RSA, the earliest being [Lamport signatures](/wiki/Lamport_signature),[[18]](#cite_note-ejiWf-18) [Merkle signatures](/wiki/Merkle_signature_scheme) (also known as "Merkle trees" or simply "Hash trees"),[[19]](#cite_note-jl9LD-19) and [Rabin signatures](/wiki/Rabin_signature).[[20]](#cite_note-rabin1979lcs-tr-20)

In 1988, [Shafi Goldwasser](/wiki/Shafi_Goldwasser), [Silvio Micali](/wiki/Silvio_Micali), and [Ronald Rivest](/wiki/Ronald_Rivest) became the first to rigorously define the security requirements of digital signature schemes.[[21]](#cite_note-SJC_17(2)-21)
They described a hierarchy of attack models for signature schemes, and also presented the [GMR signature scheme](/wiki/GMR_(cryptography)), the first that could be proved to prevent even an existential forgery against a chosen message attack, which is the currently accepted security definition for signature schemes.[[21]](#cite_note-SJC_17(2)-21)  The first such scheme which is not built on trapdoor functions but rather on a family of function with a much weaker required property of one-way permutation was presented by [Moni Naor](/wiki/Moni_Naor) and [Moti Yung](/wiki/Moti_Yung).[[22]](#cite_note-Z2zaX-22)



## Method


[![icon](https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/60px-Question_book-new.svg.png)

---](/wiki/File:Question_book-new.svg)This Method section **needs additional citations for [verification](/wiki/Wikipedia:Verifiability)**. Please help [improve this article](/wiki/Special:EditPage/Digital_signature) by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners) in this Method section. Unsourced material may be challenged and removed.*Find sources:* ["Digital signature"](https://www.google.com/search?as_eq=wikipedia&q=%22Digital+signature%22) – [news](https://www.google.com/search?tbm=nws&q=%22Digital+signature%22+-wikipedia&tbs=ar:1) **·** [newspapers](https://www.google.com/search?&q=%22Digital+signature%22&tbs=bkt:s&tbm=bks) **·** [books](https://www.google.com/search?tbs=bks:1&q=%22Digital+signature%22+-wikipedia) **·** [scholar](https://scholar.google.com/scholar?q=%22Digital+signature%22) **·** [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Digital+signature%22&acc=on&wc=on) *(January 2022)**([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal))*
One digital signature scheme (of many) is based on [RSA](/wiki/RSA_(algorithm)). To create signature keys, generate an RSA key pair containing a modulus, *N*, that is the product of two random secret distinct large primes, along with integers, *e* and *d*, such that *e* *d* [≡](/wiki/Modular_arithmetic) 1 (mod *φ*(*N*)), where *φ* is [Euler's totient function](/wiki/Euler%27s_totient_function). The signer's public key consists of *N* and *e*, and the signer's secret key contains *d*.

Used directly, this type of signature scheme is vulnerable to key-only existential forgery attack. To create a forgery, the attacker picks a random signature σ and uses the verification procedure to determine the message, *m*, corresponding to that signature.[[23]](#cite_note-2Zzbo-23) In practice, however, this type of signature is not used directly, but rather, the message to be signed is first [hashed](/wiki/Cryptographic_hash_function) to produce a short digest, that is then [padded](/wiki/Padding_(cryptography)#Public_key_cryptography) to larger width comparable to *N*, then signed with the reverse [trapdoor function](/wiki/Trapdoor_function).[[24]](#cite_note-Jwm4G-24) This forgery attack, then, only produces the padded hash function output that corresponds to σ, but not a message that leads to that value, which does not lead to an attack. In the random oracle model, [hash-then-sign](/wiki/Full_domain_hash) (an idealized version of that practice where hash and padding combined have close to *N* possible outputs), this form of signature is existentially unforgeable, even against a [chosen-plaintext attack](/wiki/Chosen-plaintext_attack).[[14]](#cite_note-lysythesis-14)[[25]](#cite_note-25)[*[clarification needed](/wiki/Wikipedia:Please_clarify)*]

There are several reasons to sign such a hash (or message digest) instead of the whole document.


For efficiency
The signature will be much shorter and thus save time since hashing is generally much faster than signing in practice.
For compatibility
Messages are typically bit strings, but some signature schemes operate on other domains (such as, in the case of RSA, numbers modulo a composite number *N*). A hash function can be used to convert an arbitrary input into the proper format.
For integrity
Without the hash function, the text "to be signed" may have to be split (separated) in blocks small enough for the signature scheme to act on them directly. However, the receiver of the signed blocks is not able to recognize if all the blocks are present and in the appropriate order.

## Applications


As organizations move away from paper documents with ink signatures or authenticity stamps, digital signatures can provide added assurances of the evidence to provenance, identity, and status of an [electronic document](/wiki/Electronic_document) as well as acknowledging informed consent and approval by a signatory.[*[citation needed](/wiki/Wikipedia:Citation_needed)*]  The [United States Government Printing Office](/wiki/United_States_Government_Printing_Office) (GPO) publishes electronic versions of the budget, public and private laws, and congressional bills with digital signatures.[*[citation needed](/wiki/Wikipedia:Citation_needed)*][[26]](#cite_note-26)[*[failed verification](/wiki/Wikipedia:Verifiability)*]  Universities including [Penn State](/wiki/Penn_State), [University of Chicago](/wiki/University_of_Chicago), and [Stanford](/wiki/Stanford_University) are publishing electronic student transcripts with digital signatures.[*[citation needed](/wiki/Wikipedia:Citation_needed)*]

Below are some common reasons for applying a digital signature to communications:



### Authentication


A message may have letterhead or a handwritten signature identifying its sender, but letterheads and handwritten signatures can be copied and pasted onto forged messages.
Even legitimate messages may be modified in transit.[[6]](#cite_note-stinson3e2006digsigs-6)

If a bank's central office receives a letter claiming to be from a [branch office](/wiki/Branch_office) with instructions to change the balance of an account, the central bankers need to be sure, before acting on the instructions, that they were actually sent by a branch banker, and not forged—whether a forger fabricated the whole letter, or just modified an existing letter in transit by adding some digits.

With a digital signature scheme, the central office can arrange beforehand to have a public key on file whose private key is known only to the branch office.
The branch office can later sign a message and the central office can use the public key to verify the signed message was not a forgery before acting on it.
A forger who *doesn't* know the sender's private key can't sign a different message, or even change a single digit in an existing message without making the recipient's signature verification fail.[[6]](#cite_note-stinson3e2006digsigs-6)[[1]](#cite_note-bellare-goldwasser2008digsigs-1)[[2]](#cite_note-katz-lindell2007digsigs-2)

[Encryption](/wiki/Encryption) can hide the content of the message from an eavesdropper, but encryption on its own may not let recipient verify the message's authenticity, or even detect [selective modifications like changing a digit](/wiki/Malleability_(cryptography))—if the bank's offices simply encrypted the messages they exchange, they could still be vulnerable to forgery.
In other applications, such as software updates, the messages are not secret—when a software author publishes a patch for all existing installations of the software to apply, the patch itself is not secret, but computers running the software must verify the authenticity of the patch before applying it, lest they become victims to malware.[[2]](#cite_note-katz-lindell2007digsigs-2)



#### Limitations


**Replays.**
A digital signature scheme on its own does not prevent a valid signed message from being recorded and then maliciously reused in a [replay attack](/wiki/Replay_attack).
For example, the branch office may legitimately request that bank transfer be issued once in a signed message.
If the bank doesn't use a system of transaction IDs in their messages to detect which transfers have already happened, someone could illegitimately reuse the same signed message many times to drain an account.[[6]](#cite_note-stinson3e2006digsigs-6)

**Uniqueness and malleability of signatures.**
A signature itself cannot be used to uniquely identify the message it signs—in some signature schemes, every message has a large number of possible valid signatures from the same signer, and it may be easy, even without knowledge of the private key, to transform one valid signature into another.[[27]](#cite_note-bcjz2020ed25519sectheorypractice-27)
If signatures are misused as transaction IDs in an attempt by a bank-like system such as a [Bitcoin](/wiki/Bitcoin) exchange to detect replays, this can be exploited to replay transactions.[[28]](#cite_note-decker-wattenhofer2014btcmalleablemtgox-28)

**Authenticating a public key.**
Prior knowledge of a *public key* can be used to verify authenticity of a *signed message*, but not the other way around—prior knowledge of a *signed message* cannot be used to verify authenticity of a *public key*.
In some signature schemes, given a signed message, it is easy to construct a public key under which the signed message will pass verification, even without knowledge of the private key that was used to make the signed message in the first place.[[29]](#cite_note-ayer2015sigmisuseacme-29)



### Non-repudiation


[Non-repudiation](/wiki/Non-repudiation), or more specifically non-repudiation of origin, is an important aspect of digital signatures. By this property, an entity that has signed some information cannot at a later time deny having signed it. Similarly, access to the public key only does not enable a fraudulent party to fake a valid signature.

Note that these authentication, non-repudiation etc. properties rely on the secret key *not having been revoked* prior to its usage. Public [revocation](/wiki/Certificate_revocation) of a key-pair is a required ability, else leaked secret keys would continue to implicate the claimed owner of the key-pair. Checking revocation status requires an "online" check; e.g., checking a [certificate revocation list](/wiki/Certificate_revocation_list) or via the [Online Certificate Status Protocol](/wiki/Online_Certificate_Status_Protocol).[[30]](#cite_note-CryptomathicDigSigServicesAshiqJA-30)  Very roughly this is analogous to a vendor who receives credit-cards first checking online with the credit-card issuer to find if a given card has been reported lost or stolen. Of course, with stolen key pairs, the theft is often discovered only after the secret key's use, e.g., to sign a bogus certificate for espionage purpose.



## Notions of security


In their foundational paper, Goldwasser, Micali, and Rivest lay out a hierarchy of attack models against digital signatures:[[21]](#cite_note-SJC_17(2)-21)


1. In a *key-only* attack, the attacker is only given the public verification key.
2. In a *known message* attack, the attacker is given valid signatures for a variety of messages known by the attacker but not chosen by the attacker.
3. In an *adaptive chosen message* attack, the attacker first learns signatures on arbitrary messages of the attacker's choice.


They also describe a hierarchy of attack results:[[21]](#cite_note-SJC_17(2)-21)


1. A *total break* results in the recovery of the signing key.
2. A [universal forgery](/wiki/Universal_forgery) attack results in the ability to forge signatures for any message.
3. A [selective forgery](/wiki/Selective_forgery) attack results in a signature on a message of the adversary's choice.
4. An [existential forgery](/wiki/Existential_forgery) merely results in some valid message/signature pair not already known to the adversary.


The strongest notion of security, therefore, is security against existential forgery under an adaptive chosen message attack.



## Additional security precautions



### Putting the private key on a smart card


All public key / private key cryptosystems depend entirely on keeping the private key secret. A private key can be stored on a user's computer, and protected by a local password, but this has two disadvantages:


- the user can only sign documents on that particular computer
- the security of the private key depends entirely on the [security](/wiki/Computer_insecurity) of the computer


A more secure alternative is to store the private key on a [smart card](/wiki/Smart_card). Many smart cards are designed to be tamper-resistant (although some designs have been broken, notably by [Ross Anderson](/wiki/Ross_J._Anderson) and his students[[31]](#cite_note-jKyz7-31)). In a typical digital signature implementation, the hash calculated from the document is sent to the smart card, whose CPU signs the hash using the stored private key of the user, and then returns the signed hash. Typically, a user must activate their smart card by entering a [personal identification number](/wiki/Personal_identification_number) or PIN code (thus providing [two-factor authentication](/wiki/Two-factor_authentication)). It can be arranged that the private key never leaves the smart card, although this is not always implemented. If the smart card is stolen, the thief will still need the PIN code to generate a digital signature. This reduces the security of the scheme to that of the PIN system, although it still requires an attacker to possess the card. A mitigating factor is that private keys, if generated and stored on smart cards, are usually regarded as difficult to copy, and are assumed to exist in exactly one copy. Thus, the loss of the smart card may be detected by the owner and the corresponding certificate can be immediately revoked. Private keys that are protected by software only may be easier to copy, and such compromises are far more difficult to detect.



### Using smart card readers with a separate keyboard


Entering a PIN code to activate the smart card commonly requires a [numeric keypad](/wiki/Numeric_keypad). Some card readers have their own numeric keypad. This is safer than using a card reader integrated into a PC, and then entering the PIN using that computer's keyboard. Readers with a numeric keypad are meant to circumvent the eavesdropping threat where the computer might be running a [keystroke logger](/wiki/Keystroke_logging), potentially compromising the PIN code. Specialized card readers are also less vulnerable to tampering with their software or hardware and are often [EAL3](/wiki/Evaluation_Assurance_Level) certified.



### Other smart card designs


Smart card design is an active field, and there are smart card schemes which are intended to avoid these particular problems, despite having few security proofs so far.



### Using digital signatures only with trusted applications


One of the main differences between a digital signature and a written signature is that the user does not "see" what they sign. The user application presents a hash code to be signed by the digital signing algorithm using the private key. An attacker who gains control of the user's PC can possibly replace the user application with a foreign substitute, in effect replacing the user's own communications with those of the attacker. This could allow a malicious application to trick a user into signing any document by displaying the user's original on-screen, but presenting the attacker's own documents to the signing application.

To protect against this scenario, an authentication system can be set up between the user's application (word processor, email client, etc.) and the signing application. The general idea is to provide some means for both the user application and signing application to verify each other's integrity. For example, the signing application may require all requests to come from digitally signed binaries.



### Using a network attached hardware security module


One of the main differences between a [cloud](/wiki/Cloud_computing) based digital signature service and a locally provided one is risk.  Many risk averse companies, including governments, financial and medical institutions,  and payment processors require more secure standards, like [FIPS 140-2](/wiki/FIPS_140-2) level 3 and [FIPS 201](/wiki/FIPS_201) certification, to ensure the signature is validated and secure.



### WYSIWYS



Technically speaking, a digital signature applies to a string of bits, whereas humans and applications "believe" that they sign the semantic interpretation of those bits. In order to be semantically interpreted, the bit string must be transformed into a form that is meaningful for humans and applications, and this is done through a combination of hardware and software based processes on a computer system. The problem is that the semantic interpretation of bits can change as a function of the processes used to transform the bits into semantic content. It is relatively easy to change the interpretation of a digital document by implementing changes on the computer system where the document is being processed. From a semantic perspective this creates uncertainty about what exactly has been signed. [WYSIWYS](/wiki/WYSIWYS) (What You See Is What You Sign)[[32]](#cite_note-WYSIWYS_SeminalPaper-32) means that the semantic interpretation of a signed message cannot be changed. In particular this also means that a message cannot contain hidden information that the signer is unaware of, and that can be revealed after the signature has been applied. WYSIWYS is a requirement for the validity of digital signatures, but this requirement is difficult to guarantee because of the increasing complexity of modern computer systems. The term WYSIWYS was coined by [Peter Landrock](/wiki/Peter_Landrock) and [Torben Pedersen](/wiki/Cryptomathic) to describe some of the principles in delivering secure and legally binding digital signatures for Pan-European projects.[[32]](#cite_note-WYSIWYS_SeminalPaper-32)



### Digital signatures versus ink on paper signatures


An ink signature could be replicated from one document to another by copying the image manually or digitally, but to have credible signature copies that can resist some scrutiny is a significant manual or technical skill, and to produce ink signature copies that resist professional scrutiny is very difficult.

Digital signatures cryptographically bind an electronic identity to an electronic document and the digital signature cannot be copied to another document. Paper contracts sometimes have the ink signature block on the last page, and the previous pages may be replaced after a signature is applied.  Digital signatures can be applied to an entire document, such that the digital signature on the last page will indicate tampering if any data on any of the pages have been altered, but this can also be achieved by signing with ink and numbering all pages of the contract.



## Some digital signature algorithms


- [RSA](/wiki/RSA_(algorithm))
- [DSA](/wiki/Digital_Signature_Algorithm)
- [ECDSA](/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
- [EdDSA](/wiki/EdDSA)
- RSA with [SHA](/wiki/Secure_Hash_Algorithm)
- ECDSA with SHA[[33]](#cite_note-4zta8-33)
- [ElGamal signature scheme](/wiki/ElGamal_signature_scheme) as the predecessor to DSA, and variants [Schnorr signature](/wiki/Schnorr_signature) and [Pointcheval–Stern signature algorithm](/wiki/Pointcheval%E2%80%93Stern_signature_algorithm)
- [Rabin signature algorithm](/wiki/Rabin_signature_algorithm)
- [Pairing](/wiki/Pairing)-based schemes such as [BLS](/wiki/Boneh%E2%80%93Lynn%E2%80%93Shacham)
- CRYSTALS-Dilithium, a [quantum-resistant scheme](/wiki/Post-quantum_cryptography) based on [LWE](/wiki/Learning_with_errors) in [lattices](/wiki/Lattice-based_cryptography)
- [Falcon](/wiki/Falcon_(signature_scheme)), a [quantum-resistant scheme](/wiki/Post-quantum_cryptography) based on [CVP](/wiki/Closest_vector_problem) in [lattices](/wiki/Lattice-based_cryptography)
- [SPHINCS+](/wiki/SPHINCS%2B), a [quantum-resistant scheme](/wiki/Post-quantum_cryptography) based on [hash functions](/wiki/Hash_function)
- [Undeniable signatures](/wiki/Undeniable_signature)
- [Aggregate signature](/w/index.php?title=Aggregate_signature&action=edit&redlink=1) [[ru](https://ru.wikipedia.org/wiki/%D0%9C%D0%BD%D0%BE%D0%B6%D0%B5%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%8C)] – a signature scheme that supports aggregation: Given n signatures on n messages from n users, it is possible to aggregate all these signatures into a single signature whose size is constant in the number of users. This single signature will convince the verifier that the n users did indeed sign the n original messages. A scheme by [Mihir Bellare](/wiki/Mihir_Bellare) and [Gregory Neven](/w/index.php?title=Gregory_Neven&action=edit&redlink=1) may be used with [Bitcoin](/wiki/Bitcoin).[[34]](#cite_note-DdBGf-34)
- [Signatures with efficient protocols](/wiki/Signatures_with_efficient_protocols) – are signature schemes that facilitate efficient cryptographic protocols such as [zero-knowledge proofs](/wiki/Zero-knowledge_proofs) or [secure computation](/wiki/Secure_computation).



## The current state of use – legal and practical



Most digital signature schemes share the following goals regardless of cryptographic theory or legal provision:


1. Quality algorithms: Some public-key algorithms are known to be insecure, as practical attacks against them have been discovered.
2. 
3. Quality implementations: An implementation of a good algorithm (or [protocol](/wiki/Cryptographic_protocol)) with mistake(s) will not work.
4. 
5. Users (and their software) must carry out the signature protocol properly.
6. 
7. The private key must remain private: If the private key becomes known to any other party, that party can produce *perfect* digital signatures of anything.
8. 
9. The public key owner must be verifiable: A public key associated with Bob actually came from Bob. This is commonly done using a [public key infrastructure](/wiki/Public_key_infrastructure) (PKI) and the public key↔user association is attested by the operator of the PKI (called a [certificate authority](/wiki/Certificate_authority)). For 'open' PKIs in which anyone can request such an attestation (universally embodied in a cryptographically protected [public key certificate](/wiki/Public_key_certificate)), the possibility of mistaken attestation is non-trivial. Commercial PKI operators have suffered several publicly known problems. Such mistakes could lead to falsely signed, and thus wrongly attributed, documents. 'Closed' PKI systems are more expensive, but less easily subverted in this way.


Only if all of these conditions are met will a digital signature actually be any evidence of who sent the message, and therefore of their assent to its contents. Legal enactment cannot change this reality of the existing engineering possibilities, though some such have not reflected this actuality.

Legislatures, being importuned by businesses expecting to profit from operating a PKI, or by the technological avant-garde advocating new solutions to old problems, have enacted statutes and/or regulations in many jurisdictions authorizing, endorsing, encouraging, or permitting digital signatures and providing for (or limiting) their legal effect. The first appears to have been in [Utah](/wiki/Utah) in the United States, followed closely by the states [Massachusetts](/wiki/Massachusetts) and [California](/wiki/California). Other countries have also passed statutes or issued regulations in this area as well and the UN has had an active model law project for some time. These enactments (or proposed enactments) vary from place to place, have typically embodied expectations at variance (optimistically or pessimistically) with the state of the underlying cryptographic engineering, and have had the net effect of confusing potential users and specifiers, nearly all of whom are not cryptographically knowledgeable.

Adoption of technical standards for digital signatures have lagged behind much of the legislation, delaying a more or less unified engineering position on [interoperability](/wiki/Interoperability), [algorithm](/wiki/Algorithm) choice, [key lengths](/wiki/Key_length), and so on what the engineering is attempting to provide.




## Industry standards


[![icon](https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/60px-Question_book-new.svg.png)

---](/wiki/File:Question_book-new.svg)This section **does not [cite](/wiki/Wikipedia:Citing_sources) any [sources](/wiki/Wikipedia:Verifiability)**. Please help [improve this section](/wiki/Special:EditPage/Digital_signature) by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners). Unsourced material may be challenged and [removed](/wiki/Wikipedia:Verifiability#Burden_of_evidence). *(January 2015)**([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal))*
Some industries have established common interoperability standards for the use of digital signatures between members of the industry and with regulators.  These include the [Automotive Network Exchange](/wiki/Automotive_Network_Exchange) for the automobile industry and the SAFE-BioPharma Association for the [healthcare industry](/wiki/Healthcare_industry).



### Using separate key pairs for signing and encryption


In several countries, a digital signature has a status somewhat like that of a traditional pen and paper signature, as in the
[1999 EU digital signature directive](/wiki/Electronic_Signatures_Directive) and [2014 EU follow-on legislation](/wiki/EIDAS).[[35]](#cite_note-Cryptomathic_MajorStandardsDigSig-35) Generally, these provisions mean that anything digitally signed legally binds the signer of the document to the terms therein. For that reason, it is often thought best to use separate key pairs for encrypting and signing. Using the encryption key pair, a person can engage in an encrypted conversation (e.g., regarding a real estate transaction), but the encryption does not legally sign every message he or she sends. Only when both parties come to an agreement do they sign a contract with their signing keys, and only then are they legally bound by the terms of a specific document. After signing, the document can be sent over the encrypted link.  If a signing key is lost or compromised, it can be revoked to mitigate any future transactions.  If an encryption key is lost, a backup or [key escrow](/wiki/Key_escrow) should be utilized to continue viewing encrypted content.  Signing keys should never be backed up or escrowed unless the backup destination is securely encrypted.



## See also




[![Wikiversity logo](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Wikiversity_logo_2017.svg/40px-Wikiversity_logo_2017.svg.png)

---](/wiki/File:Wikiversity_logo_2017.svg)
Wikiversity has learning resources about ***[Digital Signature](https://en.wikiversity.org/wiki/Digital_Signature)***

- [21 CFR 11](/wiki/21_CFR_11)
- [X.509](/wiki/X.509)
- [Advanced electronic signature](/wiki/Advanced_electronic_signature)
- [Blind signature](/wiki/Blind_signature)
- [Detached signature](/wiki/Detached_signature)
- [Public key certificate](/wiki/Public_key_certificate)
- [Digital signature in Estonia](/wiki/Digital_signature_in_Estonia)
- [Electronic lab notebook](/wiki/Electronic_lab_notebook)
- [Electronic signature](/wiki/Electronic_signature)
- [Electronic signatures and law](/wiki/Electronic_signatures_and_law)
- [eSign (India)](/wiki/ESign_(India))
- [GNU Privacy Guard](/wiki/GNU_Privacy_Guard)
- [Public key infrastructure](/wiki/Public_key_infrastructure)
- [Public key fingerprint](/wiki/Public_key_fingerprint)
- [Server-based signatures](/wiki/Server-based_signatures)
- [Probabilistic signature scheme](/wiki/Probabilistic_signature_scheme)



## Notes



1. ^ [***a***](#cite_ref-bellare-goldwasser2008digsigs_1-0) [***b***](#cite_ref-bellare-goldwasser2008digsigs_1-1) [Goldwasser, Shafi](/wiki/Shafi_Goldwasser); [Bellare, Mihir](/wiki/Mihir_Bellare) (July 2008). ["Chapter 10: Digital signatures"](https://cseweb.ucsd.edu/~mihir/papers/gb.pdf#page=168) (PDF). *Lecture Notes on Cryptography*. p. 168. [Archived](https://web.archive.org/web/20220420003617/https://cseweb.ucsd.edu/~mihir/papers/gb.pdf#page=168) (PDF) from the original on 2022-04-20. Retrieved 2023-06-11.
2. ^ [***a***](#cite_ref-katz-lindell2007digsigs_2-0) [***b***](#cite_ref-katz-lindell2007digsigs_2-1) [***c***](#cite_ref-katz-lindell2007digsigs_2-2) [Katz, Jonathan](/wiki/Jonathan_Katz_(computer_scientist)); [Lindell, Yehuda](/wiki/Yehuda_Lindell) (2007). "Chapter 12: Digital Signature Schemes". *Introduction to Modern Cryptography*. p. 399.
3. **[^](#cite_ref-boneh-shoup_3-0)** [Boneh, Dan](/wiki/Dan_Boneh); [Shoup, Victor](/wiki/Victor_Shoup) (January 2023). "13. Digital Signatures". [*A Graduate Course in Applied Cryptography*](https://toc.cryptobook.us/book.pdf#page=542) (PDF) (Version 0.6 ed.).
4. **[^](#cite_ref-debian-package-signing_4-0)** ["§ 7.5. Package signing in Debian"](https://web.archive.org/web/20250611053211/https://www.debian.org/doc/manuals/securing-debian-manual/deb-pack-sign.en.html). *Securing Debian Manual*. Debian Project. Archived from [the original](https://www.debian.org/doc/manuals/securing-debian-manual/deb-pack-sign.en.html) on 2025-06-11. Retrieved 2025-07-17.
5. **[^](#cite_ref-apple-code-distribution_5-0)** ["Distributing your app to registered devices"](https://web.archive.org/web/20240313192757/https://developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices). *Apple Developer Documentation*. Apple, Inc. Archived from [the original](https://docs.developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices) on 2024-03-13. Retrieved 2025-07-17.
6. ^ [***a***](#cite_ref-stinson3e2006digsigs_6-0) [***b***](#cite_ref-stinson3e2006digsigs_6-1) [***c***](#cite_ref-stinson3e2006digsigs_6-2) [***d***](#cite_ref-stinson3e2006digsigs_6-3) [***e***](#cite_ref-stinson3e2006digsigs_6-4) 
[Stinson, Douglas](/wiki/Doug_Stinson) (2006). "7: Signature Schemes". *Cryptography: Theory and Practice* (3rd ed.). Chapman & Hall/CRC. p. 281. [ISBN](/wiki/ISBN_(identifier)) [978-1-58488-508-5](/wiki/Special:BookSources/978-1-58488-508-5).
7. **[^](#cite_ref-cEMCl_7-0)** ["US ESIGN Act of 2000"](http://frwebgate.access.gpo.gov/cgi-bin/getdoc.cgi?dbname=106_cong_public_laws&docid=f:publ229.106.pdf) (PDF). [Archived](https://web.archive.org/web/20110522212411/http://frwebgate.access.gpo.gov/cgi-bin/getdoc.cgi?dbname=106_cong_public_laws&docid=f:publ229.106.pdf) (PDF) from the original on 2011-05-22. Retrieved 2006-05-10.
8. **[^](#cite_ref-6TaHP_8-0)** [State of WI](http://enterprise.state.wi.us/home/strategic/esig.htm) [Archived](https://web.archive.org/web/20060925104000/http://enterprise.state.wi.us/home/strategic/esig.htm) 2006-09-25 at the [Wayback Machine](/wiki/Wayback_Machine)
9. **[^](#cite_ref-uExGJ_9-0)** [National Archives of Australia](http://www.naa.gov.au/recordkeeping/er/Security/6-glossary.html) [Archived](https://web.archive.org/web/20141109180215/http://www.naa.gov.au/recordkeeping/er/Security/6-glossary.html) November 9, 2014, at the [Wayback Machine](/wiki/Wayback_Machine)
10. **[^](#cite_ref-galbraith2012mathpkcbook-kemdem_10-0)** Galbraith, Steven (2012). ["§1.3.2: Security of signatures"](https://ia600600.us.archive.org/7/items/mathematics_202103/Steven.D.Galbraith.Mathematics.of.Public.Key.Cryptography.2012.pdf#page=23) (PDF). *Mathematics of Public-Key Cryptography*. Cambridge University Press. pp. 7–9. [ISBN](/wiki/ISBN_(identifier)) [978-1-107-01392-6](/wiki/Special:BookSources/978-1-107-01392-6).
11. ^ [***a***](#cite_ref-IjhTrs_11-0) [***b***](#cite_ref-IjhTrs_11-1) Pass, def 135.1
12. **[^](#cite_ref-nOvvy_12-0)** Goldreich's FoC, vol. 2, def 6.1.2. Pass, def 135.2
13. **[^](#cite_ref-ikWoF_13-0)** Diffie, W.; Hellman, M. (1976). ["New directions in cryptography"](https://www-ee.stanford.edu/~hellman/publications/24.pdf) (PDF). *IEEE Transactions on Information Theory*. **22** (6): 644–654. [Bibcode](/wiki/Bibcode_(identifier)):[1976ITIT...22..644D](https://ui.adsabs.harvard.edu/abs/1976ITIT...22..644D). [doi](/wiki/Doi_(identifier)):[10.1109/TIT.1976.1055638](https://doi.org/10.1109%2FTIT.1976.1055638).
14. ^ [***a***](#cite_ref-lysythesis_14-0) [***b***](#cite_ref-lysythesis_14-1) "[Signature Schemes and Applications to Cryptographic Protocol Design](https://dspace.mit.edu/handle/1721.1/29271) [Archived](https://web.archive.org/web/20220908083823/https://dspace.mit.edu/handle/1721.1/29271) 2022-09-08 at the [Wayback Machine](/wiki/Wayback_Machine)", [Anna Lysyanskaya](/wiki/Anna_Lysyanskaya), PhD thesis, [MIT](/wiki/Massachusetts_Institute_of_Technology), 2002.
15. **[^](#cite_ref-rsa_15-0)** Rivest, R.; Shamir, A.; Adleman, L. (1978). ["A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"](https://web.archive.org/web/20081217101831/http://people.csail.mit.edu/rivest/Rsapaper.pdf) (PDF). *Communications of the ACM*. **21** (2): 120–126. [CiteSeerX](/wiki/CiteSeerX_(identifier)) [10.1.1.607.2677](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.607.2677). [doi](/wiki/Doi_(identifier)):[10.1145/359340.359342](https://doi.org/10.1145%2F359340.359342). [S2CID](/wiki/S2CID_(identifier)) [2873616](https://api.semanticscholar.org/CorpusID:2873616). Archived from [the original](https://people.csail.mit.edu/rivest/Rsapaper.pdf) (PDF) on 2008-12-17. Retrieved 2025-07-02.
16. **[^](#cite_ref-7aSJZ_16-0)** For example any integer, *r*, "signs" *m*=*r**e* and the product, *s*1*s*2, of any two valid signatures, *s*1, *s*2 of *m*1, *m*2 is a valid signature of the product, *m*1*m*2.
17. **[^](#cite_ref-CKgyC_17-0)** ["The History of Notes and Domino"](http://www.ibm.com/developerworks/lotus/library/ls-NDHistory/). *developerWorks*. 2007-11-14. [Archived](https://web.archive.org/web/20130305042623/http://www.ibm.com/developerworks/lotus/library/ls-NDHistory/) from the original on 2013-03-05. Retrieved 17 September 2014.
18. **[^](#cite_ref-ejiWf_18-0)** "Constructing digital signatures from a one-way function.", [Leslie Lamport](/wiki/Leslie_Lamport), Technical Report CSL-98, SRI International, Oct. 1979.
19. **[^](#cite_ref-jl9LD_19-0)** 
Merkle, Ralph C. (1990). ["A Certified Digital Signature"](https://link.springer.com/content/pdf/10.1007/0-387-34805-0_21.pdf) (PDF). *Advances in Cryptology — CRYPTO' 89 Proceedings*. Lecture Notes in Computer Science. Vol. 435. pp. 218–238. [doi](/wiki/Doi_(identifier)):[10.1007/0-387-34805-0_21](https://doi.org/10.1007%2F0-387-34805-0_21). [ISBN](/wiki/ISBN_(identifier)) [978-0-387-97317-3](/wiki/Special:BookSources/978-0-387-97317-3).
20. **[^](#cite_ref-rabin1979lcs-tr_20-0)** [Rabin, Michael O.](/wiki/Michael_O._Rabin) (January 1979). [*Digitalized Signatures and Public Key Functions as Intractable as Factorization*](http://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TR-212.pdf) (PDF) (Technical report). Cambridge, MA, United States: MIT Laboratory for Computer Science. TR-212.
21. ^ [***a***](#cite_ref-SJC_17(2)_21-0) [***b***](#cite_ref-SJC_17(2)_21-1) [***c***](#cite_ref-SJC_17(2)_21-2) [***d***](#cite_ref-SJC_17(2)_21-3) 
[Goldwasser, Shafi](/wiki/Shafi_Goldwasser); [Micali, Silvio](/wiki/Silvio_Micali); [Rivest, Ronald L.](/wiki/Ron_Rivest) (1988). ["A Digital Signature Scheme Secure Against Adaptive Chosen-Message Attacks"](https://web.archive.org/web/20240918024817/https://cr.yp.to/bib/1988/goldwasser.pdf) (PDF). *[SIAM Journal on Computing](/wiki/SIAM_Journal_on_Computing)*. **17** (2): 281–308. [doi](/wiki/Doi_(identifier)):[10.1137/0217017](https://doi.org/10.1137%2F0217017). Archived from [the original](https://cr.yp.to/bib/1988/goldwasser.pdf) (PDF) on 2024-09-18.
22. **[^](#cite_ref-Z2zaX_22-0)** 
[Naor, Moni](/wiki/Moni_Naor); [Yung, Moti](/wiki/Moti_Yung) (1989). "Universal one-way hash functions and their cryptographic applications". *Proceedings of the twenty-first annual ACM symposium on Theory of computing - STOC '89*. [ACM](/wiki/Association_for_Computing_Machinery). pp. 33–43. [doi](/wiki/Doi_(identifier)):[10.1145/73007.73011](https://doi.org/10.1145%2F73007.73011). [ISBN](/wiki/ISBN_(identifier)) [978-0-89791-307-2](/wiki/Special:BookSources/978-0-89791-307-2).
23. **[^](#cite_ref-2Zzbo_23-0)** "Modern Cryptography: Theory & Practice", Wenbo Mao, Prentice Hall Professional Technical Reference, New Jersey, 2004, pg. 308. [ISBN](/wiki/ISBN_(identifier)) [0-13-066943-1](/wiki/Special:BookSources/0-13-066943-1)
24. **[^](#cite_ref-Jwm4G_24-0)** Handbook of Applied Cryptography by Alfred J. Menezes, Paul C. van Oorschot, Scott A. Vanstone. Fifth Printing (August 2001) page 445.
25. **[^](#cite_ref-25)** 
[Bellare, Mihir](/wiki/Mihir_Bellare); [Rogaway, Phillip](/wiki/Phillip_Rogaway) (1996). "The Exact Security of Digital Signatures-How to Sign with RSA and Rabin". In [Maurer, Ueli](/wiki/Ueli_Maurer_(cryptographer)) (ed.). *Advances in Cryptology — EUROCRYPT '96*. Lecture Notes in Computer Science. Vol. 1070. Berlin, Heidelberg: Springer. pp. 399–416. [doi](/wiki/Doi_(identifier)):[10.1007/3-540-68339-9_34](https://doi.org/10.1007%2F3-540-68339-9_34). [ISBN](/wiki/ISBN_(identifier)) [978-3-540-68339-1](/wiki/Special:BookSources/978-3-540-68339-1).
26. **[^](#cite_ref-26)** ["FY2018 Performance and Accountability Report"](https://www.gpo.gov/docs/default-source/mission-vision-and-goals-pdfs/fy18-and-fy16-performance-report.pdf) (PDF). United States Government Publising Office. 2018. Retrieved 2026-03-23.
27. **[^](#cite_ref-bcjz2020ed25519sectheorypractice_27-0)** 
Brendel, Jacqueline; Cremers, Cas; Jackson, Dennis; Zhao, Meng (2020-10-14). [*The Provable Security of Ed25519: Theory and Practice*](https://eprint.iacr.org/2020/823) (Technical report). IACR Cryptology ePrint Archive. 2020/823.
28. **[^](#cite_ref-decker-wattenhofer2014btcmalleablemtgox_28-0)** 
Decker, Christian; Wattenhofer, Roger (2014). "Bitcoin Transaction Malleability and MtGox". In Kutyłowski, Mirosław; Vaidya, Jaideep (eds.). *Computer Security - ESORICS 2014*. Lecture Notes in Computer Science. Vol. 8713. Springer. pp. 313–326. [arXiv](/wiki/ArXiv_(identifier)):[1403.6676](https://arxiv.org/abs/1403.6676). [doi](/wiki/Doi_(identifier)):[10.1007/978-3-319-11212-1_18](https://doi.org/10.1007%2F978-3-319-11212-1_18). [ISBN](/wiki/ISBN_(identifier)) [978-3-319-11212-1](/wiki/Special:BookSources/978-3-319-11212-1).
29. **[^](#cite_ref-ayer2015sigmisuseacme_29-0)** Ayer, Andrew (2015-08-11). ["Signature misuse vulnerability in draft-barnes-acme-04"](https://mailarchive.ietf.org/arch/msg/acme/F71iz6qq1o_QPVhJCV4dqWf-4Yc/). *acme@ietf.org* (Mailing list). Retrieved 2023-06-12.
30. **[^](#cite_ref-CryptomathicDigSigServicesAshiqJA_30-0)** JA, Ashiq. ["Recommendations for Providing Digital Signature Services"](http://www.cryptomathic.com/news-events/blog/recommendations-for-providing-digital-signature-services). Cryptomathic. [Archived](https://web.archive.org/web/20160209203856/http://www.cryptomathic.com/news-events/blog/recommendations-for-providing-digital-signature-services) from the original on 9 February 2016. Retrieved 7 January 2016.
31. **[^](#cite_ref-jKyz7_31-0)** ["Chip and Skim: cloning EMV cards with the pre-play attack"](https://web.archive.org/web/20180516203624/http://sec.cs.ucl.ac.uk/users/smurdoch/papers/oakland14chipandskim.pdf) (PDF). Archived from [the original](http://sec.cs.ucl.ac.uk/users/smurdoch/papers/oakland14chipandskim.pdf) (PDF) on 2018-05-16. Retrieved 2018-04-06.
32. ^ [***a***](#cite_ref-WYSIWYS_SeminalPaper_32-0) [***b***](#cite_ref-WYSIWYS_SeminalPaper_32-1) Landrock, Peter; Pedersen, Torben (1998). "WYSIWYS? – What you see is what you sign?". *Information Security Technical Report*. **3** (2): 55–61. [doi](/wiki/Doi_(identifier)):[10.1016/S0167-4048(98)80005-8](https://doi.org/10.1016%2FS0167-4048%2898%2980005-8).
33. **[^](#cite_ref-4zta8_33-0)** RFC 5758
34. **[^](#cite_ref-DdBGf_34-0)** ["Technology roadmap – Schnorr signatures and signature aggregation"](https://bitcoincore.org/en/2017/03/23/schnorr-signature-aggregation/). *bitcoincore.org*. Bitcoin Core. 23 March 2017. [Archived](https://web.archive.org/web/20180324211259/https://bitcoincore.org/en/2017/03/23/schnorr-signature-aggregation/) from the original on 24 March 2018. Retrieved 1 April 2018.
35. **[^](#cite_ref-Cryptomathic_MajorStandardsDigSig_35-0)** Turner, Dawn. ["Major Standards and Compliance of Digital Signatures – A World-Wide Consideration"](http://www.cryptomathic.com/news-events/blog/major-standards-and-compliance-of-digital-signatures-a-world-wide-consideration). Cryptomathic. [Archived](https://web.archive.org/web/20160209203857/http://www.cryptomathic.com/news-events/blog/major-standards-and-compliance-of-digital-signatures-a-world-wide-consideration) from the original on 9 February 2016. Retrieved 7 January 2016.



## References


- Goldreich, Oded (2001), *Foundations of cryptography I: Basic Tools*, Cambridge: Cambridge University Press, [ISBN](/wiki/ISBN_(identifier)) [978-0-511-54689-1](/wiki/Special:BookSources/978-0-511-54689-1)
- Goldreich, Oded (2004), *Foundations of cryptography II: Basic Applications* (1. publ. ed.), Cambridge [u.a.]: Cambridge Univ. Press, [ISBN](/wiki/ISBN_(identifier)) [978-0-521-83084-3](/wiki/Special:BookSources/978-0-521-83084-3)
- Pass, Rafael, [*A Course in Cryptography*](https://www.cs.cornell.edu/courses/cs4830/2010fa/lecnotes.pdf) (PDF), retrieved 31 December 2015



## Further reading


- J. Katz and Y. Lindell, "Introduction to Modern Cryptography" (Chapman & Hall/CRC Press, 2007)
- Lorna Brazell, Electronic Signatures and Identities Law and Regulation (2nd edn, London: Sweet & Maxwell, 2008)
- Dennis Campbell, editor, E-Commerce and the Law of Digital Signatures (Oceana Publications, 2005)
- M. H. M Schellenkens, Electronic Signatures Authentication Technology from a Legal Perspective, (TMC Asser Press, 2004)
- Jeremiah S. Buckley, John P. Kromer, Margo H. K. Tank, and R. David Whitaker, The Law of Electronic Signatures (3rd Edition, West Publishing, 2010).
- [*Digital Evidence and Electronic Signature Law Review*](http://journals.sas.ac.uk/deeslr/) Free open source


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


[Discrete logarithm](/wiki/Discrete_logarithm)
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
- [Discrete logarithm cryptography](/wiki/Discrete_logarithm#Cryptography)
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
- Digital signature
- [OAEP](/wiki/Optimal_asymmetric_encryption_padding)
- [Fingerprint](/wiki/Public_key_fingerprint)
- [PKI](/wiki/Public_key_infrastructure)
- [Web of trust](/wiki/Web_of_trust)
- [Key size](/wiki/Key_size)
- [Identity-based cryptography](/wiki/Identity-based_cryptography)
- [Post-quantum cryptography](/wiki/Post-quantum_cryptography)
- [OpenPGP card](/wiki/OpenPGP_card)


- [v](/wiki/Template:Cryptography)
- [t](/wiki/Template_talk:Cryptography)
- [e](/wiki/Special:EditPage/Template:Cryptography)

[Cryptography](/wiki/Cryptography)General
- [History of cryptography](/wiki/History_of_cryptography)
- [Outline of cryptography](/wiki/Outline_of_cryptography)
- [Classical cipher](/wiki/Classical_cipher)
- [Cryptographic protocol](/wiki/Cryptographic_protocol)
- [Authentication protocol](/wiki/Authentication_protocol)
- [Cryptographic primitive](/wiki/Cryptographic_primitive)
- [Cryptanalysis](/wiki/Cryptanalysis)
- [Cryptocurrency](/wiki/Cryptocurrency)
- [Cryptosystem](/wiki/Cryptosystem)
- [Cryptographic nonce](/wiki/Cryptographic_nonce)
- [Cryptovirology](/wiki/Cryptovirology)
- [Hash function](/wiki/Hash_function)
- [Cryptographic hash function](/wiki/Cryptographic_hash_function)
- [Key derivation function](/wiki/Key_derivation_function)
- [Secure Hash Algorithms](/wiki/Secure_Hash_Algorithms)
- Digital signature
- [Kleptography](/wiki/Kleptography)
- [Key (cryptography)](/wiki/Key_(cryptography))
- [Key exchange](/wiki/Key_exchange)
- [Key generator](/wiki/Key_generator)
- [Key schedule](/wiki/Key_schedule)
- [Key stretching](/wiki/Key_stretching)
- [Keygen](/wiki/Keygen)
- [Machines](/wiki/Template:Cryptography_machines)
- [Ransomware](/wiki/Ransomware)
- [Random number generation](/wiki/Random_number_generation)
- [Cryptographically secure pseudorandom number generator](/wiki/Cryptographically_secure_pseudorandom_number_generator) (CSPRNG)
- [Pseudorandom noise](/wiki/Pseudorandom_noise) (PRN)
- [Secure channel](/wiki/Secure_channel)
- [Insecure channel](/wiki/Insecure_channel)
- [Subliminal channel](/wiki/Subliminal_channel)
- [Encryption](/wiki/Encryption)
- [Decryption](/wiki/Decryption)
- [End-to-end encryption](/wiki/End-to-end_encryption)
- [Harvest now, decrypt later](/wiki/Harvest_now,_decrypt_later)
- [Information-theoretic security](/wiki/Information-theoretic_security)
- [Plaintext](/wiki/Plaintext)
- [Codetext](/wiki/Codetext)
- [Ciphertext](/wiki/Ciphertext)
- [Shared secret](/wiki/Shared_secret)
- [Trapdoor function](/wiki/Trapdoor_function)
- [Trusted timestamping](/wiki/Trusted_timestamping)
- [Key-based routing](/wiki/Key-based_routing)
- [Onion routing](/wiki/Onion_routing)
- [Garlic routing](/wiki/Garlic_routing)
- [Kademlia](/wiki/Kademlia)
- [Mix network](/wiki/Mix_network)


Mathematics
- [Cryptographic hash function](/wiki/Cryptographic_hash_function)
- [Block cipher](/wiki/Block_cipher)
- [Stream cipher](/wiki/Stream_cipher)
- [Symmetric-key algorithm](/wiki/Symmetric-key_algorithm)
- [Authenticated encryption](/wiki/Authenticated_encryption)
- [Public-key cryptography](/wiki/Public-key_cryptography)
- [Quantum key distribution](/wiki/Quantum_key_distribution)
- [Quantum cryptography](/wiki/Quantum_cryptography)
- [Post-quantum cryptography](/wiki/Post-quantum_cryptography)
- [Message authentication code](/wiki/Message_authentication_code)
- [Random numbers](/wiki/Cryptographically_secure_pseudorandom_number_generator)
- [Steganography](/wiki/Steganography)



- ![](https://upload.wikimedia.org/wikipedia/en/thumb/9/96/Symbol_category_class.svg/20px-Symbol_category_class.svg.png)

---

 [Category](/wiki/Category:Cryptography)



[Authority control databases](/wiki/Help:Authority_control) [![Edit this at Wikidata](https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png)

---](https://www.wikidata.org/wiki/Q220849#identifiers)National- [United States](https://id.loc.gov/authorities/sh00007219)
- [Israel](https://www.nli.org.il/en/authorities/987007286475805171)

Other- [Yale LUX](https://lux.collections.yale.edu/view/concept/d246e56d-ee66-4e31-8d11-03d578f14969)


 
NewPP limit report
Parsed by mw‐api‐int.eqiad.main‐bd466b4d5‐rkz5n
Cached time: 20260504135430
Cache expiry: 2592000
Cache expiry source: Module:Citation/CS1 (os.date(%Y))
Reduced expiry: false
Complications: [vary‐revision‐sha1, prevent‐selective‐update, show‐toc]
CPU time usage: 0.712 seconds
Real time usage: 0.929 seconds
Preprocessor visited node count: 3644/1000000
Revision size: 43260/2097152 bytes
Post‐expand include size: 167528/2097152 bytes
Template argument size: 5914/2097152 bytes
Highest expansion depth: 13/100
Expensive parser function count: 10/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 132934/5000000 bytes
Lua time usage: 0.445/10.000 seconds
Lua memory usage: 8139320/52428800 bytes
Number of Wikibase entities loaded: 1/500


Transclusion expansion time report (%,ms,calls,template)
100.00%  792.014      1 -total
 33.31%  263.837      1 Template:Reflist
 19.53%  154.643      4 Template:Navbox
 17.11%  135.526      9 Template:Cite_book
 12.01%   95.120      1 Template:Cryptography_navbox
  9.99%   79.122      1 Template:Short_description
  9.18%   72.676      5 Template:Cn
  9.12%   72.223      1 Template:Authority_control
  9.01%   71.357      6 Template:Fix
  5.95%   47.149      1 Template:Cryptography_public-key

 Render ID c59eb2d9-47c0-11f1-ad24-d5899dcacb1d 
 Saved in parser cache with key enwiki:pcache:59644:|#|:idhash:canonical and timestamp 20260504135430 and revision id 1352486526. Rendering was triggered because: api-parse
 
![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

---


Retrieved from "[https://en.wikipedia.org/w/index.php?title=Digital_signature&oldid=1352486526](https://en.wikipedia.org/w/index.php?title=Digital_signature&oldid=1352486526)"
