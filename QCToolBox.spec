# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('N:\\Images\\Shahaf\\Tools\\QCToolBox\\venv\\lib\\site-packages\\eel\\eel.js', 'eel'), ('web', 'web')],
<<<<<<< HEAD
    hiddenimports=['bottle_websocket'],
=======
    hiddenimports=['bottle_websocket', 'pyi_splash'],
>>>>>>> 84b359e (Initial commit)
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
<<<<<<< HEAD
=======
splash = Splash(
    'N:\\Images\\Shahaf\\Tools\\QCToolBox\\web\\assets\\loadingicon2.png',
    binaries=a.binaries,
    datas=a.datas,
    text_pos=None,
    text_size=12,
    minify_script=True,
    always_on_top=True,
)
>>>>>>> 84b359e (Initial commit)

exe = EXE(
    pyz,
    a.scripts,
<<<<<<< HEAD
=======
    splash,
>>>>>>> 84b359e (Initial commit)
    [],
    exclude_binaries=True,
    name='QCToolBox',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['N:\\Images\\Shahaf\\Tools\\QCToolBox\\web\\assets\\tabicon.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
<<<<<<< HEAD
=======
    splash.binaries,
>>>>>>> 84b359e (Initial commit)
    strip=False,
    upx=True,
    upx_exclude=[],
    name='QCToolBox',
)
