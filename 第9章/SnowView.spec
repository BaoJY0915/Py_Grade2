# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['D:\\包驾驭\\考级考证\\计算机二级\\python二级\\2-行文代码\\第9章\\SnowView.py'],
             pathex=['D:\\包驾驭\\考级考证\\计算机二级\\python二级\\2-行文代码\\第9章'],
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='SnowView',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='snowflake.ico')
