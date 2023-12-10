import os

leaderboard_file = "leaderboard.txt"

def initialize_leaderboard():
    if not os.path.exists(leaderboard_file):
        open(leaderboard_file, "x").close()

def update_leaderboard(name, score):
    with open(leaderboard_file, "a") as file:
        file.write(f"{name},{score}\n")

def read_leaderboard():
    with open(leaderboard_file, "r") as file:
        lines = file.readlines()
    leaderboard = [line.strip().split(",") for line in lines]
    leaderboard.sort(key=lambda x: int(x[1]), reverse=True)
    return leaderboard
