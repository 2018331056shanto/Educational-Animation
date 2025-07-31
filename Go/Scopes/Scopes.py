from manim import *

class Scopes(Scene):
    def construct(self):
        # Go code lines
        code_lines = [
            "package main",
            'import "fmt"',
            "var a, b = 20, 30",
            "func add(x int, y int) {",
            "    z := x + y",
            "    fmt.Println(z)",
            "}",
            "func main() {",
            "    p := 30",
            "    q := 40",
            "    add(p, q)",   
            "    add(a, b)",   
            "    add(a, z)",   
            "}",
        ]

        code_texts = VGroup()

        for i, line in enumerate(code_lines):
            color =  WHITE
            text = Text(line, font="Consolas", color=color).scale(0.2)
            text.align_to(ORIGIN, LEFT)
            text.set_stroke(width=.5)
            code_texts.add(text)

        # Arrange lines top-down, aligned to left
        code_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        code_texts.to_edge(LEFT).shift(RIGHT * 0.5)

    

        self.play(Write(code_texts))
       
