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

np.random.seed(2019)
output_1 = []
for num in range(10):
    output_1.append(int(np.random.choice(pizza_slices, size=1)))
print(output_1)

np.random.seed(2019)
output_2 = []
for num in range(10):
    output_2.append(int(np.random.choice(pizza_slices, size=1)))
print(output_2)

print(f"Are output 1 and output 2 the same? {output_1 == output_2}")

from random import randint
np.random.seed(2019)
print(randint(0, 10))
print(randint(0, 10))