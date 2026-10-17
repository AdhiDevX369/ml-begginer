<div align="center">

![Machine Learning Curriculum Banner](assets/banner.jpg)

# 🧠 Machine Learning for Beginners
### *A 15-Week Practical & Mathematical Curriculum*
**Machine Learning from Scratch with Practical Mathematics**

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Notebooks-Jupyter%20%2F%20Colab-orange.svg?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Deployment-Streamlit-FF4B4B.svg?logo=streamlit&logoColor=white)](https://streamlit.io/)

</div>

---

## 📌 1. Course Overview

* **Course Title:** Machine Learning from Scratch with Practical Mathematics
* **Level:** Beginner to Intermediate
* **Duration:** 15 Weeks (1 session per week, 2 hours per session = 30 total contact hours)
* **Delivery Mode:** Interactive lectures, mathematical derivations, and hands-on coding labs
* **Core Stack & Environment:** Python, NumPy, Pandas, Matplotlib, Seaborn, Scikit-Learn, Google Colab, Streamlit
* **Prerequisites:** Basic Python programming syntax (variables, functions, loops) and standard high school algebra

---

## 📊 2. Assessment & Grading Structure

| Component | Weight | Description |
| :--- | :---: | :--- |
| **Weekly Coding Tasks & Quizzes** | **40%** | 10 short assignments reinforcing practical lab concepts and mathematical foundations |
| **Mid-Course Project** | **20%** | Conducted at Week 7, covering end-to-end regression or classification pipelines |
| **Final Capstone Project** | **40%** | Complete end-to-end ML system with data pipeline, model training, and web deployment |

---

## 📂 Repository Structure

```plaintext
ML-2/
├── assets/
│   └── banner.jpg                     # Course banner image
├── week1/
│   └── Week_01_Foundations_of_Machine_Learning.ipynb
├── week2/
│   └── Week_02_Linear_Algebra_for_Machine_Learning.ipynb
├── environment.yml                    # Conda environment (recommended)
├── requirements.txt                   # pip / venv / uv alternative
├── .gitignore                         # Python, Jupyter, Conda, and dataset ignores
└── README.md                          # Course overview and syllabus
```

---

## 🗺️ 3. Weekly Syllabus & Module Breakdown

```mermaid
flowchart LR
    A["Phase 1: Foundations & Math (W1-4)"] --> B["Phase 2: Regression (W5-6)"]
    B --> C["Phase 3: Classification (W7-9)"]
    C --> D["Phase 4: Unsupervised Learning (W10-12)"]
    D --> E["Phase 5: Pipelines & Deployment (W13-15)"]
```

---

### 🔹 Phase 1: Foundations & Mathematics for ML (Weeks 1 to 4)

#### [Week 01: Machine Learning Foundations — The Big Picture](week1/Week_01_Foundations_of_Machine_Learning.ipynb)
*Expanded Ethics & Data Security Edition · zero heavy math*
* **Course & Mindset:**
  * ML Engineer (the engine builder) vs. AI Engineer (the complete vehicle)
  * 3-month roadmap: Data & Python → ML Engineering → DL & Live AI App (Capstone)
* **Conceptual Foundations:**
  * How AI, ML, DL and Data Science fit together
  * The Paradigm Shift: Traditional Programming (*Data + Rules = Answers*) vs. Machine Learning (*Data + Answers = Rules*)
  * The 3 pillars: Supervised (Regression vs. Classification), Unsupervised (Clustering), Reinforcement Learning
* **The 6-Step ML Lifecycle:**
  * Problem framing (business goal → target $y$ → task type), 4 reasons to use ML, and when **not** to use ML
  * Data collection sources (internal, public, APIs & sensors)
  * **Data privacy & ethics:** PII masking, Sri Lanka PDPA & GDPR, algorithmic bias, allowed vs. forbidden data
  * EDA basics (missing values, outliers), training (guess → loss → adjust), evaluation (80/20 split, overfitting), deployment (`model.pkl` + Streamlit/FastAPI)
* **Data Basics:**
  * Features ($\mathbf{X}$) vs. Target ($\mathbf{y}$); structured vs. unstructured data
* **Hands-on Lab:**
  * Environment setup & verification (Colab / Conda / venv)
  * Rule-based vs. ML spam filter, regression, classification, K-Means and a trial-and-error RL agent
  * PII pseudonymization with salted SHA-256 hashing and dropping sensitive columns
  * Cleaning NaNs and outliers, an overfitting demo, saving/loading a model with `joblib`
  * **Bonus appendix:** NumPy tensors, slicing, reshaping, and vectorization benchmark

#### [Week 02: Linear Algebra for Machine Learning](week2/Week_02_Linear_Algebra_for_Machine_Learning.ipynb)
* **Conceptual Foundations:**
  * Feature spaces and geometric interpretation of data vectors
  * Linear transformations and projections
* **Mathematical Foundations:**
  * Vector addition, scalar multiplication, and geometric angles
  * Vector Dot Product and inner products: algebraic calculation and cosine similarity
  * Matrix multiplication (compatibility rules, dimensional analysis, and intuition)
  * Identity matrix, matrix inverse, and singularity
  * Vector Norms: $L_1$ Norm (Manhattan distance) and $L_2$ Norm (Euclidean distance / magnitude)
* **Hands-on Lab:**
  * Vectorized dot products, matrix multiplications, and transpositions with NumPy (`np.dot`, `@` operator)
  * Implementing Euclidean and Manhattan distance metrics from scratch
  * Numerical image representations as pixel matrices and basic manipulations

#### Week 03: Calculus & Optimization (Gradient Descent)
* **Conceptual Foundations:**
  * How machines learn: Objective functions, Loss functions, and Empirical Risk Minimization
  * Optimization landscape: Convex vs. non-convex optimization, local vs. global minima
* **Mathematical Foundations:**
  * Limits, rates of change, and derivatives
  * Geometric intuition of tangent lines and slopes
  * Partial derivatives and the gradient vector ($\nabla L$)
  * The Gradient Descent update rule: $\mathbf{w} := \mathbf{w} - \alpha \nabla L(\mathbf{w})$
  * Hyperparameter impact of learning rate $\alpha$ (overshooting, oscillations, slow convergence)
* **Hands-on Lab:**
  * Implementing numerical derivatives in Python
  * Coding a 1D Gradient Descent optimization algorithm from scratch
  * Visualizing convergence trajectories on loss surfaces using Matplotlib

#### Week 04: Probability & Statistics for Data Science
* **Conceptual Foundations:**
  * Managing uncertainty and variability in real-world data
  * Population parameters vs. sample statistics
* **Mathematical Foundations:**
  * Measures of Central Tendency: Mean, Median, Mode
  * Measures of Dispersion: Variance, Standard Deviation, Interquartile Range (IQR)
  * Probability distributions: Normal (Gaussian) distribution, 68-95-99.7 empirical rule, Z-scores
  * Covariance, Pearson Correlation Coefficient, and Correlation vs. Causation
  * Introduction to Conditional Probability and Bayes' Theorem
* **Hands-on Lab:**
  * Exploratory Data Analysis (EDA) using Pandas (`.describe()`, `.corr()`)
  * Visualizing statistical distributions with Seaborn (Histograms, KDE plots, Box plots, Heatmaps)

---

### 🔹 Phase 2: Supervised Learning - Regression (Weeks 5 to 6)

#### Week 05: Simple & Multiple Linear Regression
* **Conceptual Foundations:**
  * Modeling continuous dependent variables
  * Ordinary Least Squares (OLS) assumptions (linearity, homoscedasticity, independence, normality)
* **Mathematical Foundations:**
  * Simple Linear model: $\hat{y} = w_1 x + w_0$
  * Multiple Linear model: $\hat{y} = \mathbf{w}^T \mathbf{x} + b$
  * Cost Functions: Mean Squared Error (MSE) and Root Mean Squared Error (RMSE)
  * Analytical Closed-Form Solution (The Normal Equation): $\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$
  * Trade-offs: Analytical solution vs. Gradient Descent optimization
* **Hands-on Lab:**
  * Implementing Simple Linear Regression from scratch with the Normal Equation
  * Building a Multiple Linear Regression model with Scikit-Learn (`LinearRegression`)
  * Interpreting model coefficients, intercept, and $R^2$ score

#### Week 06: Generalization, Bias-Variance Tradeoff & Regularization
* **Conceptual Foundations:**
  * Underfitting (high bias) vs. Overfitting (high variance)
  * The Generalization Gap and Train/Test split methodology
* **Mathematical Foundations:**
  * Error decomposition: $\text{Error} = \text{Bias}^2 + \text{Variance} + \text{Irreducible Noise}$
  * Complexity penalties in cost functions
  * $L_2$ Regularization (Ridge Regression): $\mathcal{L}_{\text{Ridge}} = \text{MSE} + \lambda \sum w_j^2$
  * $L_1$ Regularization (Lasso Regression): $\mathcal{L}_{\text{Lasso}} = \text{MSE} + \lambda \sum |w_j|$
  * Geometric intuition: Why Lasso drives weights to zero (automatic feature selection)
* **Hands-on Lab:**
  * Dataset partitioning via `train_test_split`
  * Demonstrating polynomial regression overfitting
  * Implementing Ridge and Lasso regularization with Scikit-Learn

---

### 🔹 Phase 3: Supervised Learning - Classification (Weeks 7 to 9)

#### Week 07: Logistic Regression & Classification Evaluation
* **Conceptual Foundations:**
  * Binary classification problems and decision boundaries
  * Why Linear Regression fails for categorical outcomes
* **Mathematical Foundations:**
  * The Sigmoid (Logistic) activation function: $\sigma(z) = \frac{1}{1 + e^{-z}}$
  * Converting linear combinations to probabilities: $P(y=1|\mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x} + b)$
  * Odds ratio and log-odds (logit transformation)
  * Binary Cross-Entropy Loss (Log Loss): $-\frac{1}{m} \sum [y \log(\hat{y}) + (1-y) \log(1-\hat{y})]$
