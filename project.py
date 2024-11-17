import math
import time

import engine
from engine.events import *
from engine.operators import *
from engine.types import *


@sprite('Stage')
class Stage(Target):
    """Sprite Stage"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 100, "None", [
            {
                'name': "backdrop1",
                'path': "e0a0a42f498c19162bc4572cf41f6bb2.svg",
                'center': (240, 180),
                'scale': 1
            },
            {
                'name': "backdrop2",
                'path': "1f535ea3194b2872afa6716f5a79cde5.svg",
                'center': (240, 180),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "551527_BOT-LAB",
                'path': "eee6519718375f0c228bff86f515f048.wav"
            }
        ])

        self.varlsx = 19
        self.varlsy = 13
        self.varlsz = 247
        self.varofx = 228
        self.varofy = 156
        self.varDrawPaths = 0
        self.varMMUL = 10
        self.varGameStatus = 0
        self.varGraphics = 2
        self.varRMUL = 6
        self.varFrame = 0
        self.varCoins = 15
        self.varNewCoins = 0
        self.varToolType = 1
        self.varDTMUL = 13
        self.varMobCount = 0
        self.varWave = 0
        self.varLives = 20
        self.varSpeed = 1
        self.varDMMUL = 15
        self.varSelected = 0
        self.varAction = 2
        self.varSellPrice = 0
        self.varUpgradePrice = 0
        self.varUpgradeTower = 0
        self.var_Difficulty = 0
        self.varDiffMul = 0.5
        self.varSoundMachine = 0
        self.varSoundGlue = 0
        self.varLevel = 1
        self.varLevelCount = 3

        self.listLevel = List(
            [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 3, 2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 3, 2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 3, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        )
        self.listPath = List(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1, 0, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1, 0, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1, 0, 0, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 1, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 100, 0, 0, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 100, 0, 0, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 100, 0, 0, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 110, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
        self.list_find = List(
            []
        )
        self.listExits = List(
            [0, 152, 0, 133, 0, 114]
        )
        self.listLevelUpdates = List(
            []
        )
        self.listEntrances = List(
            [0, 134, 0, 115, 0, 96]
        )
        self.listGunClones = List(
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        )
        self.listMob = List(
            [0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", "", 0, "", "", "", "", "", "", "", "", ""]
        )
        self.listRockets = List(
            [0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", "", 0, "", "", "", "", ""]
        )
        self.listMobPool = List(
            [1, 11, 21, 31, 41, 51, 61, 71, 81, 91, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 201, 211, 221, 231, 241, 251, 261, 271, 281, 291, 301, 311, 321, 331, 341, 351, 361, 371, 381, 391, 401, 411, 421, 431, 441, 451, 461, 471, 481, 491]
        )
        self.list_DATA_Turrets = StaticList(
            ["1 - Turret ID", "2 - Turret Base Type (1=Gatling, 2=Glue, 3=Rocket, 4=Tesla)", "3 - Description", "4 - Cost", "5 - Next Upgrade ID", "6 - Turret Base Costume #", "7 - Tool Costume #", "8 - Target Range", "9 - Rotate Speed", "10 - Damage Per Hit", "11 - Sell Price", "12 - Reload Delay", "", 1, 1, "Gatling", 5, 2, 10, 1, 2.4, 9, 0.4, 3, 4, "", 2, 1, "Gatling b", 4, 3, 1, 1, 2.4, 9, 0.7, 5, 4, "", 3, 1, "Gatling c", 4, 0, 13, 1, 2.4, 9, 1.0, 7, 4, "", 4, 2, "Glue Gun", 10, 5, 7, 9, 2.8, 6, 0.1, 6, 45, "", 5, 2, "Glue Gun b", 8, 6, 16, 9, 2.8, 6, 0.1, 10, 25, "", 6, 2, "Glue Gun c", 8, 0, 19, 9, 2.8, 6, 0.1, 14, 15, "", 7, 3, "Rocket", 20, 8, 4, 5, 3.4, 5, 1, 12, 45, "", 8, 3, "Rocket b", 15, 9, 22, 5, 3.4, 5, 1, 20, 25, "", 9, 3, "Rocket c", 15, 0, 25, 5, 3.4, 5, 1, 25, 15, "", 10, 4, "Tesla", 70, 0, 28, 13, 2.5, 360, 15, 35, 45]
        )
        self.listTools = List(
            [1, 4, 7, 10]
        )
        self.list_DATA_Mobs = StaticList(
            ["1 - Mob Type ID", "2 - Description", "3 - Earnings", "4 - Mob Base Costume #", "5 - Health", "6 - Speed", "7 - Acceleration", "8 - Wander (negative pulls to middle, 0 flies!)", "9 - Blast Distance", "10 - Resistance to bullets", "11 - Resistance to glue", "12 - Resistance to rockets", "13 - Health Sprites", "14 - Shield change to mob type id", "", 1, "Imp", 1, 1, 4, 1.5, 0.83, 0.01, 1, 1, 1, 1, 0, 0, "", 2, "Armoured Imp", 2, 3, 13, 1.4, 0.83, 0.01, 0.8, 1.2, 1.3, 1, 0, 0, "", 3, "Speedie (Green Triangle)", 1, 5, 25, 2.5, 0.83, 0.02, 1.2, 1, 1, 1, 0, 0, "", 4, "Heavy", 20, 14, 600, 0.75, 0.83, -0.01, 0.1, 1, 2, 1.2, 5, 0, "", 5, "Saucer", 10, 7, 140, 0.8, 0.83, 0, 0.1, 4, 3, 0.25, 5, 0, "", 6, "Speedie 2 (Green Triangle)", 1, 19, 50, 2.2, 0.83, 0.02, 1, 1, 2, 2, 0, 0, "", 7, "Shielded Berry (Purple)", 1, 21, 25, 1.8, 0.83, 0.01, 0, 10, 10, 10, 0, 8, "", 8, "Berry (Purple)", 1, 23, 80, 1.8, 0.83, 0.01, 1, 1, 1, 1, 0, 0]
        )

        self.sprite.layer = 0

    @on_green_flag
    async def green_flag(self, util):
        self.varGraphics = 2
        self.varMMUL = 10
        self.varRMUL = 6
        self.varDTMUL = 13
        self.varDMMUL = 15
        self.varLevel = 1
        pass # hide variable
        self.listMob.delete_all()
        await util.send_broadcast_wait("InitClones")
        await util.send_broadcast_wait("Init: Creeate Level List")
        await util.send_broadcast_wait("Init: Clone Level Tiles")
        await util.sprites["Level"].broadcast_initstamplevel(util)
        await util.sprites["Level"].broadcast_updatelevel(util)
        await util.send_broadcast_wait("Update: Guns")
        await util.sprites["Path Finder"].broadcast_gofind(util)
        if gt(self.varDrawPaths, 0):
            await util.send_broadcast_wait("Go: Draw Paths")
        await self.sleep(0.5)
        util.send_broadcast("Go: User Input")
        self.sounds.set_volume(100)
        while True:
            await self.sounds.play("551527_BOT-LAB")

            await self.yield_()

    @on_broadcast('go: game on')
    async def broadcast_GoGameOn(self, util):
        for _ in range(25):
            self.sounds.change_volume(-2)

            await self.yield_()

    @on_pressed('g')
    async def key_g_pressed(self, util):
        self.varGraphics = ((self.varGraphics + 1) % 3)
        print(self.varGraphics)
        await self.sleep(1)
        pass # hide variable


@sprite('Init')
class SpriteInit(Target):
    """Sprite Init"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 22
        self._ypos = 13
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Init",
                'path': "d36f6603ec293d2c2198d3ea05109fe0.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_t = 170

        self.listMobTiles = StaticList(
            []
        )

        self.sprite.layer = 4

    @warp
    async def my_Init(self, util, ):
        util.sprites.stage.varlsx = 19
        util.sprites.stage.varlsy = 13
        util.sprites.stage.varlsz = (util.sprites.stage.varlsx * util.sprites.stage.varlsy)
        util.sprites.stage.listLevel.delete_all()
        for _ in range(toint(util.sprites.stage.varlsx)):
            util.sprites.stage.listLevel.append(10)
        for _ in range(toint((util.sprites.stage.varlsy - 2))):
            util.sprites.stage.listLevel.append(10)
            for _ in range(toint((util.sprites.stage.varlsx - 2))):
                util.sprites.stage.listLevel.append(1)
            util.sprites.stage.listLevel.append(10)
        for _ in range(toint(util.sprites.stage.varlsx)):
            util.sprites.stage.listLevel.append(10)
        if eq(util.sprites.stage.varLevel, 1):
            await self.my_PokeLine(util, 0, (math.floor(div(util.sprites.stage.varlsy, 2)) - 1), 2, 3, 1)
            await self.my_PokeLine(util, 1, (math.floor(div(util.sprites.stage.varlsy, 2)) - 1), 5, 3, 1)
            await self.my_PokeLine(util, (util.sprites.stage.varlsx - 1), (math.floor(div(util.sprites.stage.varlsy, 2)) - 1), 3, 3, 1)
            await self.my_PokeLine(util, (util.sprites.stage.varlsx - 2), (math.floor(div(util.sprites.stage.varlsy, 2)) - 1), 5, 3, 1)
        else:
            if eq(util.sprites.stage.varLevel, 2):
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), 0, 3, 3, 2)
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), (util.sprites.stage.varlsy - 1), 2, 3, 2)
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), 1, 5, 3, 2)
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), (util.sprites.stage.varlsy - 2), 5, 3, 2)
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), 5, 5, 3, 1)
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) + 1), 5, 5, 3, 1)
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 3), 6, 5, 7, 2)
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 0), 3, 10, 3, 1)
                await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 0), 7, 10, 3, 1)
            else:
                if eq(util.sprites.stage.varLevel, 3):
                    await self.my_PokeLine(util, 0, (math.floor(div(util.sprites.stage.varlsy, 2)) - 1), 2, 3, 1)
                    await self.my_PokeLine(util, 1, (math.floor(div(util.sprites.stage.varlsy, 2)) - 1), 5, 3, 1)
                    await self.my_PokeLine(util, (util.sprites.stage.varlsx - 1), (math.floor(div(util.sprites.stage.varlsy, 2)) - 1), 3, 3, 1)
                    await self.my_PokeLine(util, (util.sprites.stage.varlsx - 2), (math.floor(div(util.sprites.stage.varlsy, 2)) - 1), 5, 3, 1)
                    await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), 0, 7, 3, 2)
                    await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), (util.sprites.stage.varlsy - 1), 6, 3, 2)
                    await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), 1, 5, 3, 2)
                    await self.my_PokeLine(util, (math.floor(div(util.sprites.stage.varlsx, 2)) - 1), (util.sprites.stage.varlsy - 2), 5, 3, 2)
                else:
                    pass
        util.sprites.stage.listTools.delete_all()
        util.sprites.stage.listTools.append(1)
        util.sprites.stage.listTools.append(4)
        util.sprites.stage.listTools.append(7)
        util.sprites.stage.listTools.append(10)

    @warp
    async def my_PokeLine(self, util, arg_x, arg_y, arg_typ, arg_count, arg_dir):
        self.var_t = (((arg_y * util.sprites.stage.varlsx) + arg_x) + 1)
        for _ in range(toint(arg_count)):
            util.sprites.stage.listLevel[toint(self.var_t)] = arg_typ
            if eq(arg_dir, 1):
                self.var_t += util.sprites.stage.varlsx
            else:
                self.var_t += 1

    @warp
    async def my_Poke(self, util, arg_x, arg_y, arg_tileID):
        util.sprites.stage.listLevel[toint((((tonum(arg_y) * util.sprites.stage.varlsx) + tonum(arg_x)) + 1))] = arg_tileID

    @on_broadcast('init: creeate level list')
    async def broadcast_InitCreeateLevelList(self, util):
        if eq(1, 1):
            await self.my_Init(util, )
        util.sprites.stage.varofx = (util.sprites.stage.varlsx * 12)
        util.sprites.stage.varofy = ((util.sprites.stage.varlsy * 12) - 0)

    @on_broadcast('reset level')
    async def broadcast_ResetLevel(self, util):
        await self.my_Init(util, )
        util.sprites.stage.varofx = (util.sprites.stage.varlsx * 12)
        util.sprites.stage.varofy = ((util.sprites.stage.varlsy * 12) + 20)


