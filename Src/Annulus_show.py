from manim import *

class AnnulusShow(Scene):
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

        current_Annulus = Annulus()
        update_params_display({"outer_radius": "默认", "inner_radius": "默认"}, changed_only=False)
        self.play(Create(current_Annulus))
        self.wait(0.5)

        new_Annulus = Annulus(outer_radius=1.5)
        update_params_display({"outer_radius": 1.5})
        self.play(ReplacementTransform(current_Annulus, new_Annulus))
        current_Annulus = new_Annulus
        self.wait(0.5)

        new_Annulus = Annulus(outer_radius=1.5,inner_radius=0.5)
        update_params_display({"outer_radius": 1.5, "inner_radius": 0.5})
        self.play(ReplacementTransform(current_Annulus, new_Annulus))
        current_Annulus = new_Annulus
        self.wait(0.5)
        
        new_Annulus = Annulus(outer_radius=1.5,inner_radius=0.5,
                              fill_opacity=0.5)
        update_params_display({"outer_radius": 1.5, "inner_radius": 0.5, "fill_opacity": 0.5})
        self.play(ReplacementTransform(current_Annulus, new_Annulus))
        current_Annulus = new_Annulus
        self.wait(0.5)

        new_Annulus = Annulus(outer_radius=1.5,inner_radius=0.5,
                              fill_opacity=0.5, color=BLUE)
        update_params_display({"outer_radius": 1.5, "inner_radius": 0.5, "fill_opacity": 0.5, "color": "BLUE"})
        self.play(ReplacementTransform(current_Annulus, new_Annulus))
        current_Annulus = new_Annulus
        self.wait(0.5)

        new_Annulus = Annulus(outer_radius=1.5,inner_radius=0.5,
                              fill_opacity=0.5, color=BLUE,
                              stroke_width=0.5)
        update_params_display({"outer_radius": 1.5, "inner_radius": 0.5, "fill_opacity": 0.5, "color": "BLUE", "stroke_width": 0.5})
        self.play(ReplacementTransform(current_Annulus, new_Annulus))
        current_Annulus = new_Annulus
        self.wait(0.5)

        new_Annulus = Annulus(outer_radius=1.5,inner_radius=0.5,
                              fill_opacity=0.5, color=BLUE,
                              stroke_width=0.5,mark_paths_closed=True)
        update_params_display({
            "outer_radius": 1.5, "inner_radius": 0.5, "fill_opacity": 0.5, "color": "BLUE", 
            "stroke_width": 0.5, "mark_paths_closed": True
        })
        self.play(ReplacementTransform(current_Annulus, new_Annulus))
        current_Annulus = new_Annulus
        self.wait(0.5)

        self.play(FadeOut(current_Annulus))