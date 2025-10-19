from manim import *

class TextShow(Scene):
    def construct(self):
        # 添加参数显示文本
        param_text = Text("", font_size=24).to_edge(UP)
        self.add(param_text)
        
        # 存储上一次的参数
        prev_params = {}
        
        def update_params_display(new_params, changed_only=True):
            nonlocal prev_params
            
            if changed_only:
                # 只显示变化的参数
                changed_params = {}
                for key, value in new_params.items():
                    if key not in prev_params or prev_params[key] != value:
                        changed_params[key] = value
                
                if changed_params:
                    display_text = "当前设置: " + ", ".join([f"{k}: {v}" for k, v in changed_params.items()])
                else:
                    display_text = "参数返回"
            else:
                # 显示所有参数
                display_text = "当前设置: " + ", ".join([f"{k}: {v}" for k, v in new_params.items()])
            
            # 更新显示
            new_text = Text(display_text, font_size=24).to_edge(UP)
            self.play(Transform(param_text, new_text))
            
            # 更新上一次参数记录
            prev_params = new_params.copy()

        # 您的原始代码保持不变
        current_text = Text("Hello, Manim!", font_size=60)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 60}, changed_only=False)
        self.play(Write(current_text))
        self.wait(0.5)
        
        new_text = Text("Hello, Manim!", font_size=48)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=0.5)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 0.5})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,stroke_width=2)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "stroke_width": 2})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,stroke_width=2,stroke_color=YELLOW)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "stroke_width": 2, "stroke_color": "YELLOW"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,line_spacing=1.5)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "line_spacing": 1.5})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, \tManim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, \\tManim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, \tManim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,tab_width=2)
        update_params_display({"text": "\"Hello, \\tManim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "tab_width": 2})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,slant=ITALIC)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "slant": "ITALIC"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,slant=ITALIC,weight=BOLD)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "slant": "ITALIC", "weight": "BOLD"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, gradient=(YELLOW, RED),
                        fill_opacity=1.0,slant=ITALIC,weight=BOLD)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "gradient": "(YELLOW, RED)", "fill_opacity": 1.0, "slant": "ITALIC", "weight": "BOLD"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,t2c={"Manim": RED})
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "t2c": "{\"Manim\": RED}"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,t2f={"Manim": "sans-serif"})
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "t2f": "{\"Manim\": \"sans-serif\"}"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,t2w={"Manim": BOLD})
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "t2w": "{\"Manim\": BOLD}"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,t2s={"Manim": ITALIC})
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "t2s": "{\"Manim\": ITALIC}"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,t2g={"Manim": (YELLOW, RED)})
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "t2g": "{\"Manim\": (YELLOW, RED)}"})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,font="Comic Sans MS")
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "font": "\"Comic Sans MS\""})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!fi", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!fi\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!fi", font_size=48, color=BLUE,
                        fill_opacity=1.0,disable_ligatures=True)
        update_params_display({"text": "\"Hello, Manim!fi\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "disable_ligatures": True})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0, warn_missing_font=False)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "warn_missing_font": False})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,should_center=True)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "should_center": True})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,height=2.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "height": 2.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,width=2.0)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "width": 2.0})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        new_text = Text("Hello, Manim!", font_size=48, color=BLUE,
                        fill_opacity=1.0,use_svg_cache=False)
        update_params_display({"text": "\"Hello, Manim!\"", "font_size": 48, "color": "BLUE", "fill_opacity": 1.0, "use_svg_cache": False})
        self.play(ReplacementTransform(current_text, new_text))
        self.wait(0.5)
        current_text = new_text

        self.play(FadeOut(current_text))