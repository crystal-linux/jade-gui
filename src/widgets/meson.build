pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
widgetsdir = join_paths(pkgdatadir, 'jade_gui/widgets')

jade_gui_sources = [
    '__init__.py',
    'timezone.py',
    'layout.py',
    'variant.py',
    'desktop.py',
    'disk.py'
]
install_data(jade_gui_sources, install_dir: widgetsdir)