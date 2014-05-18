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
s10 = Card(10,"Spades")
c11 = Card(11,"Clubs")
c6 = Card(6,"Clubs")
c3 = Card(3,"Clubs")
h12 = Card(12, "Hearts")
h10 = Card(10, "Hearts")
h11 = Card(11, "Hearts")
h6 = Card(6, "Hearts")
h3 = Card(3, "Hearts")
d4 = Card(4, 'Diamonds')
c5 = Card(5, "Clubs")
d7 = Card(7, "Diamonds")
d8 = Card(8, "Diamonds")
d9 = Card(9, "Diamonds")

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
        assert h13 in kickers
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
        assert h13 in kickers

    def test_trip(self):
        trip = self.quad._trip()
        assert bool(trip) == True
        hand = trip['hand']
        kickers = trip['kickers']
        assert da in kickers
        assert s13 in hand
        assert d13 in hand
        assert c13 in hand
        assert h13 in kickers

    def test_quad(self):
        quad = self.quad._quad()
        assert bool(quad) == True
        hand = quad['hand']
        kickers = quad['kickers']
        assert da in kickers
        assert s13 in hand
        assert d13 in hand
        assert c13 in hand
        assert h13 in hand

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

class TestCardGroup_straight_and_flush:
    def setUp(self):
        self.straight_and_flush = CardGroup([
                d2,
                d8,
                d9,
                d12,
                c11,
                h10,
                da
            ])

    def test_kickers(self):
        kickers = self.straight_and_flush._kickers()
        assert bool(kickers) == True
        
        assert d9 in kickers
        assert d12 in kickers
        assert c11 in kickers
        assert h10 in kickers
        assert da in kickers

    def test_pair(self):
        straight = self.straight_and_flush._pair()
        assert bool(straight) == False

    def test_trip(self):
        trip = self.straight_and_flush._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.straight_and_flush._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.straight_and_flush._straight()
        print straight
        assert bool(straight) == True
        hand = straight['hand']
        assert d8 in hand
        assert d9 in hand
        assert d12 in hand
        assert c11 in hand
        assert h10 in hand

    def test_two_pair(self):
        two_pair = self.straight_and_flush._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.straight_and_flush._flush()
        print flush
        assert bool(flush) == True
        hand = flush['hand']
        assert d2 in hand
        assert d8 in hand
        assert d9 in hand
        assert d12 in hand
        assert da in hand

    def test_full_house(self):
        full_house = self.straight_and_flush._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.straight_and_flush._straight_flush()
        assert bool(straight_flush) == False

class TestCardGroup_low_straight:
    def setUp(self):
        self.low_straight = CardGroup([
                d2,
                da,
                h3,
                d4,
                c5,
                h10,
                d7
            ])

    def test_kickers(self):
        kickers = self.low_straight._kickers()
        assert bool(kickers) == True
        # assert d2 in kickers
        assert da in kickers
        # assert h3 in kickers
        assert d4 in kickers
        assert c5 in kickers
        assert h10 in kickers
        assert d7 in kickers

    def test_pair(self):
        pair = self.low_straight._pair()
        assert bool(pair) == False

    def test_trip(self):
        trip = self.low_straight._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.low_straight._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.low_straight._straight()
        print straight
        assert bool(straight) == True
        hand = straight['hand']
        assert d2 in hand
        assert da in hand
        assert h3 in hand
        assert d4 in hand
        assert c5 in hand

    def test_two_pair(self):
        two_pair = self.low_straight._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.low_straight._flush()
        print flush
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.low_straight._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.low_straight._straight_flush()
        assert bool(straight_flush) == False

class TestCardGroup_two_test_pair:
    def setUp(self):
        self.two_test_pair = CardGroup([
                d2,
                d8,
                c10,
                d11,
                c11,
                h10,
                da
            ])

    def test_kickers(self):
        kickers = self.two_test_pair._kickers()
        assert bool(kickers) == True
        assert c10 in kickers
        assert d11 in kickers
        assert c11 in kickers
        assert h10 in kickers
        assert da in kickers

    def test_pair(self):
        pair = self.two_test_pair._pair()
        assert bool(pair) == True
        hand = pair['hand']
        kickers = pair['kickers']
        assert c10 in kickers
        assert h10 in kickers
        assert da in kickers

    def test_trip(self):
        trip = self.two_test_pair._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.two_test_pair._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.two_test_pair._straight()
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.two_test_pair._two_pair()
        assert bool(two_pair) == True
        hand = two_pair['hand']
        kickers = two_pair['kickers']
        assert c10 in hand
        assert d11 in hand
        assert c11 in hand
        assert h10 in hand
        assert da in kickers

    def test_flush(self):
        flush = self.two_test_pair._flush()
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.two_test_pair._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.two_test_pair._straight_flush()
        assert bool(straight_flush) == False

