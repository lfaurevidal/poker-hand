def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

def convert_value_to_int(rank):
    match rank:
        case "J":
            return 11
        case "Q":
            return 12
        case "K":
            return 13
        case "A":
            return 14
        case _:
            parsedTuple = intTryParse(rank)
            if (parsedTuple[1]):
                return parsedTuple[0]
            else: 
                return 0

class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
        self.integerValue = convert_value_to_int(value)

    def __eq__(self, other):
        return self.suit==other.suit\
               and self.value==other.value
    
    def __hash__(self):
        return hash(('suit', self.suit,
                 'value', self.value))


