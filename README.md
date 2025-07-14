# Solana Auto-Trader Bot V2

This bot trades new Solana tokens automatically based on volume, liquidity, and sentiment, with honeypot protection and auto-sell logic via Jupiter DEX. All trades are logged to Google Sheets and alerts are sent to Telegram.

## How to Deploy on Render.com

1. Unzip this project locally and upload the folder (as ZIP) to Render.
2. During Render setup:
   - Runtime: Python 3.10+
   - Start command: `python main.py`
3. Set all values from the `.env` file as Render environment variables.
4. Grant Sheets access by sharing your Google Sheet with the provided service account.

## Important Notes
- This bot operates on Solana **mainnet**.
- Never use a primary wallet. Use only a burner wallet with limited funds.
- Always test and monitor before scaling funds.