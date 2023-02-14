---
myst:
  html_meta:
    description: In this article we explain both ways of securing information and
      give examples for how you can use it on Hypernode.
    title: 'How to secure your data using encryption and hashing? '
redirect_from:
  - /en/support/solutions/articles/48001153348-how-to-secure-your-data-using-encryption-and-hashing/
---

<!-- source: https://support.hypernode.com/en/support/solutions/articles/48001153348-how-to-secure-your-data-using-encryption-and-hashing/ -->

# How to Secure Your Data Using Encryption and Hashing

Hashing and encryption are cryptographic functions that both serve a completely different purpose. Encryption is used to lock data in a way that it can be unlocked later with a key. Hashing creates a unique hash code from all the data it receives, which cannot be converted back to the original code. In this article we explain both ways of securing information and give examples for how you can use it.

Encryption is the encoding of information with the aim of making it unusable if it is used without the key with which it can be unlocked. This is used for SSL, among other things, to prevent someone who intercepts your data from reading or adjusting it. In short, there are two types of encryption; Symmetric Encryption and Asymmetric Encryption.

## Symmetric Encryption

Symmetric Encryption uses a key to lock and unlock the data. This is used in our network for, for example, SSH. It has speed as an advantage but requires both parties to have the key before the connection can be established.

## Asymmetric Encryption

Asymmetric Encryption works using two keys; one to encrypt data and the other to unlock that data. SSL, for example, uses this encryption method.

## Hashing

Hashing is useful for storing passwords, for example. In such a case, a password is stored hashed. When someone's identity is verified, the hash of the password is compared to the hash stored in the database. In this way you can check whether someone has entered the correct password without that password being stored in a way that can be recalculated to the original password.

## MD5 hashing

In the examples below we use md5 hashing; that is a form of hashing that always returns a unique 128 bit code. Hashing can generate a code of all data, regardless of the quantity, with the following properties:

- **Length:** The length of a generated hash is determined by the algorithm it generates. Md5 hashing will always generate a 128 bit (32 digit hexadecimal) code as output.
- **No collisions**: Two different files should never generate the same hash.
- **Reusable:** A hashed file or text must always generate the same hash.
- **Non-reversible:** A hash cannot be converted back to the original text.

|                        |                                  |
| ---------------------- | -------------------------------- |
| **Text**               | **Hashed text**                  |
| Hypernode over hashing | cc967ac33065d74f72590edd4f5491d5 |
| Hypernode over hashing | 95ed53c538bfa7471cf2a0604094555e |

As you can see in this first example, the only difference between the texts is the dot at the end, however the hash codes themselves are drastically different.

## Example

Using the example below, we will explain how you can store your passwords more securely using hashing:

To log in as a user, the password must of course be verified. Now the password can of course be stored in the database, but when the site is hacked, all these passwords are compromised. In addition, the email addresses of the users of these passwords are also known. Most people use their password in multiple places at the same time, so it could happen that a user's webmail is breached because the password is not encrypted.

### Example Unhashed Data

|          |              |                                  |
| -------- | ------------ | -------------------------------- |
| **Name** | **Password** | **Hash of the password**         |
| Jack     | 123456       | e10adc3949ba59abbe56e057f20f883e |
| Pete     | Password     | 701f33b8d1366cde9cb3822256a62c01 |
| Casey    | 123456       | e10adc3949ba59abbe56e057f20f883e |

That is already a lot safer! The passwords cannot be recalculated in this way. Unfortunately, the bad guys will also know about this and other methods are used to “back calculate” these hashes. Rainbow Tables is used to do this. These are large databases of words and their hashes, which checks whether those hashes exist in the database and in this way obtains the password. These hashes are all pre-calculated and this way a lot of passwords from a database can be cracked quickly.

## Salt

The text above explains the advantages and disadvantages of hashing and why just a hash of a password is insufficient to guarantee as much security as possible for everyone. For this reason, they invented Salt. Salt is the adding of information to a password before making it into a hash. An example of this is the username + password hashing.

In the previous table you saw that the hashes for the passwords of Pete and Casey were identical and that is of course not optimal. Once you know the password for a user's hash, you know which other users use that password. However, with Salt you can fix this:

|          |              |                                  |                                  |
| -------- | ------------ | -------------------------------- | -------------------------------- |
| **Name** | **Password** | **Text that needs to be hashed** | **Hash**                         |
| Jack     | 123456       | Jack+ 123456                     | 90b60bac3e1113e180ddefed30c37b6e |
| Pete     | Password     | Pete + wachtwoord                | d9bc513252dede0277c864f23df84039 |
| Casey    | 123456       | Casey + 123456                   | 6cf875073050de4d260580c39a782e03 |

And there you go, all different hashes! If the database is now hacked, every hash code will still have to be cracked before the password can be retrieved.
