pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
utilsdir = join_paths(pkgdatadir, 'jade_gui/utils')

jade_gui_sources = [
    '__init__.py',
    'disks.py',
    'threading.py',
]
install_data(jade_gui_sources, install_dir: utilsdir)