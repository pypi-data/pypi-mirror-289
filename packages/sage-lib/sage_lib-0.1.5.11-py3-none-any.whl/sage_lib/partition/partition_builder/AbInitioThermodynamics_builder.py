try:
    from sage_lib.partition.PartitionManager import PartitionManager
    from sage_lib.miscellaneous.data_mining import *

except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing PartitionManager: {str(e)}\n")
    del sys

try:
    import numpy as np
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing numpy: {str(e)}\n")
    del sys

try:
    from sklearn.manifold import TSNE
    from scipy.spatial import cKDTree
    from sklearn.decomposition import PCA
    from scipy.optimize import curve_fit
    from sklearn.cluster import KMeans


    from scipy.stats import linregress
    from scipy.optimize import nnls
    from scipy.stats import gaussian_kde
    from scipy import stats

    from sklearn.model_selection import KFold
    from sklearn.metrics import mean_squared_error
    from sklearn.preprocessing import StandardScaler
    
    from dscribe.descriptors import SOAP
    from ase import Atoms
    from ase.cell import Cell

    import umap

except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing sklearn.manifold: {str(e)}\n")
    del sys

try:
    import copy
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing copy: {str(e)}\n")
    del sys

try:
    import os
    from typing import Dict, List, Tuple, Union
    from collections import defaultdict
    from joblib import Memory

except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing os: {str(e)}\n")
    del sys
    
try:
    import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap

except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while importing matplotlib.pyplot: {str(e)}\n")
    del sys
    
try:
    import seaborn as sns
except ImportError as e:
    import sys
    sys.stderr.write(f"An error occurred while seaborn: {str(e)}\n")
    del sys

