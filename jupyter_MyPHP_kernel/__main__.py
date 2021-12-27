from ipykernel.kernelapp import IPKernelApp
from .kernel import MyPHPKernel
IPKernelApp.launch_instance(kernel_class=MyPHPKernel)
