import numpy as np

# Create a random vector of size 20 with float values in the range 1-20
random_vector = np.random.uniform(1, 20, 20)

# Reshape the array to 4 by 5
reshaped_vector = random_vector.reshape(4, 5)

# Identify the maximum values along each row
maximum_values = np.max(reshaped_vector, axis=1, keepdims=True)

# Replace the maximum values with 0
reshaped_vector[reshaped_vector == maximum_values] = 0

print("Original random vector:")
print(random_vector)
print("\nReshaped array with max values replaced by 0:")
print(reshaped_vector)