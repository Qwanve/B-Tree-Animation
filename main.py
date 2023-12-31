from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        real_slots = []
        slots = VGroup()
        for i in range(1, 5):
            self.play(slots.animate.shift(LEFT))
            sloti = Square()
            sloti.set_fill(BLUE, opacity=1)
            sloti.next_to(slots, RIGHT, buff=0)
            labeli = Integer(number=i)
            labeli.move_to(sloti)
            sloti.add(labeli)
            real_slots.append(sloti)
            slots.add(sloti)
            slots.center()
            self.play(Write(sloti))
            self.wait()


        self.play(slots.animate.shift(LEFT))
        slot4 = Square()
        slot4.set_fill(BLUE, opacity=1)
        slot4.next_to(slots, RIGHT, buff=0)
        label4 = Integer(number=5)
        label4.move_to(slot4)
        slot4.add(label4)
        self.play(Write(slot4))
        self.wait()
        real_slots.append(slot4)
        slots = VGroup(*real_slots)

        self.play(slots.animate.shift(LEFT))
        slot5 = Square()
        slot5.set_fill(BLUE, opacity=1)
        slot5.next_to(slots, RIGHT, buff=0)
        label5 = Integer(number=6)
        label5.move_to(slot5)
        slot5.add(label5)
        self.play(Write(slot5))
        self.play(Indicate(slot5, scale_factor=0.9, color=RED_A))
        self.wait()
        real_slots.append(slot5)
        slots = VGroup(*real_slots)

        self.play(Circumscribe(real_slots[2]))
        self.wait()

        left = VGroup(*real_slots[0:2])
        median = real_slots[2]
        right = VGroup(*real_slots[3:])

        # end = left.copy().shift(3*DOWN + 0.5*LEFT).get_corner(UP+RIGHT)
        # larrow = Arrow(start=UP, end=1*DOWN+0.5*LEFT)
        larrow = Arrow().put_start_and_end_on(median.get_corner(DOWN+LEFT), left.get_edge_center(UP) + (3*DOWN + 0.5*LEFT))
        rarrow = Arrow().put_start_and_end_on(median.get_corner(DOWN+RIGHT), right.get_edge_center(UP) + (3*DOWN + 0.5*RIGHT))
        # larrow.next_to(median, DOWN+LEFT, buff=0)

        self.play(left.animate.shift(3*DOWN + 0.5*LEFT), right.animate.shift(3*DOWN + 0.5*RIGHT), Create(larrow), Create(rarrow))
        tree = VGroup(*[left,larrow, median,rarrow, right])
        self.play(tree.animate.center())
        self.wait()
        







