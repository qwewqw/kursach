import numpy as np
import matplotlib.pyplot as plt

def newton_interpolation(x, y):
    n = len(x)
    F = np.zeros((n, n))
    F[:,0] = y
    
    for j in range(1, n):
        for i in range(n-j):
            F[i,j] = (F[i+1,j-1] - F[i,j-1]) / (x[i+j] - x[i])
    
    return F[0,:]

def evaluate_newton_interpolant(x, coeffs, interpolation_points):
    n = len(coeffs)
    p = coeffs[-1]
    for k in range(2, n + 1):
        p = np.multiply(p, (interpolation_points - x[n - k])) + coeffs[n - k]
    return p

def plot_interpolation(x, y, interpolation_points, interpolated_values):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Таблично-заданная функция')
    plt.plot(interpolation_points, interpolated_values, label='Интерполяционная функция')
    plt.title('Интерполяция методом Ньютона')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Ввод точек таблично-заданной функции
    n = int(input("Введите количество точек: "))
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(n):
        x[i] = float(input(f"Введите x{i+1}: "))
        y[i] = float(input(f"Введите y{i+1}: "))
    
    # Интерполяция
    coeffs = newton_interpolation(x, y)
    
    # Вывод коэффициентов
    print("Коэффициенты интерполяционного многочлена:", coeffs)
    
    # Ввод точек для интерполяции
    m = int(input("Введите количество точек для интерполяции: "))
    interpolation_points = np.zeros(m)
    for i in range(m):
        interpolation_points[i] = float(input(f"Введите x для интерполяции {i+1}: "))
    
    # Вычисление значений интерполяционной функции в заданных точках
    interpolated_values = evaluate_newton_interpolant(x, coeffs, interpolation_points)
    
    # Построение графиков
    plot_interpolation(x, y, interpolation_points, interpolated_values)

if __name__ == "__main__":
    main()
