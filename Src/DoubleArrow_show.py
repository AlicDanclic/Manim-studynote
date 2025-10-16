from manim import *

class DoubleArrowShow(Scene):
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
        
        # 初始双箭头（使用默认参数）
        current_doublearrow = DoubleArrow()
        update_params_display({}, changed_only=False)
        self.play(Create(current_doublearrow))
        self.wait(0.5)

        # stroke_width 变化
        new_doublearrow = DoubleArrow(stroke_width=3)
        update_params_display({"stroke_width": 3})
        self.play(ReplacementTransform(current_doublearrow, new_doublearrow))
        current_doublearrow = new_doublearrow
        self.wait(0.5)

        # buff 变化
        new_doublearrow = DoubleArrow(stroke_width=3, buff=0.5)
        update_params_display({"buff": 0.5})
        self.play(ReplacementTransform(current_doublearrow, new_doublearrow))
        current_doublearrow = new_doublearrow
        self.wait(0.5)

        # max_tip_length_to_length_ratio 变化
        new_doublearrow = DoubleArrow(stroke_width=3, buff=0.5,
                                      max_tip_length_to_length_ratio=0.5)
        update_params_display({"max_tip_length_to_length_ratio": 0.5})
        self.play(ReplacementTransform(current_doublearrow, new_doublearrow))
        current_doublearrow = new_doublearrow
        self.wait(0.5)

        # max_stroke_width_to_length_ratio 变化
        new_doublearrow = DoubleArrow(stroke_width=3, buff=0.5,
                                      max_tip_length_to_length_ratio=0.5,
                                      max_stroke_width_to_length_ratio=2)
        update_params_display({"max_stroke_width_to_length_ratio": 2})
        self.play(ReplacementTransform(current_doublearrow, new_doublearrow))
        current_doublearrow = new_doublearrow
        self.wait(0.5)

        # tip_shape_end 变化
        new_doublearrow = DoubleArrow(stroke_width=3, buff=0.5,
                                      max_tip_length_to_length_ratio=0.5,
                                      max_stroke_width_to_length_ratio=2,
                                      tip_shape_end=ArrowSquareTip)
        update_params_display({"tip_shape_end": "ArrowSquareTip"})
        self.play(ReplacementTransform(current_doublearrow, new_doublearrow))
        current_doublearrow = new_doublearrow
        self.wait(0.5)

        # tip_shape_start 变化
        new_doublearrow = DoubleArrow(stroke_width=3, buff=0.5,
                                      max_tip_length_to_length_ratio=0.5,
                                      max_stroke_width_to_length_ratio=2,
                                      tip_shape_end=ArrowSquareTip,
                                      tip_shape_start=ArrowCircleTip)
        update_params_display({"tip_shape_start": "ArrowCircleTip"})
        self.play(ReplacementTransform(current_doublearrow, new_doublearrow))
        current_doublearrow = new_doublearrow
        self.wait(0.5)

        self.play(FadeOut(current_doublearrow))