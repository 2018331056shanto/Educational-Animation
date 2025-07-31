from Thread import *
from Memory import *
from MemorySegment import *

class Show(Scene):
    def construct(self):
        segmented = SegmentedMemory(
            width=10,
            height=1,
            num_slots=21,
            num_segments=4,
            heap_factor=2,
            # values=[f"{i}" for i in range(21)],
            labels=["Code", "Data", "Stack", "Heap"]
        )
        # segmented.move_to(ORIGIN)

        segmented.set_value(3,6)

        self.play(Write(segmented))

        # ram=Memory(width=10,height=1,num_slots=10)
        # ram.set_value(0,"3")
        # self.play(Write(ram))
        self.wait(10)
        
