# Telegram Web App Local Server

Simple HTTP server for developing Telegram Web Apps locally.

## Quick Start

```bash
# Run the server
python server.py
```

Server starts on `http://localhost:8080` with CORS headers for Telegram WebApps.

## Expose via HTTPS (Required!)

Telegram WebApps **require HTTPS**. Use ngrok to expose your local server:

```bash
# Install ngrok: https://ngrok.com/download

# Expose local server
ngrok http 8080
```

Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`) for the next step.

## Register with BotFather

### Option A: Create a new Web App

1. Message [@BotFather](https://t.me/BotFather)
2. Send `/newapp` and follow prompts
3. Paste your ngrok HTTPS URL when asked

### Option B: Use Inline Button (Programmatic)

```python
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

web_app_url = "https://abc123.ngrok.io"  # Your ngrok URL

keyboard = [[
    InlineKeyboardButton(
        "Open Web App 🚀",
        web_app={"url": web_app_url}
    )
]]
reply_markup = InlineKeyboardMarkup(keyboard)

# Send message with Web App button
await update.message.reply_text("Click to open:", reply_markup=reply_markup)
```

## Add Menu Button

To add a persistent menu button that opens the Web App:

```python
from telegram import MenuButtonWebApp, WebAppInfo

# Set the menu button for your bot
await context.bot.set_chat_menu_button(
    menu_button=MenuButtonWebApp(
        text="Open App",
        web_app=WebAppInfo(url=web_app_url)
    )
)
```

Or use BotFather's `/setmenubutton` command.

## Project Structure

```
.
├── server.py       # HTTP server with CORS
├── README.md       # This file
└── index.html      # Your Web App (create this)
```

## Tips

- **Free ngrok**: URL changes every session — update BotFather each time
- **Static ngrok**: Use a paid plan or Cloudflare Tunnel for a fixed URL
- **Web App API**: Access Telegram features via `window.Telegram.WebApp`

## Resources

- [Telegram Web Apps Docs](https://core.telegram.org/bots/webapps)
- [Web App JS API](https://core.telegram.org/bots/webapps#initializing-mini-apps)
