import multiprocessing
import sys
from pathlib import Path

import psutil
from setproctitle import setproctitle

sys.path.append(Path(__file__).parents[1])

from Core.bot import main as botMain


class SBProcManager:
    def __init__(self):
        self.self = self

    def boot(self, name: str, token: str) -> None:
        """Fires up a Process for the bot

        Args:
            token (str): DC Bot Token
        """
        mainProc = multiprocessing.Process(target=botMain, name=name, args=(token,))
        setproctitle(name)
        mainProc.start()
        mainProc.join()

    def stop(self, bot_name: str):
        """Stops the bot given

        Args:
            bot_num (int): Bot Number
        """
        for proc in psutil.process_iter(["name"]):
            with proc.oneshot():
                if proc.name() == bot_name:
                    proc.terminate()
