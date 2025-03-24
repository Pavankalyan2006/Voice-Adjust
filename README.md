# Voice-Adjust

# 🎤 Real-Time Voice Pitch Analyzer & Adjuster

This project captures real-time voice input, analyzes its pitch frequency (Hz), and adjusts it based on predefined male and female voice frequency ranges. 

## 🚀 Features
- 🎙 **Real-time voice input analysis**
- 🔎 **Displays input pitch (Hz) and adjusted pitch (Hz)**
- 🎚 **Adjusts pitch based on gender selection**
- 🎨 **Modern UI using Tailwind CSS**
- 📊 **Live visualization of frequency data**
- 🌐 **Frontend: HTML, CSS (Tailwind)**
- 🐍 **Backend: Python (Flask, WebRTC, pyaudio, numpy)**

---

## 📌 Pitch Adjustment Logic

| Input Pitch (Hz) | Male Voice Adjustment | Female Voice Adjustment |
|-----------------|----------------------|----------------------|
| < 80           | 🔼 Increase pitch to ~100 Hz | 🔼 Increase pitch to ~100 Hz |
| 80 - 180       | ✅ Keep same | ❌ Not in female range |
| 165 - 255      | ❌ Not in male range | ✅ Keep same |
| > 255          | 🔽 Decrease pitch to ~220 Hz | 🔽 Decrease pitch to ~220 Hz |

---

## 🛠 Installation & Setup

### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/voice-pitch-analyzer.git
cd voice-pitch-analyzer
