<<<<<<< HEAD
# from Tools import Duplicator
# from Tools import ExcelCells2Files
# from Tools import FileList
# from Tools import FolderMapper
# from Tools import IDnJsonResults2Excel
# from Tools import Jsons2Excel
# from Tools import NameScrambler
# from Tools import NameSwitcher
# from Tools import PDF2JPG
# from Tools import PickleDictSearch
# from Tools import POAnJsonResults2Excel

import eel

from past.builtins import execfile

eel.init('web')


@eel.expose
def Duplicator_script():
    # execfile('Tools/Duplicator.py')
    from Tools import Duplicator
=======
import subprocess
import eel

from Tools.DoubleDisplay import ToolRun_DoubleDisplay
from Tools.Duplicator import ToolRun_Duplicator
from Tools.PDF2JPG import ToolRun_PDF2JPG


eel.init('web')

@eel.expose
def Duplicator_script():
    # from Tools import Duplicator
    ToolRun_Duplicator()
>>>>>>> 84b359e (Initial commit)


@eel.expose
def ExcelCells2Files_script():
<<<<<<< HEAD
    # execfile('Tools/ExcelCells2Files.py')
=======
>>>>>>> 84b359e (Initial commit)
    from Tools import ExcelCells2Files


@eel.expose
def FileList_script():
<<<<<<< HEAD
    # execfile('Tools/FileList.py')
=======
>>>>>>> 84b359e (Initial commit)
    from Tools import FileList

@eel.expose
def IDnJsonResults2Excel_script():
<<<<<<< HEAD
    # execfile('Tools/IDnJsonResults2Excel.py')
=======
>>>>>>> 84b359e (Initial commit)
    from Tools import IDnJsonResults2Excel

@eel.expose
def Jsons2Excel_script():
<<<<<<< HEAD
    # execfile('Tools/Jsons2Excel.py')
=======
>>>>>>> 84b359e (Initial commit)
    from Tools import Jsons2Excel

@eel.expose
def NameScrambler_script():
<<<<<<< HEAD
    # execfile('Tools/NameScrambler.py')
=======
>>>>>>> 84b359e (Initial commit)
    from Tools import NameScrambler

@eel.expose
def NameSwitcher_script():
<<<<<<< HEAD
    # execfile('Tools/NameSwitcher.py')
=======
>>>>>>> 84b359e (Initial commit)
    from Tools import NameSwitcher

@eel.expose
def PDF2JPG_script():
<<<<<<< HEAD
    # execfile('Tools/PDF2JPG.py')
    from Tools import PDF2JPG

@eel.expose
def PickleDictSearch_script():
    # execfile('Tools/PickleDictSearch.py')
=======
    from Tools import PDF2JPG
    ToolRun_PDF2JPG()

@eel.expose
def PickleDictSearch_script():
>>>>>>> 84b359e (Initial commit)
    from Tools import PickleDictSearch

@eel.expose
def POAnJsonResults2Excel_script():
<<<<<<< HEAD
    # execfile('Tools/POAnJsonResults2Excel.py')
=======
>>>>>>> 84b359e (Initial commit)
    from Tools import POAnJsonResults2Excel

@eel.expose
def SendMail_script():
<<<<<<< HEAD
    # execfile('Tools/SendMail.py')
    from Tools import SendMail

eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')
eel.start('index.html', size=(710, 900), position=(50, 50), app_mode=True)
=======
    from Tools import SendMail

@eel.expose
def JsonAge2Excel_script():
    from Tools import JsonAge2Excel

@eel.expose
def JsonFaceLiveness2Excel_script():
    from Tools import JsonFaceLiveness2Excel

@eel.expose
def DoubleDisplay_script():
    # from Tools import DoubleDisplay
    ToolRun_DoubleDisplay()

@eel.expose
def ImageCollector_script():
    subprocess.call([r"N:\Images\Nadav\scripts\imgcl 13.06.21\ImageCollector.exe"])

@eel.expose
def FileScrambler_script():
    subprocess.call([r"N:\Images\Nadav\scripts\FileScrambler\FileScrambler.exe"])

@eel.expose
def FormatClientDemoExcel_script():
    subprocess.call([r"N:\Images\Nadav\scripts\FormatClientDemoExcel\PowershellInvoke.exe"])

@eel.expose
def FilesToSubDirectories_script():
    subprocess.call([r"N:\Images\Nadav\scripts\FilesToSubDirectories\FilesToSubDirectories.exe"])


try:
    import pyi_splash
    pyi_splash.update_text('UI Loaded ...')
    pyi_splash.close()
except:
    pass

eel.browsers.set_path('electron', 'node_modules/electron/dist/electron')
eel.start('index.html', size=(950, 900), position=(50, 50), app_mode=True)

# python -m eel QCToolBox.spec web --onedir --noconsole -n=QCToolBox --icon="N:\Images\Shahaf\Tools\QCToolBox\web\assets\tabicon.png" --splash="N:\Images\Shahaf\Tools\QCToolBox\web\assets\loadingicon2.png" --hidden-import=pyi_splash
# N:\Images\Shahaf\Tools\QCToolBox\venv\python\Scripts\python.exe -m eel main.py web --onedir --noconsole -n=QCToolBox --icon="N:\Images\Shahaf\Tools\QCToolBox\web\assets\tabicon.png" --splash="N:\Images\Shahaf\Tools\QCToolBox\web\assets\loadingicon2.png" --hidden-import=pyi_splash
# pyi-makespec -m eel main.py web --onedir --noconsole -n=QCToolBox --icon="N:\Images\Shahaf\Tools\QCToolBox\web\assets\tabicon.png" --splash="N:\Images\Shahaf\Tools\QCToolBox\web\assets\loadingicon2.png" --hidden-import=pyi_splash


# N:\Images\Shahaf\Tools\QCToolBox\venv\python3-11\Scripts\python.exe -m eel main.py web --onedir --noconsole -n=QCToolBox --icon="N:\Images\Shahaf\Tools\QCToolBox\web\assets\tabicon.png" --splash="N:\Images\Shahaf\Tools\QCToolBox\web\assets\loadingicon2.png" --hidden-import=pyi_splash

# N:\Images\Shahaf\Tools\QCToolBox\venv\python3-11\Scripts\pyinstaller.exe -m eel main.py web --onedir --noconsole -n=QCToolBox --icon="N:\Images\Shahaf\Tools\QCToolBox\web\assets\tabicon.png" --splash="N:\Images\Shahaf\Tools\QCToolBox\web\assets\loadingicon2.png" --hidden-import=pyi_splash

>>>>>>> 84b359e (Initial commit)
