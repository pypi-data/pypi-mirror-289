# plotdetection/visualization.py

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


class PlotDetection:
    def __init__(self, safe_mass=5, safe_angle=np.pi / 4):
        self.ani = None
        self.safe_mass = safe_mass
        self.safe_angle = safe_angle

        # Setup plot
        self.fig, self.ax = plt.subplots(subplot_kw={'projection': 'polar'})
        self.ax.set_facecolor('lightgreen')
        self.ax.grid(True, color='black')
        self.ax.xaxis.set_tick_params(color='black')
        self.ax.yaxis.set_tick_params(color='black', labelleft=False)

        # Plot safe point
        self.safe_point, = self.ax.plot(self.safe_angle, self.safe_mass, 'bo', markersize=10, label='Safe Point')

        # Initialize point for current data
        self.current_point, = self.ax.plot([], [], 'ro', markersize=5, label='Current Point')

        # Add labels and legend
        self.ax.set_rmax(10)  # Set maximum radius
        self.ax.legend(loc='upper right')
        self.ax.set_title('Real-Time Rotor Monitoring')

    def update_plot(self, mass, angle):
        """Update the plot with new data."""
        self.current_point.set_data([angle], [mass])

        # Check tolerance and compare
        mass_difference = mass - self.safe_mass
        angle_difference = angle - self.safe_angle
        print(f"Current Mass: {mass:.2f}, Angle: {np.degrees(angle):.2f}°")
        print(f"Mass Difference: {mass_difference:.2f}, Angle Difference: {np.degrees(angle_difference):.2f}°")

        return self.current_point,

    def start_animation(self, data_generator, interval=1000, frames=100):
        """Start the animation with data from a generator function."""
        self.ani = FuncAnimation(self.fig, self._update_func, frames=frames, blit=True, interval=interval, fargs=(data_generator,))
        plt.show()

    def _update_func(self, frame, data_generator):
        mass, angle = next(data_generator)
        return self.update_plot(mass, angle)
