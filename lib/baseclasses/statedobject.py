from basecardgroup import BaseCardGroup

class StatedObject(object):
    """docstring for StatedObject"""
    def __init__(self):
        super(StatedObject, self).__init__()
        self.states = []
        self.current_state = None

    def state_change(self):
        after = self.states.pop()
        self.current_state = after


class StatedCardGroup(BaseCardGroup, StatedObject):
    """docstring for StatedCardGroup"""
    def __init__(self):
        super(StatedCardGroup, self).__init__([])
        self.states = [
            "river",
            "turn",
            "flop",
            "preflop",
            "pregame"
        ]
        self.current_state = None

    def state_change(self):
        after = self.states.pop()
        self.current_state = after
        