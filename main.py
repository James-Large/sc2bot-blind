
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

from sc2.ids.unit_typeid import UnitTypeId
#from sc2.ids.ability_id import AbilityId
#from sc2.ids.buff_id import BuffId
#from sc2.ids.upgrade_id import UpgradeId
#from sc2.ids.effect_id import EffectId

#from sc2.constants import *


# https://github.com/Dentosal/python-sc2/issues/283#issuecomment-495991889

# this package is currently not working as of a new starcraft2 client update, will resume upon update


class BlindBotV0(sc2.BotAI):
    async def on_step(self, iteration):
        await self.distribute_workers()
        await self.build_workers()
        await self.build_pylons()

    async def build_workers(self):
        for nexus in self.units(UnitTypeId.NEXUS).ready.noqueue:
            if self.can_afford(UnitTypeId.PROBE):
                await self.do(nexus.train(UnitTypeId.PROBE))

    async def build_pylons(self):
        if self.supply_left < 3 and not self.already_pending(UnitTypeId.PYLON):
            nexuses = self.units(UnitTypeId.NEXUS).ready
            if nexuses.exists:
                if self.can_afford(UnitTypeId.PYLON):
                    await self.build(UnitTypeId.PYLON, near=nexuses.first)


def main():
    run_game(maps.get("AutomatonLE"), [
        Bot(Race.Protoss, BlindBotV0()),
        Computer(Race.Terran, Difficulty.Easy)
    ], realtime=True)

if __name__ == "__main__":
    main()
