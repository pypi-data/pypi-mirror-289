import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd
import seaborn as sns
from scipy.cluster.vq import kmeans
import numpy as np
import os

def extract_dominant_colors(image_path, max_clusters=10, save_plots=False):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Error: The image file '{image_path}' does not exist.")
    
    image = img.imread(image_path)
    if image is None:
        raise ValueError("Error: Failed to load image.")
    
    r, g, b = [], [], []
    for row in image:
        for pixel in row:
            if len(pixel) == 4:
                temp_r, temp_g, temp_b, _ = pixel
            else:
                temp_r, temp_g, temp_b = pixel
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
    
    df = pd.DataFrame({'red': r, 'green': g, 'blue': b})
    data = df[['red', 'green', 'blue']].astype(np.float32)
    
    distortions = []
    num_clusters_range = range(1, max_clusters + 1)
    for i in num_clusters_range:
        cluster_centers, distortion = kmeans(data, i)
        distortions.append(distortion)
    
    if save_plots:
        elbow_plot = pd.DataFrame({'num_clusters': num_clusters_range, 'distortions': distortions})
        plt.figure(figsize=(10, 5))
        sns.lineplot(x='num_clusters', y='distortions', data=elbow_plot)
        plt.xticks(num_clusters_range)
        plt.xlabel('Number of Clusters')
        plt.ylabel('Distortion')
        plt.title('Elbow Plot for Optimal Number of Clusters')
        plt.savefig('elbow_plot.png')
        plt.close()
    
    optimal_clusters = int(input("Enter the optimal number of clusters based on the elbow plot: ")) if not save_plots else 3
    
    cluster_centers, _ = kmeans(data, optimal_clusters)
    colors = np.clip(cluster_centers, 0, 1)
    
    if save_plots:
        plt.figure(figsize=(8, 2))
        plt.imshow([colors])
        plt.axis('off')
        plt.title(f'Dominant Colors (Total: {optimal_clusters})')
        plt.savefig('dominant_colors.png')
        plt.close()
    
    return colors
import matplotlib.pyplot as plt
import matplotlib.image as img
import pandas as pd
import seaborn as sns
from scipy.cluster.vq import kmeans
import numpy as np
import os

def extract_dominant_colors(image_path, max_clusters=10, save_plots=False):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"Error: The image file '{image_path}' does not exist.")
    
    image = img.imread(image_path)
    if image is None:
        raise ValueError("Error: Failed to load image.")
    
    r, g, b = [], [], []
    for row in image:
        for pixel in row:
            if len(pixel) == 4:
                temp_r, temp_g, temp_b, _ = pixel
            else:
                temp_r, temp_g, temp_b = pixel
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
    
    df = pd.DataFrame({'red': r, 'green': g, 'blue': b})
    data = df[['red', 'green', 'blue']].astype(np.float32)
    
    distortions = []
    num_clusters_range = range(1, max_clusters + 1)
    for i in num_clusters_range:
        cluster_centers, distortion = kmeans(data, i)
        distortions.append(distortion)
    
    if save_plots:
        elbow_plot = pd.DataFrame({'num_clusters': num_clusters_range, 'distortions': distortions})
        plt.figure(figsize=(10, 5))
        sns.lineplot(x='num_clusters', y='distortions', data=elbow_plot)
        plt.xticks(num_clusters_range)
        plt.xlabel('Number of Clusters')
        plt.ylabel('Distortion')
        plt.title('Elbow Plot for Optimal Number of Clusters')
        plt.savefig('elbow_plot.png')
        plt.close()
    
    optimal_clusters = int(input("Enter the optimal number of clusters based on the elbow plot: ")) if not save_plots else 3
    
    cluster_centers, _ = kmeans(data, optimal_clusters)
    colors = np.clip(cluster_centers, 0, 1)
    
    if save_plots:
        plt.figure(figsize=(8, 2))
        plt.imshow([colors])
        plt.axis('off')
        plt.title(f'Dominant Colors (Total: {optimal_clusters})')
        plt.savefig('dominant_colors.png')
        plt.close()
    
    return colors

