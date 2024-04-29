import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Sample hog features (replace with your actual data)
# Assuming you have two separate numpy arrays for sad and neutral features
# where each row represents a data point and each column represents a hog feature
sad_features = np.random.rand(100, 128)  # 100 data points, 128 features
# Just an example, replace with actual data
neutral_features = 2 * sad_features + 0.5

# Combine sad and neutral features
all_features = np.vstack((sad_features, neutral_features))

# Create PCA object (adjust n_components as needed)
pca = PCA(n_components=2)  # Reduce to 2 dimensions for visualization

# Apply PCA transformation
pca_data = pca.fit_transform(all_features)

# Separate transformed features for sad and neutral emotions
pca_sad_features = pca_data[:100, :]  # Assuming first 100 rows are sad
pca_neutral_features = pca_data[100:, :]

# # Plot the transformed data
plt.scatter(pca_sad_features[:, 0],
            pca_sad_features[:, 1], label='Sad', c='red')
plt.scatter(pca_neutral_features[:, 0],
            pca_neutral_features[:, 1], label='Neutral', c='blue')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Visualization of Hog Features (Sad vs Neutral)')
plt.legend()
plt.show()
