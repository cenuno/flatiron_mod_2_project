import numpy as np

np.random.seed(2019)

pizza_slices = np.array([1, 32, 45, 65, 90, 87, 2, 3, 4, 55, 99])

# every time I run this script, I have a value of 4 in the rand_int object
random_int = np.random.choice(pizza_slices, size=1)
random_int = int(random_int)
print(
    f"""
    I know a random stranger who ate {random_int} slices of pizza in an hour!
    """
)
