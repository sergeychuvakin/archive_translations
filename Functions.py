def languages_intext(text):
    '''
    Function requires polyglot.detect.Detector class
    '''
    l = []
    langs = []
    try:
        d = Detector(text, quiet=True)    
        for i in d.languages:
            l.append((i.confidence, i.name))
        for ii in l:
            if ii[0] > 20.:
                langs.append(ii[1])
        return langs
    except Exception as e: 
        print('Detector error: ', e)
        return ['Unknown']

def findTags_intext(text, tags): 
    '''
    Function returns the first match of tags in doc. Tags should be dict. 
    '''
    tags_indoc = []
    for i in re.split(' ', text[:1700].replace('\n',' ').lower()):
        for ii in tags: 
            for iii in tags[ii]:
                if iii in i: 
                    tags_indoc.append(ii)
    try:
        return tags_indoc[:2]
    except: 
        return []


# Функция, определяющяя формат документа
def DetermineFormat(filename):
    name, ext = os.path.splitext(filename)
    format_doc = ext[1:]
    return format_doc

# Функция, определяющяя дату создания документа
def DateOfCreation(filename):
    ut = os.path.getctime(filename)
    t = datetime.utcfromtimestamp(ut).strftime('%Y-%m-%d')
    return t 

# Функция, определяющяя дату изменения документа
def DateOfModification(filename):
    ut = os.path.getmtime(filename)
    t = datetime.utcfromtimestamp(ut).strftime('%Y-%m-%d')
    return t 

def LanguagesFromNames(name_file):
    langs = {'английский': '_eng',
            'русский': '_rus' 
           }
    lan = []
    for i in re.split(' ', name_file.replace('\n',' ').lower()):
        for name, lang in langs.items():
            if lang in i: 
                lan.append(name)
    return lan

def TagsInNames(name_file, tags):
    tags_i = []
    for i in re.split(' ', name_file.lower()):
        for name, tag in tags.items():
            for ii in tag:
                if ii in i: 
                    tags_i.append(name)
    return tags_i 


def Author(fullpath, start_folder): 
    '''
    start_folder - where all authors folders are. 
    '''
    return re.findall(r'({}\/(\w*))'.format(start_folder), fullpath)[0][1]


# ищем исходник это или перевод, в имени или в пути. 
def orign(name): 
    o_t = {'исходник': 'исходн','перевод': 'перев'}
    for i in o_t: 
        if o_t[i] in name.lower():
            return i
    else: 
        return ''

# def original_translating_from_path(file_path):
#     o_t = {'исходник': 'исходн','перевод': 'перев'}
#     orig_trans = []
#     for i in re.split(' ', file_path.lower()):
#         for name, or_tr in o_t.items():
#             if or_tr in i:
#                 orig_trans.append(name)
#     return orig_trans

def original_translating_from_path(file_path):
    for i in re.split('/', file_path.lower()):
        if 'исходн' in i:
            return 'исходник'
        elif 'перев' in i:
            return 'перевод'
#############RENAME_FOLDERS##############
def folder_FOR_translate(initial_path):
    '''
    This procedure changes all names of folders, that can be misunderstood by algorithm
    '''
    for i in os.walk(initial_path):
        for ii in i[1]:
            if 'для перев' in ii.lower(): 
                os.rename(i[0]+'\\'+ii, i[0]+'\\'+'исходник')



###############ZIP##############

def extractZIP(fullpath, dest): 
    with ZipFile(fullpath, 'r') as zip: 
    #zip.printdir() 
        zip.extractall(dest) 
