# failed to solve

def length(wires, i):
    tmp = list(wires)
    tmp.pop(i)
    output = [set(), set()]
    for wire in tmp:
        if output[0] != set():
            if (wire[0] in output[0]) or (wire[1] in output[0]):
                output[0].add(wire[0])
                output[0].add(wire[1])
            else:
                output[1].add(wire[0])
                output[1].add(wire[1])
        else:
            output[0].add(wire[0])
            output[0].add(wire[1])
    if len(output[1]) == 0:
        return len(output[0]) - 1
    return abs(len(output[0])-len(output[1]))


def solution(n, wires):
    for wire in wires:
        wire.sort()
    wires.sort()
    answer = n
    for i in range(len(wires)):
        leng = length(wires, i)
        if answer > leng:
            answer = leng
    return answer

print(solution(6, [[1, 4], [6, 3], [2, 5], [5, 1], [5, 3]]))