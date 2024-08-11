import umap
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from .utils import extract_features
import logging

logger = logging.getLogger(__name__)


def generate_umap_kmeans_plot(fname, data, n_neighbors=15, min_dist=0.1, n_components=2, n_clusters=3,
                              output_file='output.png', plot_size=(8, 6)):
    try:
        logger.info("Starting UMAP dimensionality reduction")
        features = extract_features(data)
        reducer = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist, n_components=n_components)
        embedding = reducer.fit_transform(features)
        logger.info("UMAP dimensionality reduction completed")

        logger.info(f"Starting KMeans clustering with {n_clusters} clusters")
        kmeans = KMeans(n_clusters=n_clusters)
        labels = kmeans.fit_predict(embedding)
        logger.info("KMeans clustering completed")

        logger.info(f"Generating plot with size {plot_size}")
        plt.figure(figsize=plot_size)
        plt.scatter(embedding[:, 0], embedding[:, 1], c=labels, cmap='Spectral', s=50)
        plt.title(f'UMAP-KMeans {fname} n={len(data)}, k={n_clusters}')
        plt.savefig(output_file)
        logger.info(f"Plot saved to {output_file}")
        plt.close()
    except Exception as e:
        logger.error(f"Failed to generate plot: {e}")
        raise
