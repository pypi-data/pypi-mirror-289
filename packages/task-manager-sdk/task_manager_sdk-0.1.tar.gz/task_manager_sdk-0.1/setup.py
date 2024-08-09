from setuptools import setup, find_packages

setup(
    name='task_manager_sdk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    tests_require=[
        'unittest',
    ],
    description='Un SDK para interactuar con la API TaskManager',
    long_description=open('README.md').read(),
    author='Tu Nombre',
    author_email='tuemail@example.com',
    url='https://github.com/tuusuario/task_manager_sdk',
)
