from manim import *
import sys
import os

# Import custom components
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from Computertools.CodeWrite import CustomCode
from Computertools.MemorySegment import SegmentedMemory
from Computertools.PointingArrowScene import ArrowConnector

class Scopes(Scene):
    def construct(self):
        # Code to be shown
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

        # Visual code block
        code_block = CustomCode(code_lines=code_lines, scale_factor=0.20)
        code_block.shift(RIGHT * 11 + DOWN * 2)

        # Memory representation with 2 segments: Global and Local
        segmented_memory = SegmentedMemory(
            labels=["Global", "Local"], 
            num_segments=2, 
            segment_ranges=[(0, 4), (5, 14)],
            height=0.8,
            num_slots=15
        )
        segmented_memory.shift(UP * 2.5 + LEFT * 2)

        self.play(Write(code_block))
        self.play(Write(segmented_memory))

        # Compilation-time explanation
        compilation_messages = [
            "During Compilation Time",
            "Codes are read line by line", 
            "All Variables & Functions",
            "Stored in Global Scope"
        ]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.7)
        self.play(Write(compilation_explainer))

        # Ranges in the code to highlight as blocks
        highlight_ranges = {
            2: 2,    # "var a, b = 20, 30"
            3: 6,    # "func add(...)"
            7: 13    # "func main(...)"
        }

        # Data to be inserted into memory
        memory_data = {
            0: ["20", "30"],                      # values of a, b
            1: ["add(){..}"],                # function add
            2: ["main(){..}"]                # function main
        }
        memory_labels = ["a", "b", "add", "main"]

        current_memory_index = 0
        data_block_index = 0
        label_index = 0

        # Highlight and update memory
        i = 0
        while i < len(code_block.code_texts):
            if i in highlight_ranges:
                end = highlight_ranges[i]
                if end < i or end >= len(code_block.code_texts):
                    print(f"Invalid highlight range: {i} to {end}")
                    i += 1
                    continue

                # Highlight block of code
                block_highlight = code_block.set_group_highlight(i, end)
                self.play(Indicate(block_highlight))

                # Insert memory values and labels
                for item in memory_data[data_block_index]:
                    segmented_memory.set_value(current_memory_index, item, color=WHITE, factor=0.3)
                    segmented_memory.set_label_down(label_index, memory_labels[label_index], color=WHITE, factor=0.4)

                    # Draw arrow connection from code to memory
                    arrow = ArrowConnector(block_highlight, segmented_memory.memory.rects[current_memory_index], start_p="left", end_p="down")
                    self.play(Write(arrow))

                    current_memory_index += 1
                    label_index += 1
                    self.wait(2)
                    self.play(FadeOut(arrow))

                self.play(FadeOut(block_highlight))
                i = end + 1
                data_block_index += 1
            else:
                # Highlight single line
                single_highlight = code_block.set_highlight(i)
                self.play(Indicate(single_highlight))
                self.play(FadeOut(single_highlight))
                i += 1
        self.play(FadeOut(compilation_explainer))
        compilation_messages=["Execution starts with the main() function"," it is the entry point of any Go program"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))
        self.play(FadeOut(compilation_explainer))

        compilation_messages=["When main() function is called","A new Stack is created in Local Scope "]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))

        segmented_memory.add_nested_segment(
        parent_segment_index=1,
        num_slots=3,
        label="main Stack",
        color=BLUE,
        fill_opacity=0.2,
        scale=.65

)
        self.play(FadeOut(compilation_explainer))
        # segmented_memory.delete_nested_segment(self,0)

        compilation_messages=["Local Variable p, q are allocated inside Stack"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer)) 
        

        
        values_in_nested_segment=["30","40"]
        labels_in_nested_segment=["p","q"]
        track_nested_block=0
        for i in range(9,11):
            line=code_block[i]
            self.play(Indicate(line))
            seg_start,seg_end=segmented_memory.segment_ranges[1]
    
            segmented_memory.set_value(seg_start+track_nested_block,values_in_nested_segment[track_nested_block],color=WHITE, factor=0.3)
            segmented_memory.set_label_down(seg_start+track_nested_block, labels_in_nested_segment[track_nested_block], color=WHITE, factor=0.4)
            arrow = ArrowConnector(line, segmented_memory.memory.rects[seg_start+track_nested_block], start_p="left", end_p="down")
            track_nested_block=track_nested_block+1

            self.play(Write(arrow))
            self.wait(2)
            self.play(FadeOut(arrow))
            self.play(FadeOut(line))
        self.play(FadeOut(compilation_explainer))

        compilation_messages=["Now it will search for add()"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer)) 
        self.play(FadeOut(compilation_explainer))
        
        block=code_block.set_highlight(10)
        self.play(Write(block))

        compilation_messages=["Search add() in Local Scope"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer)) 

        
        seg_start,seg_end=segmented_memory.segment_ranges[1]

        main_stack=seg_start
        while main_stack<=seg_start+2:
            self.play(Indicate(segmented_memory.memory.rects[main_stack]))
            main_stack=main_stack+1

        self.play(FadeOut(compilation_explainer))

        compilation_messages=["As add() not in Local Scope","Now Search in Global Scope"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))

        seg_start,seg_end=segmented_memory.segment_ranges[0]

        global_memory_index=seg_start
        while global_memory_index<=seg_end:
            if global_memory_index==2:
                self.play(Indicate(segmented_memory.memory.rects[global_memory_index],scale_factor=1.3,color=RED))
                break
            else:
                self.play(Indicate(segmented_memory.memory.rects[global_memory_index]))
                global_memory_index=global_memory_index+1

        self.play(FadeOut(compilation_explainer))
        
        compilation_messages=["So a new Local Scope is created for add()"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.3)
        self.play(Write(compilation_explainer))

        segmented_memory.add_nested_segment(
        parent_segment_index=1,
        num_slots=3,
        label="add Stack",
        color=GREEN_D,
        fill_opacity=0.2,
        scale=.65

)
        self.play(FadeOut(compilation_explainer))  


       
        compilation_messages=["And now it will search for p & q","in local main's local scope","As it's in there so value of","p & q will get copied inside","add's stack in variable x & y"]

        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))    

        self.play(FadeOut(block))

        block=code_block.set_highlight(3)
        self.play(Write(block))

        indication_index=[5,6]
        copy_value_index=[8,9]
        value_to_copy=[30,40]
        labels_for_copy_value=["x","y"]
        i=0
        while i<len(indication_index):
          
            highlight=SurroundingRectangle(segmented_memory.memory.rects[indication_index[i]])
            self.play(Indicate(highlight))
            highlight1=segmented_memory.memory.rects[copy_value_index[i]]
            self.play(Indicate(highlight1))
            arrow=ArrowConnector(highlight,highlight1,curved=True,path_arc=PI*.83,start_p="down",end_p="down")
            self.play(Write(arrow))
            segmented_memory.set_value(copy_value_index[i],new_value=value_to_copy[i])
            segmented_memory.set_label_down(copy_value_index[i],labels_for_copy_value[i])

            self.play(FadeOut(arrow))
            self.play(FadeOut(highlight))

            i=i+1


        self.play(FadeOut(block))
        block=code_block.set_highlight(4)
        self.play(Write(block))
        self.play(FadeOut(compilation_explainer))
        compilation_messages=["Now our program search for x & y","In add's Local Scope and store","sum of x & y in z"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer)) 

        highlighted_cells=[]
        for i in range(8,10):
            highlighted_cell=SurroundingRectangle(segmented_memory.memory.rects[i],buff=0)
            self.play(Write(highlighted_cell))
            highlighted_cells.append(highlighted_cell)

        self.play(FadeOut(compilation_explainer))

        compilation_messages=["30 + 40 = 70"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))
        arrow=ArrowConnector(code_block[4], segmented_memory.memory.rects[10],start_p="left",end_p="down")
        self.play(Write(arrow))
        segmented_memory.set_value(10,"70")
        segmented_memory.set_label_down(10,"z")
        
        self.play(FadeOut(arrow))
        # self.play(FadeOut(highlighted_cell))
        for i in highlighted_cells:
            self.play(FadeOut(i))

        self.play(FadeOut(block))
        self.play(FadeOut(compilation_explainer))


        compilation_messages=["Now value of z wil print","And it will serch for z inside add's Local Scope"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))

        block=code_block.set_highlight(5)
        self.play(Write(block))

        value_block=SurroundingRectangle()
        for i in range(8,11):
            if i==10:
                value_block=SurroundingRectangle(segmented_memory.memory.rects[i],color=BLUE)
                self.play(Write(value_block))
                break
            else:
                self.play(Indicate(segmented_memory.memory.rects[i]))

        self.play(FadeOut(compilation_explainer))

        compilation_messages=["Now value of z will get printed","70"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))

        self.play(FadeOut(block))

        self.play(FadeOut(value_block))

        self.play(FadeOut(compilation_explainer))

        compilation_messages=["As execution completed add's stack","will get deleted"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))
        for i in range(8,11):
            segmented_memory.clear_value(i)
            segmented_memory.set_label_down(i,"-")

        segmented_memory.delete_nested_segment(self,index=1)

        self.play(FadeOut(compilation_explainer))



        # =========================================================================================================
        compilation_messages=["Again it will search for add()"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer)) 
        self.play(FadeOut(compilation_explainer))
        
        block=code_block.set_highlight(11)
        self.play(Write(block))

        compilation_messages=["Search add() in Local Scope"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer)) 

        
        seg_start,seg_end=segmented_memory.segment_ranges[1]

        main_stack=seg_start
        while main_stack<=seg_start+2:
            self.play(Indicate(segmented_memory.memory.rects[main_stack]))
            main_stack=main_stack+1

        self.play(FadeOut(compilation_explainer))

        compilation_messages=["As add() not in Local Scope","Now Search in Global Scope"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))

        seg_start,seg_end=segmented_memory.segment_ranges[0]

        global_memory_index=seg_start
        while global_memory_index<=seg_end:
            if global_memory_index==2:
                self.play(Indicate(segmented_memory.memory.rects[global_memory_index],scale_factor=1.3,color=RED))
                break
            else:
                self.play(Indicate(segmented_memory.memory.rects[global_memory_index]))
                global_memory_index=global_memory_index+1

        self.play(FadeOut(compilation_explainer))
        
        compilation_messages=["So a new Local Scope is created for add()"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.3)
        self.play(Write(compilation_explainer))

        segmented_memory.add_nested_segment(
        parent_segment_index=1,
        num_slots=6,
        label="add Stack",
        color=YELLOW_B,
        fill_opacity=0.9,
        scale=.65

)
        self.play(FadeOut(compilation_explainer))  


       
        compilation_messages=["And now it will search for a & b","in local main's local scope"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))   
        for i in range(5,8):
            self.play(Indicate(segmented_memory.memory.rects[i]))
        
        self.play(FadeOut(compilation_explainer))


        compilation_messages=["As a & b not in Local Scope","Now it will search for a & b","in Global scope"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))

        

        self.play(FadeOut(block))

        block=code_block.set_highlight(3)
        self.play(Write(block))

        indication_index=[0,1]
        copy_value_index=[8,9]
        value_to_copy=[20,30]
        labels_for_copy_value=["x","y"]
        i=0
        while i<len(indication_index):
          
            highlight=SurroundingRectangle(segmented_memory.memory.rects[indication_index[i]])
            self.play(Indicate(highlight))
            highlight1=segmented_memory.memory.rects[copy_value_index[i]]
            self.play(Indicate(highlight1))
            arrow=ArrowConnector(highlight,highlight1,curved=True,path_arc=PI*.83,start_p="down",end_p="down")
            self.play(Write(arrow))
            segmented_memory.set_value(copy_value_index[i],new_value=value_to_copy[i])
            segmented_memory.set_label_down(copy_value_index[i],labels_for_copy_value[i])

            self.play(FadeOut(arrow))
            self.play(FadeOut(highlight))

            i=i+1


        self.play(FadeOut(block))
        block=code_block.set_highlight(4)
        self.play(Write(block))
        self.play(FadeOut(compilation_explainer))
        compilation_messages=["Now our program search for x & y","In add's Local Scope and store","sum of x & y in z"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer)) 

        highlighted_cells=[]
        for i in range(8,10):
            highlighted_cell=SurroundingRectangle(segmented_memory.memory.rects[i],buff=0)
            self.play(Write(highlighted_cell))
            highlighted_cells.append(highlighted_cell)

        self.play(FadeOut(compilation_explainer))

        compilation_messages=["20 + 30 = 50"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))
        arrow=ArrowConnector(code_block[4], segmented_memory.memory.rects[10],start_p="left",end_p="down")
        self.play(Write(arrow))
        segmented_memory.set_value(10,"50")
        segmented_memory.set_label_down(10,"z")
        
        self.play(FadeOut(arrow))
        # self.play(FadeOut(highlighted_cell))
        for i in highlighted_cells:
            self.play(FadeOut(i))

        self.play(FadeOut(block))
        self.play(FadeOut(compilation_explainer))


        compilation_messages=["Now value of z wil print","And it will serch for z inside add's Local Scope"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))

        block=code_block.set_highlight(5)
        self.play(Write(block))

        value_block=SurroundingRectangle()
        for i in range(8,11):
            if i==10:
                value_block=SurroundingRectangle(segmented_memory.memory.rects[i],color=BLUE)
                self.play(Write(value_block))
                break
            else:
                self.play(Indicate(segmented_memory.memory.rects[i]))

        self.play(FadeOut(compilation_explainer))

        compilation_messages=["Now value of z will get printed","70"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))

        self.play(FadeOut(block))

        self.play(FadeOut(value_block))

        self.play(FadeOut(compilation_explainer))

        compilation_messages=["As execution completed add's stack","will get deleted"]
        compilation_explainer = CustomCode(code_lines=compilation_messages, scale_factor=0.5)
        self.play(Write(compilation_explainer))
        for i in range(8,11):
            segmented_memory.clear_value(i)
            segmented_memory.set_label_down(i,"-")

        segmented_memory.delete_nested_segment(self,index=1)

        self.play(FadeOut(compilation_explainer))

        self.wait(3)
      