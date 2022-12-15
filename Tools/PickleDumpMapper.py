import os
import pickle
import re
from collections import defaultdict


def ToolRun_PickleDumpMapper():
    def FolderMapper(folders_to_look, file_name):
        # folder_name = root[root.rfind("\\"):]
        # folder_name = "test"
        pattern = re.compile(r'^[A-Z\d]+$')
        exclude = {'BackUp_DEEP', 'Eli.Zick', 'OcrDataSet', 'Moving', 'Paravision', 'DeepTrainingData', '~snapshot'}

        data_dict = defaultdict(list)
        for root in folders_to_look:
            for path, subdirs, files in os.walk(root):
                subdirs[:] = [d for d in subdirs if d not in exclude]
                print(subdirs)
                #
                # print(subdirs)
                # if ("N:\Images\Eli.Zick" in path) or ("\cdr" in path) or ("N:\Images\Dudi\BackUp_DEEP" in path) or ("N:\Images\IP\OcrDataSet" in path) or ("N:\Images\Moving" in path) or ("N:\Images\QA\Paravision" in path) or ("N:\Images\Davidd\DeepTrainingData" in path):
                #     continue
                # else:
                print(path)
                for name in files:
                    if ("_photo" in name.lower()) or ("_thumbnail" in name.lower()) or ("_fullHD".lower() in name.lower()) or ("PhotoOfHolder".lower() in name.lower()) or ("SignatureOfHolder".lower() in name.lower()) or ("_supp." in name.lower()) or ("PhotoForFaceComparison" in name.lower()):
                        continue
                    elif ("page" in name.lower()) and ((".png" in name[name.rfind("."):]) or (".jpg" in name[name.rfind("."):]) or (".jpeg" in name[name.rfind("."):]) or (".pdf" in name[name.rfind("."):])):
                        # print(os.path.join(path, name))
                        key_name = name[name.lower().find("_page")-32:name.lower().find("_page")]
                        if re.match(pattern, key_name) and len(key_name) == 32:
                            print(key_name)
                            data_dict[key_name].append(os.path.join(path, name))

        try:
            geeky_file = open("N:\Images\Shahaf\Tools\Tools4Work\Mapper" + "/" + file_name, 'wb')
            pickle.dump(data_dict, geeky_file)
            geeky_file.close()
        except:
            print("Something went wrong")

        print('Done')


    folders_to_look = ["N:\\", "M:\\"]
    file_name = "FullMap"

    FolderMapper(folders_to_look, file_name)
