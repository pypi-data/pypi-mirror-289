from time import time
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name='abstract_apis',
    version='0.0.0.2',
    author='putkoff',
    author_email='partners@abstractendeavors.com',
    description="`abstract_apis` is a Python module designed to streamline HTTP request operations by abstracting away common setup procedures and processing details. It provides tools for constructing URLs and handling JSON data serialization automatically, making it easier to integrate API calls in your applications.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.11',
      ],
    install_requires=['abstract_utilities','requests'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    # Add this line to include wheel format in your distribution
    setup_requires=['wheel'],
)
