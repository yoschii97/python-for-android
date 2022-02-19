from pythonforandroid.recipe import PythonRecipe
from pythonforandroid.toolchain import shprint, current_directory, info
from os.path import exists, join, dirname
import sh
import glob

class RandomXpy(PythonRecipe):

    name = 'RandomXpy'
    version = '0.0.1'
    url = 'https://github.com/yoschii97/RandomXpy/raw/master/archive/RandomXpy_{version}.zip'

    depends = ['python3','setuptools','distutils']

    patches = ['Ignore_CMAKE_SIZEOF_VOID_IO.patch']

    # To activate setuptools
    call_hostpython_via_targetpython = False;

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        # Manipulate the env here if you want
        env['CFLAGS'] += ' -no-integrated-as'
        env['CFLAGS'] += ' -no-integrated-as'
        env['CXXFLAGS'] += ' -std=c++17'
        return env

    def build_arch(self, arch):
        super().build_arch(arch)
        self.install_python_package(arch)

    def install_python_package(self,arch):
        env = self.get_recipe_env(arch)

        info('RandomXpy(Recipe): get_recipe_env was called.')
        info('RandomXpy(Recipe): Enviorement /env/ is {}'.format(env))

        with current_directory(self.get_build_dir(arch.arch)):
            info('hostpython location {}'.format(self.hostpython_location))
            hostpython = sh.Command(self.hostpython_location)
            shprint(hostpython, 'setup.py', 'build', _env=env)

recipe = RandomXpy()
