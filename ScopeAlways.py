import sublime, sublime_plugin

status_format = '%s'
status_key    = 'scope_always'
on            = False

settings      = None

def plugin_loaded():
  """
  When the plugin is loaded then load the plugin's settings.
  """
  global settings
  update_settings()
  settings.add_on_change('extensions_path', update_settings)

def update_settings():
  """
  Updates the settings variable with the settings.
  """
  global settings
  settings = sublime.load_settings('ScopeAlways.sublime-settings')
  load_settings()

def load_setting(setting_key, var_name = None):
  """
  Load a setting defined by setting_key and put it into a global variable
  defined by var_name.  If var_name is not given then the global variable is
  assumed to share it's name with setting_key.
  """
  if var_name == None:
    var_name = setting_key
  globals()[var_name] = settings.get(setting_key, globals()[var_name])

def load_settings():
  """
  Load all of the settings associated with this package.
  """
  load_setting('status_format')
  load_setting('status_key')
  load_setting('start_on', 'on')

def show_scope(view):
  global on
  global status_format
  global status_key
  if on:
    position = view.sel()[0].begin()
    scope    = view.scope_name(position)
    view.set_status(status_key, status_format % scope)
  else:
    view.set_status(status_key, '')

class ScopeAlways(sublime_plugin.EventListener):

  def on_selection_modified(self, view):
    """
    Displays the current scope if the plugin is on or clears it if its off.
    """
    show_scope(view)

class ToggleScopeAlways(sublime_plugin.WindowCommand):

  def run(self):
    """
    This command toggles whether or not to show the scope in the status bar.
    """
    global on
    on = not on
    show_scope(self.window.active_view())

class CopyToClipboard(sublime_plugin.WindowCommand):

  def run(self):
    """
    This command copies the current scope to the clipboard
    """
    current_scope = self.window.active_view().get_status(status_key)
    if type(current_scope) is str:
      sublime.set_clipboard(current_scope.rstrip())