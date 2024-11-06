# Circular Buffer
class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = [None] * self.size
        self.get_cycle = 0
        self.put_cycle = 0

    def get(self):
        if all(pos is None for pos in self.buffer):
            return None

        idx_value = self.buffer[self.get_cycle]
        self.buffer[self.get_cycle] = None
        self.get_cycle += 1

        self.get_cycle %= len(self.buffer)

        return idx_value

    def put(self, num):
        self.buffer[self.put_cycle] = num
        self.put_cycle += 1

        self.put_cycle %= len(self.buffer)

        if self.put_cycle == self.get_cycle - 1 and None not in self.buffer:
            self.get_cycle -= 1

        if self.put_cycle > self.get_cycle and None not in self.buffer:
            self.get_cycle += 1


buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)

print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

print(buffer.buffer)