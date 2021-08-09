"""
File: parserapp.py
View for the infix expression parser.
Handles user interaction.
"""

from parsers import Parser

class ParserView(object):

    def run(self):
        parser = Parser()
        while True:
            sourceStr = input("Enter an arithmetic expression or just enter to quit: ")
            if sourceStr == "": break
            try:
                parser.parse(sourceStr)
                print(parser.parseStatus())
                print(parser.tree)
            except Exception as e:
                print("Error:")
                print(e)

ParserView().run()
