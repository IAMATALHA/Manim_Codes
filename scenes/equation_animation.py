from manim import *

class SolveEquation(Scene):
    def construct(self):
        eq1 = MathTex("2x + 5 = 0")
        eq2 = MathTex("2x = -5")
        eq3 = MathTex("x = -\\frac{5}{2}")

        self.play(Write(eq1))
        self.wait(1)
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(1)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(2)
