# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sathybrid']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.26.4,<2.0.0',
 'pandas>=2.1.4',
 'rasterio>=1.3.10',
 'requests>=2.32.3',
 'scikit-image>=0.23.2',
 'timm>=1.0.8',
 'torch>=2.3.1']

setup_kwargs = {
    'name': 'sathybrid',
    'version': '0.1.0',
    'description': 'A Python package to fusion LR and HR imagery',
    'long_description': '# sathybrid\nA Python package to fusion LR and HR imagery\n\n\n## Installation\n```bash\npip install sathybrid\n```\n\n## Usage\n\n```python\nimport sathybrid\nimport pathlib\n\n\n# Select the HR image\nPATH = pathlib.Path("/home/cesar/demo/NA5120_E1186N0724/")\nHRfile = PATH / "naip" / "m_3812243_nw_10_060_20220524.tif"\n\n# Find the most similar LR image\ndata_stats = sathybrid.utils.find_similar_lr(\n    hr_file=HRfile,\n    lr_folder=PATH / "s2",\n    hr_bands=[1, 2, 3],\n    hr_normalization=255,\n    lr_bands=[3, 2, 1],\n    lr_normalization=10_000,\n    downsampling_method="lanczos3",\n    method="fft_l1",\n)\n\n# Select the best LR image\nLRfile = PATH / "s2" / (data_stats.iloc[0]["lr_img"] + ".tif")\n\n# Define the output path\nOUTfile = PATH / "fusion.tif"\n\n# Fusion\nsathybrid.image_fusion(\n    hr_file=HRfile,\n    lr_file=LRfile,\n    output_file=OUTfile,\n    hr_bands=[1, 2, 3],\n    hr_normalization=255,\n    lr_bands=[3, 2, 1],\n    lr_normalization=10_000,\n    upsampling_method="lanczos3",\n    fourier=True,\n    fourier_params={"method": "ideal", "order": 6, "sharpness": 3},\n    scale_factor=8,\n    denoise=True,\n)    \n```',
    'author': 'Cesar Aybar',
    'author_email': 'fcesar.aybar@uv.es',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/csaybar/sathybrid',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
