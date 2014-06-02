from lib.baseclasses.generics import Card
from lib.ranker import *
from random import shuffle

def pretty(d, indent=2):
   for key, value in d.iteritems():
      print '\t' * indent + str(key)
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print '\t' * (indent+1) + str(value)


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



class TestRankerNoHand:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_no_hand(self):
        result = get_no_hand(self.no_hand_1)
        kickers = get_kickers(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_2(self):
        result = get_no_hand(self.hand_is_pair_1)
        kickers = get_kickers(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_3(self):
        result = get_no_hand(self.hand_is_pair_2)
        kickers = get_kickers(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_4(self):
        result = get_no_hand(self.hand_is_two_two_kind_1)
        kickers = get_kickers(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_5(self):
        result = get_no_hand(self.hand_is_three_kind_1)
        kickers = get_kickers(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_6(self):
        result = get_no_hand(self.hand_is_double_trips)
        kickers = get_kickers(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_7(self):
        result = get_no_hand(self.hand_is_four_kind_1)
        kickers = get_kickers(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_8(self):
        result = get_no_hand(self.hand_is_full_house_1)
        kickers = get_kickers(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_9(self):
        result = get_no_hand(self.hand_is_full_house_2)
        kickers = get_kickers(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_10(self):
        result = get_no_hand(self.hand_is_full_house_3)
        kickers = get_kickers(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_11(self):
        result = get_no_hand(self.hand_is_almost_straight)
        kickers = get_kickers(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_12(self):
        result = get_no_hand(self.hand_is_high_straight_1)
        kickers = get_kickers(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_13(self):
        result = get_no_hand(self.hand_is_low_straight)
        kickers = get_kickers(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_14(self):
        result = get_no_hand(self.hand_is_flush_1)
        kickers = get_kickers(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_15(self):
        result = get_no_hand(self.hand_is_straight_flush_1)
        kickers = get_kickers(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_16(self):
        result = get_no_hand(self.hand_is_straight_flush_2)
        kickers = get_kickers(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_17(self):
        result = get_no_hand(self.hand_is_straight_flush_3)
        kickers = get_kickers(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_18(self):
        result = get_no_hand(self.hand_is_straight_flush_4)
        kickers = get_kickers(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

    def test_no_hand_19(self):
        result = get_no_hand(self.hand_is_straight_flush_5)
        kickers = get_kickers(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result != {}
        assert result['name'] == "High Card"
        assert result['hand_rank'] == 0
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        print kickers
        assert result["ordered_kickers"] == kickers

class TestRankerTwoKind:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_two_kind(self):
        result = get_two_kind(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == {}

    def test_two_kind_2(self):
        result = get_two_kind(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 11
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_3(self):
        result = get_two_kind(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 11
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_4(self):
        result = get_two_kind(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 14
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_5(self):
        result = get_two_kind(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 13
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_6(self):
        result = get_two_kind(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 11
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_7(self):
        result = get_two_kind(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 13
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_8(self):
        result = get_two_kind(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 13
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_9(self):
        result = get_two_kind(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 13
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_10(self):
        result = get_two_kind(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 11
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_11(self):
        result = get_two_kind(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == {}

    def test_two_kind_12(self):
        result = get_two_kind(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result == {}

    def test_two_kind_13(self):
        result = get_two_kind(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result == {}

    def test_two_kind_14(self):
        result = get_two_kind(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 14
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_15(self):
        result = get_two_kind(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 3
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 10
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_two_kind_16(self):
        result = get_two_kind(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result == {}

    def test_two_kind_17(self):
        result = get_two_kind(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result == {}

    def test_two_kind_18(self):
        result = get_two_kind(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result == {}

    def test_two_kind_19(self):
        result = get_two_kind(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result == {}


class TestRankerTwoTwoKind:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_two_two_kind(self):
        result = get_two_two_kind(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == {}

    def test_two_two_kind_2(self):
        result = get_two_two_kind(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Two Pair"
        assert result['hand_rank'] == 2
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 1
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 11
        assert result["two_kind_value_2"] == 10
        assert result["ordered_kickers"] != []

    def test_two_two_kind_3(self):
        result = get_two_two_kind(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result == {}

    def test_two_two_kind_4(self):
        result = get_two_two_kind(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Two Pair"
        assert result['hand_rank'] == 2
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 1
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 14
        assert result["two_kind_value_2"] == 13
        assert result["ordered_kickers"] != []

    def test_two_two_kind_5(self):
        result = get_two_two_kind(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result == {}

    def test_two_two_kind_6(self):
        result = get_two_two_kind(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result != {}
        assert result['name'] == "Two Pair"
        assert result['hand_rank'] == 2
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 1
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 11
        assert result["two_kind_value_2"] == 10
        assert result["ordered_kickers"] != []

    def test_two_two_kind_7(self):
        result = get_two_two_kind(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result == {}

    def test_two_two_kind_8(self):
        result = get_two_two_kind(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Two Pair"
        assert result['hand_rank'] == 2
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 1
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 13
        assert result["two_kind_value_2"] == 6
        assert result["ordered_kickers"] != []

    def test_two_two_kind_9(self):
        result = get_two_two_kind(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result != {}
        assert result['name'] == "Two Pair"
        assert result['hand_rank'] == 2
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 1
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 13
        assert result["two_kind_value_2"] == 6
        assert result["ordered_kickers"] != []

    def test_two_two_kind_10(self):
        result = get_two_two_kind(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result != {}
        assert result['name'] == "Two Pair"
        assert result['hand_rank'] == 2
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 1
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == 11
        assert result["two_kind_value_2"] == 10
        assert result["ordered_kickers"] != []

    def test_two_two_kind_11(self):
        result = get_two_two_kind(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == {}

    def test_two_two_kind_12(self):
        result = get_two_two_kind(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result == {}

    def test_two_two_kind_13(self):
        result = get_two_two_kind(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result == {}

    def test_two_two_kind_14(self):
        result = get_two_two_kind(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result == {}

    def test_two_two_kind_15(self):
        result = get_two_two_kind(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result == {}

    def test_two_two_kind_16(self):
        result = get_two_two_kind(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result == {}

    def test_two_two_kind_17(self):
        result = get_two_two_kind(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result == {}

    def test_two_two_kind_18(self):
        result = get_two_two_kind(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result == {}

    def test_two_two_kind_19(self):
        result = get_two_two_kind(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result == {}

class TestRankerThreeKind:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_three_kind(self):
        result = get_three_kind(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == {}

    def test_three_kind_2(self):
        result = get_three_kind(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result == {}

    def test_three_kind_3(self):
        result = get_three_kind(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result == {}

    def test_three_kind_4(self):
        result = get_three_kind(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result == {}

    def test_three_kind_5(self):
        result = get_three_kind(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Three of a Kind"
        assert result['hand_rank'] == 3
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 2
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == 13
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_three_kind_6(self):
        result = get_three_kind(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result != {}
        assert result['name'] == "Three of a Kind"
        assert result['hand_rank'] == 3
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 2
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == 11
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_three_kind_7(self):
        result = get_three_kind(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Three of a Kind"
        assert result['hand_rank'] == 3
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 2
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == 13
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_three_kind_8(self):
        result = get_three_kind(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Three of a Kind"
        assert result['hand_rank'] == 3
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 2
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == 13
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_three_kind_9(self):
        result = get_three_kind(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result != {}
        assert result['name'] == "Three of a Kind"
        assert result['hand_rank'] == 3
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 2
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == 6
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_three_kind_10(self):
        result = get_three_kind(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result != {}
        assert result['name'] == "Three of a Kind"
        assert result['hand_rank'] == 3
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 2
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == 10
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_three_kind_11(self):
        result = get_three_kind(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == {}

    def test_three_kind_12(self):
        result = get_three_kind(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result == {}

    def test_three_kind_13(self):
        result = get_three_kind(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result == {}

    def test_three_kind_14(self):
        result = get_three_kind(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result == {}

    def test_three_kind_15(self):
        result = get_three_kind(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result == {}

    def test_three_kind_16(self):
        result = get_three_kind(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result == {}

    def test_three_kind_17(self):
        result = get_three_kind(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result == {}

    def test_three_kind_18(self):
        result = get_three_kind(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result == {}

    def test_three_kind_19(self):
        result = get_three_kind(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result == {}

class TestRankerFourKind:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_four_kind(self):
        result = get_four_kind(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == {}

    def test_four_kind_2(self):
        result = get_four_kind(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result == {}

    def test_four_kind_3(self):
        result = get_four_kind(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result == {}

    def test_four_kind_4(self):
        result = get_four_kind(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result == {}

    def test_four_kind_5(self):
        result = get_four_kind(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result == {}

    def test_four_kind_6(self):
        result = get_four_kind(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result == {}

    def test_four_kind_7(self):
        result = get_four_kind(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Four of a Kind"
        assert result['hand_rank'] == 7
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 1
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == 13
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_four_kind_8(self):
        result = get_four_kind(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result == {}

    def test_four_kind_9(self):
        result = get_four_kind(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result == {}

    def test_four_kind_10(self):
        result = get_four_kind(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result == {}

    def test_four_kind_11(self):
        result = get_four_kind(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == {}

    def test_four_kind_12(self):
        result = get_four_kind(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result == {}

    def test_four_kind_13(self):
        result = get_four_kind(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result == {}

    def test_four_kind_14(self):
        result = get_four_kind(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result == {}

    def test_four_kind_15(self):
        result = get_four_kind(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result == {}

    def test_four_kind_16(self):
        result = get_four_kind(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result == {}

    def test_four_kind_17(self):
        result = get_four_kind(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result == {}

    def test_four_kind_18(self):
        result = get_four_kind(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result == {}

    def test_four_kind_19(self):
        result = get_four_kind(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result == {}


class TestRankerStraight:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_straight(self):
        result = get_straight(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == {}

    def test_straight_2(self):
        result = get_straight(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result == {}

    def test_straight_3(self):
        result = get_straight(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result == {}

    def test_straight_4(self):
        result = get_straight(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result == {}

    def test_straight_5(self):
        result = get_straight(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result == {}

    def test_straight_6(self):
        result = get_straight(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result == {}

    def test_straight_7(self):
        result = get_straight(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result == {}

    def test_straight_8(self):
        result = get_straight(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result == {}

    def test_straight_9(self):
        result = get_straight(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result == {}

    def test_straight_10(self):
        result = get_straight(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result == {}

    def test_straight_11(self):
        result = get_straight(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == {}

    def test_straight_12(self):
        result = get_straight(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight"
        assert result['hand_rank'] == 4
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 14
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_13(self):
        result = get_straight(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight"
        assert result['hand_rank'] == 4
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 5
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_14(self):
        result = get_straight(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result == {}

    def test_straight_15(self):
        result = get_straight(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight"
        assert result['hand_rank'] == 4
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 12
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_16(self):
        result = get_straight(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight"
        assert result['hand_rank'] == 4
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 12
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_17(self):
        result = get_straight(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight"
        assert result['hand_rank'] == 4
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 5
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_18(self):
        result = get_straight(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight"
        assert result['hand_rank'] == 4
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 7
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_19(self):
        result = get_straight(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight"
        assert result['hand_rank'] == 4
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 5
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []


class TestRankerFlush:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_flush(self):
        result = get_flush(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == {}

    def test_flush_2(self):
        result = get_flush(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result == {}

    def test_flush_3(self):
        result = get_flush(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result == {}

    def test_flush_4(self):
        result = get_flush(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Flush"
        assert result['hand_rank'] == 5
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_flush_5(self):
        result = get_flush(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result == {}

    def test_flush_6(self):
        result = get_flush(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result == {}

    def test_flush_7(self):
        result = get_flush(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result == {}

    def test_flush_8(self):
        result = get_flush(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result == {}

    def test_flush_9(self):
        result = get_flush(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result == {}

    def test_flush_10(self):
        result = get_flush(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result == {}

    def test_flush_11(self):
        result = get_flush(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == {}

    def test_flush_12(self):
        result = get_flush(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result == {}

    def test_flush_13(self):
        result = get_flush(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result == {}

    def test_flush_14(self):
        result = get_flush(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Flush"
        assert result['hand_rank'] == 5
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_flush_15(self):
        result = get_flush(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Flush"
        assert result['hand_rank'] == 5
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_flush_16(self):
        result = get_flush(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result != {}
        assert result['name'] == "Flush"
        assert result['hand_rank'] == 5
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_flush_17(self):
        result = get_flush(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result != {}
        assert result['name'] == "Flush"
        assert result['hand_rank'] == 5
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_flush_18(self):
        result = get_flush(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result != {}
        assert result['name'] == "Flush"
        assert result['hand_rank'] == 5
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

    def test_flush_19(self):
        result = get_flush(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result != {}
        assert result['name'] == "Flush"
        assert result['hand_rank'] == 5
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 5
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

class TestRankerFullHouse:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_full_house(self):
        result = get_full_house(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == {}

    def test_full_house_2(self):
        result = get_full_house(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result == {}

    def test_full_house_3(self):
        result = get_full_house(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result == {}

    def test_full_house_4(self):
        result = get_full_house(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result == {}

    def test_full_house_5(self):
        result = get_full_house(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result == {}

    def test_full_house_6(self):
        result = get_full_house(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result != {}
        assert result['name'] == "Full House"
        assert result['hand_rank'] == 6
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == 11
        assert result["two_kind_value"] == 10
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_full_house_7(self):
        result = get_full_house(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result == {}

    def test_full_house_8(self):
        result = get_full_house(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Full House"
        assert result['hand_rank'] == 6
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == 13
        assert result["two_kind_value"] == 6
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_full_house_9(self):
        result = get_full_house(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result != {}
        assert result['name'] == "Full House"
        assert result['hand_rank'] == 6
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == 6
        assert result["two_kind_value"] == 13
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_full_house_10(self):
        result = get_full_house(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result != {}
        assert result['name'] == "Full House"
        assert result['hand_rank'] == 6
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == None 
        assert result["three_kind_value"] == 10
        assert result["two_kind_value"] == 11
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_full_house_11(self):
        result = get_full_house(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == {}

    def test_full_house_12(self):
        result = get_full_house(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result == {}

    def test_full_house_13(self):
        result = get_full_house(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result == {}

    def test_full_house_14(self):
        result = get_full_house(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result == {}

    def test_full_house_15(self):
        result = get_full_house(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result == {}

    def test_full_house_16(self):
        result = get_full_house(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result == {}

    def test_full_house_17(self):
        result = get_full_house(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result == {}

    def test_full_house_18(self):
        result = get_full_house(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result == {}

    def test_full_house_19(self):
        result = get_full_house(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result == {}

class TestRankerStraightFlush:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_straight_flush(self):
        result = get_straight_flush(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == {}

    def test_straight_flush_2(self):
        result = get_straight_flush(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result == {}

    def test_straight_flush_3(self):
        result = get_straight_flush(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result == {}

    def test_straight_flush_4(self):
        result = get_straight_flush(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result == {}

    def test_straight_flush_5(self):
        result = get_straight_flush(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result == {}

    def test_straight_flush_6(self):
        result = get_straight_flush(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result == {}

    def test_straight_flush_7(self):
        result = get_straight_flush(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result == {}

    def test_straight_flush_8(self):
        result = get_straight_flush(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result == {}

    def test_straight_flush_9(self):
        result = get_straight_flush(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result == {}

    def test_straight_flush_10(self):
        result = get_straight_flush(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result == {}

    def test_straight_flush_11(self):
        result = get_straight_flush(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == {}

    def test_straight_flush_12(self):
        result = get_straight_flush(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result == {}

    def test_straight_flush_13(self):
        result = get_straight_flush(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result == {}

    def test_straight_flush_14(self):
        result = get_straight_flush(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result == {}

    def test_straight_flush_15(self):
        result = get_straight_flush(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight Flush"
        assert result['hand_rank'] == 8
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 12
        assert result["three_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_flush_16(self):
        result = get_straight_flush(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight Flush"
        assert result['hand_rank'] == 8
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 12
        assert result["three_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_flush_17(self):
        result = get_straight_flush(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight Flush"
        assert result['hand_rank'] == 8
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 5 
        assert result["three_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_flush_18(self):
        result = get_straight_flush(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight Flush"
        assert result['hand_rank'] == 8
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 7
        assert result["three_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

    def test_straight_flush_19(self):
        result = get_straight_flush(self.hand_is_straight_flush_5)
        print self.hand_is_straight_flush_5
        pretty(result)
        assert result != {}
        assert result['name'] == "Straight Flush"
        assert result['hand_rank'] == 8
        assert result["suit"] == "Diamonds"
        assert result["all_cards"] != []
        assert len(result['all_cards']) == 5
        assert len(result['ordered_kickers']) == 0
        assert result["s_or_sf_high_card"] == 5 
        assert result["three_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

class TestRankerBestHand:
    def setUp(self):
        self.no_hand_1 = [d2,d6,da,h11,c10,h13,d3]

        self.hand_is_pair_1 = [d2,d8,c10,d11,c11,h10,da]
        self.hand_is_pair_2 = [d2,sa,d3,d6,c11,h13,d11]

        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]

        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_double_trips = [d2,h11,c10,d11,c11,h10,s10]


        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        
        self.hand_is_full_house_1 = [d2,c6,h13,s13,d13,d6,d5]
        self.hand_is_full_house_2 = [d2,c6,h13,s13,h6,d6,d5]
        self.hand_is_full_house_3 = [d2,d8,c10,d11,c11,h10,s10]

        self.hand_is_almost_straight = [d2, d3, d4, h12, c11, h10, da]

        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_low_straight = [d2,da,h3,d4,c5,h10,d7]

        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

        self.hand_is_straight_flush_1 = [d2, d8, d9, d10, d11, d12, s10]
        self.hand_is_straight_flush_2 = [d2,d8,d9,d10,d11,d12,da]
        self.hand_is_straight_flush_3 = [d2,d3,d4,d5,c11,h12,da]
        self.hand_is_straight_flush_4 = [d2,d3,d4,d5,d6,d7,da]
        self.hand_is_straight_flush_5 = [d2,d3,d4,d5,d8,d9,da]

    def test_best_hand(self):
        result = get_best_hand(self.no_hand_1)
        r2 = get_no_hand(self.no_hand_1)
        print self.no_hand_1
        pretty(result)
        assert result == r2

    def test_best_hand_2(self):
        result = get_best_hand(self.hand_is_pair_1)
        r2 = get_two_two_kind(self.hand_is_pair_1)
        print self.hand_is_pair_1
        pretty(result)
        assert result == r2

    def test_best_hand_3(self):
        result = get_best_hand(self.hand_is_pair_2)
        r2 = get_two_kind(self.hand_is_pair_2)
        print self.hand_is_pair_2
        pretty(result)
        assert result == r2

    def test_best_hand_4(self):
        result = get_best_hand(self.hand_is_two_two_kind_1)
        r2 = get_flush(self.hand_is_two_two_kind_1)
        print self.hand_is_two_two_kind_1
        pretty(result)
        assert result == r2

    def test_best_hand_5(self):
        result = get_best_hand(self.hand_is_three_kind_1)
        r2 = get_three_kind(self.hand_is_three_kind_1)
        print self.hand_is_three_kind_1
        pretty(result)
        assert result == r2

    def test_best_hand_6(self):
        result = get_best_hand(self.hand_is_double_trips)
        r2 = get_full_house(self.hand_is_double_trips)
        print self.hand_is_double_trips
        pretty(result)
        assert result == r2

    def test_best_hand_7(self):
        result = get_best_hand(self.hand_is_four_kind_1)
        r2 = get_four_kind(self.hand_is_four_kind_1)
        print self.hand_is_four_kind_1
        pretty(result)
        assert result == r2

    def test_best_hand_8(self):
        result = get_best_hand(self.hand_is_full_house_1)
        r2 = get_full_house(self.hand_is_full_house_1)
        print self.hand_is_full_house_1
        pretty(result)
        assert result == r2

    def test_best_hand_9(self):
        result = get_best_hand(self.hand_is_full_house_2)
        r2 = get_full_house(self.hand_is_full_house_2)
        print self.hand_is_full_house_2
        pretty(result)
        assert result == r2

    def test_best_hand_10(self):
        result = get_best_hand(self.hand_is_full_house_3)
        r2 = get_full_house(self.hand_is_full_house_3)
        print self.hand_is_full_house_3
        pretty(result)
        assert result == r2

    def test_best_hand_11(self):
        result = get_best_hand(self.hand_is_almost_straight)
        r2 = get_no_hand(self.hand_is_almost_straight)
        print self.hand_is_almost_straight
        pretty(result)
        assert result == r2

    def test_best_hand_12(self):
        result = get_best_hand(self.hand_is_high_straight_1)
        r2 = get_straight(self.hand_is_high_straight_1)
        print self.hand_is_high_straight_1
        pretty(result)
        assert result == r2

    def test_best_hand_13(self):
        result = get_best_hand(self.hand_is_low_straight)
        r2 = get_straight(self.hand_is_low_straight)
        print self.hand_is_low_straight
        pretty(result)
        assert result == r2

    def test_best_hand_14(self):
        result = get_best_hand(self.hand_is_flush_1)
        r2 = get_flush(self.hand_is_flush_1)
        print self.hand_is_flush_1
        pretty(result)
        assert result == r2

    def test_best_hand_15(self):
        result = get_best_hand(self.hand_is_straight_flush_1)
        r2 = get_straight_flush(self.hand_is_straight_flush_1)
        print self.hand_is_straight_flush_1
        pretty(result)
        assert result == r2


    def test_best_hand_16(self):
        result = get_best_hand(self.hand_is_straight_flush_2)
        r2 = get_straight_flush(self.hand_is_straight_flush_2)
        print self.hand_is_straight_flush_2
        pretty(result)
        assert result == r2

    def test_best_hand_17(self):
        result = get_best_hand(self.hand_is_straight_flush_3)
        r2 = get_straight_flush(self.hand_is_straight_flush_3)
        print self.hand_is_straight_flush_3
        pretty(result)
        assert result == r2

    def test_best_hand_18(self):
        result = get_best_hand(self.hand_is_straight_flush_4)
        r2 = get_straight_flush(self.hand_is_straight_flush_4)
        print self.hand_is_straight_flush_4
        pretty(result)
        assert result == r2

    def test_best_hand_19(self):
        result = get_best_hand(self.hand_is_straight_flush_5)
        r2 = get_straight_flush(self.hand_is_straight_flush_5)
        pretty(result)
        assert result == r2

class TestRankHandsAlgorithm:
    def setUp(self):
        rand = list(set([d2,da,sa,s13,d13,c13,h13,d12,d10,d11,d6,d3,c12,c10,s10,c11,c6,c3,h12,h10,h11,h6,h3,d4,c5,d7,d8,d9,d5]))
        shuffle(rand)
        self.hands = {}
        board = [rand.pop() for x in range(0,5)]
        for x in range(1, 4):
            temp = [rand.pop() for z in range(0,2)]
            self.hands[x] = temp + board

    def test_ranking_algo(self):
        print self.hands
        rank_hands(self.hands)
        assert False

class TestRankHandsAlgorithmParts:
    def setUp(self):
        board = [c12,c10,c11,c6,c3]
        self.same_flush = {2: [s10, d3] + board, 5: [sa, da] + board}

    # def test_compare_hands_of_0(self):
    #     pass
    # def test_compare_hands_of_1(self):
    #     pass
    # def test_compare_hands_of_2(self):
    #     pass
    # def test_compare_hands_of_3(self):
    #     pass
    # def test_compare_hands_of_4(self):
    #     pass
    def test_compare_hands_of_5(self):
        rank_hands(self.same_flush)
        assert False
        
    # def test_compare_hands_of_6(self):
    #     pass
    # def test_compare_hands_of_7(self):
    #     pass
    # def test_compare_hands_of_8(self):
    #     pass







