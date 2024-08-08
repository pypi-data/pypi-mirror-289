import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from scipy import stats
from tqdm import tqdm

import os

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score, calinski_harabasz_score, davies_bouldin_score
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error

import umap
from scipy.spatial.distance import pdist, squareform
from scipy import stats

from kneed import KneeLocator

def sensitivity_analysis(linear_predict, compositions, energies, noise_levels=np.logspace(-4, -3, num=10000)
):
    """
    Perform sensitivity analysis by adding noise to the target values.

    Args:
        linear_predict (function): The function used for linear prediction.
        compositions (np.array): Input features.
        energies (np.array): Target values.
        noise_levels (list): Levels of noise to add.

    Returns:
        dict: Dictionary containing sensitivity coefficients and noise levels.
    """
    sensitivity_coeffs = []
    for noise in tqdm(noise_levels, desc="Processing noise levels"):
        noisy_energies = energies + np.max(energies)*np.random.normal(0, noise, size=energies.shape)
        coeffs, _, _ = linear_predict(compositions, noisy_energies, regularization=1e-2, verbose=False, zero_intercept=True, force_negative=False)
        sensitivity_coeffs.append(coeffs[1:])

    return {'coefficients': sensitivity_coeffs, 'noise_levels': noise_levels}

def cross_validation(linear_predict, compositions, energies, n_splits=5):
    """
    Perform cross-validation analysis.

    Args:
        linear_predict (function): The function used for linear prediction.
        compositions (np.array): Input features.
        energies (np.array): Target values.
        n_splits (int): Number of cross-validation splits.

    Returns:
        dict: Dictionary containing cross-validation coefficients and MSE.
    """
    kf = KFold(n_splits=n_splits)
    cv_coeffs = []
    cv_mse = []
    for train_index, test_index in tqdm(kf.split(compositions), desc="Processing cross_validation"):
        X_train, X_test = compositions[train_index], compositions[test_index]
        y_train, y_test = energies[train_index], energies[test_index]
        coeffs, _, _ = linear_predict(X_train, y_train, regularization=1e-2, verbose=False, zero_intercept=True, force_negative=False)
        cv_coeffs.append(coeffs)
        cv_mse.append(mean_squared_error(y_test, X_test @ coeffs[1:]))
    return {'coefficients': cv_coeffs, 'mse': cv_mse}

def bootstrap_analysis(linear_predict, compositions, energies, n_iterations=1000):
    """
    Perform bootstrap analysis.

    Args:
        linear_predict (function): The function used for linear prediction.
        compositions (np.array): Input features.
        energies (np.array): Target values.
        n_iterations (int): Number of bootstrap iterations.

    Returns:
        dict: Dictionary containing bootstrap coefficients and confidence intervals.
    """
    bootstrap_coeffs = []
    for _ in tqdm(range(n_iterations), desc="Processing bootstrap_analysis"):
        indices = np.random.choice(len(compositions), size=len(compositions), replace=True)
        X_boot, y_boot = compositions[indices], energies[indices]
        coeffs, _, _ = linear_predict(X_boot, y_boot, regularization=1e-2, verbose=False, zero_intercept=True, force_negative=False)
        bootstrap_coeffs.append(coeffs[1:])
    
    ci_lower = np.percentile(bootstrap_coeffs, 2.5, axis=0)
    ci_upper = np.percentile(bootstrap_coeffs, 97.5, axis=0)
    
    return {'coefficients': bootstrap_coeffs, 'ci_lower': ci_lower, 'ci_upper': ci_upper}

def regularization_analysis(linear_predict, compositions, energies, reg_range=np.logspace(-10, 1, 1000)):
    """
    Perform regularization analysis.

    Args:
        linear_predict (function): The function used for linear prediction.
        compositions (np.array): Input features.
        energies (np.array): Target values.
        reg_range (np.array): Range of regularization values to test.

    Returns:
        dict: Dictionary containing coefficients for each regularization value and the reg_range.
    """
    reg_coeffs = []
    for reg in tqdm(reg_range):
        coeffs, _, _ = linear_predict(compositions, energies, regularization=reg, verbose=False, zero_intercept=True, force_negative=False)
        reg_coeffs.append(coeffs[1:])
    return {'coefficients': reg_coeffs, 'reg_range': reg_range}