* **Hands-on Lab:**
  * Training a Logistic Regression model for medical diagnosis (e.g., Diabetes prediction)
  * Confusion Matrix breakdown: TP, FP, TN, FN
  * Evaluating Accuracy, Precision, Recall, and $F_1$-Score
  * Plotting ROC curves, AUC, and Precision-Recall Curves

#### Week 08: Tree-Based Models & Ensemble Learning
* **Conceptual Foundations:**
  * Non-parametric learning and recursive binary splitting
  * Ensemble learning: Wisdom of crowds and variance reduction via bagging
* **Mathematical Foundations:**
  * Information Theory: Shannon Entropy $H(S) = -\sum p_i \log_2(p_i)$
  * Information Gain $= \text{Entropy}(\text{Parent}) - \sum \frac{|S_v|}{|S|} \text{Entropy}(S_v)$
  * Gini Impurity $= 1 - \sum p_i^2$
  * Bootstrap Aggregation (Bagging) mathematics and Random Forest variance reduction
* **Hands-on Lab:**
  * Training `DecisionTreeClassifier` and rendering decision tree diagrams
  * Hyperparameter tuning (`max_depth`, `min_samples_split`)
  * Training `RandomForestClassifier` and plotting Feature Importance rankings

#### Week 09: Distance-Based Classifiers (KNN & Support Vector Machines)
* **Conceptual Foundations:**
  * Instance-based / lazy learning vs. eager parametric models
  * Maximum Margin Classifiers and robust decision boundaries
