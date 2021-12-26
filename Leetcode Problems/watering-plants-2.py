class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        a, b, cp1, cp2, self.cnt = 0, len(plants)-1, capacityA, capacityB, 0
        
        def refill(name):
            self.cnt += 1
            return capacityA if name == 'Alice' else capacityB
        
        while a <= b:
            
            if a == b:
                mx = max(cp1,cp2)
                if plants[a] > mx: refill('Anyone')
                break
            
            if cp1 < plants[a]: cp1 = refill('Alice')
            cp1 -= plants[a]
            
            if cp2 < plants[b]: cp2 = refill('Bob')
            cp2 -= plants[b]
            
            a += 1
            b -= 1
            
        return self.cnt