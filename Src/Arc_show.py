from manim import *

class ArcShow(Scene):
    def construct(self):
        # 创建参数显示文本
        param_text = Text("", font_size=24).to_edge(UP)
        self.add(param_text)
        
        # 创建TAU/PI关系说明文本
        relation_text = Text("TAU = 2 × PI", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Write(relation_text))
        
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
                    display_text = "当前设置: " + ", \n".join([f"{k}: {v}" for k, v in changed_params.items()])
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
        
        # 初始弧
        current_Arc = Arc()
        update_params_display({"radius": "1.0", "start_angle": "0", "angle": "PI/2"}, changed_only=False)
        self.play(Create(current_Arc))
        self.wait(0.5)

        # 半径变化
        new_Arc = Arc(radius=2.0) #更改半径
        update_params_display({"radius": "2.0"})
        self.play(ReplacementTransform(current_Arc, new_Arc))
        self.wait(0.5)
        current_Arc = new_Arc

        # 更改起始角度 - 使用TAU
        new_Arc = Arc(radius=2.0, start_angle=TAU/8) #更改起始角度
        update_params_display({"start_angle": "TAU/8"})
        self.play(ReplacementTransform(current_Arc, new_Arc))
        self.wait(0.5)
        current_Arc = new_Arc

        # 更改圆弧角度 - 使用TAU
        new_Arc = Arc(radius=2.0, start_angle=TAU/8, angle=TAU/2) #更改圆弧角度
        update_params_display({"angle": "TAU/2"})
        self.play(ReplacementTransform(current_Arc, new_Arc))
        self.wait(0.5)
        current_Arc = new_Arc
        
        # 测试PI和TAU的关系 - 使用PI
        new_Arc = Arc(radius=2.0, start_angle=PI/2,angle=TAU/2) #更改起始角度
        update_params_display({"start_angle": "PI/2"})
        self.play(ReplacementTransform(current_Arc, new_Arc))
        self.wait(0.5)
        current_Arc = new_Arc

        # 更改圆弧角度 - 使用PI
        new_Arc = Arc(radius=2.0, start_angle=PI/2, angle=3*PI/4) #更改圆弧角度
        update_params_display({"angle": "3*PI/4"})
        self.play(ReplacementTransform(current_Arc, new_Arc))
        self.wait(0.5)
        current_Arc = new_Arc

        # 展示TAU和PI的关系
        relation_text2 = Text("TAU = 2 × PI = 6.283...", font_size=24, color=YELLOW).to_edge(DOWN)
        self.play(Transform(relation_text, relation_text2))
        self.wait(1)
        
        # 创建一个完整的圆来展示TAU
        full_circle = Arc(radius=2.0, start_angle=0, angle=TAU, color=GREEN)
        update_params_display({"angle": "TAU (完整圆)"})
        self.play(ReplacementTransform(current_Arc, full_circle))
        self.wait(1)
        current_Arc = full_circle
        
        # 创建一个半圆来展示PI
        half_circle = Arc(radius=2.0, start_angle=0, angle=PI, color=RED)
        update_params_display({"angle": "PI (半圆)"})
        self.play(ReplacementTransform(current_Arc, half_circle))
        self.wait(1)
        current_Arc = half_circle

        self.play(FadeOut(current_Arc), FadeOut(relation_text))
        self.wait(0.5)