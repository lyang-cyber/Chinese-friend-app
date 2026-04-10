import streamlit as st
import google.generativeai as genai
import time

# --- 1. SETUP ---
# (Keep your dictionaries with Pinyin here from our previous code!)
# ... [Insert cities, jobs, hobbies, looks, etc. dictionaries here] ...

cities = {
    "上海 (Shànghǎi)": "上海", "北京 (Běijīng)": "北京", "成都 (Chéngdū)": "成都", 
    "广州 (Guǎngzhōu)": "广州", "深圳 (Shēnzhèn)": "深圳", "西安 (Xī'ān)": "西安", 
    "香港 (Xiānggǎng)": "香港", "沈阳 (Shěnyáng)": "沈阳"
}

# (I will add a simplified list of jobs, hobbies, and personalities for this example)
jobs = {"学生 (Xuésheng)": "学生", "老师 (Lǎoshī)": "老师", "医生 (Yīshēng)": "医生"}
hobbies = {"唱歌 (Chànggē)": "唱歌", "听音乐 (Tīng yīnyuè)": "听音乐"}
personalities = {"友好 (Yǒuhǎo)": "友好", "聪明 (Cōngmíng)": "聪明", "可爱 (Kě'ài)": "可爱"}

# --- 2. THE UI (A clean look for a class activity) ---
st.set_page_config(page_title="Find a Chinese Friend", page_icon="🏮", layout="centered")

st.markdown("# 🏮 找一个中国朋友")
st.markdown("### Let's find your new friend together!")
st.divider()

# Arrange input controls nicely
col1, col2 = st.columns(2)

with col1:
    gender = st.radio("Gender (性别)", ["男 (Mán)", "女 (Nǚ)"])
    display_city = st.selectbox("City (城市)", list(cities.keys()))

with col2:
    display_job = st.selectbox("Job (职业)", list(jobs.keys()))
    display_personality = st.selectbox("Personality (性格)", list(personalities.keys()))

# --- 3. THE "REVEAL" BUTTON ---
if st.button("Generate My Friend! ✨"):
    st.divider()
    
    with st.spinner("AI is drawing your friend... 正在画画..."):
        # This creates a "seed" (a unique text fingerprint) based on their choices
        # We need a fallback seed just in case
        try:
            seed_text = f"{gender}-{display_city}-{display_job}".replace(" ", "")
        except:
            seed_text = "default-friend-seed"

        # (Simulate waiting 1 second for effect)
        time.sleep(1) 

        # --- THE IMAGE MAGIC: Japanese Anime-Style Avatar ---
        # Multiavatar generates a unique character based on the seed
        avatar_url = f"https://api.multiavatar.com/{seed_text}.svg"
        
        # Display the result (Anime-Style Avatar)
        st.header(" Meet Your Friend! 你好！👋")
        st.image(avatar_url, width=300)
        
        # CHINESE SUMMARY FOR STUDENTS (with Pinyin)
        st.success("Success!")
        st.markdown(f"### 介绍 (Introduction)")
        st.markdown(f"**他是我的朋友 (He is my friend).**")
        st.markdown(f"* 他住在**{display_city}**。")
        st.markdown(f"* 他是一个**{display_job}**。")
        st.markdown(f"* 他很**{display_personality}**。")
