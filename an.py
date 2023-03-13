from manimlib import *
class lim(Scene):
    def construct(self) -> None:
        self.add_sound("soul and mind.mp3")
        
        text_ = Tex("数列极限的定义")
        self.play(ShowCreation(text_))
        self.wait(2)
        self.play(Uncreate(text_))
        
        tex_1 = Tex("\\lim_{n \\to \\infty} a_n{}", color=BLUE_C).scale(2)
        self.play(ShowCreation(tex_1))
        self.wait(2)
        self.play(tex_1.animate.shift((UP)))
        self.wait(1)
        self.play(Uncreate(tex_1))

        axes = Axes((-1, 10, 0.5), (0, 7)).scale(1)
        self.play(ShowCreation(axes))
        self.wait()
        F = axes.get_graph(
            lambda x: 1 / x,
            color=BLUE_C,
            x_range=[0.1, 9]
        )
        x_label = axes.get_graph_label(F, Tex("1/x").scale(3))
        self.play(ShowCreation(F),
                  FadeIn(x_label, DOWN),
                  )
        self.wait()
        # self.play(FadeOut(F),FadeOut(x_label))
        self.wait()

        dot1 = Dot(color=RED)
        dot1_1 = Dot(color=RED)
        dot1.move_to((axes.c2p(0.5, 0)))
        dot1_1.move_to((axes.c2p(0.5, 2)))
        v_line = always_redraw(lambda: axes.get_v_line(dot1_1.get_bottom()))
        self.play(
            ShowCreation(dot1),
            ShowCreation(dot1_1),
            ShowCreation(v_line)
        )
        self.wait(1)

        dot2 = Dot(color=RED)
        dot2_1 = Dot(color=RED)
        dot2.move_to((axes.c2p(1, 0)))
        dot2_1.move_to((axes.c2p(1, 1)))
        v_line2 = always_redraw(lambda: axes.get_v_line(dot2_1.get_bottom()))
        self.play(
            ShowCreation(dot2),
            ShowCreation(dot2_1),
            ShowCreation(v_line2)
        )

        self.wait(1)

        dot3 = Dot(color=RED)
        dot3_1 = Dot(color=RED)
        dot3.move_to((axes.c2p(1.5, 0)))
        dot3_1.move_to((axes.c2p(1.5, 0.66)))
        v_line3 = always_redraw(lambda: axes.get_v_line(dot3_1.get_bottom()))
        self.play(
            ShowCreation(dot3),
            ShowCreation(dot3_1),
            ShowCreation(v_line3)
        )

        self.wait(1)

        dot4 = Dot(color=RED)
        dot4_1 = Dot(color=RED)
        dot4.move_to((axes.c2p(2, 0)))
        dot4_1.move_to((axes.c2p(2, 0.5)))
        v_line4 = always_redraw(lambda: axes.get_v_line(dot4_1.get_bottom()))
        self.play(
            ShowCreation(dot4),
            ShowCreation(dot4_1),
            ShowCreation(v_line4)
        )
        dot5 = Dot(color=RED)
        dot6 = Dot(color=RED)
        dot7 = Dot(color=RED)
        dot5_1 = Dot(color=RED)
        dot6_1 = Dot(color=RED)
        dot7_1 = Dot(color=RED)
        dot5.move_to(axes.c2p(2.5, 0.4))
        dot6.move_to(axes.c2p(3, 0.33))
        dot7.move_to(axes.c2p(3.5, 0.285))
        dot5_1.move_to(axes.c2p(2.5, 0))
        dot6_1.move_to(axes.c2p(3, 0))
        dot7_1.move_to(axes.c2p(3.5, 0))
        self.play(ShowCreation(dot5),
                  ShowCreation(dot6),
                  ShowCreation(dot7),
                  ShowCreation(dot5_1),
                  ShowCreation(dot6_1),
                  ShowCreation(dot7_1)
                  )
        self.wait(4)
        grp1 = VGroup(x_label, axes, dot1, dot1_1, dot2, dot2_1, dot3, dot3_1, dot4, dot4_1, dot5, dot5_1, dot6, dot6_1,
                      dot7, dot7_1, v_line, v_line2, v_line3, v_line4, F)
        self.play(FadeOut(grp1))
        self.wait(2)

        text1 = Text("从上面例子看出", font="Kai", color=BLUE_C)
        text2 = Text("随着x的增大，y的数值无限接近于0", font="Kai", color=BLUE_C).scale(0.8)
        text3 = Text("那么就说这个函数的极限是0", font="Kai", color=BLUE_C).scale(0.8)
        text4 = Text("那么在数学上又如何严格定义极限呢？", font="Kai", color=BLUE_C).scale(0.8)
        text5 = Text("继续看下一个例子", font="Kai", color=BLUE_C).scale(0.8)
        self.play(ShowCreation(text1))
        self.wait(2)
        self.play(Transform(text1, text2))
        self.wait(2)
        self.play(Transform(text1, text3))
        self.wait(2)
        self.play(Transform(text1, text4))
        self.wait(2)
        self.play(Transform(text1, text5))
        self.wait(2)

        tex1 = Tex("\\left \\{ a_n{} \\right \\} =\\left \\{ \\frac{(-1)^{n} }{n}  \\right \\} ", color=BLUE_C)
        tex1.to_edge(UP)
        self.play(ShowCreation(tex1),FadeOut(text1))
        self.wait(2)
        self.play(tex1.animate.shift(LEFT * 5))
        self.wait(2)
        tex2 = Tex(
            "\\begin{matrix} n & 1 & 2 & 3 & 4 &…… \\\\ a_n{}  & -1 & \\frac{1}{2}  & -\\frac{1}{3} & \\frac{1}{4} &……\\end{matrix}",
            color=BLUE_C).scale(0.8)
        tex2.to_edge(UP)

        self.play(ShowCreation(tex2))
        self.wait(1)
        self.play(tex2.animate.shift(RIGHT * 0.5))

        axes = Axes((0, 10, 1), (-1, 1, 0.5)).scale(1)
        # axes.add_coordinate_labels().scale(0.6)
        self.play(ShowCreation(axes))
        self.wait(1)

        dot = Dot(color=RED)
        dot.move_to(axes.c2p(0, 0))
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        )
        self.play(dot.animate.move_to(axes.c2p(1, -1)))
        dot2 = Dot(color=RED)
        dot2.move_to(axes.c2p(1, -1))
        self.add(dot2)
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(2, 0.5)))
        dot3 = Dot(color=RED)
        dot3.move_to(axes.c2p(2, 0.5))
        self.add(dot3)
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(3, -0.33)))
        dot4 = Dot(color=RED)
        dot4.move_to(axes.c2p(3, -0.33))
        self.add(dot4)
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(4, 0.25)))
        self.wait()

        dot5 = Dot(color=RED)
        dot5.move_to(axes.c2p(5, -0.2))
        dot6 = Dot(color=RED)
        dot6.move_to(axes.c2p(6, 0.167))
        self.play(FadeOut(h_line), FadeOut(v_line),
                  FadeIn(dot5), FadeIn(dot6),
                  )
        self.wait(2)
        text_1 = Text("从图像上看到，随着x增大，y的值逐渐接近x轴", font="Kai", color=BLUE_C).scale(0.6)
        text_2 = Text("可以猜测，数列的极限为0", font="Kai", color=BLUE_C).scale(0.6)
        text_3 = Text("在图像上看，an的值无限接近于0，也就是其极限为0", font="Kai", color=BLUE_C).scale(0.6)
        text_4 = Text("这就是说", font="Kai", color=BLUE_C).scale(0.6)
        tex3_1 = Tex("\\lim_{n \\to \\infty} \\frac{(-1)^{n} }{n} =0", color=PURPLE_B).scale(0.8)
        text_5 = Text("下面看看数学上的严格定义", font="Kai", color=BLUE_C).scale(0.6)
        text_1.to_edge(DOWN)
        self.play(ShowCreation(text_1))
        self.wait(1)
        text_2.to_edge(DOWN)
        self.play(Transform(text_1, text_2))
        self.wait()
        text_3.to_edge(DOWN)
        self.play(Transform(text_1, text_3))
        tex3_1.to_edge(DOWN)
        self.wait()
        text_4.to_edge(DOWN)
        self.play(Transform(text_1, text_4))
        self.wait()
        self.play(Transform(text_1, tex3_1))
        self.wait()
        text_5.to_edge(DOWN)
        self.play(Transform(text_1, text_5))
        self.wait(2)

        self.play(FadeOut(VGroup(text_1, axes, dot, dot2, dot3, dot4, dot5, dot6, tex1, tex2)))
        self.wait()

        text4_1 = Text("设an为一个数列，如果存在一个给定的实数L，对于任意给定的正实数 ε（无论大小）", font="Kai",
                       color=BLUE_B).scale(0.3)
        text4_2 = Text("总是存在一个正整数N，当n>N时，有", font="Kai", color=BLUE_B).scale(0.4)
        tex4_3 = Tex("\\left | a_n{} -L \\right | <\\varepsilon ", color=BLUE_B).scale(1.7)
        text4_4 = Text("那么就称实数L为数列an的极限，或是说an收敛于L，写作：", font="Kai", color=BLUE_B).scale(0.4)
        text4_5 = Tex("\\lim_{n \\to \\infty} a_n{} =L", color=BLUE_B).scale(1.7)
        grp4_1 = VGroup(text4_1, text4_2, tex4_3, text4_4, text4_5)
        grp4_1.arrange(DOWN, buff=1)
        self.play(ShowCreation(grp4_1, run_time=6))
        self.wait(6)
        text4_6 = Text("这看上去或许有些抽象", font="Kai", color=BLUE_B).scale(0.4)
        text4_7 = Text("我们再看一个例子", font="Kai", color=BLUE_B).scale(0.4)
        self.play(FadeOut(grp4_1), FadeIn(text4_6))
        self.wait()
        self.play(Transform(text4_6, text4_7))
        self.wait()

        axes5_1 = Axes((-1, 10, 0.5), (-1, 8, 1)).scale(0.6)

        self.play(ShowCreation(axes5_1),FadeOut(text4_6))
        self.wait()
        dot5_1 = Dot(color=PURPLE_A).scale(2)
        dot5_1.move_to(axes5_1.c2p(1, 7))

        dot5_2 = Dot(color=PURPLE_A).scale(2)
        dot5_2.move_to(axes5_1.c2p(2, 1.5))

        dot5_3 = Dot(color=PURPLE_A).scale(2)
        dot5_3.move_to(axes5_1.c2p(3, 6))

        dot5_4 = Dot(color=PURPLE_A).scale(2)
        dot5_4.move_to(axes5_1.c2p(4, 2.5))

        dot5_41 = Dot(color=PURPLE_A).scale(2)
        dot5_41.move_to(axes5_1.c2p(5, 5.5))

        dot5_5 = Dot(color=PURPLE_A).scale(2)
        dot5_5.move_to(axes5_1.c2p(6, 3.1))

        dot5_6 = Dot(color=PURPLE_A).scale(2)
        dot5_6.move_to(axes5_1.c2p(7, 5.1))

        dot5_7 = Dot(color=PURPLE_A).scale(2)
        dot5_7.move_to(axes5_1.c2p(8, 3.5))

        dot5_8 = Dot(color=PURPLE_A).scale(2)
        dot5_8.move_to(axes5_1.c2p(9, 4.9))

        dot5_9 = Dot(color=PURPLE_A).scale(2)
        dot5_9.move_to(axes5_1.c2p(10, 3.7))

        text5_1 = Text("在这个图像中，数列的极限可能是它", font="Kai", color=BLUE_C).scale(0.8)
        text5_2 = Text("也可能是它", font="Kai", color=BLUE_C).scale(0.8)
        text5_3 = Text("但最有可能的还是它", font="Kai", color=BLUE_C).scale(0.8)
        text5_1.to_edge(DOWN)
        text5_2.to_edge(DOWN)
        text5_3.to_edge(DOWN)

        self.play(FadeIn(VGroup(dot5_1, dot5_2, dot5_3, dot5_4, dot5_5, dot5_6, dot5_7, dot5_8, dot5_9, dot5_41)))
        self.wait(2)
        v_line5_1 = always_redraw(lambda: axes5_1.get_h_line(dot5_3.get_left()))
        v_line5_2 = always_redraw(lambda: axes5_1.get_h_line(dot5_7.get_left()))
        self.play(ShowCreation(v_line5_1), ShowCreation(text5_1))
        self.wait()
        self.play(ReplacementTransform(v_line5_1, v_line5_2), ReplacementTransform(text5_1, text5_2))
        self.wait(2)
        step_graph = axes5_1.get_graph(
            lambda x: 4.0,
            discontinuities=[3],
            color=GREEN,
        )

        self.play(FadeOut(v_line5_2), FadeIn(step_graph), ReplacementTransform(text5_2, text5_3))
        self.wait()
        step_label = axes5_1.get_graph_label(step_graph, Text("L"), x=4).next_to(step_graph)
        self.play(FadeIn(step_label))
        self.wait()

        step_graph5_2 = axes5_1.get_graph(
            lambda x: 5,
            discontinuities=[3],
            color=BLUE_C,
        )

        step_graph5_3 = axes5_1.get_graph(
            lambda x: 3,
            discontinuities=[3],
            color=BLUE_C,
        )

        text5_4 = Text("假设一个区间", font="Kai", color=BLUE_C).scale(0.8)
        text5_5 = Text("区间中划入了这些点", font="Kai", color=BLUE_C).scale(0.8)
        text5_4.to_edge(DOWN)
        text5_5.to_edge(DOWN)

        self.play(FadeIn(step_graph5_2), FadeIn(step_graph5_3), ReplacementTransform(text5_3, text5_4))
        self.wait(2)
        self.play(dot5_5.animate.set_color(YELLOW),
                  dot5_6.animate.set_color(YELLOW),
                  dot5_7.animate.set_color(YELLOW),
                  dot5_8.animate.set_color(YELLOW),
                  dot5_9.animate.set_color(YELLOW),
                  ReplacementTransform(text5_4, text5_5)

                  )
        self.wait(2)

        step_graph5_4 = axes5_1.get_graph(
            lambda x: 4.5,
            discontinuities=[3],
            color=BLUE_C,
        )

        step_graph5_5 = axes5_1.get_graph(
            lambda x: 3.5,
            discontinuities=[3],
            color=BLUE_C,
        )
        text5_6 = Text("区域中有无穷多个点，也可理解为", font="Kai", color=BLUE_C).scale(0.8)
        text5_6.to_edge(DOWN)

        self.play(ReplacementTransform(step_graph5_2, step_graph5_4),
                  ReplacementTransform(step_graph5_3, step_graph5_5),
                  ReplacementTransform(text5_5, text5_6,run_time=2))

        self.wait()

        text5_7 = Text("从某一个an开始后面的点都在区域内", font="Kai", color=BLUE_C).scale(0.8)
        text5_7.to_edge(DOWN)
        self.play(ReplacementTransform(text5_6, text5_7), dot5_5.animate.set_color(WHITE),
                  dot5_6.animate.set_color(WHITE),
                  dot5_7.animate.set_color(YELLOW),
                  dot5_8.animate.set_color(WHITE),
                  dot5_9.animate.set_color(YELLOW))
        self.wait()
        text5_8 = Text("以L为中心缩小区域", font="Kai", color=BLUE_C).scale(0.8)
        text5_8.to_edge(DOWN)
        text5_9 = Text("依旧有无穷多个点落在区域内", font="Kai", color=BLUE_C).scale(0.8)
        text5_9.to_edge(DOWN)
        text5_10 = Text("也依旧能找到一个an使得这个点之后的点都落在区域内", font="Kai", color=BLUE_C).scale(0.5)
        text5_10.to_edge(DOWN)
        text5_11 = Text("我们说L是这个数列的极限", font="Kai", color=BLUE_C).scale(0.8)
        text5_11.to_edge(DOWN)
        text5_12 = Text("这就是数学家给出的数列极限的定义", font="Kai", color=BLUE_C).scale(0.8)
        text5_12.to_edge(DOWN)

        self.play(ReplacementTransform(text5_7, text5_8,run_time=2))
        self.wait(1)

        self.play(ReplacementTransform(text5_8, text5_9,run_time=2))
        self.wait(1)

        self.play(ReplacementTransform(text5_9, text5_10,run_time=2))
        self.wait(1)

        self.play(ReplacementTransform(text5_10, text5_11,run_time=2))
        self.wait(1)

        self.play(ReplacementTransform(text5_11, text5_12,run_time=2))
        self.wait(1)