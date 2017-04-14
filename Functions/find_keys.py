def find_keys(str, *keys) :
	indexList = []
	for key in keys:
		temp = str.find(key)
		if temp != -1 :
			indexList.append(temp)

	return indexList