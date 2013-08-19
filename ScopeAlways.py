import sublime, sublime_plugin

STATUS_FORMAT = '%s'

on       = False
settings = None

def plugin_loaded():
  """
  When the plugin is loaded then load the plugin's settings.
  """
  update_settings()
  settings.add_on_change('extensions_path', update_settings)
  on = settings.get('start_on')

def update_settings():
  """
  Updates the settings variable with the settings.
  """
  global settings
  settings = sublime.load_settings('ScopeAlways.sublime-settings')

def show_scope(view, hide=False):
  """
  Display the current scope in the status bar.
  (or remove it if the plugin is currently off)
  """
  key = settings.get('status_key', 'scope_always')
  if not hide:
    position = view.sel()[0].begin()
    scope    = view.scope_name(position)
    view.set_status(key, STATUS_FORMAT % scope)
  else:
    view.set_status(key, '')

class ScopeAlways(sublime_plugin.EventListener):

  def on_selection_modified(self, view):
    """
    Triggered when the selector's position changes.
    """
    show_scope(view, hide=not on)

class ToggleScopeAlways(sublime_plugin.WindowCommand):

  def run(self):
    """
    This command toggles whether or not to show the scope in the status bar.
    """
    global on
    on = not on
    show_scope(self.window.active_view(), hide=not on)
