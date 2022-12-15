import os
import pickle
import PySimpleGUI as sg

def PickleDictSearch(mapfile, searchs, output):
    folder_name = mapfile[mapfile.rfind("/"):]

    def pickleLoader(mapfile):
        with open(mapfile, 'rb') as handle:
            data = pickle.load(handle)
        return data

    data_dict = pickleLoader(mapfile)

    def FileSearcher(data_dict, searchs_list, output, file_suffix):
        result_found_path = []
        result_found_path_short = []
        result_notfound = []
        result_found = []
        print(searchs_list)
        print(data_dict)

        for search_line in searchs_list:
            search_item = search_line
            if "\n" in search_item:
                search_item = search_line[:-1]
            if "-" in search_item:
                search_item = search_item.replace("-", "")
            else:
                search_item = search_item
            print("Searching- " + search_item)
            if search_item in data_dict:

                result_found_path.append(str(data_dict[search_item]))
                result_found_path_short.append(str(data_dict[search_item][0]))
                print(str(data_dict[search_item]))
                result_found.append(search_line)
            else:
                result_notfound.append(search_line)

        new_folder = file_suffix + "_Results"
        results = os.path.join(output + new_folder)
        os.mkdir(results)

        with open(results + "/" + file_suffix + "_Results_Found_Path_Short.txt", 'w') as fp:
            for item in result_found_path_short:
                try:
                    key_name = item[item.lower().find("_page") - 32:item.lower().find("_page")]
                    fp.write(key_name + ": " + item + "\n")
                except:
                    fp.write(item.encode('utf-8').decode('ascii', 'ignore'))

        with open(results + "/" + file_suffix + "_Results_Found.txt", 'w') as fp:
            for item in result_found:
                try:
                    fp.write(item)
                except:
                    fp.write(item.encode('utf-8').decode('ascii', 'ignore'))

        with open(results + "/" + file_suffix + "_Results_Found_Path.txt", 'w') as fp:
            for item in result_found_path:
                try:
                    fp.write(item + "\n")

                except:
                    fp.write(item.encode('utf-8').decode('ascii', 'ignore') + "\n")

        with open(results + "/" + file_suffix + "_Results_NotFound.txt", 'w') as fp:
            for item in result_notfound:
                try:
                    fp.write(item)
                except:
                    fp.write(item.encode('utf-8').decode('ascii', 'ignore'))

            print('Done')

    searches_list = open(searchs).readlines()

    FileSearcher(data_dict, searches_list, output, folder_name)

pickleDumpPath = "N:/Images/Shahaf/Tools/Tools4Work/Mapper/FullMap"
searchListFile = "N:/Images/Shahaf/Tools/Tools4Work/Mapper/alisa.txt"
outputFolder = "N:/Images/Shahaf/Tools/Tools4Work/Mapper"

PickleDictSearch(pickleDumpPath, searchListFile, outputFolder)
