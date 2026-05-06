[![icon](https://upload.wikimedia.org/wikipedia/en/thumb/9/99/Question_book-new.svg/60px-Question_book-new.svg.png)

---](/wiki/File:Question_book-new.svg)This article **needs additional citations for [verification](/wiki/Wikipedia:Verifiability)**. Please help [improve this article](/wiki/Special:EditPage/Public-key_cryptography) by [adding citations to reliable sources](/wiki/Help:Referencing_for_beginners). Unsourced material may be challenged and removed.*Find sources:* ["Public-key cryptography"](https://www.google.com/search?as_eq=wikipedia&q=%22Public-key+cryptography%22) – [news](https://www.google.com/search?tbm=nws&q=%22Public-key+cryptography%22+-wikipedia&tbs=ar:1) **·** [newspapers](https://www.google.com/search?&q=%22Public-key+cryptography%22&tbs=bkt:s&tbm=bks) **·** [books](https://www.google.com/search?tbs=bks:1&q=%22Public-key+cryptography%22+-wikipedia) **·** [scholar](https://scholar.google.com/scholar?q=%22Public-key+cryptography%22) **·** [JSTOR](https://www.jstor.org/action/doBasicSearch?Query=%22Public-key+cryptography%22&acc=on&wc=on) *(January 2024)**([Learn how and when to remove this message](/wiki/Help:Maintenance_template_removal))*

[![](https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Public-key-crypto-1.svg/250px-Public-key-crypto-1.svg.png)](/wiki/File:Public-key-crypto-1.svg)An unpredictable (typically large and [random](/wiki/Random)) number is used to begin generation of an acceptable pair of [keys](/wiki/Cryptographic_key) suitable for use by an asymmetric key algorithm.

---



[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/Private_key_signing.svg/250px-Private_key_signing.svg.png)](/wiki/File:Private_key_signing.svg)In this example the message is [digitally signed](/wiki/Digital_signature) with Alice's private key, but the message itself is not encrypted. 1) Alice signs a message with her private key. 2) Using Alice's public key, Bob can verify that Alice sent the message and that the message has not been modified.

---



[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Public_key_shared_secret.svg/250px-Public_key_shared_secret.svg.png)](/wiki/File:Public_key_shared_secret.svg) In the [Diffie–Hellman key exchange](/wiki/Diffie%E2%80%93Hellman_key_exchange) scheme, each party generates a public/private key pair and distributes the public key of the pair. After obtaining an authentic (n.b., this is critical) copy of each other's public keys, Alice and Bob can compute a shared secret offline. The shared secret can be used, for instance, as the key for a [symmetric cipher](/wiki/Symmetric_cipher).

---



[![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Public_key_encryption.svg/250px-Public_key_encryption.svg.png)](/wiki/File:Public_key_encryption.svg)In an asymmetric key encryption scheme, anyone can encrypt messages using a public key, but only the holder of the paired private key can decrypt such a message. The security of the system depends on the secrecy of the private key, which must not become known to any other.

---


