# memory.py
from manim import *
import numpy as np

class Memory(VGroup):
    

    def __init__(self, width=10, height=1, num_slots=21, values=None, **kwargs):
        super().__init__(**kwargs)

        self.width = width
        self.height = height
        self.num_slots = num_slots
        self.slot_width = width / num_slots

        # 1. Outer rectangle
        rect = Rectangle(width=width, height=height)

        # 2. Divider lines
        lines_group = VGroup()
        for i in range(num_slots):
            line = Line(
                start=[0, 0, 0],
                end=[0, height, 0]
            ).shift(
                LEFT * (width / 2) + RIGHT * i * self.slot_width
            ).shift(
                DOWN * (height / 2)
            )
            lines_group.add(line)

        # 3. Index labels (above slots)
        index_labels = VGroup()
        for i in range(num_slots):
            index = Tex(str(i), color=WHITE).scale(0.3)
            x_pos = -width / 2 + (i + 0.5) * self.slot_width
            y_pos = height / 2 + 0.3
            index.move_to([x_pos, y_pos, 0])
            index_labels.add(index)

        # 4. Value labels (inside slots)
        value_labels = VGroup()
        for i in range(num_slots):
            val = str(values[i]) if values and i < len(values) else ""
            value = Tex(val, color=YELLOW).scale(0.35)
            x_pos = -width / 2 + (i + 0.5) * self.slot_width
            y_pos = 0  # center vertically
            value.move_to([x_pos, y_pos, 0])
            value_labels.add(value)

        # 5. Group everything
        self.add(rect, lines_group, index_labels, value_labels)

        # 6. Expose elements for later use
        self.rect = rect
        self.lines = lines_group
        self.index_labels = index_labels
        self.value_labels = value_labels


    def set_value(self, index, new_value, color=YELLOW):
        x_pos = -self.width / 2 + (index + 0.5) * self.slot_width
        y_pos = 0
        new_tex = Tex(str(new_value), color=color).scale(0.35)
        new_tex.move_to([x_pos, y_pos, 0])

        # Replace the old label at `index`
        self.value_labels[index].become(new_tex)


        
