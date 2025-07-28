# 8BDSS.spec

block_cipher = None

a = Analysis(
    ['8BDSS.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['pygame.joystick', 'pygame.event', 'pygame.display'],
    hookspath=[],
    runtime_hooks=[],
    excludes=['pygame.mixer', 'pygame.font', 'pygame.image', 'pygame.movie'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='8BDSS',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='8BDSS',
)
