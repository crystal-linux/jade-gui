pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
functionsdir = join_paths(pkgdatadir, 'jade_gui/functions')

jade_gui_sources = [
    '__init__.py',
    'keyboard_screen.py',
    'timezone_screen.py',
    'user_screen.py',
    'desktop_screen.py',
    'misc_screen.py',
    'partition_screen.py',
    'summary_screen.py',
    'install_screen.py',
    'finished_screen.py',
]
install_data(jade_gui_sources, install_dir: functionsdir)