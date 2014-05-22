from lib.hand import PokerHand
from lib.player import Player

p1 = Player(1234, "Bill")
p2 = Player(123, "Bill")
p3 = Player(1323, "Bill")
p4 = Player(1243, "Bill")
p5 = Player(1213, "Bill")

class TestPokerHand:
    def setUp(self):
        self.g = PokerHand()

    def test_position_count(self):
        assert len(self.g.positions) == 12

    def test_players_count(self):
        assert len(self.g.players) == 0

    def test_set_players_1(self):
        positions = dict([(x,None) for x in range(1,13)])
        positions[2] = p1
        try:
            self.g._set_players(positions)
            assert False
        except ValueError:
            assert True

    def test_set_players(self):
        positions = dict([(x,None) for x in range(1,13)])
        positions[2] = p1
        positions[5] = p2
        assert len(self.g.players) == 0
        self.g._set_players(positions)
        assert self.g.positions[2] == p1
        assert self.g.positions[5] == p2
        assert len(self.g.players) == 2

    def test_get_player(self):
        positions = dict([(x,None) for x in range(1,13)])
        positions[2] = p1
        positions[5] = p2
        self.g._set_players(positions)
        assert self.g.get_player_from_position(2) == p1

    def test_get_position(self):
        positions = dict([(x,None) for x in range(1,13)])
        positions[2] = p1
        positions[5] = p2
        self.g._set_players(positions)
        assert self.g.get_position_from_player(p1) == 2

    def test_set_blinds_2(self):
        positions = dict([(x,None) for x in range(1,13)])
        positions[2] = p1
        positions[5] = p2
        self.g._set_players(positions)
        self.g._set_blinds()
        assert self.g.bigposition == self.g.buttonposition
        assert self.g.get_big_blind_player() == self.g.get_button_player()
        assert self.g.smallposition != 0
        assert self.g.smallposition != self.g.bigposition

    def test_set_blinds_3(self):
        positions = dict([(x,None) for x in range(1,13)])
        positions[2] = p1
        positions[5] = p2
        positions[3] = p3
        positions[9] = p4
        positions[7] = p5
        self.g._set_players(positions)
        self.g._set_blinds(2)
        assert self.g.buttonposition == 2
        assert self.g.smallposition == 3
        assert self.g.bigposition == 5
        assert self.g.get_button_player() == p1
        assert self.g.get_big_blind_player() == p2
        assert self.g.get_small_blind_player() == p3