from yabox import PDE
PDE(lambda x: sum(x**2), [(-10, 10)]).solve()