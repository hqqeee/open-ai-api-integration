from setuptools import setup, find_packages

setup(
    name='openai_websocket_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'websockets',
        'openai',
    ],
    entry_points={
        'console_scripts': [
            'start-server=openai_websocket.server:main',  # Adjust if needed
        ],
    },
)

