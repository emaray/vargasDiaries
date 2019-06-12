###Use this script for Diaries 1

import re
import unidecode

fileName = input('Enter the name of the file.')
pageNumber = int(input('Which page does the text begin on? If there are two page numbers, enter the diary page number.'))

with open('%s.txt' %(fileName), 'r', encoding='UTF-8') as diaryBook:
	diaryText = diaryBook.read()
	diaryText = re.sub("’","'",diaryText)

##This works!
def splitPages(pageNumber):	
	with open('%s.txt' %(fileName), 'r', encoding='UTF-8') as diaryBook:
		diaryText = diaryBook.read()
		diaryPageList = re.split('-\d+-', diaryText)
		for page in diaryPageList:
			page = unidecode.unidecode(page)
			with open('%s.txt' %(pageNumber), 'w', encoding='UTF-8') as diaryPage:
				diaryPage.write(page)
			with open('%s_plainText.txt' %(fileName), 'a', encoding='UTF-8') as plainText:
				justDiaryText = re.sub('________________','',page)
				justDiaryText = re.sub('[A-z]{5}\s{1}[A-z]{4}:{1}','',justDiaryText)
				justDiaryText = re.sub('[A-Z]{1}[A-z]{3}\:.*','',justDiaryText)
				justDiaryText = re.sub('Location:','',justDiaryText)
				justDiaryText = re.sub('\[Date\]','',justDiaryText)
				justDiaryText = re.sub('\[Date Unknown\]','',justDiaryText)
				justDiaryText = re.sub('\[unknown\]','',justDiaryText)
				justDiaryText = re.sub('\({1}break\){1}','',justDiaryText)
				justDiaryText = re.sub('\(cont\.{0,1}\)','',justDiaryText)
				justDiaryText = re.sub('\*.+http.+','',justDiaryText)
				justDiaryText = re.sub('[A-z].+http.+','',justDiaryText)
				plainText.write(justDiaryText)
				with open('%s_%s_plainText.txt' %(fileName,pageNumber),'w', encoding='UTF-8') as diaryPage_plain:
					diaryPage_plain.write(justDiaryText)
			pageNumber+=1

splitPages(pageNumber)
