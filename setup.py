from setuptools import setup

APP=["main.py"]
OPTIONS= {
    'iconfile':'ytdl.icns',
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
