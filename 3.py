class  Cell():
    def __init__(self,val):
        self.val = val

    def __add__(self, other):
        long = self.val if len(self.val) >= len(other.val) else other.val
        new_cletka = [fst_val+scd_val for fst_val, scd_val in zip(self.val,other.val)] + \
                     long[min(len(self.val), len(other.val)):]
        return new_cletka

    def __sub__(self, other):
        long = self.val if len(self.val) >= len(other.val) else other.val
        new_cletka = [fst_val - scd_val for fst_val, scd_val in zip(self.val, other.val)] + \
                     long[min(len(self.val), len(other.val)):]
        return new_cletka

    def __mul__(self, other):
        long = self.val if len(self.val) >= len(other.val) else other.val
        new_cletka = [fst_val * scd_val for fst_val, scd_val in zip(self.val, other.val)] + \
                     long[min(len(self.val), len(other.val)):]
        return new_cletka

    def __truediv__(self, other):
        long = self.val if len(self.val) >= len(other.val) else other.val
        new_cletka = [fst_val / scd_val for fst_val, scd_val in zip(self.val, other.val)] + \
                     long[min(len(self.val), len(other.val)):]
        return new_cletka

    def make_order(self, order):
        return [self.val[i: i + order] for i in range(0 , len(self.val), order)]




h2o =[2,1,4,5,6,7,8,90]
h2so4 = [2,1,4]

cell_1 = Cell(h2o)
cell_2 = Cell(h2so4)
print(f'результат сложения  клеток {cell_1 + cell_2}')
print(f'результат вычитания клеток {cell_1 - cell_2}')
print(f'результат умножения клеток {cell_1 * cell_2}')
print(f'результат деления  клеток {cell_1 / cell_2}')
print(cell_1.make_order(5))



