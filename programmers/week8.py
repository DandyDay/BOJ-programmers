def solution(sizes):
    widths = []
    heights = []
    for size in sizes:
        widths.append(max(size))
        heights.append(min(size))
    answer = max(widths)*max(heights)
    return answer