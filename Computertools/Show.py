from Thread import *
from Memory import *
from MemorySegment import *
from CodeWrite import *
from PointingArrowScene import *
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
        # custom_code = [
        #     "package main",
        #     'import "fmt"',
        #     "func main() {",
        #     '    fmt.Println("Hello, Go")',
        #     "    undeclaredVar := 5",
        #     "}",
        # ]

        # # Create the code block
        # scopes = CustomCode(code_lines=custom_code)
        # self.play(Write(scopes))

        # self.wait(1)

        # # Highlight line 1 (import "fmt")
        # highlight_1 = scopes.set_highlight(1, color=RED)
        # self.play(Create(highlight_1))

        # self.wait(1)

        # # Highlight line 4
        # highlight_4 = scopes.set_highlight(4, color=GREEN_C)
        # self.play(Create(highlight_4))

        # self.wait(1)

        # # Remove line 1 highlight
        # self.play(FadeOut(highlight_1))
        # scopes.remove_highlight(1)

        # self.wait(2)
        # nodes = [
        #     Text("Start", color=BLUE).shift(LEFT * 4),
        #     Text("Middle", color=GREEN),
        #     Text("End", color=ORANGE).shift(RIGHT * 4),
        #     Text("Start", color=BLUE).shift(LEFT * 5),
        #     Text("Middle", color=GREEN).shift(UP*2),
        #     Text("End", color=ORANGE).shift(DOWN * 4)
        # ]

        # # Show text nodes
        # self.play(*[Write(node) for node in nodes])

        # arrows = VGroup()
        # for i in range(len(nodes) - 1):
        #     connector = ArrowConnector(
        #         nodes[i],
        #         nodes[i + 1],
        #         curved=(i % 2 == 0),  # curve every alternate arrow
        #         color=YELLOW,
        #         path_arc=PI / 2 if i % 2 == 0 else 0,
        #         start_p="left",
        #         end_p="top"
        #     )
        #     arrows.add(connector)

        # # Animate arrows creation
        # for arrow in arrows:
        #     self.play(Create(arrow))
        # self.wait(2)
        # demo=Memory()

        # self.play(Write(demo))
        # demo.set_value(index=10,new_value="10")
        # self.play(Indicate(demo))
        # self.wait(10)
        # initial_values = [5, 3, 8, 1, 9, 2, 7]
        # memory = Memory(width=12, height=1.2, num_slots=10, values=initial_values)
        
        # self.play(Write(memory))
        # self.wait(1)
        
        # # Demonstrate set_value
        # memory.set_value(3, "NEW", RED)
        # self.play(Indicate(memory.get_value_label(3)))
        # self.wait(1)
        
        # # Demonstrate highlighting
        # highlight_anim = memory.highlight_cell(5, GREEN)
        # if highlight_anim:
        #     self.play(highlight_anim)
        # self.wait(1)
        
        # # Demonstrate filling multiple values
        # new_values = ["A", "B", "C", "D", "E"]
        # memory.fill_values(new_values)
        # self.wait(2)

        # seg_mem = SegmentedMemory(
        #     width=14,
        #     height=1,
        #     num_slots=20,
        #     labels=["Code", "Data", "Stack", "Heap"],
        #     segment_ranges=[(0, 4), (5, 9), (10, 14), (15, 19)],
        #     up=1
        # )
        
        # self.play(Write(seg_mem))
        # self.wait(1)
        # seg_mem.set_value(1,"shanto")
        # self.play(Write(seg_mem))
        
        # # Fill different segments
        # # seg_mem.fill_segment(0, ["int", "main", "{", "}", "ret"])
        # # seg_mem.fill_segment(1, ["x=5", "y=10", "arr[]"])
        # # seg_mem.fill_segment(2, ["func1", "func2"])
        
        # self.wait(1)
        
        # # Highlight segments
        # # self.play(seg_mem.highlight_segment(0, YELLOW))
        # # self.wait(0.5)
        # # self.play(seg_mem.highlight_segment(1, GREEN))
        # # self.wait(0.5)
        
        # # # Push to stack
        # # stack_addr = seg_mem.animate_push_to_segment(2, "new_var", RED)
        # # if stack_addr is not None:
        # #     self.play(Indicate(seg_mem.get_value_label(stack_addr)))
        
        # # self.wait(2)
        
        # # # Show segment info
        # # info = seg_mem.get_segment_info(0)
        # # print(f"Segment info: {info}")
        
        # # self.wait(3)

        mem=Memory()
        mem.shift(UP*2+LEFT*2)

        self.play(Write(mem))



        mem.set_value(1,"shanto")
        self.wait(10)