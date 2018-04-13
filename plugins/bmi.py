async def bmi(bot, msg):
    print('GET /bmi')
	lst = msg['text'].split()[1:]
	lst = person(lst[0], lst[1]).convert()
	bmi = bmi_object(lst[0], lst[1]).calc_bmi()
	await bot.sendMessage(msg['chat']['id'], bmi)

class person:
	weight = height = 0
	def __init__(self, arg_1, arg_2):
		arg_1 = self.arg_1
		arg_2 = self.arg_2

	def convert(self):
		for i in [arg_1, arg_2]:
			if 'kg' in i:
				weight = i
			elif 'jin' in i:
				weight = i
			elif 'cm' in i:
				height = i
			elif 'm' in i and 'c' not in i:
				height = i
			else:
				return
		return [weight, height]

class bmi_object:
	def __init__(self, weight, height):
		weight = self.weight
		height = self.height

	def calc_bmi(self):
		if 'm' in height and 'c' not in height and 'kg' in weight:
			weight = float(weight.replace("kg", ""))
			height = float(height.replace("m", ""))
			return "%.1f" % (weight / height ** 2)
		else:
			if 'cm' in height:
				height = float(height.replace('cm', '')) / 100
			if 'jin' in weight:
				weight = float(weight.replace('jin', '')) / 2
			calc_bmi()
		