def multicollinearity_analysis(compositions):
    """
    Analyze multicollinearity among input features.

    Args:
        compositions (np.array): Input features.

    Returns:
        np.array: Correlation matrix of input features.
    """
    return np.corrcoef(compositions.T)

def residuals_analysis(linear_predict, compositions, energies):
    """
    Analyze residuals of the linear fit.

    Args:
        linear_predict (function): The function used for linear prediction.
        compositions (np.array): Input features.
        energies (np.array): Target values.

    Returns:
        dict: Dictionary containing residuals and normality test results.
    """
    _, predictions, residuals = linear_predict(compositions, energies, regularization=1e-2, verbose=False, zero_intercept=True, force_negative=False)
    _, p_value = stats.normaltest(residuals)
    return {'residuals': residuals, 'normality_p_value': p_value}

# ============ Plotting functions ============ ============ Plotting functions =========== ============ Plotting functions ===========

def plot_coefficients_distribution(coeff_list, title, output_file='coefficients_distribution.png'):
    """
    Plot the distribution of coefficients with an enhanced appearance.

    Args:
        coeff_list (list): List of coefficient arrays.
        title (str): Title of the plot.
    """
    directory = os.path.dirname(output_file)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    plt.figure(figsize=(12, 7))
    num_coeffs = len(coeff_list[0])
    colors = plt.cm.viridis(np.linspace(0, 1, num_coeffs))
    
    for i in range(num_coeffs):
        plt.hist([c[i] for c in coeff_list], bins=100, alpha=0.7, color=colors[i], 
                 label=f'Coefficient {i+1}', edgecolor='black', linewidth=0.5)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel('Coefficient Value', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save the figure to a file
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f" >> Plot saved as {output_file}")

def plot_regularization_path(reg_coeffs, reg_range, output_file='regularization_path.png'):
    """
    Plot the regularization path with an enhanced appearance.

    Args:
        reg_coeffs (list): List of coefficient arrays for different regularization values.
        reg_range (np.array): Range of regularization values.
    """
    directory = os.path.dirname(output_file)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    plt.figure(figsize=(12, 7))
    num_coeffs = len(reg_coeffs[0])
    colors = plt.cm.viridis(np.linspace(0, 1, num_coeffs))
    
    for i in range(num_coeffs):
        plt.semilogx(reg_range, [c[i] for c in reg_coeffs], label=f'Coefficient {i+1}',
                     linewidth=2, color=colors[i], marker='o', markersize=4)
    
    plt.title('Regularization Path', fontsize=16, fontweight='bold')
    plt.xlabel('Regularization Parameter', fontsize=12)
    plt.ylabel('Coefficient Value', fontsize=12)
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, which="both", linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save the figure to a file
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f" >> Plot saved as {output_file}")
    '''
    Interpretación:

    Estabilidad de coeficientes: Si los coeficientes cambian drásticamente con pequeños cambios en la regularización, esto podría indicar inestabilidad en el modelo o multicolinealidad entre las características.
    Shrinkage (reducción): A medida que aumenta la regularización, normalmente verás que los coeficientes se acercan a cero. Esto es el efecto de "shrinkage" de la regularización.
    Importancia de las características: Las características cuyos coeficientes se mantienen grandes incluso con alta regularización son probablemente más importantes para el modelo.
    Overfitting vs Underfitting:

    Con baja regularización (izquierda del gráfico), los coeficientes pueden ser grandes, lo que podría indicar overfitting.
    Con alta regularización (derecha del gráfico), los coeficientes tienden a cero, lo que podría llevar a underfitting.


    Punto de inflexión: Busca un punto donde los coeficientes comienzan a estabilizarse. Este podría ser un buen valor de regularización para tu modelo final.
    '''
