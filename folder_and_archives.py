#Projects
p = []
with open('projects.txt', 'r') as f: 
    p = f.read()
p = [re.sub(r'"','',i) for i in p.split('\n')]
p = [i for i in p if i not in [1,2,3,4,5, -1] and i not in ["1",'2','3','4','5','-1','-2'] ]


def project(p, text):
    '''function returns project, if it written in text'''
    for i in p: 
        if i in text:
            return i

folder_FOR_translate(PATH)

for i in os.walk(PATH): 
    for ii in i[2]: 
        if DetermineFormat(ii) == 'zip': 
            extractZIP(i[0]+'//'+ii, i[0])

# for i in os.walk(PATH): 
#     for ii in i[2]: 
#         if DetermineFormat(ii) == 'rar':
#             print(ii, i[0])
#             #patoolib.extract_archive(i[0]+'//'+ii, i[0], outdir=".")
