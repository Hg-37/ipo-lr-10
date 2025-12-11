def isCorrectRect(coords):
  left_bottom = coords[0]
  right_top = coords[1]
  x1, y1 = left_bottom
  x2, y2 = right_top

  return x1 < x2 and y1 < y2
