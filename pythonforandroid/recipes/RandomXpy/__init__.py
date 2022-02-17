from pythonforandroid.recipe import CompiledComponentsPythonRecipe

class RandomXpy(CompiledComponentsPythonRecipe):

    name = 'RandomXpy'
    version = '0.0.1'
    url = 'https://github.com/yoschii97/RandomXpy/raw/master/archive/RandomXpy_{version}.zip'

    depends = ['python3','setuptools','distutils']
    call_hostpython_via_targetpython = False
    build_cmd = 'build'

recipe = RandomXpy()
