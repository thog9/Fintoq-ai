# Fintoq Bot Scripts 🚀

This collection of Python scripts automates tasks on the [Fintoq AI](https://fintoq.ai/referral/1o731077) platform — an AI-powered platform with daily check-ins, chat rewards, quests, and boost features.

🔗 Register (Web): [Fintoq AI](https://fintoq.ai/referral/1o731077)
🔗 Register (Telegram): [Fintoq Bot](https://t.me/Fintoq_Bot?start=ref_921415493)

---

## ✨ Features Overview

### General Features

- **Multi-Account Support**: Reads Telegram initData from `accounts.txt` and email accounts from `email.txt` to process multiple accounts in parallel.
- **Central Menu System**: Interactive menu for easy script selection via `main.py`.
- **Colorful CLI**: Uses `colorama` for visually appealing output with box-drawing borders and colored icons.
- **Asynchronous Execution**: Built with `asyncio` for efficient concurrent task processing using semaphore-based threading.
- **Error Handling**: Comprehensive error catching with retry logic and real-time response debugging.
- **Bilingual Support**: Supports both English and Vietnamese output.
- **Proxy Support**: Supports HTTP, HTTPS, SOCKS4, and SOCKS5 proxies via `proxies.txt`.

---

### Included Scripts

✨ **Web Check-in** (`checkin_web.py`)

- ✅ Daily check-in via web login (email/password)
- ✅ Login with `POST /api/login`
- ✅ Checks daily reward availability via `GET /api/checkDailyRewardAvailable`
- ✅ Auto-claims daily login XP via `POST /api/addDailyLoginXp`
- ✅ Displays profile info (name, level, XP, premium status)
- ✅ Multi-account parallel execution
- ✅ Proxy support

✨ **Telegram Check-in** (`checkin.py`)

- ✅ Daily bonus claim via Telegram Mini App
- ✅ Telegram auth with initData via `POST /api/auth/telegram`
- ✅ Checks daily bonus availability via `GET /api/bonus/daily`
- ✅ Auto-claims daily bonus (coins + XP) via `POST /api/bonus/daily/claim`
- ✅ Multi-account support
- ✅ Proxy support

✨ **Nova Boost** (`boost.py`)

- ✅ Activates Nova boost for 2x message multiplier
- ✅ Checks boost status via `GET /api/nova/boost/status`
- ✅ Auto-activates via `POST /api/nova/boost/activate`
- ✅ Displays remaining messages, multiplier, daily boost count
- ✅ Multi-account support
- ✅ Proxy support

✨ **Nova Chat FXP Farm** (`chat.py`)

- ✅ Sends messages to Nova AI for FXP rewards
- ✅ Auto-chat via `POST /api/nova/message`
- ✅ Respects daily chat limit (`dailyChatLimit`)
- ✅ Random message selection from predefined list
- ✅ Displays FXP earned per message and total balance
- ✅ Multi-account parallel execution with configurable delay
- ✅ Proxy support

✨ **Web Chat XP Farm** (`chat_web.py`)

- ✅ Sends Gemini search queries via web login
- ✅ Chat via `POST /api/gemini-search` with multipart form data
- ✅ Fetches profile data before and after for XP tracking
- ✅ Multi-account support
- ✅ Proxy support

✨ **Quests** (`quests.py`)

- ✅ Lists all available quests (Social, Daily, Growth)
- ✅ Displays quest progress, rewards, and status
- ✅ Starts social quests (Telegram join, X follow) via `POST /api/quests/{id}/start`
- ✅ Verifies social quests completion via `POST /api/quests/{key}/verify`
- ✅ Claims completed quest rewards via `POST /api/quests/{id}/claim`
- ✅ Only processes quests with ACTIVE or COMPLETED status
- ✅ Multi-account support
- ✅ Proxy support

---

## 🛠️ Prerequisites

Before running the scripts, ensure you have the following installed:

- **Python 3.8+**
- **pip** (Python package manager)
- **Dependencies**: Install via `pip install aiohttp aiohttp-socks colorama inquirer`
- **accounts.txt**: Add Telegram initData query strings (one per line) for Telegram scripts
- **email.txt**: Add email accounts (email|password per line) for web scripts
- **proxies.txt** (optional): Add proxy addresses for network requests

---

## 📦 Installation

1. **Clone or download this repository:**
   ```sh
   git clone https://github.com/thog9/Fintoq-ai.git
   cd Fintoq-ai
   ```

2. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Prepare Input Files:**

   Create `accounts.txt` for Telegram scripts (initData from DevTools — one per line):
   ```
   query_id=AAFFr-s9AAAAA...
   query_id=AAFFr-s9AAAAA...
   ```

   Create `email.txt` for web scripts (email|password — one per line):
   ```
   email1@gmail.com|password1
   email2@gmail.com|password2
   ```

   Create `proxies.txt` (optional) — one proxy per line:
   ```
   http://user:pass@ip:port
   socks5://user:pass@ip:port
   ip:port:user:pass
   ```

4. **Run:**
   ```sh
   python main.py
   ```
   - Choose a language (Vietnamese / English).
   - Select the script you want to run.

**Language Selection:**
- Choose between Vietnamese (Tiếng Việt) and English.
- All scripts support bilingual output.

---

## 📁 Project Structure

```
Fintoq-ai/
├── main.py                 # Central menu system
├── accounts.txt            # Telegram initData
├── email.txt               # Email accounts for web login
├── proxies.txt             # Proxies (optional)
├── README.md               # This file
└── scripts/                # Individual scripts
    ├── checkin_web.py      # Web daily check-in
    ├── checkin.py          # Telegram daily check-in
    ├── boost.py            # Nova boost activator
    ├── chat.py             # Telegram Nova chat FXP farm
    ├── chat_web.py         # Web Gemini chat XP farm
    └── quests.py           # Quest listing & claiming
```

---

## 📨 Contact

Connect with us for support or updates:

- **Telegram**: [thog099](https://t.me/thog099)
- **Channel**: [CHANNEL](https://t.me/thogairdrops)
- **Group**: [GROUP CHAT](https://t.me/thogchats)
- **X**: [Thog](https://x.com/thog099)

---

## ☕ Support Us

Love these scripts? Fuel our work with a coffee!

🔗 BUYMECAFE: [BUY ME CAFE](https://buymecafe.vercel.app/)

🔗 WEBSITE: [BUY SCRIPTS](https://thogtoolhub.com/)