**Public-key cryptography**, or **asymmetric cryptography**, is the field of [cryptographic](/wiki/Cryptographic) systems that use pairs of related keys. Each key pair consists of a **public key** and a corresponding **private key**.[[1]](#cite_note-rfc4949-1)[[2]](#cite_note-2) Key pairs are generated with [algorithms](/wiki/Algorithm) based on [mathematical](/wiki/Mathematical) problems termed [one-way functions](/wiki/One-way_function). Security of public-key cryptography depends on keeping the private key secret; the public key can be openly distributed without compromising security.[[3]](#cite_note-3) There are many kinds of public-key cryptosystems, with different security goals, including [digital signature](/wiki/Digital_signature), [Diffie–Hellman key exchange](/wiki/Diffie%E2%80%93Hellman_key_exchange), [public-key key encapsulation](/wiki/Key_encapsulation_mechanism), and public-key encryption.

Public key algorithms are fundamental security primitives in modern [cryptosystems](/wiki/Cryptosystem), including applications and protocols that offer assurance of the confidentiality and authenticity of electronic communications and data storage. They underpin numerous Internet standards, such as [Transport Layer Security](/wiki/Transport_Layer_Security) (TLS), [SSH](/wiki/SSH), [S/MIME](/wiki/S/MIME), and [PGP](/wiki/Pretty_Good_Privacy). Compared to [symmetric cryptography](/wiki/Symmetric_cryptography), public-key cryptography can be too slow for many purposes,[[4]](#cite_note-4) so these protocols often combine symmetric cryptography with public-key cryptography in [hybrid cryptosystems](/wiki/Hybrid_cryptosystem).




## Description


Before the mid-1970s, all cipher systems used [symmetric key algorithms](/wiki/Symmetric_key_algorithm), in which the same [cryptographic key](/wiki/Cryptographic_key) is used with the underlying algorithm by both the sender and the recipient, who must both keep the key secret. Of necessity, the key in every such system had to be exchanged between the communicating parties in some secure way prior to any use of the system – for instance, via a [secure channel](/wiki/Secure_channel). This requirement is never trivial and very rapidly becomes unmanageable as the number of participants increases, when secure channels are not available, or when (as is sensible cryptographic practice) keys are frequently changed. In particular, if messages are meant to be secure from other users, a separate key is required for each possible pair of users.

By contrast, in a public-key cryptosystem, the public keys can be disseminated widely and openly, and only the corresponding private keys need be kept secret. The two best-known types of public key cryptography are [digital signature](/wiki/Digital_signature) and public-key encryption.

In a [digital signature](/wiki/Digital_signature) system, a sender can use a private key together with a message to create a *signature*.  Anyone with the corresponding public key can verify whether the signature matches the message, but a forger who does not know the private key cannot generate any message/signature pair that will pass verification with the public key.[[5]](#cite_note-hac-digsig-5)[[6]](#cite_note-djb-forgery-6)[[7]](#cite_note-bellare-goldwasser2008digsigs-7) For example, a software publisher can create a signature key pair and include the public key in software installed on computers.  Later, the publisher can distribute an update to the software signed using the private key, and any computer receiving an update can confirm it is genuine by verifying the signature using the public key.  As long as the software publisher keeps the private key secret, even if a forger can distribute malicious updates to computers, they cannot convince the computers that any malicious updates are genuine.

In a public-key encryption system, anyone with a public key can encrypt a message, yielding a *ciphertext*, but only those who know the corresponding private key can decrypt the ciphertext to obtain the original message.[[8]](#cite_note-hac-pke-8) For example, a journalist can publish the public key of an encryption key pair on a website so that sources can send secret messages to the news organization in ciphertext. Only the journalist who knows the corresponding private key can decrypt the ciphertexts to obtain the sources' messages—an eavesdropper reading email on its way to the journalist cannot decrypt the ciphertexts.[[9]](#cite_note-dds2009anoncomm-9)[[10]](#cite_note-rackoff-simon1993cryptotrafficanalysis-10)[[11]](#cite_note-karger1977nondiscretionaryaccesscontrol-11)[[12]](#cite_note-chaum1981untraceableemail-12)  Public-key encryption on its own also does not tell the recipient anything about who sent a message[[8]](#cite_note-hac-pke-8): 283 [[13]](#cite_note-13)[[14]](#cite_note-14)—it just conceals the content of the message.[[a]](#cite_note-15)

Applications built on public-key cryptography include authenticating web servers with [TLS](/wiki/Transport_Layer_Security), [digital cash](/wiki/Digital_cash), [password-authenticated key agreement](/wiki/Password-authenticated_key_agreement), authenticating and concealing email content with [OpenPGP](/wiki/OpenPGP) or [S/MIME](/wiki/S/MIME), and [time-stamping services](/wiki/Trusted_timestamping) and [non-repudiation](/wiki/Non-repudiation) protocols.

One important issue is confidence/proof that a particular public key is authentic, i.e. that it is correct and belongs to the person or entity claimed, and has not been tampered with or replaced by some (perhaps malicious) third party. There are several possible approaches, including:

A [public key infrastructure](/wiki/Public_key_infrastructure) (PKI), in which one or more third parties – known as [certificate authorities](/wiki/Certificate_authorities) – certify ownership of key pairs. [TLS](/wiki/Transport_Layer_Security) relies upon this. This implies that the PKI system (software, hardware, and management) is trust-able by all involved.

A "[web of trust](/wiki/Web_of_trust)" decentralizes authentication by using individual endorsements of links between a user and the public key belonging to that user. [PGP](/wiki/Pretty_Good_Privacy) uses this approach, in addition to lookup in the [domain name system](/wiki/Domain_name_system) (DNS). The [DKIM](/wiki/DKIM) system for digitally signing emails also uses this approach.



## Hybrid cryptosystems


Because asymmetric key algorithms are nearly always much more computationally intensive than symmetric ones, it is common to use a public/private *asymmetric* [key-exchange algorithm](/wiki/Key-exchange_algorithm) to encrypt and exchange a *symmetric key*, which is then used by  [symmetric-key cryptography](/wiki/Symmetric-key_cryptography) to transmit data using the now-shared *symmetric key* for a symmetric key encryption algorithm. [PGP](/wiki/Pretty_Good_Privacy), [SSH](/wiki/SSH), and the [SSL/TLS](/wiki/SSL/TLS) family of schemes use this procedure;  they are thus called *[hybrid cryptosystems](/wiki/Hybrid_cryptosystem)*. The initial *asymmetric* cryptography-based key exchange to share a server-generated *symmetric* key from the server to client has the advantage of not requiring that a symmetric key be pre-shared manually, such as on printed paper or discs transported by a courier, while providing the higher data throughput of symmetric key cryptography over asymmetric key cryptography for the remainder of the shared connection.



## Weaknesses


As with all security-related systems, there are various potential weaknesses in public-key cryptography.  Aside from poor choice of an asymmetric key algorithm (there are few that are widely regarded as satisfactory) or too short a key length, the chief security risk is that the private key of a pair becomes known.  All security of messages, authentication, etc., encrypted with this private key will then be lost. This is commonly mitigated (such as in recent [TLS](/wiki/Transport_Layer_Security) schemes) by using [Forward secrecy](/wiki/Forward_secrecy) capable schemes that generate an ephemeral set of keys during the communication which must also be known for the communication to be compromised.

Additionally, with the advent of [quantum computing](/wiki/Quantum_computing), many asymmetric key algorithms are considered vulnerable to attacks, and new quantum-resistant schemes are being developed to overcome the problem.[[15]](#cite_note-16)[[16]](#cite_note-17)

Beyond algorithmic or key-length weaknesses, some studies have noted risks when private key control is delegated to third parties. Research on Uruguay’s implementation of Public Key Infrastructure under Law 18.600 found that centralized key custody by Trust Service Providers (TSPs) may weaken the principle of private-key secrecy, increasing exposure to [man-in-the-middle attacks](/wiki/Man-in-the-middle_attack) and raising concerns about legal non-repudiation.[[17]](#cite_note-18)



### Algorithms


All public key schemes are in theory susceptible to a "[brute-force key search attack](/wiki/Brute-force_attack)".[[18]](#cite_note-19) However, such an attack is impractical if the amount of computation needed to succeed – termed the "work factor" by [Claude Shannon](/wiki/Claude_Shannon) – is out of reach of all potential attackers. In many cases, the work factor can be increased by simply choosing a longer key. But other algorithms may inherently have much lower work factors, making resistance to a brute-force attack (e.g., from longer keys) irrelevant. Some special and specific algorithms have been developed to aid in attacking some public key encryption algorithms; both [RSA](/wiki/RSA_(algorithm)) and [ElGamal encryption](/wiki/ElGamal_encryption) have known attacks that are much faster than the brute-force approach.[*[citation needed](/wiki/Wikipedia:Citation_needed)*] None of these are sufficiently improved to be actually practical, however.

Major weaknesses have been found for several formerly promising asymmetric key algorithms. The ["knapsack packing" algorithm](/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem) was found to be insecure after the development of a new attack.[[19]](#cite_note-20) As with all cryptographic functions, public-key implementations may be vulnerable to [side-channel attacks](/wiki/Side-channel_attack) that exploit information leakage to simplify the search for a secret key. These are often independent of the algorithm being used. Research is underway to both discover, and to protect against, new attacks.



### Alteration of public keys


Another potential security vulnerability in using asymmetric keys is the possibility of a ["man-in-the-middle" attack](/wiki/Man-in-the-middle_attack), in which the communication of public keys is intercepted by a third party (the "man in the middle") and then modified to provide different public keys instead. Encrypted messages and responses must, in all instances, be intercepted, decrypted, and re-encrypted by the attacker using the correct public keys for the different communication segments so as to avoid suspicion.[*[citation needed](/wiki/Wikipedia:Citation_needed)*]

A communication is said to be insecure where data is transmitted in a manner that allows for interception (also called "[sniffing](/wiki/Sniffing_attack)"). These terms refer to reading the sender's private data in its entirety. A communication is particularly unsafe when interceptions can not be prevented or monitored by the sender.[[20]](#cite_note-21)

A man-in-the-middle attack can be difficult to implement due to the complexities of modern security protocols. However, the task becomes simpler when a sender is using insecure media such as public networks, the [Internet](/wiki/Internet), or wireless communication. In these cases an attacker can compromise the communications infrastructure rather than the data itself. A hypothetical malicious staff member at an [Internet service provider](/wiki/Internet_service_provider) (ISP) might find a man-in-the-middle attack relatively straightforward. Capturing the public key would only require searching for the key as it gets sent through the ISP's communications hardware;  in properly implemented asymmetric key schemes, this is not a significant risk.[*[citation needed](/wiki/Wikipedia:Citation_needed)*]

In some advanced man-in-the-middle attacks, one side of the communication will see the original data while the other will receive a malicious variant. Asymmetric man-in-the-middle attacks can prevent users from realizing their connection is compromised. This remains so even when one user's data is known to be compromised because the data appears fine to the other user. This can lead to confusing disagreements between users such as "it must be on your end!" when neither user is at fault. Hence, man-in-the-middle attacks are only fully preventable when the communications infrastructure is physically controlled by one or both parties; such as via a wired route inside the sender's own building. In summation, public keys are easier to alter when the communications hardware used by a sender is controlled by an attacker.[[21]](#cite_note-22)[[22]](#cite_note-martin-GF-23)[[23]](#cite_note-percy-GF-24)



### Public key infrastructure


One approach to prevent such attacks involves the use of a [public key infrastructure](/wiki/Public_key_infrastructure) (PKI); a set of roles, policies, and procedures needed to create, manage, distribute, use, store and [revoke](/wiki/Certificate_revocation) digital certificates and manage public-key encryption. However, this has potential weaknesses.

For example, the certificate authority issuing the certificate must be trusted by all participating parties to have properly checked the identity of the key-holder, to have ensured the correctness of the public key when it issues a certificate, to be secure from computer piracy, and to have made arrangements with all participants to check all their certificates before protected communications can begin. [Web browsers](/wiki/Web_browser), for instance, are supplied with a long list of "self-signed identity certificates" from PKI providers – these are used to check the *bona fides* of the certificate authority and then, in a second step, the certificates of potential communicators. An attacker who could subvert one of those certificate authorities into issuing a certificate for a bogus public key could then mount a "man-in-the-middle" attack as easily as if the certificate scheme were not used at all. An attacker who penetrates an authority's servers and obtains its store of certificates and keys (public and private) would be able to spoof, masquerade, decrypt, and forge transactions without limit, assuming that they were able to place themselves in the communication stream.

Despite its theoretical and potential problems, Public key infrastructure is widely used. Examples include [TLS](/wiki/Transport_Layer_Security) and its predecessor [SSL](/wiki/Transport_Layer_Security#SSL_1.0,_2.0,_and_3.0), which are commonly used to provide security for web browser transactions (for example, most websites utilize TLS for [HTTPS](/wiki/HTTPS)).

Aside from the resistance to attack of a particular key pair, the security of the certification [hierarchy](/wiki/Hierarchy) must be considered when deploying public key systems. Some certificate authority – usually a purpose-built program running on a server computer – vouches for the identities assigned to specific private keys by producing a digital certificate. [Public key digital certificates](/wiki/Digital_certificate) are typically valid for several years at a time, so the associated private keys must be held securely over that time. When a private key used for certificate creation higher in the PKI server hierarchy is compromised, or accidentally disclosed, then a "[man-in-the-middle attack](/wiki/Man-in-the-middle_attack)" is possible, making any subordinate certificate wholly insecure.



### Unencrypted metadata


Most of the available public-key encryption software does not conceal [metadata](/wiki/Metadata) in the message header, which might include the identities of the sender and recipient, the sending date, subject field, and the software they use etc.  Rather, only the body of the message is concealed and can only be decrypted with the private key of the intended recipient.  This means that a third party could construct quite a detailed model of participants in a communication network, along with the subjects being discussed, even if the message body itself is hidden.

However, there has been a recent demonstration of messaging with encrypted headers, which obscures the identities of the sender and recipient, and significantly reduces the available metadata to a third party.[[24]](#cite_note-25)  The concept is based around an open repository containing separately encrypted metadata blocks and encrypted messages. Only the intended recipient is able to decrypt the metadata block, and having done so they can identify and download their messages and decrypt them.  Such a messaging system is at present in an experimental phase and not yet deployed.  Scaling this method would reveal to the third party only the inbox server being used by the recipient and the timestamp of sending and receiving.  The server could be shared by thousands of users, making social network modelling much more challenging.



## History


During the early [history of cryptography](/wiki/History_of_cryptography), two parties would rely upon a key that they would exchange by means of a secure, but non-cryptographic, method such as a face-to-face meeting, or a trusted courier. This key, which both parties must then keep absolutely secret, could then be used to exchange encrypted messages. A number of significant practical difficulties arise with this approach to [distributing keys](/wiki/Key_distribution).



### Anticipation

In his 1874 book *The Principles of Science*, [William Stanley Jevons](/wiki/William_Stanley_Jevons) wrote:[[25]](#cite_note-TPS_1-26)

Can the reader say what two numbers multiplied together will produce the number [8,616,460,799](/wiki/William_Stanley_Jevons#Jevons'_number)?[[26]](#cite_note-JN_1-27) I think it unlikely that anyone but myself will ever know.[[25]](#cite_note-TPS_1-26)


Here he described the relationship of [one-way functions](/wiki/One-way_function) to cryptography, and went on to discuss specifically the [factorization](/wiki/Factorization) problem used to create a [trapdoor function](/wiki/Trapdoor_function). In July 1996, mathematician [Solomon W. Golomb](/wiki/Solomon_W._Golomb) said: "Jevons anticipated a key feature of the RSA Algorithm for public key cryptography, although he certainly did not invent the concept of public key cryptography."[[27]](#cite_note-28)



### Classified discovery


In 1970, [James H. Ellis](/wiki/James_H._Ellis), a British cryptographer at the UK [Government Communications Headquarters](/wiki/Government_Communications_Headquarters) (GCHQ), conceived of the possibility of "non-secret encryption", (now called public key cryptography), but could see no way to implement it.[[28]](#cite_note-29)[[29]](#cite_note-30)[[30]](#cite_note-31)

In 1973, his colleague [Clifford Cocks](/wiki/Clifford_Cocks) implemented what has become known as the [RSA encryption algorithm](/wiki/RSA_(cryptosystem)), giving a practical method of "non-secret encryption", and in 1974 another GCHQ mathematician and cryptographer, [Malcolm J. Williamson](/wiki/Malcolm_J._Williamson), developed what is now known as [Diffie–Hellman key exchange](/wiki/Diffie%E2%80%93Hellman_key_exchange).
The scheme was also passed to the US's [National Security Agency](/wiki/National_Security_Agency).[[31]](#cite_note-zdnet-32) Both organisations had a military focus and only limited computing power was available in any case;  the potential of public key cryptography remained unrealised by either organization. According to [Ralph Benjamin](/wiki/Ralph_Benjamin):


I judged it most important for military use ... if you can share your key rapidly and electronically, you have a major advantage over your opponent. Only at the end of the evolution from [Berners-Lee](/wiki/Tim_Berners-Lee) designing an open internet architecture for [CERN](/wiki/CERN), its adaptation and adoption for the [Arpanet](/wiki/Arpanet) ... did public key cryptography realise its full potential.[[31]](#cite_note-zdnet-32)


These discoveries were not publicly acknowledged until the research was declassified by the British government in 1997.[[32]](#cite_note-singh-33)



### Public discovery


In 1976, an asymmetric key cryptosystem was published by [Whitfield Diffie](/wiki/Whitfield_Diffie) and [Martin Hellman](/wiki/Martin_Hellman) who, influenced by [Ralph Merkle](/wiki/Ralph_Merkle)'s work on public key distribution, disclosed a method of public key agreement. This method of key exchange, which uses [exponentiation in a finite field](/wiki/Finite_field#Applications), came to be known as [Diffie–Hellman key exchange](/wiki/Diffie%E2%80%93Hellman_key_exchange).[[33]](#cite_note-Diffie_1976-34) This was the first published practical method for establishing a shared secret-key over an authenticated (but not confidential) communications channel without using a prior shared secret. Merkle's "public key-agreement technique" became known as [Merkle's Puzzles](/wiki/Merkle%27s_Puzzles), and was invented in 1974 and only published in 1978. This makes asymmetric encryption a rather new field in cryptography although cryptography itself dates back more than 2,000 years.[[34]](#cite_note-35)

In 1977, a generalization of Cocks's scheme was independently invented by [Ron Rivest](/wiki/Ron_Rivest), [Adi Shamir](/wiki/Adi_Shamir) and [Leonard Adleman](/wiki/Leonard_Adleman), all then at [MIT](/wiki/MIT). The latter authors published their work in 1978 in [Martin Gardner](/wiki/Martin_Gardner)'s [Scientific American](/wiki/Scientific_American) column, and the algorithm came to be known as [RSA](/wiki/RSA_(cryptosystem)), from their initials.[[35]](#cite_note-rsa-36) RSA uses [exponentiation modulo](/wiki/Modular_exponentiation) a product of two very large [primes](/wiki/Prime), to encrypt and decrypt, performing both public key encryption and public key digital signatures. Its security is connected to the extreme difficulty of [factoring large integers](/wiki/Integer_factorization), a problem for which there is no known efficient general technique. A description of the algorithm was published in the [Mathematical Games](/wiki/List_of_Martin_Gardner_Mathematical_Games_columns) column in the August 1977 issue of [Scientific American](/wiki/Scientific_American).[[36]](#cite_note-37)

Since the 1970s, a large number and variety of encryption, digital signature, key agreement, and other techniques have been developed, including the [Rabin signature](/wiki/Rabin_signature), [ElGamal encryption](/wiki/ElGamal_encryption), [DSA](/wiki/Digital_Signature_Algorithm) and [ECC](/wiki/Elliptic-curve_cryptography).

In addition to the algorithms developed within the open academic and standards communities, several countries have developed national public-key cryptography standards for use within their jurisdictions. These include [SM2 and SM9](/wiki/SM9_(cryptography_standard)) (China), GOST R 34.10-2012 (Russia), [EC-KCDSA](/wiki/EC-KCDSA) (South Korea), and DSTU 4145 ([Ukraine](/wiki/Ukraine)).



## Examples


Examples of well-regarded asymmetric key techniques for varied purposes include:


- [Diffie–Hellman key exchange](/wiki/Diffie%E2%80%93Hellman_key_exchange) protocol
- DSS (Digital Signature Standard), which incorporates the [Digital Signature Algorithm](/wiki/Digital_Signature_Algorithm)
- [ElGamal](/wiki/ElGamal)
- [Elliptic-curve cryptography](/wiki/Elliptic-curve_cryptography)
- [Elliptic Curve Digital Signature Algorithm](/wiki/Elliptic_Curve_Digital_Signature_Algorithm) (ECDSA)
- [Elliptic-curve Diffie–Hellman](/wiki/Elliptic-curve_Diffie%E2%80%93Hellman) (ECDH)
- [Ed25519](/wiki/Ed25519) and [Ed448](/wiki/Ed448) ([EdDSA](/wiki/EdDSA))
- [X25519](/wiki/X25519) and [X448](/wiki/X448) (ECDH/EdDH)
- Various [password-authenticated key agreement](/wiki/Password-authenticated_key_agreement) techniques
- [Paillier cryptosystem](/wiki/Paillier_cryptosystem)
- [RSA](/wiki/RSA_(cryptosystem)) encryption algorithm ([PKCS#1](/wiki/PKCS1))
- [Cramer–Shoup cryptosystem](/wiki/Cramer%E2%80%93Shoup_cryptosystem)
- [YAK](/wiki/YAK_(cryptography)) authenticated key agreement protocol


Examples of asymmetric key algorithms not yet widely adopted include:


- [NTRUEncrypt](/wiki/NTRUEncrypt) cryptosystem
- [Kyber](/wiki/Kyber)
- [McEliece cryptosystem](/wiki/McEliece_cryptosystem)


Examples of notable – yet insecure – asymmetric key algorithms include:


- [Merkle–Hellman knapsack cryptosystem](/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem)


Examples of protocols using asymmetric key algorithms include:


- [S/MIME](/wiki/S/MIME)
- [GPG](/wiki/GNU_Privacy_Guard), an implementation of [OpenPGP](/wiki/OpenPGP), and an Internet Standard
- [EMV](/wiki/EMV), EMV Certificate Authority
- [IPsec](/wiki/IPsec)
- [PGP](/wiki/Pretty_Good_Privacy)
- [ZRTP](/wiki/ZRTP), a secure [VoIP](/wiki/VoIP) protocol
- [Transport Layer Security](/wiki/Transport_Layer_Security) standardized by [IETF](/wiki/IETF) and its predecessor [Secure Socket Layer](/wiki/Secure_Socket_Layer)
- [SILC](/wiki/SILC_(protocol))
- [SSH](/wiki/SSH)
- [Bitcoin](/wiki/Bitcoin)
- [Off-the-Record Messaging](/wiki/Off-the-Record_Messaging)
- [SM2](/wiki/SM9_(cryptography_standard)) (China, elliptic curve)
- [SM9](/wiki/SM9_(cryptography_standard)) (China, identity-based)
- GOST R 34.10-2012 (Russia, elliptic curve signatures)
- [EC-KCDSA](/wiki/EC-KCDSA) (South Korea, elliptic curve signatures)
- DSTU 4145 ([Ukraine](/wiki/Ukraine), elliptic curve)



## See also



- [Books on cryptography](/wiki/Books_on_cryptography)
- [GNU Privacy Guard](/wiki/GNU_Privacy_Guard)
- [Identity-based encryption](/wiki/Identity-based_encryption) (IBE)
- [Key escrow](/wiki/Key_escrow)
- [Key-agreement protocol](/wiki/Key-agreement_protocol)
- [PGP word list](/wiki/PGP_word_list)
- [Post-quantum cryptography](/wiki/Post-quantum_cryptography)
- [Pretty Good Privacy](/wiki/Pretty_Good_Privacy)
- [Pseudonym](/wiki/Pseudonym)
- [Public key fingerprint](/wiki/Public_key_fingerprint)
- [Public key infrastructure](/wiki/Public_key_infrastructure) (PKI)
- [Quantum computing](/wiki/Quantum_computing)
- [Quantum cryptography](/wiki/Quantum_cryptography)
- [Secure Shell](/wiki/Secure_Shell) (SSH)
- [Symmetric-key algorithm](/wiki/Symmetric-key_algorithm)
- [Threshold cryptosystem](/wiki/Threshold_cryptosystem)
- [Web of trust](/wiki/Web_of_trust)




## Notes



1. **[^](#cite_ref-15)** However, public-key encryption does not conceal [metadata](/wiki/Metadata) like what computer a source used to send a message, when they sent it, or how long it is.



## References



1. **[^](#cite_ref-rfc4949_1-0)** R. Shirey (August 2007). [*Internet Security Glossary, Version 2*](https://www.rfc-editor.org/rfc/rfc4949). Network Working Group. [doi](/wiki/Doi_(identifier)):[10.17487/RFC4949](https://doi.org/10.17487%2FRFC4949). [RFC](/wiki/Request_for_Comments) [4949](https://datatracker.ietf.org/doc/html/rfc4949). *Informational.*
2. **[^](#cite_ref-2)** Bernstein, Daniel J.; Lange, Tanja (14 September 2017). ["Post-quantum cryptography"](http://www.nature.com/articles/nature23461). *Nature*. **549** (7671): 188–194. [Bibcode](/wiki/Bibcode_(identifier)):[2017Natur.549..188B](https://ui.adsabs.harvard.edu/abs/2017Natur.549..188B). [doi](/wiki/Doi_(identifier)):[10.1038/nature23461](https://doi.org/10.1038%2Fnature23461). [ISSN](/wiki/ISSN_(identifier)) [0028-0836](https://search.worldcat.org/issn/0028-0836). [PMID](/wiki/PMID_(identifier)) [28905891](https://pubmed.ncbi.nlm.nih.gov/28905891). [S2CID](/wiki/S2CID_(identifier)) [4446249](https://api.semanticscholar.org/CorpusID:4446249).
3. **[^](#cite_ref-3)** Stallings, William (3 May 1990). [*Cryptography and Network Security: Principles and Practice*](https://books.google.com/books?id=Dam9zrViJjEC). Prentice Hall. p. 165. [ISBN](/wiki/ISBN_(identifier)) [9780138690175](/wiki/Special:BookSources/9780138690175).
4. **[^](#cite_ref-4)** 
Alvarez, Rafael; Caballero-Gil, Cándido; Santonja, Juan; Zamora, Antonio (27 June 2017). ["Algorithms for Lightweight Key Exchange"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5551094). *Sensors*. **17** (7): 1517. [doi](/wiki/Doi_(identifier)):[10.3390/s17071517](https://doi.org/10.3390%2Fs17071517). [ISSN](/wiki/ISSN_(identifier)) [1424-8220](https://search.worldcat.org/issn/1424-8220). [PMC](/wiki/PMC_(identifier)) [5551094](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5551094). [PMID](/wiki/PMID_(identifier)) [28654006](https://pubmed.ncbi.nlm.nih.gov/28654006).
5. **[^](#cite_ref-hac-digsig_5-0)** [Menezes, Alfred J.](/wiki/Alfred_Menezes); [van Oorschot, Paul C.](/wiki/Paul_van_Oorschot); [Vanstone, Scott A.](/wiki/Scott_Vanstone) (October 1996). "Chapter 8: Public-key encryption". [*Handbook of Applied Cryptography*](https://cacr.uwaterloo.ca/hac/about/chap11.pdf) (PDF). CRC Press. pp. 425–488. [ISBN](/wiki/ISBN_(identifier)) [0-8493-8523-7](/wiki/Special:BookSources/0-8493-8523-7). Retrieved 8 October 2022.
6. **[^](#cite_ref-djb-forgery_6-0)** [Bernstein, Daniel J.](/wiki/Daniel_J._Bernstein) (1 May 2008). "Protecting communications against forgery". [*Algorithmic Number Theory*](https://cr.yp.to/antiforgery/forgery-20080501.pdf) (PDF). Vol. 44. MSRI Publications. §5: Public-key signatures, pp. 543–545. Retrieved 8 October 2022.
7. **[^](#cite_ref-bellare-goldwasser2008digsigs_7-0)** [Bellare, Mihir](/wiki/Mihir_Bellare); [Goldwasser, Shafi](/wiki/Shafi_Goldwasser) (July 2008). "Chapter 10: Digital signatures". [*Lecture Notes on Cryptography*](https://cseweb.ucsd.edu/~mihir/papers/gb.pdf#page=168) (PDF). p. 168. [Archived](https://web.archive.org/web/20220420003617/https://cseweb.ucsd.edu/~mihir/papers/gb.pdf#page=168) (PDF) from the original on 20 April 2022. Retrieved 11 June 2023.
8. ^ [***a***](#cite_ref-hac-pke_8-0) [***b***](#cite_ref-hac-pke_8-1) [Menezes, Alfred J.](/wiki/Alfred_Menezes); [van Oorschot, Paul C.](/wiki/Paul_van_Oorschot); [Vanstone, Scott A.](/wiki/Scott_Vanstone) (October 1996). "8: Public-key encryption". [*Handbook of Applied Cryptography*](https://cacr.uwaterloo.ca/hac/about/chap8.pdf) (PDF). CRC Press. pp. 283–319. [ISBN](/wiki/ISBN_(identifier)) [0-8493-8523-7](/wiki/Special:BookSources/0-8493-8523-7). Retrieved 8 October 2022.
9. **[^](#cite_ref-dds2009anoncomm_9-0)** [Danezis, George](/wiki/George_Danezis); Diaz, Claudia; [Syverson, Paul](/wiki/Paul_Syverson) (2010). "Chapter 13: Anonymous Communication". In Rosenberg, Burton (ed.). [*Handbook of Financial Cryptography and Security*](https://www.freehaven.net/anonbib/cache/systems-anon-communication.pdf) (PDF). Chapman & Hall/CRC. pp. 341–390. [ISBN](/wiki/ISBN_(identifier)) [978-1420059816](/wiki/Special:BookSources/978-1420059816). Since PGP, beyond compressing the messages, does not make any further attempts to hide their size, it is trivial to follow a message in the network just by observing its length.
10. **[^](#cite_ref-rackoff-simon1993cryptotrafficanalysis_10-0)** [Rackoff, Charles](/wiki/Charles_Rackoff); Simon, Daniel R. (1993). "Cryptographic defense against traffic analysis". *Proceedings of the twenty-fifth annual ACM symposium on Theory of Computing*. STOC '93: ACM [Symposium on the Theory of Computing](/wiki/Symposium_on_the_Theory_of_Computing). [Association for Computing Machinery](/wiki/Association_for_Computing_Machinery). pp. 672–681. [doi](/wiki/Doi_(identifier)):[10.1145/167088.167260](https://doi.org/10.1145%2F167088.167260). Now, certain types of information cannot reasonably be assumed to be concealed.  For instance, an upper bound on the total volume of a party's sent or received communication (of any sort) is obtainable by anyone with the resources to examine all possible physical communication channels available to that party.
11. **[^](#cite_ref-karger1977nondiscretionaryaccesscontrol_11-0)** Karger, Paul A. (May 1977). "11: Limitations of End-to-End Encryption". [*Non-Discretionary Access Control for Decentralized Computing Systems*](https://dspace.mit.edu/handle/1721.1/149471) (S.M. thesis). [Laboratory for Computer Science](/wiki/Laboratory_for_Computer_Science), [Massachusetts Institute of Technology](/wiki/Massachusetts_Institute_of_Technology). [hdl](/wiki/Hdl_(identifier)):[1721.1/149471](https://hdl.handle.net/1721.1%2F149471). The scenario just described would seem to be secure, because all data is encrypted before being passed to the communications processors.  However, certain control information must be passed in cleartext from the host to the communications processor to allow the network to function. This control information consists of the destination address for the packet, the length of the packet, and the time between successive packet transmissions.
12. **[^](#cite_ref-chaum1981untraceableemail_12-0)** [Chaum, David L.](/wiki/David_Chaum) (February 1981). [Rivest, R.](/wiki/Ron_Rivest) (ed.). "Untraceable Electronic Mail, Return Addresses, and Digital Pseudonyms". *[Communications of the ACM](/wiki/Communications_of_the_ACM)*. **24** (2). [Association for Computing Machinery](/wiki/Association_for_Computing_Machinery). Recently, some new solutions to the "key distribution problem" (the problem of providing each communicant with a secret key) have been suggested, under the name of public key cryptography.  Another cryptographic problem, the "traffic analysis problem" (the problem of keeping confidential who converses with whom, and when they converse), will become increasingly important with the growth of electronic mail.
13. **[^](#cite_ref-13)** Davis, Don (2001). ["Defective Sign & Encrypt in S/MIME, PKCS#7, MOSS, PEM, PGP, and XML"](https://www.usenix.org/legacy/events/usenix01/full_papers/davis/davis_html/). *Proceedings of the 2001 USENIX Annual Technical Conference*. [USENIX](/wiki/USENIX). pp. 65–78. Why is naïve Sign & Encrypt insecure?  Most simply, S&E is vulnerable to "surreptitious forwarding:" Alice signs & encrypts for Bob's eyes, but Bob re-encrypts Alice's signed message for Charlie to see.  In the end, Charlie believes Alice wrote to him directly, and can't detect Bob's subterfuge.
14. **[^](#cite_ref-14)** An, Jee Hea (12 September 2001). [*Authenticated Encryption in the Public-Key Setting: Security Notions and Analyses*](https://eprint.iacr.org/2001/079) (Technical report). IACR Cryptology ePrint Archive. 2001/079. Retrieved 24 November 2024.
15. **[^](#cite_ref-16)** Escribano Pablos, José Ignacio; González Vasco, María Isabel (April 2023). ["Secure post-quantum group key exchange: Implementing a solution based on Kyber"](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/cmu2.12561). *IET Communications*. **17** (6): 758–773. [doi](/wiki/Doi_(identifier)):[10.1049/cmu2.12561](https://doi.org/10.1049%2Fcmu2.12561). [hdl](/wiki/Hdl_(identifier)):[10016/37141](https://hdl.handle.net/10016%2F37141). [ISSN](/wiki/ISSN_(identifier)) [1751-8628](https://search.worldcat.org/issn/1751-8628). [S2CID](/wiki/S2CID_(identifier)) [255650398](https://api.semanticscholar.org/CorpusID:255650398).
16. **[^](#cite_ref-17)** Stohrer, Christian; Lugrin, Thomas (2023), Mulder, Valentin; Mermoud, Alain; Lenders, Vincent; Tellenbach, Bernhard (eds.), "Asymmetric Encryption", *Trends in Data Protection and Encryption Technologies*, Cham: Springer Nature Switzerland, pp. 11–14, [doi](/wiki/Doi_(identifier)):[10.1007/978-3-031-33386-6_3](https://doi.org/10.1007%2F978-3-031-33386-6_3), [ISBN](/wiki/ISBN_(identifier)) [978-3-031-33386-6](/wiki/Special:BookSources/978-3-031-33386-6)`{{[citation](/wiki/Template:Citation)}}`:  CS1 maint: work parameter with ISBN ([link](/wiki/Category:CS1_maint:_work_parameter_with_ISBN))
17. **[^](#cite_ref-18)** Sabiguero, Ariel; Vicente, Alfonso; Esnal, Gonzalo (November 2024). ["Let There Be Trust"](https://doi.org/10.1109/URUCON63440.2024.10850093). *2024 IEEE URUCON*. [doi](/wiki/Doi_(identifier)):[10.1109/URUCON63440.2024.10850093](https://doi.org/10.1109%2FURUCON63440.2024.10850093).
18. **[^](#cite_ref-19)** Paar, Christof; Pelzl, Jan; Preneel, Bart (2010). [*Understanding Cryptography: A Textbook for Students and Practitioners*](http://www.crypto-textbook.com). Springer. [ISBN](/wiki/ISBN_(identifier)) [978-3-642-04100-6](/wiki/Special:BookSources/978-3-642-04100-6).
19. **[^](#cite_ref-20)** Shamir, Adi (November 1982). "A polynomial time algorithm for breaking the basic Merkle-Hellman cryptosystem". *23rd Annual Symposium on Foundations of Computer Science (SFCS 1982)*. pp. 145–152. [doi](/wiki/Doi_(identifier)):[10.1109/SFCS.1982.5](https://doi.org/10.1109%2FSFCS.1982.5).
20. **[^](#cite_ref-21)** 
Tunggal, Abi (20 February 2020). ["What Is a Man-in-the-Middle Attack and How Can It Be Prevented – What is the difference between a man-in-the-middle attack and sniffing?"](https://www.upguard.com/blog/man-in-the-middle-attack#mitm-sniffing). *UpGuard*. Retrieved 26 June 2020.[*[self-published source?](/wiki/Wikipedia:Verifiability#Self-published_sources)*]
21. **[^](#cite_ref-22)** 
Tunggal, Abi (20 February 2020). ["What Is a Man-in-the-Middle Attack and How Can It Be Prevented - Where do man-in-the-middle attacks happen?"](https://www.upguard.com/blog/man-in-the-middle-attack#where). *UpGuard*. Retrieved 26 June 2020.[*[self-published source?](/wiki/Wikipedia:Verifiability#Self-published_sources)*]
22. **[^](#cite_ref-martin-GF_23-0)** 
martin (30 January 2013). ["China, GitHub and the man-in-the-middle"](https://web.archive.org/web/20160819165216/https://en.greatfire.org/blog/2013/jan/china-github-and-man-middle). *GreatFire*. Archived from [the original](https://en.greatfire.org/blog/2013/jan/china-github-and-man-middle) on 19 August 2016. Retrieved 27 June 2015.[*[self-published source?](/wiki/Wikipedia:Verifiability#Self-published_sources)*]
23. **[^](#cite_ref-percy-GF_24-0)** 
percy (4 September 2014). ["Authorities launch man-in-the-middle attack on Google"](https://en.greatfire.org/blog/2014/sep/authorities-launch-man-middle-attack-google). *GreatFire*. Retrieved 26 June 2020.[*[self-published source?](/wiki/Wikipedia:Verifiability#Self-published_sources)*]
24. **[^](#cite_ref-25)** 
Bjorgvinsdottir, Hanna; Bentley, Phil (24 June 2021). "Warp2: A Method of Email and Messaging with Encrypted Addressing and Headers". [arXiv](/wiki/ArXiv_(identifier)):[1411.6409](https://arxiv.org/abs/1411.6409) [[cs.CR](https://arxiv.org/archive/cs.CR)].
25. ^ [***a***](#cite_ref-TPS_1_26-0) [***b***](#cite_ref-TPS_1_26-1) Jevons, W.S. (1874). [*The Principles of Science: A Treatise on Logic and Scientific Method*](https://archive.org/details/principlesofscie00jevorich/principlesofscie00jevorich/page/n166/mode/1up?view=theater). [Macmillan & Co.](/wiki/Macmillan_%26_Co.) p. 141. Retrieved 18 January 2024.
26. **[^](#cite_ref-JN_1_27-0)** Weisstein, E.W. (2024). ["Jevons' Number"](https://mathworld.wolfram.com/JevonsNumber.html). [MathWorld](/wiki/MathWorld). Retrieved 18 January 2024.
27. **[^](#cite_ref-28)** Golob, Solomon W. (1996). "On Factoring Jevons' Number". *Cryptologia*. **20** (3): 243. [doi](/wiki/Doi_(identifier)):[10.1080/0161-119691884933](https://doi.org/10.1080%2F0161-119691884933). [S2CID](/wiki/S2CID_(identifier)) [205488749](https://api.semanticscholar.org/CorpusID:205488749).
28. **[^](#cite_ref-29)** Ellis, James H. (January 1970). ["The Possibility of Secure Non-secret Digital Encryption"](https://cryptocellar.org/cesg/possnse.pdf) (PDF). CryptoCellar. Retrieved 18 January 2024.
29. **[^](#cite_ref-30)** Ellis, James H. (January 1970). ["The Possibility of Secure Non-secret Digital Encryption"](https://nsarchive.gwu.edu/document/21971-document-02). The George Washington University. Retrieved 8 December 2025.
30. **[^](#cite_ref-31)** Sawer, Patrick (11 March 2016). ["The unsung genius who secured Britain's computer defences and paved the way for safe online shopping"](https://www.newindianexpress.com/world/2016/mar/12/the-anonymous-researcher-who-held-the-key-to-cyber-security-910751.html). *The Telegraph*.
31. ^ [***a***](#cite_ref-zdnet_32-0) [***b***](#cite_ref-zdnet_32-1) Espiner, Tom (26 October 2010). ["GCHQ pioneers on birth of public key crypto"](https://www.zdnet.com/article/gchq-pioneers-on-birth-of-public-key-crypto/). *[ZDNet](/wiki/ZDNet)*.
32. **[^](#cite_ref-singh_33-0)** [Singh, Simon](/wiki/Simon_Singh) (1999). [*The Code Book*](/wiki/The_Code_Book). Doubleday. pp. [279](https://archive.org/details/codebookevolutio00sing/page/279)–292.
33. **[^](#cite_ref-Diffie_1976_34-0)** [Diffie, Whitfield](/wiki/Whitfield_Diffie); [Hellman, Martin E.](/wiki/Martin_Hellman) (November 1976). ["New Directions in Cryptography"](http://ee.stanford.edu/%7Ehellman/publications/24.pdf) (PDF). *[IEEE Transactions on Information Theory](/wiki/IEEE_Transactions_on_Information_Theory)*. **22** (6): 644–654. [Bibcode](/wiki/Bibcode_(identifier)):[1976ITIT...22..644D](https://ui.adsabs.harvard.edu/abs/1976ITIT...22..644D). [CiteSeerX](/wiki/CiteSeerX_(identifier)) [10.1.1.37.9720](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.37.9720). [doi](/wiki/Doi_(identifier)):[10.1109/TIT.1976.1055638](https://doi.org/10.1109%2FTIT.1976.1055638). [Archived](https://web.archive.org/web/20141129035850/https://ee.stanford.edu/%7Ehellman/publications/24.pdf) (PDF) from the original on 29 November 2014.
34. **[^](#cite_ref-35)** ["Asymmetric encryption"](https://www.ionos.com/digitalguide/server/security/public-key-encryption/). *IONOS Digitalguide*. Retrieved 9 June 2022.
35. **[^](#cite_ref-rsa_36-0)** 
Rivest, R.; Shamir, A.; Adleman, L. (February 1978). ["A Method for Obtaining Digital Signatures and Public-Key Cryptosystems"](https://web.archive.org/web/20081217101831/http://people.csail.mit.edu/rivest/Rsapaper.pdf) (PDF). *[Communications of the ACM](/wiki/Communications_of_the_ACM)*. **21** (2): 120–126. [CiteSeerX](/wiki/CiteSeerX_(identifier)) [10.1.1.607.2677](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.607.2677). [doi](/wiki/Doi_(identifier)):[10.1145/359340.359342](https://doi.org/10.1145%2F359340.359342). [S2CID](/wiki/S2CID_(identifier)) [2873616](https://api.semanticscholar.org/CorpusID:2873616). Archived from [the original](http://people.csail.mit.edu/rivest/Rsapaper.pdf) (PDF) on 17 December 2008. Retrieved 15 November 2019.
36. **[^](#cite_ref-37)** Robinson, Sara (June 2003). ["Still Guarding Secrets after Years of Attacks, RSA Earns Accolades for its Founders"](http://www.msri.org/people/members/sara/articles/rsa.pdf) (PDF). *SIAM News*. **36** (5).



## Sources



- Hirsch, Frederick J. ["SSL/TLS Strong Encryption: An Introduction"](https://httpd.apache.org/docs/2.2/ssl/ssl_intro.html#cryptographictech). *Apache HTTP Server*. Retrieved 17 April 2013.. The first two sections contain a very good introduction to public-key cryptography.
- [Ferguson, Niels](/wiki/Niels_Ferguson); [Schneier, Bruce](/wiki/Bruce_Schneier) (2003). *Practical Cryptography*. [Wiley](/wiki/John_Wiley_%26_Sons). [ISBN](/wiki/ISBN_(identifier)) [0-471-22357-3](/wiki/Special:BookSources/0-471-22357-3).
- [Katz, Jon](/wiki/Jon_Katz); Lindell, Y. (2007). [*Introduction to Modern Cryptography*](https://archive.org/details/Introduction_to_Modern_Cryptography). [CRC Press](/wiki/CRC_Press). [ISBN](/wiki/ISBN_(identifier)) [978-1-58488-551-1](/wiki/Special:BookSources/978-1-58488-551-1).
- [Menezes, A. J.](/wiki/Alfred_Menezes); van Oorschot, P. C.; [Vanstone, Scott A.](/wiki/Scott_Vanstone) (1997). [*Handbook of Applied Cryptography*](https://archive.org/details/handbookofapplie0000mene). Taylor & Francis. [ISBN](/wiki/ISBN_(identifier)) [0-8493-8523-7](/wiki/Special:BookSources/0-8493-8523-7).
- [IEEE 1363: Standard Specifications for Public-Key Cryptography](https://web.archive.org/web/20081119061833/http://grouper.ieee.org/groups/1363/)
- Christof Paar, Jan Pelzl, ["Introduction to Public-Key Cryptography"](https://archive.today/20121208212741/http://wiki.crypto.rub.de/Buch/movies.php), Chapter 6 of "Understanding Cryptography, A Textbook for Students and Practitioners". (companion web site contains online cryptography course that covers public-key cryptography), Springer, 2009.
- Salomaa, Arto (1996). *Public-Key Cryptography* (2 ed.). Berlin: [Springer](/wiki/Springer_Science%2BBusiness_Media). 275. [doi](/wiki/Doi_(identifier)):[10.1007/978-3-662-03269-5](https://doi.org/10.1007%2F978-3-662-03269-5). [ISBN](/wiki/ISBN_(identifier)) [978-3-662-03269-5](/wiki/Special:BookSources/978-3-662-03269-5). [S2CID](/wiki/S2CID_(identifier)) [24751345](https://api.semanticscholar.org/CorpusID:24751345).



## External links


- [Oral history interview with Martin Hellman](http://conservancy.umn.edu/handle/11299/107353), [Charles Babbage Institute](/wiki/Charles_Babbage_Institute), University of Minnesota. Leading cryptography scholar [Martin Hellman](/wiki/Martin_Hellman) discusses the circumstances and fundamental insights of his invention of public key cryptography with collaborators [Whitfield Diffie](/wiki/Whitfield_Diffie) and [Ralph Merkle](/wiki/Ralph_Merkle) at Stanford University in the mid-1970s.
- [An account of how GCHQ kept their invention of PKE secret until 1997](https://web.archive.org/web/20080625052129/http://www.ladlass.com/intel/archives/010256.html)


[Authority control databases](/wiki/Help:Authority_control) [![Edit this at Wikidata](https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/OOjs_UI_icon_edit-ltr-progressive.svg/20px-OOjs_UI_icon_edit-ltr-progressive.svg.png)

---](https://www.wikidata.org/wiki/Q201339#identifiers)International- [GND](https://d-nb.info/gnd/4209133-0)

National- [United States](https://id.loc.gov/authorities/sh00004804)
- [France](https://catalogue.bnf.fr/ark:/12148/cb13554544f)
- [BnF data](https://data.bnf.fr/ark:/12148/cb13554544f)
- [Japan](https://id.ndl.go.jp/auth/ndlna/00966793)
- [Israel](https://www.nli.org.il/en/authorities/987007290951705171)

Other- [Yale LUX](https://lux.collections.yale.edu/view/concept/9524f3a8-c6f3-4e35-8aad-9c59a49eaf27)


 
NewPP limit report
Parsed by mw‐api‐int.eqiad.main‐bd466b4d5‐5p2xj
Cached time: 20260504135341
Cache expiry: 2592000
Cache expiry source: Module:Citation/CS1 (os.date(%Y))
Reduced expiry: false
Complications: [vary‐revision‐sha1, prevent‐selective‐update, show‐toc]
CPU time usage: 0.911 seconds
Real time usage: 1.152 seconds
Preprocessor visited node count: 4335/1000000
Revision size: 42385/2097152 bytes
Post‐expand include size: 124336/2097152 bytes
Template argument size: 10057/2097152 bytes
Highest expansion depth: 17/100
Expensive parser function count: 6/500
Unstrip recursion depth: 1/20
Unstrip post‐expand size: 157628/5000000 bytes
Lua time usage: 0.574/10.000 seconds
Lua memory usage: 7912076/52428800 bytes
Number of Wikibase entities loaded: 1/500


Transclusion expansion time report (%,ms,calls,template)
100.00% 1023.125      1 -total
 49.23%  503.724      2 Template:Reflist
 15.00%  153.513      1 Template:Cite_IETF
 12.00%  122.798      1 Template:Authority_control
  9.70%   99.237     14 Template:Cite_book
  9.06%   92.674      1 Template:Short_description
  6.72%   68.735      1 Template:More_citations_needed
  6.38%   65.284      1 Template:Ambox
  6.21%   63.511     10 Template:Cite_web
  6.17%   63.123      2 Template:Pagetype

 Render ID a869e20b-47c0-11f1-9ed4-99c777189eba 
 Saved in parser cache with key enwiki:pcache:24222:|#|:idhash:canonical and timestamp 20260504135341 and revision id 1352486414. Rendering was triggered because: api-parse
 
![](https://en.wikipedia.org/wiki/Special:CentralAutoLogin/start?useformat=desktop&type=1x1&usesul3=1)

---


Retrieved from "[https://en.wikipedia.org/w/index.php?title=Public-key_cryptography&oldid=1352486414](https://en.wikipedia.org/w/index.php?title=Public-key_cryptography&oldid=1352486414)"
