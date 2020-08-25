import sge
import pykingdom
from numpy import zeros


class Sky(sge.dsp.Object):

    def __init__(self, weather: pykingdom.weather.Weather):
        super().__init__(0, 0, sprite=sge.gfx.Sprite(width=sge.game.width, height=sge.game.height))
        self.weather = weather
        self.weather_changed = 0

    def event_step(self, time_passed, delta_mult):
        if self.weather.changed > self.weather_changed:
            pixels = zeros((sge.game.width, sge.game.height))
            pixels = pykingdom.utils.gradient_overlay(pixels, [self.weather.variables['sky'],
                                                                        self.weather.variables['horizon'],
                                                                        self.weather.variables['haze']])
            for x in range(sge.game.width):
                for y in range(sge.game.height):
                    self.sprite.draw_dot(x, y, sge.gfx.Color(int(pixels[x][y])))
            self.weather_changed = self.weather.t