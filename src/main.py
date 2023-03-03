from loguru import logger
from typing import final
from rich import print


# === Initialing ===
def init():
    # Remove Default (Console) Logger
    REMOVE_DEFAULT_LOGGER: final = False

    # Logger Config
    if REMOVE_DEFAULT_LOGGER:
        logger.remove(0)
    logger.add(
        "./logs/{time}.log", level="DEBUG", enqueue=True)


# === Main Function ===
def main():
    print("Hello World! :wave:")


if __name__ == "__main__":
    init()
    main()
