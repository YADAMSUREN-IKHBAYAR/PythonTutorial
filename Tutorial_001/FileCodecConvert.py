import os
import sys
import chardet
import csv

filePathSrc=r"ХавтасныЗам"
charencConverted = ''
LogWriteFileName = u'ЛогБичихФайлынНэр.CSV'
with open(LogWriteFileName,'w',newline='')as f:
    FieldNames =[u'FilePath','FileName','FileCodec','ReadTheUnicodeFileCodec','ConvertFileCodecToUnicode']
    thewriter=csv.DictWriter(f,fieldnames=FieldNames)
    thewriter.writeheader()

    for root, dirs, files in os.walk(filePathSrc):
        for fn in files:
            if fn[-3:] == '.vb' or fn[-6:] == '.myapp' or fn[-7:] == '.config' or fn[-7:] == '.vbproj' or fn[-5:] == '.resX':
                fName = root + "\\" + fn
                rawdata = open(fName, 'rb').read()
                result = chardet.detect(rawdata)
                charenc = result['encoding']

                if charenc == 'GB2312' or charenc == 'Windows-1254' or charenc == 'ascii' :
                    charencConverted = 'cp932'
                else:
                    charencConverted = result['encoding']

                with open(fName, 'r', encoding=charencConverted, errors='surrogateescape') as f:
                    data = f.read()
                with open(fName, 'w', encoding="UTF-8-SIG", errors="surrogateescape") as f:
                    f.write(data)
                    
                thewriter.writerow({'FilePath': root, 'FileName': fn,'FileCodec': charenc, 'ReadTheUnicodeFileCodec': charencConverted,'ConvertFileCodecToUnicode': 'UTF-8-SIG'})

print('амжилттай дууслаа')