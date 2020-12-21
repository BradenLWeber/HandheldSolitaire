# HandheldSolitaire

Running the code will display this opening: 

Welcome! This code is for gathering data on handheld solitaire.

Normal handheld solitaire is played by shuffling a deck of cards and pulling the cards out from the back one by one to form a new pile.
Any time the top card and the 4th card down have the same number, both cards and the two in between are taken away.
Any time the top card and the 4th card down have the same suite, the two cards between them are taken away.
Finally, any time the 4 top cards all have the same suite, all 4 are taken away.
You win if you can take away every card from the new stack.

Pretty simple, huh?

The frustration you will run into rather quickly is that you will get through the entire deck without taking away every card.
This leaves you with a mere small (or big) pile of cards and a heart full of sadness.
So I wondered, how often do you actually win this game? It can't be often, or so my experiences told me.

So, this code will win the game for a set number of times and return the stats for how many games it takes to win on average.
It will also return the longest game played so you can have a sense of the horrible misfortune you may experience in real life.

And finally, it also includes another version of this game. I call it the recycling version.
This version plays the game once, and if you lose, it uses the exact same deck without shuffling again.
The question is, does this actually increase the frequency in which you win the game?
Guess you'll have to find out yourself.

That is all. Happy stat hunting!
