from manim import *

class CircleShow(Scene):
    def construct(self):
        # 创建参数显示文本
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
        
        # 初始圆
        circle = Circle(radius=1)
        update_params_display({"radius": 1}, changed_only=False)
        self.play(Create(circle))
        self.wait(0.5)

        # 半径变化
        new_circle = Circle(radius=2)
        update_params_display({"radius": 2})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 边框颜色变化
        new_circle = Circle(radius=2, color=BLUE)
        update_params_display({"radius": 2, "color": "BLUE"})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)
        
        # 填充透明度变化
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 填充颜色变化
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E"})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 中心位置变化
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E, arc_center=UP)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E", "arc_center": "UP"})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 返回中心
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E"})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 贝塞尔曲线段数变化
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E, num_components=3)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E", "num_components": 3})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 返回
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E"})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 描边属性变化
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E,
                           stroke_color=RED, stroke_opacity=0.5, stroke_width=1)
        update_params_display({
            "radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E",
            "stroke_color": "RED", "stroke_opacity": 0.5, "stroke_width": 1
        })
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)
        
        # 返回
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E"})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 背景描边变化
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E,
                           background_stroke_color=RED, background_stroke_opacity=0.5, background_stroke_width=1)
        update_params_display({
            "radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E",
            "background_stroke_color": "RED", "background_stroke_opacity": 0.5, "background_stroke_width": 1
        })
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 返回
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E"})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 光泽效果变化
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E,
                           sheen_factor=0.5, sheen_direction=UP+LEFT)
        update_params_display({
            "radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E",
            "sheen_factor": 0.5, "sheen_direction": "UP+LEFT"
        })
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 返回
        new_circle = Circle(radius=2, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E)
        update_params_display({"radius": 2, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E"})
        self.play(ReplacementTransform(circle, new_circle))
        circle = new_circle
        self.wait(0.5)

        # 淡出
        self.play(FadeOut(circle))
        self.wait(0.5)
