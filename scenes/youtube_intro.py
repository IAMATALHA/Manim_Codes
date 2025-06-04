from manim import *

class YouTubeLogo(VGroup):
    def __init__(self, width=4, height=2.5, **kwargs):
        super().__init__(**kwargs)
        bg = RoundedRectangle(width=width, height=height,
                              corner_radius=0.5,
                              color=RED, fill_opacity=1)
        triangle = Polygon(
            [-0.3, -0.5, 0],
            [-0.3, 0.5, 0],
            [0.6, 0, 0],
            color=WHITE,
            fill_opacity=1,
            stroke_width=0
        )
        triangle.move_to(bg.get_center())
        self.add(bg, triangle)

class YouTubeIntro(Scene):
    def construct(self):
        logo = YouTubeLogo()
        text = Text("Subscribe!", color=WHITE)
        VGroup(logo, text).arrange(DOWN)
        self.play(FadeIn(logo))
        self.play(Write(text))
        self.wait(2)
