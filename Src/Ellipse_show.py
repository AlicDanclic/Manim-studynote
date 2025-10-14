from manim import *

class EllipseShow(Scene):
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

        current_ellipse = Ellipse()
        update_params_display({"width": "默认", "height": "默认"}, changed_only=False)
        self.play(Create(current_ellipse))
        self.wait(0.5)

        new_ellipse = Ellipse(width=4)
        update_params_display({"width": 4})
        self.play(ReplacementTransform(current_ellipse, new_ellipse))
        current_ellipse = new_ellipse
        self.wait(0.5)

        new_ellipse = Ellipse(width=4, height=2)
        update_params_display({"width": 4, "height": 2})
        self.play(ReplacementTransform(current_ellipse, new_ellipse))
        current_ellipse = new_ellipse
        self.wait(0.5)

        self.play(FadeOut(current_ellipse))