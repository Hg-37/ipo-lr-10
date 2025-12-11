def isCorrectRect(coords):
    left_bottom = coords[0]
    right_top = coords[1]
    x1, y1 = left_bottom
    x2, y2 = right_top

    return x1 < x2 and y1 < y2
class RectCorrectError(Exception):
     pass
def isCollisionRect(rectangles):
    def is_valid_rect(rect_points, rect_number):
        (x1, y1), (x2, y2) = rect_points
        if not (x1 < x2 and y1 < y2):
            raise RectCorrectError(f"{rect_number}й прямоугольник некоректный")
    
    rect1, rect2 = rectangles
    try:
        is_valid_rect(rect1, 1)
    except RectCorrectError as e:
        raise RectCorrectError("1й прямоугольник некоректный") from e
    
    try:
        is_valid_rect(rect2, 2)
    except RectCorrectError as e:
        raise RectCorrectError("2й прямоугольник некоректный") from e
    
    (x1, y1), (x2, y2) = rect1 
    (x3, y3), (x3_max, y3_max) = rect2  
    x3, y3 = x3, y3
    x4, y4 = x3_max, y3_max

    not_collide = (x2 <= x3 or  
                   x4 <= x1 or  
                   y2 <= y3 or  
                   y4 <= y1)    

    return not not_collide
def intersectionAreaRect(rect1, rect2):
    try:
        isCorrectRect(rect1, 1)
    except RectCorrectError as e:
        raise RectCorrectError("1й прямоугольник некоректный") from e
    
    try:
        isCorrectRect(rect2, 2)
    except RectCorrectError as e:
        raise RectCorrectError("2й прямоугольник некоректный") from e
    
    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2
    
    left = max(x1, x3)
    right = min(x2, x4)
    bottom = max(y1, y3)
    top = min(y2, y4)
    
    if left < right and bottom < top:
        width = right - left
        height = top - bottom
        return width * height
    else:
        return 0
def getIntersection(rect1: list[tuple[float, float]], rect2: list[tuple[float, float]]) -> list[tuple[float, float]]:
    (x1, y1), (x2, y2) = rect1
    (x3, y3), (x4, y4) = rect2
    
    left = max(x1, x3)
    right = min(x2, x4)
    bottom = max(y1, y3)
    top = min(y2, y4)

    if left < right and bottom < top:
        return [(left, bottom), (right, top)]
    else:
        return None



