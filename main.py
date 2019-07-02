d = {
    'path':[],
    'name':[],
    'langs':[],
    'langs_name':[],
    'tag':[],
    'tag_name':[],
    'format':[],
    'C_date':[],
    'M_date':[],  
    'author':[],
    'project':[],
    'orign_path':[],
    #'orign_name':[]
    'orign':[]
    
}
c = 1
for i in os.walk(PATH): 
    for ii in i[2]:
        #if re.match(r'.*\.d', ii):
        d['path'].append(i[0]+'//'+ii)
        d['name'].append(ii)
        d['format'].append(DetermineFormat(ii))
        d['C_date'].append(DateOfCreation(i[0]+'//'+ii))
        d['M_date'].append(DateOfModification(i[0]+'//'+ii))
        if DetermineFormat(ii) == 'docx':
            try:
                t = textract.process(i[0]+'//'+ii).decode('utf-8')
                t = re.sub(r'\\x\w\w', ' ', t)
            except Exception as e:
                print(e)
                print(i[0]+'//'+ii)
                next
        elif DetermineFormat(ii) == 'doc':
            try: 
                t = textract.process(i[0]+'//'+ii).decode('utf-8')
            except Exception as e:
                print(e)
                print(i[0]+'//'+ii) 
                next 
        elif DetermineFormat(ii) == 'txt':
            with open(i[0]+'//'+ii, 'r') as f:
                t = f.read()
        elif DetermineFormat(ii) == 'pdf':
            try:
                t = textract.process(i[0]+'//'+ii).decode('utf-8')
            except Exception as e:
                print(e)
                print(i[0]+'//'+ii) 
                next
        d['project'].append(project(p,t))
        d['langs'].append(languages_intext(t))
        d['langs_name'].append(LanguagesFromNames(ii))
        d['tag_name'].append(TagsInNames(ii, tags))
        d['tag'].append(findTags_intext(t, tags))
        d['author'].append(Author(i[0]+'//'+ii, 'per'))
        d['orign_path'].append(original_translating_from_path(i[0]+'//'+ii)) 
        d['orign'].append(orign(ii))
        print(c)
        c+=1
        pd.DataFrame(d).to_excel('inter.xlsx')
            #d['orign_name'].append(key_words(tf, corpus))
            
            
            
#d['origin_name'] = origins_byName(d['name'])
pd.DataFrame(d).to_excel('second.xlsx')
print('Конец!')
