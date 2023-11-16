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
            self.play(Create(sloti))
            self.wait()


        self.play(slots.animate.shift(LEFT))
        slot4 = Square()
        slot4.set_fill(BLUE, opacity=1)
        slot4.next_to(slots, RIGHT, buff=0)
        label4 = Integer(number=5)
        label4.move_to(slot4)
        slot4.add(label4)
        self.play(Create(slot4))
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
        self.play(Create(slot5))
        self.play(slot5.animate.set_fill(RED_A, opacity=1), label5.animate.set_fill(WHITE, opacity=1))
        self.wait()
        # self.play(slot5.animate.set_fill(BLUE, opacity=1).add(label5))
        real_slots.append(slot5)
        slots = VGroup(*real_slots)

        median = SurroundingRectangle(real_slots[2], buff=0.1)
        self.play(Create(median), slot5.animate.set_fill(BLUE, opacity=1), label5.animate.set_fill(WHITE, opacity=1))
        self.wait()
        # self.play(Uncreate(median))
        # self.wait()

        left = VGroup(*real_slots[0:2])
        median = real_slots[2]
        right = VGroup(*real_slots[3:])

        # self.play(Uncreate(median), left.animate.shift(3*DOWN + 0.5*LEFT), right.animate.shift(3*DOWN + 0.5*RIGHT))
        self.play(left.animate.shift(3*DOWN + 0.5*LEFT), right.animate.shift(3*DOWN + 0.5*RIGHT))
        self.play(Uncreate(median))
        self.wait()
        







