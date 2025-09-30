import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Dot grid
x = np.arange(-4, 5, 1)
y = np.arange(-4, 5, 1)
X, Y = np.meshgrid(x, y)

plt.figure(figsize=(6,6))
sns.scatterplot(x=X.flatten(), y=Y.flatten(), s=80, color="black")

# Add a flower-like loop around
theta = np.linspace(0, 2*np.pi, 500)
r = 4 * np.sin(6*theta)
plt.plot(r*np.cos(theta), r*np.sin(theta), color="red")

plt.gca().set_aspect('equal')
plt.axis("off")
plt.show()