[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=16444168)
# Caesar Cipher

The Caesar Cipher is one of the oldest and most famous types of encryption ever used (and now one of the most basic)

The general idea is that you take a message, and "shift" all the letters along the alphabet a set number of times

For example, if we encrypt the message "hello" with a shift of 3:

* h goes to k
* e goes to h
* l goes to o
* o goes to r

So "hello" with a shift of 3 becomes "khoor"

Then to un-encrypt it, we need to shift back 3 letters

For boundaries, the shift moves to the other end of the alphabet - e.g. shifting "z" forwards 2 results in "b"

You will write a code with two functions, one will shift "forwards" through the alphabet to encrypt a message, the other will shift "backwards" through the alphabet to un-encrypt the message

Each function should accept two arguments, the first is a string which is the text to be encrypted/un-encrypted, the second is the "shift" to be applied, which should be an integer

You may assume that all messages will be only lower case text, with no other characters except spaces

Ensure that the code you write is well documented and follows coding standards and best practices

The two functions should be called "encrypt" and "unencrypt"

In both funcitons the "shift" value will be a positive integer