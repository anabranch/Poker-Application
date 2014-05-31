from baseclasses.generics import Chips

class PlayerChips(Chips):
    """docstring for PlayerChips"""
    def __init__(self):
        super(PlayerChips, self).__init__()

class PotChips(Chips):
    """docstring for PotChips"""
    def __init__(self):
        super(PotChips, self).__init__()
        self.player_commit_amounts = {}
        self.commitrequirement = 0

    def commit_players(self, players):
        for p in players:
            self.player_commit_amounts[p] = 0

    def add(self, player, amount):
        super(PotChips, self).add(amount)
        self.player_commit_amounts[player] += amount
        if amount > self.commitrequirement:
            self.commitrequirement = amount

    def as_dict(self):
        return {
            "stack":self.stack,
            "commit_amounts": dict([(p.pk, a) for p, a in self.player_commit_amounts.items()]),
            "commit_requirement":self.commitrequirement
        }
