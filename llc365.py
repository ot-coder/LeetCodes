class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y == target or x == target or y == target:
            return True

        visited = set()

        def dfs(jug1: int, jug2:int):
            state = (jug1, jug2)

            if state in visited:
                return False
            
            visited.add(state)

            if jug1 == target or jug2 == target or jug1 + jug2 == target:
                return True
            
            if dfs(x, jug2):
                return True
            if dfs(y, jug1):
                return True
            if dfs(0, jug1):
                return True
            if dfs(0, jug2):
                return True
            
            pour1to2 = min(jug1, y - jug2)
            if dfs(jug1 - pour1to2, jug2 + pour1to2):
                return True
            
            pour2to1 = min(jug2, x - jug1)
            if dfs(jug1 + pour2to1, jug2 - pour2to1):
                return True
            
            return False
        
        return dfs(0,0)

