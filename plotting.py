def time_centers(months, month_centers, months_range):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    x = months
    y = month_centers
    ax = fig.add_subplot(111)
    ax.set_xlabel("Number of Months")
    ax.set_ylabel("Number of Centers")
    title_obj = plt.title("Total Number of Open Centers")
    plt.setp(title_obj, color = '#401F51')
    ax.xaxis.label.set_color('#401F51')
    ax.yaxis.label.set_color('#401F51')
    ax.spines['left'].set_color('#00181A')
    ax.spines['right'].set_color('#00181A')
    ax.spines['top'].set_color('#00181A')
    ax.spines['bottom'].set_color('#00181A')
    ax.set_ylim((0, max(month_centers)))
    ax.set_xlim((0, max(months_range)))
    plt.plot(x, y,
             color='#E23761')
    plt.savefig('Training_centers.png')



def time_trainees(months, month_trainees):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = months
    y = month_trainees
    ax.set_xlabel("Number of Months")
    ax.set_ylabel("Number of Trainees")
    title_obj = plt.title("Total Number of Trainees Each months")
    plt.setp(title_obj, color='#401F51')
    ax.xaxis.label.set_color('#401F51')
    ax.yaxis.label.set_color('#401F51')
    ax.spines['left'].set_color('#00181A')
    ax.spines['right'].set_color('#00181A')
    ax.spines['top'].set_color('#00181A')
    ax.spines['bottom'].set_color('#00181A')
    ax.set_ylim((0, max(month_trainees)))
    ax.set_xlim((0, max(months)))
    plt.plot(x, y,
             color='#E23761')


def show():
    import matplotlib.pyplot as plt
    plt.show()

