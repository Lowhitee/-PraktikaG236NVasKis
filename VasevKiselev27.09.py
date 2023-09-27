from scipy.optimize import linprog

c = [-1, -2]
A_ub = [[1, -2], [-1, 2], [1, 2]]
b_ub = [4, 4, 6]
x1_bounds = (0, None)
x2_bounds = (0, None)
bounds = [x1_bounds, x2_bounds]

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)

print("Значение переменных x1 и x2, при которых достигается максимальное значение функции Z(x):")
print(result.x)
print("Максимальное значение функции Z(x):")
print(-result.fun)