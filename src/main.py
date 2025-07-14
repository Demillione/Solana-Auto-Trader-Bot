from bot.scanner import get_new_tokens
from bot.narrative_check import ask_gpt_about_token
from bot.trade import buy_token, sell_token
from bot.telegram_bot import send_telegram_alert
from bot.logger import log_to_sheet

def main():
    tokens = get_new_tokens()
    for token in tokens:
        sentiment = ask_gpt_about_token(token['symbol'])
        if "trending" in sentiment or "influencer" in sentiment:
            tx = buy_token(token['address'], token['symbol'])
            send_telegram_alert(f"✅ Bought {token['symbol']} at {token['address']}\nTX: {tx}")
            log_to_sheet(token['symbol'], 'BUY', tx)

            # Simulated auto-sell
            tx_sell = sell_token(token['address'], token['symbol'])
            send_telegram_alert(f"💸 Sold {token['symbol']} at 2x\nTX: {tx_sell}")
            log_to_sheet(token['symbol'], 'SELL', tx_sell)
        else:
            send_telegram_alert(f"⚠️ Skipped {token['symbol']} – weak sentiment.\n{sentiment}")

if __name__ == "__main__":
    main()
