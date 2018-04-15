async def bmi(bot, msg):
    print('GET /bmi')
    lst = msg['text'].split()[1:]
    lst = person(lst[0], lst[1]).convert()
    bmi = bmi_object(lst[0], lst[1]).calc_bmi()
    await bot.sendMessage(msg['chat']['id'], bmi)
class person:
    weight = height = 0
    def __init__(self, arg_1, arg_2):
        self.arg_1 = arg_1
        self.arg_2 = arg_2

    def convert(self):
        for i in [self.arg_1, self.arg_2]:
            if 'kg' in i:
                weight = i
            elif 'jin' in i:
                weight = i
            elif 'cm' in i:
                height = i
            elif 'm' in i and 'c' not in i:
                height = i
            else:
                pass
        return [weight, height]

class bmi_object:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
    
    def calc_bmi(self):
        if 'm' in self.height and 'c' not in self.height and 'kg' in self.weight:
            self.weight = float(self.weight.replace("kg", ""))
            self.height = float(self.height.replace("m", ""))
        else:
            if 'cm' in self.height:
                self.height = float(self.height.replace('cm', '')) / 100
            if 'jin' in self.weight:
                self.weight = float(self.weight.replace('jin', '')) / 2
            if type(self.weight) is str:
                self.weight = float(self.weight.replace("kg", ""))
            if type(self.height) is str:
                self.height = float(self.height.replace("m", ""))
        return "%.1f" % (self.weight / self.height ** 2)