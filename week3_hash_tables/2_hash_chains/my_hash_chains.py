# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.index = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    def __init__(self, m):
        self.m = m
        self.hashtable = [[] for i in range(m)]

    def hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * 263 + ord(c)) % 1000000007
        return ans % self.m

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(elem for elem in reversed(self.hashtable[query.index]))
        else:
            hash_val = self.hash_func(query.s)
            is_present = query.s in self.hashtable[hash_val]
            if query.type == 'add' and not is_present:
                self.hashtable[hash_val].append(query.s)
            elif query.type == 'del' and is_present:
                self.hashtable[hash_val].remove(query.s)
            if query.type == 'find':
                self.write_search_result(is_present)


    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
