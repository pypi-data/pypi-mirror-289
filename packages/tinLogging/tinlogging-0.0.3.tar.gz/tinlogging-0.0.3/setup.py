from setuptools import setup, find_packages


def readme():
    with open("README.md", "r") as f:
        return f.read()


setup(
    name="tinLogging",  # Имя
    version="0.0.3",  # Версия
    author="tinokil",  # Автор
    author_email="zemedeuk@gmail.com",  # Почта
    description="Python library for convenient and beautiful logging of information",  # Описание
    long_description=readme(),  # Файл README.md
    long_description_content_type="text/markdown",  # Тип текста в README.md
    url="https://github.com/Tinokil/tinLogging/",  # Ссылка на домашнюю страницу (github)
    packages=find_packages(),  # Пакеты
    install_requires=[],  # Зависимости
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Информация о пакете
    keywords=[
        "Logging",
        "tinLogging",
        "Logger",
        "tinLogger",
        "python logging",
    ],  # Ключевые слова
    project_urls={"Source Code": "https://github.com/Tinokil/tinLogging/blob/main/tinLogging/logging.py"},  # Допополнительные ссылки (документация и тд)
    python_requires=">=3.6",  # Минимальная версия python
    license="MIT"  # Лицензия
)
