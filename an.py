from manimlib import *
class lim(Scene):
    def construct(self) -> None:
        self.add_sound("D:\\manim\\manim-master\\venv\\music.mp3")  #加背景音乐
        text0 = Text("Definition of Series Limits", color=PURPLE_A) #视频标题内容
        tex_1 = Tex("\\lim_{n \\to \\infty} a_{n}", color=BLUE_C).scale(2) #极限表达式
        self.play(Write(text0)) #写字一样显示text0
        self.wait() #等一秒
        self.play(FadeOut(text0)) #text0逐渐消失
        self.play(ShowCreation(tex_1)) #tex_1出现
        self.wait(2) #等两秒
        self.play(tex_1.animate.shift((UP))) #tex_1向上移动一下
        self.wait(1) #等一秒
        self.play(Uncreate(tex_1)) #tex_1消失

        axes = Axes((-1, 10, 0.5), (0, 7)).scale(1) #定义一个坐标轴，横轴范围[-1, 10]间隔0.5，纵轴范围[0, 7]间隔默认1，整体大小为“1”
        self.play(ShowCreation(axes)) #显示定义的坐标轴
        self.wait() #等一秒
        F1 = axes.get_graph(
            lambda x: 1 / x,
            color=BLUE_C,
            x_range=[0.1, 0.2]
        ) #定义坐标轴上的函数1/x，定义域为[0.1, 0.2]，颜色为蓝色
        F2 = axes.get_graph(
            lambda x: 1 / x,
            color=BLUE_C,
            x_range=[0.2, 10]
        )#定义坐标轴上的函数1/x，定义域为[0.2, 10]，颜色为蓝色
        x_label = axes.get_graph_label(F1, Tex("1/x").scale(3)) #定义函数的标签“1/x”，大小为“3”
        self.play(ShowCreation(F1), ShowCreation(F2),
                  FadeIn(x_label, DOWN),
                  ) #展示定义的函数和标签
        self.wait(2) #等两秒
        # self.play(FadeOut(F),FadeOut(x_label))

        dot1 = Dot(color=WHITE) #定义一个白色的点
        dot1_1 = Dot(color=WHITE) #定义一个白色的点
        dot1.move_to((axes.c2p(0.5, 0))) #定义点的位置（c2p是coords_to_point的缩写）
        dot1_1.move_to((axes.c2p(0.5, 2))) #定义点的位置
        v_line = always_redraw(lambda: axes.get_v_line(dot1_1.get_bottom())) #定义一条直线，从点dot1_1到x轴的垂线
        self.play(
            ShowCreation(dot1),
            ShowCreation(dot1_1),
            ShowCreation(v_line)
        ) #显示定义的点和直线
        self.wait(1) #等一秒

        dot2 = Dot(color=WHITE) #定义一个白色的点
        dot2_1 = Dot(color=WHITE) #定义一个白色的点
        dot2.move_to((axes.c2p(1, 0))) #定义点的位置（c2p是coords_to_point的缩写）
        dot2_1.move_to((axes.c2p(1, 1))) #定义点的位置
        v_line2 = always_redraw(lambda: axes.get_v_line(dot2_1.get_bottom())) #定义一条直线，从点dot2_1到x轴的垂线
        self.play(
            ShowCreation(dot2),
            ShowCreation(dot2_1),
            ShowCreation(v_line2)
        ) #显示定义的点和直线
        self.wait(1) #等一秒

        dot3 = Dot(color=WHITE) #定义一个白色的点
        dot3_1 = Dot(color=WHITE) #定义一个白色的点
        dot3.move_to((axes.c2p(1.5, 0))) #定义点的位置（c2p是coords_to_point的缩写）
        dot3_1.move_to((axes.c2p(1.5, 0.66))) #定义点的位置
        v_line3 = always_redraw(lambda: axes.get_v_line(dot3_1.get_bottom())) #定义一条直线，从点dot3_1到x轴的垂线
        self.play(
            ShowCreation(dot3),
            ShowCreation(dot3_1),
            ShowCreation(v_line3)
        ) #显示定义的点和直线
        self.wait(1)#等一秒

        dot4 = Dot(color=WHITE) #定义一个白色的点
        dot4_1 = Dot(color=WHITE) #定义一个白色的点
        dot4.move_to((axes.c2p(2, 0))) #定义点的位置（c2p是coords_to_point的缩写)
        dot4_1.move_to((axes.c2p(2, 0.5))) #定义点的位置
        v_line4 = always_redraw(lambda: axes.get_v_line(dot4_1.get_bottom())) #定义一条直线，从点dot4_1到x轴的垂线
        self.play(
            ShowCreation(dot4),
            ShowCreation(dot4_1),
            ShowCreation(v_line4)
        ) #显示定义的点和直线
        dot5 = Dot(color=WHITE) #定义一个白色的点
        dot6 = Dot(color=WHITE) #定义一个白色的点
        dot7 = Dot(color=WHITE) #定义一个白色的点
        dot5_1 = Dot(color=WHITE) #定义一个白色的点
        dot6_1 = Dot(color=WHITE) #定义一个白色的点
        dot7_1 = Dot(color=WHITE) #定义一个白色的点
        dot5.move_to(axes.c2p(2.5, 0.4)) #定义点的位置
        dot6.move_to(axes.c2p(3, 0.33)) #定义点的位置
        dot7.move_to(axes.c2p(3.5, 0.285)) #定义点的位置
        dot5_1.move_to(axes.c2p(2.5, 0)) #定义点的位置
        dot6_1.move_to(axes.c2p(3, 0)) #定义点的位置
        dot7_1.move_to(axes.c2p(3.5, 0)) #定义点的位置
        self.play(ShowCreation(dot5),
                  ShowCreation(dot6),
                  ShowCreation(dot7),
                  ShowCreation(dot5_1),
                  ShowCreation(dot6_1),
                  ShowCreation(dot7_1)
                  ) #显示定义的点和直线
        self.wait(5) #等5秒
        grp1 = VGroup(x_label, axes, dot1, dot1_1, dot2, dot2_1, dot3, dot3_1, dot4, dot4_1, dot5, dot5_1, dot6, dot6_1,
                      dot7, dot7_1, v_line, v_line2, v_line3, v_line4, F1,F2) #将元素放进一个组合里面，便于集中处理
        self.play(FadeOut(grp1)) #grp1里面的元素逐渐消失
        self.wait(2) #等两秒

        text1 = Text("从上面例子看出", font="楷体", color=BLUE_C) #定义文本内容，字体，和大小
        text2_1 = Text("随着", font="楷体", color=BLUE_C).scale(0.8) #定义文本内容，字体，和大小
        text_2_2 = Tex("x", color=BLUE_C) #定义文本内容，字体，和大小
        text_2_3 = Text("的增大，", font="楷体", color=BLUE_C).scale(0.6) #定义文本内容，字体，和大小
        text_2_4 = Tex("y", color=BLUE_C) #定义文本内容，字体，和大小
        text_2_5_1 = Text("的数值无限接近于", font="楷体", color=BLUE_C).scale(0.6) #定义文本内容，字体，和大小
        text_2_5_2 = Tex("0", color=BLUE_C).scale(1.6) #定义文本内容，字体，和大小
        text_2_5 = VGroup(text_2_5_1, text_2_5_2) #将若干文本内容放进一个组合
        text_2_5.arrange(RIGHT) #组合中的元素后一个在前一个的右边

        text2 = VGroup(text2_1, text_2_2, text_2_3, text_2_4, text_2_5) #将若干文本内容放进一个组合
        text2.arrange(RIGHT) #组合中的元素后一个在前一个的右边

        text3_1 = Text("那么就说这个函数的极限是", font="楷体", color=BLUE_C).scale(0.8) #定义文本内容，字体，和大小
        text3_2 = Tex("0", color=BLUE_C).scale(1.8) #定义文本内容，字体，和大小
        text3 = VGroup(text3_1, text3_2).arrange(RIGHT) #将若干文本放进一个组合，并且后一个元素在前一个元素的右边
        text4 = Text("那么在数学上又严格定义极限呢？", font="楷体", color=BLUE_C).scale(0.8) #定义文本内容，字体，和大小
        text5 = Text("继续看下一个例子", font="楷体", color=BLUE_C).scale(0.8) #定义文本内容，字体，和大小
        self.play(ShowCreation(text1)) #显示文本
        self.wait(2) #等两秒
        self.play(Transform(text1, text2)) #前一个文本转换成后一个文本
        self.wait(2) #等两秒
        self.play(Transform(text1, text3)) #前一个文本转换成后一个文本
        self.wait(2) #等两秒
        self.play(Transform(text1, text4)) #前一个文本转换成后一个文本
        self.wait(2) #等两秒
        self.play(Transform(text1, text5)) #前一个文本转换成后一个文本
        self.wait(2) #等两秒

        tex1 = Tex("\\left \\{ a_{n} \\right \\} =\\left \\{ \\frac{(-1)^{n} }{n}  \\right \\} ", color=BLUE_C) #定义LaTeX文本内容和颜色
        tex1.to_edge(UP) #定义文本tex1的位置：上方边缘
        self.play(ShowCreation(tex1),FadeOut(text1)) #tex1出现，text1逐渐消失
        self.wait(2) #等两秒
        self.play(tex1.animate.shift(LEFT * 5)) #tex1向左移动某个距离(需要自己调试)
        self.wait(2) #等两秒
        tex2 = Tex(
            "\\begin{matrix} n & 1 & 2 & 3 & 4 &…… \\\\ a_{n}  & -1 & \\frac{1}{2}  & -\\frac{1}{3} & \\frac{1}{4} &……\\end{matrix}",
            color=BLUE_C).scale(0.8) #定义LaTeX文本内容，颜色，和大小
        tex2.to_edge(UP) #定义文本tex2的位置：上方边缘

        self.play(ShowCreation(tex2)) #显示tex2
        self.wait(1) #等一秒
        self.play(tex2.animate.shift(RIGHT * 0.5)) #tex2向右移动某个距离(需要自己调试)

        axes = Axes((0, 10, 1), (-1, 1, 0.5)).scale(1) #定义坐标轴，x轴范围[0, 10]间隔为1，y轴范围为[-1, 1]间隔为0.5
        # axes.add_coordinate_labels().scale(0.6)
        self.play(ShowCreation(axes)) #显示定义的坐标轴
        self.wait(3) #等三秒

        dot = Dot(color=WHITE) #定义一个白色的点点
        dot.move_to(axes.c2p(0, 0)) #定义白点的位置
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left())) #定义一条从白点到左的线，也就是到y轴的垂线
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom())) #定义一条从白点到下的线，也就是到x轴的垂线
        self.play(
            ShowCreation(h_line),
            ShowCreation(v_line),
        ) #显示定义的两条线
        self.play(dot.animate.move_to(axes.c2p(1, -1))) #显示白点移动到指定坐标的动画
        dot2 = Dot(color=WHITE) #定义一个白点
        dot2.move_to(axes.c2p(1, -1)) #定义白点的坐标
        self.add(dot2) #在图上显示定义的点
        self.wait() #等一秒
        self.play(dot.animate.move_to(axes.c2p(2, 0.5))) #显示白点移动到指定坐标的动画
        dot3 = Dot(color=WHITE) #定义一个白点
        dot3.move_to(axes.c2p(2, 0.5)) #定义白点的坐标
        self.add(dot3) #在图上显示定义的点
        self.wait() #等一秒
        self.play(dot.animate.move_to(axes.c2p(3, -0.33))) #显示白点移动到指定坐标的动画
        dot4 = Dot(color=WHITE) #定义一个白点
        dot4.move_to(axes.c2p(3, -0.33)) #定义白点的坐标
        self.add(dot4) #在图上显示定义的点
        self.wait() #等一秒
        self.play(dot.animate.move_to(axes.c2p(4, 0.25))) #显示白点移动到指定坐标的动画
        self.wait() #等一秒

        dot5 = Dot(color=WHITE) #定义一个白点
        dot5.move_to(axes.c2p(5, -0.2)) #定义白点的坐标
        dot6 = Dot(color=WHITE) #定义一个白点
        dot6.move_to(axes.c2p(6, 0.167)) #定义白点的坐标
        self.play(FadeOut(h_line), FadeOut(v_line),
                  FadeIn(dot5), FadeIn(dot6),
                  ) #定义的两条线逐渐消失，定义的两个点逐渐出现
        self.wait(2) #等两秒
        text_1_1 = Text("从图像上看到，随着", font="楷体", color=BLUE_C).scale(0.6) #定义文本的内容，字体，颜色和大小
        text_1_2 = Tex("x", color=BLUE_C) #定义LaTeX文本的内容和颜色
        text_1_3 = Text("增大，", font="楷体", color=BLUE_C).scale(0.6) #定义文本的内容，字体，颜色和大小
        text_1_4 = Tex("y", color=BLUE_C) #定义LaTeX文本的内容和颜色
        text_1_5 = Text("的值逐渐接近", font="楷体", color=BLUE_C).scale(0.6) #定义文本的内容，字体，颜色和大小
        text_1_6 = Tex("x", color=BLUE_C) #定义LaTeX文本的内容和颜色
        text_1_7 = Text("轴", font="楷体", color=BLUE_C).scale(0.6) #定义文本的内容，字体，颜色和大小
        text_1 = VGroup(text_1_1, text_1_2, text_1_3, text_1_4, text_1_5, text_1_6, text_1_7) #将指定文本放进一个组合
        text_1.arrange(RIGHT) #组合的后一个元素在前一个元素的右边
        text_2_1 = Text("可以猜测，数列的极限为", font="楷体", color=BLUE_C).scale(0.6) #定义文本的内容，字体，颜色和大小
        text_2_2 = Tex("0",color=BLUE_C).scale(1.6) #定义LaTeX文本的内容和颜色
        text_2 = VGroup(text_2_1,text_2_2).arrange(RIGHT) #将指定文本放进一个组合，组合的后一个元素在前一个元素的右边

        text_3_1 = Text("在图像上看，数列的值无限接近于", font="楷体", color=BLUE_C).scale(0.5) #定义文本的内容，字体，颜色和大小
        text3_2 = Tex("0", color=BLUE_C).scale(1) #定义LaTeX文本的内容和颜色
        text3_3 = Text("，也就是其极限为", font="楷体", color=BLUE_C).scale(0.5) #定义文本的内容，字体，颜色和大小
        text3_4 = Tex("0", color=BLUE_C).scale(1) #定义LaTeX文本的内容和颜色
        text_3 = VGroup(text_3_1, text3_2, text3_3, text3_4).arrange(RIGHT) #将指定文本放进一个组合，组合的后一个元素在前一个元素的右边


        text_4 = Text("这就是说", font="楷体", color=BLUE_C).scale(0.6) #定义文本的内容，字体，颜色和大小
        tex3_1 = Tex("\\lim_{n \\to \\infty} \\frac{(-1)^{n} }{n} =0", color=PURPLE_B).scale(0.8) #定义LaTeX文本的内容，颜色和大小
        text_5 = Text("下面看看数学上的严格定义", font="楷体", color=BLUE_C).scale(0.6) #定义文本的内容，字体，颜色和大小
        text_1.to_edge(DOWN) #定义文本的位置：下方边缘
        self.play(ShowCreation(text_1)) #显示文本
        self.wait(1) #等一秒
        text_2.to_edge(DOWN) #定义文本的位置：下方边缘
        self.play(Transform(text_1, text_2)) #前一个文本转化成后一个文本
        self.wait() #等一秒
        text_3.to_edge(DOWN) #定义文本的位置：下方边缘
        self.play(Transform(text_1, text_3)) #前一个文本转化成后一个文本
        tex3_1.to_edge(DOWN) #定义文本的位置：下方边缘
        self.wait() #等一秒
        text_4.to_edge(DOWN) #定义文本的位置：下方边缘
        self.play(Transform(text_1, text_4)) #前一个文本转化成后一个文本
        self.wait() #等一秒
        self.play(Transform(text_1, tex3_1)) #前一个文本转化成后一个文本
        self.wait() #等一秒
        text_5.to_edge(DOWN) #定义文本的位置：下方边缘
        self.play(Transform(text_1, text_5)) #前一个文本转化成后一个文本
        self.wait(2) #等两秒

        self.play(FadeOut(VGroup(text_1, axes, dot, dot2, dot3, dot4, dot5, dot6, tex1, tex2))) #组合内元素整体消失
        self.wait() #等一秒

        text4_1 = Tex(
            "For \ \    series \ \   a_{n} , \ \  if \ \  there  \ \  is \ \  a \ \  L  \ \  given,  \ \  for  \ \  any  \ \  given  \ \  positive \ \ \epsilon",
            color=BLUE_B).scale(0.9) #定义LaTeX文本的内容，颜色和大小
        text4_2 = Tex(" A\ \ positive\ \ N \ \ can \ \ always\ \ be \ \ found\ \ when\ \ n \ \ \\textgreater \ \ N :",
                      color=BLUE_B).scale(0.9) #定义LaTeX文本的内容，颜色和大小
        tex4_3 = Tex("\\left | a_{n} -L \\right | \\textless \\varepsilon ", color=BLUE_B).scale(1.7) #定义LaTeX文本的内容，颜色和大小
        text4_4 = Tex(
            "Then \ \ we \ \ say\ \ the\ \ limit\ \ of\ \ a_{n}\ \  is\ \ L,\ \ which\ \ means\ \ a_{n}\ \ converges\ \  to \ \ L",
            color=BLUE_B).scale(0.8) #定义LaTeX文本的内容，颜色和大小
        text4_5 = Tex("\\lim_{n \\to \\infty} a_{n} =L", color=BLUE_B).scale(1.7) #定义LaTeX文本的内容，颜色和大小
        grp4_1 = VGroup(text4_1, text4_2, tex4_3, text4_4, text4_5) #将指定元素放进一个组合
        grp4_1.arrange(DOWN, buff=1) #组合中后一个元素在前一个元素的下方，距离为"1"(可以根据情况自己调试)
        self.play(ShowCreation(grp4_1, run_time=6)) #展示组合的元素，一共6秒
        self.wait(6) #等六秒
        text4_6 = Text("如果你觉得这个还很抽象", font="楷体", color=BLUE_C).scale(0.8) #定义文本内容，字体，颜色和大小
        text4_7 = Text("继续看看下面这个例子", font="楷体", color=BLUE_C).scale(0.8) #定义文本内容，字体，颜色和大小
        self.play(FadeOut(grp4_1), FadeIn(text4_6)) #指定组合消失，指定文本出现
        self.wait(2) #等两秒
        self.play(Transform(text4_6, text4_7)) #前一个文本转化成后一个文本
        self.wait(2) #等两秒

        axes5_1 = Axes((-1, 10, 0.5), (-1, 8, 1)).scale(0.6) #定义一个坐标轴，x轴范围[-1, 10]间隔为0.5， y轴为[-1. 8]间隔为1，大小为"0.6"

        self.play(ShowCreation(axes5_1),FadeOut(text4_6)) #显示坐标轴，指定文本消失
        self.wait() #等一秒
        dot5_1 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_1.move_to(axes5_1.c2p(1, 7)) #定义点的坐标

        dot5_2 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_2.move_to(axes5_1.c2p(2, 1.5)) #定义点的坐标

        dot5_3 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_3.move_to(axes5_1.c2p(3, 6)) #定义点的坐标

        dot5_4 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_4.move_to(axes5_1.c2p(4, 2.5)) #定义点的坐标

        dot5_41 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_41.move_to(axes5_1.c2p(5, 5.5)) #定义点的坐标

        dot5_5 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_5.move_to(axes5_1.c2p(6, 3.1)) #定义点的坐标

        dot5_6 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_6.move_to(axes5_1.c2p(7, 5.1)) #定义点的坐标

        dot5_7 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_7.move_to(axes5_1.c2p(8, 3.5)) #定义点的坐标

        dot5_8 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_8.move_to(axes5_1.c2p(9, 4.9)) #定义点的坐标

        dot5_9 = Dot(color=WHITE).scale(2) #定义一个点的颜色和大小
        dot5_9.move_to(axes5_1.c2p(10, 3.7)) #定义点的坐标

        text5_1_1 = Text("这个图像中，数列极限明显不是", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_1_2 = Tex("6", color=BLUE_C).scale(1.6) #定义LaTeX文本的内容，颜色和大小
        text5_1 = VGroup(text5_1_1, text5_1_2).arrange(RIGHT) #将若干元素放进一个组合，组合中后一个元素在前一个元素右边
        text5_2_1 = Text("也不是", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_2_2 = Tex("3.5", color=BLUE_C).scale(1.6) #定义LaTeX文本的内容，颜色和大小
        text5_2 = VGroup(text5_2_1, text5_2_2).arrange(RIGHT) #将若干元素放进一个组合，组合中后一个元素在前一个元素右边
        text5_3_1 = Text("答案是它——", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_3_2 = Tex("4", color=BLUE_C).scale(1.6) #定义LaTeX文本的内容，颜色和大小
        text5_3 = VGroup(text5_3_1, text5_3_2).arrange(RIGHT) #将若干元素放进一个组合，组合中后一个元素在前一个元素右边
        text5_1.to_edge(DOWN) #定义文本的位置：下方边缘
        text5_2.to_edge(DOWN) #定义文本的位置：下方边缘
        text5_3.to_edge(DOWN) #定义文本的位置：下方边缘

        self.play(FadeIn(VGroup(dot5_1, dot5_2, dot5_3, dot5_4, dot5_5, dot5_6, dot5_7, dot5_8, dot5_9, dot5_41))) #一起展示组合中的元素
        self.wait(2) #等两秒
        v_line5_1 = always_redraw(lambda: axes5_1.get_h_line(dot5_3.get_left())) #定义从dot5_3到y轴的垂线
        v_line5_2 = always_redraw(lambda: axes5_1.get_h_line(dot5_7.get_left())) #定义从dot5_3到y轴的垂线
        self.play(ShowCreation(v_line5_1), ShowCreation(text5_1)) #显示定义的两条垂线
        self.wait() #等一秒
        self.play(ReplacementTransform(v_line5_1, v_line5_2), ReplacementTransform(text5_1, text5_2)) #ReplacementTransform函数中，前一个元素转化成后一个元素
        self.wait(2) #等两秒
        step_graph = axes5_1.get_graph(
            lambda x: 4.0,
            discontinuities=[3],
            color=GREEN,
        ) #定义坐标轴axes5_1中的一条直线：y = 4，颜色为绿色，discountinuities为间断点，这里随便定义也不影响输出，但是如果是有间断点的函数将很实用，因此保留

        self.play(FadeOut(v_line5_2), FadeIn(step_graph), ReplacementTransform(text5_2, text5_3)) #定义的垂线消失，直线出现，指定文本替换
        self.wait() #等疫苗
        step_label = axes5_1.get_graph_label(step_graph, Tex("L"), x=4).next_to(step_graph) #定义函数标签内容和位置
        self.play(FadeIn(step_label)) #定义的标签出现
        self.wait() #等一秒

        step_graph5_2 = axes5_1.get_graph(
            lambda x: 5,
            discontinuities=[3],
            color=BLUE_C,
        ) #定义坐标轴axes5_1中的一条直线：y = 5，颜色为绿色，discountinuities为间断点，这里随便定义也不影响输出，但是如果是有间断点的函数将很实用，因此保留

        step_graph5_3 = axes5_1.get_graph(
            lambda x: 3,
            discontinuities=[3],
            color=BLUE_C,
        ) #定义坐标轴axes5_1中的一条直线：y = 3，颜色为绿色，discountinuities为间断点，这里随便定义也不影响输出，但是如果是有间断点的函数将很实用，因此保留

        text5_4 = Text("一般来说，假定一个如图的区间", font="楷体", color=BLUE_C).scale(0.8)  #定义文本的内容，字体，颜色和大小
        text5_5 = Text("区间中划入了这些点", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_4.to_edge(DOWN) #定义文本的位置：下方边缘
        text5_5.to_edge(DOWN) #定义文本的位置：下方边缘

        self.play(FadeIn(step_graph5_2), FadeIn(step_graph5_3), ReplacementTransform(text5_3, text5_4)) #指定直线出现，指定文本替换
        self.wait(2) #等两秒
        self.play(dot5_5.animate.set_color(YELLOW),
                  dot5_6.animate.set_color(YELLOW),
                  dot5_7.animate.set_color(YELLOW),
                  dot5_8.animate.set_color(YELLOW),
                  dot5_9.animate.set_color(YELLOW),
                  ReplacementTransform(text5_4, text5_5)

                  ) #指定点变成黄色，指定文本替换
        self.wait(2) #等两秒

        step_graph5_4 = axes5_1.get_graph(
            lambda x: 4.5,
            discontinuities=[3],
            color=BLUE_C,
        ) #定义坐标轴axes5_1中的一条直线：y = 4.5，颜色为绿色，discountinuities为间断点，这里随便定义也不影响输出，但是如果是有间断点的函数将很实用，因此保留

        step_graph5_5 = axes5_1.get_graph(
            lambda x: 3.5,
            discontinuities=[3],
            color=BLUE_C,
        ) #定义坐标轴axes5_1中的一条直线：y = 3.5，颜色为绿色，discountinuities为间断点，这里随便定义也不影响输出，但是如果是有间断点的函数将很实用，因此保留
        
        text5_6 = Text("区域中有无穷多个点，也可理解为", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_6.to_edge(DOWN)

        self.play(
                  ReplacementTransform(text5_5, text5_6,run_time=2))

        self.wait()

        text5_7 = Text("从某一个点开始后面的点都在区域内", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_7.to_edge(DOWN) #定义文本的位置：下方边缘处
        self.play(ReplacementTransform(text5_6, text5_7), dot5_5.animate.set_color(WHITE),
                  dot5_6.animate.set_color(WHITE),
                  dot5_7.animate.set_color(YELLOW),
                  dot5_8.animate.set_color(WHITE),
                  dot5_9.animate.set_color(YELLOW)) #指定文本替换，指定点颜色变换或者不变
        self.wait() #等一秒
        text5_8_1 = Text("以", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_8_2 = Tex("L", color=BLUE_C).scale(1.2) #定义LaTeX文本的内容，颜色和大小
        text5_8_3 = Text("为中心缩小区域", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_8 = VGroup(text5_8_1, text5_8_2, text5_8_3) #将若干元素放进一个组合
        text5_8.arrange(RIGHT) #组合中后一个元素在前一个元素右边
        text5_8.to_edge(DOWN) #定义文本位置：下方边缘
        text5_9 = Text("依旧有无穷多个点落在区域内", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_9.to_edge(DOWN) #定义文本位置：下方边缘
        text5_10 = Text("也依旧能找到一个点使得这个点之后的点都落在区域内", font="楷体", color=BLUE_C).scale(0.5) #定义文本的内容，字体，颜色和大小
        text5_10.to_edge(DOWN) #定义文本位置：下方边缘

        text5_11_1 = Text("我们说", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_11_2 = Text("是这个数列的极限", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_11_3 = Tex(r"L", color=BLUE_C).scale(1.4) #定义LaTeX文本的内容，颜色和大小

        text5_11 = VGroup(text5_11_1, text5_11_3, text5_11_2).arrange(RIGHT) #将指定的若干元素放进一个组合，组合中后面的元素在前面元素的右边


        text5_11.to_edge(DOWN) #定义文本的位置：下方边缘处
        text5_12 = Text("这就是数学家所说的数列极限的定义", font="楷体", color=BLUE_C).scale(0.8) #定义文本的内容，字体，颜色和大小
        text5_12.to_edge(DOWN) #定义文本的位置：下方边缘处

        self.play(ReplacementTransform(text5_7, text5_8,run_time=2),ReplacementTransform(step_graph5_2, step_graph5_4),
                  ReplacementTransform(step_graph5_3, step_graph5_5)) #指定文本替换以及过程的时间长度，指定线的替换
        self.wait(1) #等一秒

        self.play(ReplacementTransform(text5_8, text5_9,run_time=2)) #指定文本替换，过程时长2s
        self.wait(1) #等一秒

        self.play(ReplacementTransform(text5_9, text5_10,run_time=2)) #指定文本替换，过程时长2s
        self.wait(1) #等一秒

        self.play(ReplacementTransform(text5_10, text5_11,run_time=2)) #指定文本替换，过程时长2s
        self.wait(1) #等一秒

        self.play(ReplacementTransform(text5_11, text5_12,run_time=2)) #指定文本替换，过程时长2s
        self.wait(1) #等一秒
