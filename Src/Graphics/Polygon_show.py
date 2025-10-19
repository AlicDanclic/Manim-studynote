from manim import *
import numpy as np

class PolygonShow(Scene):
    def construct(self):
        # 创建参数显示文本 - 使用更明显的初始文本
        param_text = Text("参数显示区域", font_size=36, color=WHITE).to_edge(UP)
        self.add(param_text)
        
        # 存储上一次的参数
        prev_params = {}
        
        def update_params_display(new_params, polygon_type="普通多边形", changed_only=True):
            nonlocal prev_params, param_text
            
            # 添加多边形类型信息
            type_info = f"类型: {polygon_type}"
            
            if changed_only:
                # 只显示变化的参数
                changed_params = {}
                for key, value in new_params.items():
                    if key not in prev_params or prev_params[key] != value:
                        changed_params[key] = value
                
                if changed_params:
                    display_text = f"{type_info}\n当前设置: " + ", ".join([f"{k}: {v}" for k, v in changed_params.items()])
                else:
                    display_text = f"{type_info}\n参数未变化"
            else:
                # 显示所有参数
                display_text = f"{type_info}\n当前设置: " + ", ".join([f"{k}: {v}" for k, v in new_params.items()])
            
            # 创建新的文本对象
            new_text = Text(display_text, font_size=36, color=WHITE).to_edge(UP)
            
            # 使用Transform更新文本
            self.play(Transform(param_text, new_text))
            
            # 更新上一次参数记录
            prev_params = new_params.copy()
        
        # ========== 普通多边形部分 ==========
        
        # 初始三角形
        current_Polygon = Polygon(
            *[  # 三角形
                [0, 0, 0],
                [2, 0.5, 0],
                [1, 1.8, 0]
            ],
            color=ORANGE, fill_opacity=0.5
        )
        
        # 先显示初始参数
        update_params_display({
            "顶点数": 3,
            "color": "ORANGE",
            "fill_opacity": 0.5
        }, polygon_type="普通多边形", changed_only=False)
        
        self.play(Create(current_Polygon))
        self.wait(0.5)
        
        # 变换到四边形
        new_Polygon = Polygon(
            *[  # 四边形
                [0, 0, 0],
                [2, 0.3, 0],
                [1.8, 1.5, 0],
                [0.2, 1.7, 0]
            ],
            color=ORANGE, fill_opacity=0.5
        )
        
        update_params_display({"顶点数": 4}, polygon_type="普通多边形")
        self.play(ReplacementTransform(current_Polygon, new_Polygon))
        current_Polygon = new_Polygon
        self.wait(0.5)
    
        # 变换到六边形
        new_Polygon = Polygon(
            *[  # 六边形
                [0, 0, 0],
                [1.8, 0.4, 0],
                [2, 1.2, 0],
                [1.2, 2, 0],
                [0.3, 1.8, 0],
                [-0.5, 1, 0]
            ],
            color=ORANGE, fill_opacity=0.5
        )
        
        update_params_display({"顶点数": 6}, polygon_type="普通多边形")
        self.play(ReplacementTransform(current_Polygon, new_Polygon))
        current_Polygon = new_Polygon
        self.wait(0.5)

        # 变换到九边形
        new_Polygon = Polygon(
            *[  # 九边形
                [0, 0, 0],
                [1, 0.1, 0],
                [1.7, 0.5, 0],
                [2, 1.1, 0],
                [1.8, 1.7, 0],
                [1.2, 2, 0],
                [0.5, 1.8, 0],
                [0, 1.2, 0],
                [-0.4, 0.6, 0]
            ],
            color=ORANGE, fill_opacity=0.5
        )
        
        update_params_display({"顶点数": 9}, polygon_type="普通多边形")
        self.play(ReplacementTransform(current_Polygon, new_Polygon))
        current_Polygon = new_Polygon
        self.wait(0.5)
        
        self.play(FadeOut(current_Polygon))
        self.wait(0.5)
        
        # ========== 正多边形部分 ==========
        
        # 重置参数记录
        prev_params = {}
        
        # 初始正三角形
        current_RegularPolygon = RegularPolygon(
            n=3,
            color=ORANGE, fill_opacity=0.5
        )
        
        update_params_display({
            "边数": 3,
            "color": "ORANGE",
            "fill_opacity": 0.5
        }, polygon_type="正多边形", changed_only=False)
        
        self.play(Create(current_RegularPolygon))
        self.wait(0.5)

        # 变换到正四边形
        new_RegularPolygon = RegularPolygon(
            n=4,
            color=ORANGE, fill_opacity=0.5
        )
        
        update_params_display({"边数": 4}, polygon_type="正多边形")
        self.play(ReplacementTransform(current_RegularPolygon, new_RegularPolygon))
        current_RegularPolygon = new_RegularPolygon
        self.wait(0.5)

        # 变换到正六边形
        new_RegularPolygon = RegularPolygon(
            n=6,
            color=ORANGE, fill_opacity=0.5
        )
        
        update_params_display({"边数": 6}, polygon_type="正多边形")
        self.play(ReplacementTransform(current_RegularPolygon, new_RegularPolygon))
        current_RegularPolygon = new_RegularPolygon
        self.wait(0.5)

        # 变换到正九边形
        new_RegularPolygon = RegularPolygon(
            n=9,
            color=ORANGE, fill_opacity=0.5
        )
        
        update_params_display({"边数": 9}, polygon_type="正多边形")
        self.play(ReplacementTransform(current_RegularPolygon, new_RegularPolygon))
        current_RegularPolygon = new_RegularPolygon
        self.wait(0.5)
        
        self.play(FadeOut(current_RegularPolygon))
        self.wait(0.5)
        
        # ========== 参数变化演示 ==========
        
        # 重置参数记录
        prev_params = {}
        
        # 创建正五边形用于演示参数变化
        demo_polygon = RegularPolygon(
            n=5,
            color=BLUE,
            fill_opacity=0.7,
            stroke_width=4
        )
        
        update_params_display({
            "边数": 5,
            "color": "BLUE",
            "fill_opacity": 0.7,
            "stroke_width": 4
        }, polygon_type="正多边形", changed_only=False)
        
        self.play(Create(demo_polygon))
        self.wait(0.5)
        
        # 改变颜色
        new_demo_polygon = RegularPolygon(
            n=5,
            color=RED,
            fill_opacity=0.7,
            stroke_width=4
        )
        
        update_params_display({"color": "RED"}, polygon_type="正多边形")
        self.play(ReplacementTransform(demo_polygon, new_demo_polygon))
        demo_polygon = new_demo_polygon
        self.wait(0.5)
        
        # 改变填充透明度
        new_demo_polygon = RegularPolygon(
            n=5,
            color=RED,
            fill_opacity=0.3,
            stroke_width=4
        )
        
        update_params_display({"fill_opacity": 0.3}, polygon_type="正多边形")
        self.play(ReplacementTransform(demo_polygon, new_demo_polygon))
        demo_polygon = new_demo_polygon
        self.wait(0.5)
        
        # 改变边框宽度
        new_demo_polygon = RegularPolygon(
            n=5,
            color=RED,
            fill_opacity=0.3,
            stroke_width=8
        )
        
        update_params_display({"stroke_width": 8}, polygon_type="正多边形")
        self.play(ReplacementTransform(demo_polygon, new_demo_polygon))
        demo_polygon = new_demo_polygon
        self.wait(0.5)
        
        # 改变边数
        new_demo_polygon = RegularPolygon(
            n=8,
            color=RED,
            fill_opacity=0.3,
            stroke_width=8
        )
        
        update_params_display({"边数": 8}, polygon_type="正多边形")
        self.play(ReplacementTransform(demo_polygon, new_demo_polygon))
        demo_polygon = new_demo_polygon
        self.wait(0.5)
        
        self.play(FadeOut(demo_polygon), FadeOut(param_text))
        self.wait(0.5)