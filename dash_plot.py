import matplotlib.pyplot as plt
import numpy as np

# Prepare the data
x = np.array([1, 2, 3, 4, 5])
y = x ** 2

# Create the line chart
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Line Chart')

# Create the bar chart
plt.bar(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Chart')

# Display the plots
plt.show()
