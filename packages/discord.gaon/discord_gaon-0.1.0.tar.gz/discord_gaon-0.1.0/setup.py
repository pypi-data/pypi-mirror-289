from setuptools import setup, find_packages

setup(
    name="discord.gaon",  # 패키지 이름
    version="0.1.0",  # 패키지 버전
    author="gugaon0210",
    author_email="ngng01010@naver.com",
    description="Finally, the discord.gaon Python module is complete! Let's all try it together!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gugaon0210aa/discord.gaon",  # GitHub 저장소 URL
    packages=find_packages(),  # 패키지 자동 탐색
    install_requires=[
        "websockets>=10.0",
        "aiohttp>=3.8.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
