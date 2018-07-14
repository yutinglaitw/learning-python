'''
Check if the input is English by coding
'''
def is_english(text):
    return all(ord(c) < 128 for c in text)

'''
Check if the input is Chinese by coding
'''
def is_chinese(text):
    for c in text.encode().decode('utf-8'):
        if u'\u4e00' <= c <= u'\u9fff':
            return True
        return False

'''
Classify langeage of the input using langdetect (Google's library)
Faster but less accurate
'''
def classify_lang_langdetect(text):
    from langdetect import detect_langs
    
    # e.g. [cy:0.5714271709983919, it:0.42856972028922663]
    return detect_langs(text)

'''
Classify langeage of the input using langid
Higher accuracy, limited language set can be more accurate
'''
def classify_lang_langid(text):
    import langid
    # constrain the language set
    langid.set_languages(['en', 'zh', 'ru', 'ja', 'ko'])
    
    # e.g. ('zh', -19.244097471237183)
    return langid.classify(text)
    
