class task_queue:
    queue = []
    #def __init__(self):
    #    self.queue = []

    def append(self, obj):
        self.queue.append(obj)

    def print_queue(self):
        print self.queue


if __name__ == "__main__":
    a = task_queue()
    b = task_queue()
    c = task_queue()

    a.append('tc_1')

    a.print_queue()
    b.print_queue()
    c.print_queue()