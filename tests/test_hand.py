from lib.hand import PokerHand
from lib.table import PokerHandTable
from lib.player import PokerPlayer

class TestPokerHand:
    def setUp(self):
        p1 = PokerPlayer(1234, "Bill")
        p2 = PokerPlayer(123, "Bill")
        p3 = PokerPlayer(1323, "Bill")
        p4 = PokerPlayer(1243, "Bill")
        p5 = PokerPlayer(1213, "Bill")
        table = PokerHandTable()
        table.add_player(2, p1)
        table.add_player(4, p2)
        table.add_player(5, p3)
        table.add_player(6, p4)
        table.add_player(10, p5)
        self.hand = PokerHand(123,table)

    def test_pregame(self):
        assert self.hand.currentstate == None
        self.hand.pregame(4)
        print self.hand.bigblind
        assert self.hand.bigblind == 20
        assert self.hand.smallblind == 10
        assert self.hand.minbet == 20
        assert self.hand.table.smallposition == 5
        assert self.hand.table.bigposition == 6
        assert self.hand.table.dealerposition == 4
        assert self.hand.currentstate == "dealpocket"

    def test_dealpocket(self):
        self.hand.pregame(4)
        cards = list(reversed(self.hand.deck.local_card_copy()))
        self.hand.deal_pocket()
        assert len(self.hand.deck) == 42
        assert cards[4] in self.hand.table.active[4].pocket.cards
        assert cards[9] in self.hand.table.active[4].pocket.cards
        assert cards[0] in self.hand.table.active[5].pocket.cards
        assert cards[5] in self.hand.table.active[5].pocket.cards
        assert cards[2] in self.hand.table.active[10].pocket.cards
        assert cards[7] in self.hand.table.active[10].pocket.cards
        assert cards[2] in self.hand.table.active[10].pocket.cards
        assert cards[7] in self.hand.table.active[10].pocket.cards
        assert self.hand.table.currentactor == 10
        assert self.hand.currentstate == 'preflopbetting'

    def test_preflop_betting(self):
        self.hand.pregame(4)
        self.hand.deal_pocket()
        print self.hand.hand_status()
        assert self.hand.action() == True

