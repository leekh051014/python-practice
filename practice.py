import math

def calculate_reaction_rate(k, concentration):
    """
    일차 반응 속도식을 통해 반응 속도를 계산하는 함수
    k: 반응 속도 상수
    concentration: 반응물 농도
    """
    rate = k * concentration
    return rate

# 반응 속도 상수와 반응물 농도 설정
k = 0.05   # 반응 속도 상수
concentration = 0.1   # 반응물 농도

# 반응 속도 계산
reaction_rate = calculate_reaction_rate(k, concentration)
print("반응 속도:", reaction_rate)
