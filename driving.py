# 輸入年齡 國家 再判斷可不可以開車
#新增美國 16歲就可以開車
age = input('請輸入年齡: ')
age = int(age)
nat = input('請輸入您的國家: ')
if nat == Taiwan:
	if age >= 18:
		print('你可以開車')
	else:
		print('你還不可以開車')
elif nat == America:
	if age >= 16:
		print('你可以開車')
	else:
		print('你還不可以開車')
