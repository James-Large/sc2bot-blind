
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer


class BlindBotV0(sc2.BotAI):
    async def on_step(self, iteration):
        await self.distribute_workers()



def main():
    run_game(maps.get("AutomatonLE"), [
        Bot(Race.Protoss, BlindBotV0()),
        Computer(Race.Terran, Difficulty.Easy)
    ], realtime=True)

if __name__ == "__main__":
    main()
