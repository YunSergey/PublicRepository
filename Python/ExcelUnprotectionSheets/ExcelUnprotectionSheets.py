# "Снятие защиты листа в документах Microsoft Excel" v1.1 (18.12.2019)
# Yun Sergey
# wot@yun.kz

import os
import shutil
import tempfile
import zipfile


# FUNCTIONS

def checkFileExtension(file_name: str, import_path: str, export_path: str, NotXLSX=None):
    """ Проверка расширения файла.
        Если не xlsx - переместить в export без обработки(перезаписать если имеется).
        Если xlsx - вернуть признак NotXLSX == False."""

    if not file_name.endswith('.xlsx'):
        NotXLSX = True
        print(f'> {file_name} не является файлом Microsoft Excel и был перемещен без обработки.')
        if os.path.exists(export_path):
            os.remove(export_path)
        os.rename(import_path, export_path)
    else:
        print(f'> {file_name} документ Microsoft Excel, обработка начата.')
    return NotXLSX


def unpackFile(import_path: str, temp_dir: str):  # Распаковка файла .xlsx во временную папку
    ''' Распаковка файла во временную папку'''
    with zipfile.ZipFile(import_path) as extFile:
        extFile.extractall(temp_dir)  # распаковка во временную папку
    return


def checkSheetProtection(temp_dir: str):
    """'Перебор файлов для поиска защищенных страниц xml с тегом защиты).
        В случае обнаружения защищенной страницы, поиск позиции: открытия тега, закрытия тега.
        Объединение содержимого файла до тега и после тега, запись нового файла"""

    tempPatch = temp_dir + '\\xl\worksheets\\'
    get_list_files = set(os.listdir(tempPatch))

    for xml_file_name in get_list_files:
        if not xml_file_name.endswith('.xml'):
            print(xml_file_name, 'не xml файл, обработка пропущена')
            continue

        fo = open(tempPatch + xml_file_name, 'r+')
        file = fo.read()

        if '<sheetProtection' in file:
            statusText = 'защищен паролем (!)'
            startStr = file.find('<sheetProtection')  # Начало нужного тега
            endStr = file.find('/><', startStr) + 2  # +2 символа "/>"
            texts = file[:startStr] + file[endStr:]  # Собираем новый файл: текст "до тега" + текст "после тега"
            fo = open(tempPatch + xml_file_name, 'w')  # Перезапись исходного файла пустым
            fo.write(texts)  # Запись значений
        else:
            statusText = 'не защищен паролем'
        print(f'\tстраница {xml_file_name} {statusText}')
    return


def packFile(file_name, export_path):
    '''Упаковка и смена расширения готового файла xlsx'''
    if os.path.exists(export_path):  # Удалить файл в export если он уже имеется
        os.remove(export_path)

    shutil.make_archive(file_name, 'zip', tempDir)
    os.rename(f'{os.getcwd()} \\{file_name}.zip', export_path)
    print(f'> Файл {file_name} обработан')
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

    if checkFileExtension(fileName, importPath,
                          exportPath): continue  # Если не файл xlsx, перемещение и переход к новому файлу

    with tempfile.TemporaryDirectory(dir=os.getcwd()) as tempDir:  # Создание временной директории

        unpackFile(importPath, tempDir)  # Распаковка .xlsx файла во временный каталог

        checkSheetProtection(tempDir, fileName)  # Проверка защиты листа и удаление тэга защиты

        packFile(fileName, exportPath)  # Упаковка .xlsx файла и перемещение в export

    os.remove(importPath)  # Удаление оригинального файла из import, после успешного выполнения операций

print('Выполнение программы завершенно, все файлы перемещены в папку', exportDirectory)
