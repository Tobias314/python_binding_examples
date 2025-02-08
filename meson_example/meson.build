project(
    'meson_example',
    'cpp',
    version: '0.1.0',
    default_options: [
        'cpp_std=c++11',
    ],
)
py = import('python').find_installation(pure: false)
pybind11_dep = dependency('pybind11')
python_sources = ['src/meson_example/__init__.py']
py.install_sources(python_sources, subdir: 'meson_example')
py.extension_module('core',
    'src/core.cpp',
    install: true,
    dependencies : [pybind11_dep],
    subdir: 'meson_example',
)   