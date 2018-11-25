import sublime, sublime_plugin

class InsertIncludeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
    	contents=self.view.substr(sublime.Region(0, self.view.size()))
    	indexOfLastInclude = contents.rfind('#include')
    	indexOfNewlineFollowingLastInclude = contents.find('\n', indexOfLastInclude) + 1
    	highlightedText = self.view.substr(self.view.sel()[0])
    	textToBeInsterted = ''
    	# Qt classes do not need the .h
    	if highlightedText[0] == 'Q': 
    		textToBeInsterted = '#include <' + highlightedText + '>\n'
    	else:
    		textToBeInsterted = '#include <' + highlightedText + '.h>\n'
    	self.view.insert(edit, indexOfNewlineFollowingLastInclude, textToBeInsterted)

class InsertForwardDeclareCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        contents=self.view.substr(sublime.Region(0, self.view.size()))
        indexOfLastInclude = contents.rfind('#include')
        indexOfNewlineFollowingLastInclude = contents.find('\n', indexOfLastInclude) + 1
        highlightedText = self.view.substr(self.view.sel()[0])
        textToBeInsterted = ''
        textToBeInsterted = 'class ' + highlightedText + ';\n'
        self.view.insert(edit, indexOfNewlineFollowingLastInclude, textToBeInsterted)