def plot_correlation_matrix(correlation_matrix, output_file='correlation_matrix.png'):
    """
    Plot the correlation matrix of input features with an enhanced appearance.

    Args:
        correlation_matrix (np.array): Correlation matrix to plot.
    """
    directory = os.path.dirname(output_file)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    plt.figure(figsize=(10, 8))
    im = plt.imshow(correlation_matrix, cmap='coolwarm', aspect='auto', vmin=-1, vmax=1)
    plt.colorbar(im, label='Correlation Coefficient')
    
    plt.title('Correlation Matrix of Predictors', fontsize=16, fontweight='bold')
    plt.xticks(range(len(correlation_matrix)), [f'X{i+1}' for i in range(len(correlation_matrix))], rotation=45)
    plt.yticks(range(len(correlation_matrix)), [f'X{i+1}' for i in range(len(correlation_matrix))])
    
    for i in range(len(correlation_matrix)):
        for j in range(len(correlation_matrix)):
            plt.text(j, i, f'{correlation_matrix[i, j]:.2f}', 
                     ha='center', va='center', color='black', fontweight='bold')
    
    plt.tight_layout()

    # Save the figure to a file
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f" >> Plot saved as {output_file}")

def plot_residuals(residuals, output_file='residuals.png'):
    """
    Plot the residuals of the linear fit with an enhanced appearance.

    Args:
        residuals (np.array): Residuals to plot.
    """
    directory = os.path.dirname(output_file)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    plt.figure(figsize=(12, 7))
    plt.scatter(range(len(residuals)), residuals, alpha=0.7, color='#1f77b4', edgecolor='black', linewidth=0.5)
    
    plt.title('Residuals Plot', fontsize=16, fontweight='bold')
    plt.xlabel('Data Point', fontsize=12)
    plt.ylabel('Residual', fontsize=12)
    
    plt.axhline(y=0, color='r', linestyle='--', linewidth=2)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add mean and std annotations
    mean_residual = np.mean(residuals)
    std_residual = np.std(residuals)
    plt.annotate(f'Mean: {mean_residual:.4f}\nStd Dev: {std_residual:.4f}', 
                 xy=(0.05, 0.95), xycoords='axes fraction',
                 fontsize=10, ha='left', va='top',
                 bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                 )
    
    plt.tight_layout()

    # Save the figure to a file
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f" >> Plot saved as {output_file}")

# Example usage:
# sensitivity_results = sensitivity_analysis(linear_predict, compositions, energies)
# cv_results = cross_validation(linear_predict, compositions, energies)
# bootstrap_results = bootstrap_analysis(linear_predict, compositions, energies)
# regularization_results = regularization_analysis(linear_predict, compositions, energies)
# multicollinearity_results = multicollinearity_analysis(compositions)
# residuals_results = residuals_analysis(linear_predict, compositions, energies)

# Plot results:
# plot_coefficients_distribution(sensitivity_results['coefficients'], 'Sensitivity Analysis')
# plot_coefficients_distribution(cv_results['coefficients'], 'Cross-Validation Coefficients')
# plot_coefficients_distribution(bootstrap_results['coefficients'], 'Bootstrap Coefficients')
# plot_regularization_path(regularization_results['coefficients'], regularization_results['reg_range'])
# plot_correlation_matrix(multicollinearity_results)
# plot_residuals(residuals_results['residuals'])

