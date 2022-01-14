# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrival_time", "time_to_process", "request_index"])
Response = namedtuple("Response", ["finished_at", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size

    def process_requests(self, requests):
        responses = [0]*len(requests)
        queue = []
        while requests:
            while not queue:
                queue.append(requests.pop(0))
                self.finish_time += queue[0].time_to_process
            while queue:
                if self.finish_time == self.current_time:
                    responses[queue[0].request_index] = Response(self.current_time + self.finish_time, self.start_time)
                    queue.pop(0)
                    self.start_time = self.current_time

                while requests:
                    if len(queue) < self.size:
                        queue.append(requests.pop(0))
                    else:
                        if requests[0].arrival_time == self.current_time:
                            responses[requests.pop(0).request_index] = Response(False, -1)
                        else:
                            break

                if self.finish_time == self.current_time:
                    if queue:
                        self.finish_time = self.current_time + queue[0].time_to_process
                    if requests:
                        self.current_time = min(self.current_time + self.finish_time, requests[0].arrival_time)
                    else:
                        self.current_time = self.current_time + self.finish_time
                else:
                    if requests:
                        self.current_time = min(self.current_time + self.finish_time, requests[0].arrival_time)
                    else:
                        self.current_time = self.current_time + self.finish_time
        return responses

    def process_requests_new(self, requests):
        responses = [0] * len(requests)
        queue = []
        while requests:
            if not queue:
                queue.append(requests.pop(0))
                self.start_time = queue[0].arrival_time
                self.current_time = self.start_time
                self.finish_time = self.start_time + queue[0].time_to_process

            while queue:
                if self.current_time == self.finish_time:
                    responses[queue.pop(0).request_index] = Response(self.start_time + self.finish_time, self.start_time)
                    if queue:
                        self.start_time = max(queue[0].arrival_time, self.current_time)
                        self.finish_time = self.start_time + queue[0].time_to_process
                    elif requests:
                        self.start_time = max(requests[0].arrival_time, self.current_time)
                        self.finish_time = self.start_time + requests[0].time_to_process


                while requests:
                    if len(queue) < self.size:
                        queue.append(requests.pop(0))
                    elif requests[0].arrival_time == self.current_time:
                        responses[requests.pop(0).request_index] = Response(False, -1)
                    else:
                        break

                if requests:
                    self.current_time = min(self.finish_time, requests[0].arrival_time)
                else:
                    self.current_time = self.finish_time

        return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process, _))

    buffer = Buffer(buffer_size)
    responses = buffer.process_requests_new(requests)

    for response in responses:
        print(response.started_at) #


if __name__ == "__main__":
    main()