* **Mathematical Foundations:**
  * K-Nearest Neighbors (KNN): Distance metric selection, choice of $k$, majority voting
  * Support Vector Machines (SVM): Hyperplane equation $\mathbf{w}^T \mathbf{x} + b = 0$, margin calculation $\frac{2}{\|\mathbf{w}\|}$
  * Hard-margin vs. Soft-margin SVM (Slack variables $\xi_i$ and the $C$ penalty parameter)
  * Non-linear separation and the Kernel Trick (Polynomial and RBF kernels)
* **Hands-on Lab:**
  * Implementing KNN with Scikit-Learn and analyzing feature scaling sensitivity
  * Training Linear and RBF Support Vector Classifiers (`SVC`)
  * Comparing 2D decision boundary geometries (KNN vs. Decision Trees vs. SVMs)

---

### 🔹 Phase 4: Unsupervised Learning & Feature Engineering (Weeks 10 to 12)

#### Week 10: Clustering Algorithms & Pattern Discovery
* **Conceptual Foundations:**
  * Unsupervised discovery of clusters without labeled ground truth
  * Industry use cases: Customer segmentation, behavioral cohorting, anomaly detection
* **Mathematical Foundations:**
  * K-Means objective: Minimizing Within-Cluster Sum of Squares (WCSS / Inertia)
  * K-Means convergence algorithm: Assignment step and Centroid update step
  * Determining optimal cluster count: The Elbow Method and Silhouette Score
