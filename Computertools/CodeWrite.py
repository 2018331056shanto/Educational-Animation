from manim import *

class CustomCode(VGroup):
    def __init__(
        self,
        code_lines=None,
        scale_factor=0.25,
        stroke_width=0.5,
        font="Consolas",
        default_color=WHITE,
        **kwargs
    ):
        super().__init__(**kwargs)

        if code_lines is None:
            code_lines = [""]

        self.code_texts = VGroup()
        self.highlights = {}  # Dictionary to keep track of highlights

        for line in code_lines:
            text = Text(line, font=font, color=default_color)
            text.scale(scale_factor)
            text.set_stroke(width=stroke_width)
            text.align_to(ORIGIN, LEFT)
            self.code_texts.add(text)

        self.code_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        self.code_texts.to_edge(LEFT).shift(RIGHT * 0.5)

        self.add(self.code_texts)

    def set_highlight(self, index, color=GREEN):
        if index < len(self.code_texts):
            highlight = SurroundingRectangle(self.code_texts[index], color=color, buff=0.05)
            self.highlights[index] = highlight
            self.add(highlight)
            return highlight  # Return the highlight for animation
        return None

    def remove_highlight(self, index):
        if index in self.highlights:
            self.remove(self.highlights[index])
            del self.highlights[index]
    def set_group_highlight(self, start, end, color=YELLOW):
        group = VGroup()
        for i in range(start, end + 1):
            if i < len(self.code_texts):
                rect = SurroundingRectangle(self.code_texts[i], color=color, buff=0.05)
                self.add(rect)
                group.add(rect)
        return group

    
    def remove_group_highlight(self, start_index, end_index):
        for i in range(start_index, end_index + 1):
            if i in self.highlights:
                self.remove(self.highlights[i])
                del self.highlights[i]