class TestCardGroup_full_test_house:
    def setUp(self):
        self.full_test_house = CardGroup([
                d2,
                d8,
                c10,
                d11,
                c11,
                h10,
                s10
            ])

    def test_kickers(self):
        kickers = self.full_test_house._kickers()
        assert bool(kickers) == True
        assert c10 in kickers
        assert d11 in kickers
        assert c11 in kickers
        assert h10 in kickers
        assert s10 in kickers

    def test_pair(self):
        pair = self.full_test_house._pair()
        assert bool(pair) == True
        hand = pair['hand']
        kickers = pair['kickers']
        assert c10 in kickers
        assert d11 in hand
        assert c11 in hand
        assert h10 in kickers
        assert s10 in kickers

    def test_trip(self):
        trip = self.full_test_house._trip()
        assert bool(trip) == True
        hand = trip['hand']
        kickers = trip['kickers']
        assert c10 in hand
        assert d11 in kickers
        assert c11 in kickers
        assert h10 in hand
        assert s10 in hand

    def test_quad(self):
        quad = self.full_test_house._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.full_test_house._straight()
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.full_test_house._two_pair()
        assert bool(two_pair) == True
        hand = two_pair['hand']
        kickers = two_pair['kickers']
        assert c10 in hand
        assert d11 in hand
        assert c11 in hand
        assert h10 in hand
        assert s10 in kickers

    def test_flush(self):
        flush = self.full_test_house._flush()
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.full_test_house._full_house()
        assert bool(full_house) == True
        hand = full_house['hand']
        assert c10 in hand
        assert d11 in hand
        assert c11 in hand
        assert h10 in hand
        assert s10 in hand

    def test_straight_flush(self):
        straight_flush = self.full_test_house._straight_flush()
        assert bool(straight_flush) == False

class TestCardGroup_full_test_house_double_trips:
    def setUp(self):
        self.full_test_house_double_trips = CardGroup([
                d2,
                h11,
                c10,
                d11,
                c11,
                h10,
                s10
            ])

    def test_kickers(self):
        kickers = self.full_test_house_double_trips._kickers()
        assert bool(kickers) == True
        assert c10 in kickers
        assert d11 in kickers
        assert c11 in kickers
        assert h10 in kickers
        assert h11 in kickers

    def test_pair(self):
        pair = self.full_test_house_double_trips._pair()
        assert bool(pair) == True
        hand = pair['hand']
        kickers = pair['kickers']
        assert c10 in kickers
        assert d11 in hand
        assert h11 in hand
        assert h10 in kickers
        assert c11 in kickers

    def test_trip(self):
        trip = self.full_test_house_double_trips._trip()
        assert bool(trip) == True
        hand = trip['hand']
        kickers = trip['kickers']
        assert c10 in kickers
        assert d11 in hand
        assert c11 in hand
        assert h11 in hand
        assert c10 in kickers

    def test_quad(self):
        quad = self.full_test_house_double_trips._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.full_test_house_double_trips._straight()
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.full_test_house_double_trips._two_pair()
        assert bool(two_pair) == True
        hand = two_pair['hand']
        kickers = two_pair['kickers']
        assert c10 in hand
        assert d11 in hand
        assert h11 in hand
        assert h10 in hand
        assert c11 in kickers

    def test_flush(self):
        flush = self.full_test_house_double_trips._flush()
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.full_test_house_double_trips._full_house()
        assert bool(full_house) == True
        hand = full_house['hand']
        print hand
        assert c10 in hand
        assert d11 in hand
        assert c11 in hand
        assert h10 in hand
        assert h11 in hand

    def test_straight_flush(self):
        straight_flush = self.full_test_house_double_trips._straight_flush()
        assert bool(straight_flush) == False
