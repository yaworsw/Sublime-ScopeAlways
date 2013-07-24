import sublime, sublime_plugin

STATUS_FORMAT = '%s'

def init():
  settings.add_on_change('extensions_path', update_settings)
  update_settings()

def update_settings():
  self.settings = sublime.load_settings('ScopeAlways.sublime-settings')

class ScopeAlways(sublime_plugin.EventListener):

  def on_selection_modified(self, view):
    position = view.sel()[0].begin()
    scope    = view.scope_name(position)
    key      = self.settings.get('status_key', 'scope_always')
    view.set_status(key, STATUS_FORMAT % scope)

init()
