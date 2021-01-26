

class Connect4:

    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.arr = [['_' for i in range(x)] for j in range(y)]
        self.print()

    def print(self):
        print('-------------------------')
        for x in self.arr:
            print(x)

    def Xplay1(self, y):
        x=(self.y)-1
        for i in range(x,-1,-1):
            if self.arr[i][y]=='_':
                x = i
                break
        self.arr[x][y] = 'X'
        self.print()
        print('X played')
        self.Xcheck(x, y)
        if self.Xcheck(x, y)=='X WIN':
            return 'X WIN'

    def Oplay1(self, y):
        x=(self.y)-1
        for i in range(x,0,-1):
            if self.arr[i][y]=='_':
                x = i
                break
        self.arr[x][y] = '@'
        self.print()
        print('@ played')
        self.Xcheck(x, y)
        if self.Xcheck(x, y)=='@ WIN':
            return '@ WIN'

    def Xcheck(self, x, y):
        try:
            if self.arr[x - 1][y] == self.arr[x - 2][y] == self.arr[x - 3][y] == 'X' or self.arr[x + 1][y] == self.arr[x + 2][y] == self.arr[x + 3][y] == 'X' or self.arr[x + 1][y] == self.arr[x + 2][y] == self.arr[x + 3][y] =='X'  or self.arr[x][y - 1] ==  self.arr[x][y - 2] ==  self.arr[x][y - 3] =='X'  or self.arr[x][y + 1] ==  self.arr[x][y + 2] ==  self.arr[x][y + 3] =='X'  or self.arr[x - 1][y + 1] ==  self.arr[x - 2][y + 2] ==  self.arr[x - 3][y - 3] =='X'  or self.arr[x + 1][y + 1] ==  self.arr[x + 2][y + 2] ==  self.arr[x + 3][y - 3] =='X'  or self.arr[x - 1][y - 1] ==  self.arr[x - 2][y - 2] ==  self.arr[x - 3][y - 3] =='X'  or self.arr[x + 1][y - 1] ==  self.arr[x + 2][y - 2] ==  self.arr[x + 3][y - 3] =='X':
                return 'X WIN'
            else:
                pass
        except:
            pass

    def Ocheck(self, x, y):
        try:
            if self.arr[x - 1][y] == self.arr[x - 2][y] == self.arr[x - 3][y] == '@' or self.arr[x + 1][y] == self.arr[x + 2][y] == self.arr[x + 3][y] ==  '@' or self.arr[x + 1][y] == self.arr[x + 2][y] == self.arr[x + 3][y] == '@'  or self.arr[x][y - 1] ==  self.arr[x][y - 2] ==  self.arr[x][y - 3] == '@'  or self.arr[x][y + 1] ==  self.arr[x][y + 2] ==  self.arr[x][y + 3] == '@'  or self.arr[x - 1][y + 1] ==  self.arr[x - 2][y + 2] ==  self.arr[x - 3][y - 3] == '@'  or self.arr[x + 1][y + 1] ==  self.arr[x + 2][y + 2] ==  self.arr[x + 3][y - 3] == '@'  or self.arr[x - 1][y - 1] ==  self.arr[x - 2][y - 2] ==  self.arr[x - 3][y - 3] == '@'  or self.arr[x + 1][y - 1] ==  self.arr[x + 2][y - 2] ==  self.arr[x + 3][y - 3] == '@':
                return '@ WIN'
            else:
                pass
        except:
            pass

print('Welcome to CONNECT4 game!')
print('-------------------------')
print('Enter the size you wanna play(X then Enter then Y:')
a = Connect4(eval(input()), eval(input()))
print('-------------------------')
print('------GAME STARTED------')

while True:
    print('Hey X Choose Column')
    play1 = a.Xplay1(eval(input()))
    if play1 =='X WIN':
        print('X WON')
        break
    print('Hey @ Choose Column')
    play2 = a.Oplay1(eval(input()))
    if play2 == '@ WIN':
        print('@ WON')
        break

print('------GAME OVER------')
