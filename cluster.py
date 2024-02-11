import math
import random

type Point = tuple[float, ...]
type Cluster = list[Point]

calculate_distance = lambda p, q: math.sqrt(sum([(p[i] - q[i]) ** 2 for i in range(len(p))]))

def calculate_mass_center(points: Cluster, m=1) -> Point:
    return tuple(sum(m * [point[dimension] for point in points]) / len(points) for dimension in range(len(points[0])))

class Model:
    def __init__(self, n_clusters: int, dataset: Cluster, max_iterations=1000) -> None:
        self.centroids = []
        self.dataset = dataset
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations

    def initialize_centroids(self) -> Cluster:
        length = len(self.dataset)
        return [self.dataset[random.randint(0, length-1)] for _ in range(self.n_clusters)]
    
    def fit(self) -> list[Cluster]:
        clusters = [[self.centroids[i]] for i in range(self.n_clusters)]
        
        for data in self.dataset:
            distances = [calculate_distance(data, centroid) for centroid in self.centroids]
            centroid_index = distances.index(min(distances))
            clusters[centroid_index].append(data)

        return clusters
    
    def recompute_centroids(self, clusters: list[Cluster]) -> Cluster:
        cluster_centroids = []
        
        for cluster in clusters:
            mass_center = calculate_mass_center(cluster)
            cluster_centroids.append(mass_center)

        return cluster_centroids
    
    def evaluate(self) -> list[Cluster]:
        clusters = []
        self.centroids = self.initialize_centroids()

        for count in range(self.max_iterations):
            clusters = self.fit()
            new_centroids = self.recompute_centroids(clusters)
            if new_centroids == self.centroids:
                return clusters
            self.centroids = new_centroids

        return clusters
