class Recursion_QueensProblem:
    def __init__(self, size):
        self.size = size
        self.results = 0
        self.calc()

    def calc(self):
        vector = [-1] * self.size
        self.add(vector, 0)
        print(self.results)

    def add(self, vector, tgt_x):
        if tgt_x == self.size:
            self.build(vector)
            self.results += 1
        else:
            for y in range(self.size):
                if self.validate(vector, tgt_x, y):
                    vector[tgt_x] = y
                    self.add(vector, tgt_x + 1)

    def validate(self, vector, occupied_rows, y):
        for i in range(occupied_rows):
            if vector[i] == y or \
                    vector[i] - i == y - occupied_rows or \
                    vector[i] + i == y + occupied_rows:

                return False
        return True

    def build(self, vector):
        for x in range(self.size):
            line = ""
            for y in range(self.size):
                if vector[x] == y:
                    line += "Q "
                else:
                    line += "x "
            print(line)
        print("\n")


# x & y are grid coordinates
# if n = 8 possible combinations are n! = 40320
# place queens on the first x rows. then for valid positions place a queen on all y of x k+1 and then reject the invalid states
Recursion_QueensProblem(8)
