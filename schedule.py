from manimlib import *
# import numpy as np
# from scipy import misc

# day = {
#     idx: 0,
#     time: "",
#     title: ""
# }

# schedule = {
#     title: "Schedule",
#     days: [
#         {
#             idx: 0,
#             time: "",
#             title: ""
#         }
#     ],
#     map_days: [
#         "lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"
#     ]
# }


'''
    Schedule structure
    ________________
    |              |
    |     North    |
    |--------------|
    |              |
    |              |
    |    Main      |
    |     area     |
    |              |
    |              |
    |--------------|
    |     South    |
    |______________|


    Inner structure:

    North
      |-kanji
      |-main title

    Main area
      |-day
          |-time info
              |-day
              |-time
          |-title
    ...

    South
      |-link
          |-link domain
          |-username




  TODO: divide into different functions or different scenes
      - Init: set image as background
      - North: write title
      - Main area: make & write actual schedule
      - South: write link
      ? wait
      - Fade out
'''


class Schedule(Scene):

    style = {
        "fill_color": WHITE,
        "background_stroke_color": WHITE,
        "stroke_color": WHITE
    }

    days = ["lunedì", "martedì", "mercoledì",
            "giovedì", "venerdì", "sabato", "domenica"]

    def _day(self, day, time, title):
        _day = Text(self.days[day].upper() + " ⋅ " + time,
                    font_size=14, **self.style).set_opacity(.5)
        _title = Text(title, font_size=24, **self.style)

        _d = VGroup(_day, _title).arrange(direction=DOWN,
                                          aligned_edge=LEFT, buff=.1)

        return _d

    def construct(self):

        # Set image as background

        bg = ImageMobject("assets/FipWRp9aAAASCHW.jpeg").scale(2)
        # bg.fade(darkness=.5)
        bg.set_opacity(.4)
        self.add(bg)

        primary = WHITE

        # North

        sched_bg = Text("予定", font="Noto Serif JP",
                        font_size=64, **self.style).move_to([0, 3, 0])
        sched_bg.set_fill(primary, opacity=.3)
        sched_bg.set_stroke(primary, opacity=.1)

        sched_fg = Text("Schedule", font="Amiri",
                        font_size=40, **self.style).move_to([0, 3, 0])

        # Main area

        sched = [
            self._day(0, "20:30", "Robe"),
            self._day(2, "22:00", "Blender"),
            self._day(3, "21:30", "Gaming"),
            self._day(4, "16:00", "Arte")
        ]

        _days = VGroup(*sched).arrange(direction=DOWN,
                                       aligned_edge=LEFT, buff=.5).move_to(LEFT)

        # South

        _link_dom = Text("twitch.tv/", font_size=20,
                         **self.style).set_opacity(.5)

        _link_spc = Text("febueldo", font_size=20, **self.style)
        _link_spc.set_color(primary)
        _link_spc.set_stroke(primary)

        _link = VGroup(_link_dom, _link_spc).arrange(
            direction=RIGHT, buff=.05).to_edge(2*DOWN)

        # Animate

        self.play(AnimationGroup(Write(sched_bg),
                  Write(sched_fg), lag_ratio=.2))       # North
        self.play(Write(_days))                         # Main area
        self.play(Write(_link))                         # South

        # self.wait(5)

        # Fade out

        # self.play(AnimationGroup(FadeOut(sched_bg), FadeOut(
        #     sched_fg), *[FadeOut(mob) for mob in _days], *[FadeOut(mob) for mob in _link], lag_ratio=.2))
