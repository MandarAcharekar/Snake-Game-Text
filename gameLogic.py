import textRes

snakeList = []

w, h = textRes.width, textRes.height

start_location = (int(w/2), int(h/2))

# Snake head is at start_location
snakeList.append(start_location)

# Here, [0] is x, [1] is y
# But, rows are y, cols are x, but that means
# those are the ones which are wrong ordered.
# Snake body of head + 2
snakeList.append((start_location[0], start_location[1] + 1))
snakeList.append((start_location[0], start_location[1] + 2))

tailPosition = snakeList[-1]

boolFirstRun = True
