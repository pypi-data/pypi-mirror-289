from setuptools import setup

setup(name='references_finder',
      version='0.3.7',
      description='Looking for similar words in Bible. Third Edition. This edition adds ancient Greek texts to the search programme. Подпункт, где убрали обязательное задание образа при создание объекта Obraz',
      packages=['references_finder'],
      author_email='vl.sergiiy@gmail.com',
      install_requires=[
        #   'transformers', 'python-docx'
      ],
      zip_safe=False,
      include_package_data=True,)

