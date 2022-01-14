# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["thread", "started_at"])
node = namedtuple("node", ["thread", "finish_time"])


class Heap():
    def __init__(self, n, jobs):
        self.heap = [node(i, 0) for i in range(n)]
        self.size = n-1

    def parent(self, i):
        return (i-1)//2

    def left_child(self, i):
        return 2*i+1

    def right_child(self, i):
        return 2*i+2

    def sift_down(self, i):
        min_index = i
        l = self.left_child(i)
        if l <= self.size and self.heap[l].finish_time < self.heap[min_index].finish_time:
            min_index = l
        elif l <= self.size and self.heap[l].finish_time == self.heap[min_index].finish_time and self.heap[l].thread < self.heap[min_index].thread:
            min_index = l

        r = self.right_child(i)
        if r <= self.size and self.heap[r].finish_time < self.heap[min_index].finish_time:
            min_index = r
        elif r <= self.size and self.heap[r].finish_time == self.heap[min_index].finish_time and self.heap[r].thread < self.heap[min_index].thread:
            min_index = r
        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self.sift_down(min_index)

    def update_root(self, job):
        to_return = AssignedJob(self.heap[0].thread, self.heap[0].finish_time)
        self.heap[0] = node(self.heap[0].thread, self.heap[0].finish_time + job)
        self.sift_down(0)

        return to_return

    def build_heap_fast(self):
        for i in range(self.size//2, 0, -1):
            self.sift_down(i)


def assign_jobs(n, jobs):
    result = []
    processor = Heap(n, jobs)
    processor.build_heap_fast()
    for job in jobs:
        result.append(processor.update_root(job))
    return result



def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.thread, job.started_at)


if __name__ == "__main__":
    main()