@sprite('Level')
class SpriteLevel(Target):
    """Sprite Level"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -216
        self._ypos = -144
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           2, 200, "all around", [
            {
                'name': "floor2",
                'path': "ea10a555e74fc86376069ad8e522ef1a.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "floorShadow",
                'path': "5bec0370705871f714b41443035ca778.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "tile1b",
                'path': "88121ae6a0a6863679999253a026f235.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "space",
                'path': "df3184d098af3706e2a824e76041f872.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "spaceShadow",
                'path': "8d906061332e66d965eca124167c2b67.png",
                'center': (12, 12),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_TileIdx = 0
        self.var_X = 0
        self.var_Y = 0
        self.var_tileID = 10
        self.var_i = 7
        self.var_fi = 3



        self.sprite.layer = 2

    @on_green_flag
    async def green_flag(self, util):
        self.costume.size = 200
        self.shown = False

    @warp
    async def my_StampTile(self, util, arg_shadow):
        self.var_X = ((tonum(self.var_TileIdx) - 1) % util.sprites.stage.varlsx)
        self.var_Y = math.floor(div((tonum(self.var_TileIdx) - 1), util.sprites.stage.varlsx))
        if (eq(self.var_tileID, 2) and not self.var_TileIdx in util.sprites.stage.listEntrances):
            util.sprites.stage.listEntrances.append(0)
            util.sprites.stage.listEntrances.append(self.var_TileIdx)
        if (eq(self.var_tileID, 3) and not self.var_TileIdx in util.sprites.stage.listExits):
            util.sprites.stage.listExits.append(0)
            util.sprites.stage.listExits.append(self.var_TileIdx)
        if (eq(self.var_tileID, 6) and not self.var_TileIdx in util.sprites.stage.listEntrances):
            util.sprites.stage.listEntrances.append(1)
            util.sprites.stage.listEntrances.append(self.var_TileIdx)
        if (eq(self.var_tileID, 7) and not self.var_TileIdx in util.sprites.stage.listExits):
            util.sprites.stage.listExits.append(1)
            util.sprites.stage.listExits.append(self.var_TileIdx)
        if gt(self.var_tileID, 9):
            if (eq(self.var_X, 0) or eq(self.var_Y, (util.sprites.stage.varlsy - 1))):
                await self.my_DeleteExitEntrace(util, self.var_TileIdx)
            else:
                if (eq(self.var_X, (util.sprites.stage.varlsx - 1)) or eq(self.var_Y, 0)):
                    await self.my_DeleteExitEntrace(util, self.var_TileIdx)
        if eq(self.var_tileID, 10):
            await self.my_DoStamp(util, 3)
        else:
            if (eq(self.var_tileID, 1) or gt(self.var_tileID, 99)):
                if arg_shadow:
                    await self.my_DoStamp(util, 2)
                else:
                    await self.my_DoStamp(util, 1)
            else:
                if arg_shadow:
                    await self.my_DoStamp(util, 5)
                else:
                    await self.my_DoStamp(util, 4)

    @on_broadcast('update: level')
    async def broadcast_updatelevel(self, util):
        if gt(len(util.sprites.stage.listLevelUpdates), 0):
            await self.my_FiddleEntrancesExits(util, )
            await util.sprites["Path Finder"].broadcast_gofindvalid(util)
            await self.my_LevelUpdates(util, )
            await util.send_broadcast_wait("Update: Guns")
            if eq(util.sprites["Path Finder"].var_IsValid, 0):
                await util.sprites["Path Finder"].broadcast_gofindpathwayinterative(util)

    @warp
    async def my_DeleteExitEntrace(self, util, arg_tileIdx):
        self.var_i = 1
        while not gt(self.var_i, len(util.sprites.stage.listEntrances)):
            if eq(util.sprites.stage.listEntrances[toint((self.var_i + 1))], arg_tileIdx):
                util.sprites.stage.listEntrances.delete(toint(self.var_i))
                util.sprites.stage.listEntrances.delete(toint(self.var_i))
            else:
                self.var_i += 2
        self.var_i = 1
        while not gt(self.var_i, len(util.sprites.stage.listExits)):
            if eq(util.sprites.stage.listExits[toint((self.var_i + 1))], arg_tileIdx):
                util.sprites.stage.listExits.delete(toint(self.var_i))
                util.sprites.stage.listExits.delete(toint(self.var_i))
            else:
                self.var_i += 2

    @warp
    async def my_LevelUpdates(self, util, ):
        while not eq(len(util.sprites.stage.listLevelUpdates), 0):
            self.var_TileIdx = util.sprites.stage.listLevelUpdates[1]
            util.sprites.stage.listLevelUpdates.delete(1)
            if eq(util.sprites["Path Finder"].var_IsValid, 0):
                util.sprites.stage.listLevel[toint(self.var_TileIdx)] = util.sprites.stage.listLevelUpdates[1]
            util.sprites.stage.listLevelUpdates.delete(1)
            self.var_tileID = util.sprites.stage.listLevel[toint(self.var_TileIdx)]
            await self.my_StampTile(util, eq(10, util.sprites.stage.listLevel[toint((tonum(self.var_TileIdx) + util.sprites.stage.varlsx))]))

    @warp
    async def my_FiddleEntrancesExits(self, util, ):
        self.var_fi = 1
        while not gt(self.var_fi, len(util.sprites.stage.listLevelUpdates)):
            self.var_TileIdx = util.sprites.stage.listLevelUpdates[toint(self.var_fi)]
            self.var_tileID = util.sprites.stage.listLevel[toint(self.var_TileIdx)]
            if eq(self.var_tileID, 2):
                util.sprites.stage.listEntrances.append(self.var_TileIdx)
            if eq(self.var_tileID, 3):
                util.sprites.stage.listExits.append(self.var_TileIdx)
            self.var_fi += 2

    @on_broadcast('init: stamp level')
    async def broadcast_initstamplevel(self, util):
        await self.my_StampLevel(util, )

    @warp
    async def my_StampLevel(self, util, ):
        self.pen.clear_all()
        self.var_TileIdx = util.sprites.stage.varlsz
        util.sprites.stage.listEntrances.delete_all()
        util.sprites.stage.listExits.delete_all()
        util.sprites.stage.listGunClones.delete_all()
        for _ in range(toint(util.sprites.stage.varlsz)):
            util.sprites.stage.listGunClones.append(0)
            self.var_tileID = util.sprites.stage.listLevel[toint(self.var_TileIdx)]
            await self.my_StampTile(util, eq(10, util.sprites.stage.listLevel[toint((tonum(self.var_TileIdx) + util.sprites.stage.varlsx))]))
            self.var_TileIdx = tonum(self.var_TileIdx) + -1

    @warp
    async def my_DoStamp(self, util, arg_costumeID):
        if not eq(arg_costumeID, self.costume.number):
            self.costume.switch(arg_costumeID)
        self.gotoxy((((self.var_X * 24) - util.sprites.stage.varofx) + 12), (((self.var_Y * 24) - util.sprites.stage.varofy) + 12))
        self.pen.stamp(util)


@sprite('Path Finder')
class SpritePathFinder(Target):
    """Sprite Path Finder"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -180
        self._ypos = -120
        self._direction = 180
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           1, 44, "all around", [
            {
                'name': "Cube",
                'path': "24aa0ec500c92df7597c102ff833efbe.png",
                'center': (24, 24),
                'scale': 2
            },
            {
                'name': "arrow",
                'path': "8e831d97322bbe707b70702ee0ec5e82.png",
                'center': (24, 24),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_i = 13
        self.var_dist = 0
        self.var_count = 0
        self.var_tileId = 10
        self.var_TileIdx = 0
        self.var_tileID = 0
        self.var_X = 0
        self.var_Y = 1
        self.var_dir = 1
        self.var_ResetReqired = 0
        self.var_findIdx = 1
        self.var_IsValid = 1
        self.var_Path = 2

        self.list_ToDo = List(
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        )

        self.sprite.layer = 3

    @on_green_flag
    async def green_flag(self, util):
        self.var_ResetReqired = 0
        self.shown = False

    @on_broadcast('init: clone level tiles')
    async def broadcast_InitCloneLevelTiles(self, util):
        await self.my_Init(util, )

    @warp
    async def my_Init(self, util, ):
        self.list_ToDo.delete_all()
        util.sprites.stage.listPath.delete_all()
        for _ in range(toint(util.sprites.stage.varlsz)):
            self.list_ToDo.append(0)
            util.sprites.stage.listPath.append(0)
            util.sprites.stage.listPath.append(0)

    @on_broadcast('go: find')
    async def broadcast_gofind(self, util):
        await self.my_Find(util, )

    @on_broadcast('go: find pathway interative')
    async def broadcast_gofindpathwayinterative(self, util):
        self.var_ResetReqired = 1

    @on_broadcast('loop')
    async def broadcast_loop(self, util):
        if gt(self.var_ResetReqired, 0):
            await self.my_InitPathSearch(util, )

    @on_broadcast('go: find valid')
    async def broadcast_gofindvalid(self, util):
        await self.my_FindValid(util, )

    @warp
    async def my_FindValid(self, util, ):
        self.var_IsValid = 1
        self.var_Path = 0
        for _ in range(2):
            await self.my_InitPathSearch(util, )
            await self.my_FindPathLoop(util, (self.var_Path * util.sprites.stage.varlsz))
            self.var_i = 1
            for _ in range(len(util.sprites.stage.listEntrances)):
                if eq(util.sprites.stage.listEntrances[toint(self.var_i)], self.var_Path):
                    if gt(self.list_ToDo[toint(util.sprites.stage.listEntrances[toint((tonum(self.var_i) + 1))])], 0):
                        self.var_IsValid = 0
                self.var_i = tonum(self.var_i) + 2
            self.var_i = 1
            while not (gt(self.var_i, len(util.sprites.stage.listMob)) or eq(self.var_IsValid, 0)):
                self.var_dist = util.sprites.stage.listMob[toint((tonum(self.var_i) + 0))]
                if (gt(self.var_dist, 0) and eq(util.sprites.stage.listMob[toint((tonum(self.var_i) + 999))], self.var_Path)):
                    self.var_dist = (((math.floor(tonum(util.sprites.stage.listMob[toint((tonum(self.var_i) + 2))])) * util.sprites.stage.varlsx) + math.floor(tonum(util.sprites.stage.listMob[toint((tonum(self.var_i) + 1))]))) + 1)
                    if gt(self.list_ToDo[toint(self.var_dist)], 0):
                        self.var_IsValid = 0
                self.var_i = tonum(self.var_i) + util.sprites.stage.varMMUL
            self.var_Path += 1

    @warp
    async def my_Find(self, util, ):
        self.var_Path = 0
        for _ in range(2):
            await self.my_InitPathSearch(util, )
            await self.my_FindPathLoop(util, (self.var_Path * util.sprites.stage.varlsz))
            self.var_Path += 1

    @warp
    async def my_InitPathSearch(self, util, ):
        self.var_ResetReqired = 0
        util.sprites.stage.list_find.delete_all()
        self.var_i = 1
        for _ in range(toint(util.sprites.stage.varlsz)):
            self.list_ToDo[toint(self.var_i)] = 1
            self.var_i = tonum(self.var_i) + 1
        self.var_i = 1
        for _ in range(len(util.sprites.stage.listExits)):
            if eq(util.sprites.stage.listExits[toint(self.var_i)], self.var_Path):
                util.sprites.stage.list_find.append(util.sprites.stage.listExits[toint((tonum(self.var_i) + 1))])
                if lt(util.sprites.stage.listExits[toint((tonum(self.var_i) + 1))], util.sprites.stage.varlsx):
                    util.sprites.stage.list_find.append(100)
                else:
                    util.sprites.stage.list_find.append(10)
            self.var_i = tonum(self.var_i) + 2
        self.var_dist = len(util.sprites.stage.list_find)
        self.var_findIdx = 1

    @warp
    async def my_FindPathLoop(self, util, arg_off):
        while not eq(len(util.sprites.stage.list_find), 0):
            if eq(self.var_findIdx, 1):
                self.var_findIdx = (len(util.sprites.stage.list_find) + 1)
                for _ in range(toint(div(len(util.sprites.stage.list_find), 2))):
                    self.var_findIdx += -2
                    self.list_ToDo[toint(util.sprites.stage.list_find[toint(self.var_findIdx)])] = 2
            self.var_i = util.sprites.stage.list_find[toint(self.var_findIdx)]
            self.var_tileId = util.sprites.stage.listLevel[toint(self.var_i)]
            if lt(self.var_tileId, 10):
                self.var_dir = util.sprites.stage.list_find[toint((self.var_findIdx + 1))]
                if eq(self.list_ToDo[toint(self.var_i)], 2):
                    self.list_ToDo[toint(self.var_i)] = 3
                    util.sprites.stage.listPath[toint((tonum(self.var_i) + arg_off))] = self.var_dir
                    if (not eq(self.var_dir, 100) and eq(self.list_ToDo[toint((tonum(self.var_i) - util.sprites.stage.varlsx))], 1)):
                        util.sprites.stage.list_find.append((tonum(self.var_i) - util.sprites.stage.varlsx))
                        util.sprites.stage.list_find.append(1)
                    if (not eq(self.var_dir, 1) and eq(self.list_ToDo[toint((tonum(self.var_i) + util.sprites.stage.varlsx))], 1)):
                        util.sprites.stage.list_find.append((tonum(self.var_i) + util.sprites.stage.varlsx))
                        util.sprites.stage.list_find.append(100)
                    if (not (eq(self.var_dir, 1000) or eq(self.var_tileId, 2)) and eq(self.list_ToDo[toint((tonum(self.var_i) - 1))], 1)):
                        util.sprites.stage.list_find.append((tonum(self.var_i) - 1))
                        util.sprites.stage.list_find.append(10)
                    if (not (eq(self.var_dir, 10) or eq(self.var_tileId, 3)) and eq(self.list_ToDo[toint((tonum(self.var_i) + 1))], 1)):
                        util.sprites.stage.list_find.append((tonum(self.var_i) + 1))
                        util.sprites.stage.list_find.append(1000)
                else:
                    util.sprites.stage.listPath[toint((tonum(self.var_i) + arg_off))] = (tonum(util.sprites.stage.listPath[toint((tonum(self.var_i) + arg_off))]) + tonum(self.var_dir))
            self.var_findIdx += 2
            if gt(self.var_findIdx, self.var_dist):
                for _ in range(toint(div(self.var_dist, 2))):
                    self.list_ToDo[toint(util.sprites.stage.list_find[1])] = 0
                    util.sprites.stage.list_find.delete(1)
                    util.sprites.stage.list_find.delete(1)
                self.var_dist = len(util.sprites.stage.list_find)
                self.var_findIdx = 1


@sprite('Cursor')
class SpriteCursor(Target):
    """Sprite Cursor"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Hidden",
                'path': "d36f6603ec293d2c2198d3ea05109fe0.png",
                'center': (480, 360),
                'scale': 2
            },
            {
                'name': "Cursor",
                'path': "dad4c6aa2938f482617b0d0e1eec129c.png",
                'center': (24, 24),
                'scale': 2
            },
            {
                'name': "Cursor2",
                'path': "4d7af2c5f602f0f93d642f8fcc8e8ef7.png",
                'center': (24, 24),
                'scale': 2
            },
            {
                'name': "GO",
                'path': "1093f83ee5cfc2c3d2922d4c29727028.png",
                'center': (144, 80),
                'scale': 2
            },
            {
                'name': "GameOver",
                'path': "b6862337496069d84f869266a0259dee.png",
                'center': (80, 48),
                'scale': 2
            },
            {
                'name': "Range5",
                'path': "2dc95a40dcf7a08d5d2a8a48603e7350.png",
                'center': (124, 124),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_X = 17
        self.var_Y = 14
        self.var_DrawType = 0
        self.var_tileIdx = 104
        self.var_tileID = 1
        self.var_PlaceType = 5
        self.var_t = 70
        self.var_t2 = 110



        self.sprite.layer = 15

    @on_green_flag
    async def green_flag(self, util):
        self.costume.size = 100
        util.sprites.stage.varGameStatus = 0
        self.var_PlaceType = 5
        util.sprites.stage.varFrame = 0
        util.sprites.stage.varSelected = 0
        util.sprites.stage.varToolType = 1
        self.shown = False
        await self.my_Reset(util, )

    async def my_ReplaceTile(self, util, arg_tileIdx, arg_tileID):
        if eq(arg_tileID, 0):
            self.var_t = util.sprites.stage.listLevel[toint(arg_tileIdx)]
            self.var_t = (0 - tonum(util.sprites.stage.varSellPrice))
            self.var_t2 = 1
        else:
            self.var_t = util.sprites.stage.list_DATA_Turrets[toint(((tonum(arg_tileID) * util.sprites.stage.varDTMUL) + 4))]
            self.var_t2 = (tonum(arg_tileID) + 100)
        if not lt(util.sprites.stage.varCoins, self.var_t):
            util.sprites.stage.listLevelUpdates.append(arg_tileIdx)
            util.sprites.stage.listLevelUpdates.append(util.sprites.stage.listLevel[toint(arg_tileIdx)])
            util.sprites.stage.listLevel[toint(arg_tileIdx)] = self.var_t2
            await util.sprites["Level"].broadcast_updatelevel(util)
            if eq(util.sprites.stage.listLevel[toint(arg_tileIdx)], self.var_t2):
                util.sprites.stage.varNewCoins += (0 - tonum(self.var_t))

    @on_pressed('r')
    async def key_r_pressed(self, util):
        util.sprites.stage.varGameStatus = -1

    @on_broadcast('go: game on')
    async def broadcast_GoGameOn(self, util):
        util.send_broadcast("Update: Coins")
        self.costume.switch("Hidden")
        self.shown = True
        while not eq(util.sprites.stage.varGameStatus, -1):
            util.sprites.stage.varFrame += 1
            if eq(util.sprites.stage.varSelected, 0):
                self.var_X = math.floor(div((util.inputs.mouse_x + util.sprites.stage.varofx), 24))
                self.var_Y = math.floor(div((util.inputs.mouse_y + util.sprites.stage.varofy), 24))
                if ((gt(self.var_X, 0) and lt(self.var_X, (util.sprites.stage.varlsx - 1))) and (gt(self.var_Y, 0) and lt(self.var_Y, (util.sprites.stage.varlsy - 1)))):
                    if not eq(self.costume.number, 2):
                        self.costume.switch("Cursor")
                    self.gotoxy((((self.var_X * 24) - util.sprites.stage.varofx) + 12), (((self.var_Y * 24) - util.sprites.stage.varofy) + 12))
                    if util.inputs.mouse_down:
                        if gt(self.var_DrawType, -1):
                            self.var_tileIdx = (((self.var_Y * util.sprites.stage.varlsx) + self.var_X) + 1)
                            self.var_tileID = util.sprites.stage.listLevel[toint(self.var_tileIdx)]
                            if eq(self.var_tileID, 1):
                                await self.my_ReplaceTile(util, self.var_tileIdx, util.sprites.stage.listTools[toint(util.sprites.stage.varToolType)])
                            else:
                                if gt(self.var_tileID, 99):
                                    util.sprites.stage.varAction = 0
                                    util.sprites.stage.varSelected = self.var_tileIdx
                                    util.sprites.stage.varSellPrice = util.sprites.stage.list_DATA_Turrets[toint((((tonum(self.var_tileID) - 100) * util.sprites.stage.varDTMUL) + 11))]
                                    util.sprites.stage.varUpgradeTower = util.sprites.stage.list_DATA_Turrets[toint((((tonum(self.var_tileID) - 100) * util.sprites.stage.varDTMUL) + 5))]
                                    if gt(util.sprites.stage.varUpgradeTower, 0):
                                        util.sprites.stage.varUpgradePrice = util.sprites.stage.list_DATA_Turrets[toint(((tonum(util.sprites.stage.varUpgradeTower) * util.sprites.stage.varDTMUL) + 4))]
                                    else:
                                        util.sprites.stage.varUpgradePrice = 0
                                    self.costume.switch("Range5")
                                    await util.send_broadcast_wait("Do: Selected")
                                    await util.send_broadcast_wait("Do: Selected2")
                            self.var_DrawType = -1
                    else:
                        self.var_DrawType = 0
                else:
                    if not eq(self.costume.number, 1):
                        self.costume.switch("Hidden")
                    self.gotoxy(0, 0)
            else:
                if util.inputs.mouse_down:
                    if not self.get_touching(util, "_mouse_"):
                        util.sprites.stage.varAction = -1
                    self.var_DrawType = -1
                if not eq(util.sprites.stage.varAction, 0):
                    if eq(util.sprites.stage.varAction, 1):
                        await self.my_ReplaceTile(util, util.sprites.stage.varSelected, 0)
                    else:
                        if eq(util.sprites.stage.varAction, 2):
                            await self.my_ReplaceTile(util, util.sprites.stage.varSelected, util.sprites.stage.varUpgradeTower)
                    util.sprites.stage.varSellPrice = 0
                    util.sprites.stage.varUpgradePrice = 0
                    util.sprites.stage.varUpgradeTower = 0
                    await util.send_broadcast_wait("Do: Unselect")
                    util.sprites.stage.varSelected = 0
                    self.costume.switch("Cursor")
                    self.front_layer(util)
            if not eq(util.sprites.stage.varNewCoins, 0):
                util.sprites.stage.varCoins += util.sprites.stage.varNewCoins
                util.sprites.stage.varNewCoins = 0
                util.send_broadcast("Update: Coins")
            await util.send_broadcast_wait("loop")

            await self.yield_()
        await util.send_broadcast_wait("loop")
        self.shown = False
        self.gotoxy(0, 0)
        self.costume.size = 200
        self.costume.switch("GameOver")
        self.shown = True

    @warp
    async def my_Reset(self, util, ):
        util.sprites.stage.varCoins = 15
        util.sprites.stage.varNewCoins = 0
        util.sprites.stage.varLives = 20
        self.var_DrawType = 0
        util.sprites.stage.varGameStatus = 0
        util.sprites.stage.varFrame = 0

    @on_broadcast('go: user input')
    async def broadcast_GoUserInput(self, util):
        await self.my_Reset(util, )


@sprite('Mobs')
class SpriteMobs(Target):
    """Sprite Mobs"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 6.879482066290336
        self._ypos = 0.27570520671213217
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 200, "all around", [
            {
                'name': "imp",
                'path': "7d8dabfe5cc84da95d17d37a1b1ecaf6.png",
                'center': (10, 10),
                'scale': 2
            },
            {
                'name': "imp_hurt",
                'path': "c24a36f1fa572a480b6d2d1923e3d725.png",
                'center': (10, 10),
                'scale': 2
            },
            {
                'name': "imp2",
                'path': "ac5022b65c21735a0b51fbd335ff57d5.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "imp2_hurt",
                'path': "5c566dfb1ccfee664958d78064d9bd20.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "speedie",
                'path': "8413a6917f81a8f9524732266ecd8503.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "speedie_hurt",
                'path': "07b346e8bc000d8ae35cc5fb9b2969f6.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "saucer_h2",
                'path': "f8ffba102cd21c8e08dc0977d2eb8a46.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "saucer_h4",
                'path': "75a5d113d4d564a702a8acdb713f4ae3.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "saucer_h6",
                'path': "5631414294833fc7078d565ea300fb21.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "saucer_h8",
                'path': "5481be37d1467dafcff60b0baec9a0ea.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "saucer_h10",
                'path': "3d25a6766c78c15eb05d1bb5e61e6cd7.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "saucer",
                'path': "f6dfc13f3a6d6c48dd36165075ec3a04.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "saucer_hurt",
                'path': "2aa8046fc422d09a6fc23c64c77e2725.png",
                'center': (20, 18),
                'scale': 2
            },
            {
                'name': "heavy_h2",
                'path': "7048b2964c75aced4ac2f8374bb0bee0.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "heavy_h4",
                'path': "bd9c4aff9d06124875b757d477dc3f61.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "heavy_h6",
                'path': "13ea3e197a12bb0faea908fc830198f0.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "heavy_h8",
                'path': "fc9e82804f69fbc55f803245c4bceb17.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "heavy_h10",
                'path': "93f83bdf5d647dac37e230362c567657.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "speedie2",
                'path': "ba871b92263580c3bd8f438f81310099.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "speedie2_hurt",
                'path': "f010ee4ffea212891bf5fae9020ea530.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "berry_s",
                'path': "4fa0102a1fbc8901d94c13bf4c27c190.png",
                'center': (14, 14),
                'scale': 2
            },
            {
                'name': "berry_s2",
                'path': "a57bcd250efc3a8e7d34043d05f08206.png",
                'center': (14, 14),
                'scale': 2
            },
            {
                'name': "berry",
                'path': "830fe0be5086600191954ec0b9664ade.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "berry2",
                'path': "2a5936057d95996749d66feb60def968.png",
                'center': (12, 12),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_X = 9.862922352335803
        self.var_Y = 6.512710463920526
        self.var_tileIdx = 124
        self.var_SX = 0.3839267945555496
        self.var_SY = "0.16686076584952028"
        self.var_tileID = 1
        self.var_Speed = "0.015623055486008524"
        self.var_PrevTileID = 2
        self.var_PrevTileIdx = 124
        self.var_of = 3
        self.var_tcp = 1
        self.var_ID = 491
        self.var_Health = 0
        self.var_costume = 1
        self.var_Hurting = 6
        self.var_Slowed = 0
        self.var_t = "0.4186195155001587"
        self.var_Type = 0
        self.var_DMM = 15
        self.var_Wander = 0.01
        self.var_pathID = 2
        self.var_SlowResistance = 0.25
        self.var_HealthSpr = 0
        self.var_BaseCostume = 1
        self.var_PathOffset = 0



        self.sprite.layer = 1

    @warp
    async def my_InitClones(self, util, ):
        util.sprites.stage.listMobPool.delete_all()
        self.var_ID = 1
        self.var_Type = 0
        for _ in range(49):
            await self.my_cloned(util, )
            self.create_clone_of(util, "_myself_")
            self.var_ID += util.sprites.stage.varMMUL
        await self.my_cloned(util, )
        util.sprites.stage.varMobCount = 0

    @warp
    async def my_Spawn(self, util, ):
        util.sprites.stage.varMobCount += 1
        self.var_X = util.sprites.stage.listMob[toint((self.var_ID + 1))]
        self.var_Y = util.sprites.stage.listMob[toint((self.var_ID + 2))]
        self.var_PathOffset = (tonum(util.sprites.stage.listMob[toint((self.var_ID + 9))]) * util.sprites.stage.varlsz)
        if eq(self.var_X, 0):
            self.var_SX = pick_rand(0, 0.01)
            self.var_SY = str(pick_rand(-0.01, 0.01))
        else:
            self.var_SX = pick_rand(-0.01, 0.01)
            self.var_SY = str(pick_rand(-0.01, 0))
        self.var_X = tonum(self.var_X) + pick_rand(0.2, 0.8)
        self.var_Y = tonum(self.var_Y) + pick_rand(0.2, 0.8)
        self.var_PrevTileIdx = 0
        self.var_PrevTileID = 0
        self.var_Slowed = 0
        await self.my_SetupType(util, util.sprites.stage.listMob[toint((self.var_ID + 0))])
        if eq(self.var_Wander, 0):
            if lt(self.var_X, 1):
                self.var_pathID = 2
            else:
                self.var_pathID = 3
            self.front_layer(util)
        else:
            self.change_layer(util, -1000)
        util.sprites.stage.listMob[toint((self.var_ID + 7))] = self.var_SX
        util.sprites.stage.listMob[toint((self.var_ID + 8))] = self.var_SY
        self.costume.switch(util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 4))])
        self.shown = True
        self.gotoxy(toint(((tonum(self.var_X) * 24) - util.sprites.stage.varofx)), toint(((tonum(self.var_Y) * 24) - util.sprites.stage.varofy)))

    @on_broadcast('go: user input')
    async def broadcast_GoUserInput(self, util):
        self.costume.switch("imp")
        self.costume.size = 200
        await self.my_InitClones(util, )

    @on_broadcast('reset level')
    async def broadcast_ResetLevel(self, util):
        self.delete_clone(util)

    @warp
    async def my_Loop(self, util, ):
        for _ in range(toint(util.sprites.stage.varSpeed)):
            if gt(self.var_Type, 0):
                self.var_tileIdx = (((math.floor(tonum(self.var_Y)) * util.sprites.stage.varlsx) + math.floor(tonum(self.var_X))) + 1)
                if not eq(self.var_Wander, 0):
                    self.var_pathID = util.sprites.stage.listPath[toint((self.var_tileIdx + self.var_PathOffset))]
                    self.var_of = (len(str(self.var_pathID)) + 1)
                    if eq(letter_of(str(self.var_pathID), toint((self.var_of - self.var_PrevTileID))), 1):
                        if (eq(self.var_tileIdx, self.var_PrevTileIdx) or gt(pick_rand(1, 3), 1)):
                            self.var_pathID = self.var_PrevTileID
                        else:
                            await self.my_ChoosePath(util, )
                    else:
                        await self.my_ChoosePath(util, )
                if eq((tonum(self.var_pathID) % 2), 1):
                    if eq(self.var_pathID, 1):
                        self.var_SY = str(tonum(self.var_SY) + tonum(self.var_Speed))
                    else:
                        self.var_SY = str(tonum(self.var_SY) + (0 - tonum(self.var_Speed)))
                    if gt(self.var_Wander, 0):
                        self.var_SX += pick_rand((0 - tonum(self.var_Wander)), tonum(self.var_Wander))
                    else:
                        self.var_SX += (((tonum(self.var_X) % 1) - 0.5) * -0.01)
                else:
                    if eq(self.var_pathID, 2):
                        self.var_SX += tonum(self.var_Speed)
                    else:
                        self.var_SX += (0 - tonum(self.var_Speed))
                    if gt(self.var_Wander, 0):
                        self.var_SY = str(tonum(self.var_SY) + pick_rand((0 - tonum(self.var_Wander)), tonum(self.var_Wander)))
                    else:
                        self.var_SY = str(tonum(self.var_SY) + (((tonum(self.var_Y) % 1) - 0.5) * -0.01))
                if gt(self.var_pathID, 0):
                    self.var_SX = (self.var_SX * 0.83)
                    self.var_SY = str((tonum(self.var_SY) * 0.83))
                if (gt((tonum(self.var_X) + self.var_SX), util.sprites.stage.varlsx) or lt((tonum(self.var_Y) + tonum(self.var_SY)), 0)):
                    await self.my_DeSpawn(util, )
                    util.sprites.stage.varLives += -1
                    if lt(util.sprites.stage.varLives, 1):
                        util.sprites.stage.varGameStatus = -1
                else:
                    if eq(self.var_Wander, 0):
                        self.var_tileID = 10
                    else:
                        self.var_tileID = util.sprites.stage.listLevel[toint(self.var_tileIdx)]
                    if gt(self.var_Slowed, 0):
                        self.var_t = str((self.var_SlowResistance * self.var_SX))
                    else:
                        self.var_t = str(self.var_SX)
                    if (gt(self.var_tileID, 9) or lt(util.sprites.stage.listLevel[toint((((math.floor(tonum(self.var_Y)) * util.sprites.stage.varlsx) + math.floor((tonum(self.var_X) + tonum(self.var_t)))) + 1))], 10)):
                        self.var_X = tonum(self.var_X) + tonum(self.var_t)
                        if lt(self.var_X, 0):
                            self.var_X = 0
                        util.sprites.stage.listMob[toint((self.var_ID + 7))] = self.var_t
                    if gt(self.var_Slowed, 0):
                        self.var_t = str((0.6 * tonum(self.var_SY)))
                        self.var_Slowed = tonum(self.var_Slowed) + -1
                        if lt(self.var_Slowed, 1):
                            util.sprites.stage.listMob[toint((self.var_ID + 6))] = 0
                    else:
                        self.var_t = self.var_SY
                    if (gt(self.var_tileID, 9) or lt(util.sprites.stage.listLevel[toint((((math.floor((tonum(self.var_Y) + tonum(self.var_t))) * util.sprites.stage.varlsx) + math.floor(tonum(self.var_X))) + 1))], 10)):
                        self.var_Y = tonum(self.var_Y) + tonum(self.var_t)
                        if gt(self.var_Y, (util.sprites.stage.varlsy - 0.1)):
                            self.var_Y = (util.sprites.stage.varlsy - 0.1)
                        util.sprites.stage.listMob[toint((self.var_ID + 8))] = self.var_t
                if gt(self.var_Type, 0):
                    if gt(util.sprites.stage.listMob[toint((self.var_ID + 3))], 0):
                        self.var_Hurting = 6
                        self.var_Health += (0 - tonum(util.sprites.stage.listMob[toint((self.var_ID + 3))]))
                        self.var_SX += tonum(util.sprites.stage.listMob[toint((self.var_ID + 4))])
                        self.var_SY = str(tonum(self.var_SY) + tonum(util.sprites.stage.listMob[toint((self.var_ID + 5))]))
                        self.var_t = str(sqrt(((self.var_SX * self.var_SX) + (tonum(self.var_SY) * tonum(self.var_SY)))))
                        if gt(self.var_t, 0.8):
                            self.var_t = str(div(self.var_t, 0.8))
                            self.var_SX = div(self.var_SX, self.var_t)
                            self.var_SY = str(div(self.var_SY, self.var_t))
                        util.sprites.stage.listMob[toint((self.var_ID + 3))] = 0
                        util.sprites.stage.listMob[toint((self.var_ID + 4))] = 0
                        util.sprites.stage.listMob[toint((self.var_ID + 5))] = 0
                        if (lt(self.var_Slowed, 1) and gt(util.sprites.stage.listMob[toint((self.var_ID + 6))], 0)):
                            self.var_Slowed = util.sprites.stage.listMob[toint((self.var_ID + 6))]
                    util.sprites.stage.listMob[toint((self.var_ID + 1))] = self.var_X
                    util.sprites.stage.listMob[toint((self.var_ID + 2))] = self.var_Y
                    if lt(self.var_Health, 0):
                        util.sprites.stage.varNewCoins += tonum(util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 3))])
                        if eq(util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 14))], 0):
                            await self.my_DeSpawn(util, )
                        else:
                            await self.my_SetupType(util, util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 14))])
                    else:
                        pass
        if gt(self.var_Type, 0):
            self.var_costume = self.var_BaseCostume
            if gt(self.var_Hurting, 0):
                self.var_Hurting += (0 - util.sprites.stage.varSpeed)
                if eq(self.var_HealthSpr, 0):
                    self.var_costume = tonum(self.var_costume) + 1
            if gt(self.var_HealthSpr, 0):
                self.var_costume = tonum(self.var_costume) + math.floor((self.var_Health * tonum(self.var_HealthSpr)))
            self.gotoxy(((tonum(self.var_X) * 24) - util.sprites.stage.varofx), ((tonum(self.var_Y) * 24) - util.sprites.stage.varofy))
            if gt(util.sprites.stage.varGraphics, 0):
                if not eq(self.var_costume, self.costume.number):
                    self.costume.switch(self.var_costume)

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False

    @on_broadcast('do: unselect')
    async def broadcast_DoUnselect(self, util):
        if eq(self.var_Wander, 0):
            self.front_layer(util)
        else:
            self.change_layer(util, -1000)

    @warp
    async def my_SetupType(self, util, arg_typeId):
        self.var_Type = arg_typeId
        self.var_DMM = (tonum(arg_typeId) * util.sprites.stage.varDMMUL)
        self.var_Hurting = 0
        util.sprites.stage.listMob[toint((self.var_ID + 0))] = arg_typeId
        util.sprites.stage.listMob[toint((self.var_ID + 3))] = 0
        util.sprites.stage.listMob[toint((self.var_ID + 4))] = 0
        util.sprites.stage.listMob[toint((self.var_ID + 5))] = 0
        util.sprites.stage.listMob[toint((self.var_ID + 6))] = 0
        self.var_BaseCostume = util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 4))]
        self.var_Health = (util.sprites.stage.varDiffMul * tonum(util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 5))]))
        self.var_Speed = str(div(util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 6))], 100))
        self.var_Speed = str(tonum(self.var_Speed) + pick_rand(0, 0.001))
        self.var_Wander = util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 8))]
        self.var_SlowResistance = (1 - div(0.75, util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 11))]))
        self.var_HealthSpr = util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 13))]
        if gt(self.var_HealthSpr, 0):
            self.var_HealthSpr = div((tonum(util.sprites.stage.list_DATA_Mobs[toint((self.var_DMM + 13))]) - 0.1), self.var_Health)

    @warp
    async def my_DeSpawn(self, util, ):
        self.shown = False
        self.var_Health = 0
        self.var_Type = 0
        util.sprites.stage.listMob[toint((self.var_ID + 0))] = 0
        util.sprites.stage.listMobPool.append(self.var_ID)
        util.sprites.stage.varMobCount += -1

    @warp
    async def my_ChoosePath(self, util, ):
        self.var_PrevTileIdx = self.var_pathID
        if eq(self.var_pathID, 0):
            self.var_PrevTileID = 0
        else:
            self.var_t = str(len(str(self.var_pathID)))
            self.var_PrevTileID = pick_rand(1, tonum(self.var_t))
            for _ in range(toint(pick_rand(1, 2))):
                self.var_PrevTileID = ((self.var_PrevTileID % tonum(self.var_t)) + 1)
                self.var_tcp = 0
                while not (eq(letter_of(str(self.var_pathID), toint((self.var_of - self.var_PrevTileID))), 1) or gt(self.var_tcp, self.var_t)):
                    self.var_PrevTileID = ((self.var_PrevTileID % tonum(self.var_t)) + 1)
                    self.var_tcp += 1
            self.var_pathID = self.var_PrevTileID
        self.var_PrevTileIdx = self.var_tileIdx

    @warp
    async def my_cloned(self, util, ):
        for _ in range(toint(util.sprites.stage.varMMUL)):
            util.sprites.stage.listMob.append("")
        util.sprites.stage.listMob[toint((self.var_ID + 0))] = 0
        util.sprites.stage.listMobPool.append(self.var_ID)

    @on_broadcast('loop')
    async def broadcast_loop(self, util):
        if gt(self.var_Type, 0):
            await self.my_Loop(util, )
        else:
            if gt(util.sprites.stage.listMob[toint((self.var_ID + 0))], 0):
                await self.my_Spawn(util, )


