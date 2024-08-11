from setuptools import setup, find_packages

setup(
    name='DreamBoothFineTune',
    version='0.2.2',
    packages=find_packages(),
    install_requires=[
        "pillow~=10.4.0",
        "torchvision~=0.19.0",
        "diffusers~=0.30.0",
        "transformers~=4.44.0",
        "tqdm~=4.66.4",
        "datasets~=2.20.0",
        "bitsandbytes",
        "ftfy",
        "gradio",
        "tensorboard",
        "xformers~=0.0.27"
    ],
    extras_require={'cuda': ['torch==2.4.0+cu124', 'torchvision==0.19.0+cu124','torchaudio==2.4.0+cu124']},
    author='Alex',
    long_description=open('README.md').read(),
    long_description_content='text/markdown',
    url='https://github.com/skillfi/fine-tuning',
    classifiers=[],
    python_requires='>=3.8'
)
