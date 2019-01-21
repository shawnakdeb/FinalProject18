
class move:

    def __init__(self, name, m_type, power, accuracy, max_pp):
        self.name = name
        self.m_type = m_type
        self.power = power
        self.accuracy = accuracy
        self.max_pp = max_pp
        self.pp = max_pp

    def use_move(self):
        self.pp -= 1