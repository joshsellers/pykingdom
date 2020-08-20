#import xml.etree.ElementTree as et
#root = et.parse("assets/levels/fields.oel").getroot()
#print(root.get('backdropFarImg'))
from os import getcwd
import sge
import pykingdom

_cwd = getcwd()

_level_city = f'{_cwd}\\pykingdom\\assets\\levels\\compiled\\fields.oel'

_tiles_img = f'{_cwd}\\pykingdom\\assets\\gfx\\tiles.png'
_skyline_hills_img = f'{_cwd}\\pykingdom\\assets\\gfx\\skyline_hills.png'
_skyline_trees_img = f'{_cwd}\\pykingdom\\assets\\gfx\\skyline_trees.png'
_hill_img = f'{_cwd}\\pykingdom\\assets\\gfx\\hill.png'

_hit_sound = f'{_cwd}\\pykingdom\\assets\\sounds\\hit.mp3'
_hit_big_sound = f'{_cwd}\\pykingdom\\assets\\sounds\\hitbig.mp3'

_cicada_sound = f'{_cwd}\\pykingdom\\assets\\sounds\\cicada.mp3'
_owls_sound = f'{_cwd}\\pykingdom\\assets\\sounds\\owls.mp3'
_birds_sound = f'{_cwd}\\pykingdom\\assets\\sounds\\birds.mp3'

_music_night_1 = f'{_cwd}\\pykingdom\\assets\\music\\night1.mp3'
_music_night_2 = f'{_cwd}\\pykingdom\\assets\\music\\night2.mp3'
_music_night_3 = f'{_cwd}\\pykingdom\\assets\\music\\night3.mp3'
_music_night_4 = f'{_cwd}\\pykingdom\\assets\\music\\night4.mp3'
_music_night_5 = f'{_cwd}\\pykingdom\\assets\\music\\night5.mp3'
_music_day_1 = f'{_cwd}\\pykingdom\\assets\\music\\day1.mp3'
_music_day_2 = f'{_cwd}\\pykingdom\\assets\\music\\day2.mp3'
_music_day_3 = f'{_cwd}\\pykingdom\\assets\\music\\day3.mp3'
_music_day_4 = f'{_cwd}\\pykingdom\\assets\\music\\day4.mp3'
_music_day_5 = f'{_cwd}\\pykingdom\\assets\\music\\day5.mp3'


CHEATS = False
WEATHER_CONTROLS = False

GAME_WIDTH = 3840
MIN_KINGDOM_WIDTH = 200

MAX_BUNNIES = 50
MIN_BUNNY_SPAWN_TIME = 6.0

MIN_TROLL_SPAWN_TIME = 1.0

TROLL_WALL_DAMAGE = 2.0

TEXT_MAX_ALPHA = 0.7
TEXT_READ_SPEED = 0.2
TEXT_MIN_TIME = 6


class PlayState(sge.dsp.Room):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sky: pykingdom.sky.Sky
        self.sun_moon: pykingdom.sunmoon.SunMoon
        self.backdrop_far: sge.gfx.Background
        self.backdrop_close: sge.gfx.Background
        self.backdrop: [sge.gfx.Background] #? maybe
        self.haze: pykingdom.haze.Haze

        self.player: sge.gfx.Sprite
        self.bunnies: [sge.gfx.Sprite] #? maybe
        self.farmland: [sge.gfx.Sprite]
        self.coins: [sge.gfx.Sprite]
        self.beggars: [sge.gfx.Sprite]
        self.characters: [sge.gfx.Sprite]
        self.trolls: [sge.gfx.Sprite]
        self.trolls_no_collide: [sge.gfx.Sprite]
        self.gibs: [sge.gfx.Sprite]
        self.indicators: [sge.gfx.Sprite]

        self.walls: [sge.gfx.Sprite]
        self.level: [sge.gfx.Sprite]
        self.archers: [sge.gfx.Sprite]
        self.objects: [sge.gfx.Sprite]
        self.shops: [sge.gfx.Sprite]
        self.floor: [sge.gfx.Sprite] # might have to implement FlxTileMap for this
        self.farmlands: [sge.gfx.Sprite]
        self.props: [sge.gfx.Sprite]
        self.lights: [sge.gfx.Sprite]
        self.darkness: sge.gfx.Sprite
        self.water: pykingdom.water.Water
        self.arrows: [sge.gfx.Sprite]
        self.fx: [sge.gfx.Sprite]
        self.fog: pykingdom.fog.Fog
        self.text: str #implement FlxText
        self.center_text: str
        self.sack: pykingdom.coinsack.Coinsack
        self.noise: sge.gfx.Sprite

        self.weather: pykingdom.weather.Weather

        self.castle: pykingdom.castle.Castle
        self.minimap: pykingdom.minimap.Minimap

        self.weather_input: None # maybe make this a command interface

    def event_room_start(self):
        self._font = sge.gfx.Font(name=f'{_cwd}\\pykingdom\\assets\\04b03.ttf', size=8)