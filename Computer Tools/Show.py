from Thread import *
from Memory import *
from MemorySegment import *
from CodeWrite import *

class Show(Scene):
    def construct(self):
        # segmented = SegmentedMemory(
        #     width=10,
        #     height=1,
        #     num_slots=21,
        #     num_segments=2,
        #     heap_factor=2,
        #     # values=[f"{i}" for i in range(21)],
        #     labels=["Global", "Local"]
        # )
        # # segmented.move_to(ORIGIN)

        # segmented.set_value(3,6)
      

        # self.play(Write(segmented))

        # self.play(Indicate(segmented.segments[0],color=RED))
        # # ram=Memory(width=10,height=1,num_slots=10)
        # # ram.set_value(0,"3")
        # # self.play(Write(ram))
        # self.wait(10)
        custom_code = [
            "package main",
            'import "fmt"',
            "func main() {",
            '    fmt.Println("Hello, Go")',
            "    undeclaredVar := 5",
            "}",
        ]

        # Create the code block
        scopes = CustomCode(code_lines=custom_code)
        self.play(Write(scopes))

        self.wait(1)

        # Highlight line 1 (import "fmt")
        highlight_1 = scopes.set_highlight(1, color=RED)
        self.play(Create(highlight_1))

        self.wait(1)

        # Highlight line 4
        highlight_4 = scopes.set_highlight(4, color=GREEN_C)
        self.play(Create(highlight_4))

        self.wait(1)

        # Remove line 1 highlight
        self.play(FadeOut(highlight_1))
        scopes.remove_highlight(1)

        self.wait(2)