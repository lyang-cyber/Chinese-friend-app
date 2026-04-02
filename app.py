import streamlit as st
import google.generativeai as genai

# --- 1. SETUP & API CONFIG ---
API_KEY = "YOUR_API_KEY" # Make sure your real key is here!
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="Find a Chinese Friend", page_icon="🏮")

# --- 2. VOCABULARY LISTS WITH PINYIN ---
# We use a Dictionary { "Display Name": "Clean Chinese for AI" }
cities = {
    "上海 (Shànghǎi)": "上海", "北京 (Běijīng)": "北京", "成都 (Chéngdū)": "成都", 
    "广州 (Guǎngzhōu)": "广州", "深圳 (Shēnzhèn)": "深圳", "西安 (Xī'ān)": "西安", 
    "香港 (Xiānggǎng)": "香港", "沈阳 (Shěnyáng)": "沈阳"
}

jobs = {
    "学生 (Xuésheng)": "学生", "老师 (Lǎoshī)": "老师", 
    "电脑工程师 (Diànnǎo gōngchéngshī)": "电脑工程师", "医生 (Yīshēng)": "医生"
}

hobbies = {
    "唱歌 (Chànggē)": "唱歌", "听音乐 (Tīng yīnyuè)": "听音乐", "跳舞 (Tiàowǔ)": "跳舞", 
    "做饭 (Zuòfàn)": "做饭", "看书 (Kànshū)": "看书", "看电影 (Kàn diànyǐng)": "看电影", 
    "打游戏 (Dǎ yóuxì)": "打游戏", "打球 (Dǎqiú)": "打球", "爬山 (Páshān)": "爬山", 
    "游泳 (Yóuyǒng)": "游泳", "看电视 (Kàn diànshì)": "看电视"
}

personalities = {
    "友好 (Yǒuhǎo)": "友好", "聪明 (Cōngmíng)": "聪明", "内向 (Nèixiàng)": "内向", 
    "外向 (Wàixiàng)": "外向", "幽默 (Yōumò)": "幽默", "可爱 (Kě'ài)": "可爱", "有意思 (Yǒu yìsi)": "有意思"
}

looks = {
    "胖 (Pàng)": "胖", "瘦 (Shòu)": "瘦", "不胖不瘦 (Bú pàng bú shòu)": "不胖不瘦", 
    "高 (Gāo)": "高", "矮 (Ǎi)": "矮", "不高不矮 (Bù gāo bù ǎi)": "不高不矮", 
    "帅 (Shuài)": "帅", "漂亮 (Piàoliang)": "漂亮", "大眼睛 (Dà yǎnjīng)": "大眼睛", 
    "小眼睛 (Xiǎo yǎnjīng)": "小眼睛", "长头发 (Cháng tóufa)": "长头发", 
    "短头发 (Duǎn tóufa)": "短头发", "中等头发 (Zhōngděng tóufa)": "中等头发", 
    "黑头发 (Hēi tóufa)": "黑头发", "金发 (Jīnfà)": "金发", "棕色头发 (Zōngsè tóufa)": "棕色头发"
}

purposes = {
    "我教他英文 (Wǒ jiāo tā Yīngwén)": "我教他英文", 
    "跟他说英文 (Gēn tā shuō Yīngwén)": "跟他说英文", 
    "他教我中文 (Tā jiāo wǒ Zhōngwén)": "他教我中文", 
    "跟他说中文 (Gēn tā shuō Zhōngwén)": "跟他说中文", 
    "他教我做中国菜 (Tā jiāo wǒ zuò Zhōngguó cài)": "他教我做中国菜", 
    "他帮我做作业 (Tā bāng wǒ zuò zuòyè)": "他帮我做作业", 
    "一起打游戏 (Yìqǐ dǎ yóuxì)": "一起打游戏", 
    "聊天 (Liáotiān)": "聊天"
}

st.title("🏮 找一个中国朋友")
st.write("Select the words to meet your new friend!")

# --- 3. UI LAYOUT ---
col1, col2 = st.columns(2)
with col1:
    gender = st.radio("Gender (性别)", ["男 (Mán - Male)", "女 (Nǚ - Female)"])
    # .keys() shows the label with Pinyin, but returns the clean Chinese
    display_city = st.selectbox("City (城市)", list(cities.keys()))
    display_job = st.selectbox("Job (职业)", list(jobs.keys()))

with col2:
    display_hobby = st.selectbox("Hobby (爱好)", list(hobbies.keys()))
    display_look = st.multiselect("Look (长相)", list(looks.keys()))
    display_personality = st.selectbox("Personality (性格)", list(personalities.keys()))

display_purpose = st.selectbox("Purpose (目的)", list(purposes.keys()))

# --- 4. GENERATION ---
if st.button("Generate My Friend! ✨"):
    # Convert labels back to clean Chinese for the AI prompt
    city = cities[display_city]
    job = jobs[display_job]
    hobby = hobbies[display_hobby]
    personality = personalities[display_personality]
    look_list = [looks[item] for item in display_look]
    purpose = purposes[display_purpose]
    
    with st.spinner("AI is drawing... 正在画画..."):
        # (The rest of your image generation code goes here)
        # Construct prompt using the clean 'city', 'job', etc.
        prompt = f"A realistic portrait of a {gender} from {city}, China. Job: {job}. Personality: {personality}. Look: {', '.join(look_list)}. Hobby: {hobby}."
        
        # [Simulating Image Generation for this example]
        st.success("Success!")
        st.write(f"### 你好！我是你的新朋友。")
        st.write(f"我住在**{display_city}**。我是一个**{display_job}**。")
