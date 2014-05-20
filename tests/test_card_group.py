from lib.card import Card
from lib.cardgroups import ValuedCardGroup

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
d5 = Card(5, "Diamonds")

class TestCardGroup_no_hand:
    def setUp(self):
        self.no_hand = ValuedCardGroup([
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
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.no_hand._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.no_hand._flush()
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.no_hand._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.no_hand._straight_flush()
        assert bool(straight_flush) == False

    def test_best_hand(self):
        assert self.no_hand.best_hand() == self.no_hand._kickers()

class TestCardGroup_pair:
    def setUp(self):
        self.pair = ValuedCardGroup([
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
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.pair._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.pair._flush()
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.pair._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.pair._straight_flush()
        assert bool(straight_flush) == False

    def test_best_hand(self):
        assert self.pair.best_hand() == self.pair._pair()

class TestCardGroup_trip:
    def setUp(self):
        self.trip = ValuedCardGroup([
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
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.trip._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.trip._flush()
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.trip._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.trip._straight_flush()
        assert bool(straight_flush) == False

    def test_best_hand(self):
        assert self.trip.best_hand() == self.trip._trip()

class TestCardGroup_quad:
    def setUp(self):
        self.quad = ValuedCardGroup([
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
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.quad._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.quad._flush()
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.quad._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.quad._straight_flush()
        assert bool(straight_flush) == False

    def test_best_hand(self):
        assert self.quad.best_hand() == self.quad._quad()

class TestCardGroup_straight_and_flush:
    def setUp(self):
        self.straight_and_flush = ValuedCardGroup([
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
        assert bool(straight) == True
        hand = straight['hand']
        assert len(hand) == 5
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
        assert bool(flush) == True
        hand = flush['hand']
        assert len(hand) == 5
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

    def test_best_hand(self):
        assert self.straight_and_flush.best_hand() == self.straight_and_flush._flush()

class TestCardGroup_almost_straight:
    def setUp(self):
        self.almost_straight = ValuedCardGroup([
                d2,
                d3,
                d4,
                h12,
                c11,
                h10,
                da
            ])

    def test_kickers(self):
        kickers = self.almost_straight._kickers()
        assert bool(kickers) == True
        
        assert h12 in kickers
        assert c11 in kickers
        assert d4 in kickers
        assert h10 in kickers
        assert da in kickers

    def test_pair(self):
        straight = self.almost_straight._pair()
        assert bool(straight) == False

    def test_trip(self):
        trip = self.almost_straight._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.almost_straight._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.almost_straight._straight()
        assert bool(straight) == False

    def test_two_pair(self):
        two_pair = self.almost_straight._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.almost_straight._flush()
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.almost_straight._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.almost_straight._straight_flush()
        assert bool(straight_flush) == False

    def test_best_hand(self):
        assert self.almost_straight.best_hand() == self.almost_straight._kickers()

class TestCardGroup_low_straight:
    def setUp(self):
        self.low_straight = ValuedCardGroup([
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
        assert bool(straight) == True
        hand = straight['hand']
        assert len(hand) == 5
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
        assert bool(flush) == False

    def test_full_house(self):
        full_house = self.low_straight._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.low_straight._straight_flush()
        assert bool(straight_flush) == False

    def test_best_hand(self):
        assert self.low_straight.best_hand() == self.low_straight._straight()

class TestCardGroup_two_test_pair:
    def setUp(self):
        self.two_test_pair = ValuedCardGroup([
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

    def test_best_hand(self):
        assert self.two_test_pair.best_hand() == self.two_test_pair._two_pair()

class TestCardGroup_full_test_house:
    def setUp(self):
        self.full_test_house = ValuedCardGroup([
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

    def test_best_hand(self):
        assert self.full_test_house.best_hand() == self.full_test_house._full_house()

class TestCardGroup_full_test_house_double_trips:
    def setUp(self):
        self.full_test_house_double_trips = ValuedCardGroup([
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
        assert c10 in hand
        assert d11 in hand
        assert c11 in hand
        assert h10 in hand
        assert h11 in hand

    def test_straight_flush(self):
        straight_flush = self.full_test_house_double_trips._straight_flush()
        assert bool(straight_flush) == False

    def test_best_hand(self):
        assert self.full_test_house_double_trips.best_hand() == self.full_test_house_double_trips._full_house()

class TestCardGroup_straight_test_flush:
    def setUp(self):
        self.straight_test_flush = ValuedCardGroup([
                d2,
                d8,
                d9,
                d10,
                d11,
                d12,
                s10
            ])

    def test_kickers(self):
        kickers = self.straight_test_flush._kickers()
        assert bool(kickers) == True
        assert d11 in kickers
        assert d10 in kickers
        assert s10 in kickers
        assert d12 in kickers
        assert d9 in kickers

    def test_pair(self):
        pair = self.straight_test_flush._pair()
        assert bool(pair) == True
        hand = pair['hand']
        kickers = pair['kickers']
        assert d11 in kickers
        assert d10 in hand
        assert s10 in hand
        assert d12 in kickers
        assert d9 in kickers

    def test_trip(self):
        trip = self.straight_test_flush._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.straight_test_flush._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.straight_test_flush._straight()
        assert bool(straight) == True
        hand = straight['hand']
        assert len(hand) == 5
        assert d8 in hand
        assert d9 in hand
        assert d10 in hand
        assert d11 in hand
        assert d12 in hand

    def test_two_pair(self):
        two_pair = self.straight_test_flush._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.straight_test_flush._flush()
        assert bool(flush) == True
        hand = flush['hand']
        assert len(hand) == 5
        assert d8 in hand
        assert d9 in hand
        assert d10 in hand
        assert d11 in hand
        assert d12 in hand

    def test_full_house(self):
        full_house = self.straight_test_flush._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.straight_test_flush._straight_flush()
        assert bool(straight_flush) == True
        hand = straight_flush['hand']
        assert len(hand) == 5
        assert d8 in hand
        assert d9 in hand
        assert d10 in hand
        assert d11 in hand
        assert d12 in hand

    def test_best_hand(self):
        assert self.straight_test_flush.best_hand() == self.straight_test_flush._straight_flush()

class TestCardGroup_straight_long_flush:
    def setUp(self):
        self.straight_long_flush = ValuedCardGroup([
                d2,
                d8,
                d9,
                d10,
                d11,
                d12,
                da
            ])

    def test_kickers(self):
        kickers = self.straight_long_flush._kickers()
        assert bool(kickers) == True
        assert d11 in kickers
        assert d10 in kickers
        assert da in kickers
        assert d12 in kickers
        assert d9 in kickers

    def test_pair(self):
        pair = self.straight_long_flush._pair()
        assert bool(pair) == False

    def test_trip(self):
        trip = self.straight_long_flush._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.straight_long_flush._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.straight_long_flush._straight()
        assert bool(straight) == True
        hand = straight['hand']
        assert len(hand) == 5
        assert d8 in hand
        assert d9 in hand
        assert d10 in hand
        assert d11 in hand
        assert d12 in hand

    def test_two_pair(self):
        two_pair = self.straight_long_flush._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.straight_long_flush._flush()
        assert bool(flush) == True
        hand = flush['hand']
        assert len(hand) == 5
        assert da in hand
        assert d9 in hand
        assert d10 in hand
        assert d11 in hand
        assert d12 in hand

    def test_full_house(self):
        full_house = self.straight_long_flush._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.straight_long_flush._straight_flush()
        assert bool(straight_flush) == True
        hand = straight_flush['hand']
        assert len(hand) == 5
        assert d8 in hand
        assert d9 in hand
        assert d10 in hand
        assert d11 in hand
        assert d12 in hand

class TestCardGroup_straight_low_flush:
    def setUp(self):
        self.straight_low_flush = ValuedCardGroup([
                d2,
                d3,
                d4,
                d5,
                c11,
                h12,
                da
            ])

    def test_kickers(self):
        kickers = self.straight_low_flush._kickers()
        assert bool(kickers) == True
        assert c11 in kickers
        assert d5 in kickers
        assert da in kickers
        assert h12 in kickers
        assert d4 in kickers

    def test_pair(self):
        pair = self.straight_low_flush._pair()
        assert bool(pair) == False

    def test_trip(self):
        trip = self.straight_low_flush._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.straight_low_flush._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.straight_low_flush._straight()
        assert bool(straight) == True
        hand = straight['hand']
        assert len(hand) == 5
        assert d2 in hand
        assert d3 in hand
        assert d4 in hand
        assert d5 in hand
        assert da in hand

    def test_two_pair(self):
        two_pair = self.straight_low_flush._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.straight_low_flush._flush()
        assert bool(flush) == True
        hand = flush['hand']
        assert len(hand) == 5
        assert d2 in hand
        assert d3 in hand
        assert d4 in hand
        assert d5 in hand
        assert da in hand

    def test_full_house(self):
        full_house = self.straight_low_flush._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.straight_low_flush._straight_flush()
        assert bool(straight_flush) == True
        hand = straight_flush['hand']
        assert len(hand) == 5
        assert d2 in hand
        assert d3 in hand
        assert d4 in hand
        assert d5 in hand
        assert da in hand

    def test_best_hand(self):
        assert self.straight_low_flush.best_hand() == self.straight_low_flush._straight_flush()


class TestCardGroup_straight_low_long_flush:
    def setUp(self):
        self.straight_low_long_flush = ValuedCardGroup([
                d2,
                d3,
                d4,
                d5,
                d6,
                d7,
                da
            ])

    def test_kickers(self):
        kickers = self.straight_low_long_flush._kickers()
        assert bool(kickers) == True
        assert d7 in kickers
        assert d6 in kickers
        assert d5 in kickers
        assert da in kickers
        assert d4 in kickers

    def test_pair(self):
        pair = self.straight_low_long_flush._pair()
        assert bool(pair) == False

    def test_trip(self):
        trip = self.straight_low_long_flush._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.straight_low_long_flush._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.straight_low_long_flush._straight()
        assert bool(straight) == True
        hand = straight['hand']
        assert len(hand) == 5
        assert d7 in hand
        assert d6 in hand
        assert d5 in hand
        assert d3 in hand
        assert d4 in hand

    def test_two_pair(self):
        two_pair = self.straight_low_long_flush._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.straight_low_long_flush._flush()
        assert bool(flush) == True
        hand = flush['hand']
        assert len(hand) == 5
        assert d6 in hand
        assert d7 in hand
        assert d4 in hand
        assert d5 in hand
        assert da in hand

    def test_full_house(self):
        full_house = self.straight_low_long_flush._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.straight_low_long_flush._straight_flush()
        assert bool(straight_flush) == True
        hand = straight_flush['hand']
        assert len(hand) == 5
        assert d7 in hand
        assert d6 in hand
        assert d5 in hand
        assert d3 in hand
        assert d4 in hand

    def test_best_hand(self):
        assert self.straight_low_long_flush.best_hand() == self.straight_low_long_flush._straight_flush()

class TestCardGroup_straight_low_flush_long_two:
    def setUp(self):
        self.straight_low_flush_long_two = ValuedCardGroup([
                d2,
                d3,
                d4,
                d5,
                d8,
                d9,
                da
            ])

    def test_kickers(self):
        kickers = self.straight_low_flush_long_two._kickers()
        assert bool(kickers) == True
        assert d4 in kickers
        assert d5 in kickers
        assert d9 in kickers
        assert da in kickers
        assert d8 in kickers

    def test_pair(self):
        pair = self.straight_low_flush_long_two._pair()
        assert bool(pair) == False

    def test_trip(self):
        trip = self.straight_low_flush_long_two._trip()
        assert bool(trip) == False

    def test_quad(self):
        quad = self.straight_low_flush_long_two._quad()
        assert bool(quad) == False

    def test_straight(self):
        straight = self.straight_low_flush_long_two._straight()
        assert bool(straight) == True
        hand = straight['hand']
        assert len(hand) == 5
        print hand
        assert d2 in hand
        assert da in hand
        assert d5 in hand
        assert d3 in hand
        assert d4 in hand

    def test_two_pair(self):
        two_pair = self.straight_low_flush_long_two._two_pair()
        assert bool(two_pair) == False

    def test_flush(self):
        flush = self.straight_low_flush_long_two._flush()
        assert bool(flush) == True
        hand = flush['hand']
        assert len(hand) == 5
        assert d8 in hand
        assert d4 in hand
        assert d9 in hand
        assert d5 in hand
        assert da in hand

    def test_full_house(self):
        full_house = self.straight_low_flush_long_two._full_house()
        assert bool(full_house) == False

    def test_straight_flush(self):
        straight_flush = self.straight_low_flush_long_two._straight_flush()
        assert bool(straight_flush) == True
        hand = straight_flush['hand']
        assert len(hand) == 5
        print hand
        assert da in hand
        assert d2 in hand
        assert d5 in hand
        assert d3 in hand
        assert d4 in hand

    def test_best_hand(self):
        assert self.straight_low_flush_long_two.best_hand() == self.straight_low_flush_long_two._straight_flush()