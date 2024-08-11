# setup.py

from setuptools import setup, find_packages

setup(
    name='SlickRecorder',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'SlickRecorder=SlickRecorder.main:main',
        ],
    },
        package_data={
        'SlickRecorder': ['*.png'],  # Include all .png files in the slickrecorder directory
    },
    install_requires=[
"SpeechRecognition",
"moviepy",
"pydub",
"numpy",
"pillow",
"opencv-python",
"pyautogui",
"pynput",
"screeninfo",
"pyaudio",
"PyQt5",
"noisereduce",
"scipy",
"pystray"

    ],
    description='A Slick screen recorder for linux! With some cool features :]',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/merwin-asm/SlickRecorder',
    author='Merwin M',
    license='MIT',
        include_package_data=True,  # Ensure that package_data is included

)

