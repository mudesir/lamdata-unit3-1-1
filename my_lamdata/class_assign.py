# my_lamdata/class_assign
# This a class about complx number
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i
        
    def __repr__(self):
        return '({}, {})'.format(self.r, self.i)
