# segmented_memory.py
from manim import *
import sys
import os

# Add path to 'Computertools' package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from Computertools.Memory import Memory

class SegmentedMemory(VGroup):
    def __init__(
        self,
        width=10,
        height=1,
        num_slots=21,
        num_segments=4,
        heap_factor=2,
        values=None,            # Optional: List of values per slot
        labels=None,            # Optional: Segment labels
        colors=None,            # Optional: Segment colors  
        segment_ranges=None,    # Allow manual segment definition
        left=0,
        right=0,
        up=0,
        down=0,
        opacity=0,
        **kwargs
    ):
        super().__init__(**kwargs)

        self.width = width
        self.height = height
        self.num_slots = num_slots
        self.num_segments = num_segments
        self.heap_factor = heap_factor
        self.opacity=opacity

        # 1. Memory bar with optional values
        self.memory = Memory(width=width, height=height, num_slots=num_slots, values=values)
        slot_width = width / num_slots
        segment_height = height * 2

        # 2. Compute segment ranges
        if segment_ranges is None:
            # Automatic segmentation
            segments = []
            total_weight = num_segments - 1 + heap_factor
            base = num_slots / total_weight

            for i in range(num_segments):
                if i < num_segments - 1:
                    slot_count = int(base)
                else:
                    used = sum(e - s + 1 for (s, e) in segments)
                    slot_count = num_slots - used
                start = segments[-1][1] + 1 if segments else 0
                end = start + slot_count - 1
                segments.append((start, end))
        else:
            # Manual segment ranges
            segments = segment_ranges

        # 3. Draw segment rectangles + labels
        self.segments = VGroup()
        self.segment_labels = VGroup()

        default_labels = [f"Segment {i}" for i in range(len(segments) - 1)] + ["Heap"]
        self.labels_text = labels or default_labels

        default_colors = [YELLOW, GREEN, BLUE, RED, ORANGE, PURPLE]
        self.segment_colors = colors or default_colors

        for i, (start_idx, end_idx) in enumerate(segments):
            num_cells = end_idx - start_idx + 1
            seg_width = num_cells * slot_width
            x_center = -width / 2 + (start_idx + num_cells / 2) * slot_width

            rect = Rectangle(
                width=seg_width,
                height=segment_height,
                color=self.segment_colors[i % len(self.segment_colors)],
                fill_opacity=self.opacity
            )
            rect.move_to([x_center, 0, 0])
            self.segments.add(rect)

            label = Tex(self.labels_text[i], color=WHITE).scale(0.4)
            label.next_to(rect, UP, buff=0.1)
            self.segment_labels.add(label)

        # 4. Add everything to the group
        self.add(self.memory, self.segments, self.segment_labels)
        
        # Apply positioning
        if left or right or up or down:
            self.shift(LEFT*left + RIGHT*right + UP*up + DOWN*down)

        # 5. Store segment information
        self.segment_ranges = segments
        self.nested_segments_by_parent = {}


    # Memory manipulation methods
    def set_value(self, index, new_value, color=YELLOW ,factor=.35):
        """Set value at specific memory index"""
        if hasattr(self.memory, 'set_value'):
            self.memory.set_value(index, new_value, color,factor)
        else:
            print(f"Memory object missing set_value method")

    def set_label_down(self, index, new_value, color=YELLOW ,factor=.35):
        """Set value at specific memory index"""
        if hasattr(self.memory, 'set_value'):
            self.memory.set_label_down(index, new_value, color,factor)
        else:
            print(f"Memory object missing set_value method")

    def get_value_label(self, index):
        """Get value label at specific index"""
        if hasattr(self.memory, 'get_value_label'):
            return self.memory.get_value_label(index)
        elif hasattr(self.memory, 'value_labels') and 0 <= index < len(self.memory.value_labels):
            return self.memory.value_labels[index]
        return None

    def clear_value(self, index):
        """Clear value at specific index"""
        if hasattr(self.memory, 'clear_value'):
            self.memory.clear_value(index)
        else:
            self.set_value(index, "", YELLOW)

    def fill_values(self, values_list, start_index=0):
        """Fill multiple values starting from start_index"""
        for i, value in enumerate(values_list):
            if start_index + i < self.num_slots:
                self.set_value(start_index + i, value)

    def fill_segment(self, segment_index, values_list):
        """Fill specific segment with values"""
        if 0 <= segment_index < len(self.segment_ranges):
            start_idx, end_idx = self.segment_ranges[segment_index]
            print(f"Filling segment {segment_index}: range {start_idx}-{end_idx} with {values_list}")
            for i, value in enumerate(values_list):
                if start_idx + i <= end_idx:
                    self.set_value(start_idx + i, value)
                    print(f"  Set index {start_idx + i} to {value}")

    def clear_segment(self, segment_index):
        """Clear all values in a specific segment"""
        if 0 <= segment_index < len(self.segment_ranges):
            start_idx, end_idx = self.segment_ranges[segment_index]
            for i in range(start_idx, end_idx + 1):
                self.clear_value(i)

    # Highlighting methods
    def highlight_cell(self, index, color=RED, width=3):
        """Highlight a specific memory cell"""
        return self.memory.highlight_cell(index, color)

    def highlight_segment(self, segment_index, color=RED, width=4):
        """Highlight a specific segment"""
        if 0 <= segment_index < len(self.segments):
            return self.segments[segment_index].animate.set_stroke(color, width=width)
        return None

    def highlight_segment_range(self, segment_index, color=RED):
        """Highlight all cells in a segment"""
        if 0 <= segment_index < len(self.segment_ranges):
            start_idx, end_idx = self.segment_ranges[segment_index]
            animations = []
            for i in range(start_idx, end_idx + 1):
                anim = self.highlight_cell(i, color)
                if anim:
                    animations.append(anim)
            return animations
        return []

    # Information methods
    def get_segment_info(self, segment_index):
        """Get information about a specific segment"""
        if 0 <= segment_index < len(self.segment_ranges):
            start_idx, end_idx = self.segment_ranges[segment_index]
            return {
                'index': segment_index,
                'label': self.labels_text[segment_index],
                'range': (start_idx, end_idx),
                'size': end_idx - start_idx + 1,
                'color': self.segment_colors[segment_index % len(self.segment_colors)]
            }
        return None

    def get_segment_by_address(self, address):
        """Get which segment contains the given address"""
        for i, (start_idx, end_idx) in enumerate(self.segment_ranges):
            if start_idx <= address <= end_idx:
                return i
        return None

    def get_all_segments_info(self):
        """Get information about all segments"""
        return [self.get_segment_info(i) for i in range(len(self.segment_ranges))]

    # Visual customization methods
    def set_segment_color(self, segment_index, color):
        """Change color of a specific segment"""
        if 0 <= segment_index < len(self.segments):
            self.segments[segment_index].set_color(color)
            self.segment_colors[segment_index] = color

    def set_segment_label(self, segment_index, new_label):
        """Change label of a specific segment"""
        if 0 <= segment_index < len(self.segment_labels):
            new_tex = Tex(new_label, color=WHITE).scale(0.4)
            new_tex.move_to(self.segment_labels[segment_index].get_center())
            self.segment_labels[segment_index].become(new_tex)
            self.labels_text[segment_index] = new_label

    def resize_segment(self, segment_index, new_size):
        """Resize a segment (advanced - may require reconstruction)"""
        # This would require rebuilding the segments
        # Implementation depends on specific requirements
        pass

    # Animation helpers
    def animate_push_to_segment(self, segment_index, value, color=YELLOW):
        """Animate pushing a value to the first available slot in segment"""
        if 0 <= segment_index < len(self.segment_ranges):
            start_idx, end_idx = self.segment_ranges[segment_index]
            # Find first empty slot
            for i in range(start_idx, end_idx + 1):
                current_label = self.get_value_label(i)
                if current_label and (not hasattr(current_label, 'tex_string') or current_label.tex_string == ""):
                    self.set_value(i, value, color)
                    return i
        return None

    def animate_pop_from_segment(self, segment_index):
        """Animate popping a value from the last occupied slot in segment"""
        if 0 <= segment_index < len(self.segment_ranges):
            start_idx, end_idx = self.segment_ranges[segment_index]
            # Find last occupied slot
            for i in range(end_idx, start_idx - 1, -1):
                current_label = self.get_value_label(i)
                if current_label and hasattr(current_label, 'tex_string') and current_label.tex_string:
                    old_value = current_label.tex_string
                    self.clear_value(i)
                    return old_value, i
        return None, None
    
    # def add_nested_segment(
    #     self,
    #     parent_segment_index,
    #     nested_start_offset,
    #     nested_end_offset,
    #     label="Nested",
    #     color=WHITE,
    #     fill_opacity=0.2,
    #     stroke_width=1,
    #     scale=0.2,
    #     buff=0
    # ):
    #     if not (0 <= parent_segment_index < len(self.segments)):
    #         print("Invalid parent segment index")
    #         return

    #     start, end = self.segment_ranges[parent_segment_index]
    #     slot_width = self.width / self.num_slots

    #     if start + nested_start_offset > start + nested_end_offset or start + nested_end_offset > end:
    #         print("Invalid nested range")
    #         return

    #     nested_start_idx = start + nested_start_offset
    #     nested_end_idx = start + nested_end_offset
    #     num_slots = nested_end_idx - nested_start_idx 

    #     nested_width = num_slots * slot_width

    #     nested_rect = Rectangle(
    #         width=nested_width,
    #         height=self.height * scale,
    #         color=color,
    #         fill_opacity=fill_opacity,
    #         stroke_width=stroke_width,
    #     )
    #     label_tex = Tex(label, color=color).scale(scale * 0.7)
    #     label_tex.next_to(nested_rect, UP, buff=buff)

    #     if not hasattr(self, "nested_segments"):
    #         self.nested_segments = []

    #     if len(self.nested_segments)==0:
    #         nested_rect.move_to(self.segments[parent_segment_index],LEFT)
    #     else:
    #         nested_rect.next_to(self.nested_segments[len(self.nested_segments)-1][0],RIGHT,buff=0)
    #     self.add(nested_rect, label_tex)
        
    #     self.nested_segments.append((nested_rect, label_tex))
    
    #     # Add to group
     

    #     # Track them
        
        

    #     return nested_rect, label_tex
    def add_nested_segment(
    self,
    parent_segment_index,
    num_slots=1,
    label="Nested",
    color=WHITE,
    fill_opacity=0.2,
    stroke_width=1,
    scale=0.2,
    buff=0
):
        if not (0 <= parent_segment_index < len(self.segments)):
            print("Invalid parent segment index")
            return

        slot_width = self.width / self.num_slots   

        nested_width = num_slots * slot_width

        nested_rect = Rectangle(
            width=nested_width,
            height=self.height * scale,
            color=color,
            fill_opacity=fill_opacity,
            stroke_width=stroke_width,
        )

        if not hasattr(self, "nested_segments"):
            self.nested_segments = []

        # Position the nested rectangle
        if len(self.nested_segments) == 0:
            nested_rect.move_to(self.segments[parent_segment_index], LEFT)
        else:
            last_nested_rect = self.nested_segments[-1][0]
            nested_rect.next_to(last_nested_rect, RIGHT, buff=0)

        # Now that the rect is positioned, position the label relative to it
        label_tex = Tex(label, color=color).scale(scale * 0.7)
        label_tex.next_to(nested_rect, UP, buff=buff)

        # Track and add to group
        self.nested_segments.append((nested_rect, label_tex))
        self.add(nested_rect, label_tex)

        return nested_rect, label_tex

    
    def delete_nested_segment(self, scene, index):
        if not hasattr(self, "nested_segments") or index >= len(self.nested_segments):
            print(f"No nested segment at index {index}")
            return

        nested_rect, label_tex = self.nested_segments[index]
        
        # Play fade out animation
        scene.play(FadeOut(nested_rect), FadeOut(label_tex))
        
        # 🔥 THIS IS CRITICAL
        self.remove(nested_rect)
        self.remove(label_tex)
        
        # Remove from tracking list
        del self.nested_segments[index]

   