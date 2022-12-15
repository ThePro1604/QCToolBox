import subprocess
import eel
from Tools.DoubleDisplay import ToolRun_DoubleDisplay
from Tools.Duplicator import ToolRun_Duplicator
from Tools.ExcelCells2Files import ToolRun_ExcelCells2Files
from Tools.FileList import ToolRun_FileList
from Tools.IDnJsonResults2Excel import ToolRun_IDnJsonResults2Excel
from Tools.JsonAge2Excel import ToolRun_JsonAge2Excel
from Tools.JsonFaceLiveness2Excel import ToolRun_JsonFaceLiveness2Excel
from Tools.Jsons2Excel import ToolRun_Jason2Excel
from Tools.NameScrambler import ToolRun_scrambler
from Tools.NameSwitcher import ToolRun_NameSwitcher
from Tools.PDF2JPG import ToolRun_PDF2JPG
from Tools.POAnJsonResults2Excel import ToolRun_POAnJsonResults2Excel
from Tools.SendMail import ToolRun_SendMail

eel.init('web')


@eel.expose
def Duplicator_script():
    # from Tools import Duplicator
    ToolRun_Duplicator()


@eel.expose
def ExcelCells2Files_script():
    # from Tools import ExcelCells2Files
    ToolRun_ExcelCells2Files()


@eel.expose
def FileList_script():
    # from Tools import FileList
    ToolRun_FileList()


@eel.expose
def IDnJsonResults2Excel_script():
    # from Tools import IDnJsonResults2Excel
    ToolRun_IDnJsonResults2Excel()


@eel.expose
def Jsons2Excel_script():
    # from Tools import Jsons2Excel
    ToolRun_Jason2Excel()


@eel.expose
def NameScrambler_script():
    # from Tools import NameScrambler
    ToolRun_scrambler()


@eel.expose
def NameSwitcher_script():
    # from Tools import NameSwitcher
    ToolRun_NameSwitcher()


@eel.expose
def PDF2JPG_script():
    # from Tools import PDF2JPG
    ToolRun_PDF2JPG()


# @eel.expose
# def PickleDictSearch_script():
#     from Tools import PickleDictSearch

@eel.expose
def POAnJsonResults2Excel_script():
    # from Tools import POAnJsonResults2Excel
    ToolRun_POAnJsonResults2Excel()


@eel.expose
def SendMail_script():
    # from Tools import SendMail
    ToolRun_SendMail()


@eel.expose
def JsonAge2Excel_script():
    # from Tools import JsonAge2Excel
    ToolRun_JsonAge2Excel()


@eel.expose
def JsonFaceLiveness2Excel_script():
    # from Tools import JsonFaceLiveness2Excel
    ToolRun_JsonFaceLiveness2Excel()


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
