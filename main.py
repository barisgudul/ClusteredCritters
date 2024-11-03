# Import necessary libraries for data manipulation and visualization
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load and clean the dataset
# -----------------------------------
# Load the dataset from a CSV file called "msleep.csv"
# Drop any rows containing missing values to ensure consistency in analysis
dataset = pd.read_csv("msleep.csv")
dataset = dataset.dropna()

# Step 2: Select specific columns for clustering
# ----------------------------------------------
# Choose key attributes: 'sleep_total', 'brainwt', and 'bodywt' for clustering analysis
# Extract animal names for labeling the clusters in the visualization
clustering_data = dataset[["sleep_total", "brainwt", "bodywt"]]
animal_names = dataset["name"].tolist()

# Define the labels for the columns to make the visualization more readable
column_labels = ['Total Sleep (hours)', 'Brain Weight (kg)', 'Body Weight (kg)']

# Step 3: Normalize the data
# --------------------------
# Use StandardScaler to standardize the data to have a mean of 0 and standard deviation of 1
# This normalization step is essential for clustering algorithms to treat each feature equally
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
clustering_data = scaler.fit_transform(clustering_data)

# Step 4: Perform hierarchical clustering
# ---------------------------------------
# Generate a linkage matrix using Ward's method, which minimizes the variance of clusters being merged
# This linkage matrix will be used to determine cluster relationships for visualization
from scipy.cluster.hierarchy import linkage
linkage_matrix = linkage(clustering_data, method="ward")

# Step 5: Visualize the clusters with a clustermap
# ------------------------------------------------
# Create a cluster map to visually represent the grouping of animals based on sleep and body attributes
# Use the linkage matrix to display relationships between data points (animal species)
# Set color map to "Spectral" for a visually distinct palette
plt.figure(figsize=(15, 8))  # Set the size of the plot
sns.clustermap(
    clustering_data,
    row_linkage=linkage_matrix,  # Use linkage matrix for row clustering
    col_cluster=False,  # Disable column clustering (only rows are clustered)
    cmap="Spectral",  # Color map for visual distinction
    yticklabels=animal_names,  # Label rows with animal names
    xticklabels=column_labels  # Label columns with descriptive names
)

# Add a title to the plot for context
plt.title("Cluster Map of Animal Groups")

# Display the plot
plt.show()
