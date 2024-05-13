def area(rec1, rec2, rec3):
    rects = [rec1, rec2, rec3]

    # Individual Rectangle Area Function
    def rect_area(rec):
        x1, y1, x2, y2 = rec
        return abs(x2 - x1) * abs(y1 - y2)
    
    # Pair-wise Overlap Area Function
    def overlap_area(rec1, rec2):
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        overlap_width = max(0, min(x2, x4) - max(x1, x3))
        overlap_height = max(0, min(y1, y3) - max(y2, y4))
        return overlap_width * overlap_height
    
    # Calculate all individual areas
    total = sum(rect_area(rec) for rec in rects)
    
    # Calculate all pair-wise overlapping areas between each pair of rectangles
    pairwise = sum(overlap_area(rects[i], rects[j]) for i in range(len(rects)) for j in range(i+1, len(rects)))
    
    # Calculate the area where all three rectangles overlap
    x1, x2, x3, x4, x5, x6 = rects[0][0], rects[0][2], rects[1][0], rects[1][2], rects[2][0], rects[2][2]
    y1, y2, y3, y4, y5, y6 = rects[0][1], rects[0][3], rects[1][1], rects[1][3], rects[2][1], rects[2][3]
    overlap_width = max(0, min(x2, x4, x6) - max(x1, x3, x5))
    overlap_height = max(0, min(y1, y3, y5) - max(y2, y4, y6))
    all_overlap = overlap_width * overlap_height
    
    # Subtract overlapping areas and add back non-overlapping areas
    area = total - pairwise + all_overlap
    
    return area