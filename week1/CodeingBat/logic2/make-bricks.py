def make_bricks(small, big, goal):
  if small == goal:
    return True
  if 5 * big == goal:
    return True
  if small + 5 * big == goal:
    return True
  if 0 <= goal - big * 5 <= small:
    return True
  if big * 5 > goal:
    return goal % 5 <= small
  return False
