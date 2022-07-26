pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'jade_gui')
gnome = import('gnome')

blueprints = custom_target('blueprints',
  input: files(
    'gtk/help-overlay.blp',
    'window.blp',
    'widgets/timezone.blp',
    'widgets/layout.blp',
    'widgets/variant.blp',
    'widgets/desktop.blp',
    'widgets/disk.blp',
    'pages/keyboard_screen.blp',
    'pages/timezone_screen.blp',
    'pages/user_screen.blp',
    'pages/desktop_screen.blp',
    'pages/misc_screen.blp',
    'pages/partition_screen.blp',
    'pages/summary_screen.blp',
    'pages/install_screen.blp',
    'pages/finished_screen.blp',
  ),
  output: '.',
  command: [find_program('blueprint-compiler'), 'batch-compile', '@OUTPUT@', '@CURRENT_SOURCE_DIR@', '@INPUT@'],
)



gnome.compile_resources('jade_gui_resources',
  'resources.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)


gnome.compile_resources('jade_gui',
  'jade_gui.gresource.xml',
  dependencies: blueprints,
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'jade_gui.in',
  output: 'jade_gui',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

subdir('widgets')
subdir('functions')
subdir('classes')
subdir('locales')
subdir('utils')
subdir('scripts')

jade_gui_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'keymaps.py',
  'desktops.py',
]

install_data(jade_gui_sources, install_dir: moduledir)