@sprite('Gun1')
class SpriteGun1(Target):
    """Sprite Gun1"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -100
        self._ypos = -180
        self._direction = 0
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           29, 200, "all around", [
            {
                'name': "gun",
                'path': "7020b111e4945270b1259750a0576f93.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "gun_s1",
                'path': "6dca63d44f79b7f7e479750c9eb28b23.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "gun_s2",
                'path': "66cbb58e8ead1c2bcfdfce056d46a0e4.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "rocket",
                'path': "9cab2b6d5f56fe3b605b8ad610d2e9dd.png",
                'center': (14, 12),
                'scale': 2
            },
            {
                'name': "rocket2",
                'path': "9cab2b6d5f56fe3b605b8ad610d2e9dd.png",
                'center': (16, 12),
                'scale': 2
            },
            {
                'name': "rocket3",
                'path': "9cab2b6d5f56fe3b605b8ad610d2e9dd.png",
                'center': (16, 12),
                'scale': 2
            },
            {
                'name': "glue",
                'path': "adbe40cf7720f35ae1fb44e9c2195486.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "glue_s1",
                'path': "2c1f4589b56d252328bf8cb5bc0d3464.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "glue_s2",
                'path': "e17479ce8e5bf658961ca3432d78b399.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "gun_a",
                'path': "93203b0291ddc689c420d962bcf848e6.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "gun_a_s1",
                'path': "d79bd3ff72748c2eed7cbf8e8e154d3e.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "gun_a_s2",
                'path': "d79bd3ff72748c2eed7cbf8e8e154d3e.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "gun_c",
                'path': "0ef8b95a96e72350bf53ffba10eefb24.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "gun_c_s1",
                'path': "c2f7feed7ca1b5490dab02c003b58788.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "gun_c_s2",
                'path': "8924b6716df9f7c6790aa93419ef2f40.png",
                'center': (12, 12),
                'scale': 2
            },
            {
                'name': "glue_b",
                'path': "6a8b22ae916c471f3b471cd97defdad0.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "glue_b_s1",
                'path': "f49aa2999f1737a219e442b1cd8cc326.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "glue_b_s2",
                'path': "bb3b51008748b349fc71d72b091f6db1.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "glue_c",
                'path': "86f536f69539703de203d2098cf98bb1.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "glue_c_s1",
                'path': "ab047ed2169bd9947f67a5d9944b25c8.png",
                'center': (16, 18),
                'scale': 2
            },
            {
                'name': "glue_c_s2",
                'path': "2fe59170d1ae29afa2f4aaaf56b6d4e3.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "rocket_b",
                'path': "5cb1c6ce1f1ceb889cb412ea0a2fdc4a.png",
                'center': (14, 12),
                'scale': 2
            },
            {
                'name': "rocket_b2",
                'path': "5cb1c6ce1f1ceb889cb412ea0a2fdc4a.png",
                'center': (16, 12),
                'scale': 2
            },
            {
                'name': "rocket_b3",
                'path': "5cb1c6ce1f1ceb889cb412ea0a2fdc4a.png",
                'center': (16, 12),
                'scale': 2
            },
            {
                'name': "rocket_c",
                'path': "8e8e80a1086a1651b0fa96ca03daefb4.png",
                'center': (14, 14),
                'scale': 2
            },
            {
                'name': "rocket_c2",
                'path': "8e8e80a1086a1651b0fa96ca03daefb4.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "rocket_c3",
                'path': "8e8e80a1086a1651b0fa96ca03daefb4.png",
                'center': (16, 14),
                'scale': 2
            },
            {
                'name': "Tesla",
                'path': "84daf649ec5a46857575e6c0c077ad4d.png",
                'center': (14, 14),
                'scale': 2
            },
            {
                'name': "Tesla_s1",
                'path': "7999d4c7f38efde4867935b2a096d12c.png",
                'center': (16, 16),
                'scale': 2
            },
            {
                'name': "Tesla_s2",
                'path': "e7fa5370f6ad03a1c9a2813d63e1090a.png",
                'center': (16, 16),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])

        self.var_TileIdx = 248
        self.var_i = 451
        self.var_IsClone = 0
        self.var_X = 0
        self.var_Y = 0
        self.var_LockMobID = 0
        self.var_GetDirection = 19.657489447947555
        self.var_distance = 3.1526578916842274
        self.var_bestDir = 999
        self.var_ShootWait = -1264185
        self.var_Status = 0
        self.var_costume = "6 - Turret Base Costume #"
        self.var_Angle = 0
        self.var_Type = 0
        self.var_RotSpeed = 5
        self.var_Range = 0
        self.var_ID = 0
        self.var_TT = 0
        self.var_BaseType = 0
        self.var_Resistance = 0
        self.var_ReloadTime = 0

        self.listMobTiles = List(
            []
        )

        self.sprite.layer = 5

    @on_broadcast('init: creeate level list')
    async def broadcast_InitCreeateLevelList(self, util):
        self.costume.size = 200
        self.shown = False
        self.listMobTiles.delete_all()
        self.var_TileIdx = 0
        self.var_IsClone = 0
        self.var_LockMobID = 0
        self.var_Status = 0
        self.var_Angle = 0
        self.var_ID = 0
        self.direction = 0

    @warp
    async def my_CloneTime(self, util, ):
        self.var_TileIdx = 1
        while not gt(self.var_TileIdx, len(util.sprites.stage.listLevel)):
            if gt(util.sprites.stage.listLevel[toint(self.var_TileIdx)], 100):
                if eq(0, util.sprites.stage.listGunClones[toint(self.var_TileIdx)]):
                    util.sprites.stage.listGunClones[toint(self.var_TileIdx)] = 1
                    self.var_ID += 1
                    self.create_clone_of(util, "_myself_")
            self.var_TileIdx += 1

    @on_clone_start
    async def clone_start(self, util):
        await self.my_Init(util, )

    @on_broadcast('do: selected')
    async def broadcast_DoSelected(self, util):
        if eq(util.sprites.stage.varSelected, self.var_TileIdx):
            self.front_layer(util)

    @warp
    async def my_Init(self, util, ):
        self.var_IsClone = 1
        self.var_X = (((self.var_TileIdx - 1) % util.sprites.stage.varlsx) + 0.5)
        self.var_Y = (math.floor(div((self.var_TileIdx - 1), util.sprites.stage.varlsx)) + 0.5)
        self.var_ShootWait = 0
        self.var_Type = (tonum(util.sprites.stage.listLevel[toint(self.var_TileIdx)]) - 100)
        self.var_TT = (self.var_Type * util.sprites.stage.varDTMUL)
        self.var_RotSpeed = util.sprites.stage.list_DATA_Turrets[toint((self.var_TT + 9))]
        self.var_Range = util.sprites.stage.list_DATA_Turrets[toint((self.var_TT + 8))]
        self.var_ReloadTime = util.sprites.stage.list_DATA_Turrets[toint((self.var_TT + 12))]
        self.var_BaseType = util.sprites.stage.list_DATA_Turrets[toint((self.var_TT + 2))]
        self.gotoxy((((self.var_X * 24) - util.sprites.stage.varofx) + 1), (((self.var_Y * 24) - util.sprites.stage.varofy) - 1))
        await self.my_Loop2(util, not False, 1)
        self.shown = True

    @on_broadcast('update: guns')
    async def broadcast_updateguns1(self, util):
        if eq(self.var_IsClone, 0):
            await self.my_CloneTime(util, )
        else:
            if not eq(util.sprites.stage.listLevel[toint(self.var_TileIdx)], (self.var_Type + 100)):
                if eq(util.sprites.stage.listLevel[toint(self.var_TileIdx)], 1):
                    util.sprites.stage.listGunClones[toint(self.var_TileIdx)] = 0
                    self.delete_clone(util)
                else:
                    await self.my_Init(util, )

    @warp
    async def my_GetDirection(self, util, arg_dx, arg_dy, arg_maxDist):
        self.var_distance = sqrt(((tonum(arg_dx) * tonum(arg_dx)) + (tonum(arg_dy) * tonum(arg_dy))))
        if lt(self.var_distance, arg_maxDist):
            if eq(arg_dy, 0):
                if gt(arg_dx, 0):
                    self.var_GetDirection = 90
                else:
                    self.var_GetDirection = -90
            else:
                self.var_GetDirection = math.degrees(math.atan(div(arg_dx, arg_dy)))
                if lt(arg_dy, 0):
                    if gt(arg_dx, 0):
                        self.var_GetDirection += 180
                    else:
                        if lt(arg_dx, 0):
                            self.var_GetDirection += -180
                        else:
                            self.var_GetDirection = 180

    @warp
    async def my_GetDirectionMissile(self, util, arg_dx, arg_dy, arg_maxDist):
        self.var_distance = sqrt(((arg_dx * arg_dx) + (arg_dy * arg_dy)))
        self.var_bestDir = util.sprites.stage.listMob[toint((self.var_LockMobID + 0))]
        self.var_bestDir = (self.var_distance * 4.6)
        await self.my_GetDirection(util, (arg_dx + (tonum(self.var_bestDir) * tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 7))]))), (arg_dy + (tonum(self.var_bestDir) * tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 8))]))), arg_maxDist)

    @warp
    async def my_Loop2(self, util, arg_force, arg_loop):
        for _ in range(toint(arg_loop)):
            self.var_costume = util.sprites.stage.list_DATA_Turrets[toint((self.var_TT + 6))]
            self.var_ShootWait = tonum(self.var_ShootWait) + -1
            if eq(self.var_LockMobID, 0):
                await self.my_FindLockTarget(util, )
            else:
                if gt(self.var_LockMobID, 0):
                    if eq(util.sprites.stage.listMob[toint((self.var_LockMobID + 0))], 0):
                        self.var_LockMobID = 0
            if lt(self.var_LockMobID, 1):
                self.var_LockMobID += -1
                if lt(self.var_LockMobID, -4):
                    self.var_LockMobID = 0
            else:
                if eq(self.var_BaseType, 3):
                    await self.my_GetDirectionMissile(util, (tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 1))]) - self.var_X), (tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 2))]) - self.var_Y), (tonum(self.var_Range) * 2))
                else:
                    await self.my_GetDirection(util, (tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 1))]) - self.var_X), (tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 2))]) - self.var_Y), self.var_Range)
                if lt(self.var_distance, self.var_Range):
                    if (eq(self.var_BaseType, 1) or lt(self.var_ShootWait, 0)):
                        if lt((((self.var_GetDirection - self.var_Angle) + tonum(self.var_RotSpeed)) % 360), (tonum(self.var_RotSpeed) * 2)):
                            self.var_Angle = self.var_GetDirection
                            if lt(self.var_ShootWait, 1):
                                self.var_costume = tonum(self.var_costume) + (1 + self.var_Status)
                                if lt(self.var_ShootWait, -9999):
                                    self.var_Status = (1 - self.var_Status)
                                    if (eq(self.var_BaseType, 1) or eq(self.var_BaseType, 4)):
                                        if eq(self.var_BaseType, 4):
                                            await self.my_Launch(util, 2)
                                        else:
                                            util.sprites.stage.varSoundMachine += 1
                                        self.var_ShootWait = self.var_ReloadTime
                                        util.sprites.stage.listMob[toint((self.var_LockMobID + 3))] = (tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 3))]) + div(util.sprites.stage.list_DATA_Turrets[toint((self.var_TT + 10))], self.var_Resistance))
                                        if eq(self.var_BaseType, 4):
                                            self.var_LockMobID = 0
                                    else:
                                        if eq(self.var_BaseType, 3):
                                            await self.my_Launch(util, 1)
                                            self.var_ShootWait = self.var_ReloadTime
                                            self.var_LockMobID = 0
                                        else:
                                            util.sprites.stage.varSoundGlue += 1
                                            util.sprites.stage.listMob[toint((self.var_LockMobID + 6))] = (tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 6))]) + 70)
                                            util.sprites.stage.listMob[toint((self.var_LockMobID + 3))] = (tonum(util.sprites.stage.listMob[toint((self.var_LockMobID + 3))]) + tonum(util.sprites.stage.list_DATA_Turrets[toint((self.var_TT + 10))]))
                                            self.var_ShootWait = self.var_ReloadTime
                                            self.var_LockMobID = 0
                                else:
                                    self.var_ShootWait = -9999
                        else:
                            if lt(((self.var_GetDirection - self.var_Angle) % 360), 180):
                                self.var_Angle += tonum(self.var_RotSpeed)
                            else:
                                self.var_Angle += (0 - tonum(self.var_RotSpeed))
                else:
                    self.var_LockMobID = 0
        if (arg_force or (gt(util.sprites.stage.varGraphics, 0) and eq(((self.var_ID + util.sprites.stage.varFrame) % util.sprites.stage.varGraphics), 0))):
            if (not eq(self.direction, self.var_Angle) and not eq(self.var_BaseType, 4)):
                self.direction = self.var_Angle
            if not eq(self.costume.number, self.var_costume):
                self.costume.switch(self.var_costume)

    @warp
    async def my_Launch(self, util, arg_type):
        self.var_i = 1
        while not gt(self.var_i, len(util.sprites.stage.listRockets)):
            if eq(util.sprites.stage.listRockets[toint(self.var_i)], 0):
                util.sprites.stage.listRockets[toint(self.var_i)] = 0
                util.sprites.stage.listRockets[toint((self.var_i + 1))] = self.var_X
                util.sprites.stage.listRockets[toint((self.var_i + 2))] = self.var_Y
                util.sprites.stage.listRockets[toint((self.var_i + 3))] = self.var_Angle
                util.sprites.stage.listRockets[toint((self.var_i + 4))] = self.var_distance
                util.sprites.stage.listRockets[toint(self.var_i)] = arg_type
                self.var_i = 99999
            self.var_i += util.sprites.stage.varRMUL

    @warp
    async def my_FindLockTarget(self, util, ):
        self.var_i = 1
        self.var_bestDir = 999
        self.var_LockMobID = 0
        while not gt(self.var_i, len(util.sprites.stage.listMob)):
            if gt(util.sprites.stage.listMob[toint((self.var_i + 0))], 0):
                if (not eq(self.var_BaseType, 2) or lt(util.sprites.stage.listMob[toint((self.var_i + 6))], 1)):
                    if lt(abs((tonum(util.sprites.stage.listMob[toint((self.var_i + 1))]) - self.var_X)), self.var_Range):
                        if lt(abs((tonum(util.sprites.stage.listMob[toint((self.var_i + 2))]) - self.var_Y)), self.var_Range):
                            await self.my_GetDirection(util, (tonum(util.sprites.stage.listMob[toint((self.var_i + 1))]) - self.var_X), (tonum(util.sprites.stage.listMob[toint((self.var_i + 2))]) - self.var_Y), self.var_Range)
                            if lt(self.var_distance, self.var_Range):
                                self.var_GetDirection = abs(((((self.var_GetDirection - self.var_Angle) + 180) % 360) - 180))
                                if lt(self.var_GetDirection, self.var_bestDir):
                                    self.var_LockMobID = self.var_i
                                    self.var_bestDir = self.var_GetDirection
            self.var_i += util.sprites.stage.varMMUL
        if gt(self.var_LockMobID, 0):
            if eq(self.var_BaseType, 4):
                self.var_Resistance = 1.0
            else:
                self.var_Resistance = util.sprites.stage.listMob[toint((self.var_LockMobID + 0))]
                self.var_Resistance = util.sprites.stage.list_DATA_Mobs[toint(((tonum(self.var_Resistance) * util.sprites.stage.varDMMUL) + (9 + tonum(self.var_BaseType))))]

    @on_broadcast('reset level')
    async def broadcast_ResetLevel(self, util):
        self.delete_clone(util)

    @on_broadcast('loop')
    async def broadcast_loop(self, util):
        if gt(self.var_IsClone, 0):
            await self.my_Loop2(util, False, util.sprites.stage.varSpeed)
        else:
            pass


@sprite('rocket')
class Spriterocket(Target):
    """Sprite rocket"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 244
        self._ypos = 43
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 200, "all around", [
            {
                'name': "Rocket",
                'path': "3888b3959137d532c29f1997a209ffd3.png",
                'center': (12, 6),
                'scale': 2
            },
            {
                'name': "Bang!",
                'path': "06a2d9bdc440539d6e414632b3c1ab21.svg",
                'center': (12, 10),
                'scale': 1
            },
            {
                'name': "ligtning1",
                'path': "fa845d3dc36bccb860800ccde22562fb.png",
                'center': (4, 10),
                'scale': 2
            },
            {
                'name': "ligtning2",
                'path': "79678d4bc14b4c3794a3ba0628d754df.png",
                'center': (4, 10),
                'scale': 2
            },
            {
                'name': "ligtning3",
                'path': "39ffbc70c4ed1d5a4be980365c353b08.png",
                'center': (4, 12),
                'scale': 2
            },
            {
                'name': "ligtning4",
                'path': "3f153484e08a91a4b93b891d1ce0e7ed.png",
                'center': (4, 14),
                'scale': 2
            },
            {
                'name': "ligtning5",
                'path': "3478cf6c0552ad7c1443cfdbf74a1a05.png",
                'center': (4, 14),
                'scale': 2
            },
            {
                'name': "ligtning6",
                'path': "7a228793a2c2abc4db3e131f51574513.png",
                'center': (4, 16),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "47251__nthompson__rocket",
                'path': "fcad23f639bf78176a709858cced9c80.wav"
            },
            {
                'name': "755__elmomo__missile01",
                'path': "6c34830a9675c2806e44b33bfb614fed.wav"
            },
            {
                'name': "101961__cgeffex__heavy-machine-gun",
                'path': "fea371ae541fdde34d993b0c84077704.wav"
            },
            {
                'name': "explosion",
                'path': "e246b6597a49d23c1169bdef12166c8b.wav"
            },
            {
                'name': "tesla",
                'path': "f40ca44eb93e4c4609e6abb75e5a872e.wav"
            }
        ])

        self.var_ID = 115
        self.var_Type = ""
        self.var_X = 0
        self.var_Y = 0
        self.var_Range = 0
        self.var_i = 0
        self.var_GetDirection = 0
        self.var_distance = 0
        self.var_Resistance = 0



        self.sprite.layer = 16

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False
        self.costume.size = 200
        self.front_layer(util)
        self.var_Type = ""

    @warp
    async def my_Loop(self, util, ):
        for _ in range(toint(util.sprites.stage.varSpeed)):
            if eq(self.var_Type, 1):
                self.var_X = tonum(self.var_X) + (0.2 * math.sin(math.radians(self.direction)))
                self.var_Y = tonum(self.var_Y) + (0.2 * math.cos(math.radians(self.direction)))
                self.gotoxy(((tonum(self.var_X) * 24) - util.sprites.stage.varofx), ((tonum(self.var_Y) * 24) - util.sprites.stage.varofy))
                self.var_Range = tonum(self.var_Range) + -0.2
                if not gt(self.var_Range, 0):
                    self.costume.switch("Bang!")
                    self.sounds.play("explosion")
                    self.var_Type = 99
                    self.var_Range = 3
                    await self.my_Explode(util, 1.2, 0.4, 4)
            else:
                self.var_Range = tonum(self.var_Range) + -1
                if lt(self.var_Range, 1):
                    self.shown = False
                    util.sprites.stage.listRockets[toint(self.var_ID)] = 0
                    self.var_Type = ""

    @on_broadcast('reset level')
    async def broadcast_ResetLevel(self, util):
        util.sprites.stage.listRockets[toint(self.var_ID)] = 0
        self.var_Type = ""
        self.shown = False

    @on_broadcast('initclones')
    async def broadcast_InitClones(self, util):
        await self.my_InitClone(util, )

    @warp
    async def my_GetDirection(self, util, arg_dx, arg_dy, arg_maxDist):
        self.var_distance = sqrt(((arg_dx * arg_dx) + (arg_dy * arg_dy)))
        if lt(self.var_distance, arg_maxDist):
            if eq(arg_dy, 0):
                if gt(arg_dx, 0):
                    self.var_GetDirection = 90
                else:
                    self.var_GetDirection = -90
            else:
                self.var_GetDirection = math.degrees(math.atan(div(arg_dx, arg_dy)))
                if lt(arg_dy, 0):
                    if gt(arg_dx, 0):
                        self.var_GetDirection += 180
                    else:
                        if lt(arg_dx, 0):
                            self.var_GetDirection += -180
                        else:
                            self.var_GetDirection = 180

    @warp
    async def my_InitClone(self, util, ):
        self.costume.switch("Rocket")
        util.sprites.stage.listRockets.delete_all()
        self.var_ID = 1
        for _ in range(19):
            await self.my_cloned(util, )
            self.create_clone_of(util, "_myself_")
            self.var_ID += util.sprites.stage.varRMUL
        await self.my_cloned(util, )

    @warp
    async def my_Init(self, util, ):
        self.var_Type = util.sprites.stage.listRockets[toint(self.var_ID)]
        self.var_X = util.sprites.stage.listRockets[toint((self.var_ID + 1))]
        self.var_Y = util.sprites.stage.listRockets[toint((self.var_ID + 2))]
        self.var_Range = util.sprites.stage.listRockets[toint((self.var_ID + 4))]
        self.gotoxy(((tonum(self.var_X) * 24) - util.sprites.stage.varofx), ((tonum(self.var_Y) * 24) - util.sprites.stage.varofy))
        self.direction = tonum(util.sprites.stage.listRockets[toint((self.var_ID + 3))])
        if eq(self.var_Type, 1):
            self.sounds.set_volume(50)
            self.sounds.play("755__elmomo__missile01")
            self.costume.switch("Rocket")
        else:
            self.sounds.set_volume(50)
            self.sounds.play("tesla")
            self.costume.switch(toint((2.1 + tonum(self.var_Range))))
            self.var_Range = 3
        await self.my_Loop(util, )
        self.shown = True

    @warp
    async def my_Explode(self, util, arg_range, arg_force, arg_damage):
        self.var_i = 1
        while not gt(self.var_i, len(util.sprites.stage.listMob)):
            if gt(util.sprites.stage.listMob[toint((self.var_i + 0))], 0):
                if lt(abs((tonum(util.sprites.stage.listMob[toint((self.var_i + 1))]) - tonum(self.var_X))), arg_range):
                    if lt(abs((tonum(util.sprites.stage.listMob[toint((self.var_i + 2))]) - tonum(self.var_Y))), arg_range):
                        await self.my_GetDirection(util, (tonum(util.sprites.stage.listMob[toint((self.var_i + 1))]) - tonum(self.var_X)), (tonum(util.sprites.stage.listMob[toint((self.var_i + 2))]) - tonum(self.var_Y)), arg_range)
                        if lt(self.var_distance, arg_range):
                            self.var_Resistance = util.sprites.stage.listMob[toint(self.var_i)]
                            self.var_Resistance = util.sprites.stage.list_DATA_Mobs[toint(((tonum(self.var_Resistance) * util.sprites.stage.varDMMUL) + 12))]
                            self.var_distance = div((arg_range - self.var_distance), arg_range)
                            util.sprites.stage.listMob[toint((self.var_i + 3))] = (tonum(util.sprites.stage.listMob[toint((self.var_i + 3))]) + div((arg_damage * self.var_distance), self.var_Resistance))
                            self.var_distance = (self.var_distance * tonum(util.sprites.stage.list_DATA_Mobs[toint(((tonum(util.sprites.stage.listMob[toint((self.var_i + 0))]) * util.sprites.stage.varDMMUL) + 9))]))
                            util.sprites.stage.listMob[toint((self.var_i + 4))] = (tonum(util.sprites.stage.listMob[toint((self.var_i + 4))]) + ((arg_force * self.var_distance) * math.sin(math.radians(self.var_GetDirection))))
                            util.sprites.stage.listMob[toint((self.var_i + 5))] = (tonum(util.sprites.stage.listMob[toint((self.var_i + 5))]) + ((arg_force * self.var_distance) * math.cos(math.radians(self.var_GetDirection))))
            self.var_i += util.sprites.stage.varMMUL

    @warp
    async def my_cloned(self, util, ):
        util.sprites.stage.listRockets.append(0)
        for _ in range(toint((util.sprites.stage.varRMUL - 1))):
            util.sprites.stage.listRockets.append("")

    @on_broadcast('loop')
    async def broadcast_loop(self, util):
        if eq(self.var_Type, ""):
            if gt(util.sprites.stage.listRockets[toint(self.var_ID)], 0):
                await self.my_Init(util, )
        else:
            await self.my_Loop(util, )


