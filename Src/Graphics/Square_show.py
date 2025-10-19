from manim import *

class SquareShow(Scene):
    def construct(self):
        current_square = Square()
        
        self.play(Create(current_square))
        self.wait(0.5)

        new_square = Square(side_length= 1.2)
        self.play(ReplacementTransform(current_square,new_square))
        current_square = new_square
        self.wait(0.5)

        self.play(FadeOut(current_square))