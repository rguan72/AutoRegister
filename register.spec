# -*- mode: python -*-

block_cipher = None

binary_files = [('./chromedrivers/chromedriver_linux', './selenium/webdriver'),
                ('./chromedrivers/chromedriver_mac', './selenium/webdriver'),
                ('./chromedrivers/chromedriver.exe', './selenium/webdriver')]
a = Analysis(['register.py'],
             pathex=['/home/richard/projects/auto_register'],
             binaries=binary_files,
             datas=[('./cookies/filler.txt', './cookies')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='register',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='register')
