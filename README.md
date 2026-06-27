# 🌤️ Weather App

A clean, responsive weather forecast app built with vanilla HTML, CSS, and JavaScript. Enter any city and get real-time weather data with dynamic backgrounds and Lottie animations that match the current conditions.

![Weather App Preview](https://img.shields.io/badge/status-live-brightgreen) ![HTML](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white) ![CSS](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

---

## ✨ Features

- 🔍 Search weather for any city worldwide
- 🌡️ Real-time temperature and condition data via OpenWeatherMap API
- 🎨 Dynamic gradient backgrounds that change based on weather conditions
- 🎞️ Lottie animations for sunny, cloudy, rainy, snowy, foggy, and more
- 📱 Fully responsive — works great on mobile and desktop
- ⚡ Zero dependencies, no build step required

---

## 🌦️ Supported Weather Conditions

| Condition | Background | Animation |
|-----------|-----------|-----------|
| ☀️ Clear | Warm golden gradient | Sun animation |
| ☁️ Clouds | Dark grey gradient | Cloud animation |
| 🌧️ Rain | Deep blue-grey gradient | Rain animation |
| ⛈️ Thunderstorm | Dark stormy gradient | Lightning animation |
| ❄️ Snow | Icy white gradient | Snow animation |
| 🌫️ Mist / Fog / Haze | Earthy gradient | Fog animation |
| 🌦️ Drizzle | Navy blue gradient | Drizzle animation |
| 🌬️ Wind / Tornado | Sky blue gradient | Wind animation |

---

## 🚀 Live Demo

> Deployed on [Vercel](https://vercel.com) — add your deployment URL here once live.

---

## 🛠️ Getting Started

### Run Locally

No build tools needed. Just open the file in a browser:

```bash
# Clone the repository
git clone https://github.com/your-username/weather-app.git

# Navigate into the folder
cd weather-app

# Open in browser
start weather-app.html        # Windows
open weather-app.html         # macOS
xdg-open weather-app.html     # Linux
```

### Deploy to Vercel

**Option 1 — Vercel CLI**

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy from the project folder
vercel
```

Follow the prompts. Vercel will auto-detect the static site and deploy it.

**Option 2 — Vercel Dashboard (no CLI)**

1. Push this project to a GitHub repository
2. Go to [vercel.com](https://vercel.com) and sign in
3. Click **Add New → Project**
4. Import your GitHub repository
5. Leave all settings as default and click **Deploy**

That's it — Vercel handles the rest.

---

## 🔑 API Key

This app uses the [OpenWeatherMap API](https://openweathermap.org/api). The key is included in the source for demo purposes.

If you want to use your own key:

1. Sign up at [openweathermap.org](https://openweathermap.org) (free tier is enough)
2. Copy your API key
3. In `weather-app.html`, replace the value on this line:

```js
const apiKey = 'YOUR_API_KEY_HERE';
```

---

## 📁 Project Structure

```
weather-app/
├── weather-app.html   # Main app — all markup, styles, and logic
├── style.css          # Standalone stylesheet (referenced externally)
├── vercel.json        # Vercel deployment config
└── README.md          # This file
```

---

## 🧰 Tech Stack

- **HTML5** — structure and layout
- **CSS3** — glassmorphism card, gradients, responsive design
- **JavaScript (ES6+)** — API calls, DOM manipulation, dynamic theming
- **OpenWeatherMap API** — live weather data
- **Lottie (lottie-player)** — weather condition animations
- **Google Fonts (Outfit)** — typography

---

## 📸 Screenshots

> Add screenshots here after deployment. You can use `![alt text](image-url)` syntax.

---

## 👤 Author

**Muhammad Ahmad**
📧 [mahmad937ak@gmail.com](mailto:mahmad937ak@gmail.com)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
