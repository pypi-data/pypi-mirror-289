from setuptools import setup

setup(
  name = 'DPConFil',
  packages = ['DPConFil'],
  version = '0.0.1',
  description = 'A collection of filament identification and analysis algorithms',
  author = ['Jiang Yu'],
  author_email = 'yujiang@pmo.ac.cn',
  url = 'https://github.com/JiangYuTS/DPConFil',
#   download_url = '',
  keywords = ['astrophysics', 'DPConFil', 'filaments'],
  classifiers = [],
  install_requires=[
      'numpy',
      'scipy',
      'matplotlib',
      'astropy',
      'scikit-learn',
      'scikit-image',
      'networkx',
      'pandas',
      'tqdm',
      'FacetClumps',
      'radfil',
      
  ]
)
