from math import gcd


class CRT:
    ''' for solving a system of equations : x = a1 (mod n1)
        x = a2 (mod n2) , x = a3 (mod n3) , x = a4 (mod n4) 
        ... . It will give the x mod (LCM(a1,a2,a3,a4,..))
    '''

    def __init__(self, num):
        ''' num = number of equations
            a = list of a's 
            n = list of n's
        '''
        self.num = num
        self.a = [0]*num
        self.n = [0]*num

    def lcm(self, a, b):
        return (a*b//gcd(a, b))

    def GCD(self, a, b):  # solves a*x + b*y == gcd(a,b)
        x = 1
        y = 0
        x1, y1, a1, b1 = 0, 1, a, b
        while(b1):
            q = a1//b1
            x, x1 = x1, x-q*x1
            y, y1 = y1, y-q*y1
            a1, b1 = b1, a1-q*b1
        return(x, y)

    def solve2(self, a1, n1, a2, n2):
        ''' solving two equations x = a1 (mod n1) and x = a2 (mod n2) 
            returns the x (mod LCM(a1,a2))
        '''
        x1 = self.GCD(n1, n2)[0]
        d = gcd(n1, n2)
        if (a1-a2) % d != 0:
            return -1
        ans = -x1*(a1-a2)//d*n1+a1
        mod = self.lcm(n1, n2)
        ans = (ans % mod+mod) % mod
        return ans

    def solve(self):
        ''' solve the system of equations '''
        ans = self.a[0]
        N = self.n[0]
        for i in range(1, self.num):
            ans = self.solve2(ans, N, self.a[i], self.n[i])
            if ans == -1:
                return -1
            N = self.lcm(N, self.n[i])
        return ans

# read input from stdin an put a's in a and put n's in n
# then answer = obj.solve()
# if the answer does not exist it will return -1





