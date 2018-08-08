from opencc import OpenCC

'''
! pip install opencc-python-reimplemented

s2t: Simplified Chinese to Traditional Chinese
s2tw: Simplified Chinese to Traditional Chinese (Taiwan standard)
s2twp: Simplified Chinese to Traditional Chinese (Taiwan standard, with phrases)

t2s: Traditional Chinese to Simplified Chinese
t2tw: Traditional Chinese to Traditional Chinese (Taiwan standard)

tw2s: Traditional Chinese (Taiwan standard) to Simplified Chinese
tw2sp: Traditional Chinese (Taiwan standard) to Simplified Chinese (with phrases)
'''

cc = OpenCC('t2s')  
text = '這是一個繁中句子'
converted = cc.convert(text)