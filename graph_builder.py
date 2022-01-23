import matplotlib.pyplot as plt

work_intensity = []
x = []


def get_stats(hours):
    for hour in hours:
        intensity = sum([hour[app][2] for app in hour])
        work_intensity.append(intensity)
    x = range(1,len(work_intensity))


def show_graph():
    fig, ax = plt.subplots()
    ax.bar(x, work_intensity)

    ax.set_xlabel('Рабочие часы')
    ax.set_ylabel('Интенсивность работы')

    ax.set_facecolor('white')
    fig.set_facecolor('floralwhite')
    fig.set_figwidth(12)
    fig.set_figheight(6)

    plt.show()