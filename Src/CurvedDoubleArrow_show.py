from manim import *

class CurvedDoubleArrowShow(Scene):
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
        current_CurvedDoubleArrow = CurvedDoubleArrow(start_point=LEFT*2, end_point=RIGHT*2)
        update_params_display({"start_point": "LEFT*2", "end_point": "RIGHT*2"}, changed_only=False)
        self.play(Create(current_CurvedDoubleArrow))
        self.wait(0.5)

        new_CurvedDoubleArrow = CurvedDoubleArrow(start_point=LEFT*2, end_point=RIGHT*2, angle=PI/4)
        update_params_display({"start_point": "LEFT*2", "end_point": "RIGHT*2", "angle": "PI/4"})
        self.play(ReplacementTransform(current_CurvedDoubleArrow, new_CurvedDoubleArrow))
        self.wait(0.5)
        current_CurvedDoubleArrow = new_CurvedDoubleArrow

        new_CurvedDoubleArrow = CurvedDoubleArrow(start_point=LEFT*2, end_point=RIGHT*2, angle=PI/4,radius=4)
        update_params_display({"start_point": "LEFT*2", "end_point": "RIGHT*2", "angle": "PI/4", "radius": 4})
        self.play(ReplacementTransform(current_CurvedDoubleArrow, new_CurvedDoubleArrow))
        self.wait(0.5)
        current_CurvedDoubleArrow = new_CurvedDoubleArrow

        new_CurvedDoubleArrow = CurvedDoubleArrow(start_point=LEFT*2, end_point=RIGHT*2, angle=PI/4,radius=4,tip_shape_start=ArrowCircleTip)
        update_params_display({"start_point": "LEFT*2", "end_point": "RIGHT*2", "angle": "PI/4", "radius": 4, "tip_shape_start": "ArrowCircleTip"})
        self.play(ReplacementTransform(current_CurvedDoubleArrow, new_CurvedDoubleArrow))
        self.wait(0.5)
        current_CurvedDoubleArrow = new_CurvedDoubleArrow

        new_CurvedDoubleArrow = CurvedDoubleArrow(start_point=LEFT*2, end_point=RIGHT*2, angle=PI/4,radius=4,tip_shape_start=ArrowCircleTip,tip_shape_end=ArrowSquareTip)
        update_params_display({"start_point": "LEFT*2", "end_point": "RIGHT*2", "angle": "PI/4", "radius": 4, "tip_shape_start": "ArrowCircleTip", "tip_shape_end": "ArrowSquareTip"})
        self.play(ReplacementTransform(current_CurvedDoubleArrow, new_CurvedDoubleArrow))
        self.wait(0.5)
        current_CurvedDoubleArrow = new_CurvedDoubleArrow

        self.play(FadeOut(current_CurvedDoubleArrow))