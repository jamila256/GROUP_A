import matplotlib.pyplot as plt
import math

# Coordinates
x = [441489.397, 441486, 441471.393]
y = [68052.014, 68032.001, 68051.298]

# Plot the curve
plt.plot(x, y, marker='o', linestyle='-')
plt.title('Curve Ranging Exercise')
plt.xlabel('Easting (E)')
plt.ylabel('Northi(N)')

# Calculate tangent length
tangent_length = math.sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2)

# Calculate radius of the curve
radius = tangent_length / (2 * math.sin(math.radians(90)))

# Calculate radius of curvature
radius_of_curvature = radius / math.cos(math.radians(90))

# Calculate tangential angles
angle1 = math.atan2(y[2] - y[0], x[2] - x[0])
angle2 = math.atan2(y[2] - y[1], x[2] - x[1])

# Convert angles to degrees
angle1_deg = math.degrees(angle1)
angle2_deg = math.degrees(angle2)

# Display the results
print("Tangent Length:", tangent_length)
print("Radius of the Curve:", radius)
print("Radius of Curvature:", radius_of_curvature)
print("Tangential Angle 1 (degrees):", angle1_deg)
print("Tangential Angle 2 (degrees):", angle2_deg)

# Display the plot
plt.grid(True)
plt.show()
