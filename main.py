import streamlit as st
import os

# --- 1. 기본 설정 ---
# 브라우저 탭 이름 설정 및 모바일 화면처럼 보이기 위한 레이아웃 설정
st.set_page_config(page_title="ABLE MEDISKIN 랜딩페이지 시안", layout="centered")

# --- 2. 비밀번호 인증 로직 ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.title("🔒 Security Check")
    pwd = st.text_input("시안을 확인하려면 비밀번호를 입력하세요.", type="password")
    
    if st.button("확인", use_container_width=True):
        if pwd == "able1231":  # 요청하신 비밀번호 설정
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("비밀번호가 올바르지 않습니다.")

# 인증되지 않았으면 비밀번호 입력창만 띄우고 아래 코드는 실행하지 않음
if not st.session_state["authenticated"]:
    check_password()
    st.stop()


# --- 3. 모바일 UI 스타일링 (CSS) ---
# PC에서 봐도 모바일처럼 좁게 보이고, 이미지 사이의 여백을 없앱니다.
st.markdown("""
    <style>
    /* 상단 메뉴, 헤더, 푸터 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* 배경색 지정 */
    .stApp {
        background-color: #f0f0f0;
    }

    /* 화면 중앙 480px(모바일 사이즈) 고정 및 여백 제거 */
    .main .block-container {
        max-width: 480px; 
        padding-top: 0;
        padding-bottom: 0;
        padding-left: 0;
        padding-right: 0;
        margin: 0 auto;
        background-color: white;
        box-shadow: 0 0 20px rgba(0,0,0,0.1);
    }
    
    /* Streamlit 이미지 간의 기본 여백 최소화 */
    [data-testid="stImage"] {
        margin-bottom: -5px; 
    }
    </style>
    """, unsafe_allow_html=True)


# --- 4. 시안 이미지 순서대로 불러오기 ---
# 첨부해주신 순서대로 파일명을 배열로 정리했습니다. 
# 실제 저장하신 파일명과 확장자(.jpg, .png)가 완벽히 일치해야 합니다.
image_files = [
    "랜딩페이지_시안_v1피부-고민.png",
    "랜딩페이지_시안_v12.png",
    "랜딩페이지_시안_v13.png",
    "랜딩페이지_시안_v14-2-첫-방문-체험-프로그램.png",
    "랜딩페이지_시안_v15.png",
    "랜딩페이지_시안_v16.png"
    "랜딩페이지_시안_v17.png"
    "랜딩페이지_시안_v18.png"
]

# 이미지를 반복문을 통해 순서대로 화면에 렌더링
for img_file in image_files:
    if os.path.exists(img_file):
        st.image(img_file, use_container_width=True)
    else:
        # 파일이 없을 경우 에러 메시지 출력 (디버깅 용도)
        st.error(f"⚠️ 이미지를 찾을 수 없습니다: {img_file}")
        st.info("파일 이름과 확장자가 코드와 정확히 일치하는지 확인해주세요.")