import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cluster import Model

plt.switch_backend('agg')

def Plot2D() -> None:
    points = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(1000)]
    
    model = Model(3, points)
    clusters = model.evaluate()
    colors = ['blue', 'red', 'green']
    
    fig = plt.figure()

    for i, array in enumerate(clusters):
        x, y = zip(*array)
        plt.scatter(x, y, color=colors[i], label=f'Cluster {i+1}')
    
    plt.legend()
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig('2d_plot.png', dpi=500)

def Plot3D() -> None:
    points = [(random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)) for _ in range(100)]

    model = Model(3, points)
    clusters = model.evaluate()
    colors = ['blue', 'red', 'green']
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    for i, array in enumerate(clusters):
        x, y, z = zip(*array)
        ax.scatter(x, y, z, color=colors[i], label=f'Cluster {i+1}')
    
    plt.legend()
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.savefig('3d_plot.png', dpi=500)

if __name__ == "__main__":
    Plot2D()
    Plot3D()