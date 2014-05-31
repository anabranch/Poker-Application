from lib.baseclasses.generics import Table
from lib.tables import PokerHandTable
from lib.player import PokerPlayer

p1 = PokerPlayer(1234, "Bill")
p2 = PokerPlayer(123, "Bill")
p3 = PokerPlayer(1323, "Bill")
p4 = PokerPlayer(1243, "Bill")
p5 = PokerPlayer(1213, "Bill")

class TestTable:
    def setUp(self):
        self.table = Table()
        self.table.add_player(2, "x")

    def test_add(self):
        self.table.add_player(4, "r")
        assert len(self.table.active) == 2

    def test_remove(self):
        self.table.remove_by_seat(2)
        assert len(self.table.active) == 0

    def test_remove_2(self):
        self.table.remove_by_player("x")
        assert len(self.table.active) == 0

    def test_set_button_and_more(self):
        self.table.add_player(4, "r")
        self.table.add_player(5, "p")
        self.table.add_player(6, "g")
        self.table.add_player(10, "f")
        self.table.set_button(4)
        assert self.table.dealerposition == 4
        assert self.table.currentactor == 4
        self.table.next_active_player()
        assert self.table.currentactor == 5
        self.table.next_active_player()
        assert self.table.currentactor == 6
        self.table.next_active_player()
        assert self.table.currentactor == 10

class TestPokerTable:
    def setUp(self):
        self.table = PokerHandTable()
        self.table.add_player(2, p1)
        self.table.add_player(4, p2)
        self.table.add_player(5, p3)
        self.table.add_player(6, p4)
        self.table.add_player(10, p5)

    def test_set_button_and_more(self):
        self.table.set_button(4)
        self.table.assign_blinds()
        assert self.table.smallposition == 5
        assert self.table.bigposition == 6
        assert self.table.currentactor == 10

    def test_as_dict(self):
        self.table.set_button(4)
        self.table.assign_blinds()
        print self.table.as_dict()
        assert self.table.as_dict() == {
            "small": 5,
            "big": 6,
            "button": 4,
            "current_actor": 10
        }
