# Brainstorm

## Run unit tests

python -m unittest test_pokerhand

## Things to think about

### Determine the result of each hand
First
- Sort cards in order of value high to low
- Secondary sort cards in a pre determined order of suits
  - D H S C

Then
- Does the hand have Straight Flush
  - Are all the card of the same suit
  - Reuse Flush check
  - Are each of the values in consecutive descending order (eg: K Q J 10 9)
  - Return the value of the highest card (first of the sorted list)
  - Reuse Straight check
- Does the hand have Four of a kind
  - Are 4 values the same 
  - Return that value
- Does the hand have Full House
  - Are 3 values the same
  - Are the other two the same
  - Reuse Three of a kind check
  - Print both values
- Does the hand have Flush
  - Are all the card of the same suit
  - Print suit
- Does the hand have Straight
  - Are each of the values in consecutive descending order (eg: K Q J 10 9)
  - Return the value of the highest card (first of the sorted list)
- Does the hand have Three of a kind
  - Are 3 values the same
  - Return that value
- Does the hand have Two pairs
  - Are 2 values the same
  - Reuse Pair check
  - Are 2 values in the remaining cards the same
  - Return both values 
- Does the hand have Pair
  - Are 2 values the same
  - Find the pair 
- Does the hand have High card
  - Find the highest card 

### Determine the best hand of both player

### Compare the hands

### Determine winning hand

### Output the Winning hand


## Architecture

### Card object 
- Suit
- Value

### Winning hand
- Rank
- Subrank?
- HandResult

### HandResult
- Value (eg. Full House)
- string output

