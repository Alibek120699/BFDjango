def make_chocolate(small, big, goal):
  reminder = goal % 5
  quotient = goal // 5
  if quotient <= big and reminder <= small:
    return reminder
  if big * 5 + small >= goal and reminder <= small:
    return goal - big * 5
  return -1
