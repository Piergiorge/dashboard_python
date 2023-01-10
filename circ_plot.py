import matplotlib.pyplot as plt
import numpy as np

# Set the radius of the circle
radius = 1.0

# Set the number of points to use for the circle
num_points = 100

# Generate the x and y coordinates of the points on the circle
theta = np.linspace(0, 2*np.pi, num_points, endpoint=False)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# Create a figure and a subplot
fig, ax = plt.subplots()

# Plot the circle
ax.plot(x, y, color="k")

# Add ticks and labels
ax.set_xticks(np.linspace(-radius, radius, 5))
ax.set_yticks(np.linspace(-radius, radius, 5))
ax.set_xticklabels([])
ax.set_yticklabels([])

# Show the plot
plt.show()
