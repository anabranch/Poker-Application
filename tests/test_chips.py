from lib.baseclasses.generics import Chips

class TestChips:
    def setUp(self):
        self.c = Chips()

    def test_stack(self):
        self.c.set_stack(5000)
        assert self.c.stack == 5000
        self.c.remove(2000)
        assert self.c.stack == 3000
        self.c.add(20)
        assert self.c.stack == 3020
        assert self.c.as_dict() == {"stack":3020}

    def test_stack_2(self):
        self.c.set_stack(5000)
        assert self.c.stack == 5000
        try:
            self.c.remove(6000)
            assert False
        except ValueError:
            assert self.c.stack == 5000
