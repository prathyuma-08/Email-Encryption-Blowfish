# Email encryption using Blowfish Algorithm

The focus of this project is to secure the contents of an email using the Blowfish algorithm. 
Each character in the message is converted to its ASCII code and encrypted to its corresponding cipher text, which is then sent as an email. 
The received email is decrypted using the reverse process. 
A flask application is developed which sends email to the specified email address, with the mentioned abstract and the body.

## Repository structure

app.py - The flask application for sending and decrypting emails

blowfish.py - The algorithm for encryption and decryption

send.py - The code for sending emails

## References

[Blowfish algorithm](https://en.wikipedia.org/wiki/Blowfish_(cipher))

[P and S boxes](https://www.schneier.com/wp-content/uploads/2015/12/constants-2.txt)
