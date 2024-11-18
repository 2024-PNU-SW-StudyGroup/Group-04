import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define constants
c = 3e8  # Speed of light (m/s)
frequency = 5.8e9  # Frequency (Hz)
wavelength = c / frequency  # Wavelength (m)
turns = 25  # Number of turns
radius = wavelength / (2 * np.pi)  # Approximate radius for 5.8 GHz helix
pitch = wavelength / 16  # Pitch of the helix

# Define theta (elevation) and phi (azimuth) angles
theta = np.linspace(0, np.pi, 180)  # Elevation angles from 0 to 180 degrees
phi = np.linspace(0, 2 * np.pi, 360)  # Azimuth angles from 0 to 360 degrees
theta, phi = np.meshgrid(theta, phi)

# Helical antenna directivity pattern function with side lobe suppression
def helical_directivity_main_lobe(theta, phi, turns, wavelength, radius, pitch):
    k = 2 * np.pi / wavelength  # Wave number
    axial_mode_gain = 20  # Gain adjusted for 25 turns
    R = radius
    
    # Axial mode (main lobe) gain formula
    main_lobe = np.sin(theta) ** 2 * np.exp(-((theta - np.pi/2) ** 2) / (0.05 * turns))
    
    # Suppress side lobes (values outside a certain range)
    main_lobe[theta < np.pi / 4] = 0  # Suppress below 45 degrees
    main_lobe[theta > 3 * np.pi / 4] = 0  # Suppress above 135 degrees
    
    # Apply a gain factor to simulate a realistic directivity pattern
    gain = axial_mode_gain * main_lobe
    
    return gain

# Calculate directivity with side lobe suppression
directivity = helical_directivity_main_lobe(theta, phi, turns, wavelength, radius, pitch)

# Convert spherical coordinates to Cartesian coordinates for 3D plot
x = directivity * np.sin(theta) * np.cos(phi)
y = directivity * np.sin(theta) * np.sin(phi)
z = directivity * np.cos(theta)

# Create 3D plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with color mapping for intensity
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Labels and title
ax.set_title('Helical Antenna 3D Main Lobe Radiation Pattern (25 Turns, Pitch = λ/16)', fontsize=16)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Ensure equal scaling for all axes (for accurate representation)
max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
mid_x = (x.max()+x.min()) * 0.5
mid_y = (y.max()+y.min()) * 0.5
mid_z = (z.max()+z.min()) * 0.5

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range)

# Show plot
plt.show()
