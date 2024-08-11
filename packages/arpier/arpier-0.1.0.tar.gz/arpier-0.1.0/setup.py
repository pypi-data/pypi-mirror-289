from setuptools import setup, find_packages

setup(
    name="arpier",  # Название пакета
    version="0.1.0",  # Версия
    packages=find_packages(),  # Автоматический поиск пакетов
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'arpier=arpier.run_arpier:run',  # Команда для запуска через терминал
        ],
    },
    author="BlackGonza",
    author_email="edgargevorgyan988@gmail.com",
    description="ARP Spoofing attack script",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BlackGonza/arpier",  # URL проекта
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Минимальная версия Python
)
