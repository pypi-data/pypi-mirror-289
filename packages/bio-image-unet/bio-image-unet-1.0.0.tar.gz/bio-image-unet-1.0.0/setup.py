# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bio_image_unet',
 'bio_image_unet.progress',
 'bio_image_unet.siam_unet',
 'bio_image_unet.siam_unet.helpers',
 'bio_image_unet.unet',
 'bio_image_unet.unet3d',
 'bio_image_unet.utils']

package_data = \
{'': ['*']}

install_requires = \
['albumentations>=1.3,<2.0',
 'napari>=0.4.18,<0.5.0',
 'numpy>=1.20,<2.0',
 'packaging',
 'scikit-image>0.18,<1.0',
 'tifffile',
 'torch>=2.0.0,<3.0.0',
 'tqdm>=4.61,<5.0']

setup_kwargs = {
    'name': 'bio-image-unet',
    'version': '1.0.0',
    'description': 'Implementations of U-Net, Siam U-Net and 3D U-Net for biological image segmentation',
    'long_description': '# Bio Image U-Net\n\nImplementations of U-Net, Siam U-Net and 3D U-Net for biological image segmentation\n\n\n## Installation\n### PyPI\n``pip install bio-image-unet``\n### GitHub\n``pip install git+https://github.com/danihae/bio-image-unet``\n\n## Usage example\nImport package with ``import bio_image_unet``\n\n[iPython Notebook for getting started with U-Net](https://github.com/danihae/bio-image-unet/blob/master/using_unet.ipynb) \\\n[iPython Notebook for getting started with Siam U-Net](https://github.com/danihae/bio-image-unet/blob/master/using_siam_unet.ipynb)\n',
    'author': 'Daniel Haertter',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/danihae/bio-image-unet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