* **Hands-on Lab:**
  * Implementing K-Means clustering on customer shopping behavioral datasets
  * Plotting inertia curves to evaluate optimal $k$
  * Visualizing cluster assignments and centroids in 2D space

#### Week 11: Dimensionality Reduction (PCA)
* **Conceptual Foundations:**
  * The Curse of Dimensionality: Distance sparsity in high dimensions
  * Feature selection vs. Feature extraction
* **Mathematical Foundations:**
  * Data centering and Sample Covariance Matrix calculation
  * Eigenvalues and Eigenvectors: Geometric interpretation of variance axes
  * Principal Components: Orthogonal projections that maximize preserved variance
  * Explained Variance Ratio calculation
* **Hands-on Lab:**
  * Computing PCA mathematically from scratch with NumPy (`np.cov`, `np.linalg.eig`)
  * Applying Scikit-Learn `PCA` to high-dimensional datasets (30+ features)
  * Projecting data onto 2 components for visual exploration

#### Week 12: Rigorous Validation & Hyperparameter Optimization
* **Conceptual Foundations:**
  * Data leakage prevention and honest model evaluation
  * Hyperparameters (external settings) vs. Model Parameters (learned weights)
* **Mathematical Foundations:**
  * K-Fold Cross-Validation mechanics and estimator variance
  * Stratified K-Fold for imbalanced class distributions
  * Search spaces: Grid Search exhaustive evaluation vs. Random Search probabilistic sampling
* **Hands-on Lab:**
  * Evaluating models using `cross_val_score`
  * Fine-tuning Random Forest and SVM hyperparameters via `GridSearchCV` and `RandomizedSearchCV`
  * Serializing and saving trained models using `joblib` / `pickle`

---

### 🔹 Phase 5: Production Pipelines & Deep Learning Introduction (Weeks 13 to 15)

#### Week 13: Feature Engineering, Preprocessing & Scikit-Learn Pipelines
* **Conceptual Foundations:**
  * Handling real-world messy data: Missingness, categorical variables, differing scales
  * Designing modular, production-grade transformation pipelines
