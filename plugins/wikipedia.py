import wikipedia
import shlex

async def wikipedia_summary(bot, msg):
    lst = shlex.split(msg['text'])[1:]
    inp = lst[0]
    lang = 'en'
    if len(lst) != 1
        lang = lst[1]
    result = wikipedia_logic(lang, inp)
    await bot.sendMessage(msg['chat']['id'], result)

# inp * input
async def wikipedia_logic(lang = 'en', inp)
    try:
        if lang == 'en':
            wikipedia.set_lang('en')
        else:
            wikipedia.set_lang(lang)
        url = wikipedia.page(msg).url
        msg = wikipedia.summary(msg)
        f = []
        for i in msg:
            if i != '\n':
                f.append(i)
            else:
                break
        msg = "".join(f)
        return msg + '\n' + url
    except:
        return "Not Found Page or LANG"