class AbInitioThermodynamics_builder(PartitionManager):
    """
    A class for performing Ab Initio Thermodynamics analysis on atomic structures.

    This class extends PartitionManager to handle composition data, energy data, and perform
    various analyses such as phase diagram generation, local linear regression, and global linear prediction.

    Attributes:
        composition_data (np.ndarray): Array containing composition data for each structure.
        energy_data (np.ndarray): Array containing energy data for each structure.
        area_data (np.ndarray): Array containing area data for each structure.
    """

    def __init__(self, file_location: str = None, name: str = None, **kwargs):
        """
        Initialize the AbInitioThermodynamics_builder.

        Args:
            file_location (str, optional): Location of input files.
            name (str, optional): Name of the analysis.
            **kwargs: Additional keyword arguments.
        """
        super().__init__(name=name, file_location=file_location)
        
        self.composition_data = None
        self.energy_data = None 
        self.area_data = None
    '''
    def get_composition_data(self) -> Dict[str, np.ndarray]:
        """
        Extract composition, energy, and area data from containers.

        Returns:
            Dict[str, np.ndarray]: Dictionary containing composition_data, energy_data, and area_data.
        """
        print("Extracting composition, energy, and area data from containers...")
        
        composition_data = np.zeros((len(self.containers), len(self.uniqueAtomLabels)), dtype=np.float64)
        energy_data = np.zeros(len(self.containers), dtype=np.float64)
        area_data = np.zeros(len(self.containers), dtype=np.float64)
        
        for c_i, c in enumerate(self.containers):  
            comp = np.zeros_like(self.uniqueAtomLabels, dtype=np.int64)
            for ual, ac in zip(c.AtomPositionManager.uniqueAtomLabels, c.AtomPositionManager.atomCountByType):
                comp[self.uniqueAtomLabels_order[ual]] = ac 

            composition_data[c_i,:] = comp
            energy_data[c_i] = c.AtomPositionManager.E
            area_data[c_i] = c.AtomPositionManager.get_area('z')

        self.composition_data, self.energy_data, self.area_data = composition_data, energy_data, area_data

        print(f"Extracted data for {len(self.containers)} structures.")
        return {'composition_data': composition_data, 'energy_data': energy_data, 'area_data': area_data}


    def get_diagram_data(self, ID_reference: List[int], composition_data: np.ndarray, 
                         energy_data: np.ndarray, area_data: np.ndarray, especie: str) -> np.ndarray:
        """
        Calculate diagram data for phase diagram generation.

        Args:
            ID_reference (List[int]): List of reference structure IDs.
            composition_data (np.ndarray): Array of composition data.
            energy_data (np.ndarray): Array of energy data.
            area_data (np.ndarray): Array of area data.
            especie (str): Chemical species to focus on.

        Returns:
            np.ndarray: Array containing diagram data for phase diagram plotting.
        """
        print(f"Calculating diagram data for phase diagram generation, focusing on species: {especie}")
        
        composition_reference = composition_data[ID_reference, :] 
        energy_reference = energy_data[ID_reference] 

        reference_mu_index = next(cr_i for cr_i, cr in enumerate(composition_reference) 
                                  if np.sum(cr) == cr[self.uniqueAtomLabels_order[especie]])

        mask = np.ones(len(energy_data), dtype=bool)
        mask[ID_reference] = False

        composition_relevant = composition_data[mask,:]
        energy_relevant = energy_data[mask]
        area_relevant = area_data[mask]

        diagram_data = np.zeros((energy_relevant.shape[0], 2))

        for mu in [0, 1]:
            for i, (E, C, A) in enumerate(zip(energy_relevant, composition_relevant, area_relevant)):
                E_ref_mask = np.zeros_like(energy_reference)
                E_ref_mask[reference_mu_index] = mu

                mu_value = np.linalg.solve(composition_reference, energy_reference + E_ref_mask)
                gamma = 1/A * (E - np.sum(mu_value * C))

                diagram_data[i, mu] = gamma

        print(f"Diagram data calculated for {energy_relevant.shape[0]} structures.")
        return diagram_data


    # Function to create linear model
    def data_linear(X, y, force_negative=False):
        if force_negative:
            # Use non-negative least squares and negate the result
            from scipy.optimize import nnls
            coefficients, _ = nnls(X, -y)
            coefficients = -coefficients
        else:
            coefficients, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
        y_pred = X @ coefficients
        errors = y - y_pred
        return coefficients, errors, y_pred

    def linear_predict(self, compositions: np.ndarray, energies: np.ndarray, target:np.ndarray=None,
                              regularization: float = 1e-8, verbose: bool = False, 
                              weights: str = None, center: bool = False, force_negative: bool = False
                              ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Perform global linear prediction on composition-energy data.

        Args:
            compositions (np.ndarray): Array of composition data.
            energies (np.ndarray): Array of energy data.
            regularization (float): Regularization parameter for linear regression.
            verbose (bool): If True, print detailed information.
            center (bool): If True, center the data before prediction.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray]: Compositions, predicted energies, and coefficients.
        """
        if verbose:
            print(f"Trainning linear model. ")
            print(f"      * Regularization:{regularization}  ")
            print(f"      * Weight:{weight}  ")
            print(f"      * Center:{center}  ")
            print(f"      * Force_negative:{force_negative}")

        target = compositions if type(target) is type(None) else target

        mean_compositions = np.mean(compositions, axis=0) if center else np.zeros(compositions.shape[1])
        centered_compositions = compositions - mean_compositions 
        mean_target = np.mean(target, axis=0) if center else np.zeros(target.shape[1])
        centered_target = target - mean_target

        if weights == 'distances':
            tree = cKDTree(compositions)
            distances, indices = tree.query(target, k=k)
            w = np.exp(-distances)

            #nearest_compositions = compositions[indices]
            #nearest_energies = energies[indices]
        else:
            w = np.ones_like(distances)

        w_norm = w / w.sum(axis=1, keepdims=True)

        sqrt_w_norm = np.sqrt(w_norm)
        weighted_compositions = centered_compositions * sqrt_w_norm

        mean_energy = np.mean(energies) if center else 0
        centered_energies = energies - mean_energy
        weighted_energies = centered_energies * sqrt_w_norm.ravel()

        if force_negative:
            # Use non-negative least squares and negate the result
            coeffs, _ = nnls(weighted_compositions, -weighted_energies)
            coeffs = -coeffs
        else:
            A = np.dot(weighted_compositions.T, weighted_compositions)
            A += regularization * np.eye(A.shape[0])
            B = np.dot(weighted_compositions.T, weighted_energies)
            coeffs = np.linalg.solve(A, B)

        #A = np.dot(centered_compositions.T, centered_compositions * w_norm[:, np.newaxis])
        #A += regularization * np.eye(A.shape[0])
        
        #mean_energy = np.mean(energies) if center else 0
        #centered_energies = energies - mean_energy

        #B = np.dot(centered_compositions.T, centered_energies * w_norm)
        #coeffs = np.linalg.solve(A, B)

        predicted_energy = mean_energy + np.dot(centered_target, coeffs)

        if verbose: 
            train_rmse = np.sqrt(np.mean((energies - np.dot(centered_compositions, coeffs) - mean_energy)**2))
            validation_rmse = np.sqrt(np.mean((energies - predicted_energy)**2))
            print(f"RMSE (train): {train_rmse:.4f}")
            print(f"RMSE (validation): {validation_rmse:.4f}")
            print(f"Coefficients: {' '.join([f'mu({ual})={cd:.3f}' for cd, ual in zip(coeffs, self.uniqueAtomLabels)])}")
        
        return target, predicted_energy, coeffs

    def locally_linear_predict(self, compositions: np.ndarray, energies: np.ndarray, 
                               target: np.ndarray, k: int = 5, regularization: float = 1e-8, 
                               verbose: bool = False, center: bool = True, 
                               weights: str = 'none') -> Tuple[float, np.ndarray]:
        """
        Predict energy for a target composition using locally linear regression.

        Args:
            compositions (np.ndarray): Array of composition data.
            energies (np.ndarray): Array of energy data.
            target (np.ndarray): Target composition for prediction.
            k (int): Number of nearest neighbors to use.
            regularization (float): Regularization parameter for linear regression.
            verbose (bool): If True, print detailed information.
            center (bool): If True, center the data before prediction.
            weights (str): Weighting method ('none' or 'distances').

        Returns:
            Tuple[float, np.ndarray]: Predicted energy and coefficients.
        """
        if verbose:
            print(f"Performing locally linear prediction for target composition: {target}")

        tree = cKDTree(compositions)
        distances, indices = tree.query(target, k=k)

        nearest_compositions = compositions[indices]
        nearest_energies = energies[indices]
        
        mean_target = np.mean(target) if center else 0
        centered_compositions = nearest_compositions - mean_target 

        if weights == 'distances':
            weights = np.exp(-distances)
        else:
            weights = np.ones_like(distances)

        weights /= weights.sum()  

        A = np.dot(centered_compositions.T, centered_compositions * weights[:, np.newaxis])
        A += regularization * np.eye(A.shape[0])
        
        mean_energy = np.mean(nearest_energies) if center else 0
        centered_energies = nearest_energies - mean_energy

        B = np.dot(centered_compositions.T, centered_energies * weights)
        coeffs = np.linalg.solve(A, B)

        predicted_energy = mean_energy + np.dot(coeffs, target - mean_target)

        if verbose: 
            print(f"Nearest compositions: \n{nearest_compositions}")
            print(f"Distances: \n{distances}")
            print(f"Weights: \n{weights}")
            print(f"Predicted energy: {predicted_energy:.4f}")
            print(f" Coefficients { '  '.join([f'mu({ual})={cd:.3f}' for cd, ual in zip( coeffs, self.uniqueAtomLabels ) ]) } ")

        return predicted_energy, coeffs
    '''

    def n_fold_cross_validation(self, compositions: np.ndarray, energies: np.ndarray, 
                                k: int = 20, output_path: str = None, 
                                verbose: bool = False) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Perform N-fold cross-validation on the dataset.

        Args:
            compositions (np.ndarray): Array of composition data.
            energies (np.ndarray): Array of energy data.
            k (int): Number of nearest neighbors for local linear regression.
            output_path (str, optional): Path to save output files.
            verbose (bool): If True, print detailed information.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: Arrays of errors, predicted energies, 
                                                                   composition data, and coefficients.
        """
        print(f"Performing {k}-fold cross-validation...")

        unique_compositions = np.unique(compositions, axis=0)
        errors = []
        real_E = []
        predicted_E = []
        composition_data = []
        coeffs_data = []

        for i, comp in enumerate(unique_compositions):
            if verbose:
                print(f"Processing unique composition {i+1}/{len(unique_compositions)}: {comp}")
            
            mask = np.all(compositions == comp, axis=1)
            train_compositions = compositions[~mask]
            train_energies = energies[~mask]
            test_compositions = compositions[mask]
            test_energies = energies[mask]

            for test_comp, real_energy in zip(test_compositions, test_energies):
                predicted_energy, coeffs = self.locally_linear_predict(train_compositions, train_energies, test_comp, k, verbose=False)
                error = predicted_energy - real_energy

                coeffs_data.append(coeffs)
                errors.append(error / np.sum(test_comp))
                predicted_E.append(predicted_energy)
                real_E .append(real_energy)
                composition_data.append(test_comp)
            
        data = np.array([np.concatenate((c, [e], [Ep], [Er], Mu)) for e, c, Ep, Er, Mu in zip(errors, composition_data, predicted_E, real_E, coeffs_data)])

        if verbose:
            print(f"Processing {len(unique_compositions)} unique composition : error {np.sum(errors)}")
            print(f" Mean Coefficients { '  '.join([f'mu({ual})={cd:.3f}' for cd, ual in zip( np.mean(coeffs_data,axis=0), self.uniqueAtomLabels ) ]) } ")

        if output_path:
            self.save_array_to_csv(data, column_names=np.concatenate((self.uniqueAtomLabels, ['error', 'predicted e', 'E', *[f'Coeff {ua}' for ua in self.uniqueAtomLabels] ])), 
                                   sample_numbers=True, file_path=output_path)
            print(f"Cross-validation results saved to {output_path}")

        print(f"Cross-validation completed. RMSE: {np.sqrt(np.mean(np.array(errors)**2)):.4f}")
        return np.array(errors), np.array(predicted_E), np.array(composition_data), np.array(coeffs_data)

    def find_optimal_k(self, composition_data: Dict[str, np.ndarray], initial_step: int = 10, 
                       refinement_step: int = 1, verbose: bool = False) -> Tuple[int, List, List, np.ndarray]:
        """
        Find the optimal value of k for locally linear regression.

        Args:
            composition_data (Dict[str, np.ndarray]): Dictionary containing composition and energy data.
            initial_step (int): Step size for initial broad search.
            refinement_step (int): Step size for refined search.
            verbose (bool): If True, print detailed information.

        Returns:
            Tuple[int, List, List, np.ndarray]: Optimal k value, initial errors, refined errors, and coefficients.
        """
        print("Finding optimal k for locally linear regression...")

        compositions = composition_data['composition_data']
        energies = composition_data['energy_data']
        n_samples = int(compositions.shape[0] * 0.9)

        k_values = range(compositions.shape[1], n_samples, initial_step)
        initial_errors = []
        error_history = []
        coeffs_history = []

        for idx, k in enumerate(k_values):
            errors, _, _, coeffs = self.n_fold_cross_validation(compositions, energies, k=k, verbose=False)
            current_rmse = np.mean(errors**2)**0.5
            initial_errors.append((k, current_rmse))
            error_history.append(current_rmse)
            coeffs_history.append(coeffs)

            if verbose:
                print(f"Initial search - k: {k}, RMSE: {current_rmse:.4f}, Progress: {100*(idx+1)/len(k_values):.2f}%")

            if len(error_history) > 4 and all(abs(error_history[-i-1] - error_history[-i-2]) < 1e-4 for i in range(1, 5)):
                if verbose:
                    print(f"Early stopping at k: {k} due to minimal change in error.")
                break

        initial_best_k = min(initial_errors, key=lambda x: x[1])[0]
        print(f"Best k after initial search: {initial_best_k}")

        refined_range = range(max(1, initial_best_k - initial_step), 
                              min(n_samples, initial_best_k + initial_step), 
                              refinement_step)
        refined_errors = []
        for idx, k in enumerate(refined_range):
            errors, _, _, coeffs = self.n_fold_cross_validation(compositions, energies, k=k, verbose=False)
            current_rmse = np.mean(errors**2)**0.5
            refined_errors.append((k, current_rmse))
            coeffs_history.append(coeffs)

            if verbose:
                print(f"Refined search - k: {k}, RMSE: {current_rmse:.4f}, Progress: {100*(idx+1)/len(refined_range):.2f}%")

        best_k = min(refined_errors, key=lambda x: x[1])[0]
        print(f"Optimal k after refined search: {best_k}")

        return best_k, initial_errors, refined_errors, np.array(coeffs_history)

    def plot_k_convergence(self, initial_errors: List[Tuple[int, float]], 
                           refined_errors: List[Tuple[int, float]], 
                           coeffs: np.ndarray, output_path: str = None, 
                           verbose: bool = False) -> None:
        """
        Plot the convergence of RMSE and coefficients with respect to k values.

        Args:
            initial_errors (List[Tuple[int, float]]): List of (k, RMSE) from initial search.
            refined_errors (List[Tuple[int, float]]): List of (k, RMSE) from refined search.
            coeffs (np.ndarray): Array of coefficients for different k values.
            output_path (str, optional): Path to save the plot.
            verbose (bool): If True, print additional information.
        """
        print("Plotting k convergence and coefficient trends...")

        initial_k, initial_rmse = zip(*initial_errors)
        refined_k, refined_rmse = zip(*refined_errors)
        
        fig, ax = plt.subplots(2, 1, figsize=(12, 14))

        # RMSE convergence plot
        ax[0].plot(initial_k, initial_rmse, 'o-', label='Initial Search', color='blue')
        ax[0].plot(refined_k, refined_rmse, 'x-', label='Refined Search', color='red')
        ax[0].set_xlabel('k value')
        ax[0].set_ylabel('RMSE')
        ax[0].set_title('Convergence of RMSE with Different k Values')
        ax[0].legend()
        ax[0].grid(True)
        
        # Coefficients plot
        N, samples, atom_types = coeffs.shape
        colors = plt.cm.viridis(np.linspace(0, 1, atom_types))
        
        for atom_type in range(atom_types):
            for n in range(samples):
                label = f'{self.uniqueAtomLabels[atom_type]}' if n == 0 else None
                ax[1].plot(initial_k + refined_k, coeffs[:, n, atom_type], 'o-', 
                           color=colors[atom_type], alpha=0.2, label=label)

        ax[1].set_xlabel('k value')
        ax[1].set_ylabel('Coefficient Value')
        ax[1].set_title('Coefficients Trend with k Values')
        ax[1].legend()

        plt.tight_layout()
        
        if output_path:
            plt.savefig(f'{output_path}/k_convergence_with_coeffs.png', dpi=300)
            if verbose:
                print(f"Convergence plot saved to {output_path}/k_convergence_with_coeffs.png")
        else:
            plt.show()

    def plot_phase_diagram(self, diagram_data: np.ndarray, mu_max: float, mu_min: float, 
                           output_path: str = None, window_size: Tuple[int, int] = (12, 8), 
                           save: bool = True, verbose: bool = True) -> None:
        """
        Plot a phase diagram with extrapolated lines and highlight the lower envelope.

        Args:
            diagram_data (np.ndarray): An Nx2 array with each row being [y-intercept, slope] for a line.
            mu_max (float): Maximum chemical potential value.
            mu_min (float): Minimum chemical potential value.
            output_path (str, optional): Path to save the plot image.
            window_size (Tuple[int, int]): Size of the plotting window.
            save (bool): Whether to save the plot to a file.
            verbose (bool): Whether to print additional information.
        """
        print("Generating phase diagram plot...")

        plt.figure(figsize=window_size)

        x_values = np.linspace(mu_min, mu_max, 100)
        lower_envelope = np.inf * np.ones_like(x_values)
        optimal_structures = []

        for index, (x, y) in enumerate(diagram_data):
            m = (y - x) / (1 - 0)
            b = y - m * 1
            y_values = m * x_values + b
            
            plt.plot(x_values, y_values, alpha=0.5, label=f'Structure {index}')

            # Update lower envelope
            mask = y_values < lower_envelope
            lower_envelope[mask] = y_values[mask]
            optimal_structures.append(index)

        # Plot lower envelope
        plt.plot(x_values, lower_envelope, 'k-', linewidth=2, label='Lower Envelope')

        plt.xlabel('Chemical Potential (μ)')
        plt.ylabel('Formation Energy (γ)')
        plt.title('Phase Diagram with Lower Envelope')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True)

        if save:
            if not output_path:
                output_path = '.'
            plt.savefig(f'{output_path}/phase_diagram_plot.png', dpi=300, bbox_inches='tight')
            if verbose:
                print(f"Phase diagram plot saved to {output_path}/phase_diagram_plot.png")
        else:
            plt.show()

        if verbose:
            print(f"Optimal structures: {optimal_structures}")

    def plot_manifold(self, features: np.ndarray, response: np.ndarray, 
                      output_path: str = None, save: bool = True, 
                      verbose: bool = True) -> None:
        """
        Plot the manifold of the data using T-SNE and PCA, along with the response variable.

        Args:
            features (np.ndarray): Feature array (typically composition data).
            response (np.ndarray): Response array (typically energy or error data).
            output_path (str, optional): Path to save the plot.
            save (bool): Whether to save the plot to a file.
            verbose (bool): Whether to print additional information.
        """
        print("Generating manifold plots using T-SNE and PCA...")

        tsne = TSNE(n_components=2, random_state=42)
        tsne_results = tsne.fit_transform(features)

        pca = PCA(n_components=3)
        pca_results = pca.fit_transform(features)
        explained_variance = pca.explained_variance_ratio_

        fig, ax = plt.subplots(2, 2, figsize=(20, 20))

        # T-SNE plot
        sc = ax[0, 0].scatter(tsne_results[:, 0], tsne_results[:, 1], c=response, cmap='viridis')
        ax[0, 0].set_title('T-SNE Projection')
        ax[0, 0].set_xlabel('T-SNE Component 1')
        ax[0, 0].set_ylabel('T-SNE Component 2')
        plt.colorbar(sc, ax=ax[0, 0], label='Response')

        # PCA plot (2D projection)
        sc_pca = ax[0, 1].scatter(pca_results[:, 0], pca_results[:, 1], c=response, cmap='viridis')
        ax[0, 1].set_title('PCA Projection (2D)')
        ax[0, 1].set_xlabel(f'PCA Component 1 ({explained_variance[0]*100:.2f}% variance)')
        ax[0, 1].set_ylabel(f'PCA Component 2 ({explained_variance[1]*100:.2f}% variance)')
        plt.colorbar(sc_pca, ax=ax[0, 1], label='Response')

        # PCA plot (3D projection)
        ax_3d = fig.add_subplot(223, projection='3d')
        sc_pca_3d = ax_3d.scatter(pca_results[:, 0], pca_results[:, 1], pca_results[:, 2], 
                                  c=response, cmap='viridis')
        ax_3d.set_title('PCA Projection (3D)')
        ax_3d.set_xlabel(f'PC1 ({explained_variance[0]*100:.2f}%)')
        ax_3d.set_ylabel(f'PC2 ({explained_variance[1]*100:.2f}%)')
        ax_3d.set_zlabel(f'PC3 ({explained_variance[2]*100:.2f}%)')
        plt.colorbar(sc_pca_3d, ax=ax_3d, label='Response')

        # Response plot
        ax[1, 1].plot(response, 'o-', c='#1f77b4')
        RMSE = np.sqrt(np.mean(response**2))
        ax[1, 1].axhline(y=RMSE, color='r', linestyle='--', label=f'RMSE: {RMSE:.5f}')
        ax[1, 1].set_title('Response Distribution')
        ax[1, 1].set_xlabel('Index')
        ax[1, 1].set_ylabel('Response')
        ax[1, 1].legend()
        plt.tight_layout()

        if save:
            if not output_path:
                output_path = '.'
            plt.savefig(f'{output_path}/manifold_plot.png', dpi=300)
            if verbose:
                print(f"Manifold plot saved to {output_path}/manifold_plot.png")
        else:
            plt.show()

        if verbose:
            print(f"PCA explained variance ratios: {explained_variance}")

    def cluster_analysis(self, features: np.ndarray, n_clusters: int = 5, 
                         output_path: str = None, save: bool = True, 
                         verbose: bool = True) -> Tuple[np.ndarray, np.ndarray]:
        """
        Perform cluster analysis on the feature data using K-means clustering.

        Args:
            features (np.ndarray): Feature array (typically composition data).
            n_clusters (int): Number of clusters for K-means algorithm.
            output_path (str, optional): Path to save the plot.
            save (bool): Whether to save the plot to a file.
            verbose (bool): Whether to print additional information.

        Returns:
            Tuple[np.ndarray, np.ndarray]: Cluster labels and cluster centers.
        """
        print(f"Performing cluster analysis with {n_clusters} clusters...")

        # Perform K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(features)
        cluster_centers = kmeans.cluster_centers_

        # Reduce dimensionality for visualization
        pca = PCA(n_components=2)
        reduced_features = pca.fit_transform(features)
        reduced_centers = pca.transform(cluster_centers)

        # Plotting
        plt.figure(figsize=(12, 8))
        scatter = plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=cluster_labels, cmap='viridis')
        plt.scatter(reduced_centers[:, 0], reduced_centers[:, 1], c='red', marker='x', s=200, linewidths=3)
        plt.title('Cluster Analysis of Compositions')
        plt.xlabel(f'PCA Component 1 ({pca.explained_variance_ratio_[0]:.2f}% variance)')
        plt.ylabel(f'PCA Component 2 ({pca.explained_variance_ratio_[1]:.2f}% variance)')
        plt.colorbar(scatter, label='Cluster')

        if save:
            if not output_path:
                output_path = '.'
            plt.savefig(f'{output_path}/cluster_analysis.png', dpi=300)
            if verbose:
                print(f"Cluster analysis plot saved to {output_path}/cluster_analysis.png")
        else:
            plt.show()

        if verbose:
            print(f"Clustering completed. Found {n_clusters} clusters.")

        return cluster_labels, cluster_centers

    def composition_energy_correlation(self, compositions: np.ndarray, energies: np.ndarray, 
                                       output_path: str = None, save: bool = True, 
                                       verbose: bool = True) -> Dict[str, float]:
        """
        Analyze the correlation between composition and energy.

        Args:
            compositions (np.ndarray): Composition data.
            energies (np.ndarray): Energy data.
            output_path (str, optional): Path to save the plot.
            save (bool): Whether to save the plot to a file.
            verbose (bool): Whether to print additional information.

        Returns:
            Dict[str, float]: Dictionary of correlation coefficients for each element.
        """
        print("Analyzing correlation between composition and energy...")

        correlations = {}
        n_elements = compositions.shape[1]

        fig, axs = plt.subplots(n_elements, 1, figsize=(12, 6 * n_elements))
        if n_elements == 1:
            axs = [axs]

        for i in range(n_elements):
            element_composition = compositions[:, i]
            slope, intercept, r_value, p_value, std_err = linregress(element_composition, energies)
            correlations[f'Element_{i}'] = r_value

            axs[i].scatter(element_composition, energies)
            axs[i].plot(element_composition, slope * element_composition + intercept, color='red')
            axs[i].set_xlabel(f'Composition of Element {i}')
            axs[i].set_ylabel('Energy')
            axs[i].set_title(f'Correlation for Element {i} (r = {r_value:.2f})')

        plt.tight_layout()

        if save:
            if not output_path:
                output_path = '.'
            plt.savefig(f'{output_path}/composition_energy_correlation.png', dpi=300)
            if verbose:
                print(f"Correlation plot saved to {output_path}/composition_energy_correlation.png")
        else:
            plt.show()

        if verbose:
            print("Correlation analysis completed.")
            for element, correlation in correlations.items():
                print(f"{element} correlation with energy: {correlation:.2f}")

        return correlations

    def energy_landscape_analysis(self, compositions: np.ndarray, energies: np.ndarray, 
                                  output_path: str = None, save: bool = True, 
                                  verbose: bool = True) -> None:
        """
        Analyze and visualize the energy landscape of the system.

        Args:
            compositions (np.ndarray): Composition data.
            energies (np.ndarray): Energy data.
            output_path (str, optional): Path to save the plot.
            save (bool): Whether to save the plot to a file.
            verbose (bool): Whether to print additional information.
        """
        print("Analyzing energy landscape...")

        # Reduce dimensionality to 2D for visualization
        pca = PCA(n_components=2)
        reduced_compositions = pca.fit_transform(compositions)

        # Create a grid for interpolation
        x = np.linspace(reduced_compositions[:, 0].min(), reduced_compositions[:, 0].max(), 100)
        y = np.linspace(reduced_compositions[:, 1].min(), reduced_compositions[:, 1].max(), 100)
        X, Y = np.meshgrid(x, y)

        # Interpolate energy values
        from scipy.interpolate import griddata
        Z = griddata(reduced_compositions, energies, (X, Y), method='cubic')

        # Plotting
        fig, ax = plt.subplots(figsize=(12, 8))
        contour = ax.contourf(X, Y, Z, levels=20, cmap='viridis')
        scatter = ax.scatter(reduced_compositions[:, 0], reduced_compositions[:, 1], c=energies, 
                             cmap='viridis', edgecolor='black')
        
        plt.colorbar(contour, label='Energy')
        ax.set_xlabel(f'PCA Component 1 ({pca.explained_variance_ratio_[0]:.2f}% variance)')
        ax.set_ylabel(f'PCA Component 2 ({pca.explained_variance_ratio_[1]:.2f}% variance)')
        ax.set_title('Energy Landscape Analysis')

        if save:
            if not output_path:
                output_path = '.'
            plt.savefig(f'{output_path}/energy_landscape.png', dpi=300)
            if verbose:
                print(f"Energy landscape plot saved to {output_path}/energy_landscape.png")
        else:
            plt.show()

        if verbose:
            print("Energy landscape analysis completed.")

    def thermodynamic_stability_prediction(self, compositions: np.ndarray, energies: np.ndarray, 
                                           temperatures: np.ndarray, 
                                           output_path: str = None, save: bool = True, 
                                           verbose: bool = True) -> np.ndarray:
        """
        Predict thermodynamic stability at different temperatures using a simple model.

        Args:
            compositions (np.ndarray): Composition data.
            energies (np.ndarray): Energy data.
            temperatures (np.ndarray): Array of temperatures to analyze.
            output_path (str, optional): Path to save the plot.
            save (bool): Whether to save the plot to a file.
            verbose (bool): Whether to print additional information.

        Returns:
            np.ndarray: Predicted stable compositions at each temperature.
        """
        print("Predicting thermodynamic stability at different temperatures...")

        def gibbs_energy(E, T, S):
            return E - T * S

        # Estimate entropy (this is a simplification and should be replaced with a more accurate model)
        entropies = np.sum(compositions * np.log(compositions + 1e-10), axis=1)

        stable_compositions = []
        for T in temperatures:
            G = gibbs_energy(energies, T, entropies)
            stable_index = np.argmin(G)
            stable_compositions.append(compositions[stable_index])

        stable_compositions = np.array(stable_compositions)

        # Plotting
        fig, ax = plt.subplots(figsize=(12, 8))
        for i in range(compositions.shape[1]):
            ax.plot(temperatures, stable_compositions[:, i], label=f'Element {i}')

        ax.set_xlabel('Temperature (K)')
        ax.set_ylabel('Composition Fraction')
        ax.set_title('Predicted Stable Compositions vs Temperature')
        ax.legend()

        if save:
            if not output_path:
                output_path = '.'
            plt.savefig(f'{output_path}/thermodynamic_stability.png', dpi=300)
            if verbose:
                print(f"Thermodynamic stability plot saved to {output_path}/thermodynamic_stability.png")
        else:
            plt.show()

        if verbose:
            print("Thermodynamic stability prediction completed.")

        return stable_compositions

    def calculate_ensemble_properties(self, energies: np.ndarray, volumes: np.ndarray, 
                                      temperatures: np.ndarray, particles: np.ndarray,
                                      ensemble: str = 'canonical', mass: float = 1.0,
                                      output_path: str = None, save: bool = True, 
                                      verbose: bool = True) -> Dict[str, np.ndarray]:
        """
        Calculate partition function and thermodynamic parameters for different ensembles.

        Args:
            energies (np.ndarray): Energy levels of the system.
            volumes (np.ndarray): Volumes of the system.
            temperatures (np.ndarray): Array of temperatures to analyze.
            particles (np.ndarray): Array of particle numbers (for grand canonical ensemble).
            ensemble (str): Type of ensemble ('canonical', 'microcanonical', 'grand_canonical').
            mass (float): Mass of the particles (used in some calculations).
            output_path (str, optional): Path to save the plots.
            save (bool): Whether to save the plots to files.
            verbose (bool): Whether to print additional information.

        Returns:
            Dict[str, np.ndarray]: Dictionary of calculated thermodynamic properties.
        """
        print(f"Calculating ensemble properties for {ensemble} ensemble...")

        k_B = Boltzmann
        h = hbar * 2 * pi
        properties = {}

        if ensemble == 'canonical':
            # Canonical ensemble calculations
            Z = np.sum(np.exp(-energies[:, np.newaxis] / (k_B * temperatures)), axis=0)
            properties['partition_function'] = Z
            
            # Free energy
            F = -k_B * temperatures * np.log(Z)
            properties['free_energy'] = F
            
            # Internal energy
            U = np.sum(energies[:, np.newaxis] * np.exp(-energies[:, np.newaxis] / (k_B * temperatures)), axis=0) / Z
            properties['internal_energy'] = U
            
            # Entropy
            S = k_B * np.log(Z) + U / temperatures
            properties['entropy'] = S
            
            # Heat capacity
            C_V = k_B * (np.sum(energies[:, np.newaxis]**2 * np.exp(-energies[:, np.newaxis] / (k_B * temperatures)), axis=0) / Z
                         - (np.sum(energies[:, np.newaxis] * np.exp(-energies[:, np.newaxis] / (k_B * temperatures)), axis=0) / Z)**2) / temperatures**2
            properties['heat_capacity'] = C_V

        elif ensemble == 'microcanonical':
            # Microcanonical ensemble calculations
            # Assuming a simple model where Ω(E) ~ E^(3N/2-1) for an ideal gas
            N = len(particles)  # Number of particles
            Omega = energies**(3*N/2 - 1)
            properties['density_of_states'] = Omega
            
            # Entropy
            S = k_B * np.log(Omega)
            properties['entropy'] = S
            
            # Temperature (derived from entropy)
            T = 1 / (np.gradient(S, energies))
            properties['temperature'] = T
            
            # Heat capacity
            C_V = 1 / (np.gradient(1/T, energies))
            properties['heat_capacity'] = C_V

        elif ensemble == 'grand_canonical':
            # Grand Canonical ensemble calculations
            mu = np.linspace(np.min(energies), np.max(energies), 100)  # Chemical potential range
            Z_grand = np.sum(np.exp((mu[:, np.newaxis, np.newaxis] - energies[:, np.newaxis]) / (k_B * temperatures)), axis=0)
            properties['grand_partition_function'] = Z_grand
            
            # Grand potential
            Omega = -k_B * temperatures * np.log(Z_grand)
            properties['grand_potential'] = Omega
            
            # Average number of particles
            N_avg = np.sum(particles[:, np.newaxis, np.newaxis] * np.exp((mu[:, np.newaxis, np.newaxis] - energies[:, np.newaxis]) / (k_B * temperatures)), axis=0) / Z_grand
            properties['average_particles'] = N_avg
            
            # Internal energy
            U = np.sum(energies[:, np.newaxis, np.newaxis] * np.exp((mu[:, np.newaxis, np.newaxis] - energies[:, np.newaxis]) / (k_B * temperatures)), axis=0) / Z_grand
            properties['internal_energy'] = U

        # Plotting
        fig, axs = plt.subplots(2, 2, figsize=(16, 16))
        
        if ensemble == 'canonical':
            axs[0, 0].plot(temperatures, properties['free_energy'])
            axs[0, 0].set_xlabel('Temperature (K)')
            axs[0, 0].set_ylabel('Free Energy (J)')
            axs[0, 0].set_title('Free Energy vs Temperature')

            axs[0, 1].plot(temperatures, properties['internal_energy'])
            axs[0, 1].set_xlabel('Temperature (K)')
            axs[0, 1].set_ylabel('Internal Energy (J)')
            axs[0, 1].set_title('Internal Energy vs Temperature')

            axs[1, 0].plot(temperatures, properties['entropy'])
            axs[1, 0].set_xlabel('Temperature (K)')
            axs[1, 0].set_ylabel('Entropy (J/K)')
            axs[1, 0].set_title('Entropy vs Temperature')

            axs[1, 1].plot(temperatures, properties['heat_capacity'])
            axs[1, 1].set_xlabel('Temperature (K)')
            axs[1, 1].set_ylabel('Heat Capacity (J/K)')
            axs[1, 1].set_title('Heat Capacity vs Temperature')

        elif ensemble == 'microcanonical':
            axs[0, 0].plot(energies, properties['density_of_states'])
            axs[0, 0].set_xlabel('Energy (J)')
            axs[0, 0].set_ylabel('Density of States')
            axs[0, 0].set_title('Density of States vs Energy')

            axs[0, 1].plot(energies, properties['entropy'])
            axs[0, 1].set_xlabel('Energy (J)')
            axs[0, 1].set_ylabel('Entropy (J/K)')
            axs[0, 1].set_title('Entropy vs Energy')

            axs[1, 0].plot(energies, properties['temperature'])
            axs[1, 0].set_xlabel('Energy (J)')
            axs[1, 0].set_ylabel('Temperature (K)')
            axs[1, 0].set_title('Temperature vs Energy')

            axs[1, 1].plot(energies, properties['heat_capacity'])
            axs[1, 1].set_xlabel('Energy (J)')
            axs[1, 1].set_ylabel('Heat Capacity (J/K)')
            axs[1, 1].set_title('Heat Capacity vs Energy')

        elif ensemble == 'grand_canonical':
            axs[0, 0].pcolormesh(temperatures, mu, properties['grand_potential'])
            axs[0, 0].set_xlabel('Temperature (K)')
            axs[0, 0].set_ylabel('Chemical Potential (J)')
            axs[0, 0].set_title('Grand Potential')

            axs[0, 1].pcolormesh(temperatures, mu, properties['average_particles'])
            axs[0, 1].set_xlabel('Temperature (K)')
            axs[0, 1].set_ylabel('Chemical Potential (J)')
            axs[0, 1].set_title('Average Number of Particles')

            axs[1, 0].pcolormesh(temperatures, mu, properties['internal_energy'])
            axs[1, 0].set_xlabel('Temperature (K)')
            axs[1, 0].set_ylabel('Chemical Potential (J)')
            axs[1, 0].set_title('Internal Energy')

        plt.tight_layout()

        if save:
            if not output_path:
                output_path = '.'
            plt.savefig(f'{output_path}/{ensemble}_ensemble_properties.png', dpi=300)
            if verbose:
                print(f"{ensemble.capitalize()} ensemble properties plot saved to {output_path}/{ensemble}_ensemble_properties.png")
        else:
            plt.show()

        if verbose:
            print(f"Calculation of {ensemble} ensemble properties completed.")

        return properties


























    def get_composition_data(self) -> Dict[str, np.ndarray]:
        """
        Extract composition, energy, and area data from containers.

        Returns:
            Dict[str, np.ndarray]: Dictionary containing composition_data, energy_data, and area_data.
        """
        print("Extracting composition, energy, and area data from containers...")
        
        composition_data = np.zeros((len(self.containers), len(self.uniqueAtomLabels)), dtype=np.float64)
        energy_data = np.zeros(len(self.containers), dtype=np.float64)
        area_data = np.zeros(len(self.containers), dtype=np.float64)
        
        for c_i, c in enumerate(self.containers):  
            comp = np.zeros_like(self.uniqueAtomLabels, dtype=np.int64)
            for ual, ac in zip(c.AtomPositionManager.uniqueAtomLabels, c.AtomPositionManager.atomCountByType):
                comp[self.uniqueAtomLabels_order[ual]] = ac 

            composition_data[c_i,:] = comp
            energy_data[c_i] = c.AtomPositionManager.E
            area_data[c_i] = c.AtomPositionManager.get_area('z')

        self.composition_data, self.energy_data, self.area_data = composition_data, energy_data, area_data

        print(f"Extracted data for {len(self.containers)} structures.")
        return {'composition_data': composition_data, 'energy_data': energy_data, 'area_data': area_data, 'uniqueAtomLabels':self.uniqueAtomLabels}

    def get_diagram_data(self, ID_reference: List[int], composition_data: np.ndarray, 
                         energy_data: np.ndarray, area_data: np.ndarray, especie: str) -> np.ndarray:
        """
        Calculate diagram data for phase diagram generation.

        Args:
            ID_reference (List[int]): List of reference structure IDs.
            composition_data (np.ndarray): Array of composition data.
            energy_data (np.ndarray): Array of energy data.
            area_data (np.ndarray): Array of area data.
            especie (str): Chemical species to focus on.

        Returns:
            np.ndarray: Array containing diagram data for phase diagram plotting.
        """
        print(f"Calculating diagram data for phase diagram generation, focusing on species: {especie}")
        
        composition_reference = composition_data[ID_reference, :] 
        energy_reference = energy_data[ID_reference] 

        reference_mu_index = next(cr_i for cr_i, cr in enumerate(composition_reference) 
                                  if np.sum(cr) == cr[self.uniqueAtomLabels_order[especie]])

        mask = np.ones(len(energy_data), dtype=bool)
        mask[ID_reference] = False

        composition_relevant = composition_data[mask,:]
        energy_relevant = energy_data[mask]
        area_relevant = area_data[mask]

        diagram_data = np.zeros((energy_relevant.shape[0], 2))

        for mu in [0, 1]:
            for i, (E, C, A) in enumerate(zip(energy_relevant, composition_relevant, area_relevant)):
                E_ref_mask = np.zeros_like(energy_reference)
                E_ref_mask[reference_mu_index] = mu

                mu_value = np.linalg.solve(composition_reference, energy_reference + E_ref_mask)
                gamma = 1/A * (E - np.sum(mu_value * C))

                diagram_data[i, mu] = gamma

        print(f"Diagram data calculated for {energy_relevant.shape[0]} structures.")
        return diagram_data

    def n_fold_cross_validation(self, compositions: np.ndarray, energies: np.ndarray, 
                                k: int = 20, output_path: str = None, 
                                verbose: bool = False) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """
        Perform N-fold cross-validation on the dataset.

        Args:
            compositions (np.ndarray): Array of composition data.
            energies (np.ndarray): Array of energy data.
            k (int): Number of nearest neighbors for local linear regression.
            output_path (str, optional): Path to save output files.
            verbose (bool): If True, print detailed information.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]: Arrays of errors, predicted energies, 
                                                                   composition data, and coefficients.
        """
        print(f"Performing {k}-fold cross-validation...")

        unique_compositions = np.unique(compositions, axis=0)
        errors = []
        real_E = []
        predicted_E = []
        composition_data = []
        coeffs_data = []

        for i, comp in enumerate(unique_compositions):
            if verbose:
                print(f"Processing unique composition {i+1}/{len(unique_compositions)}: {comp}")
            
            mask = np.all(compositions == comp, axis=1)
            train_compositions = compositions[~mask]
            train_energies = energies[~mask]
            test_compositions = compositions[mask]
            test_energies = energies[mask]

            for test_comp, real_energy in zip(test_compositions, test_energies):
                coefficients, predictions, residuals = self.linear_predict(
                                            train_compositions, train_energies,
                                            regularization = 1e-8, verbose = False, 
                                            zero_intercept = True, force_negative = True)

                predicted_energy = np.sum(test_comp*coefficients[1:])
                error = predicted_energy - real_energy

                coeffs_data.append(coefficients[1:])
                errors.append(error / np.sum(test_comp))
                predicted_E.append(predicted_energy)
                real_E .append(real_energy)
                composition_data.append(test_comp)
            
        data = np.array([np.concatenate((c, [e], [Ep], [Er], Mu)) for e, c, Ep, Er, Mu in zip(errors, composition_data, predicted_E, real_E, coeffs_data)])

        if verbose:
            print(f"Processing {len(unique_compositions)} unique composition : error {np.sum(errors)}")
            print(f" Mean Coefficients { '  '.join([f'mu({ual})={cd:.3f}' for cd, ual in zip( np.mean(coeffs_data,axis=0), self.uniqueAtomLabels ) ]) } ")

        if output_path:
            self.save_array_to_csv(data, column_names=np.concatenate((self.uniqueAtomLabels, ['error', 'predicted e', 'E', *[f'Coeff {ua}' for ua in self.uniqueAtomLabels] ])), 
                                   sample_numbers=True, file_path=output_path)
            print(f"Cross-validation results saved to {output_path}")

        print(f"Cross-validation completed. RMSE: {np.sqrt(np.mean(np.array(errors)**2)):.4f}")
        return np.array(errors), np.array(predicted_E), np.array(composition_data), np.array(coeffs_data)

    def find_optimal_k(self, composition_data: Dict[str, np.ndarray], initial_step: int = 10, 
                       refinement_step: int = 1, verbose: bool = False) -> Tuple[int, List, List, np.ndarray]:
        """
        Find the optimal value of k for locally linear regression.

        Args:
            composition_data (Dict[str, np.ndarray]): Dictionary containing composition and energy data.
            initial_step (int): Step size for initial broad search.
            refinement_step (int): Step size for refined search.
            verbose (bool): If True, print detailed information.

        Returns:
            Tuple[int, List, List, np.ndarray]: Optimal k value, initial errors, refined errors, and coefficients.
        """
        print("Finding optimal k for locally linear regression...")

        compositions = composition_data['composition_data']
        energies = composition_data['energy_data']
        n_samples = int(compositions.shape[0] * 0.9)

        k_values = range(compositions.shape[1], n_samples, initial_step)
        initial_errors = []
        error_history = []
        coeffs_history = []

        for idx, k in enumerate(k_values):
            errors, _, _, coeffs = self.n_fold_cross_validation(compositions, energies, k=k, verbose=False)
            current_rmse = np.mean(errors**2)**0.5
            initial_errors.append((k, current_rmse))
            error_history.append(current_rmse)
            coeffs_history.append(coeffs)

            if verbose:
                print(f"Initial search - k: {k}, RMSE: {current_rmse:.4f}, Progress: {100*(idx+1)/len(k_values):.2f}%")

            if len(error_history) > 4 and abs(error_history[-1] - error_history[-2]) < 1e-4:
                if verbose:
                    print(f"Early stopping at k: {k} due to minimal change in error.")
                break

        initial_best_k = min(initial_errors, key=lambda x: x[1])[0]
        print(f"Best k after initial search: {initial_best_k}")

        refined_range = range(max(1, initial_best_k - initial_step), 
                              min(n_samples, initial_best_k + initial_step), 
                              refinement_step)
        refined_errors = []
        for idx, k in enumerate(refined_range):
            errors, _, _, coeffs = self.n_fold_cross_validation(compositions, energies, k=k, verbose=False)
            current_rmse = np.mean(errors**2)**0.5
            refined_errors.append((k, current_rmse))
            coeffs_history.append(coeffs)

            if verbose:
                print(f"Refined search - k: {k}, RMSE: {current_rmse:.4f}, Progress: {100*(idx+1)/len(refined_range):.2f}%")

        best_k = min(refined_errors, key=lambda x: x[1])[0]
        print(f"Optimal k after refined search: {best_k}")

        return best_k, initial_errors, refined_errors, np.array(coeffs_history)

    def linear_predict(self, X: np.ndarray, y: np.ndarray, 
                       regularization: float = 1e-8, verbose: bool = False, 
                       force_negative: bool = False, zero_intercept: bool = False,
                       method: str = 'ridge'
                       ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Ajusta un modelo lineal usando varios métodos, con opciones de regularización,
        forzar coeficientes negativos y hacer cero el término independiente.
        
        Args:
        X (np.ndarray): Matriz de características de entrada.
        y (np.ndarray): Vector de valores objetivo.
        regularization (float): Parámetro de regularización (por defecto 1e-8).
        verbose (bool): Si es True, imprime información adicional.
        force_negative (bool): Si es True, fuerza los coeficientes a ser no positivos usando NNLS.
        zero_intercept (bool): Si es True, fuerza el término independiente a ser cero.
        method (str): Método de resolución ('ridge', 'ols', o 'nnls').
        
        Returns:
        Tuple[np.ndarray, np.ndarray, np.ndarray]: Coeficientes, predicciones y residuos.
        """
        
        if zero_intercept:
            X_model = X
        else:
            X_model = np.column_stack([np.ones(X.shape[0]), X])
        
        n_features = X_model.shape[1]
        
        def solve_nnls(A, b):
            try:
                return nnls(A, b)
            except RuntimeError:
                if verbose:
                    print("NNLS no convergió. Usando solución de mínimos cuadrados con proyección.")
                coeffs, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
                coeffs[coeffs < 0] = 0  # Proyectar a no-negativos
                return coeffs, None

        if method == 'ls':
            if force_negative:
                X_aug = np.vstack([X_model, np.sqrt(regularization) * np.eye(n_features)])
                y_aug = np.concatenate([y, np.zeros(n_features)])
                coefficients, _ = solve_nnls(X_aug, -y_aug)
                coefficients = -coefficients

            else:
                coefficients, _, _, _ = np.linalg.lstsq(X_model, y, rcond=None)

        else:  # default to ridge regression
            if force_negative:
                X_aug = np.vstack([X_model, np.sqrt(regularization) * np.eye(n_features)])
                y_aug = np.concatenate([y, np.zeros(n_features)])
                coefficients, _ = solve_nnls(X_aug, -y_aug)
                coefficients = -coefficients
            else:
                XTX = X_model.T @ X_model
                XTy = X_model.T @ y
                coefficients = np.linalg.solve(XTX + regularization * np.eye(n_features), XTy)
        
        predictions = X_model @ coefficients
        residuals = y - predictions
        
        if verbose:
            print(f"Método utilizado: {method}")
            print(f"Coeficientes: {coefficients}")
            print(f"Error cuadrático medio: {np.mean(residuals**2)}")
        
        if zero_intercept:
            coefficients = np.insert(coefficients, 0, 0)
        
        return coefficients, predictions, residuals

    # PLOTs
    def correlation_plot(self, data, feature_names=None, figsize=(15, 15), output_file='correlation_plot.png'):
        """
        Generate a correlation plot with distributions on the diagonal, improved scatter plots 
        on the upper triangle, and correlation coefficients on the lower triangle, then save it to a file.
        
        Parameters:
        data (np.ndarray): Input data matrix with shape [samples, features].
        feature_names (list): List of feature names (optional).
        figsize (tuple): Figure size (width, height) in inches.
        output_file (str): Output filename for saving the plot.
        
        Returns:
        matplotlib.figure.Figure: The generated figure object.
        """
        directory = os.path.dirname(output_file)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        if feature_names is None:
            feature_names = [f'Feature_{i}' for i in range(data.shape[1])]
        
        n_features = data.shape[1]
        
        # Create figure and axes objects
        fig, axes = plt.subplots(n_features, n_features, figsize=figsize)
        
        # Create a custom colormap similar to 'coolwarm'
        colors = ['blue', 'white', 'red']
        n_bins = 100
        cmap = LinearSegmentedColormap.from_list('custom_diverging', colors, N=n_bins)
        
        for i in range(n_features):
            for j in range(n_features):
                ax = axes[i, j]
                
                if i == j:
                    # Diagonal: Distribution plot
                    ax.hist(data[:, i], bins=20, density=True, alpha=0.7)
                    kde = gaussian_kde(data[:, i])
                    x_range = np.linspace(data[:, i].min(), data[:, i].max(), 100)
                    ax.plot(x_range, kde(x_range))
                    ax.set_title(feature_names[i], fontsize=10)
                    ax.tick_params(axis='both', which='major', labelsize=8)
                elif i < j:
                    # Upper triangle: Scatter plot
                    ax.scatter(data[:, j], data[:, i], alpha=0.3, s=10)  # Smaller, more transparent points
                    ax.set_xlabel(feature_names[j], fontsize=8)
                    ax.set_ylabel(feature_names[i], fontsize=8)
                    ax.tick_params(axis='both', which='major', labelsize=6)
                else:
                    # Lower triangle: Correlation coefficient
                    corr = np.corrcoef(data[:, i], data[:, j])[0, 1]
                    ax.text(0.5, 0.5, f"{corr:.2f}", ha="center", va="center", fontsize=12)
                    ax.set_facecolor(cmap((corr + 1) / 2))
                    ax.set_xticks([])
                    ax.set_yticks([])
        
        plt.tight_layout()
        
        # Save the figure to a file
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f" >> Plot saved as {output_file}")
        
        return fig

    #achedir = './cache_dir'
    #memory = Memory(cachedir, verbose=0) 
    #@memory.cache   
    def calculate_soap_descriptors(self, r_cut: float = None, n_max: int = None, l_max: int = None, sigma: float = None):
        """
        Calculate Smooth Overlap of Atomic Positions (SOAP) descriptors for atomic structures.

        This method computes SOAP descriptors for each atom in the stored containers,
        organizing the results by atomic species.

        Args:
            r_cut (float, optional): Cutoff radius for atomic interactions. Defaults to 5.0.
            n_max (int, optional): Maximum number of radial basis functions. Defaults to 8.
            l_max (int, optional): Maximum degree of spherical harmonics. Defaults to 6.
            sigma (float, optional): The standard deviation of the Gaussian smearing function. Defaults to 0.03.

        Returns:
            tuple: A tuple containing two dictionaries:
                - descriptors_by_species: SOAP descriptors for each atomic species.
                - atom_info_by_species: Information about atom indices and container indices for each species.

        Note:
            This method assumes the existence of 'self.containers' and 'self.uniqueAtomLabels'.
        """
        # Set default values if None is provided
        r_cut = 5.0 if r_cut is None else r_cut
        n_max = 8 if n_max is None else n_max
        l_max = 6 if l_max is None else l_max
        sigma = 0.03 if sigma is None else sigma

        # Initialize SOAP descriptor
        soap = SOAP(species=self.uniqueAtomLabels, periodic=True, r_cut=r_cut, 
                    n_max=n_max, l_max=l_max, sigma=sigma, sparse=False)

        # Initialize dictionaries to store results
        descriptors_by_species = defaultdict(list)
        atom_info_by_species = defaultdict(list)

        # Iterate through containers to calculate descriptors
        for c_idx, c in enumerate(self.containers):
            # Create ASE Atoms object from container data
            atoms = Atoms(symbols=c.AtomPositionManager.atomLabelsList, 
                          positions=c.AtomPositionManager.atomPositions, 
                          cell=Cell(c.AtomPositionManager.latticeVectors))
            
            # Calculate SOAP descriptors for the current structure
            descriptors = soap.create(atoms)
            
            # Organize descriptors and atom info by species
            for atom_idx, (specie, descriptor) in enumerate(zip(c.AtomPositionManager.atomLabelsList, descriptors)):
                descriptors_by_species[specie].append(descriptor)
                atom_info_by_species[specie].append((c_idx, atom_idx))
        
        # Convert descriptor lists to numpy arrays for each species
        for species in descriptors_by_species:
            descriptors_by_species[species] = np.array(descriptors_by_species[species])
        
        return descriptors_by_species, atom_info_by_species

    def save_descriptors(self, descriptors_by_species, atom_info_by_species, output_dir):
        """
        Save SOAP descriptors and corresponding atom information to files.

        This method saves the calculated SOAP descriptors and associated atom information
        for each atomic species to separate files in the specified output directory.

        Args:
            descriptors_by_species (dict): A dictionary containing SOAP descriptors for each species.
                                           Key: atomic species, Value: numpy array of descriptors.
            atom_info_by_species (dict): A dictionary containing atom information for each species.
                                         Key: atomic species, Value: list of tuples (structure_index, atom_index).
            output_dir (str): Path to the directory where files will be saved.

        Returns:
            None

        Note:
            - Creates the output directory if it doesn't exist.
            - Saves descriptors as .npy files and atom information as .txt files.
            - Prints information about saved files to the console.
        """
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Iterate through each species and save its data
        for species, descriptors in descriptors_by_species.items():
            # Save descriptors as numpy array
            desc_filename = os.path.join(output_dir, f"descriptors_{species}.npy")
            np.save(desc_filename, descriptors)
            print(f"Descriptors for {species} saved to {desc_filename}")

            # Save atom information as text file
            info_filename = os.path.join(output_dir, f"atom_info_{species}.txt")
            with open(info_filename, 'w') as f:
                # Write header
                f.write("descriptor_index,structure_index,atom_index\n")
                # Write data for each atom
                for desc_idx, (struct_idx, atom_idx) in enumerate(atom_info_by_species[species]):
                    f.write(f"{desc_idx},{struct_idx},{atom_idx}\n")
            print(f"Atom information for {species} saved to {info_filename}")

    def verify_and_load_soap(self, output_dir='SOAPs'):
        """
        Verify the existence of SOAP descriptor files and load them if they exist.

        This method checks for the presence of SOAP descriptor and atom information files
        for each atomic species in the specified directory. If all files exist, it loads
        the data and returns it. If any file is missing, it returns False.

        Args:
            output_dir (str): Path to the directory where SOAP files are stored. Default is 'SOAPs'.

        Returns:
            tuple or bool: If all files exist, returns a tuple containing:
                           (descriptors_by_species, atom_info_by_species)
                           If any file is missing, returns False.

        Note:
            - Assumes the file naming convention: 'descriptors_{species}.npy' and 'atom_info_{species}.txt'
            - Requires self.uniqueAtomLabels to be defined with the list of atomic species.
        """
        descriptors_by_species = {}
        atom_info_by_species = {}

        for species in tqdm(self.uniqueAtomLabels, desc="Verifying and loading soap"):
            desc_filename = os.path.join(output_dir, f"descriptors_{species}.npy")
            info_filename = os.path.join(output_dir, f"atom_info_{species}.txt")

            # Check if both files exist for the current species
            if not (os.path.exists(desc_filename) and os.path.exists(info_filename)):
                print(f"Missing SOAP files for species {species}")
                return False

            # Load descriptor data
            descriptors_by_species[species] = np.load(desc_filename)

            # Load atom information
            atom_info_by_species[species] = []
            with open(info_filename, 'r') as f:
                next(f)  # Skip header
                for line in f:
                    _, struct_idx, atom_idx = line.strip().split(',')
                    atom_info_by_species[species].append((int(struct_idx), int(atom_idx)))

        print("All SOAP files found and loaded successfully.")
        return descriptors_by_species, atom_info_by_species

    def generate_atom_labels_and_cluster_counts(self,
        atom_clusters: Dict[str, Union[List[int], np.ndarray]],
        atom_structures: Dict[str, Union[List[Union[List[int], np.ndarray]], np.ndarray]]
    ) -> Tuple[List[np.ndarray], np.ndarray, List[str]]:
        """
        Generate atom labels for each structure, count clusters across structures, and create class labels.

        This function processes atomic clustering data and structural information to produce:
        1. A list of numpy arrays, each containing cluster labels for atoms in a structure.
        2. A matrix counting the number of atoms in each cluster for each structure.
        3. A list of class labels in the format "Element_ClusterNumber", including outliers.

        Parameters:
        atom_clusters (Dict[str, Union[List[int], np.ndarray]]): A dictionary where keys are element symbols
                                              and values are lists or arrays of cluster labels for each atom.
        atom_structures (Dict[str, Union[List[Union[List[int], np.ndarray]], np.ndarray]]): A dictionary where keys are element symbols
                                                      and values are either:
                                                      - A list of two arrays: [structure_ids, atom_ids]
                                                      - A 2D numpy array with columns [structure_id, atom_id]

        Returns:
        Tuple[List[np.ndarray], np.ndarray, List[str]]: 
            - A list of numpy arrays, each containing cluster labels for atoms in a structure.
            - A 2D numpy array where rows represent structures and columns represent clusters,
              with each cell containing the count of atoms in that cluster for that structure.
            - A list of class labels in the format "Element_ClusterNumber", including outliers.

        Note:
        - Clusters are treated independently for each species.
        - Outliers (cluster label -1) are treated as a separate class for each species.
        """
        # Determine the number of structures
        num_structures = max(
            np.max(structures[0] if isinstance(structures, list) else structures[:, 0])
            for structures in atom_structures.values()
        ) + 1

        # Count total clusters, create a mapping for cluster indices, and generate class labels
        total_clusters = 0
        cluster_mapping = {}
        class_labels = []
        for element, clusters in atom_clusters.items():
            unique_clusters = sorted(set(clusters))  # Include -1 in unique cluster count
            cluster_mapping[element] = {c: i + total_clusters for i, c in enumerate(unique_clusters)}
            class_labels.extend([f"{element}_{c}" if c != -1 else f"{element}_outlier" for c in unique_clusters])
            total_clusters += len(unique_clusters)

        # Initialize output structures
        structure_labels = [[] for _ in range(int(num_structures))]
        cluster_counts = np.zeros((int(num_structures), int(total_clusters)), dtype=int)

        # Process each element
        for element, clusters in atom_clusters.items():
            structures = atom_structures[element]
            element_mapping = cluster_mapping[element]

            if isinstance(structures, list):  # [structure_ids, atom_ids]
                struct_ids, atom_ids = structures
            else:  # 2D numpy array
                struct_ids, atom_ids = structures[:, 0], structures[:, 1]

            for struct_id, atom_id in zip(struct_ids, atom_ids):
                struct_id = int(struct_id)
                atom_id = int(atom_id)
                cluster = int(clusters[atom_id])

                # Map the cluster to its new index
                mapped_cluster = element_mapping[cluster]

                # Assign cluster label to the atom in its structure
                structure_labels[struct_id].append(mapped_cluster)

                # Update cluster count for this structure
                cluster_counts[struct_id, mapped_cluster] += 1

        # Convert structure_labels to numpy arrays
        structure_labels = [np.array(labels) for labels in structure_labels]

        return structure_labels, cluster_counts, class_labels

    def plot_species_clusters(self, class_labels, coefficients_cluster, uniqueAtomLabels, coefficients, output_file='./species_clusters.png'):

        directory = os.path.dirname(output_file)
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Crear un diccionario para agrupar los clusters por especie
        species_clusters = {species: [] for species in uniqueAtomLabels}
        for label, coef in zip(class_labels, coefficients_cluster):
            species = label.split('_')[0]
            species_clusters[species].append((label, coef))
        
        # Crear un gráfico para cada especie
        for i, species in enumerate(uniqueAtomLabels):
            plt.figure(figsize=(10, 6))
            
            # Línea horizontal para el coeficiente de la especie
            plt.axhline(y=coefficients[i], color='r', linestyle='-', label=f'{species} coefficient')
            
            # Puntos para cada cluster
            clusters = species_clusters[species]
            x = np.arange(len(clusters))
            y = [coef for _, coef in clusters]
            
            plt.scatter(x, y, color='b')
            
            # Añadir etiquetas para cada cluster
            for j, (label, coef) in enumerate(clusters):
                plt.annotate(label, (x[j], y[j]), xytext=(5, 5), textcoords='offset points')
            
            plt.title(f'Comparison of {species} coefficient with its clusters')
            plt.xlabel('Clusters')
            plt.ylabel('Coefficient value')
            plt.legend()
            plt.grid(True)
            
            # Ajustar los límites del eje y para que se vean bien todos los puntos
            plt.ylim(min(min(y), coefficients[i]) - 0.1, max(max(y), coefficients[i]) + 0.1)
            
            # Quitar las etiquetas del eje x
            plt.xticks([])
            
            plt.tight_layout()
            plt.savefig(f'{output_file}_{species}.png')
            plt.close()

    def handleABITAnalysis(self, values: Dict[str, Dict], file_location: str = None) -> None:
        """
        Handle Ab Initio Thermodynamics analysis based on specified values.

        Args:
            values (Dict[str, Dict]): Dictionary of analysis types and their parameters.
            file_location (str, optional): File location for output data.
        """
        print("Starting Ab Initio Thermodynamics analysis...")

        composition_data = self.get_composition_data()
        uniqueAtomLabels = composition_data['uniqueAtomLabels']
        compositions = composition_data['composition_data']
        energies = composition_data['energy_data']

        for abit, params in values.items():

            if abit.upper() == 'PHASE_DIAGRAM':
                print(f"Performing Phase Diagram analysis. Reference : {params.get('reference', ['GLOBAL'])[0].upper()},")

                if params.get('reference', ['GLOBAL'])[0].upper() == 'GLOBAL':

                    coefficients, predictions, residuals = self.linear_predict(
                              compositions, energies,
                              regularization = 1e-8, verbose = params.get('verbose', True), 
                              zero_intercept = True, force_negative = True)

                elif params.get('reference', ['GLOBAL'])[0].upper() == 'LOCAL':
                    if params.get('opt', True):
                        print("Optimizing k value for local linear regression...")
                        params['k'], initial_errors, refined_errors, coeffs = self.find_optimal_k(
                            composition_data=composition_data,
                            verbose=params.get('verbose', False)
                            )

                else:
                    diagram_data = self.get_diagram_data(
                        ID_reference=params.get('reference', [0]),
                        composition_data=composition_data['composition_data'],
                        energy_data=composition_data['energy_data'],
                        area_data=composition_data['area_data'],
                        especie=params.get('especie', None)
                    )

                    self.plot_phase_diagram(
                        diagram_data,
                        output_path=params.get('output_path', '.'),
                        save=True,
                        verbose=params.get('verbose', True),
                        mu_max=params.get('mu_max', 1),
                        mu_min=params.get('mu_min', 0)
                        )

            if abit.upper() == 'ENSEMBLE_ANALYSIS':
                pass 

            if abit.upper() == 'COMPOSITION_ANALYSIS':

                print("Performing COMPOSITION analysis...")

                print(" >< Generating correlation plot.")
                print(" >> Linear model.")
                coefficients, predictions, residuals = self.linear_predict(
                              compositions, energies,
                              regularization = 1e-5, verbose = params.get('verbose', True), 
                              zero_intercept = True, force_negative = False)    
                '''
                self.correlation_plot( np.concatenate((compositions, energies.reshape(-1, 1)), axis=1), feature_names=np.append(uniqueAtomLabels, 'E'), output_file='linear/correlation_plot.png' )           

                sensitivity_results = sensitivity_analysis(self.linear_predict, compositions, energies)
                plot_coefficients_distribution(sensitivity_results['coefficients'], 'Sensitivity Analysis', output_file='Sensitivity Analysis')

                cross_validation_results = cross_validation(self.linear_predict, compositions, energies)
                plot_coefficients_distribution(cross_validation_results['coefficients'], 'Cross-Validation Coefficients', output_file='Cross-Validation Coefficients')

                bootstrap_results = bootstrap_analysis(self.linear_predict, compositions, energies)
                plot_coefficients_distribution(bootstrap_results['coefficients'], 'Bootstrap Coefficients', output_file='Bootstrap Coefficients')
                
                regularization_results = regularization_analysis(self.linear_predict, compositions, energies)
                plot_regularization_path(regularization_results['coefficients'], regularization_results['reg_range'], output_file='regularization_results')

                multicollinearity_results = multicollinearity_analysis(compositions)
                plot_correlation_matrix(multicollinearity_results, output_file='multicollinearity_results')

                residuals_results = residuals_analysis(self.linear_predict, compositions, energies)
                plot_residuals(residuals_results['residuals'], output_file='residuals_results')
                '''
                # =========== =========== =========== =========== #
                print(" >< Making SOAP.")
                if params.get('cache', True):
                    soap_data = self.verify_and_load_soap()
                    if soap_data:
                        descriptors_by_species, atom_info_by_species = soap_data
                        print("Loaded existing SOAP data.")

                    else:
                        print("Some SOAP files are missing. Recalculating...")
                        r_cut, n_max, l_max, sigma = 5.0, 8, 6, 0.03
                        descriptors_by_species, atom_info_by_species = self.calculate_soap_descriptors(r_cut=r_cut, n_max=n_max, l_max=l_max, sigma=sigma)
                        self.save_descriptors(descriptors_by_species, atom_info_by_species, output_dir='SOAPs')
                else:
                    print("Cache disabled. Calculating SOAP descriptors...")
                    r_cut, n_max, l_max, sigma = 5.0, 8, 6, 0.03
                    descriptors_by_species, atom_info_by_species = self.calculate_soap_descriptors(r_cut=r_cut, n_max=n_max, l_max=l_max, sigma=sigma)
                    self.save_descriptors(descriptors_by_species, atom_info_by_species, output_dir='SOAPs')

                # =========== =========== =========== =========== #
                print(" >< Compress UMAP.")
                n_components = 10
                compressor = Compress(unique_labels=self.uniqueAtomLabels)
                compressed_data = compressor.verify_and_load_or_compress(descriptors_by_species, method='umap', n_components=n_components)

                # =========== =========== =========== =========== #
                print(" >< Cluster dbscan.")
                cluster_analysis_results = {}
                for species_idx, species in enumerate(self.uniqueAtomLabels):
                    analyzer = ClusteringAnalysis()
                    cluster_analysis_results[species] = analyzer.cluster_analysis(compressed_data[species], output_dir=f'./cluster_results/{species}', use_cache=True, methods=['dbscan'])
                    print( f' Especie: {species} dbscan clusters: { len(set(cluster_analysis_results[species]['dbscan']))}')

                print(" >< Linear model in cluster space.")
                structure_labels, cluster_counts, class_labels = self.generate_atom_labels_and_cluster_counts( 
                                        atom_clusters   = {key:cluster_analysis_results[key]['dbscan'] for key, item in cluster_analysis_results.items()},
                                        atom_structures = {key:np.array(atom_info_by_species[key]) for key, item in atom_info_by_species.items()},
                                      )

                coefficients_cluster, predictions_cluster, residuals_cluster = self.linear_predict(
                              cluster_counts, energies,
                              regularization = 1e-5, verbose = params.get('verbose', True), 
                              zero_intercept = True, force_negative = False)             

                sensitivity_results = sensitivity_analysis(self.linear_predict, cluster_counts, energies)
                plot_coefficients_distribution(sensitivity_results['coefficients'], 'Sensitivity Analysis', output_file='linear_cluster/lieSensitivity Analysis.png')

                cross_validation_results = cross_validation(self.linear_predict, cluster_counts, energies)
                plot_coefficients_distribution(cross_validation_results['coefficients'], 'Cross-Validation Coefficients', output_file='linear_cluster/Cross-Validation Coefficients.png')

                bootstrap_results = bootstrap_analysis(self.linear_predict, cluster_counts, energies)
                plot_coefficients_distribution(bootstrap_results['coefficients'], 'Bootstrap Coefficients', output_file='linear_cluster/Bootstrap Coefficients.png')
                
                regularization_results = regularization_analysis(self.linear_predict, cluster_counts, energies)
                plot_regularization_path(regularization_results['coefficients'], regularization_results['reg_range'], output_file='linear_cluster/regularization_results.png')

                multicollinearity_results = multicollinearity_analysis(cluster_counts)
                plot_correlation_matrix(multicollinearity_results, output_file='linear_cluster/multicollinearity_results.png')

                residuals_results = residuals_analysis(self.linear_predict, cluster_counts, energies)
                plot_residuals(residuals_results['residuals'], output_file='linear_cluster/residuals_results.png')

                self.plot_species_clusters(class_labels=class_labels, coefficients_cluster=coefficients_cluster[1:], 
                                        uniqueAtomLabels=self.uniqueAtomLabels, coefficients=coefficients[1:], 
                                        output_file='linear_cluster/species_clusters')

                # =========== =========== =========== =========== #
                print(" >< RBF interpretation.")
                

                print(" >< .")





            elif abit.upper() == 'LOCAL_LINEAR':
                print("Performing Local Linear Regression analysis...")

                if params.get('opt', True):
                    print("Optimizing k value for local linear regression...")
                    params['k'], initial_errors, refined_errors, coeffs = self.find_optimal_k(
                        composition_data=composition_data,
                        verbose=params.get('verbose', False)
                    )
                    self.plot_k_convergence(
                        initial_errors,
                        refined_errors,
                        coeffs=coeffs,
                        output_path=params.get('output_path', '.')
                    )

                errors, predicted_E, composition_data, coeffs = self.n_fold_cross_validation(
                    compositions=composition_data['composition_data'],
                    energies=composition_data['energy_data'],
                    k=params['k'],
                    output_path=params.get('output_path', '.'),
                    verbose=params.get('verbose', False)
                )
                
                if params.get('output_path', False):
                    self.plot_manifold(
                        features=composition_data,
                        response=errors,
                        output_path=params.get('output_path', '.'),
                        save=True,
                        verbose=params.get('verbose', True)
                    )

            elif abit.upper() == 'GLOBAL_LINEAR':
                print("Performing Global Linear Regression analysis...")
                composition_data = self.get_composition_data()
                composition, predicted_E, coeffs = self.global_linear_predict(
                    compositions=composition_data['composition_data'],
                    energies=composition_data['energy_data'],
                    regularization=params.get('regularization', 1e-8),
                    verbose=params.get('verbose', True),
                    center=params.get('center', True)
                )
                
                if params.get('output_path', False):
                    self.plot_manifold(
                        features=composition,
                        response=composition_data['energy_data'] - predicted_E,
                        output_path=params.get('output_path', '.'),
                        save=True,
                        verbose=params.get('verbose', True)
                    )
                
                print("Global Linear Regression analysis completed.")

            elif abit.upper() == 'CLUSTER_ANALYSIS':
                print("Performing Cluster Analysis...")
                n_clusters = params.get('n_clusters', 5)
                cluster_labels, cluster_centers = self.cluster_analysis(
                    features=compositions,
                    n_clusters=n_clusters,
                    output_path=params.get('output_path', '.'),
                    save=params.get('save', True),
                    verbose=params.get('verbose', True)
                )

            elif abit.upper() == 'COMPOSITION_ENERGY_CORRELATION':
                print("Analyzing Composition-Energy Correlation...")
                correlations = self.composition_energy_correlation(
                    compositions=compositions,
                    energies=energies,
                    output_path=params.get('output_path', '.'),
                    save=params.get('save', True),
                    verbose=params.get('verbose', True)
                )

            elif abit.upper() == 'ENERGY_LANDSCAPE':
                print("Analyzing Energy Landscape...")
                self.energy_landscape_analysis(
                    compositions=compositions,
                    energies=energies,
                    output_path=params.get('output_path', '.'),
                    save=params.get('save', True),
                    verbose=params.get('verbose', True)
                )

            elif abit.upper() == 'THERMODYNAMIC_STABILITY':
                print("Predicting Thermodynamic Stability...")
                temperatures = params.get('temperatures', np.linspace(300, 1500, 50))
                stable_compositions = self.thermodynamic_stability_prediction(
                    compositions=compositions,
                    energies=energies,
                    temperatures=temperatures,
                    output_path=params.get('output_path', '.'),
                    save=params.get('save', True),
                    verbose=params.get('verbose', True)
                )

            elif abit.upper() == 'ENSEMBLE_ANALYSIS':
                print("Performing Ensemble Analysis...")
                ensemble_type = params.get('ensemble', 'canonical')
                temperatures = params.get('temperatures', np.linspace(100, 1000, 100))
                volumes = params.get('volumes', np.ones_like(energies))  # Assuming unit volume if not provided
                particles = params.get('particles', np.arange(1, len(energies) + 1))
                mass = params.get('mass', 1.0)

                ensemble_properties = self.calculate_ensemble_properties(
                    volumes=volumes,
                    temperatures=temperatures,
                    particles=particles,
                    ensemble=ensemble_type,
                    mass=mass,
                    output_path=params.get('output_path', '.'),
                    save=params.get('save', True),
                    verbose=params.get('verbose', True)
                )

        print("Ab Initio Thermodynamics analysis completed.")




