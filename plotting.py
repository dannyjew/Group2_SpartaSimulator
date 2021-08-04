def time_centers(months, month_centers):
    import matplotlib.pyplot as plt
    x = months
    y = month_centers
    plt.plot(x, y)
    plt.xlabel("Number of Months")
    plt.ylabel("Number of Centers")
    plt.title("Total Number of Open Centers")
    plt.show()

def time_trainees(months, month_trainees):
    import matplotlib.pyplot as plt
    x = months
    y = month_trainees
    plt.plot(x, y)
    plt.xlabel("Number of Months")
    plt.ylabel("Number of Centers")
    plt.title("Total Number of Trainees Each month")
    plt.show()