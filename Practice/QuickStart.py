from manim import *


class demo(Scene):
    def construct(self):
        circle=Circle(color=GREEN_C,radius=1.2)
        rectangle=Rectangle(height=1.2,width=1.2,color=YELLOW_C)

        # circle.set_stroke(width=1)
        circle.set_fill(color=GREEN_D,opacity=1)
        rectangle.set_fill(RED_B,opacity=1)

        circle.shift(UP+1)

        
        self.play(ReplacementTransform(circle,rectangle))
        self.wait(1)