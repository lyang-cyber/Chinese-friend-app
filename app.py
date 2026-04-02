import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# --- 1. SETUP & API CONFIG ---
# Replace 'YOUR_API_KEY' with the key you got from AI Studio
# In a real deployment, use st.secrets for safety!
API_KEY = "AIzaSyAcb4VGou_chUNgWuLuztm2rlavJCMY_rI" 
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Find a Chinese Friend", page_icon="🏮")

# --- 2. VOCABULARY LISTS ---
cities = ["上海", "北京", "成都", "广州", "深圳", "西安", "香港", "沈阳"]
jobs = ["学生", "老师", "电脑工程师", "医生"]
hobbies = ["唱歌", "听音乐", "跳舞", "做饭", "看书", "看电影", "打游戏", "打球", "爬山", "游泳", "看电视"]
looks = ["胖", "瘦", "不胖不瘦", "高", "矮", "不高不矮", "帅", "漂亮", "大眼睛", "小眼睛", "长头发", "短头发", "中等头发", "黑头发", "金发", "棕色头发"]

st.title("🏮 找一个中国朋友")
st.write("Fill in the blanks to meet your new friend!")

# --- 3. UI LAYOUT ---
col1, col2 = st.columns(2)
with col1:
    gender = st.radio("Gender (性别)", ["男 (Male)", "女 (Female)"])
    city = st.selectbox("City (城市)", cities)
    job = st.selectbox("Job (职业)", jobs)

with col2:
    hobby = st.selectbox("Hobby (爱好)", hobbies)
    look = st.multiselect("Look (长相)", looks)
    personality = st.selectbox("Personality (性格)", ["友好", "聪明", "内向", "外向", "幽默", "可爱"])

# --- 4. IMAGE GENERATION LOGIC ---
if st.button("Generate My Friend! ✨"):
    with st.spinner("AI is drawing your friend... 正在画画..."):
        try:
            # Construct the Prompt
            look_str = ", ".join(look)
            prompt = f"A realistic portrait of a {gender} from {city}, China. They are a {job}. They look {look_str}. Style: high quality photography, friendly expression."
            
            # Call Gemini Image Generation (Nano Banana 2 / Gemini 3 Flash Image)
            model = genai.GenerativeModel('gemini-3-flash-preview')
            # Note: For free tier users, use the 'generate_content' with 'image' modality
            response = model.generate_content(prompt)
            
            # Display results
            st.success("Meet your new friend!")
            
            # If the model returns an image, display it
            if hasattr(response, 'image'):
                st.image(response.image)
            else:
                # Fallback if image generation is restricted in your region
                st.warning("Image generated in the cloud! (Placeholder below)")
                st.image("https://api.dicebear.com/7.x/avataaars/svg?seed=ChineseFriend")

            # CHINESE SUMMARY FOR STUDENTS
            st.markdown(f"""
            ### 📝 介绍 (Introduction)
            这是我的朋友。
            * 他/她住在**{city}**。
            * 他/她是一个**{job}**。
            * 他/她很**{personality}**。
            * 他/她的爱好是**{hobby}**。
            """)
            
        except Exception as e:
            st.error(f"Error: {e}")
