import os
from enum import Enum
__author__ = 'Chase'

pxtPath = 'C:/Users/Chase/Desktop/Arcade/pxt-arcade/libs'
outputPath = 'Output'

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

interfaces = {}
namespaces = {}
enums = {}

def parse(path):


    typeOfDoc = DocType.UNDEFINED
    target = Target.UNDEFINED

    description = ""
    functionName = ""
    with open(path, 'r') as f:
        for line in f:
            if '{' in line :
                if 'namespace' in line:
                    name = line[(line.find('namespace') + len('namespace')):(line.find('{') - 1)].strip()
                    print('namespace\t'  + name + '\t\t\t' + path)
                    typeOfDoc = DocType.NAMESPACE
                    target = Target.DESCRIPTION_BEGIN
                elif 'interface' in line:
                    name = line[(line.find('interface') + len('interface')):(line.find('{') - 1)].strip()
                    if '<' in name:
                        name = name[:name.find('<')]
                    print('interface\t'  + name + '\t\t\t' + path)
                    typeOfDoc = DocType.INTERFACE
                    target = Target.DESCRIPTION_BEGIN
                elif 'enum' in line:
                    name = line[(line.find('enum') + len('enum')):(line.find('}') - 2)].strip()
                    print('enum\t\t'  + name + '\t\t\t' + path)
                    typeOfDoc = DocType.ENUM
                    target = Target.NAME
                else:
                    print(path)
                if '}' in line :
                    typeOfDoc = DocType.UNDEFINED
                    target = Target.UNDEFINED

            elif '}' in line :
                typeOfDoc = DocType.UNDEFINED
                target = Target.UNDEFINED

            elif typeOfDoc == DocType.NAMESPACE:
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
                        functionName = functionName.replace('\n', '').strip()
                        target = Target.DESCRIPTION_BEGIN
                        #print("\t" + functionName)
                        #print(description)
                        if name not in namespaces:
                            namespaces[name] = {}
                        namespaces[name][functionName] = description.replace('\n', '')


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
                        functionName = functionName.replace('\n', '').strip()
                        target = Target.DESCRIPTION_BEGIN
                        #print("\t" + functionName)
                        #print(description)

                        description = description.replace('\n', '')
                        if name not in interfaces:
                            interfaces[name] = {}
                        interfaces[name][functionName] = description
                        description = ""

            elif typeOfDoc == DocType.ENUM:
                if target == Target.NAME:
                    if '//' not in line:
                        valueName = line[0:line.find('=')].strip()
                        value = line[line.find('=') + 2:line.find(',')]
                        #print("\t" + valueName)
                        #print("\t" + value)
                        if name not in enums:
                            enums[name] = {}
                        enums[name][valueName] = value



crawl(pxtPath, 0)

print("Interfaces:")
for interface in interfaces:
    f = open('Output/Interfaces/' + interface + '.md','w+')
    f.write('# ' + interface + '\n\n')
    f.write('|Function Name| Description|\n')
    f.write('|:---|:---|\n')
    for functionName in interfaces[interface]:
        interfaces[interface][functionName].replace('\n', '')
        f.write('|' + functionName + ' |' + interfaces[interface][functionName] + '|\n')
        print(functionName)
        print(interfaces[interface][functionName])
    #print ('\t' + interface)

print("Namespaces:")
for namespace in namespaces:
    f = open('Output/Namespaces/' + namespace + '.md','w+')
    f.write('# ' + namespace + '\n\n')
    f.write('|Function Name| Description|\n')
    f.write('|:---|:---|\n')
    for functionName in namespaces[namespace]:
        namespaces[namespace][functionName].replace('\n', '')
        f.write('|' + functionName + ' |' + namespaces[namespace][functionName] + '|\n')
        print(functionName)
        print(namespaces[namespace][functionName])
    #print ('\t' + namespace)

print("Enums:")
for enum in enums:
    f = open('Output/Enums/' + enum + '.md','w+')
    f.write('# ' + enum + '\n\n')
    f.write('|Function Name| Description|\n')
    f.write('|:---|:---|\n')
    for functionName in enums[enum]:
        enums[enum][functionName].replace('\n', '')
        f.write('|' + functionName + ' |' + enums[enum][functionName] + '|\n')
        print(functionName)
        print(enums[enum][functionName])
    #print ('\t' + namespace)
