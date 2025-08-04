import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_netflix(num_clusters):
    # Load dataset
    df = pd.read_csv('data/netflix_titles.csv')
    df = df.dropna(subset=['description'])

    # TF-IDF Vectorization of descriptions
    tfidf = TfidfVectorizer(stop_words='english', max_features=1000)
    tfidf_matrix = tfidf.fit_transform(df['description'])

    # KMeans Clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(tfidf_matrix)

    # Get TF-IDF terms
    terms = tfidf.get_feature_names_out()

    # HTML result string
    result_html = ""

    for i in range(num_clusters):
        # Boolean mask for the current cluster
        cluster_mask = df['cluster'] == i

        # Convert boolean Series to row indices
        row_indices = np.where(cluster_mask.to_numpy())[0]

        # Extract TF-IDF rows for the cluster
        cluster_data = tfidf_matrix[row_indices]

        if cluster_data.shape[0] > 0:
            # Mean TF-IDF for terms in this cluster
            avg_tfidf = np.asarray(cluster_data.mean(axis=0)).flatten()
            top_indices = avg_tfidf.argsort()[-5:][::-1]
            top_keywords = [terms[index] for index in top_indices]
        else:
            top_keywords = ["No keywords found"]

        # Get example titles
        sample_titles = df[cluster_mask]['title'].head(5).tolist()

        # Add to HTML
        result_html += f"<h3>Cluster {i+1}: {' | '.join(top_keywords)}</h3><ul>"
        for title in sample_titles:
            result_html += f"<li>{title}</li>"
        result_html += "</ul>"

    return result_html