@sprite('font')
class Spritefont(Target):
    """Sprite font"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -85
        self._ypos = -37
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           5, 100, "all around", [
            {
                'name': "font",
                'path': "87d55bd1677024a4a3be6d44aaaa0ddc.png",
                'center': (460, 8),
                'scale': 2
            },
            {
                'name': "0",
                'path': "876e2d39d75895b0070b809786ec8af8.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "1",
                'path': "0d96c550920ad2fb9657dbed2d25c4b3.png",
                'center': (6, 8),
                'scale': 2
            },
            {
                'name': "2",
                'path': "5992ac15576f1a630fabd1147556d6ec.png",
                'center': (10, 8),
                'scale': 2
            },
            {
                'name': "3",
                'path': "aab23113707a698626b6d2e0db6d70d7.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "4",
                'path': "7ddfb60a958f21bee7d834321cc15728.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "5",
                'path': "cb8b676dc8163dbc4661cfc69981543d.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "6",
                'path': "26ab7738f70ed78b395d70b5a6314a43.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "7",
                'path': "d14968e8cf801026ca685207c8c15ab5.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "8",
                'path': "8a731f2c8a223e6e56131807e4088efb.png",
                'center': (8, 8),
                'scale': 2
            },
            {
                'name': "9",
                'path': "6684073edc0fba4f5313a9445564485b.png",
                'center': (10, 8),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_ID = 1
        self.var_Type = "B"
        self.var_Visible = 0



        self.sprite.layer = 14

    @on_green_flag
    async def green_flag(self, util):
        self.var_Visible = 0
        self.costume.size = 200
        self.shown = False

    @warp
    async def my_Init(self, util, ):
        if eq(self.var_Type, "C"):
            self.gotoxy((-184 + (self.var_ID * 14)), -167)
        else:
            if eq(self.var_Type, "W"):
                self.gotoxy((36 + (self.var_ID * 14)), 166)
            else:
                if eq(self.var_Type, "L"):
                    self.gotoxy((166 + (self.var_ID * 14)), 166)
                else:
                    self.costume.size = 100

    @on_broadcast('init: clone level tiles')
    async def broadcast_InitCloneLevelTiles(self, util):
        await self.my_Clone(util, )
        util.send_broadcast("Update: Coins")

    @on_clone_start
    async def clone_start(self, util):
        await self.my_Init(util, )

    @warp
    async def my_Clone(self, util, ):
        self.var_Type = "C"
        self.var_ID = 4
        for _ in range(4):
            self.create_clone_of(util, "_myself_")
            self.var_ID += -1
        self.var_Type = "W"
        self.var_ID = 3
        for _ in range(3):
            self.create_clone_of(util, "_myself_")
            self.var_ID += -1
        self.var_Type = "L"
        self.var_ID = 2
        for _ in range(2):
            self.create_clone_of(util, "_myself_")
            self.var_ID += -1
        self.var_Type = "S"
        self.var_ID = 2
        for _ in range(2):
            self.create_clone_of(util, "_myself_")
            self.var_ID += -1
        self.var_Type = "B"
        self.var_ID = 3
        for _ in range(2):
            self.create_clone_of(util, "_myself_")
            self.var_ID += -1
        await self.my_Init(util, )

    @on_broadcast('do: selected')
    async def broadcast_DoSelected(self, util):
        if eq(self.var_Type, "S"):
            if gt(util.sprites.stage.varSellPrice, 0):
                self.gotoxy(((util.sprites["Cursor"].xpos - (37 + (len(str(util.sprites.stage.varSellPrice)) * 4))) + (self.var_ID * 7)), (util.sprites["Cursor"].ypos + 11))
                await self.my_Update(util, util.sprites.stage.varSellPrice)
                self.front_layer(util)
            else:
                self.shown = False
                self.var_Visible = 0
        else:
            if eq(self.var_Type, "B"):
                if gt(util.sprites.stage.varUpgradePrice, 0):
                    self.gotoxy(((util.sprites["Cursor"].xpos + (32 - (len(str(util.sprites.stage.varUpgradePrice)) * 4))) + (self.var_ID * 7)), (util.sprites["Cursor"].ypos + 11))
                    await self.my_Update(util, util.sprites.stage.varUpgradePrice)
                    self.front_layer(util)
                else:
                    self.shown = False
                    self.var_Visible = 0
            else:
                pass

    @on_broadcast('do: unselect')
    async def broadcast_DoUnselect(self, util):
        if eq(self.var_Type, "S"):
            self.shown = False
            self.var_Visible = 0
        else:
            if eq(self.var_Type, "B"):
                self.shown = False
                self.var_Visible = 0
            else:
                pass

    @on_broadcast('do: selected2')
    async def broadcast_doselected2_1(self, util):
        self.front_layer(util)

    @on_broadcast('loop')
    async def broadcast_loop(self, util):
        if eq(self.var_Type, "C"):
            await self.my_Update(util, util.sprites.stage.varCoins)
        else:
            if eq(self.var_Type, "W"):
                await self.my_Update(util, util.sprites.stage.varWave)
            else:
                if eq(self.var_Type, "L"):
                    await self.my_Update(util, util.sprites.stage.varLives)
                else:
                    pass

    @warp
    async def my_Update(self, util, arg_txt):
        if gt(self.var_ID, len(str(arg_txt))):
            if gt(self.var_Visible, 0):
                self.shown = False
                self.var_Visible = 0
        else:
            if not eq(self.costume.number, (tonum(letter_of(str(arg_txt), toint(self.var_ID))) + 2)):
                self.costume.switch((tonum(letter_of(str(arg_txt), toint(self.var_ID))) + 2))
            if eq(self.var_Visible, 0):
                self.var_Visible = 1
                self.shown = True


@sprite('Tools')
class SpriteTools(Target):
    """Sprite Tools"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -48
        self._ypos = -157
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           3, 100, "don't rotate", [
            {
                'name': "gun_buy1d",
                'path': "2c4a9852e94c151d3e0745e4440886d9.png",
                'center': (24, 36),
                'scale': 2
            },
            {
                'name': "gun_buy2d",
                'path': "d0b46ae6e66d413f119cc15c4c8b85ab.png",
                'center': (32, 36),
                'scale': 2
            },
            {
                'name': "gun_buy1",
                'path': "d027966e89df06f8f38410ad87e09daf.png",
                'center': (24, 36),
                'scale': 2
            },
            {
                'name': "gun_buy2",
                'path': "05181ecfefd8a2f83b29fbbc22ce5740.png",
                'center': (32, 36),
                'scale': 2
            },
            {
                'name': "rocket_buy1d",
                'path': "17d5eeab574fef059b243d5324e08bb7.png",
                'center': (20, 36),
                'scale': 2
            },
            {
                'name': "rocket_buy2d",
                'path': "6d58e15bd3e8df010667367ab39843e7.png",
                'center': (28, 36),
                'scale': 2
            },
            {
                'name': "rocket_buy1",
                'path': "b82542ed7848558b1457ca83f439c79a.png",
                'center': (20, 36),
                'scale': 2
            },
            {
                'name': "rocket_buy2",
                'path': "188b1a681e99b8feb0b6492b4a6afa07.png",
                'center': (28, 36),
                'scale': 2
            },
            {
                'name': "glue_buy1d",
                'path': "3004cdedc2dd5f3a81eb104bb08cb839.png",
                'center': (26, 36),
                'scale': 2
            },
            {
                'name': "glue_buy2d",
                'path': "12899b0772bb4eaf9893347a2df79f0d.png",
                'center': (32, 36),
                'scale': 2
            },
            {
                'name': "glue_buy1",
                'path': "92a8a18a50da3c6a0ed1b27255b1be1a.png",
                'center': (26, 36),
                'scale': 2
            },
            {
                'name': "glue_buy2",
                'path': "83c5d885bcfbd07782e99b32bfd2ef26.png",
                'center': (32, 36),
                'scale': 2
            },
            {
                'name': "tesla_buy1d",
                'path': "83b9172c4b9b9800b8028a5b268e273b.png",
                'center': (24, 36),
                'scale': 2
            },
            {
                'name': "tesla_buy2d",
                'path': "f21851ed0183f00673deee915c751e11.png",
                'center': (32, 36),
                'scale': 2
            },
            {
                'name': "tesla_buy1",
                'path': "a4a5e1d8002783739ba01ca5bc464c4c.png",
                'center': (24, 36),
                'scale': 2
            },
            {
                'name': "tesla_buy2",
                'path': "29a2aad94c6506c9c7d1954e28b1a14d.png",
                'center': (32, 36),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [

        ])

        self.var_ID = 1
        self.var_i = 4
        self.var_TurretType = 1



        self.sprite.layer = 7

    @on_broadcast('update: coins')
    async def broadcast_UpdateCoins(self, util):
        await self.my_UpdateA(util, )

    @warp
    async def my_UpdateA(self, util, ):
        self.var_i = util.sprites.stage.list_DATA_Turrets[toint(((tonum(self.var_TurretType) * util.sprites.stage.varDTMUL) + 7))]
        if not gt(util.sprites.stage.list_DATA_Turrets[toint(((tonum(self.var_TurretType) * util.sprites.stage.varDTMUL) + 4))], util.sprites.stage.varCoins):
            self.var_i = tonum(self.var_i) + 2
        if eq(util.sprites.stage.varToolType, self.var_ID):
            self.var_i = tonum(self.var_i) + 1
        if not eq(self.costume.number, self.var_i):
            self.costume.switch(self.var_i)
        self.shown = True

    @on_clicked
    async def sprite_clicked(self, util):
        util.sprites.stage.varToolType = self.var_ID
        util.send_broadcast("Update: Coins")

    @on_green_flag
    async def green_flag(self, util):
        self.costume.size = 100
        self.costume.switch("gun_buy1")
        self.direction = 90
        self.shown = False

    @warp
    async def my_Init(self, util, ):
        self.var_TurretType = util.sprites.stage.listTools[toint(self.var_ID)]
        self.gotoxy((-80 + (self.var_ID * 32)), -157)
        await self.my_UpdateA(util, )

    @on_clone_start
    async def clone_start(self, util):
        await self.my_Init(util, )

    @warp
    async def my_Clone(self, util, ):
        self.var_ID = len(util.sprites.stage.listTools)
        while not lt(self.var_ID, 2):
            self.create_clone_of(util, "_myself_")
            self.var_ID += -1
        await self.my_Init(util, )

    @on_broadcast('init: clone level tiles')
    async def broadcast_InitCloneLevelTiles(self, util):
        await self.my_Clone(util, )


@sprite('Spawner')
class SpriteSpawner(Target):
    """Sprite Spawner"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -61
        self._ypos = 42
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "d36f6603ec293d2c2198d3ea05109fe0.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_SpawnIndex = 1
        self.var_pi = 1
        self.var_ps = ""
        self.var_FrameRel = 0
        self.var_RELMUL = 5
        self.var_mobID = 111
        self.var_tileIdx = 96
        self.var_TileIdx = 0
        self.var_eid = -1
        self.var_entrance = 0

        self.list_SpawnData = List(
            ["", "160,0,1,3,45", "", "120,0,1,3,30", "", "120,0,1,5,30", "", "120,1,1,5,25", "", "120,0,1,10,20", "", "120,0,1,10,15", "", "120,1,1,20,15", "", "120,0,2,3,30", "", "120,0,1,12,10", "", "120,0,2,6,30", "", "120,1,2,6,20", "", "120,0,1,10,3", "0,1,1,10,3", "", "120,0,1,10,2", "0,1,1,10,3", "", "240,0,1,10,2", "0,1,1,10,2", "", "120,0,2,15,7", "", "120,1,2,20,6", "", "120,0,3,3,15", "", "120,1,3,10,8", "", "120,0,3,15,5", "", "120,0,5,1,0", "", "120,1,2,30,4", "", "120,0,4,1,0", "", "120,1,3,20,3", "", "70,1,5,2,90", "", "120,0,2,30,2", "", "120,1,3,25,4", "", "120,0,4,3,120", "", "160,1,3,15,2", "60,0,4,3,120", "260,0,3,20,2", "", "160,0,4,3,40", "", "120,0,5,3,45", "", "120,0,3,15,2", "0,1,3,15,2", "", "120,0,7,1,30", "", "120,0,2,35,3", "260,0,3,20,2", "", "160,1,4,5,25", "", "160,0,6,10,10", "", "160,0,6,20,7", "", "120,1,7,3,30", "", "160,1,6,30,5", "", "120,1,5,3,30", "", "160,0,6,30,3", "", "120,0,7,6,25", "", "160,0,6,50,2", "", "120,1,7,12,20", "", "120,0,7,20,15", "0,1,7,20,15"]
        )
        self.list_tokens = List(
            [""]
        )
        self.list_ReleaseMob = List(
            []
        )

        self.sprite.layer = 6

    @warp
    async def my_Parse(self, util, arg_str):
        self.list_tokens.delete_all()
        self.var_pi = 1
        self.var_ps = ""
        while not gt(self.var_pi, len(str(arg_str))):
            if eq(letter_of(str(arg_str), toint(self.var_pi)), ","):
                self.list_tokens.append(self.var_ps)
                self.var_ps = ""
            else:
                self.var_ps = (self.var_ps + letter_of(str(arg_str), toint(self.var_pi)))
            self.var_pi += 1
        self.list_tokens.append(self.var_ps)

    @warp
    async def my_Loop(self, util, ):
        for _ in range(toint(util.sprites.stage.varSpeed)):
            if eq(self.list_tokens[1], ""):
                if eq(len(self.list_ReleaseMob), 0):
                    if eq(util.sprites.stage.varMobCount, 0):
                        self.var_SpawnIndex += 1
                        if gt(self.var_SpawnIndex, len(self.list_SpawnData)):
                            self.var_SpawnIndex = 1
                        await self.my_Parse(util, self.list_SpawnData[toint(self.var_SpawnIndex)])
                        self.var_FrameRel = 0
                        util.sprites.stage.varWave += 1
            else:
                if not lt(self.var_FrameRel, self.list_tokens[1]):
                    self.list_ReleaseMob.append(util.sprites.stage.varFrame)
                    self.list_ReleaseMob.append(self.list_tokens[2])
                    self.list_ReleaseMob.append(self.list_tokens[3])
                    self.list_ReleaseMob.append(self.list_tokens[4])
                    self.list_ReleaseMob.append(self.list_tokens[5])
                    self.var_SpawnIndex += 1
                    if gt(self.var_SpawnIndex, len(self.list_SpawnData)):
                        self.var_SpawnIndex = 1
                    await self.my_Parse(util, self.list_SpawnData[toint(self.var_SpawnIndex)])
                    self.var_FrameRel = 0
            self.var_pi = 1
            while not gt(self.var_pi, len(self.list_ReleaseMob)):
                if gt(util.sprites.stage.varFrame, self.list_ReleaseMob[toint(self.var_pi)]):
                    await self.my_Spawn(util, )
                    if gt(self.var_mobID, 0):
                        if lt(self.list_ReleaseMob[toint((self.var_pi + 3))], 2):
                            for _ in range(toint(self.var_RELMUL)):
                                self.list_ReleaseMob.delete(toint(self.var_pi))
                            self.var_pi += (0 - self.var_RELMUL)
                        else:
                            self.list_ReleaseMob[toint((self.var_pi + 0))] = (util.sprites.stage.varFrame + tonum(self.list_ReleaseMob[toint((self.var_pi + 4))]))
                            self.list_ReleaseMob[toint((self.var_pi + 3))] = (tonum(self.list_ReleaseMob[toint((self.var_pi + 3))]) - 1)
                self.var_pi += self.var_RELMUL
            self.var_FrameRel += 1

    @on_broadcast('init: clone level tiles')
    async def broadcast_InitCloneLevelTiles(self, util):
        pass

    @on_broadcast('initclones')
    async def broadcast_InitClones(self, util):
        self.var_SpawnIndex = 1
        self.var_FrameRel = 0
        util.sprites.stage.varWave = 0
        self.var_eid = -1
        self.list_ReleaseMob.delete_all()
        await self.my_Parse(util, self.list_SpawnData[toint(self.var_SpawnIndex)])

    @on_broadcast('loop')
    async def broadcast_loop(self, util):
        await self.my_Loop(util, )

    async def my_Spawn(self, util, ):
        if eq(len(util.sprites.stage.listMobPool), 0):
            self.var_mobID = 0
        else:
            self.var_mobID = util.sprites.stage.listMobPool[1]
            util.sprites.stage.listMobPool.delete(1)
            self.var_eid = -1
            self.var_entrance = self.list_ReleaseMob[toint((self.var_pi + 1))]
            if lt(util.sprites.stage.varLevel, 3):
                self.var_entrance = 0
            for _ in range(toint(pick_rand(1, div(len(util.sprites.stage.listEntrances), 2)))):
                self.var_eid += 2
                if gt(self.var_eid, len(util.sprites.stage.listEntrances)):
                    self.var_eid = 1
                while not eq(util.sprites.stage.listEntrances[toint(self.var_eid)], self.var_entrance):
                    self.var_eid += 2
                    if gt(self.var_eid, len(util.sprites.stage.listEntrances)):
                        self.var_eid = 1

                    await self.yield_()

                await self.yield_()
            self.var_tileIdx = util.sprites.stage.listEntrances[toint((self.var_eid + 1))]
            util.sprites.stage.listMob[toint((tonum(self.var_mobID) + 1))] = ((tonum(self.var_tileIdx) - 1) % util.sprites.stage.varlsx)
            util.sprites.stage.listMob[toint((tonum(self.var_mobID) + 2))] = math.floor(div((tonum(self.var_tileIdx) - 1), util.sprites.stage.varlsx))
            util.sprites.stage.listMob[toint((tonum(self.var_mobID) + 0))] = self.list_ReleaseMob[toint((self.var_pi + 2))]
            util.sprites.stage.listMob[toint((tonum(self.var_mobID) + 9))] = self.var_entrance


@sprite('Fast-Forward')
class SpriteFastForward(Target):
    """Sprite Fast-Forward"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 202
        self._ypos = -159
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "FF Off",
                'path': "9bb510fb25e1fa1511ebf849677a8bda.png",
                'center': (36, 28),
                'scale': 2
            },
            {
                'name': "FF Active",
                'path': "c071d9c2773fb3ce4c4a074a723064b1.png",
                'center': (42, 34),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])





        self.sprite.layer = 9

    @on_broadcast('go: user input')
    async def broadcast_GoUserInput(self, util):
        self.shown = True

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(202, -159)
        self.shown = False

    @on_broadcast('init: clone level tiles')
    async def broadcast_InitCloneLevelTiles(self, util):
        util.sprites.stage.varSpeed = 1
        self.costume.switch("FF Off")

    @on_broadcast('speed change')
    async def broadcast_SpeedChange(self, util):
        if eq(util.sprites.stage.varSpeed, 2):
            self.costume.switch("FF Active")
        else:
            self.costume.switch("FF Off")

    @on_clicked
    async def sprite_clicked(self, util):
        if eq(util.sprites.stage.varSpeed, 2):
            util.sprites.stage.varSpeed = 1
        else:
            util.sprites.stage.varSpeed = 2
        util.send_broadcast("Speed Change")


