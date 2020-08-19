#import xml.etree.ElementTree as et
#root = et.parse("assets/levels/fields.oel").getroot()
#print(root.get('backdropFarImg'))
import sge

class PlayState(sge.dsp.Room):
    def event_room_start(self):
        pass