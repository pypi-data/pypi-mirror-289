import re, collections

def get_sus(text: str):
    regex = re.compile(r'suspicious|sus|amongus|among|amogus|us', re.I)
    mo = regex.findall(text)
    named = collections.namedtuple('ඞ', ('sus_'+str(i) for i in range(len(mo))))
    return named(*mo)

def capitalize_sus(text: str) -> str:
    sus = ['suspicious', 'amongus', 'amogus', 'among', 'sus', 'us']
    for i in sus:
        text = text.replace(i, i.upper())
    return text

def is_sus(text: str) -> bool:
    regex = re.compile(r'suspicious|sus|amongus|among|amogus|us', re.I)
    return bool(regex.findall(text))

def susify(text: str) -> str:
    result = ''
    for i in text:
        if i != ' ' and i != '\n' and i != '\t':
            result += 'ඞ'
        else:
            result += i
    return result