from timeit import default_timer as timer

import plotly.express as px

fib_counter = 0


def eratosthenes(n):
    zahlen = []
    for x in range(2, n + 1):
        zahlen.append(x)  # befülle Liste aufsteigend mit Zahlen
    for x in range(len(zahlen)):
        if zahlen[x] == 0:  # Zahl ist eindeutig keine Primzahl: -> überspringen
            continue  # continue überspringt den aktuellen Schleifendurchlauf
        # alle Einträge vor zahlen[x] sind entweder 0 oder prim -> nicht prüfen
        for z in range(x, len(zahlen)):
            if zahlen[z] != zahlen[x] and zahlen[z] % zahlen[x] == 0:  # zahl[z] ist vielfaches von zahl[x]?
                zahlen[z] = 0

    ergebnisliste = []
    for x in zahlen:
        if x != 0:
            ergebnisliste.append(x)
    print(ergebnisliste)


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_recursion_counter(n):
    global fib_counter
    fib_counter += 1
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_recursion_counter(n - 1) + fibonacci_recursion_counter(n - 2)


def rbm(m1, m2):
    produkt = 0
    while m1 > 0:
        if m1 % 2 != 0:
            produkt += m2
        m1 //= 2
        m2 *= 2
    return produkt


def scatter_plot(x_values, y_values, axis):
    """ produce a scatter plot

    Keyword arguments:
    x -- x-values of the data points to be plotted
    y - y-values of the data points to be plotted
    axis -- set type of axis
    """

    if axis == "semilog":
        fig = px.scatter(x=x_values, y=y_values, log_y=True)
    elif axis == "log":
        fig = px.scatter(x=x_values, y=y_values, log_y=True, log_x=True)
    else:
        fig = px.scatter(x=x_values, y=y_values)
    fig.show()


# n: höchster Eingabewert
def eratosthenes_time_and_plot(n):
    input = []
    times = []
    for x in range(0, n, 500):
        start = timer()
        eratosthenes(x)
        end = timer()
        times.append(end - start)
        input.append(x)
    scatter_plot(input, times, "log")


def fibonacci_time_and_plot(n):
    input = []
    times = []
    for x in range(0, n, 1):
        start = timer()
        fibonacci(x)
        end = timer()
        times.append(end - start)
        input.append(x)
    scatter_plot(input, times, "semilog")


def rbm_time_and_plot(m1, m2):
    input = []
    times = []
    produkt = 0
    while m1 > 0:
        if m1 % 2 != 0:
            produkt += m2
        m1 //= 2
        m2 *= 2
        times.append(timer())
        input.append(m2)
    scatter_plot(input, times, 'NICHTS')


"""
eratosthenes_time_and_plot(10000)
fibonacci_time_and_plot(10)
print(fibonacci_recursion_counter(10))
print(fib_counter)
rbm_time_and_plot(123, 4)
"""
