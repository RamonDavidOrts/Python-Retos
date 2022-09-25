def race(actions, track):
    if len(actions) != len(track):
        raise Exception("Actions and track must be the same length")
    result_track = ""
    result = True
    for i in range(len(actions)):
        if actions[i] == "run" and track[i] == "|":
            result_track += "/"
            result = False
        elif actions[i] == "jump" and track[i] == "_":
            result_track += "x"
            result = False
        else:
            result_track += track[i]
    print(result_track)
    return result

print(race(["run", "run", "jump", "run", "jump","run", "jump","run"], "__|_|_|_"))
print(race(["run", "run", "run", "jump", "jump","run", "run","run"], "_|_|_|__"))
print(race(["run", "run", "jump", "run", "jump","run"], "__|_|_|_"))
