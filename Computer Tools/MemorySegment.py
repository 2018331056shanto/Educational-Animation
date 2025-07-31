# segmented_memory.py
from manim import *
from Memory import Memory

class SegmentedMemory(VGroup):
    def __init__(
        self,
        width=10,
        height=1,
        num_slots=21,
        num_segments=4,
        heap_factor=2,
        values=None,     # Optional: List of values per slot
        labels=None,     # Optional: Segment labels
        colors=None,     # Optional: Segment colors
        **kwargs
    ):
        super().__init__(**kwargs)

        # 1. Create memory block
        memory = Memory(width=width, height=height, num_slots=num_slots, values=values)

        slot_width = width / num_slots
        segment_height = height * 2

        # 2. Compute dynamic segments
        segments = []
        total_weight = num_segments - 1 + heap_factor
        base = num_slots / total_weight

        for i in range(num_segments):
            if i < num_segments - 1:
                slot_count = int(base)
            else:
                # Remaining slots for the last segment
                used = sum(e - s + 1 for (s, e) in segments)
                slot_count = num_slots - used
            start = segments[-1][1] + 1 if segments else 0
            end = start + slot_count - 1
            segments.append((start, end))

        # 3. Create segment rectangles + labels
        segment_group = VGroup()
        label_group = VGroup()

        default_labels = [f"Segment {i}" for i in range(num_segments - 1)] + ["Heap"]
        labels = labels or default_labels

        default_colors = [YELLOW, GREEN, BLUE, RED, ORANGE, PURPLE]
        colors = colors or default_colors

        for i, (start_idx, end_idx) in enumerate(segments):
            num_cells = end_idx - start_idx + 1
            seg_width = num_cells * slot_width
            x_center = -width / 2 + (start_idx + num_cells / 2) * slot_width

            rect = Rectangle(
                width=seg_width,
                height=segment_height,
                color=colors[i % len(colors)]
            )
            rect.move_to([x_center, 0, 0])
            segment_group.add(rect)

            label = Tex(labels[i], color=WHITE).scale(0.4)
            label.next_to(rect, UP, buff=0.1)
            label_group.add(label)

        self.add(memory, segment_group, label_group)

        # Expose for later use if needed``
        self.memory = memory
        self.segments = segment_group
        self.labels = label_group
        self.segment_ranges = segments

    def set_value(self, index, new_value, color=YELLOW):
        self.memory.set_value(index, new_value, color)
