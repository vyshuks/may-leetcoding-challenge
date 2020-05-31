"""
We have a list of points on the plane.
Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is
the Euclidean distance.)

You may return the answer in any order.  The answer is
guaranteed to be unique (except for the order that it is in.)
"""
import heapq
def k_closest(points, k):
    heap = []

    for x,y in points:
        dist = x**2 + y**2

        if len(heap) >= k:
            if dist < -heap[0][0]:
                heapq.heappop(heap)
        if len(heap) < k:
            heapq.heappush(heap, (-dist, x, y))

    return [[x,y] for _,x,y in heap]

print(k_closest([[3,3],[5,-1],[-2,4]], 2))