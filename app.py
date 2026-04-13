import streamlit as st

# --- 1. VOCABULARY DICTIONARIES ---
# (Pinyin remains the same, used for labels)
cities = {
    "上海 (Shànghǎi)": "Shanghai", "北京 (Běijīng)": "Beijing", "成都 (Chéngdū)": "Chengdu", 
    "广州 (Guǎngzhōu)": "Guangzhou", "深圳 (Shēnzhèn)": "Shenzhen", "西安 (Xī'ān)": "Xi'an", 
    "香港 (Xiānggǎng)": "Hong Kong", "沈阳 (Shěnyáng)": "Shenyang"
}

jobs = {
    "学生 (Xuésheng)": "Student", "老师 (Lǎoshī)": "Teacher", 
    "电脑工程师 (Diànnǎo gōngchéngshī)": "Computer Engineer", "医生 (Yīshēng)": "Doctor"
}

hobbies = {
    "听音乐 (Tīng yīnyuè)": "Listening to music", 
    "做饭 (Zuòfàn)": "Cooking", "看书 (Kànshū)": "Reading", 
    "看电影 (Kàn diànyǐng)": "Watching movies", "打游戏 (Dǎ yóuxì)": "Gaming", 
    "打球 (Dǎqiú)": "Playing ball", 
    "游泳 (Yóuyǒng)": "Swimming", "看电视 (Kàn diànshì)": "Watching TV"
}

personalities = {
    "友好 (Yǒuhǎo)": "Friendly", "聪明 (Cōngmíng)": "Smart", "内向 (Nèixiàng)": "Introverted", 
    "外向 (Wàixiàng)": "Extroverted", "幽默 (Yōumò)": "Humorous", 
    "可爱 (Kě'ài)": "Cute", "有意思 (Yǒu yìsi)": "Interesting"
}

looks = {
    "胖 (Pàng)": "Chubby", "瘦 (Shòu)": "Thin", "不胖不瘦 (Bú pàng bú shòu)": "Average build", 
    "高 (Gāo)": "Tall", "矮 (Ǎi)": "Short", "不高不矮 (Bù gāo bù ǎi)": "Average height", 
    "帅 (Shuài)": "Handsome", "漂亮 (Piàoliang)": "Pretty", "大眼睛 (Dà yǎnjīng)": "Big eyes", 
    "小眼睛 (Xiǎo yǎnjīng)": "Small eyes", "长头发 (Cháng tóufa)": "Long hair", 
    "短头发 (Duǎn tóufa)": "Short hair", "中等头发 (Zhōngděng tóufa)": "Medium hair", 
    "黑头发 (Hēi tóufa)": "Black hair", "金发 (Jīnfà)": "Blonde hair", "棕色头发 (Zōngsè tóufa)": "Brown hair"
}

purposes = {
    "我教他英文 (Wǒ jiāo tā Yīngwén)": "I teach them English", 
    "他教我中文 (Tā jiāo wǒ Zhōngwén)": "They teach me Chinese", 
    "跟他说中文 (Gēn tā shuō Zhōngwén)": "Speak Chinese with them", 
    "他教我做中国菜 (Tā jiāo wǒ zuò Zhōngguó cài)": "They teach me to cook Chinese food", 
    "他帮我做作业 (Tā bāng wǒ zuò zuòyè)": "They help with homework", 
    "一起打游戏 (Yìqǐ dǎ yóuxì)": "Play games together", 
    "聊天 (Liáotiān)": "Chatting"
}

# --- 2. INTERFACE ---
st.set_page_config(page_title="Find a Chinese Friend", page_icon="🏮")

st.title("🏮 找一个中国朋友")
st.write("Pick your choices and see your human friend!")

col1, col2 = st.columns(2)

with col1:
    gender_choice = st.radio("性别 (Gender)", ["男 (Mán)", "女 (Nǚ)"])
    display_city = st.selectbox("城市 (City)", list(cities.keys()))
    display_job = st.selectbox("工作 (Job)", list(jobs.keys()))

with col2:
    display_personality = st.selectbox("性格 (Personality)", list(personalities.keys()))
    display_hobby = st.selectbox("爱好 (Hobby)", list(hobbies.keys()))
    display_look = st.multiselect("长相 (Look)", list(looks.keys()))

display_purpose = st.selectbox("目的 (Purpose)", list(purposes.keys()))

# --- 3. GENERATION LOGIC (Guaranteed Human) ---
if st.button("生成我的朋友！ ✨"):
    st.divider()
    
    # Identify the correct gender for the generator
    if "男" in gender_choice:
        gen = "male"
    else:
        gen = "female"
        
    # Create a unique seed based on ALL vocabulary choices
    seed = f"{gen}-{display_city}-{display_job}-{display_hobby}-{''.join(display_look)}".replace(' ', '')
    
    # THE DICEBEAR HUMAN GENERATOR
    avatar_url = f"https://api.dicebear.com/8.x/lorelei/svg?seed={seed}&mood[]=happy"
    
    # Display the Human image (Lorelei set is very diverse and human)
    st.image(avatar_url, caption=f"你好！ 我是来自{cities[display_city]}的{jobs[display_job]}!", width=300)
    
    # CHINESE SUMMARY
    st.subheader("你的新朋友：")
    look_text = ", ".join(display_look) if display_look else "（未选择）"
    
    st.success(f"""
    * 这位是我的朋友。
    * 他/她住在 **{display_city}**。
    * 他/她是一个 **{display_job}**。
    * 他/她很 **{display_personality}**。
    * 他/她喜欢 **{display_hobby}**。
    * 他/她的长相：**{look_text}**。
    * 目的：**{display_purpose}**。
    """)
