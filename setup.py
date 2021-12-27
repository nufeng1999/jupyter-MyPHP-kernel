from setuptools import setup

setup(name='jupyter_MyPHP_kernel',
      version='0.0.1',
      description='Minimalistic PHP kernel for Jupyter',
      author='nufeng',
      author_email='18478162@qq.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      url='https://github.com/nufeng1999/jupyter-MyPHP-kernel/',
      download_url='https://github.com/nufeng1999/jupyter-MyPHP-kernel/tarball/0.0.1',
      packages=['jupyter_MyPHP_kernel'],
      scripts=['jupyter_MyPHP_kernel/install_MyPHP_kernel'],
      keywords=['jupyter', 'notebook', 'kernel', 'PHP','php'],
      include_package_data=True
      )
