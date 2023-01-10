import matplotlib.pyplot as plt
import numpy as np

# Generate some random data
data = np.random.rand(10, 10)

# Create a figure and a subplot
fig, ax = plt.subplots()

# Create the heat map
im = ax.imshow(data, cmap="YlGnBu")

# Add a colorbar
fig.colorbar(im)

# Show the plot
plt.show()
