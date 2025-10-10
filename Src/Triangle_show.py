from manim import *

class TriangleShow(Scene):
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
                    display_text = "参数未变化"
            else:
                # 显示所有参数
                display_text = "当前设置: " + ", ".join([f"{k}: {v}" for k, v in new_params.items()])
            
            # 更新显示
            new_text = Text(display_text, font_size=24).to_edge(UP)
            self.play(Transform(param_text, new_text))
            
            # 更新上一次参数记录
            prev_params = new_params.copy()
        
        # 初始三角形
        current_triangle = Triangle()
        update_params_display({}, changed_only=False)
        self.play(Create(current_triangle))
        self.wait(0.5)

        # 边框颜色变化
        new_triangle = Triangle(color=BLUE)
        update_params_display({"color": "BLUE"})
        self.play(ReplacementTransform(current_triangle, new_triangle))
        self.wait(0.5)
        current_triangle = new_triangle

        # 填充透明度变化
        new_triangle = Triangle(color=BLUE, fill_opacity=0.5)
        update_params_display({"color": "BLUE", "fill_opacity": 0.5})
        self.play(ReplacementTransform(current_triangle, new_triangle))
        self.wait(0.5)
        current_triangle = new_triangle

        # 填充颜色变化
        new_triangle = Triangle(color=BLUE, fill_color=YELLOW, fill_opacity=0.5)
        update_params_display({"color": "BLUE", "fill_opacity": 0.5, "fill_color": "YELLOW"})
        self.play(ReplacementTransform(current_triangle, new_triangle))
        self.wait(0.5)
        current_triangle = new_triangle

        # 边框宽度变化
        new_triangle = Triangle(color=BLUE, fill_color=YELLOW, fill_opacity=0.5, stroke_width=10)
        update_params_display({"color": "BLUE", "fill_opacity": 0.5, "fill_color": "YELLOW", "stroke_width": 10})
        self.play(ReplacementTransform(current_triangle, new_triangle))
        self.wait(0.5)
        current_triangle = new_triangle

        self.play(FadeOut(current_triangle))
        self.wait(0.5)