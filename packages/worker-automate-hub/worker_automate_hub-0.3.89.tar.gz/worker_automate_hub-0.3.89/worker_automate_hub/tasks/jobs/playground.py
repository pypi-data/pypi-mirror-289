
import asyncio
from time import sleep
from worker_automate_hub.utils.util import find_target_position, take_sreenshot


async def playground():
    sleep(5)

    screen = take_sreenshot()
    print(screen)
    res = find_target_position(screen, "su")
    print(res)


if __name__=="__main__":
    asyncio.run(playground())