# "Снятие защиты листа в документах Microsoft Excel" v1.1 (18.12.2019)
# Yun Sergey
# wot@yun.kz

import os
import shutil
import tempfile
import zipfile


# FUNCTIONS

def checkFileExtension(fileName, importPath, exportPath, NotXLSX=None):
    if not fileName.endswith('.xlsx'):  # Если файл не Excel переместить его в Export без обработки
        NotXLSX = True  # Не файл Excel"
        print(f'> {fileName} не является файлом Microsoft Excel и был перемещен без обработки.')
        if os.path.exists(exportPath):  # Удалить файл в export если он уже имеется
            os.remove(exportPath)
        os.rename(importPath, exportPath)
    else:
        print(f'> {fileName} документ Microsoft Excel, обработка начата.')
    return NotXLSX


def unpackFile(fileName, importPath):  # Распаковка файла .xlsx в временную папку
    extFile = zipfile.ZipFile(importPath)
    extFile.extractall(tempDir)  # распаковка во временную папку
    extFile.close()  # закрытие архива
    return


def checkSheetProtection(docName):
    tempPatch = tempDir + '\\xl\worksheets\\'
    getListFiles = set(os.listdir(tempPatch))

    for xmlFileName in getListFiles:
        if not xmlFileName.endswith('.xml'):
            print(xmlFileName, 'не xml файл, обработка пропущена')
            continue

        fo = open(tempPatch + xmlFileName, 'r+')
        file = fo.read()

        if '<sheetProtection' in file:
            statusText = 'защищен паролем (!)'
            startStr = file.find('<sheetProtection')  # Начало нужного тега
            endStr = file.find('/><', startStr) + 2  # +2 символа "/>"
            texts = file[:startStr] + file[endStr:]  # Собираем новый файл: текст "до тега" + текст "после тега"
            fo = open(tempPatch + xmlFileName, 'w')  # Перезапись исходного файла пустым
            fo.write(texts)  # Запись значений
        else:
            statusText = 'не защищен паролем'
        print(f'\tстраница {xmlFileName} {statusText}')
    return


def packFile(fileName, exportPath):
    if os.path.exists(exportPath):  # Удалить файл в export если он уже имеется
        os.remove(exportPath)

    shutil.make_archive(fileName, 'zip', tempDir)
    os.rename(os.getcwd() + '\\' + fileName + '.zip', exportPath)
    print(f'> Файл {fileName} обработан')
    return


# GLOBAL VARIABLES

importDirectory = os.getcwd() + '\\import\\'
exportDirectory = os.getcwd() + '\\export\\'

# PROGRAM

getListFiles = (os.listdir(importDirectory))  # Получение полного списка файлов в директории

print('Список файлов:', getListFiles) if getListFiles else print('Папка import не содержит файлов.')

for fileName in getListFiles:

    importPath = importDirectory + fileName  # Полный путь файла в папке import
    exportPath = exportDirectory + fileName  # Полный путь файла в папке export

    if checkFileExtension(fileName, importPath, exportPath): continue  # Если не файл xlsx, перемещение и переход к новому файлу

    with tempfile.TemporaryDirectory(dir=os.getcwd()) as tempDir:  # Создание временной директории

        unpackFile(fileName, importPath)  # Распаковка .xlsx файла во временный каталог

        checkSheetProtection(fileName)  # Проверка защиты листа и удаление тэга защиты

        packFile(fileName, exportPath)  # Упаковка .xlsx файла и перемещение в export

    os.remove(importPath)  # Удаление оригинального файла из import, после успешного выполнения операций

print('Выполнение программы завершенно, все файлы перемещены в папку', exportDirectory)
