import argparse
from .plotter import generate_umap_kmeans_plot
from .utils import load_jsonl_file, default_config
import logging

logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO)

    config = default_config()

    parser = argparse.ArgumentParser(description="Generate a 2-D UMAP plot with KMeans clustering.")
    parser.add_argument('jsonl_file', type=str, help='Path to the JSONL file containing the data.')
    parser.add_argument('--n_neighbors', type=int, default=config['n_neighbors'], help='Number of neighbors for UMAP.')
    parser.add_argument('--min_dist', type=float, default=config['min_dist'], help='Minimum distance for UMAP.')
    parser.add_argument('--n_clusters', type=int, default=config['n_clusters'], help='Number of clusters for KMeans.')
    parser.add_argument('--output_file', type=str, default=config['output_file'], help='Output filename for the plot.')
    parser.add_argument('--plot_size', type=str, default=config['plot_size'],
                        help='Matplotlib fig size of the plot width,height. e.g. 6,8')

    args = parser.parse_args()
    plot_size = tuple(map(int, args.plot_size.split(',')))

    try:
        logger.info("Loading data and generating plot")
        data = load_jsonl_file(args.jsonl_file)
        n_neighbors = min(len(data) - 1, args.n_neighbors)
        n_clusters = min(len(data), args.n_clusters)
    except Exception as e:
        logger.error(f"Failed loading file: {e}")
        raise
    try:
        generate_umap_kmeans_plot(args.jsonl_file, data, n_neighbors, args.min_dist, 2, n_clusters,
                                  args.output_file, plot_size)
        logger.info("Process completed successfully")
    except Exception as e:
        logger.error(f"Failed generating plot: {e}")
        raise



if __name__ == "__main__":
    main()
