from app import *
from card import *
from hand import *
import unittest

# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C AH
# Black: 2H 4S 4C 2D 4H  White: 2S 8S AS QS 3S
# Black: 2H 3D 5S 9C KD  White: 2C 3H 4S 8C KH
# Black: 2H 3D 5S 9C KD  White: 2D 3H 5C 9S KH

# White wins. - with high card: Ace 
# Black wins. - with full house: 4 over 2 
# Black wins. - with high card: 9
# Tie.

# HighCard
# Pair
# TwoPairs
# ThreeOfAKind
# Straight
# Flush
# FullHouse
# FourOfAKind
# StraightFlush

# class TestPokerHand_FirstHand(unittest.TestCase):
#     def test_winningHand(self):
#         self.assertEqual(determineBestHandResult("2H 3D 5S 9C KD", "2C 3H 4S 8C AH"), "HighCard")

# class TestPokerHand_SecondHand(unittest.TestCase):
#     def test_winningHand(self):
#         self.assertEqual(determineBestHandResult("2H 4S 4C 2D 4H", "2S 8S AS QS 3S"), "FullHouse")

# class TestPokerHand_ThirdHand(unittest.TestCase):
#     def test_winningHand(self):
#         self.assertEqual(determineBestHandResult("2H 3D 5S 9C KD", "2C 3H 4S 8C KH"), "HighCard")

# class TestPokerHand_FourthHand(unittest.TestCase):
#     def test_winningHand(self):
#         self.assertEqual(determineBestHandResult("2H 3D 5S 9C KD", "2D 3H 5C 9S KH"), "HighCard")



class TestPokerHand_ValidCard(unittest.TestCase):
    def test_validCard(self):
        self.assertTrue(isCardValid(Card("2", "H")))
    def test_validCard2(self):
        self.assertTrue(isCardValid(Card("3", "D")))
    def test_invalidCard_InvalidSuit(self):
        self.assertFalse(isCardValid(Card("2", "A")))
    def test_invalidCard_InvalidValue(self):
        self.assertFalse(isCardValid(Card("13", "C")))
    def test_invalidCard_InvalidSuitAndValue(self):
        self.assertFalse(isCardValid(Card("-2", "L")))
    def test_invalidCard_MissingSuitInvalidValue(self):
        self.assertFalse(isCardValid(Card("012", "")))
    def test_invalidCard_Empty(self):
        self.assertFalse(isCardValid(Card("", "")))
    def test_invalidCard_InvalidInput(self):
        self.assertFalse(isCardValid(Card("", "hgfuyoegfonaw2343")))

class TestPokerHand_ValidHand(unittest.TestCase):
    def test_validHand(self):
        self.assertTrue(isHandValid(Hand([Card("2", "H"), Card("3", "D"),Card("5", "S"), Card("9", "C"), Card("K", "D")])))
    def test_invalidHand_TooManyCards(self):
        self.assertFalse(isHandValid(Hand([Card("2", "H"), Card("3", "D"),Card("5", "S"), Card("9", "C"), Card("K", "D"), Card("4", "D")])))
    def test_invalidHand_TooManyCardsWithDuplicates(self):
        self.assertFalse(isHandValid(Hand([Card("2", "H"), Card("3", "D"),Card("5", "S"), Card("9", "C"), Card("3", "D")])))
    def test_invalidHand_SingleCard(self):
        self.assertFalse(isHandValid(Hand([Card("2", "H")])))
    def test_invalidHand_WrongType(self):
        self.assertFalse(isHandValid(""))
    def test_invalidHand_Empty(self):
        self.assertFalse(isHandValid(Hand([])))
    def test_invalidHand_InvalidCard(self):
        self.assertFalse(isHandValid(Hand([Card("2", "H"), Card("3", "D"),Card("5", "S"), Card("9", "C"), Card("16", "D")])))
    def test_invalidHand_DuplicateCards(self):
        self.assertFalse(isHandValid(Hand([Card("2", "H"), Card("9", "S"),Card("J", "H"), Card("J", "H"), Card("Q", "D")])))
# Test for:
# Output
# Actual winning hand value

# Have one method per result => Does this hand have a Straight Flush? 


class TestPokerHand_Card_ConvertValueToInt(unittest.TestCase):
    def test_validConversionJ(self):
        self.assertEqual(convert_value_to_int("J"), 11)
    def test_validConversionQ(self):
        self.assertEqual(convert_value_to_int("Q"), 12)
    def test_validConversionK(self):
        self.assertEqual(convert_value_to_int("K"), 13)
    def test_validConversionA(self):
        self.assertEqual(convert_value_to_int("A"), 14)
    def test_validConversion2(self):
        self.assertEqual(convert_value_to_int("2"), 2)
    def test_validConversion10(self):
        self.assertEqual(convert_value_to_int("10"), 10)
    def test_invalidConversion(self):
        self.assertEqual(convert_value_to_int("B"), 0)
    def test_invalid_Empty_Conversion(self):
        self.assertEqual(convert_value_to_int(""), 0)