# 🎭 Sentiment Analysis AI App

A simple web application that **analyzes text sentiment** (positive, negative, or neutral) using AI.

## ✨ Features

- 📝 **Enter text** - Type any message or review
- 🤖 **AI Analysis** - Automatically detects sentiment  
- 📊 **See Results** - Score + emoji + colored message
- 📈 **Track History** - Last 5 analyses displayed
- 📉 **Visualizations** - Line chart of sentiment trends
- 📥 **Export CSV** - Download analysis history

## 🚀 Quick Start

### 1. Setup Environment
```bash
conda create -n streamlit python=3.10 -y
conda activate streamlit
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 3. Run App
```bash
streamlit run app.py
```

Your browser opens automatically at `http://localhost:8501`

## 💡 How to Use

1. Type text in the input box (English works best)
2. Click **"🔍 Analyser le sentiment"** button
3. See instant results:
   - **Score**: -1.0 (very negative) to +1.0 (very positive)
   - **Sentiment**: POSITIF (😊) / NÉGATIF (😞) / NEUTRE (😐)
   - **Color**: Green / Red / Blue message

Example:
```
Input:  "This product is absolutely amazing!"
Score:  0.6
Result: 😊 POSITIF
```

## 📁 Project Structure

```
workshop_streamlit/
├── app.py              ← Main application
├── modules/            ← Reusable components
│   ├── analysis.py     (sentiment analysis)
│   ├── history.py      (data management)
│   └── display.py      (UI components)
├── requirements.txt    (dependencies)
```

## 🛠️ Built With

- **Streamlit** - Web interface
- **TextBlob** - Sentiment analysis  
- **Pandas** - Data handling
- **Python 3.10+**

## ⚙️ How It Works

1. **Text Input** → User types message
2. **TextBlob Analysis** → Calculates sentiment score
3. **Classification** → Labels as Positive/Negative/Neutral
4. **Save to History** → Stores last 5 analyses  
5. **Display Results** → Shows metrics and chart
6. **Export Option** → Download as CSV

## 📝 Example Tests

Try these phrases:

| Text | Expected Result |
|------|-----------------|
| "I love this!" | 😊 POSITIF (~0.7) |
| "The meeting is Tuesday" | 😐 NEUTRE (~0.0) |
| "This is terrible" | 😞 NÉGATIF (~-0.7) |

## ⚠️ Notes

- **Best in English** - TextBlob works primarily in English
- **French Support** - Limited (scores may be 0)
- **Session History** - Resets when you refresh the page

## 🐛 Troubleshooting

### Command not found: streamlit
```bash
conda activate streamlit
```

### TextBlob import error
```bash
pip install textblob
python -m textblob.download_corpora
```

### App doesn't open
Open browser manually: `http://localhost:8501`

### Changes don't show
Save file (Ctrl+S) → Click "Rerun" in Streamlit

## 📦 For Developers

The modular architecture makes it easy to:
- ✅ Test individual components
- ✅ Swap sentiment analysis model
- ✅ Add new features
- ✅ Reuse modules in other projects

```python
# Example: Use analysis module elsewhere
from modules.analysis import analyze_sentiment

result = analyze_sentiment("Amazing!")
print(result)  # {'score': 0.6, 'sentiment': 'POSITIF', 'emoji': '😊'}
```

## 🚀 Deploy Online (Free)

1. Push code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repo
4. Done! Live on internet

## 📄 License

Educational project - Free to use and modify

---

**Ready to go!** Start with: `streamlit run app.py` 🎉
