from baseclasses.generics import Chips

class PlayerChips(Chips):
    """docstring for PlayerChips"""
    def __init__(self):
        super(PlayerChips, self).__init__()

class PotChips(Chips):
    """docstring for PotChips"""
    def __init__(self):
        super(PotChips, self).__init__()
        self.involvedplayers = []
        self.commitrequirement = 0

    def add(self, amount):
        super(PotChips, self).add(amount)
        self.commitrequirement = amount

    def as_dict(self):
        return {
            "stack":self.stack,
            "commit_requirement":self.commitrequirement
        }
