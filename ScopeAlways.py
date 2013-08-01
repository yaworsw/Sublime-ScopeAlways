import sublime, sublime_plugin

STATUS_FORMAT = '%s'

on       = False
settings = None

def plugin_loaded():
  update_settings()
  settings.add_on_change('extensions_path', update_settings)
  on = settings.get('start_on')

def update_settings():
  globals()['settings'] = sublime.load_settings('ScopeAlways.sublime-settings')

def show_scope(view, hide=False):
  key = settings.get('status_key', 'scope_always')
  if not hide:
    position = view.sel()[0].begin()
    scope    = view.scope_name(position)
    view.set_status(key, STATUS_FORMAT % scope)
  else:
    view.set_status(key, '')

class ScopeAlways(sublime_plugin.EventListener):

  def on_selection_modified(self, view):
    if on:
      show_scope(view)
    else:
      show_scope(view, hide=True)

class ToggleScopeAlways(sublime_plugin.WindowCommand):

  def run(self):
    global on
    on = not on
    show_scope(self.window.active_view(), hide=not on)
