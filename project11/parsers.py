"""
File: parsers.py
Authors: Laurie Jones, Harry Pinkerton, James Lawson
Project: 11

"""

from modules.tree.tokens import Token
from scanner import Scanner
from modules.tree.expressionTree import InteriorNode, LeafNode

class Parser(object):
    """Represents a parser for arithmetic expressions."""

    def parse(self, sourceStr):
        """Sets up and runs the parser on a source string."""
        self.completionMessage = "No errors" 
        self.parseSuccessful = True
        self.scanner = Scanner(sourceStr)
        
        self.tree = self.expression()

        if self.completionMessage == "No errors":
            self.completionMessage += "\n" + str(self.tree.value()) 
            self.completionMessage += "\n" + self.tree.prefix()
            self.completionMessage += "\n" + self.tree.postfix()
            self.completionMessage += "\n" + self.tree.infix()
        
        self.accept(self.scanner.get(), Token.EOE,
                    "symbol after end of expression")
    
   
    def parseStatus(self):
        """Returns the completion message for the parse."""
        return self.completionMessage
    
    def accept(self, token, expected, errorMessage):
        """Checks the type of the given token for correctness."""
        if token.getType() != expected:
            self.fatalError(token, errorMessage)

    def fatalError(self, token, errorMessage):
        """Stops the parse with a syntax error messahge."""
        self.parseSuccessful = False
        self.completionMessage = "Parsing error -- " + \
                                 errorMessage + \
                                 "\nExpression so far = " + \
                                 self.scanner.stringUpToCurrentToken()
        raise Exception(self.completionMessage)

    # expression = term { addingOperator term }
    def expression(self):
        tree = self.term()
        token = self.scanner.get()
        while token.getType() in (Token.PLUS, Token.MINUS):
            self.scanner.next()
            tree = InteriorNode(token, tree, self.term())
            token = self.scanner.get()
        return tree

    # term = factor { multiplyingOperator factor }
    def term(self):
        tree = self.primary()
        token = self.scanner.get()
        while token.getType() in (Token.MUL, Token.DIV, Token.EXP):
            self.scanner.next()
            tree = InteriorNode(token, tree, self.primary())
            token = self.scanner.get()
        return tree

    # primary = number | "(" expression ")"
    def primary(self):
        token = self.scanner.get()
        if token.getType() == Token.INT:
            tree = LeafNode(token.getValue())
            self.scanner.next()
        elif token.getType() == Token.L_PAR:
            self.scanner.next()
            tree = self.expression()
            self.accept(self.scanner.get(),
                        Token.R_PAR,
                        "')' expected")
            self.scanner.next()
        else:
            tree = LeafNode(token.getValue())
            self.fatalError(token, "unexpected token")
        return tree

