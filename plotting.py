def time_centers(months, month_centers, months_range):
    import matplotlib.pyplot as plt
    plt.figure(1)
    x = months
    y = month_centers
    plt.ylim(0, max(month_centers))
    plt.xlim(0,max(months_range))
    plt.plot(x, y,
             color = '#E23761' )
    plt.xlabel("Number of Months")
    plt.ylabel("Number of Centers")
    plt.title("Total Number of Open Centers")
    plt.savefig('Training_centers.png')



def time_trainees(months, month_trainees):
    import matplotlib.pyplot as plt
    plt.figure(2)
    plt.ylim(0, max(month_trainees))
    plt.xlim(0, max(months))
    x = months
    y = month_trainees
    plt.plot(x, y,
             color = '#E23761' )
    plt.xlabel("Number of Months")
    plt.ylabel("Number of Trainees")
    plt.title("Total Number of Trainees Each month")
    plt.savefig('Trainees.png')


def show():
    import matplotlib.pyplot as plt
    plt.show()