@sprite('Fast-Forward2')
class SpriteFastForward2(Target):
    """Sprite Fast-Forward2"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 162
        self._ypos = -159
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Pause Off",
                'path': "d3aa6207934b58cb9eda299e70e58fb8.png",
                'center': (24, 28),
                'scale': 2
            },
            {
                'name': "Pause Active",
                'path': "8e978304b514246dcf18edfaf6059cfc.png",
                'center': (30, 34),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])





        self.sprite.layer = 8

    @on_broadcast('go: user input')
    async def broadcast_GoUserInput(self, util):
        self.shown = True

    @on_broadcast('init: clone level tiles')
    async def broadcast_InitCloneLevelTiles(self, util):
        self.costume.switch("Pause Off")

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(162, -159)
        self.shown = False

    @on_broadcast('speed change')
    async def broadcast_SpeedChange(self, util):
        if eq(util.sprites.stage.varSpeed, 0):
            self.costume.switch("Pause Active")
        else:
            self.costume.switch("Pause Off")

    @on_clicked
    async def sprite_clicked(self, util):
        if eq(util.sprites.stage.varSpeed, 0):
            util.sprites.stage.varSpeed = 1
        else:
            util.sprites.stage.varSpeed = 0
        util.send_broadcast("Speed Change")


@sprite('Sell')
class SpriteSell(Target):
    """Sprite Sell"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -154
        self._ypos = -48
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Sell",
                'path': "1570d13d2e192fc59e90706cfaef1856.png",
                'center': (40, 40),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])





        self.sprite.layer = 12

    @on_green_flag
    async def green_flag(self, util):
        self.costume.size = 100
        self.costume.switch("gun_buy1")
        self.direction = 90
        self.shown = False

    @on_broadcast('do: selected')
    async def broadcast_DoSelected(self, util):
        self.gotoxy(util.sprites["Cursor"].xpos, util.sprites["Cursor"].ypos)
        self.xpos += -34
        self.front_layer(util)
        self.shown = True

    @on_broadcast('do: unselect')
    async def broadcast_DoUnselect(self, util):
        self.shown = False

    @on_clicked
    async def sprite_clicked(self, util):
        util.sprites.stage.varAction = 1


