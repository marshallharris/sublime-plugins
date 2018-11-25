#this plugin will open the unit test of the currently open file
#it will create a unit test if one does not exits in the same directory

import sublime
import sublime_plugin
import os

class OpenUnitTestCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		filePath = self.view.file_name()
		fileName = os.path.basename(filePath)
		fileNameWithoutExtension = os.path.splitext(fileName)[0]
		testFileName = 'Test' + fileNameWithoutExtension + '.cxx'
		sublime.active_window().open_file(testFileName)