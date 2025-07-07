# https://leetcode.com/problems/angle-between-hands-of-a-clock/
def angleClock(self, hour: int, minutes: int) -> float:
    hour_angle = (( hour * 30 ) + ( minutes / 2 )) % 360
    minutes_angle = minutes * 6
    return abs(hour_angle- minutes_angle )  if abs(hour_angle- minutes_angle)  < 360 - abs(hour_angle- minutes_angle) else 360 - abs(hour_angle- minutes_angle)