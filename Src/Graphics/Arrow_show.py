from manim import *

class ArrowShow(Scene):
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

        current_Arrow = Arrow()
        update_params_display({"stroke_width": "默认", "buff": "默认", "tip_shape": "默认"}, changed_only=False)
        self.play(Create(current_Arrow))
        self.wait(0.5)

        new_Arrow = Arrow(stroke_width=3)
        update_params_display({"stroke_width": 3})
        self.play(ReplacementTransform(current_Arrow, new_Arrow))
        self.wait(0.5)
        current_Arrow = new_Arrow
        
        new_Arrow = Arrow(stroke_width=3,buff=0.5)
        update_params_display({"stroke_width": 3, "buff": 0.5})
        self.play(ReplacementTransform(current_Arrow, new_Arrow))
        self.wait(0.5)
        current_Arrow = new_Arrow

        new_Arrow = Arrow(stroke_width=3,buff=0.5,
                          max_tip_length_to_length_ratio=2)
        update_params_display({"stroke_width": 3, "buff": 0.5, "max_tip_length_to_length_ratio": 2})
        self.play(ReplacementTransform(current_Arrow, new_Arrow))
        self.wait(0.5)
        current_Arrow = new_Arrow

        new_Arrow = Arrow(stroke_width=3,buff=0.5,
                          max_tip_length_to_length_ratio=0.5,
                          max_stroke_width_to_length_ratio=2,
                          tip_shape=ArrowSquareFilledTip)
        update_params_display({
            "stroke_width": 3, "buff": 0.5, 
            "max_tip_length_to_length_ratio": 0.5,
            "max_stroke_width_to_length_ratio": 2,
            "tip_shape": "ArrowSquareFilledTip"
        })
        self.play(ReplacementTransform(current_Arrow, new_Arrow))
        self.wait(0.5)
        current_Arrow = new_Arrow

        new_Arrow = Arrow(stroke_width=3,buff=0.5,
                          max_tip_length_to_length_ratio=0.5,
                          max_stroke_width_to_length_ratio=2,
                          tip_shape=ArrowCircleTip)
        update_params_display({
            "stroke_width": 3, "buff": 0.5, 
            "max_tip_length_to_length_ratio": 0.5,
            "max_stroke_width_to_length_ratio": 2,
            "tip_shape": "ArrowCircleTip"
        })
        self.play(ReplacementTransform(current_Arrow, new_Arrow))
        self.wait(0.5)
        current_Arrow = new_Arrow

        new_Arrow = Arrow(stroke_width=3,buff=0.5,
                          max_tip_length_to_length_ratio=0.5,
                          max_stroke_width_to_length_ratio=2,
                          tip_shape=ArrowCircleFilledTip)
        update_params_display({
            "stroke_width": 3, "buff": 0.5, 
            "max_tip_length_to_length_ratio": 0.5,
            "max_stroke_width_to_length_ratio": 2,
            "tip_shape": "ArrowCircleFilledTip"
        })
        self.play(ReplacementTransform(current_Arrow, new_Arrow))
        self.wait(0.5)
        current_Arrow = new_Arrow

        new_Arrow = Arrow(stroke_width=3,buff=0.5,
                          max_tip_length_to_length_ratio=0.5,
                          max_stroke_width_to_length_ratio=2,
                          tip_shape=ArrowSquareTip)
        update_params_display({
            "stroke_width": 3, "buff": 0.5, 
            "max_tip_length_to_length_ratio": 0.5,
            "max_stroke_width_to_length_ratio": 2,
            "tip_shape": "ArrowSquareTip"
        })
        self.play(ReplacementTransform(current_Arrow, new_Arrow))
        self.wait(0.5)
        current_Arrow = new_Arrow

        new_Arrow = Arrow(stroke_width=3,buff=0.5,
                          max_tip_length_to_length_ratio=0.5,
                          max_stroke_width_to_length_ratio=2,
                          tip_shape=ArrowTriangleTip)
        update_params_display({
            "stroke_width": 3, "buff": 0.5, 
            "max_tip_length_to_length_ratio": 0.5,
            "max_stroke_width_to_length_ratio": 2,
            "tip_shape": "ArrowTriangleTip"
        })
        self.play(ReplacementTransform(current_Arrow, new_Arrow))
        self.wait(0.5)
        current_Arrow = new_Arrow

        self.play(FadeOut(current_Arrow))