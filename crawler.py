import os
from enum import Enum
__author__ = 'Chase'

pxtPath = 'C:/Users/Chase/Desktop/Arcade/pxt-arcade/libs/base'

def crawl(path, count):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith("shims.d.ts"):
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



def parse(path):

    typeOfDoc = DocType.UNDEFINED
    target = Target.UNDEFINED

    description = ""
    functionName = ""
    with open(path, 'r') as f:
        for line in f:
            if typeOfDoc == DocType.NAMESPACE:
                if target == Target.DESCRIPTION_BEGIN:
                    if '/**' in line:
                        target = Target.DESCRIPTION_END
                elif target == Target.DESCRIPTION_END:
                    if '*/' in line:
                        target = Target.NAME
                    else:
                        description += line[line.find('*') + 2:]
                elif target == Target.NAME:
                    if '//' not in line:
                        functionName = line[(line.find('function') + len('function')):(line.find(';'))]
                        target = Target.DESCRIPTION_BEGIN
                        print("\t" + functionName)
                        print(description)
                        description = ""

            elif typeOfDoc == DocType.INTERFACE:
                if target == Target.DESCRIPTION_BEGIN:
                    if '/**' in line:
                        target = Target.DESCRIPTION_END
                elif target == Target.DESCRIPTION_END:
                    if '*/' in line:
                        target = Target.NAME
                    else:
                        description += line[line.find('*') + 2:]
                elif target == Target.NAME:
                    if '//' not in line:
                        functionName = line #line[0:(line.find(';'))]
                        target = Target.DESCRIPTION_BEGIN
                        print("\t" + functionName)
                        print(description)
                        description = ""

            if '{' in line :
                if 'namespace' in line:
                    name = line[(line.find('namespace') + len('namespace')):(line.find('}') - 2)].strip()
                    print('namespace\t'  + name + '\t\t\t' + path)
                    typeOfDoc = DocType.NAMESPACE
                    target = Target.DESCRIPTION_BEGIN
                elif 'interface' in line:
                    name = line[(line.find('interface') + len('interface')):(line.find('}') - 2)].strip()
                    print('interface\t'  + name + '\t\t\t' + path)
                    typeOfDoc = DocType.INTERFACE
                    target = Target.DESCRIPTION_BEGIN
                elif 'enum' in line:
                    name = line[(line.find('enum') + len('enum')):(line.find('}') - 2)].strip()
                    print('enum\t\t'  + name + '\t\t\t' + path)
                else:
                    print(path)

            if '}' in line :
                typeOfDoc = DocType.UNDEFINED
                target = Target.UNDEFINED


crawl(pxtPath, 0)

