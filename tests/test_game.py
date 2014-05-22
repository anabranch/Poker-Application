from lib.hand import PokerHand
from lib.player import Player

p1 = Player(1234, "Bill")
p2 = Player(123, "Bill")
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