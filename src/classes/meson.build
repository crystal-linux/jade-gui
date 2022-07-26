pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
classesdir = join_paths(pkgdatadir, 'jade_gui/classes')

jade_gui_sources = [
    '__init__.py',
    'locale.py',
    'keymap.py',
    'install_prefs.py',
]
install_data(jade_gui_sources, install_dir: classesdir)