@sprite('Upgrade')
class SpriteUpgrade(Target):
    """Sprite Upgrade"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -86
        self._ypos = -48
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "Upgrade",
                'path': "20c77bc7a23235b9bba6eeb3cdec135f.png",
                'center': (40, 40),
                'scale': 2
            },
            {
                'name': "Upgrade Disabled",
                'path': "b7cf87a5d6c4a1739c876650e935ccd5.png",
                'center': (40, 40),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_costume = 1



        self.sprite.layer = 13

    @on_green_flag
    async def green_flag(self, util):
        self.costume.size = 100
        self.costume.switch("Upgrade")
        self.direction = 90
        self.shown = False

    @on_clicked
    async def sprite_clicked(self, util):
        if not gt(util.sprites.stage.varUpgradePrice, util.sprites.stage.varCoins):
            util.sprites.stage.varAction = 2

    @on_broadcast('do: unselect')
    async def broadcast_DoUnselect(self, util):
        self.shown = False

    @on_broadcast('do: selected')
    async def broadcast_DoSelected(self, util):
        if gt(util.sprites.stage.varUpgradePrice, 0):
            self.gotoxy(util.sprites["Cursor"].xpos, util.sprites["Cursor"].ypos)
            self.xpos += 34
            self.front_layer(util)
            await self.my_Show(util, )
            self.shown = True

    @on_broadcast('update: coins')
    async def broadcast_UpdateCoins(self, util):
        if gt(util.sprites.stage.varUpgradePrice, 0):
            await self.my_Show(util, )

    @warp
    async def my_Show(self, util, ):
        if gt(util.sprites.stage.varUpgradePrice, util.sprites.stage.varCoins):
            self.var_costume = 2
        else:
            self.var_costume = 1
        if not eq(self.var_costume, self.costume.number):
            self.costume.switch(self.var_costume)


@sprite('BlackFade')
class SpriteBlackFade(Target):
    """Sprite BlackFade"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 0
        self._ypos = 0
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "don't rotate", [
            {
                'name': "BlackOut",
                'path': "42b18c6ce69951cc9b153203d9c54b2f.svg",
                'center': (240, 180),
                'scale': 1
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])





        self.sprite.layer = 17

    @on_green_flag
    async def green_flag(self, util):
        self.gotoxy(0, 0)
        self.costume.clear_effects()
        self.shown = True
        self.front_layer(util)

    @on_broadcast('fade:in')
    async def broadcast_fadein(self, util):
        for _ in range(25):
            self.costume.change_effect('ghost', 4)

            await self.yield_()
        self.shown = False
        self.costume.clear_effects()

    @on_broadcast('fade:out')
    async def broadcast_fadeout(self, util):
        self.costume.clear_effects()
        self.costume.set_effect('ghost', 100)
        self.shown = True
        for _ in range(10):
            self.costume.change_effect('ghost', -10)

            await self.yield_()