# ============ ClusteringAnalysis ============ ============ ClusteringAnalysis =========== ============ ClusteringAnalysis ===========
class ClusteringAnalysis:
    def __init__(self):
        self.data = None
        self.data_scaled = None
        self.results = {}
        self.dim_reduction = {}
        self.clustering_methods = {
            'dbscan': lambda eps, min_samples: DBSCAN(eps=eps, min_samples=min_samples),
            'kmeans': lambda n_clusters: KMeans(n_clusters=n_clusters, random_state=42),
            'agglomerative': lambda n_clusters: AgglomerativeClustering(n_clusters=n_clusters),
            'gmm': lambda n_components: GaussianMixture(n_components=n_components, random_state=42)
        }

    def preprocess_data(self, data):
        scaler = StandardScaler()
        return scaler.fit_transform(data)

    def estimate_initial_params(self, data, k=5):
            neigh = NearestNeighbors(n_neighbors=k)
            nbrs = neigh.fit(data)
            distances, _ = nbrs.kneighbors(data)
            distances = np.sort(distances, axis=0)
            distances = distances[:, 1]
            kneedle = KneeLocator(range(len(distances)), distances, curve='convex', direction='increasing')
            eps = distances[kneedle.elbow]
            return eps, k

    def optimize_dbscan_params(self, data, k_range=(2, 10), eps_margin=0.5, min_samples_margin=5, n_jobs=-1):
        """
        Optimizes DBSCAN parameters using a combination of initial estimation and refined grid search.
        
        :param data: Scaled data
        :param k_range: Range of k values to consider for initial estimation
        :param eps_margin: Margin around the estimated eps for grid search
        :param min_samples_margin: Margin around the estimated min_samples for grid search
        :param n_jobs: Number of parallel jobs (-1 to use all cores)
        :return: Best parameters (eps, min_samples)
        """
        def estimate_initial_params(data, k):
            neigh = NearestNeighbors(n_neighbors=k)
            nbrs = neigh.fit(data)
            distances, _ = nbrs.kneighbors(data)
            distances = np.sort(distances, axis=0)
            distances = distances[:, 1]
            kneedle = KneeLocator(range(len(distances)), distances, curve='convex', direction='increasing')
            eps = distances[kneedle.elbow]
            return eps, k

        # Initial estimation
        best_score = -1
        best_initial_params = None
        for k in range(k_range[0], k_range[1] + 1):
            eps, min_samples = estimate_initial_params(data, k)
            dbscan = DBSCAN(eps=eps, min_samples=min_samples, n_jobs=n_jobs)
            labels = dbscan.fit_predict(data)
            if len(np.unique(labels)) > 1:
                score = silhouette_score(data, labels)
                if score > best_score:
                    best_score = score
                    best_initial_params = (eps, min_samples)

        if best_initial_params is None:
            print("Could not find a valid initial estimation.")
            return None

        # Refined grid search
        eps_init, min_samples_init = best_initial_params
        eps_range = (max(0.01, eps_init - eps_margin), eps_init + eps_margin)
        min_samples_range = (max(2, min_samples_init - min_samples_margin), min_samples_init + min_samples_margin)
        eps_values = np.linspace(eps_range[0], eps_range[1], 20)
        min_samples_values = range(min_samples_range[0], min_samples_range[1] + 1)

        best_score = -1
        best_params = None
        total_iterations = len(eps_values) * len(min_samples_values)
        with tqdm(total=total_iterations, desc="Optimizing DBSCAN") as pbar:
            for eps in eps_values:
                for min_samples in min_samples_values:
                    dbscan = DBSCAN(eps=eps, min_samples=min_samples, n_jobs=n_jobs)
                    labels = dbscan.fit_predict(data)
                    if len(np.unique(labels)) > 1:
                        score = silhouette_score(data, labels)
                        if score > best_score:
                            best_score = score
                            best_params = (eps, min_samples)
                    pbar.update(1)

        if best_params:
            print(f"Best DBSCAN parameters: eps={best_params[0]:.2f}, min_samples={best_params[1]}")
        else:
            print("Could not find optimal parameters.")

        return best_params

    def determine_optimal_clusters(self, data, max_clusters=10):
            max_clusters = min(max_clusters, data.shape[0] // 2)
            inertias = []
            for k in tqdm(range(2, max_clusters + 1), desc="Determining optimal clusters"):
                kmeans = KMeans(n_clusters=k, random_state=42)
                kmeans.fit(data)
                inertias.append(kmeans.inertia_)

            kneedle = KneeLocator(range(2, max_clusters + 1), inertias, curve='convex', direction='decreasing')
            return kneedle.elbow

    def vssovou_method(self, data, k_min=2, k_max=10, weight=0.5, seed=42):
        np.random.seed(seed)
        vssovou_scores = []

        for k in tqdm(range(k_min, k_max + 1), desc="Applying VSSOVOU method"):
            kmeans = KMeans(n_clusters=k, random_state=seed)
            labels = kmeans.fit_predict(data)
            centroids = kmeans.cluster_centers_

            ssb = np.sum([np.sum((data[labels == i] - np.mean(data, axis=0))**2) for i in range(k)])
            ssw = np.sum([np.sum((data[labels == i] - centroids[i])**2) for i in range(k)])

            vssovou = weight * (1 - 1/k) * ssb + (1 - weight) * (1 - 1/k) * ssw
            vssovou_scores.append(vssovou)

        optimal_k = np.argmin(vssovou_scores) + k_min
        return optimal_k

    def apply_clustering(self, data, methods):
        results = {}
        for name, method in tqdm(methods.items(), desc="Applying clustering methods"):
            labels = method.fit_predict(data)
            results[name] = labels

            if len(np.unique(labels)) > 1:
                silhouette = silhouette_score(data, labels)
                ch = calinski_harabasz_score(data, labels)
                db = davies_bouldin_score(data, labels)
                results[f"{name}_metrics"] = {
                    "silhouette": silhouette,
                    "calinski_harabasz": ch,
                    "davies_bouldin": db
                }

        return results

    def apply_dim_reduction(self, data):
        dim_reduction = {}
        for name, method in tqdm([("PCA", PCA(n_components=2)),
                                  ("t-SNE", TSNE(n_components=2, random_state=42)),
                                  ("UMAP", umap.UMAP(random_state=42))],
                                 desc="Applying dimensionality reduction"):
            dim_reduction[name] = method.fit_transform(data)
        return dim_reduction

    def verify_and_load_results(self, output_dir='./cluster_results', methods=None):
        """
        Verify if previous results exist and load them if they do.

        Args:
            output_dir (str): Directory where results are stored.
            methods (list): List of clustering methods to check.

        Returns:
            tuple: (bool, dict, dict) indicating if all results were loaded, 
                   and dictionaries of loaded clustering and dim reduction results.
        """
        if methods is None:
            methods = ['dbscan', 'kmeans', 'agglomerative', 'gmm', 'kmeans_vssovou']

        all_loaded = True
        loaded_results = {}
        loaded_dim_reduction = {}

        for method in tqdm(methods, desc="Verifying existing results"):
            filename = f'{output_dir}/{method}_labels.txt'

            if os.path.exists(filename):
                loaded_results[method] = np.loadtxt(filename, dtype=int)
            else:
                all_loaded = False
                break

        if all_loaded:
            for dim_method in ['PCA', 't-SNE', 'UMAP']:
                filename = f'{output_dir}/{dim_method}_reduction.npy'
                if os.path.exists(filename):
                    loaded_dim_reduction[dim_method] = np.load(filename)
                else:
                    all_loaded = False
                    break

        if all_loaded:
            print("All previous results loaded successfully.")
        else:
            print("Some results are missing. Will perform new analysis.")

        return all_loaded, loaded_results, loaded_dim_reduction

    def cluster_analysis(self, data, output_dir='./cluster_results', methods=None, max_clusters=10, use_cache=True):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if use_cache:
            all_loaded, loaded_results, loaded_dim_reduction = self.verify_and_load_results(output_dir, methods)
            if all_loaded:
                self.results = loaded_results
                self.dim_reduction = loaded_dim_reduction
                return self.results

        self.data = data
        self.data_scaled = self.preprocess_data(data)

        n_samples, n_features = self.data.shape
        print(f"Number of samples: {n_samples}")
        print(f"Number of features: {n_features}")

        # Set default methods if None
        methods = methods or ['dbscan', 'kmeans', 'agglomerative', 'gmm']

        # Initialize parameters
        params = {}

        # Determine necessary parameters
        if any(method in methods for method in ['kmeans', 'agglomerative', 'gmm']):
            params['optimal_k'] = self.determine_optimal_clusters(self.data_scaled, max_clusters)
            print(f"Optimal number of clusters (K-means): {params['optimal_k']}")

        if 'kmeans_vssovou' in methods:
            params['vssovou_k'] = self.vssovou_method(self.data_scaled, k_max=max_clusters)
            print(f"Optimal number of clusters (VSSOVOU): {params['vssovou_k']}")

        if 'dbscan' in methods:
            params['eps'], params['min_samples'] = self.optimize_dbscan_params(self.data_scaled)
            #params['eps'], params['min_samples'] = self.estimate_initial_params(self.data_scaled)

        # Create clustering methods dictionary
        clustering_methods = {
            'dbscan': lambda: self.clustering_methods['dbscan'](eps=params['eps'], min_samples=params['min_samples']),
            'kmeans': lambda: self.clustering_methods['kmeans'](n_clusters=params['optimal_k']),
            'agglomerative': lambda: self.clustering_methods['agglomerative'](n_clusters=params['optimal_k']),
            'gmm': lambda: self.clustering_methods['gmm'](n_components=params['optimal_k']),
            'kmeans_vssovou': lambda: self.clustering_methods['kmeans'](n_clusters=params['vssovou_k'])
        }

        # Select only the methods present in 'methods'
        selected_methods = {name: method() for name, method in clustering_methods.items() if name in methods}

        self.results = self.apply_clustering(self.data_scaled, selected_methods)
        self.dim_reduction = self.apply_dim_reduction(self.data_scaled)

        self.save_results(output_dir)
        self.plot_results(output_dir)

        return self.results
        
    def plot_results(self, output_dir='./cluster_results'):
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Plot clustering results
        for name, labels in self.results.items():
            if not name.endswith('_metrics'):
                plt.figure(figsize=(10, 8))
                scatter = plt.scatter(self.data_scaled[:, 0], self.data_scaled[:, 1], c=labels, cmap='viridis')
                plt.colorbar(scatter)
                plt.title(f'Clustering with {name}')
                plt.savefig(f'{output_dir}/{name}_clusters.png')
                plt.close()

        # Plot dimensionality reduction results
        for name, reduced_data in self.dim_reduction.items():
            plt.figure(figsize=(10, 8))
            for cluster_name, labels in self.results.items():
                if not cluster_name.endswith('_metrics'):
                    scatter = plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=labels, cmap='viridis', alpha=0.7)
            plt.colorbar(scatter)
            plt.title(f'Dimensionality Reduction with {name}\nColored by {cluster_name}')
            plt.savefig(f'{output_dir}/{name}_reduction.png')
            plt.close()

        # Plot distance matrix
        dist_matrix = squareform(pdist(self.data_scaled))
        plt.figure(figsize=(10, 8))
        im = plt.imshow(dist_matrix, cmap='viridis')
        plt.colorbar(im)
        plt.title('Distance Matrix')
        plt.savefig(f'{output_dir}/distance_matrix.png')
        plt.close()

    def save_results(self, output_dir='./cluster_results'):
        for name, labels in self.results.items():
            if not name.endswith('_metrics'):
                np.savetxt(f'{output_dir}/{name}_labels.txt', labels, fmt='%d')

        for name, reduced_data in self.dim_reduction.items():
            np.save(f'{output_dir}/{name}_reduction.npy', reduced_data)

        metrics = {name: metrics for name, metrics in self.results.items() if name.endswith('_metrics')}
        with open(f'{output_dir}/clustering_metrics.txt', 'w') as f:
            for method, metric_dict in metrics.items():
                f.write(f"{method}:\n")
                for metric_name, metric_value in metric_dict.items():
                    f.write(f"  {metric_name}: {metric_value}\n")
                f.write("\n")

        print(f"All results have been saved in {output_dir}")

