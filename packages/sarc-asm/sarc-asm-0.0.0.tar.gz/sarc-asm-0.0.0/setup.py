# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sarcasm_prior_publication']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'sarc-asm',
    'version': '0.0.0',
    'description': 'Sarcomere Analysis Multitool for structural and functional analysis of sarcomeres in microscopy images and movies',
    'long_description': '![SarcAsM logo](./docs/images/logo.png)\n\n## Overview\n\nSarcAsM (Sarcomere Analysis Multitool) is a Python package designed for comprehensive analysis of sarcomere structure and function in microscopy images and movies. This tool aims to provide researchers and clinicians with advanced capabilities for studying muscle biology and related disorders.\n\n## Features (coming soon)\n\n- Automated detection and analysis of Z-bands, sarcomeres, myofibrils, and sarcomere domains\n- Tracking and analysis of sarcomere motion, both individually and on average\n- Machine learning-based unbiased structural assessment\n- Compatible with various cardiomyocyte models, including human iPSC-derived cardiomyocytes\n- Available as both a Python package and a stand-alone application\n\n## Installation\n\n`pip install SarcAsM`\n\n## Usage\n\nDetailed usage instructions and documentation will be available upon full release of the package.\n\n## Development Status\n\nSarcAsM is currently under active development. The full source code and comprehensive documentation will be made available here upon publication of our research.\n\n## Citation\n\nIf you use SarcAsM in your research, please cite our upcoming paper (details to be provided upon publication).\n\n## Contact\n\nFor inquiries about SarcAsM, please contact:\n\nDaniel Haertter - daniel.haertter@med.uni-goettingen.de\n\n## License\n\nLicense information will be provided upon release.\n\n---\n\n© 2024 Institute of Pharmacology and Toxicology, University Medical Center Göttingen, Germany. All rights reserved.\n',
    'author': 'Daniel Haertter',
    'author_email': 'dani.hae@posteo.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/danihae/SarcAsM',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
