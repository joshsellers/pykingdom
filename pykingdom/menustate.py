import sge
from pykingdom.globals import VERSION
from pykingdom.playstate import PlayState
import webbrowser as web
from os import getcwd as cwd, path

_d = cwd()
_dir = f'{_d}\\pykingdom\\assets\\gfx'
_title_img = 'title'
_noio_img = 'outline_noio'
_pez_img = 'outline_pez'

class MenuState(sge.dsp.Room):

    def event_room_start(self):
        self._version_font = sge.gfx.Font(name=f'{_d}\\pykingdom\\assets\\04b03.ttf', size=8)

        title_object = sge.dsp.Object(0, 0, sprite=sge.gfx.Sprite(name=_title_img, directory=_dir))
        self.noio_highlight = sge.dsp.Object(228, 123, sprite=sge.gfx.Sprite(name=_noio_img, directory=_dir))
        self.pez_highlight = sge.dsp.Object(258, 123, sprite=sge.gfx.Sprite(name=_pez_img, directory=_dir))
        self.add(title_object)
        self.add(self.noio_highlight)
        self.add(self.pez_highlight)
        self.noio_highlight.visible = False
        self.pez_highlight.visible = False
        self.noio_highlight.z = 1
        self.pez_highlight.z = 1

    def event_mouse_button_release(self, button):
        if self.noio_highlight.visible: web.open_new_tab('http://www.noio.nl')
        elif self.pez_highlight.visible: web.open_new_tab('http://soundcloud.com/pez_pez')
        else:
            sge.game.mouse.visible = False
            PlayState(background=sge.gfx.Background([], sge.gfx.Color((0xaf, 0xb4, 0xc2, 0xff)))).start()

    def event_step(self, time_passed, delta_mult):
        x = int(sge.mouse.get_x())
        y = int(sge.mouse.get_y())

        self.noio_highlight.visible = \
            not self.pez_highlight.visible and \
            self.noio_highlight.x < x < self.noio_highlight.x + self.noio_highlight.bbox_width \
            and self.noio_highlight.y < y < self.noio_highlight.y + self.noio_highlight.bbox_height

        self.pez_highlight.visible = \
            not self.noio_highlight.visible and \
            self.pez_highlight.x < x < self.pez_highlight.x + self.pez_highlight.bbox_width \
            and self.pez_highlight.y < y < self.pez_highlight.y + self.pez_highlight.bbox_height

        self.project_text(self._version_font, f'pykingdom {VERSION}', sge.game.width / 2 - 103,
                          sge.game.height / 2 - 45, 1, halign='left',
                          color=sge.gfx.Color((0xff, 0xff, 0xff, 0x3e)))