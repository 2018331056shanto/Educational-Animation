from manim import *

class ArrowConnector(VGroup):
    def __init__(
        self,
        start_obj,
        end_obj,
        *,
        color=YELLOW,
        curved=False,
        path_arc=PI / 4,
        buff=0.2,
        stroke_width=3,
        tip_length=0.25,
        start_p="right",
        end_p="left",
        **kwargs
    ):
        super().__init__(**kwargs)

        start_point = self.get_anchor_point(start_obj, start_p)
        end_point = self.get_anchor_point(end_obj, end_p)

        if curved:
            direction = end_point - start_point
            direction /= np.linalg.norm(direction)
            start_point_adj = start_point + direction * buff
            end_point_adj = end_point - direction * buff

            arrow = CurvedArrow(
                start_point_adj,
                end_point_adj,
                color=color,
                angle=path_arc,
                stroke_width=stroke_width,
                tip_length=tip_length,
            )
        else:
            arrow = Arrow(
                start=start_point,
                end=end_point,
                color=color,
                buff=buff,
                stroke_width=stroke_width,
                tip_length=tip_length,
            )

        self.add(arrow)
        self.arrow = arrow

    @staticmethod
    def get_anchor_point(obj, direction: str) -> np.ndarray:
        mapping = {
            "left": obj.get_left,
            "right": obj.get_right,
            "top": obj.get_top,
            "bottom": obj.get_bottom,
            "center": obj.get_center,
        }
        return mapping.get(direction, obj.get_center)()