* **Mathematical Foundations:**
  * Feature Scaling: Standardization ($z = \frac{x - \mu}{\sigma}$) vs. Min-Max Normalization ($x' = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$)
  * Categorical encodings: One-Hot Encoding vs. Ordinal/Integer Encoding
  * Imputation mechanics: Mean, Median, Mode, and KNN imputation
* **Hands-on Lab:**
  * Building `ColumnTransformer` pipelines for heterogeneous data types
  * Chaining transformers and estimators inside Scikit-Learn `Pipeline`
  * Demonstrating strict isolation: `fit_transform` on train, `transform` on test to prevent data leakage

#### Week 14: Introduction to Deep Learning & Artificial Neural Networks
* **Conceptual Foundations:**
  * The paradigm transition from classical ML to Deep Learning
  * Biological vs. Artificial Neurons
  * Multilayer Perceptron (MLP) architecture: Input, Hidden, and Output layers
* **Mathematical Foundations:**
  * Single artificial neuron equation: $z = \sum w_i x_i + b, \quad a = f(z)$
  * Non-linear activation functions: Sigmoid, ReLU, Tanh, Softmax
  * Forward Propagation matrix equations
  * Intuition of Backpropagation and the Calculus Chain Rule
* **Hands-on Lab:**
  * Training a Multilayer Perceptron with Scikit-Learn (`MLPClassifier`)
  * Handwritten digit classification on the MNIST dataset
  * Analyzing loss curves and convergence rates across epochs

#### Week 15: Capstone Project Showcase & Deployment
* **Capstone Project Objectives:**
  * Integrating all 14 weeks of knowledge into a complete end-to-end data application
* **Execution Steps:**
  1. Problem formulation and dataset curation (e.g., Credit Default, Customer Churn, Real Estate Valuation)
  2. Exploratory Data Analysis, outlier detection, and data cleaning
  3. Preprocessing pipeline implementation with `ColumnTransformer`
  4. Training, tuning, and benchmark comparison of multiple candidate algorithms
  5. Model selection via cross-validated evaluation metrics
  6. Exporting the finalized pipeline artifact
  7. Creating a real-time web application interface with **Streamlit**
* **Course Wrap-Up & Industry Roadmaps:**
  * Next steps: Transitioning to PyTorch and TensorFlow
  * Introduction to MLOps, Model Monitoring, and cloud deployment (Hugging Face Spaces, Docker, AWS)
  * Building your Kaggle and GitHub data science portfolio

---

## ⚡ Quickstart & Environment Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd ML-2
```

### 2. Set Up Your Environment (pick ONE option)

#### Option A — Conda (recommended)
1. Install **Miniconda** from the [official download page](https://www.anaconda.com/download/success) (scroll to *Miniconda Installers*). Direct installers:
   [macOS Apple Silicon](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh) ·
   [macOS Intel](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh) ·
   [Windows](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe) ·
   [Linux](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
   > 💡 Prefer a fully open-source setup (or installing on a company machine)? Use **[Miniforge](https://github.com/conda-forge/miniforge)** instead. Every command below works the same.
2. Create and activate the course environment:
```bash
conda env create -f environment.yml
conda activate ml-course
python -m ipykernel install --user --name ml-course --display-name "Python (ml-course)"
```
Update later with `conda env update -f environment.yml --prune`.

#### Option B — venv (no Conda)
Use **Python 3.10 – 3.12** ([python.org](https://www.python.org/downloads/) or `brew install python@3.12`). Newer versions may not have wheels for every ML library yet.
```bash
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
python -m ipykernel install --user --name ml-course-venv --display-name "Python (ml-course venv)"
```

#### Option C — uv (fast venv alternative)
```bash
uv venv --python 3.12 && source .venv/bin/activate
uv pip install -r requirements.txt
```
Install uv from [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/).

#### Option D — Google Colab (zero install)
Open any notebook at [colab.research.google.com](https://colab.research.google.com) using **File → Open notebook → GitHub**, or click the *Open in Colab* badge at the top of each notebook.

#### Recommended tools
| Tool | Why |
| :--- | :--- |
| [VS Code](https://code.visualstudio.com/) + *Python* & *Jupyter* extensions | Run notebooks locally and select the `ml-course` kernel |
| [Git](https://git-scm.com/downloads) | Version control for your assignments |
| [Kaggle](https://www.kaggle.com) / [Hugging Face](https://huggingface.co/datasets) / [UCI](https://archive.ics.uci.edu) | Public datasets |

### 3. Launch Jupyter Lab
```bash
jupyter lab
```
Open `week1/Week_01_Foundations_of_Machine_Learning.ipynb` and run **Cell 0** to verify your setup. If it prints `Hello ML!`, you're ready.

---

<div align="center">
  <sub>Designed for aspiring Data Scientists & Machine Learning Engineers. Happy Learning!</sub>
</div>
