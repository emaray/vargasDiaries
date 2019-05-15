import re
import csv
import unidecode

fileName = input('Enter the name of the file.')
pageNumber = int(input('Which page does the text begin on? If there are two page numbers, enter the diary page number.'))
with open('%s_test.csv' %(fileName),'a',encoding='UTF-8',newline = '') as diary:
	fieldnames = ['pageNum','date','tags','notes','links','text']
	writer = csv.DictWriter(diary, fieldnames=fieldnames, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	writer.writeheader()

	with open('%s.txt' %(fileName), 'r', encoding='UTF-8') as diaryBook:
		diaryText = diaryBook.read()
		diaryText = re.sub("’","'",diaryText)
		diaryText = re.sub('(.{1}cont.{2}\n+){1,2}(Entry\sDate.+\n+)Tags.+','',diaryText)

		try:
			diaryText = re.sub('cont.{1}\n+Entry\sDate.+\n+Tags.+','',diaryText)
		except:
			pass


		diaryPageList = re.split('Entry', diaryText)


		for page in diaryPageList:
			pageIndex = diaryPageList.index(page)
			if pageIndex == 0:
				pass
			else:
				page = str(page)
				page = unidecode.unidecode(page)
				pageNum = pageNumber
				# date = re.findall('^\d{1,2}/\d{1,2}/\d{2,4}$',page, re.MULTILINE)
				date = re.findall('Date.+', page)
				date = date[0]
				date = str(date)
				date = re.sub('Date :','',date)
				tags = re.findall('^[A-Z]{1}[A-z]{3}:.*$',page, re.MULTILINE)
				tags = str(tags)
				tags = re.sub('\[\'Tags: ','',tags)
				tags = re.sub('\[\"Tags: ','',tags)				
				tags = re.sub('\'\]','',tags)
				tags = re.sub('\"\]','',tags)
				links = re.findall('[A-z].+http.+',page)
				try:
					links = links[0]
				except IndexError:
					pass
				if links == []:
					links = ''
				notes = re.findall('^\*.+$',page,re.MULTILINE)
				if notes == []:
					notes = ''
				notes = str(notes)	
				notes = re.sub('\[\'','',notes)
				notes = re.sub('\[\"','',notes)
				notes = re.sub('\'\]','',notes)					
				notes = re.sub('\"\]','',notes)				
				justDiaryText = re.sub('________________','',page)

				justDiaryText = re.sub('[A-z]{5}\s{1}[A-z]{4}:{1}','',justDiaryText)

				justDiaryText = re.sub('[A-Z]{1}[A-z]{3}\:.*','',justDiaryText)

				justDiaryText = re.sub('Location:+','',justDiaryText)

				justDiaryText = re.sub('\*[A-z]{1}.+','',justDiaryText)

				justDiaryText = re.sub('\[Date\]','',justDiaryText)

				justDiaryText = re.sub('\[Date Unknown\]','',justDiaryText)

				justDiaryText = re.sub('\[unknown\]','',justDiaryText)
				justDiaryText = re.sub('\({1}break\){1}','',justDiaryText)
				justDiaryText = re.sub('\(cont\.{0,1}\)','',justDiaryText)
				justDiaryText = re.sub('\*.+http.+','',justDiaryText)
				justDiaryText = re.sub('[A-z].+http.+','',justDiaryText)
				justDiaryText = re.sub('\n{2,}','',justDiaryText)
				justDiaryText = re.sub('^\n','',justDiaryText,re.MULTILINE)


				writer.writerow({'pageNum':pageNum,'date':date,'tags':tags,'links':links,'notes':notes,'text':justDiaryText})
				# # # writer.writerow({'pageNum':pageNum,'date':date})			

				pageNumber += 1
			# # writer.writerow({'pageNum':pageNum,'date':date,'tags':tags,'text':text})


