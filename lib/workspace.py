
    def is_straight(self):
        local_cards = copy(self.cards)

        successives = 1
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))

        values = sorted([card.as_tuple() for card in local_cards])
        for x in enumerate(values):
            location = x[0]
            num, suit = x[1]
            if location+1 >= len(values):
                break
            n2, s2 = values[location+1]
            if num+1 == n2:
                successives += 1
        if successives == 5:
            return True
        else:
            return False

    def straight_details(self):
        local_cards = copy(self.cards)
        mx = 0
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))

        values = sorted([card.as_tuple() for card in local_cards])
        for x in enumerate(values):
            location = x[0]
            num, suit = x[1]
            if location+1 >= len(values):
                break
            n2, s2 = values[location+1]
            if num+1 == n2:
                mx = n2
        print mx
        print suit
        return self.get_card(mx, suit)

    def is_straight_flush(self):
        local_cards = copy(self.cards)
        print local_cards
        mx = 0
        successives = 1
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))
        grouped_by_suit = {}
        for x in local_cards:
            num, suit = x.as_tuple()
            if suit not in grouped_by_suit:
                grouped_by_suit[suit] = [num]
            else:
                grouped_by_suit[suit].append(num)

        suited = None
        suit = None
        for k,v in grouped_by_suit.items():
            if len(v) >= 5:
                suit = k
                suited = sorted(grouped_by_suit[k])

        for location, num in enumerate(suited):
            if location+1 >= len(suited):
                break
            n2 = suited[location+1]
            if num+1 == n2:
                successives += 1
                mx = n2        
        if successives >= 5:
            return True
        return False

    def straight_flush_details(self):
        local_cards = copy(self.cards)
        print local_cards
        mx = 0
        for x in local_cards:
            if x.is_ace:
                local_cards.append(Card(1,x.suit))
        grouped_by_suit = {}
        for x in local_cards:
            num, suit = x.as_tuple()
            if suit not in grouped_by_suit:
                grouped_by_suit[suit] = [num]
            else:
                grouped_by_suit[suit].append(num)

        suited = None
        suit = None
        for k,v in grouped_by_suit.items():
            if len(v) >= 5:
                suit = k
                suited = sorted(grouped_by_suit[k])

        for location, num in enumerate(suited):
            if location+1 >= len(suited):
                break
            n2 = suited[location+1]
            if num+1 == n2:
                mx = n2
        return self.get_card(mx,suit)
            