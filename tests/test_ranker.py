from lib.baseclasses.generics import Card
from lib.ranker import *
import json

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



class TestRanker:
    def setUp(self):
        self.hand_is_two_two_kind_1 = [d2,da,sa,s13,d13,d6,d5]
        self.hand_is_three_kind_1 = [d2,c3,h13,s13,d13,d6,d5]
        self.hand_is_four_kind_1 = [d2,c3,h13,c13,d13,s13,d5]
        self.hand_is_high_straight_1 = [d2,d5,h12,h10,d11,d13,sa]
        self.hand_is_flush_1 = [d2,da,sa,d8,d13,d6,d5]

    def test_two_kind_1(self):
        assert len(self.hand_is_two_two_kind_1) == 7
        result = get_two_kind(self.hand_is_two_two_kind_1)
        pretty(result)
        assert result["name"] != None
        assert result["hand_rank"] != None
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] != None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []
        #real stuff
        assert result['name'] == "Pair"
        assert result['hand_rank'] == 1
        assert result["two_kind_value"] == 14
        assert da in result['all_cards']
        assert sa in result['all_cards']
        assert s13 in result['all_cards']
        assert d13 in result['all_cards']
        assert d6 in result['all_cards']
        assert s13 in result['ordered_kickers']
        assert d13 in result['ordered_kickers']
        assert d6 in result['ordered_kickers']

    def test_two_kind_2_id(self):
        result = get_two_kind(self.hand_is_two_two_kind_1)
        pretty(result)
        assert id(da) in [id(x) for x in result['all_cards']]
        assert id(sa) in [id(x) for x in result['all_cards']]
        assert id(s13) in [id(x) for x in result['all_cards']]
        assert id(d13) in [id(x) for x in result['all_cards']]
        assert id(d6) in [id(x) for x in result['all_cards']]
        assert id(s13) in [id(x) for x in result['ordered_kickers']]
        assert id(d13) in [id(x) for x in result['ordered_kickers']]
        assert id(d6) in [id(x) for x in result['ordered_kickers']]

    def test_three_kind_1(self):
        assert len(self.hand_is_two_two_kind_1) == 7
        result = get_three_kind(self.hand_is_two_two_kind_1)
        pretty(result)
        assert result == {}

    def test_three_kind_2(self):
        result = get_three_kind(self.hand_is_three_kind_1)
        pretty(result)
        assert result["name"] != None
        assert result["hand_rank"] != None
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] != None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

        assert result['name'] == "Three of a Kind"
        assert result['hand_rank'] == 3
        assert result["three_kind_value"] == 13

    def test_three_kind_3_id(self):
        result = get_three_kind(self.hand_is_three_kind_1)
        assert id(d6) in [id(x) for x in result['all_cards']]
        assert id(h13) in [id(x) for x in result['all_cards']]
        assert id(s13) in [id(x) for x in result['all_cards']]
        assert id(d13) in [id(x) for x in result['all_cards']]
        assert id(d5) in [id(x) for x in result['all_cards']]
        assert id(d5) in [id(x) for x in result['ordered_kickers']]
        assert id(d6) in [id(x) for x in result['ordered_kickers']]

    def test_two_two_kind_1(self):
        assert len(self.hand_is_two_two_kind_1) == 7
        result = get_two_two_kind(self.hand_is_two_two_kind_1)
        pretty(result)
        assert result["name"] != None
        assert result["hand_rank"] != None
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] != None
        assert result["two_kind_value_2"] != None
        assert result["ordered_kickers"] != []
        #real stuff
        assert result['name'] == "Two Pair"
        assert result['hand_rank'] == 2
        assert result["two_kind_value"] == 14
        assert result["two_kind_value_2"] == 13
        assert da in result['all_cards']
        assert sa in result['all_cards']
        assert s13 in result['all_cards']
        assert d13 in result['all_cards']
        assert d6 in result['all_cards']
        assert d6 in result['ordered_kickers']

    def test_two_two_kind_ids(self):
        result = get_two_two_kind(self.hand_is_two_two_kind_1)
        assert id(da) in [id(x) for x in result['all_cards']]
        assert id(sa) in [id(x) for x in result['all_cards']]
        assert id(s13) in [id(x) for x in result['all_cards']]
        assert id(d13) in [id(x) for x in result['all_cards']]
        assert id(d6) in [id(x) for x in result['all_cards']]
        assert id(d6) in [id(x) for x in result['ordered_kickers']]

    def test_four_kind_1(self):
        assert len(self.hand_is_two_two_kind_1) == 7
        result = get_four_kind(self.hand_is_two_two_kind_1)
        pretty(result)
        assert result == {}

    def test_four_kind_2(self):
        result = get_four_kind(self.hand_is_four_kind_1)
        pretty(result)
        assert result["name"] != None
        assert result["hand_rank"] != None
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] != None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

        assert result['name'] == "Four of a Kind"
        assert result['hand_rank'] == 6
        assert result["four_kind_value"] == 13
        assert c13 in result['all_cards']
        assert h13 in result['all_cards']
        assert s13 in result['all_cards']
        assert d13 in result['all_cards']
        assert d5 in result['all_cards']
        assert d5 in result['ordered_kickers']
        
    def test_four_kind_3_id(self):
        result = get_four_kind(self.hand_is_four_kind_1)

        assert id(c13) in [id(x) for x in result['all_cards']]
        assert id(h13) in [id(x) for x in result['all_cards']]
        assert id(s13) in [id(x) for x in result['all_cards']]
        assert id(d13) in [id(x) for x in result['all_cards']]
        assert id(d5) in [id(x) for x in result['all_cards']]
        assert id(d5) in [id(x) for x in result['ordered_kickers']]

    def test_straight_1(self):
        assert len(self.hand_is_two_two_kind_1) == 7
        result = get_straight(self.hand_is_two_two_kind_1)
        pretty(result)
        assert result == {}

    def test_straight_2(self):
        result = get_straight(self.hand_is_high_straight_1)
        pretty(result)
        assert result["name"] != None
        assert result["hand_rank"] != None
        assert result["suit"] == None
        assert result["all_cards"] != []
        assert result["s_or_sf_high_card"] != None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] == []

        assert result['name'] == "Straight"
        assert result['hand_rank'] == 4
        assert result["s_or_sf_high_card"] == sa
        assert h12 in result['all_cards']
        assert h10 in result['all_cards']
        assert d11 in result['all_cards']
        assert d13 in result['all_cards']
        assert sa in result['all_cards']

    def test_straight_2_id(self):
        result = get_straight(self.hand_is_high_straight_1)
        assert id(h12) in [id(x) for x in result['all_cards']]
        assert id(h10) in [id(x) for x in result['all_cards']]
        assert id(d11) in [id(x) for x in result['all_cards']]
        assert id(d13) in [id(x) for x in result['all_cards']]
        assert id(sa) in [id(x) for x in result['all_cards']]

    def test_flush_1(self):
        assert len(self.hand_is_two_two_kind_1) == 7
        result = get_flush(self.hand_is_high_straight_1)
        pretty(result)
        assert result == {}

    def test_flush_2(self):
        result = get_flush(self.hand_is_flush_1)
        pretty(result)
        assert result["name"] != None
        assert result["hand_rank"] != None
        assert result["suit"] != None
        assert result["all_cards"] != []
        assert result["s_or_sf_high_card"] == None
        assert result["three_kind_value"] == None
        assert result["four_kind_value"] == None
        assert result["two_kind_value"] == None
        assert result["two_kind_value_2"] == None
        assert result["ordered_kickers"] != []

        assert result['name'] == "Flush"
        assert result['hand_rank'] == 5

        assert da in result['all_cards']
        assert da in result['ordered_kickers']
        assert d8 in result['all_cards']
        assert d8 in result['ordered_kickers']
        assert d13 in result['all_cards']
        assert d13 in result['ordered_kickers']
        assert d6 in result['all_cards']
        assert d6 in result['ordered_kickers']
        assert d5 in result['all_cards']
        assert d5 in result['ordered_kickers']


    def test_flush_2_id(self):
        result = get_flush(self.hand_is_flush_1)
        assert id(da) in [id(x) for x in result['all_cards']]
        assert id(da) in [id(x) for x in result['ordered_kickers']]
        assert id(d8) in [id(x) for x in result['all_cards']]
        assert id(d8) in [id(x) for x in result['ordered_kickers']]
        assert id(d13) in [id(x) for x in result['all_cards']]
        assert id(d13) in [id(x) for x in result['ordered_kickers']]
        assert id(d6) in [id(x) for x in result['all_cards']]
        assert id(d6) in [id(x) for x in result['ordered_kickers']]
        assert id(d5) in [id(x) for x in result['all_cards']]
        assert id(d5) in [id(x) for x in result['ordered_kickers']]

