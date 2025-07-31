
from manim import *
import numpy as np

class Thread(VGroup):
    def __init__(self, radius=0.4, frequency=2, amplitude=0.1, stroke_color=BLUE, stroke_width=3, **kwargs):
        super().__init__(**kwargs)

        self.radius = radius
        self.frequency = frequency
        self.amplitude = amplitude
        self.length = 2 * radius

        # Draw the circle
        circle = Circle(radius=radius, color=WHITE)

        # Create the sine wave
        sine_wave = ParametricFunction(
            lambda t: [t - radius, amplitude * np.sin(frequency * (t / self.length) * TAU), 0],
            t_range=[0, self.length],
            color=stroke_color,
            stroke_width=stroke_width,
        )

        # Align center
        sine_wave.move_to(ORIGIN)
        sine_wave.rotate(PI/2)

        # Add to this group
        self.add(circle, sine_wave)

        # Expose parts if needed
        self.circle = circle
        self.wave = sine_wave
