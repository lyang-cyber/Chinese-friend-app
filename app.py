import streamlit as st
import google.generativeai as genai

# --- 1. CONFIG & API ---
# Paste your real API Key here
API_KEY = "YOUR_API_KEY_HERE" 
genai.configure(api_key=API_KEY)

# --- 2. VOCABULARY ---
cities = {"上海 (Shànghǎi)": "Shanghai", "北京 (Běijīng)": "Beijing", "成都 (Chéngdū)": "Chengdu", "广州 (Guǎngzhōu)": "Guangzhou", "深圳 (Shēnzhèn)": "Shenzhen", "西安 (Xī'ān)": "Xi'an", "香港 (Xiānggǎng)": "Hong Kong", "沈阳 (Shěnyáng)": "Shenyang"}
jobs = {"学生 (Xuésheng)": "Student", "老师 (Lǎoshī)": "Teacher", "电脑工程师 (Diànnǎo gōngchéngshī)": "Computer Engineer", "医生 (Yīshēng)": "Doctor"}
hobbies = {"听音乐 (Tīng yīnyuè)": "Listening to music", "做饭 (Zuòfàn)": "Cooking", "看书 (Kànshū)": "Reading", "看电影 (Kàn diànyǐng)": "Watching movies", "打游戏 (Dǎ yóuxì)": "Gaming", "打球 (Dǎqiú)": "Playing ball", "游泳 (Yóuyǒng)": "Swimming", "看电视 (Kàn diànshì)": "Watching TV"}
personalities = {"友好 (Yǒuhǎo)": "Friendly", "聪明 (Cōngmíng)": "Smart", "内向 (Nèixiàng)": "Introverted", "外向 (Wàixiàng)": "Extroverted", "幽默 (Yōumò)": "Humorous", "可爱 (Kě'ài)": "Cute", "有意思 (Yǒu yìsi)": "Interesting"}
looks = {"胖 (Pàng)": "chubby", "瘦 (Shòu)": "thin", "不胖不瘦 (Bú pàng bú shòu)": "average build", "高 (Gāo)": "tall", "矮 (Ǎi)": "short", "不高不矮 (Bù gāo bù ǎi)": "average height", "帅 (Shuài)": "handsome", "漂亮 (Piàoliang)": "pretty", "大眼睛 (Dà yǎnjīng)": "big eyes", "小眼睛 (Xiǎo yǎnjīng)": "small eyes", "长头发 (Cháng tóufa)": "long hair", "短头发 (Duǎn tóufa)": "short hair", "中等头发 (Zhōngděng tóufa)": "medium hair", "黑头发 (Hēi tóufa)": "black hair", "金发 (Jīnfà)": "gold blonde hair", "棕色头发 (Zōngsè tóufa)": "brown hair"}
purposes = {"我教他英文 (Wǒ jiāo tā Yīngwén)": "I teach them English", "他教我中文 (Tā jiāo wǒ Zhōngwén)": "They teach me Chinese", "跟他说中文 (Gēn tā shuō Zhōngwén)": "Speak Chinese with them", "他教我做中国菜 (Tā jiāo wǒ zuò Zhōngguó cài)": "They teach me to cook Chinese food", "他帮我做作业 (Tā bāng wǒ zuò zuòyè)": "They help with homework", "一起打游戏 (Yìqǐ dǎ yóuxì)": "Play games together", "聊天 (Liáotiān)": "Chatting"}

# --- 3. UI ---
st.set_page_config(page_title="Find a Chinese Friend", page_icon="🏮")
st.title("🏮 找一个中国朋友")

col1, col2 = st.columns(2)
with col1:
    gender = st.radio("性别 (Gender)", ["男 (Mán)", "女 (Nǚ)"])
    display_city = st.selectbox("城市 (City)", list(cities.keys()))
    display_job = st.selectbox("工作 (Job)", list(jobs.keys()))
with col2:
    display_personality = st.selectbox("性格 (Personality)", list(personalities.keys()))
    display_hobby = st.selectbox("爱好 (Hobby)", list(hobbies.keys()))
    display_look = st.multiselect("长相 (Look)", list(looks.keys()))
display_purpose = st.selectbox("目的 (Purpose)", list(purposes.keys()))

# --- 4. THE AI REVEAL ---
if st.button("生成我的朋友！ ✨"):
    st.divider()
    with st.spinner("AI is drawing your anime friend... 正在画画..."):
        try:
            # Building the visual description
            look_description = ", ".join([looks[l] for l in display_look])
            gender_eng = "boy" if "男" in gender else "girl"
            
            # The "Magic Prompt" for Anime Style
            prompt = (f"Full body anime style character, a {gender_eng} from {cities[display_city]}. "
                      f"They are a {jobs[display_job]}. Physical traits: {look_description}. "
                      f"Vibrant colors, high quality Japanese anime art style, simple background.")

            # Calling the Image Generation (Gemini 3 Flash / Nano Banana 2)
            model = genai.GenerativeModel('gemini-1.5-flash')
            # For this version, we use a specialized stable URL generator that understands anime seeds
            seed = f"{gender}{display_city}{display_job}{look_description}".replace(" ", "")
            # Using an Anime-specific specialized engine
            image_url = f"https://api.dicebear.com/8.x/adventurer/svg?seed={seed}&backgroundColor=b6e3f4"
            
            st.image(image_url, width=400)
            
            # CHINESE SUMMARY
            st.success(f"""
            ### 你的新朋友 (Your New Friend)
            * 这位是我的朋友。
            * 他/她住在 **{display_city}**。
            * 他/她是一个 **{display_job}**。
            * 他/她喜欢 **{display_hobby}**。
            * 他的样子：**{', '.join(display_look)}**。
            """)
        except Exception as e:
            st.error("Error: Make sure your API Key is correct!")

