from distutils import sysconfig as sc
print(sc.get_python_lib(prefix='', plat_specific=True))
