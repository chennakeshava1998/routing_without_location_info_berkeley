import matplotlib.pyplot as plt
def display_points(VC):
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Virtual Coordinates')
    plt.plot(VC[:, 0], VC[:, 1])
    plt.show()
