from manim import *
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from Computertools.CodeWrite import CustomCode
from Computertools.MemorySegment import *

class Scopes(Scene):
    def construct(self):
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

        codeSection = CustomCode(code_lines=code_lines, scale_factor=.20)
        codeSection.shift(RIGHT*11 + DOWN*2)

        # SOLUTION 1: Position BEFORE creating the object
        ram = SegmentedMemory(
            labels=["Global", "Local"], 
            num_segments=2, 
            segment_ranges=[(0,5), (5,9)], 
            height=.8,
            num_slots=10,
            # colors=["G"]
            # opacity=
        )

        ram.shift(UP*2.5 + LEFT*2)  # Position immediately after creation

        self.play(Write(codeSection))
        self.play(Write(ram))

        textForCompilationTime = [
            "During Compilation Time",
            "Codes are read line by line", 
            "All Variables & Functions",
            "Stored in Global Scope"
        ]
        compilationText = CustomCode(code_lines=textForCompilationTime, scale_factor=.7)
        # compilationText.shift(LEFT*2.5+UP*2)
        self.play(Write(compilationText))

        highlightText = {
            2: 2,
            3: 6,
            7: 13
        }
        i = 0
        memoryCell = 0
        valuesInsideSlot={
            0:["20","30"],
            1:["func add(){..}"],
            2:["func main(){..}"]

        }
        indexToTrackVluesInsideSlot=0
        while i < len(codeSection.code_texts):
            if i in highlightText:
                end = highlightText[i]
                if end < i or end >= len(codeSection.code_texts):
                    print(f"Invalid highlight range: {i} to {end}")
                    i += 1
                    continue 

                group_highlight = codeSection.set_group_highlight(i, end)
                self.play(Indicate(group_highlight))
                value=valuesInsideSlot[indexToTrackVluesInsideSlot]
                for i in value:
                    ram.set_value(memoryCell,i,color=WHITE,factor=.3)
                    self.play(Indicate(ram.memory.rects[memoryCell],color=BLUE))
                    memoryCell=memoryCell+1
                    

                # self.play(Indicate(ram))
                self.play(FadeOut(group_highlight))
                i = end + 1  
                indexToTrackVluesInsideSlot=indexToTrackVluesInsideSlot+1
                 # Increment memory cell counter
            else:
                highlight = codeSection.set_highlight(i)
                self.play(Indicate(highlight))
                self.play(FadeOut(highlight))
                i += 1

        self.wait(3)