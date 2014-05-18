from lib.card import Card
from lib.cardgroup import CardGroup

d2 = Card(2,"Diamonds")
da = Card(14,"Diamonds")
sa = Card(14,"Spades")
s13 = Card(13,"Spades")
d13 = Card(13,"Diamonds")
c13 = Card(13,"Clubs")
h13 = Card(13, "Hearts")
d12 = Card(12,"Diamonds")
d10 = Card(10,"Diamonds")
d11 = Card(11,"Diamonds")
d6 = Card(6,"Diamonds")
d3 = Card(3,"Diamonds")
c12 = Card(12,"Clubs")
c10 = Card(10,"Clubs")
c11 = Card(11,"Clubs")
c6 = Card(6,"Clubs")
c3 = Card(3,"Clubs")
h12 = Card(12, "Hearts")
h10 = Card(10, "Hearts")
h11 = Card(11, "Hearts")
h6 = Card(6, "Hearts")
h3 = Card(3, "Hearts")

class TestCardGroup_no_hand:
    def setUp(self):
        self.no_hand = CardGroup([
                d2,
                d6,
                da,
                h11,
                c10,
                h13,
                d3
            ])

    def test_kickers(self):
        kickers = self.no_hand._kickers()
        assert bool(kickers) == True
        
        assert d6 in kickers
        assert da in kickers
        assert h11 in kickers
        assert c10 in kickers
        assert h13 in kickers

    def test_pair(self):
        pair = self.no_hand._pair()
        assert bool(pair) == False

    def test_trip(self):
        trip = self.no_hand._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.no_hand._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.no_hand._straight()
        print straight
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.no_hand._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.no_hand._flush()
        print flush
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.no_hand._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.no_hand._straight_flush()
        assert bool(straight_flush) == False

class TestCardGroup_pair:
    def setUp(self):
        self.pair = CardGroup([
                d2,
                sa,
                d3,
                d6,
                c11,
                h13,
                d11
            ])

    def test_kickers(self):
        kickers = self.pair._kickers()
        assert bool(kickers) == True
        
        assert d6 in kickers
        assert sa in kickers
        assert c11 in kickers
        assert d11 in kickers
        assert h13 in kickers

    def test_pair(self):
        pair = self.pair._pair()
        assert bool(pair) == True
        hand = pair['hand']
        kickers = pair['kickers']
        assert d6 in kickers
        assert sa in kickers
        assert c11 in hand
        assert d11 in hand
        assert h13 in kickers

    def test_trip(self):
        trip = self.pair._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.pair._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.pair._straight()
        print straight
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.pair._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.pair._flush()
        print flush
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.pair._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.pair._straight_flush()
        assert bool(straight_flush) == False

class TestCardGroup_trip:
    def setUp(self):
        self.trip = CardGroup([
                d2,
                da,
                s13,
                d13,
                c13,
                h10,
                d6
            ])

    def test_kickers(self):
        kickers = self.trip._kickers()
        assert bool(kickers) == True
        
        assert s13 in kickers
        assert da in kickers
        assert h10 in kickers
        assert d13 in kickers
        assert c13 in kickers

    def test_pair(self):
        trip = self.trip._pair()
        assert bool(trip) == True
        hand = trip['hand']
        kickers = trip['kickers']
        assert da in kickers
        assert s13 in hand
        assert d13 in hand
        assert c13 in kickers
        assert h10 in kickers

    def test_trip(self):
        trip = self.trip._trip()
        assert bool(trip) == True
        hand = trip['hand']
        kickers = trip['kickers']
        assert da in kickers
        assert s13 in hand
        assert d13 in hand
        assert c13 in hand
        assert h10 in kickers

    def test_quad(self):
        quad = self.trip._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.trip._straight()
        print straight
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.trip._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.trip._flush()
        print flush
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.trip._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.trip._straight_flush()
        assert bool(straight_flush) == False

class TestCardGroup_quad:
    def setUp(self):
        self.quad = CardGroup([
                d2,
                da,
                s13,
                d13,
                c13,
                h13,
                d6
            ])

    def test_kickers(self):
        kickers = self.quad._kickers()
        assert bool(kickers) == True
        
        assert s13 in kickers
        assert da in kickers
        assert h10 in kickers
        assert d13 in kickers
        assert c13 in kickers

    def test_pair(self):
        quad = self.quad._pair()
        assert bool(quad) == True
        hand = quad['hand']
        kickers = quad['kickers']
        assert da in kickers
        assert s13 in hand
        assert d13 in hand
        assert c13 in kickers
        assert h10 in kickers

    def test_quad(self):
        quad = self.quad._quad()
        assert bool(quad) == True
        hand = quad['hand']
        kickers = quad['kickers']
        assert da in kickers
        assert s13 in hand
        assert d13 in hand
        assert c13 in hand
        assert h10 in kickers

    def test_quad(self):
        quad = self.quad._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.quad._straight()
        print straight
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.quad._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.quad._flush()
        print flush
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.quad._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.quad._straight_flush()
        assert bool(straight_flush) == False
