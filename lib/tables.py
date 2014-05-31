class PokerHandTable(object):
    """docstring for Table"""
    def __init__(self):
        super(Table, self).__init__()
        self.positions = dict([(x,None) for x in range(1,13)])

    def sit_player(self):
        pass






    # def _blind_assignment(self, buttonposition=0):
    #     # this could be a lot easier if we kept track of occupied positions
    #     if not buttonposition:
    #         buttonposition = choice(self.players.values())
    #     self.buttonposition = buttonposition
    #     temp = buttonposition
    #     # this can be optimized a ton, interate through keys of active players
    #     if len(self.players) == 2:
    #         while True:
    #             if temp >= 12:
    #                 temp = 0
    #             temp = temp + 1
    #             if self.positions[temp]:
    #                 self.smallposition = temp
    #                 self.bigposition = buttonposition
    #                 break
    #     else:
    #         temp = buttonposition
    #         while temp < 12:
    #             if temp >= 12:
    #                 temp = 0
    #             temp = temp + 1
    #             if self.positions[temp]:
    #                 self.smallposition = temp
    #                 break
    #         temp = self.smallposition
    #         while temp < 12:
    #             if temp >= 12:
    #                 temp = 0
    #             temp = temp + 1
    #             if self.positions[temp]:
    #                 self.bigposition = temp
    #                 break
    #     