from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = '7076940632:AAGrWEQ_x5ZY7YQt9t11H2cVqYM1-mnfag0'
GAME_URL = 'tg://resolve?domain=cryptocookietapbot&post=cryptocookietap'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    game_description = """
    🪙 *Tap to earn*
    Tap the screen and collect coins.

    ⛏ *Mine*
    Upgrade cards that will give you passive income opportunities.

    ⏰ *Profit per hour*
    The exchange will work for you on its own, even when you are not in the game for 3 hours.
    Then you need to log in to the game again.

    📈 *LVL*
    The more coins you have on your balance, the higher the level of your exchange is and the faster you can earn more coins.

    👥 *Friends*
    Invite your friends and you’ll get bonuses. Help a friend move to the next leagues and you'll get even more bonuses.

    🌕 *Token listing*
    At the end of the season, a token will be released and distributed among the players.
    Dates will be announced in our announcement channel. Stay tuned!
    """

    keyboard = [
        [InlineKeyboardButton("Play", url=GAME_URL)],
        [InlineKeyboardButton("Play in 1 click", url=GAME_URL)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        game_description,
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=reply_markup
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()

