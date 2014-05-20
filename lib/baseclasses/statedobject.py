class StatedObject(object):
    """docstring for StatedObject"""
    def __init__(self):
        super(StatedObject, self).__init__()
        self.states = []
        self.current_state = None

    def state_change(self):
        after = self.states.pop()
        self.current_state = after
        