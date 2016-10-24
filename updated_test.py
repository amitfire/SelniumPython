def testingdict():
	final_dict = {}
	test = {'myname':'anshaj',
			'a':{
				'b':{'c':'1','d':'2'},
				'e':{'f':'3','g':'4'}}}


	for k in test.itervalues():
		a = test['a']
	for k in a.itervalues():
		val = a.values()
	for i in range(len(val)):
		final_dict.update(val[i])
	for k in test.iterkeys():
		test.update({'a':final_dict})

	print test


testingdict()