@sprite('Difficulty')
class SpriteDifficulty(Target):
    """Sprite Difficulty"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = 140
        self._ypos = 0
        self._direction = 90
        self.shown = True
        self.pen = Pen(self)

        self.costume = Costumes(
           10, 100, "don't rotate", [
            {
                'name': "Play_Fun",
                'path': "2e8fa0a59823fdfa158b961167995c6f.png",
                'center': (102, 34),
                'scale': 2
            },
            {
                'name': "Play_Fun_Sel",
                'path': "72093c39743a79b53a976c53b1dfb1b7.png",
                'center': (102, 34),
                'scale': 2
            },
            {
                'name': "Play_Easy",
                'path': "d9ed44bb6299c15154e66616304b1a45.png",
                'center': (102, 34),
                'scale': 2
            },
            {
                'name': "Play_Easy_Sel",
                'path': "52395441987906b3b4968f246eb07953.png",
                'center': (102, 34),
                'scale': 2
            },
            {
                'name': "Play_Normal",
                'path': "5d0ec0349e8fb42799ebff03f9cc731c.png",
                'center': (102, 34),
                'scale': 2
            },
            {
                'name': "Play_Normal_Sel",
                'path': "bbe6c5518dc4f00999f94bde5ebeef7e.png",
                'center': (102, 34),
                'scale': 2
            },
            {
                'name': "Play_Hard",
                'path': "575d95314d54cfb5bc1082a5cc1e21f2.png",
                'center': (102, 34),
                'scale': 2
            },
            {
                'name': "Play_Hard_Sel",
                'path': "3cbc65b004452358db58c9759531e415.png",
                'center': (102, 34),
                'scale': 2
            },
            {
                'name': "Left",
                'path': "d1f50f1863a923e874ff90694e8ac72a.png",
                'center': (54, 100),
                'scale': 2
            },
            {
                'name': "Left_Sel",
                'path': "cab887b939ff8beb55e6c508ae99e069.png",
                'center': (54, 100),
                'scale': 2
            },
            {
                'name': "Right",
                'path': "b2b6db49000a74c7f37d0d16767b3f87.png",
                'center': (52, 100),
                'scale': 2
            },
            {
                'name': "Right_Sel",
                'path': "8c55774096ea5d6498691a9423302b64.png",
                'center': (52, 100),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "meow",
                'path': "83c36d806dc92327b9e7049a565c6bff.wav"
            }
        ])

        self.var_ID = 6
        self.var_t = 90
        self.var_y = -80



        self.sprite.layer = 18

    @on_green_flag
    async def green_flag(self, util):
        self.shown = False
        self.costume.size = 100

    async def my_Appear(self, util, ):
        if lt(self.var_ID, 5):
            self.gotoxy(0, -240)
            self.var_y = (15 - (self.var_ID * 38))
        else:
            self.var_y = -80
            if eq(self.var_ID, 5):
                self.gotoxy(-140, -240)
            else:
                self.gotoxy(140, -240)
        self.costume.switch(((self.var_ID * 2) - 1))
        self.costume.set_effect('ghost', 100)
        self.front_layer(util)
        self.shown = True
        self.var_t = 0
        for _ in range(20):
            self.var_t += div(90, 20)
            self.ypos = (self.var_y + (80 * math.sin(math.radians(self.var_t))))
            self.costume.change_effect('ghost', -5)

            await self.yield_()
        while not gt(util.sprites.stage.var_Difficulty, 0):
            if self.get_touching(util, "_mouse_"):
                await self.my_SetCostume(util, (self.var_ID * 2))
            else:
                await self.my_SetCostume(util, ((self.var_ID * 2) - 1))

            await self.yield_()
        await self.sleep((self.var_ID * 0.05))
        if eq(util.sprites.stage.var_Difficulty, self.var_ID):
            for _ in range(10):
                self.costume.size += 4

                await self.yield_()
        self.var_t = 0
        for _ in range(20):
            self.var_t += div(90, 20)
            if lt(self.var_ID, 5):
                if eq(util.sprites.stage.var_Difficulty, self.var_ID):
                    self.costume.size += 4
                else:
                    self.xpos = ((160 * math.cos(math.radians(self.var_t))) - 160)
            else:
                self.costume.size += -3
            self.costume.change_effect('ghost', 5)

            await self.yield_()
        self.shown = False
        self.costume.size = 100
        if eq(util.sprites.stage.var_Difficulty, self.var_ID):
            util.send_broadcast("Go: Game On")
        self.delete_clone(util)

    @on_broadcast('go: user input')
    async def broadcast_GoUserInput(self, util):
        util.sprites.stage.var_Difficulty = 0
        await self.sleep(0.3)
        util.send_broadcast("Fade:In")
        await self.sleep(0.1)
        self.var_ID = 1
        for _ in range(5):
            self.create_clone_of(util, "_myself_")
            self.var_ID += 1
            await self.sleep(0.2)

            await self.yield_()
        await self.my_Appear(util, )

    @on_clicked
    async def sprite_clicked(self, util):
        while not not util.inputs.mouse_down:
            await self.yield_()
        if lt(self.var_ID, 5):
            util.sprites.stage.var_Difficulty = self.var_ID
            if eq(util.sprites.stage.var_Difficulty, 1):
                util.sprites.stage.varDiffMul = 0.5
                util.sprites.stage.varCoins = 50
            else:
                if eq(util.sprites.stage.var_Difficulty, 2):
                    util.sprites.stage.varDiffMul = 0.5
                else:
                    if eq(util.sprites.stage.var_Difficulty, 3):
                        util.sprites.stage.varDiffMul = 1
                    else:
                        util.sprites.stage.varDiffMul = 1.4
        else:
            if eq(self.var_ID, 5):
                util.sprites.stage.varLevel = (((util.sprites.stage.varLevel - 2) % util.sprites.stage.varLevelCount) + 1)
            else:
                util.sprites.stage.varLevel = ((util.sprites.stage.varLevel % util.sprites.stage.varLevelCount) + 1)
            await util.sprites["BlackFade"].broadcast_fadeout(util)
            await util.send_broadcast_wait("Init: Creeate Level List")
            await util.sprites["Level"].broadcast_initstamplevel(util)
            await util.sprites["Level"].broadcast_updatelevel(util)
            await util.send_broadcast_wait("Update: Guns")
            await util.sprites["Path Finder"].broadcast_gofind(util)
            await util.sprites["BlackFade"].broadcast_fadein(util)

    async def my_SetCostume(self, util, arg_costume):
        if not eq(self.costume.number, arg_costume):
            self.costume.switch(arg_costume)

    @on_clone_start
    async def clone_start(self, util):
        await self.my_Appear(util, )


@sprite('Gun Sound')
class SpriteGunSound(Target):
    """Sprite Gun Sound"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -56
        self._ypos = -24
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "d36f6603ec293d2c2198d3ea05109fe0.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "machine one shot",
                'path': "e5df5d6900314b436a855ced83da20ea.wav"
            },
            {
                'name': "machine 4 shot",
                'path': "6d44fcf46603f2ea10a198cd072da7ea.wav"
            }
        ])





        self.sprite.layer = 10

    @on_green_flag
    async def green_flag(self, util):
        util.sprites.stage.varSoundMachine = 0
        self.sounds.set_volume(60)
        while True:
            while not gt(util.sprites.stage.varSoundMachine, 0):
                await self.yield_()
            await self.sounds.play("machine 4 shot")
            util.sprites.stage.varSoundMachine = 0

            await self.yield_()


@sprite('Glue Sound')
class SpriteGlueSound(Target):
    """Sprite Glue Sound"""

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            return

        self._xpos = -89
        self._ypos = 62
        self._direction = 90
        self.shown = False
        self.pen = Pen(self)

        self.costume = Costumes(
           0, 100, "all around", [
            {
                'name': "costume1",
                'path': "d36f6603ec293d2c2198d3ea05109fe0.png",
                'center': (480, 360),
                'scale': 2
            }
        ])

        self.sounds = Sounds(
            100, [
            {
                'name': "Squidge",
                'path': "d8c51c8c2872e17923d61f61c82c8acf.wav"
            }
        ])





        self.sprite.layer = 11

    @on_green_flag
    async def green_flag(self, util):
        util.sprites.stage.varSoundGlue = 0
        self.sounds.set_volume(40)
        while True:
            while not gt(util.sprites.stage.varSoundGlue, 0):
                await self.yield_()
            await self.sounds.play("Squidge")
            util.sprites.stage.varSoundGlue = 0

            await self.yield_()




if __name__ == '__main__':
    engine.start_program()
