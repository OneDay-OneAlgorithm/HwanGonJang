import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    length = 0

    for operation in operations:
        op, num = operation.split()
        num = int(num)

        if length == 0:
            min_heap = []
            max_heap = []

        if op == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            length += 1
        elif length > 0:
            if num == -1:
                heapq.heappop(min_heap)
            elif num == 1:
                heapq.heappop(max_heap)
            else:
                continue
            length -= 1

    if length <= 0:
        return [0, 0]

    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]

operations = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
print(solution(operations))