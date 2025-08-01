# memory.py
from manim import *
import numpy as np

class Memory(VGroup):
    def __init__(self, width=10, height=1, num_slots=15, values=None, **kwargs):
        super().__init__(**kwargs)
        
        self.width = width
        self.height = height
        self.num_slots = num_slots
        self.slot_width = width / num_slots
        self.values = values

        # Create rectangles
        self.rects = VGroup()
        for i in range(num_slots):
            rect = Rectangle(width=self.slot_width, height=height, fill_opacity=0)
            self.rects.add(rect)
        self.rects.arrange(RIGHT, buff=0)

        # Create index labels
        self.index_labels = VGroup()
        for i in range(num_slots):
            label = Text(str(i), color=WHITE).scale(0.3)
            x_pos = -width / 2 + (i + 0.5) * self.slot_width
            y_pos = height / 2 + 0.3
            label.move_to([x_pos, y_pos, 0])
            self.index_labels.add(label)

        # Create value labels
        self.value_labels = VGroup()
        for i in range(num_slots):
            val = str(values[i]) if values and i < len(values) else ""
            value = Tex(val, color=YELLOW).scale(0.35)
            x_pos = -width / 2 + (i + 0.5) * self.slot_width
            y_pos = 0  # center vertically
            value.move_to([x_pos, y_pos, 0])
            self.value_labels.add(value)

        # Add all components to the group
        
        self.add(self.rects, self.index_labels, self.value_labels)

    def set_value(self, index, new_value, color=YELLOW,factor=.35):
        """Set value at specific index"""
        if 0 <= index < len(self.value_labels):
            current_position = self.rects[index]
            new_tex = Tex(str(new_value), color=color).scale(factor)
            new_tex.move_to(current_position)
            self.value_labels[index].become(new_tex)

    def get_value_label(self, index):
        """Get value label at specific index"""
        if 0 <= index < len(self.value_labels):
            return self.value_labels[index]
        return None

    def highlight_cell(self, index, color=RED):
        """Highlight a specific memory cell"""
        if 0 <= index < len(self.rects):
            return self.rects[index].animate.set_stroke(color, width=3)
        return None

    def clear_value(self, index):
        """Clear value at specific index"""
        self.set_value(index, "", YELLOW)

    def fill_values(self, values_list):
        """Fill multiple values at once"""
        for i, value in enumerate(values_list):
            if i < self.num_slots:
                self.set_value(i, value)
