import sge
from pykingdom.menustate import MenuState

class King(sge.dsp.Game):

    def event_key_press(self, key, char):
        if key == 'escape':
            self.event_close()

    def event_close(self):
        self.end()

King(width=288, height=160, scale=3)

sge.game.start_room = MenuState()

if __name__ == '__main__':
    sge.game.start()