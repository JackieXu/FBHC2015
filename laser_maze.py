from __future__ import print_function
import sys
import time

def get_paths(point, maze):
    paths = []
    if point[0] > 0 and maze[point[0] - 1][point[1]]["type"] == ".":
        paths.append([point[0] - 1, point[1]])
    if point[1] < len(maze[0]) - 1 and maze[point[0]][point[1] + 1]["type"] == ".":
        paths.append([point[0], point[1] + 1])
    if point[0] < len(maze) - 1 and maze[point[0] + 1][point[1]]["type"] == ".":
        paths.append([point[0] + 1, point[1]])
    if point[1] > 0 and maze[point[0]][point[1] - 1]["type"] == ".":
        paths.append([point[0], point[1] - 1])
    return paths


def dead_by_laser(maze, point, lasers):
    for laser in lasers:
        if laser[0] == point[0]:
            if laser[2] == ">":
                if laser[1] > point[1]:
                    continue
                if not filter(lambda x: maze[laser[0]][x]["type"] == "#", xrange(laser[1] + 1, point[1], 1)):
                    return True
            if laser[2] == "<":
                if laser[1] < point[1]:
                    continue
                if not filter(lambda x: maze[laser[0]][x]["type"] == "#", xrange(laser[1] - 1, point[1], -1)):
                    return True
        elif laser[1] == point[1]:
            if laser[2] == "^":
                if laser[0] < point[0]:
                    continue
                if not filter(lambda x: maze[x][laser[1]]["type"] == "#", xrange(laser[0] - 1, point[0], -1)):
                    return True
            elif laser[2] == "v":
                if laser[0] > point[0]:
                    continue
                if not filter(lambda x: maze[x][laser[1]]["type"] == "#", xrange(laser[0] + 1, point[0], 1)):
                    return True
    return False


def solve(maze):
    maze = maze
    start_point = None
    goal_point = None
    lasers = []
    shifts = {"^": ">", ">": "v", "v": "<", "<": "^"}

    for row in xrange(len(maze)):
        for column in xrange(len(maze[row])):
            if maze[row][column]["type"] == "S":
                maze[row][column]["type"] = "."
                start_point = [row, column]
            elif maze[row][column]["type"] == "G":
                maze[row][column]["type"] = "."
                goal_point = [row, column]
            elif maze[row][column]["type"] in ["^", ">", "v", "<"]:
                lasers.append([row, column, maze[row][column]["type"]])
                maze[row][column]["type"] = "#"

    queue = [get_paths(start_point, maze)]
    state = 0
    steps = 0

    while queue:
        paths = queue.pop(0)

        if not paths:
            continue

        steps += 1
        new_paths = []
        
        for laser in lasers:
            laser[2] = shifts[laser[2]]

        for path in paths:
            if maze[path[0]][path[1]]["visited"][state] or dead_by_laser(maze, path, lasers):
                continue

            if path[0] == goal_point[0] and path[1] == goal_point[1]:
                return steps

            maze[path[0]][path[1]]["visited"][state] = True
            new_paths.extend(get_paths(path, maze))

        queue.append(new_paths)
        state = (state + 1) % 4

    return "impossible"


def main():
    with open(__file__.replace("py", "in"), "r") as input_file:
        output_file = open(__file__.replace("py", "out"), "w")
        case_count = int(next(input_file))
        case_counter = 1
        for case in xrange(case_count):
            s = time.time()
            height, width = [int(x) for x in next(input_file).split(" ")]
            maze = [[{"visited": [False, False, False, False],
                      "type": None} for _ in xrange(width)] for _ in xrange(height)]
            for row in xrange(height):
                chars = list(next(input_file))[:width]
                for column in xrange(len(chars)):
                    maze[row][column]["type"] = chars[column]
            print("Case #{0}: {1}".format(case_counter, solve(maze)), file=output_file)
            print(time.time() - s)
            case_counter += 1
    return 0


if __name__ == "__main__":
    status = main()
    sys.exit(status)
