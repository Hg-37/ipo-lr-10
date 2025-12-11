def isCorrectRect(coords):
    left_bottom = coords[0]
    right_top = coords[1]
    x1, y1 = left_bottom
    x2, y2 = right_top

    return x1 < x2 and y1 < y2
class RectCorrectError(Exception):
     pass
def isCollisionRect(rectangles):
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
def intersectionAreaMultiRect(rectangles: list[list[tuple[float, float]]]) -> float:
   
    for i, rect in enumerate(rectangles, 1):
        try:
            isCorrectRect(rect, i)
        except RectCorrectError as e:
            raise RectCorrectError(f"{i}-й прямоугольник некоректный") from e
    
    if len(rectangles) == 0:
        return 0.0
    elif len(rectangles) == 1:
        return calculateArea(rectangles[0])
def getIntersectionForGroup(rects: list[list[tuple[float, float]]]) -> list[tuple[float, float]]:
        if len(rects) == 0:
            return None
        current_intersection = rects[0]
    
        for rect in rects[1:]:
            current_intersection = getIntersection(current_intersection, rect)
            if current_intersection is None:
                return None
        
        return current_intersection
    
        n = len(rectangles)
        total_area = 0.0
        for mask in range(1, 1 << n):

         subset_size = bin(mask).count('1')
        
         current_intersection = None
        
        for i in range(n):
            if mask & (1 << i):
                if current_intersection is None:
                    current_intersection = rectangles[i]
                else:
                    current_intersection = getIntersection(current_intersection, rectangles[i])
                    if current_intersection is None:
                        break
        
        if current_intersection is not None:
            area = calculateArea(current_intersection)
            if subset_size % 2 == 1:
                total_area += area
            else:
                total_area -= area
        return total_area
 

