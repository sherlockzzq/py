import random
suits = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
class Card:
	"""
	Your Card​ class will be used to represent playing cards. Instances
	will have attributes suit​ and rank​. Suit may be one of Spades, Clubs,
	Hearts, or Diamonds. Rank may be one of 2, 3, 4, 5, 6, 7, 8, 9, 10,
	Jack, Queen, King, or Ace. This class must also implement a class
	variable, values​, a dictionary that maps ranks to their respective
	values.
	"""
	values = {"Ace":11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King": 10 }
	def __init__(self, suit, rank):
		if suit in suits:
			self.suit = suit
		if rank in ranks:
			self.rank = rank


class Hand:
	"""
	Your Hand​ class will represent a single blackjack hand. Instances of
	your Hand​ class must, at minimum, implement an attribute, cards​, that
	maintains a list of the instances of the Card​ class currently included
	in the hand. The constructor must set this attribute equal to an empty
	list at instantiation. Your Hand​ class must also implement a method,
	add_cards​, that takes an arbitrary number of instances of the card
	class and adds each to the cards​ list attribute, and a method,
	current_value​, that calculates the value(s) that the current cards
	represent in the game of blackjack. Note that the numeric cards are
	worth their respective numbers, the face cards (King, Queen, and Jack)
	are worth 10, and the Ace card is with either 11 or one. A hand
	including an Ace card has multiple possible values. Other hands have
	one possible value.
	"""
	def __init__ (self):
		self.cards = []

	def add_cards(self, card):
		self.cards.append(card)

	def current_value(self):
		ace = 0
		val = 0
		res = []
		for card in self.hand:
			if card.rank == 'Ace':
				ace += 1
			val += card.values[card.rank]
		res.add(val)
		while ace > 0:
			val -= 10
			ace -= 1
			res.append(val)
		return res

class Player(Hand):
	"""
	Your Player​ class will represent a blackjack player. Note that a
	dealer can also be a player, but we'll ignore that for now. Instances
	of your Player​ class must implement attributes first_name​, last_name​,
	purse​ (the dollar amount the player has available to bet), and hand​.
	The first_name​, last_name​, and purse​ attributes should be set by the
	constructor. Please accept them in that order as positional arguments
	to __init__​. The constructor should also initialize the instance's
	hands​ attribute as None​.
	"""
	def __init__(self, first_name, second_name, purse):
		Hand.__init__(self)
		self.first_name = first_name
		self.second_name = second_name
		self.purse = purse

class Deck():
	"""
	Your Deck​ class represents a deck of playing cards. Note that a single
	deck of playing cards comprises 52 unique cards, one for each
	suit/rank combination. Your deck class should implement two methods:
	shuffle​ and deal​. The shuffle​ method should call a generator function
	(also defined in the class) and set an instance attribute, cards​,
	equal to the resulting generator object. The deal​ method should return
	the next instance of the Card​ class yielded from the generator. Note
	that after a single call to the shuffle​ method, your deal​ method
	should support 52 successive calls, each producing a random, unique
	(i.e., a deck cannot deal the same card more than once from itself)
	instance of the Card​ class. After all 52 cards have been dealt, calls
	to the deal​ method should result in a return value of None​. Your Deck
	class must implement a constructor that takes zero arguments (aside
	from the instance reference, self) and sets its cards​ attribute to the
	result of a call to shuffle​, so that it's immediately ready to deal.
	"""

	def __init__(self):
		self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
		self.shuffle()

	def shuffle(self):
		self.card = self.deck_generator()

	def deck_generator(self):
		for i in range(0, len(self.cards) + 1):
			r = int(random.randrange(i, len(self.cards)))
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
			yield self.cards[i]

	def deal(self):
		try:
			return next(self.card)
		except StopIteration:
			return None







