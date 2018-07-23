import re

'''
Common regex patterns
'''
class Regex():
    def __init__(self):
        pattern = {}
        pattern['email'] = r'\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*'
        pattern['ip'] = r'\d+\.\d+\.\d+\.\d+(:\d+)?'
        pattern['url'] = r'[a-zA-z]+://[^\s]*'
        pattern['html'] = r'<(.*)>.*<\/\1>|<(.*) \/>'
        pattern['id'] = r'[a-zA-Z][a-zA-Z0-9_]+'
        
        # Number
        pattern['int'] = r'-?[1-9]\d*'
        pattern['float'] = r'(-?\d+)(\.\d+)?'
        pattern['prob'] = r'\d+(\.\d+)?%'
        
        # Time
        pattern['date'] = '([12]\d{3}(-|/)(0?[1-9]|1[0-2])(-|/)(0?[1-9]|[12]\d|3[01]))' #2018-07-23
        pattern['time_24'] = '([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]'                  #23:59
        pattern['time_12'] = '(([01]?[0-9]):([0-5][0-9]) ?([AaPp]\.?[Mm]\.?))'          #2:30am
        
        self.pattern = pattern


if __name__ == '__main__':
    regex = Regex()
    print(re.sub(regex.pattern['html'], '', 'Hi<a>Test</a>'))
    
