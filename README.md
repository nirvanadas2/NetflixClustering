# 🎬 Netflix Show Clustering using K-Means

This project applies unsupervised learning to cluster Netflix shows based on their **genre**, **rating**, and **duration** using the **K-Means algorithm**. It helps uncover natural groupings of content, which could be useful for recommendation engines or catalog organization.

---

## 📊 Project Overview

We use:
- `listed_in` (genre)
- `rating` (e.g., TV-14, PG)
- `duration` (e.g., 90 min)

to group similar Netflix titles into **5 clusters** using **K-Means**.

---

## 📁 Folder Structure

netflix-clustering/
├── data/
│ └── netflix_titles.csv # Netflix dataset from Kaggle
├── src/
│ └── cluster_netflix.py # Main script for clustering
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## 🧰 Technologies Used

- Python 3
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn

---

## 📦 How to Run This Project

### 1️⃣ Clone or Download

```bash
git clone <your-repo-link>
cd netflix-clustering
