import wikipedia
import shlex

async def wikipedia_summary(bot, msg):
    lst = shlex.split(msg['text'])[1:]
    inp = lst[0]
    lang = 'en'
    if len(lst) != 1:
        lang = lst[1]
    result = wikipedia_logic(inp, lang)
    await bot.sendMessage(msg['chat']['id'], result)

# inp * input
def wikipedia_logic(inp, lang = 'en'):
    try:
        if lang == 'en':
            wikipedia.set_lang('en')
        else:
            wikipedia.set_lang(lang)
        url = wikipedia.page(inp).url
        text = wikipedia.summary(text)
        return msg + '\n' + url
    except:
        return "Not Found Page or LANG"
