import sublime, sublime_plugin

settings = sublime.load_settings('ScopeAlways.sublime-settings')

class ScopeAlways(sublime_plugin.EventListener):

  def on_selection_modified(self, view):
    position = view.sel()[0].begin()
    scope    = view.scope_name(position)
    key      = settings.get('status_key', 'scope_always')
    format   = settings.get('status_format', '%s')
    view.set_status(key, format % scope)
