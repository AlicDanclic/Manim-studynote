from manim import *

class DashedLineShow(Scene):
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
        
        # 初始虚线（使用默认参数）
        current_dashedline = DashedLine()
        update_params_display({}, changed_only=False)
        self.play(Create(current_dashedline))
        self.wait(0.5)

        # dash_length 变化
        new_dashedline = DashedLine(dash_length=0.1)
        update_params_display({"dash_length": 0.1})
        self.play(ReplacementTransform(current_dashedline, new_dashedline))
        current_dashedline = new_dashedline
        self.wait(0.5)

        # dashed_ratio 变化
        new_dashedline = DashedLine(dash_length=0.1, dashed_ratio=0.6)
        update_params_display({"dash_length": 0.1, "dashed_ratio": 0.6})
        self.play(ReplacementTransform(current_dashedline, new_dashedline))
        current_dashedline = new_dashedline
        self.wait(0.5)

        # 淡出
        self.play(FadeOut(current_dashedline))