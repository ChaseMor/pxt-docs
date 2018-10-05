import os
from enum import Enum
__author__ = 'Chase'

pxtPath = 'C:/Users/Chase/Desktop/Arcade/pxt-arcade/libs'
outputPath = './output'

def crawl(path, count):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".d.ts"):
                #print(root + '/' + name)
                if "---" not in root:
                    parse(root + '/' + name)
        for name in dirs:
            crawl(path + '/' + name, count + 1)

class DocType(Enum):
    UNDEFINED = 0,
    INTERFACE = 1,
    NAMESPACE = 2,
    ENUM = 3

class Target(Enum):
    UNDEFINED = 0,
    DESCRIPTION_BEGIN = 1,
    DESCRIPTION_END = 2,
    NAME = 3


values = {
    DocType.INTERFACE: {},
    DocType.NAMESPACE: {},
    DocType.ENUM: {}
}

filetypes = {
    "interface" : DocType.INTERFACE,
    "namespace" : DocType.NAMESPACE,
    "enum" : DocType.ENUM
}

def parse(path):


    typeOfDoc = DocType.UNDEFINED
    target = Target.UNDEFINED

    description = ""
    functionName = ""
    with open(path, 'r') as f:
        for line in f:
            if '{' in line :
                for type in filetypes:
                    if type in line:
                        fileName = line[(line.find(type) + len(type)):(line.find('{') - 1)].strip()
                        if '<' in fileName:
                            fileName = fileName[:fileName.find('<')]
                        #print(type + '\t' + fileName + '\t\t\t' + path)
                        typeOfDoc = filetypes[type]
                        target = Target.NAME if typeOfDoc == DocType.ENUM else Target.DESCRIPTION_BEGIN

                if '}' in line :
                    typeOfDoc = DocType.UNDEFINED
                    target = Target.UNDEFINED

            elif '}' in line :
                typeOfDoc = DocType.UNDEFINED
                target = Target.UNDEFINED
            else:
                if '//' not in line and '@' not in line:
                    if target == Target.DESCRIPTION_BEGIN:
                        if '/**' in line:
                            target = Target.DESCRIPTION_END
                    elif target == Target.DESCRIPTION_END:
                        if '*/' in line:
                            target = Target.NAME
                        else:
                            description += ' ' + line[line.find('*') + 2:]
                    elif target == Target.NAME:

                            target = Target.DESCRIPTION_BEGIN

                            if typeOfDoc == DocType.INTERFACE:
                                functionName = line
                            elif typeOfDoc == DocType.NAMESPACE:
                                functionName = line[(line.find('function') + len('function')):(line.find(';'))]
                            elif typeOfDoc == DocType.ENUM:
                                functionName = line[0:line.find('=')].strip()
                                description = line[line.find('=') + 2:line.find(',')]
                                target = Target.NAME

                            functionName = functionName.replace('\n', '').strip()
                            #print("\t" + functionName)
                            #print(description)

                            if fileName not in values[typeOfDoc]:
                                values[typeOfDoc][fileName] = {}
                            values[typeOfDoc][fileName][functionName] = description.replace('\n', '')
                            description = ""




crawl(pxtPath, 0)

for type in filetypes:
    print(type)
    list = values[filetypes[type]]

    for file in list:
        f = open(outputPath + '/' + type + '/' + file + '.md','w+')
        f.write('# ' + file + '\n\n')
        f.write('|Function Name| Description|\n')
        f.write('|:---|:---|\n')
        for functionName in sorted(list[file]):
            list[file][functionName].replace('\n', '')
            f.write('|' + functionName + ' |' + list[file][functionName] + '|\n')
            #print(functionName)
            #print(list[file][functionName])
        #print ('\t' + interface)
