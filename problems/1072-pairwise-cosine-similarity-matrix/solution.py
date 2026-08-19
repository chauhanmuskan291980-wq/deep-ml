import numpy as np

def pairwise_cosine_similarity(X):
    X = np.array(X,dtype=float)

    # Calculate L2 norm of each row 
    norms = np.linalg.norm(X,axis=1)

    # Dot product between every pair of rows
    dot_products = X @ X.T

    # Avoid division by zero 
    denominator = np.outer(norms,norms)

    # Initialize similaroty matrix with zeros
    S = np.zeros_like(dot_products)

    # Calculate consine similarity only where denomonator is not zerp 
    np.divide(dot_products, denominator,out=S,where = denominator!=0)


    # Round to 4 decimal places

    return np.round(S,4).tolist()