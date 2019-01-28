
class move:

    def __init__(self, name, m_type, power, accuracy, max_pp):
        """Creates move object with given parameters"""
        self.name = name
        self.m_type = m_type
        self.power = power
        self.accuracy = accuracy
        self.max_pp = max_pp # unused
        self.pp = max_pp    # unused

    def use_move(self):
        """unused method that subtracts amount of moves left"""
        self.pp -= 1