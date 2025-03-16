class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            cars = sorted(zip(position, speed))
            print(cars)
            times = [float(target - p)/ s for p, s in cars] # 끝까지 가기위해 필요한 횟수, 횟수가 적을 수록 빨리 도달
            print(times)
            ans = 0

            while len(times) > 1: # 비교할 대상이 2개 이상 있어야 현재 차량이 앞 차량을 따라잡을 수 있는지 비교할 수 있음.
                lead = times.pop()
                if lead < times[-1]: # 지금꺼횟수 < 전에꺼횟수 지금꺼가 더 빨리 도착함
                    ans += 1
                else:
                    times[-1] = lead # 지금꺼가 더 느리기 때문에 전에꺼 속도도 같아짐

            print(times)
            return ans + bool(times)