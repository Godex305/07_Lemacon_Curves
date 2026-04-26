from manim import *
import numpy as np

config.frame_width = 9
config.frame_height = 16
config.pixel_width = 1080
config.pixel_height = 1920


class RightwardAndLeftwardLimacon(Scene):
    def construct(self):
        title = Tex(r"Polar Sketch of")
        title.to_edge(UP)

        polar_curve = Tex(r"Right and Left Limacons")
        polar_curve.next_to(title, DOWN, buff=0.3)

        formula = MathTex(r"r = a \pm b\cos\theta").scale(1.2)
        formula.next_to(polar_curve, DOWN, buff=0.5)

        self.play(Write(title), Write(polar_curve))
        self.play(Write(formula))

        plane = PolarPlane(
            azimuth_units="PI radians",
            size=4,
            radius_max=4,
        )
        plane.add_coordinates()
        plane.scale(1.8)

        self.play(Create(plane), run_time=2)

        a = ValueTracker(-2)
        b = ValueTracker(2)

        graph = always_redraw(
            lambda: plane.plot_polar_graph(
                lambda theta: a.get_value() + b.get_value() * np.cos(theta),
                theta_range=[0, TAU],
                color=YELLOW,
            )
        )

        label1 = MathTex("a=")
        number1 = DecimalNumber(
            a.get_value(),
            num_decimal_places=2,
            color=YELLOW
        )
        number1.add_updater(lambda d: d.set_value(a.get_value()))

        label2 = MathTex("b=")
        number2 = DecimalNumber(
            b.get_value(),
            num_decimal_places=2,
            color=RED
        )
        number2.add_updater(lambda d: d.set_value(b.get_value()))

        value_group1 = VGroup(label1, number1).arrange(RIGHT, buff=0.15)
        value_group1.to_edge(DOWN)
        value_group1.shift(UP * 2 + LEFT)

        value_group2 = VGroup(label2, number2).arrange(RIGHT, buff=0.15)
        value_group2.to_edge(DOWN)
        value_group2.shift(UP * 2 + RIGHT*1.2)

        self.play(Create(graph), Write(value_group1), Write(value_group2))

        self.play(a.animate.set_value(2), run_time=6, rate_func=linear)
        self.play(b.animate.set_value(-2), run_time=6, rate_func=linear)
        
        # second graph

        graph1 = always_redraw(
            lambda: plane.plot_polar_graph(
                lambda theta: a.get_value() - 2 * np.cos(theta),
                theta_range=[0, TAU],
                color=YELLOW,
            )
        )
        self.play(ReplacementTransform(graph, graph1), run_time=0.2)
        self.add(graph1)

        self.play(a.animate.set_value(-2), run_time=6, rate_func=linear)
        self.wait()
        self.play(FadeOut(*self.mobjects))