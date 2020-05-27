class cloth():
    def __init__(self, V, H):
        self.H = H
        self.V = V

    @property
    def total_size(self):
        total_size = (self.V / 6.5 + 0.5) + (2 * self.H + 0.3)
        return total_size


new_coth = cloth(15, 10)
print(new_coth.total_size)

