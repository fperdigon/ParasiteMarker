#########################################################################################
# Copyright (c) 2017 Francisco Perdigon Romero
# Authors: Francisco Perdigon Romero
# email: 'fperdigon88@gmail.com'
# About the license: see the file LICENSE.TXT
#########################################################################################

__author__ = 'Francisco Perdigon Romero'
__email__ = 'fperdigon88@gmail.com'

import os
import csv
import time

# Marks
Trophozoite = []
Amoeboid = []
Schizonts = []
Gametocyte = []
Other_Forms = []
Undefined = []

# Estatus Vars
ActImagesFolder = ''
ActImageName = ''
ActImageNumber = 0
ImagesList = []
AnnotationFolder = 'ImageAnnotation'
ExportFolder = 'ExportedImages'
CountFolder = 'CountFolder'
ActImageModifiedMarks = False
CSVMarkList = []

LogFolder = 'ImageLog'
UserNameTypeList = []
ActUserNameType = []


def GetBMPImagesInFolder(Path):
    """Esta funcao gera uma lista das images no folder"""
    global ImagesList
    global CSVMarkList
    global AnnotationFolder
    ImagesList = []
    CSVMarkList = []

    for file in os.listdir(Path):
        if file[-3:] == 'bmp' or file[-3:] == 'BMP':
            ImagesList.append(Path + '/' +file)
            CSVMarkList.append(Path + '/' + AnnotationFolder + '/' + file[:-3] + 'csv')

    ImagesList.sort()
    CSVMarkList.sort()
    print('ImagesList')
    print(ImagesList)
    print('CSVList')
    print(CSVMarkList)
    return ImagesList


def CSVMarkRead(CSVFile):
    """Esta funcao lee as marcas guardadas no arquivo associado a imagem"""
    global Trophozoite
    global Amoeboid
    global Schizonts
    global Gametocyte
    global Other_Forms
    global Undefined

    Trophozoite = []
    Amoeboid = []
    Schizonts = []
    Gametocyte = []
    Other_Forms = []
    Undefined = []

    if os.path.exists(ActImagesFolder + '/' + AnnotationFolder) == False:
        os.mkdir(ActImagesFolder + '/' + AnnotationFolder)

    if os.path.isfile(CSVFile) == True:
        with open(CSVFile, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 't':
                    Trophozoite.append([row[0], int(row[1]), int(row[2])])

                if row[0] == 'a':
                    Amoeboid.append([row[0], int(row[1]), int(row[2])])

                if row[0] == 's':
                    Schizonts.append([row[0], int(row[1]), int(row[2])])

                if row[0] == 'g':
                    Gametocyte.append([row[0], int(row[1]), int(row[2])])

                if row[0] == 'of':
                    Other_Forms.append([row[0], int(row[1]), int(row[2])])

                if row[0] == 'u':
                    Undefined.append([row[0],int(row[1]),int(row[2])])

    print('Variaveis recuperadas de CSV')
    print(Trophozoite)
    print(Amoeboid)
    print(Undefined)

def CSVMarkWrite(CSVFile):
    """Esta funcao guarda as marcas guardadas no arquivo associado a imagem"""
    global Trophozoite
    global Amoeboid
    global Schizonts
    global Gametocyte
    global Other_Forms
    global Undefined
    
    with open(CSVFile, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(Trophozoite)
        writer.writerows(Amoeboid)
        writer.writerows(Schizonts)
        writer.writerows(Gametocyte)
        writer.writerows(Other_Forms)
        writer.writerows(Undefined)
    Trophozoite = []
    Amoeboid = []
    Schizonts = []
    Gametocyte = []
    Other_Forms = []
    Undefined = []
    print('Variaveis guardadas em CSV')

def CSVLogRead(CSVFile):
    """Esta funcao lee o Log da imagem"""
    global UserNameTypeList

    UserNameTypeList = []

    if os.path.exists(ActImagesFolder + '/' + LogFolder) == False:
        os.mkdir(ActImagesFolder + '/' + LogFolder)

    if os.path.isfile(CSVFile) == True:
        with open(CSVFile, 'rb') as f:
            reader = csv.reader(f)
            for row in reader:
                UserNameTypeList.append([row[0], row[1], row[2]])

    print('Log recuperado')
    print(UserNameTypeList)

def CSVLogWrite(CSVFile):
    """Esta funcao guarda os usuarios que marcaram a imagem"""
    global UserNameTypeList
    global ActUserNameType
    UserNameTypeList.append([ActUserNameType[0][0], ActUserNameType[0][1], time.strftime("%c")])
    print(UserNameTypeList)

    with open(CSVFile, 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(UserNameTypeList)
    UserNameTypeList = []
    print('Log guardado')
