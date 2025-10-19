from manim import *

class RectangleShow(Scene):
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
        
        # 初始矩形
        current_Rectangle = Rectangle(width=2, height=1)
        update_params_display({"width": 2, "height": 1}, changed_only=False)
        self.play(Create(current_Rectangle))
        self.wait(0.5)

        # 高度变化
        new_Rectangle = Rectangle(width=2, height=3)
        update_params_display({"width": 2, "height": 3})
        self.play(ReplacementTransform(current_Rectangle, new_Rectangle))
        self.wait(0.5)
        current_Rectangle = new_Rectangle

        # 边框颜色变化
        new_Rectangle = Rectangle(width=2, height=3, color=BLUE)
        update_params_display({"width": 2, "height": 3, "color": "BLUE"})
        self.play(ReplacementTransform(current_Rectangle, new_Rectangle))
        self.wait(0.5)
        current_Rectangle = new_Rectangle

        # 填充透明度变化
        new_Rectangle = Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.5)
        update_params_display({"width": 2, "height": 3, "color": "BLUE", "fill_opacity": 0.5})
        self.play(ReplacementTransform(current_Rectangle, new_Rectangle))
        self.wait(0.5)
        current_Rectangle = new_Rectangle

        # 填充颜色变化
        new_Rectangle = Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E)
        update_params_display({"width": 2, "height": 3, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E"})
        self.play(ReplacementTransform(current_Rectangle, new_Rectangle))
        self.wait(0.5)
        current_Rectangle = new_Rectangle

        # 添加垂直网格线
        new_Rectangle = Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E, grid_xstep=0.5)
        update_params_display({"width": 2, "height": 3, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E", "grid_xstep": 0.5})
        self.play(ReplacementTransform(current_Rectangle, new_Rectangle))
        self.wait(0.5)
        current_Rectangle = new_Rectangle

        # 添加水平网格线
        new_Rectangle = Rectangle(width=2, height=3, color=BLUE, fill_opacity=0.5, fill_color=BLUE_E, grid_xstep=0.5, grid_ystep=0.5)
        update_params_display({"width": 2, "height": 3, "color": "BLUE", "fill_opacity": 0.5, "fill_color": "BLUE_E", "grid_xstep": 0.5, "grid_ystep": 0.5})
        self.play(ReplacementTransform(current_Rectangle, new_Rectangle))
        self.wait(0.5)
        current_Rectangle = new_Rectangle

        self.play(FadeOut(current_Rectangle))
        self.wait(0.5)