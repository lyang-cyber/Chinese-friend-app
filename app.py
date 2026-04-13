import React, { useState } from 'react';
import { Sparkles, Heart, User, Palette, Smile, Ruler, Camera, Loader2, Wand2, Image as ImageIcon, Download, RefreshCw, BoxSelect } from 'lucide-react';

export default function App() {
  const [loading, setLoading] = useState(false);
  const [generatedImage, setGeneratedImage] = useState(null);
  const [error, setError] = useState(null);

  // Options Data with Pinyin and English
  const options = {
    gender: [
      { value: 'girlfriend', label: '理想女友', pinyin: 'lǐ xiǎng nǚ yǒu', en: 'Ideal Girlfriend' },
      { value: 'boyfriend', label: '理想男友', pinyin: 'lǐ xiǎng nán yǒu', en: 'Ideal Boyfriend' }
    ],
    composition: [
      { value: 'headshot', label: '大头照', pinyin: 'dà tóu zhào', en: 'Close-up Face Shot' },
      { value: 'halfbody', label: '半身照', pinyin: 'bàn shēn zhào', en: 'Top Waist Up Portrait' },
      { value: 'fullbody', label: '全身照', pinyin: 'quán shēn zhào', en: 'Full-body Shot (Head to Toe)' },
      { value: 'sheet', label: '三视图', pinyin: 'sān shì tú', en: 'Character Sheet (Head, Half, Full)' }
    ],
    artStyle: [
      { value: '动漫风格', label: '动漫风格', pinyin: 'dòng màn fēng gé', en: 'Anime Style Illustration' },
      { value: '超写实', label: '超写实', pinyin: 'chāo xiě shí', en: 'Hyper-Realistic Photography' },
      { value: '油画风格', label: '油画风格', pinyin: 'yóu huà fēng gé', en: 'Classic Oil Painting' },
      { value: '3D卡通', label: '3D卡通', pinyin: 'sān dì kǎ tōng', en: 'Disney/Pixar 3D Style' },
      { value: '素描手绘', label: '素描手绘', pinyin: 'sù miáo shǒu huì', en: 'Pencil Sketch' },
      { value: '水彩画', label: '水彩画', pinyin: 'shuǐ cǎi huà', en: 'Soft Watercolor' }
    ],
    hairStyle: [
      { value: '长直发', label: '长直发', pinyin: 'cháng zhí fā', en: 'Long Straight Hair' },
      { value: '大波浪卷发', label: '大波浪卷发', pinyin: 'dà bō làng juǎn fā', en: 'Big Wavy Hair' },
      { value: '齐肩短发', label: '齐肩短发', pinyin: 'qí jiān duǎn fā', en: 'Shoulder-length Short' },
      { value: '利落短发', label: '利落短发', pinyin: 'lì luò duǎn fā', en: 'Clean Short Cut' },
      { value: '韩式纹理烫', label: '韩式纹理烫', pinyin: 'hán shì wén lǐ tàng', en: 'Korean Textured Perm' },
      { value: '狼尾发型', label: '狼尾发型', pinyin: 'láng wěi fā xíng', en: 'Wolf Cut / Mullet' },
      { value: '丸子头', label: '丸子头', pinyin: 'wán zi tóu', en: 'Bun Hairstyle' },
      { value: '高马尾', label: '高马尾', pinyin: 'gāo mǎ wěi', en: 'High Ponytail' }
    ],
    hairColor: [
      { value: '黑色', label: '黑色', pinyin: 'hēi sè', en: 'Black' },
      { value: '深棕色', label: '深棕色', pinyin: 'shēn zōng sè', en: 'Dark Brown' },
      { value: '栗色', label: '栗色', pinyin: 'lì sè', en: 'Chestnut' },
      { value: '亚麻色', label: '亚麻色', pinyin: 'yà má sè', en: 'Flaxen / Linen' },
      { value: '银灰色', label: '银灰色', pinyin: 'yín huī sè', en: 'Silver Grey' },
      { value: '粉色', label: '粉色', pinyin: 'fěn sè', en: 'Pink' },
      { value: '金发', label: '金发', pinyin: 'jīn fā', en: 'Blonde' },
      { value: '挑染', label: '挑染', pinyin: 'tiāo rǎn', en: 'Highlighted' }
    ],
    eyeColor: [
      { value: '深棕色', label: '深棕色', pinyin: 'shēn zōng sè', en: 'Dark Brown' },
      { value: '黑色', label: '黑色', pinyin: 'hēi sè', en: 'Black' },
      { value: '琥珀色', label: '琥珀色', pinyin: 'hǔ pò sè', en: 'Amber' },
      { value: '蓝色', label: '蓝色', pinyin: 'lán sè', en: 'Blue' },
      { value: '绿色', label: '绿色', pinyin: 'lǜ sè', en: 'Green' },
      { value: '灰蓝色', label: '灰蓝色', pinyin: 'huī lán sè', en: 'Grey Blue' }
    ],
    faceShape: [
      { value: '鹅蛋脸', label: '鹅蛋脸', pinyin: 'é dàn liǎn', en: 'Oval Face' },
      { value: '瓜子脸', label: '瓜子脸', pinyin: 'guā zǐ liǎn', en: 'V-line / Melon Face' },
      { value: '圆脸', label: '圆脸', pinyin: 'yuán liǎn', en: 'Round Face' },
      { value: '方脸', label: '方脸', pinyin: 'fāng liǎn', en: 'Square Face' },
      { value: '心形脸', label: '心形脸', pinyin: 'xīn xíng liǎn', en: 'Heart-shaped Face' },
      { value: '棱角分明', label: '棱角分明', pinyin: 'léng jiǎo fēn míng', en: 'Chiseled / Sharp' }
    ],
    noseShape: [
      { value: '小巧挺拔', label: '小巧挺拔', pinyin: 'xiǎo qiǎo tǐng bá', en: 'Small & Perky' },
      { value: '高鼻梁', label: '高鼻梁', pinyin: 'gāo bí liáng', en: 'High Bridge' },
      { value: '直挺', label: '直挺', pinyin: 'zhí tǐng', en: 'Straight' },
      { value: '圆润可爱', label: '圆润可爱', pinyin: 'yuán rùn kě ài', en: 'Round & Cute' }
    ],
    height: [
      { value: '155cm-160cm', label: '155-160cm', pinyin: "5'1\"-5'3\" - jiāo xiǎo (Petite)", en: "Petite (5'1\"-5'3\")" },
      { value: '160cm-165cm', label: '160-165cm', pinyin: "5'3\"-5'5\" - zhōng děng (Medium)", en: "Medium (5'3\"-5'5\")" },
      { value: '165cm-170cm', label: '165-170cm', pinyin: "5'5\"-5'7\" - zhōng děng (Medium)", en: "Medium Tall (5'5\"-5'7\")" },
      { value: '170cm-175cm', label: '170-175cm', pinyin: "5'7\"-5'9\" - gāo tiāo (Tall)", en: "Tall (5'7\"-5'9\")" },
      { value: '175cm-180cm', label: '175-180cm', pinyin: "5'9\"-5'11\" - gāo dà (Tall)", en: "Very Tall (5'9\"-5'11\")" },
      { value: '180cm-185cm', label: '180-185cm', pinyin: "5'11\"-6'1\" - gāo dà (Tall)", en: "Model Height (5'11\"-6'1\")" },
      { value: '185cm+', label: '185cm+', pinyin: "6'1\"+ - fēi cháng gāo (Very Tall)", en: "Basketball Player (6'1\"+)" }
    ],
    clothingStyle: [
      { value: '休闲时尚', label: '休闲时尚', pinyin: 'xiū xián shí shàng', en: 'Casual Fashion' },
      { value: '学院风', label: '学院风', pinyin: 'xué yuàn fēng', en: 'Preppy / Academic' },
      { value: '日系清新', label: '日系清新', pinyin: 'rì xì qīng xīn', en: 'Japanese Fresh' },
      { value: '优雅知性', label: '优雅知性', pinyin: 'yōu yǎ zhī xìng', en: 'Elegant' },
      { value: '运动活力', label: '运动活力', pinyin: 'yùn dòng huó lì', en: 'Sporty' },
      { value: '古风汉服', label: '古风汉服', pinyin: 'gǔ fēng hàn fú', en: 'Hanfu / Traditional' },
      { value: '赛博朋克', label: '赛博朋克', pinyin: 'sài bó péng kè', en: 'Cyberpunk' },
      { value: '晚礼服', label: '晚礼服', pinyin: 'wǎn lǐ fú', en: 'Formal / Evening' }
    ],
    personality: [
      { value: '温柔体贴', label: '温柔体贴', pinyin: 'wēn róu tǐ tiē', en: 'Gentle & Considerate' },
      { value: '开朗阳光', label: '开朗阳光', pinyin: 'kāi lǎng yáng guāng', en: 'Cheerful & Sunny' },
      { value: '高冷霸道', label: '高冷霸道', pinyin: 'gāo lěng bà dào', en: 'Cool & Domineering' },
      { value: '可爱呆萌', label: '可爱呆萌', pinyin: 'kě ài dāi méng', en: 'Cute & Ditzy' },
      { value: '幽默风趣', label: '幽默风趣', pinyin: 'yōu mò fēng qù', en: 'Humorous' },
      { value: '成熟稳重', label: '成熟稳重', pinyin: 'chéng shú wěn zhòng', en: 'Mature & Steady' },
      { value: '自信迷人', label: '自信迷人', pinyin: 'zì xìn mí rén', en: 'Confident' },
      { value: '善良纯真', label: '善良纯真', pinyin: 'shàn liáng chún zhēn', en: 'Kind & Innocent' },
      { value: '热情大方', label: '热情大方', pinyin: 'rè qíng dà fāng', en: 'Enthusiastic & Generous' },
      { value: '认真负责', label: '认真负责', pinyin: 'rèn zhēn fù zé', en: 'Serious & Responsible' },
      { value: '聪明伶俐', label: '聪明伶俐', pinyin: 'cōng míng líng lì', en: 'Smart & Clever' },
      { value: '勇敢坚强', label: '勇敢坚强', pinyin: 'yǒng gǎn jiān qiáng', en: 'Brave & Strong' },
      { value: '运动健将', label: '运动健将', pinyin: 'yùn dòng jiàn jiàng', en: 'Athletic / Sporty' },
      { value: '讲义气', label: '讲义气', pinyin: 'jiǎng yì qì', en: 'Loyal & Faithful' },
      { value: '学霸', label: '学霸', pinyin: 'xué bà', en: 'Studious / Academic Star' },
      { value: '顾家', label: '顾家', pinyin: 'gù jiā', en: 'Family-oriented' }
    ]
  };

  // State for form selections
  const [formData, setFormData] = useState({
    gender: 'girlfriend',
    composition: 'halfbody',
    artStyle: '动漫风格',
    hairStyle: '长直发',
    hairColor: '黑色',
    eyeColor: '深棕色',
    faceShape: '鹅蛋脸',
    noseShape: '小巧挺拔',
    height: '165cm-170cm',
    clothingStyle: '休闲时尚',
    personality: [],
  });

  const handleInputChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: value
    }));
  };

  const togglePersonality = (traitValue) => {
    setFormData(prev => {
      const current = prev.personality;
      if (current.includes(traitValue)) {
        return { ...prev, personality: current.filter(t => t !== traitValue) };
      } else {
        if (current.length >= 5) return prev; 
        return { ...prev, personality: [...current, traitValue] };
      }
    });
  };

  const downloadImage = () => {
    if (!generatedImage) return;
    const link = document.createElement('a');
    link.href = generatedImage;
    link.download = `dream_${formData.gender}_${Date.now()}.png`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  // Helper to get English text for prompt
  const getEnglish = (category, value) => {
    const option = options[category].find(opt => opt.value === value);
    return option ? option.en : value;
  };

  // Helper to get Label text for display
  const getLabel = (category, value) => {
    const option = options[category].find(opt => opt.value === value);
    return option ? option.label : value;
  };

  const generateImage = async () => {
    setLoading(true);
    setError(null);
    setGeneratedImage(null);

    try {
      // Construct the prompt using English translations for better AI understanding
      const genderTerm = formData.gender === 'girlfriend' ? 'beautiful girl, girlfriend' : 'handsome boy, boyfriend';
      
      const compositionEn = getEnglish('composition', formData.composition);
      const hairStyleEn = getEnglish('hairStyle', formData.hairStyle);
      const hairColorEn = getEnglish('hairColor', formData.hairColor);
      const eyeColorEn = getEnglish('eyeColor', formData.eyeColor);
      const faceShapeEn = getEnglish('faceShape', formData.faceShape);
      const noseShapeEn = getEnglish('noseShape', formData.noseShape);
      const clothingEn = getEnglish('clothingStyle', formData.clothingStyle);
      const personalityEn = formData.personality.map(p => getEnglish('personality', p)).join(', ');
      const artStyleEn = getEnglish('artStyle', formData.artStyle);
      
      // Updated prompt structure for better composition control
      const prompt = `Best quality, masterpiece, high resolution, 8k, detailed ${compositionEn} of a ${genderTerm}, 
      ${hairStyleEn} style, ${hairColorEn} hair, 
      ${eyeColorEn} eyes, ${faceShapeEn}, ${noseShapeEn} nose, 
      wearing ${clothingEn} clothes. 
      Vibe: ${personalityEn}. 
      Height visualization: ${formData.height}. 
      ${artStyleEn}.`;

      const apiKey = ""; 
      const url = `https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key=${apiKey}`;

      const response = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          instances: [{ prompt: prompt }],
          parameters: { sampleCount: 1, aspectRatio: "3:4" }
        }),
      });

      if (!response.ok) {
        let errorData;
        try {
            errorData = await response.json();
        } catch (e) {
            errorData = { error: { message: response.statusText } };
        }
        throw new Error(`Generation failed: ${errorData.error?.message || response.statusText}`);
      }
      
      const data = await response.json();
      
      if (data.predictions && data.predictions[0] && data.predictions[0].bytesBase64Encoded) {
        setGeneratedImage(`data:image/png;base64,${data.predictions[0].bytesBase64Encoded}`);
      } else {
        throw new Error("No image data received");
      }

    } catch (err) {
      console.error(err);
      setError("哎呀，图片生成遇到了一点小问题，请重试！(Error: " + err.message + ")");
    } finally {
      setLoading(false);
    }
  };

  // Helper component for Select options
  const SelectField = ({ label, field, icon: Icon }) => (
    <div className="space-y-1">
      <label className="text-sm font-medium text-slate-600 flex items-center gap-1">
        {Icon && <Icon className="w-3 h-3" />} {label}
      </label>
      <select 
        value={formData[field]}
        onChange={(e) => handleInputChange(field, e.target.value)}
        className="w-full p-2.5 rounded-lg border border-slate-300 focus:ring-2 focus:ring-pink-400 focus:border-transparent bg-white/50 text-sm md:text-base"
      >
        {options[field].map(o => (
          <option key={o.value} value={o.value}>
            {o.label} [{o.pinyin}] - {o.en}
          </option>
        ))}
      </select>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-pink-100 via-purple-100 to-indigo-100 font-sans text-slate-800 p-2 md:p-8">
      <div className="max-w-5xl mx-auto bg-white/80 backdrop-blur-xl rounded-3xl shadow-2xl overflow-hidden border border-white/50 flex flex-col md:flex-row h-auto md:h-[850px]">
        
        {/* Left Column: Controls (Scrollable) */}
        <div className="w-full md:w-1/2 flex flex-col bg-white/40">
          
          {/* Header */}
          <div className="bg-gradient-to-r from-pink-500 to-purple-600 p-4 md:p-6 text-white text-center relative flex-shrink-0">
             <div className="absolute top-0 left-0 w-full h-full opacity-10 bg-[url('https://www.transparenttextures.com/patterns/stardust.png')]"></div>
             <h1 className="text-2xl md:text-3xl font-bold flex items-center justify-center gap-2 relative z-10">
              <Sparkles className="w-6 h-6 text-yellow-300" />
              梦幻男/女朋友图片生成器
              <Heart className="w-6 h-6 text-red-300" />
            </h1>
            <p className="text-pink-100 text-xs md:text-sm mt-1">Dream Picture Generator (Nano Banana Pro)</p>
          </div>

          {/* Form Content */}
          <div className="flex-grow overflow-y-auto p-4 md:p-6 space-y-6 scrollbar-thin scrollbar-thumb-pink-200">
            
            {/* Gender */}
            <div className="space-y-2">
              <label className="flex items-center gap-2 text-base font-bold text-purple-700">
                <User className="w-4 h-4" /> 选择对象 (Select Partner)
              </label>
              <div className="grid grid-cols-2 gap-3">
                {options.gender.map((opt) => (
                  <button
                    key={opt.value}
                    onClick={() => handleInputChange('gender', opt.value)}
                    className={`py-3 px-2 rounded-xl border-2 transition-all duration-200 flex flex-col items-center justify-center text-center ${
                      formData.gender === opt.value
                        ? 'border-pink-500 bg-pink-50 text-pink-700 shadow-md scale-[1.02]'
                        : 'border-slate-200 text-slate-500 hover:border-pink-200 hover:bg-white'
                    }`}
                  >
                    <span className="text-lg font-bold">{opt.label}</span>
                    <span className="text-xs text-slate-400 italic font-serif">{opt.pinyin}</span>
                    <span className="text-xs font-medium mt-0.5">{opt.en}</span>
                  </button>
                ))}
              </div>
            </div>

            {/* Appearance */}
            <div className="space-y-4">
              <h3 className="flex items-center gap-2 text-base font-bold text-purple-700 border-b border-purple-100 pb-2">
                <Palette className="w-4 h-4" /> 长相 (Appearance)
              </h3>
              
              <div className="grid grid-cols-1 gap-4">
                <div className="grid grid-cols-2 gap-3">
                  <SelectField label="发型 (Hair Style)" field="hairStyle" />
                  <SelectField label="发色 (Hair Color)" field="hairColor" />
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <SelectField label="瞳色 (Eye Color)" field="eyeColor" />
                  <SelectField label="脸型 (Face Shape)" field="faceShape" />
                </div>
                <div className="grid grid-cols-2 gap-3">
                   <SelectField label="鼻型 (Nose)" field="noseShape" />
                   <SelectField label="身高 (Height)" field="height" icon={Ruler} />
                </div>
                <div className="grid grid-cols-2 gap-3">
                  <SelectField label="穿搭风格 (Clothing)" field="clothingStyle" />
                  <SelectField label="画风 (Art Style)" field="artStyle" icon={ImageIcon} />
                </div>
                <div className="grid grid-cols-1 gap-3">
                  <SelectField label="构图范围 (Composition)" field="composition" icon={BoxSelect} />
                </div>
              </div>
            </div>

            {/* Personality */}
            <div className="space-y-3 pb-4">
              <h3 className="flex items-center gap-2 text-base font-bold text-purple-700 border-b border-purple-100 pb-2">
                <Smile className="w-4 h-4" /> 性格特点 (Personality) - Max 5
              </h3>
              <div className="grid grid-cols-2 gap-2">
                {options.personality.map((opt) => (
                  <button
                    key={opt.value}
                    onClick={() => togglePersonality(opt.value)}
                    className={`p-2 rounded-lg text-left transition-all border ${
                      formData.personality.includes(opt.value)
                        ? 'bg-purple-100 border-purple-400 text-purple-900'
                        : 'bg-white border-slate-200 text-slate-600 hover:border-purple-200'
                    }`}
                  >
                    <div className="font-bold text-sm">{opt.label}</div>
                    <div className="text-xs text-slate-500 italic">{opt.pinyin}</div>
                    <div className="text-xs text-slate-400">{opt.en}</div>
                  </button>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Right Column: Preview & Output */}
        <div className="w-full md:w-1/2 bg-slate-50 border-l border-slate-200 flex flex-col">
          
          <div className="flex-grow flex flex-col justify-center items-center p-6 bg-[radial-gradient(ellipse_at_top_right,_var(--tw-gradient-stops))] from-purple-100/50 via-white to-white">
            {generatedImage ? (
              <div className="relative w-full max-w-sm aspect-[3/4] rounded-2xl overflow-hidden shadow-2xl group border-4 border-white">
                <img 
                  src={generatedImage} 
                  alt="Generated Dream Partner" 
                  className="w-full h-full object-cover"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-end p-6">
                  <p className="text-white font-medium text-center w-full">✨ Right click or Download below</p>
                </div>
              </div>
            ) : (
              <div className="w-full max-w-xs aspect-[3/4] bg-white border-4 border-dashed border-slate-300 rounded-3xl flex flex-col items-center justify-center text-slate-400 p-8 text-center shadow-inner">
                <div className="w-24 h-24 bg-slate-100 rounded-full flex items-center justify-center mb-6 shadow-sm">
                  {loading ? (
                    <Loader2 className="w-10 h-10 animate-spin text-pink-500" />
                  ) : (
                    <Camera className="w-10 h-10 text-slate-300" />
                  )}
                </div>
                <p className="font-medium text-lg text-slate-500">
                  {loading ? "Generating..." : "Your dream partner will appear here"}
                </p>
                {loading && <p className="text-sm mt-2 text-pink-500 animate-pulse">Designing with Gemini AI...</p>}
              </div>
            )}

            {error && (
              <div className="mt-4 p-4 bg-red-50 border border-red-100 text-red-600 text-sm rounded-xl text-center max-w-xs">
                {error}
              </div>
            )}
          </div>

          {/* Description Box */}
          <div className="p-6 bg-white border-t border-slate-200 shadow-[0_-5px_15px_rgba(0,0,0,0.02)] relative z-20">
            <div className="mb-4 text-sm text-slate-600 bg-slate-50 p-4 rounded-xl border border-slate-100">
              <span className="font-bold block text-purple-700 mb-2 flex items-center gap-1">
                <Sparkles className="w-3 h-3" /> 当前设定 (Current Settings):
              </span>
              <p className="leading-relaxed">
                {formData.gender === 'girlfriend' ? '她' : '他'} (S/He) 是一个 {getLabel('height', formData.height).split('-')[0]} 的 {getLabel('gender', formData.gender)}。
                {formData.gender === 'girlfriend' ? '她' : '他'} 拥有 {getLabel('hairColor', formData.hairColor)} 的 {getLabel('hairStyle', formData.hairStyle)} 和 {getLabel('eyeColor', formData.eyeColor)} 的眼睛。
                风格: {getLabel('artStyle', formData.artStyle)}。
                构图: {getLabel('composition', formData.composition)}。
              </p>
            </div>

            <div className="flex gap-3">
              <button
                onClick={generateImage}
                disabled={loading}
                className={`flex-1 py-4 rounded-xl text-white font-bold text-lg shadow-xl shadow-purple-200 flex items-center justify-center gap-2 transition-all transform active:scale-[0.98] ${
                  loading 
                    ? 'bg-slate-400 cursor-not-allowed' 
                    : 'bg-gradient-to-r from-pink-500 via-purple-500 to-indigo-500 hover:brightness-110'
                }`}
              >
                {loading ? (
                  <>
                    <Loader2 className="w-6 h-6 animate-spin" />
                    {generatedImage ? '重新生成 (Regenerating)...' : '正在生成 (Generating)...'}
                  </>
                ) : (
                  <>
                    {generatedImage ? <RefreshCw className="w-6 h-6" /> : <Wand2 className="w-6 h-6" />}
                    {generatedImage ? '重新生成 (Regenerate)' : '生成图片 (Generate Image)'}
                  </>
                )}
              </button>

              {generatedImage && !loading && (
                <button
                  onClick={downloadImage}
                  className="px-6 py-4 rounded-xl border-2 border-purple-200 text-purple-700 font-bold text-lg hover:bg-purple-50 transition-all transform active:scale-[0.98] flex items-center justify-center gap-2"
                  title="Download Image"
                >
                  <Download className="w-6 h-6" />
                  下载 (Download)
                </button>
              )}
            </div>
          </div>

        </div>
      </div>
      
      {/* Footer */}
      <div className="mt-6 text-center space-y-1">
        <p className="text-slate-500 font-medium text-sm">Powered by Gemini & Imagen</p>
        <p className="text-slate-400 text-xs">Updated: 2026</p>
      </div>

    </div>
  );
}
