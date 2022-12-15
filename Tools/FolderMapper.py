import os
import pandas as pd
import PySimpleGUI as sg
import glob


def FolderMapper(folders_to_look):
    # path = "N:\Images\Mamon\Bol\DbRef\Bol_1"
    # folder_name = root[root.rfind("\\"):]
    folder_name = "test"

    file_list = []
    for root in folders_to_look:
        for path, subdirs, files in os.walk(root):
            print(path)
            if ("N:\Images\Eli.Zick" in path) or ("\cdr" in path) or ("N:\Images\Dudi\BackUp_DEEP" in path) or ("N:\Images\IP\OcrDataSet" in path) or ("N:\Images\Moving" in path) or ("N:\Images\QA\Paravision" in path):
                continue
            else:
                for name in files:
                    if ("_photo" in name) or ("_thumbnail" in name) or ("_fullHD" in name) or ("PhotoOfHolder" in name) or ("SignatureOfHolder" in name) or ("_supp." in name) or ("PhotoForFaceComparison" in name):
                        continue
                    elif (".png" in name) or (".jpg" in name) or (".jpeg" in name) or (".pdf" in name):
                        print(os.path.join(path, name))
                        file_list.append(os.path.join(path, name))

                    # if ".png" in name:
                    #     print(os.path.join(path, name))
                    #     file_list.append(os.path.join(path, name))
                    # if ".jpg" in name:
                    #     print(os.path.join(path, name))
                    #     file_list.append(os.path.join(path, name))
                    # if ".jpeg" in name:
                    #     print(os.path.join(path, name))
                    #     file_list.append(os.path.join(path, name))
                    # if ".pdf" in name:
                    #     print(os.path.join(path, name))
                    #     file_list.append(os.path.join(path, name))

    with open("N:\Images\Shahaf\Tools\pythonProject\Mapper" + "/" + folder_name + ".txt", 'w') as fp:
        for item in file_list:
            # write each item on a new line
            # fp.write(item + "\n")
            try:
                fp.write("%s\n" % item)
            except:
                fp.write("%s\n" % item.encode('utf-8').decode('ascii', 'ignore'))

        print('Done')


folders_to_look = ["N:\Images\Shahaf"]

FolderMapper(folders_to_look)
