from setuptools import setup
from pathlib import Path

this_directory: Path = Path(__file__).parent
long_description: str = (this_directory / "README.md").read_text()

setup(
    name='autocode-py',
    version='0.0.1.post1',
    author='muazhari',
    url='https://github.com/muazhari/autocode',
    description='AutoCode: Automated Code Improvement by Metrics Optimization',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['autocode'],
    license='MIT',
    install_requires=[
        'pymoo',
        'pydantic_settings',
        'fastapi',
        'dependency-injector',
        'ray',
        'fastapi',
        'matplotlib<3.9.0',
        'sqlmodel',
        'dill',
        'streamlit',
        'numpy<2',
        'python-on-whales',
        'uvicorn',
        'langchain',
        'langchain-openai',
        'langgraph',
    ],
)
