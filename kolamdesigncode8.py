import numpy as np
import matplotlib.pyplot as plt

def draw_circle(ax, radius, **kwargs):
    circle = plt.Circle((0, 0), radius, fill=False, **kwargs)
    ax.add_artist(circle)

def draw_radial_lines(ax, r1, r2, num, **kwargs):
    angles = np.linspace(0, 2*np.pi, num, endpoint=False)
    for angle in angles:
        ax.plot([r1*np.cos(angle), r2*np.cos(angle)], [r1*np.sin(angle), r2*np.sin(angle)], **kwargs)

def draw_petals(ax, r_base, r_tip, num, width, **kwargs):
    angles = np.linspace(0, 2*np.pi, num, endpoint=False)
    for angle in angles:
        petal_angles = np.linspace(angle - width/2, angle + width/2, 80)
        r = np.linspace(r_base, r_tip, 80)
        x = r * np.cos(petal_angles)
        y = r * np.sin(petal_angles)
        ax.plot(x, y, **kwargs)

def draw_dots(ax, radius, num, size=25, **kwargs):
    angles = np.linspace(0, 2*np.pi, num, endpoint=False)
    for angle in angles:
        ax.scatter([radius*np.cos(angle)], [radius*np.sin(angle)], s=size, **kwargs)

fig, ax = plt.subplots(figsize=(8,8))
ax.set_aspect('equal')
ax.axis('off')

# Outer petals
draw_petals(ax, r_base=8, r_tip=10, num=24, width=np.pi/8, color='black', lw=2)
draw_petals(ax, r_base=7, r_tip=8.5, num=24, width=np.pi/10, color='black', lw=1)

# Next inner petals
draw_petals(ax, r_base=6, r_tip=8, num=24, width=np.pi/9.5, color='black', lw=1)

# Large middle flower
draw_petals(ax, r_base=3.7, r_tip=6, num=12, width=np.pi/4, color='black', lw=2)
draw_petals(ax, r_base=2.7, r_tip=4.7, num=12, width=np.pi/6, color='black', lw=1)

# Smaller inner petals
draw_petals(ax, r_base=2, r_tip=3.2, num=12, width=np.pi/5, color='black', lw=1)

# Circles
for r in [1.1, 2, 3.5, 6, 7.5, 9]:
    draw_circle(ax, r, color='black', lw=1)

# Radial lines (like a 'sun' in the middle)
draw_radial_lines(ax, 0.2, 1.1, 40, color='black', lw=1)

# Middle and outer dot rings
draw_dots(ax, radius=3.5, num=24, size=24, color='black')
draw_dots(ax, radius=7.9, num=24, size=20, color='black')
draw_dots(ax, radius=10.2, num=24, size=18, color='black')

# Center circle (solid fill)
center_circle = plt.Circle((0, 0), 0.35, color='black')
ax.add_artist(center_circle)

plt.xlim(-11, 11)
plt.ylim(-11, 11)
plt.title("Lineal Mandala Kolam", fontsize=16)
plt.show()