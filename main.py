
import streamlit as st

# 제목
st.title("💪 나의 첫 Streamlit 프로젝트: BMI 계산기")

# 설명
st.write("""
이 앱은 **BMI(체질량지수)** 를 계산해줍니다.
아래에 키(cm)와 몸무게(kg)를 입력해보세요!
""")

# 사용자 입력
height = st.number_input("키 (cm)", min_value=50.0, max_value=250.0, step=0.1)
weight = st.number_input("몸무게 (kg)", min_value=10.0, max_value=200.0, step=0.1)

# BMI 계산 함수
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    return round(weight_kg / (height_m ** 2), 2)

# 버튼을 눌렀을 때 계산
if st.button("BMI 계산하기"):
    if height > 0 and weight > 0:
        bmi = calculate_bmi(height, weight)
        st.success(f"당신의 BMI는 **{bmi}** 입니다.")

        # 상태 출력
        if bmi < 18.5:
            st.info("저체중입니다.")
        elif 18.5 <= bmi < 23:
            st.success("정상 체중입니다.")
        elif 23 <= bmi < 25:
            st.warning("과체중입니다.")
        else:
            st.error("비만입니다.")
    else:
        st.error("키와 몸무게를 정확히 입력해주세요.")
