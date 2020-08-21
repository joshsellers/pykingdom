import sge
import pykingdom as pk

class Weather(sge.dsp.Object):

    def __init__(self):
        super().__init__(0, 0)

        self.variables = {
            'sky': 0xFF8C8CA6,
            'horizon': 0xFFCF7968,
            'haze': 0xAAF3F1E8,
            'darknessColor': 0x88111114,
            'darkness': 0.1,
            'contrast': 0.3,
            'saturation': 1.0,
            'ambient': 0x11FF0000,
            'wind': 0.0,
            'fog': 0.5,
            'rain': 0.5,
            'timeOfDay': 0.5,
            'sunTint': 0xFFFFFF
        }

        self.ambient_transform = pk.colormatrix.ColorMatrix()

        self.t = 0
        self.changed = 0
        self.progress = 0
        self.ambient_amount = 0

        self.tween_start = 0
        self.tween_duration = 0.0
        self.previous_state = pk.weatherpresets.SUNNY
        self.target_state = pk.weatherpresets.SUNNY

        self._set_variables(pk.weatherpresets.SUNNY)

    def event_step(self, time_passed, delta_mult):
        self.t += time_passed
        if self.t - self.changed > 1/30:
            self.update_tween()
            self.changed = self.t

    def tween_to(self, state, d=30):
        self.target_state = state
        if d == 0:
            self._set_variables(state)
            self.previous_state = state
        else:
            self.tween_duration = d
            self.tween_start = self.t

    def update_tween(self):
        if self.target_state is self.previous_state: return

        self.progress = (self.t - self.tween_start) / self.tween_duration
        if self.tween_duration == 0 or self.progress >= 1:
            self.previous_state = self.target_state
            self.progress = 1
        self._set_variables(self.target_state, self.previous_state, self.progress)

    def _set_variables(self, target, previous=None, f=1):
        if not 'ambientAmount' in target:
            target['ambientAmount'] = ((target['ambient'] >> 24) / 0xFF)

        if previous is None:
            previous = target

        fi = 1 - f
        for v in target:
            if v == 'darkness' or v == 'contrast' or v == 'saturation' or v == 'fog' or v == 'rain' or v == 'wind' \
               or v == 'ambientAmount':
                self.variables[v] = (fi * previous[v]) + (f * target[v])
            elif v == 'timeOfDay':
                val = target[v] if target[v] > previous[v] else target[v] + 1
                self.variables[v] = (previous[v] + (val - previous[v]) * f) % 1
            else:
                self.variables[v] = pk.utils.interpolate_color(previous[v], target[v], f)

        self.ambient_transform.reset()

        self.ambient_transform.colorize(self.variables['ambient'], self.variables['ambientAmount'])
        self.ambient_transform.adjust_contrast(self.variables['contrast'])
        self.ambient_transform.adjust_saturation(self.variables['saturation'])

        self.variables['darknessColor'] = (self.variables['darknessColor'] & 0x00FFFFFF) | \
                                          (int(0xFF * self.variables['darkness']) << 24)