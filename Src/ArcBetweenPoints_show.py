from manim import *

class ArcBetweenPointsShow(Scene):
    def construct(self):
        current_arcbetweenpoints = ArcBetweenPoints(start=LEFT,end=RIGHT)
        self.play(Create(current_arcbetweenpoints))
        self.wait(0.5)



        self.play(FadeOut(current_arcbetweenpoints))