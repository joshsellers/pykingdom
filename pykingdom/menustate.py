import sge
from pykingdom.globals import VERSION

class MenuState(sge.dsp.Room):
    _dir = 'assets/gfx'
    _title_img = 'title'
    _noio_img = 'outline_noio'
    _pez_img = 'outline_pez'

    def event_room_start(self):
        self._version_font = sge.gfx.Font(name='assets/04b03.ttf', size=8)

        title_object = sge.dsp.Object(0, 0, sprite=sge.gfx.Sprite(name=MenuState._title_img, directory=MenuState._dir))
        self.noio_highlight = sge.dsp.Object(228, 123, sprite=sge.gfx.Sprite(name=MenuState._noio_img, directory=MenuState._dir))
        self.pez_highlight = sge.dsp.Object(258, 123, sprite=sge.gfx.Sprite(name=MenuState._pez_img, directory=MenuState._dir))
        self.add(title_object)
        self.add(self.noio_highlight)
        self.add(self.pez_highlight)
        self.noio_highlight.visible = True
        self.pez_highlight.visible = False
        self.noio_highlight.z = 1
        self.pez_highlight.z = 1

    def event_step(self, time_passed, delta_mult):
        x = int(sge.mouse.get_x())
        y = int(sge.mouse.get_y())

        self.noio_highlight.visible =\
            not self.pez_highlight.visible and\
            self.noio_highlight.x < x < self.noio_highlight.x + self.noio_highlight.bbox_width \
            and self.noio_highlight.y < y < self.noio_highlight.y + self.noio_highlight.bbox_height

        self.pez_highlight.visible =\
            not self.noio_highlight.visible and\
            self.pez_highlight.x < x < self.pez_highlight.x + self.pez_highlight.bbox_width \
            and self.pez_highlight.y < y < self.pez_highlight.y + self.pez_highlight.bbox_height

        self.project_text(self._version_font, VERSION, 265, 88, 1, halign='left', color=sge.gfx.Color((0xff, 0xff, 0xff, 0x3e)))