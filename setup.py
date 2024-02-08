from setuptools import setup, find_packages

# Читаємо вміст файлу requirements.txt і використовуємо його для залежностей
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='PaLM_VertexAI_Project',
    version='0.1',
    packages=find_packages(),
    install_requires=required,  # Використовуємо залежності з requirements.txt
)