from setuptools import setup, find_packages

setup(
    name="Brunfelsia_australis",  # パッケージ名
    version="0.1.0",  # バージョン番号
    author="Kanon Inuta",  # あなたの名前（著者名）
    author_email="kanoninuta@gmail.com",  # あなたのメールアドレス
    description="A package to find the closest day based on RGB values",  # パッケージの簡単な説明
    long_description=open('README.md').read(),  # README.mdから詳細な説明を読み込む
    long_description_content_type='text/markdown',  # README.mdの内容がMarkdown形式であることを指定
    # url="https://github.com/yourusername/Brunfelsia_australis",  # パッケージのURL（GitHubリポジトリなど）
    packages=find_packages(),  # パッケージに含めるモジュールを自動的に探す
    classifiers=[
        "Programming Language :: Python :: 3",  # Python 3.x向け
        "License :: OSI Approved :: MIT License",  # 使用するライセンス
        "Operating System :: OS Independent",  # OSに依存しないことを指定
    ],
    python_requires='>=3.6',  # このパッケージが対応するPythonのバージョン
    install_requires=[
        "numpy"  # このパッケージが依存するパッケージ（例: numpy）
    ],
)
