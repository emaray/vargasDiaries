import re
import csv
import unidecode

fileName = input('Enter the name of the file.')
pageNumber = int(input('Which page does the text begin on? If there are two page numbers, enter the diary page number.'))
with open('%s_test.csv' %(fileName),'a',encoding='UTF-8',newline = '') as diary:
	fieldnames = ['pageNum','date','tags','links','text']
	writer = csv.DictWriter(diary, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writeheader()

	with open('%s.txt' %(fileName), 'r', encoding='UTF-8') as diaryBook:
		diaryText = diaryBook.read()
		diaryText = re.sub("’","'",diaryText)

		##This doesn't work at all v
		diaryPageList = re.split('.{1}(?=Entry)', diaryText)

		# for page in diaryPageList:
		# 	page = str(page)
		# 	page = unidecode.unidecode(page)
		# 	pageNum = pageNumber
		# 	date = re.findall('^\d{1,2}/\d{1,2}/\d{2,4}$',page, re.MULTILINE)
		# 	if len(date) >= 1:
		# 		date = date[0]
		# 	elif len(date) == 0:
		# 		date = "undated"
		# 	tags = re.findall('^[A-Z]{1}[A-z]{3}:.*$',page, re.MULTILINE)
		# 	links = re.findall('[A-z].+http.+',page)
		# 	if links == []:
		# 		links = ''
		# 	justDiaryText = re.sub('________________','',page)

		# 	justDiaryText = re.sub('[A-z]{5}\s{1}[A-z]{4}:{1}','',justDiaryText)

		# 	justDiaryText = re.sub('[A-Z]{1}[A-z]{3}\:.*','',justDiaryText)

		# 	justDiaryText = re.sub('Location:','',justDiaryText)

		# 	justDiaryText = re.sub('\[Date\]','',justDiaryText)

		# 	justDiaryText = re.sub('\[Date Unknown\]','',justDiaryText)

		# 	justDiaryText = re.sub('\[unknown\]','',justDiaryText)
		# 	justDiaryText = re.sub('\({1}break\){1}','',justDiaryText)
		# 	justDiaryText = re.sub('\(cont\.{0,1}\)','',justDiaryText)
		# 	justDiaryText = re.sub('\*.+http.+','',justDiaryText)
		# 	justDiaryText = re.sub('[A-z].+http.+','',justDiaryText)
		# 	justDiaryText = re.sub('\n{2,}','',justDiaryText)
		# 	justDiaryText = re.sub('^\n','',justDiaryText,re.MULTILINE)

		# 	writer.writerow({'pageNum':pageNum,'date':date,'tags':tags,'links':links,'text':justDiaryText})

		# 	pageNumber += 1
		# 	# writer.writerow({'pageNum':pageNum,'date':date,'tags':tags,'text':text})