# Usage example:
# analyzer = ClusteringAnalysis()
# results = analyzer.cluster_analysis(data, use_cache=True)

# ============ Compress Compress ============ ============ Compress Compress =========== ============ Compress Compress ===========
class Compress:
    def __init__(self, unique_labels, output_dir='./compression_output'):
        """
        Initialize the Compress class.

        Args:
            unique_labels (list): List of unique labels (e.g., species) in the data.
            output_dir (str): Directory to save the compressed data.
        """
        self.unique_labels = unique_labels
        self.output_dir = output_dir
        self.compression_methods = {
            'umap': self._umap_compression,
            'pca': self._pca_compression,
            'tsne': self._tsne_compression
        }

    def compress(self, data, method='umap', **kwargs):
        """
        Compress the data using the specified method.

        Args:
            data (dict): Dictionary containing data for each label.
            method (str): Compression method to use ('umap', 'pca', or 'tsne').
            **kwargs: Additional arguments for the compression method.

        Returns:
            dict: Dictionary containing compressed data for each label.
        """
        if method not in self.compression_methods:
            raise ValueError(f"Unsupported compression method: {method}")

        compressed_data = {}
        for label, label_data in data.items():
            compressed_data[label] = self.compression_methods[method](label_data, **kwargs)

        return compressed_data

    def _umap_compression(self, data, n_components=2, n_neighbors=15, min_dist=0.1, random_state=42):
        data = np.array(data)
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        reducer = umap.UMAP(n_components=n_components, n_neighbors=n_neighbors,
                            min_dist=min_dist, ) # random_state=random_state
        return reducer.fit_transform(data_scaled)

    def _pca_compression(self, data, n_components=2, random_state=42):
        data = np.array(data)
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        pca = PCA(n_components=n_components, random_state=random_state)
        return pca.fit_transform(data_scaled)

    def _tsne_compression(self, data, n_components=2, perplexity=30, random_state=42):
        data = np.array(data)
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(data)
        tsne = TSNE(n_components=n_components, perplexity=perplexity, random_state=random_state)
        return tsne.fit_transform(data_scaled)

    def save_compression(self, compression_dict, method):
        """
        Save the compression results for each label.

        Args:
            compression_dict (dict): Dictionary containing compressed data for each label.
            method (str): Compression method used.
        """
        method_dir = os.path.join(self.output_dir, method)
        if not os.path.exists(method_dir):
            os.makedirs(method_dir)

        for label, compressed_data in compression_dict.items():
            filename = os.path.join(method_dir, f"{method}_compressed_{label}.npy")
            np.save(filename, compressed_data)
            print(f"{method.upper()} compressed data for {label} saved to {filename}")

    def load_compression(self, method):
        """
        Load the compression results for each label if they exist.

        Args:
            method (str): Compression method to load.

        Returns:
            dict or None: Dictionary containing compressed data for each label if all files exist,
                          None if any file is missing.
        """
        method_dir = os.path.join(self.output_dir, method)
        compression_dict = {}

        for label in self.unique_labels:
            filename = os.path.join(method_dir, f"{method}_compressed_{label}.npy")
            if not os.path.exists(filename):
                print(f"Missing {method.upper()} compressed data for label {label}")
                return None

            compression_dict[label] = np.load(filename)

        print(f"All {method.upper()} compressed data files found and loaded successfully.")
        return compression_dict

    def verify_and_load_or_compress(self, data, method='umap', **kwargs):
        """
        Verify if compression results exist, load them if they do, or compress the data if they don't.

        Args:
            data (dict): Dictionary containing data for each label.
            method (str): Compression method to use ('umap', 'pca', or 'tsne').
            **kwargs: Additional arguments for the compression method.

        Returns:
            dict: Dictionary containing compressed data for each label.
        """
        compressed_data = self.load_compression(method)
        if compressed_data is not None:
            print(f"Loaded existing {method.upper()} compression data.")
            return compressed_data

        print(f"Some {method.upper()} compression files are missing. Recalculating...")
        compressed_data = self.compress(data, method, **kwargs)
        self.save_compression(compressed_data, method)
        return compressed_data
