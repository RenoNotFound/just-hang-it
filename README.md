Let's # Hang Somebody!
Story
Evil SKYNET is trying to take control over the world. And guess who the only hope for mankind is? Yes, you're right - it's you! And you must prove your skills, knowledge and intelligence by showing that you are smart and able to guess words!

What are you going to learn?
You will be able to break up a simple problem into a series of steps or logical units. You will know how to use variables and basic control structures (loops and conditional structures). You will recognise basic error messages and debug your code with printing out variable values.

Starting code
Start coding with hangman.py file. Here is how to get it:

If you have not used Git before, download hangman.py

If you are already using Git, create a repository using this link: https://classroom.github.com/g/6MDOoiTQ

Tasks
Implement the simplest version of Hangman Game. In the beginning, the program should represent each letter as a dash ("_") and display them at the screen. User can guess one letter. If succeeded, then all appearances of this letter are uncovered in the dashed word. If she uncovers all occurrences, then she wins.

Add a possibility to guess a whole word at once.

Create a list of European cities to pick randomly a word to dashed.

Print an updated list of already used letters after each try.

Add life points to make a game more challenging.

Make the game fool-proof. If the user enters any character which is not a letter or a letter which is already used, the program informs about it and doesn't decrease life points.

Requirements
[1.1] Program displays a dashed word
[1.2] A user can enter a letter
[1.3] If the user guess one letter, the dashed word with uncovered letter appears
[1.4] If the whole dashed word is uncovered, a win screen appears
[2.1] A user can enter a letter or word
[2.2] If the user guess the whole word, a win screen appears
[3.1] Program picks a European capital randomly as a dashed word to guess
[4.1] Program displays already used letters
[4.2] Already used letters don't duplicate
[5.1] Program shows current life points
[5.2] If the user doesn't guess the right letter, life points decrease by 1
[5.3] If life points reach 0, user sees a loose screen
[5.4] Program works until the user wins or loses
[6.1] If the user enters a number or special character, a message about wrong input appears
[6.2] If the user enters an already used letter, a message about it appears
[6.3] If the user provides any wrong input, life points aren't decremented
Technical requirements
Capital names should be in English and capital letters (i.e. LONDON, PARIS, WARSAW).

The program should be case insensitive - i.e. no matter if the user enters d or D, it should count as D.

If a capital consists of more than one word, then whitespaces should be ignored.

Use functions and try to avoid global scope.

Hints
More code can mean more bugs and worse readability. Choose wisely what to do first and how to keep the code clean all the time
Background materials
Hangman game
triangular_flag_on_post Strings
triangular_flag_on_post Control structures
triangular_flag_on_post Functions
Acceptance review
You will need this only at review time, after completing the project. Use this form to record the review you provide for your peer.
