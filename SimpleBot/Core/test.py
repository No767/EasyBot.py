import os
from pathlib import Path

path = Path(__file__).parents[1]
print(path)
print(os.path.join(path, "Core", "Cogs"))
# print(os.listdir(os.path.join(path, "Core", "Cogs")))
# cogsList = os.listdir(os.path.join(path, "Cogs"))
# for items in cogsList:
#     if items.endswith(".py"):
#         print(items[:-3])
# cogsList = os.listdir(os.path.join(path, "Cogs"))
# for items in cogsList:
#     if items.endswith(".py"):
#         print(items)
# bot.load_extension(f"Cogs.{items[:-3]}")
