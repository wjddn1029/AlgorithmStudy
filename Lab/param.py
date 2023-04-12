import datetime, json
from urllib import parse


today = datetime.date.today()
dir = '/Users/parkdohyun/Documents/Douzone/Wehago/SS/Print/WehagoPrint/{0}.log'.format(today)

testFile = open(dir, 'rt', encoding='cp949')
fileLines = testFile.readlines()

param, data = '', ''
for line in fileLines:
    line = line.replace('\n','')
    if 'Params' in line:
        param = line
        if 'Data' in line:
            data = line

testFile.close()
strings = param.split(':')
strings2 = data.split(': ')
json_data = json.loads(strings2[-1])
print(json_data['List'][0]['0']['API'])
fin = parse.unquote(strings[-1].replace(" ",'').replace("=", ':').replace('&','\n').replace('%2C', ',').replace('?','\n'))
print(fin)




