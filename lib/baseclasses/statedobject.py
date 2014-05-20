class StatedObject(object):
    """docstring for StatedObject"""
    def __init__(self):
        super(StatedObject, self).__init__()
        self.state = None

    def state_change(self,before,after):
        self.state = after
        