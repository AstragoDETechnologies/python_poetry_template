import os

log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./../logs")
for file in os.listdir(log_dir):
    if file.endswith(".log"):
        os.remove(os.path.join(log_dir, file))
