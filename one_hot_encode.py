import numpy as np

def one_hot_encode(labels: List[int]) -> np.ndarray:
    '''
    Parameters: 
    labels (list of int): List of integer labels to be encoded

    Returns:
    numpy.ndarray: A 2D array where each row is the one-hot vector
    '''
    one_hot = np.zeros(len(labels), len(set(labels)))

    label_to_index ={label: index for index, label in enumerate(labels)}

    for i, label in enumerate(labels):
        one_hot[idx, label_to_index[label] = 1
    
    return one_hot

# Example usage:
labels = [0, 2, 1, 3]
encoded_labels = one_hot_encode(labels)
print(encoded_labels)    
