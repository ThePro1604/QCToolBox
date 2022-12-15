
def MapperSearch(mapfile, searchs, mode, output):
    searchs_list = []
    mapfile_list = []
    folder_name = mapfile[mapfile.rfind("\\"):mapfile.rfind(".")]

    def FileSearcher(mapfile_list, searchs_list, output, folder_name):
        # folder_name = mapfile[mapfile.rfind("\\"):]
        result_found_path = []
        result_notfound = []
        result_found = []
        print(mapfile_list)
        print(searchs_list)
        found = False

        for search_line in searchs_list:
            search_item = search_line[:-2]
            if "-" in search_line:
                search_item = search_item.replace("-", "")
            else:
                search_item = search_item
            print("Searching- " + search_item)
            found = False
            for map_line in mapfile_list:
                if search_item in map_line:
                    result_found_path.append(map_line)
                    result_found.append(search_line)
                    print(map_line)
                    found = True
                    break
            if not found:
                result_notfound.append(search_line)

        with open(output + "/" + folder_name + "_Results_Found.txt", 'w') as fp:
            for item in result_found:
                # write each item on a new line
                # fp.write(item + "\n")
                try:
                    # fp.write("%s\n" % item)
                    fp.write(item)

                except:
                    # fp.write("%s\n" % item.encode('utf-8').decode('ascii', 'ignore'))
                    fp.write(item.encode('utf-8').decode('ascii', 'ignore'))


        with open(output + "/" + folder_name + "_Results_Found_Path.txt", 'w') as fp:
            for item in result_found_path:
                # write each item on a new line
                # fp.write(item + "\n")
                try:
                    # fp.write("%s\n" % item)
                    fp.write(item)

                except:
                    # fp.write("%s\n" % item.encode('utf-8').decode('ascii', 'ignore'))
                    fp.write(item.encode('utf-8').decode('ascii', 'ignore'))

        with open(output + "/" + folder_name + "_Results_NotFound.txt", 'w') as fp:
            for item in result_notfound:
                # write each item on a new line
                # fp.write(item + "\n")
                try:
                    # fp.write("%s\n" % item)
                    fp.write(item)
                except:
                    # fp.write("%s\n" % item.encode('utf-8').decode('ascii', 'ignore'))
                    fp.write(item.encode('utf-8').decode('ascii', 'ignore'))

            print('Done')

    # txt
    if mode:
        searchs_list = open(searchs).readlines()
        mapfile_list = open(mapfile).readlines()


    # TextBox
    if not mode:
        mapfile_list = open(mapfile).readline()
        searchs_list = searchs


    FileSearcher(mapfile_list, searchs_list, output, folder_name)

MapperSearch("N:\Images\Shahaf\Tools\pythonProject\Mapper\Images.txt",
             "N:\Images\Shahaf\Tools\pythonProject\Mapper/searchreal.txt",
             True,
             "N:\Images\Shahaf\Tools\pythonProject\Mapper")
