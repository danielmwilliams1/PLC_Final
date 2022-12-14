## Develop a class for Token, String for a lexeme representation int for the token code

class Token:
    def __init__(self, lexeme, token_code):
        self.lexeme = lexeme
        self.token_code = token_code

    def __str__(self):
        return "Lexeme: " + self.lexeme + " Token Code: " + str(self.token_code)
    
    
## Develop a Compiler Class  takes in INPUT FILE  and converts it to one input str

class Compiler:
    def __init__(self, input_file):
        self.input_file = input_file
        self.input_str = ""
        self.token_list = []
        self.token_code = 0
        self.lexeme = ""
        self.token_dict = { 
            "program": 0,
            "if": 1,
            "then": 2,
            "else": 3,
            "end": 4,
            "repeat": 5,
            "until": 6,
            "read": 7,
            "write": 8,
            "+": 9,
            "-": 10,
            "*": 11,
            "/": 12,
            "=": 13,
            "<": 14,
            "(": 15,
            ")": 16,
            ";": 17,
            ":=": 18,
            "id": 19,
            "num": 20,
            "eof": 21,
        }

    def read_file(self):
        with open(self.input_file, "r") as f:
            self.input_str = f.read()

    def get_token(self):
        if self.input_str == "":
            return Token("eof", 21)
        
## ignore  block comments
        if self.input_str[0] == "{":
            while self.input_str[0] != "}":
                self.input_str = self.input_str[1:]
            self.input_str = self.input_str[1:]
            return self.get_token()

        

## ignore  line comments
        if self.input_str[0] == "/":
            while self.input_str[0] != " ":
                self.input_str = self.input_str[1:]
                
            self.input_str = self.input_str[1:]
            return self.get_token()

    ## parse the input string and return the next token
    def parse(self):
            if self.input_str == "":
                return Token("eof", 21)
            if self.input_str[0].isalpha():
                return self.id()
            if self.input_str[0].isdigit():
                return self.natural_literal()
            if self.input_str[0] == ".":
                return self.real_literal()
            if self.input_str[0] == "t" or self.input_str[0] == "f":
                return self.bool_literal()
            if self.input_str[0] == "+":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 9)
            if self.input_str[0] == "-":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 10)
            if self.input_str[0] == "*":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 11)
            if self.input_str[0] == "/":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 12)
            if self.input_str[0] == "=":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 13)
            if self.input_str[0] == "<":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 14)
            if self.input_str[0] == "(":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 15)
            if self.input_str[0] == ")":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 16)
            if self.input_str[0] == ";":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                return Token(self.lexeme, 17)
            if self.input_str[0] == ":":
                self.lexeme += self
            
            
## Should contain the following tokeens  and clear patterns or automata to recognize them

##real_literal = r"(\d+\.\d+)"
##natural_literal represnet whole numbers and 0
##natural_literal = r"(\d+)"

def real_literal(self):
    if self.input_str[0].isdigit():
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        while self.input_str[0].isdigit():
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
        if self.input_str[0] == ".":
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
            while self.input_str[0].isdigit():
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
            return Token(self.lexeme, 20)
        else:
            return Token(self.lexeme, 20)
    else:
        return Token("error in real_literal", 0)
    
def natural_literal(self):
    if self.input_str[0].isdigit():
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        while self.input_str[0].isdigit():
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    else:
        return Token("error in natural_literal", 0)
    
def bool_literal(self):
    if self.input_str[0] == "t":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        if self.input_str[0] == "r":
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
            if self.input_str[0] == "u":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                if self.input_str[0] == "e":
                    self.lexeme += self.input_str[0]
                    self.input_str = self.input_str[1:]
                    return Token(self.lexeme, 20)
                else:
                    return Token("error in bool_literal", 0)
            else:
                return Token("error in bool_literal", 0)
        else:
            return Token("error in bool_literal", 0)
    elif self.input_str[0] == "f":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        if self.input_str[0] == "a":
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
            if self.input_str[0] == "l":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                if self.input_str[0] == "s":
                    self.lexeme += self.input_str[0]
                    self.input_str = self.input_str[1:]
                    if self.input_str[0] == "e":
                        self.lexeme += self.input_str[0]
                        self.input_str = self.input_str[1:]
                        return Token(self.lexeme, 20)
                    else:
                        return Token("error in bool_literal", 0)
                else:
                    return Token("error in bool_literal", 0)
            else:
                return Token("error in bool_literal", 0)
        else:
            return Token("error in bool_literal", 0)
    else:
        return Token("error in bool_literal", 0)
    
## char_literal = represents a single ascii character including escape sequences 1 java char
## char_literal = r"(\w)"

def char_literal(self):
    if self.input_str[0] == "'":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        if self.input_str[0] == "'":
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
            return Token(self.lexeme, 20)
        else:
            return Token("error in char_literal", 0)
    else:
        return Token("error in char_literal", 0)
    
## string_literal represents any number of ascci characters include escape sequences

def string_literal(self): 
    if self.input_str[0] == '"':
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        while self.input_str[0] != '"':
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    else:
        return Token("error in string_literal", 0)
    
    
    
## Keywords for Selection Statements, Loop Statement, Variable Declartion for strings, naturals, character, reals, booleans

def keyword(self):
    if self.input_str[0] == "i":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        if self.input_str[0] == "f":
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
            return Token(self.lexeme, 20)
        else:
            return Token("error in keyword", 0)
    elif self.input_str[0] == "e":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        if self.input_str[0] == "l":
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
            if self.input_str[0] == "s":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                if self.input_str[0] == "e":
                    self.lexeme += self.input_str[0]
                    self.input_str = self.input_str[1:]
                    if self.input_str[0] == "i":
                        self.lexeme += self.input_str[0]
                        self.input_str = self.input_str[1:]
                        if self.input_str[0] == "f":
                            self.lexeme += self.input_str[0]
                            self.input_str = self.input_str[1:]
                            return Token(self.lexeme, 20)
                        else:
                            return Token("error in keyword", 0)
                    else:
                        return Token("error in keyword", 0)
                else:
                    return Token("error in keyword", 0)
            else:
                return Token("error in keyword", 0)
        else:
            return Token("error in keyword", 0)
    elif self.input_str[0] == "w":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        if self.input_str[0] == "h":
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
            if self.input_str[0] == "i":
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
                if self.input_str[0] == "l":
                    self.lexeme += self.input_str[ 0]
                    

## special symbols for  addition, subtraction, multiplication, division, exponentiation, symbols of breaking order, greater than, less thank 

def special_symbol(self):
    if self.input_str[0] == "+":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "-":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "*":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "/":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "^":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "(":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == ")":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == ">":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "<":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "=":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "!=":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == ">=":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    elif self.input_str[0] == "<=":
        self.lexeme += self.input_str[0]
        self.input_str = self.input_str[1:]
        return Token(self.lexeme, 20)
    else:
        return Token("error in special_symbol", 0)

    
    ## variable/ function identifier
    
def identifier(self):
        if self.input_str[0].isalpha():
            self.lexeme += self.input_str[0]
            self.input_str = self.input_str[1:]
            while self.input_str[0].isalpha() or self.input_str[0].isdigit():
                self.lexeme += self.input_str[0]
                self.input_str = self.input_str[1:]
            return Token(self.lexeme, 20)
        else:
            return Token("error in identifier", 0)
        
## Develop a Parser class: Code 10 defintions

class Parser: 
    ## An instant of this class should exist in the Compiler class
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.token = self.tokens[0]
        self.index = 0
        self.error = False
        self.error_msg = ""
        self.parse_tree = []

    

   ## Takes in aa list of Token object in its constructor 
        
    def parse(self):
        self.program()
        if self.error:
            print(self.error_msg)
        else:
            print("Parsing Successful")
        return

    
    ## aa list 
    def program(self):
        self.statement_list()
        if self.token.token_type != 0:
            self.error = True
            self.error_msg = "Error in program"
            return
        return

    ## outputs parse tree
    def statement_list(self):
        self.statement()
        if self.token.token_type == 20:
            self.statement_list()
        return

    ## outputs parse tree
    def statement(self):
        if self.token.token_type == 20:
            self.assignment_statement()
        elif self.token.token_type == 20:
            self.print_statement()
        elif self.token.token_type == 20:
            self.conditional_statement()
        elif self.token.token_type == 20:
            self.loop_statement()
        else:
            self.error = True
            self.error_msg = "Error in statement"
            return
        return
    
    def code_block(self):
        if self.token.token_type == 20:
            self.statement_list()
        else:
            self.error = True
            self.error_msg = "Error in code_block"
            return
        return


        ## expression should allow for unary negation operator
    def expression(self):
        if self.token.token_type == 20:
            self.term()
            self.expression_prime()
        else:
            self.error = True
            self.error_msg = "Error in expression"
            return
        return
    
    ## declaration statment Variables and Function Definitions
    def declaration_statement(self):
        if self.token.token_type == 20:
            self.variable_declaration()
        elif self.token.token_type == 20:
            self.function_declaration()
        else:
            self.error = True
            self.error_msg = "Error in declaration_statement"
            return
        return
    
    ## variable declaration
    def variable_declaration(self):
        if self.token.token_type == 20:
            self.variable_identifier()
            if self.token.token_type == 20:
                self.match(20)
                if self.token.token_type == 20:
                    self.expression()
                else:
                    self.error = True
                    self.error_msg = "Error in variable_declaration"
                    return
            else:
                self.error = True
                self.error_msg = "Error in variable_declaration"
                return
        else:
            self.error = True
            self.error_msg = "Error in variable_declaration"
            return
        return
    
    ## function declaration
    def function_declaration(self):
        if self.token.token_type == 20:
            self.function_identifier()
            if self.token.token_type == 20:
                self.match(20)
                if self.token.token_type == 20:
                    self.parameter_list()
                    if self.token.token_type == 20:
                        self.match(20)
                        if self.token.token_type == 20:
                            self.code_block()
                        else:
                            self.error = True
                            self.error_msg = "Error in function_declaration"
                            return
                    else:
                        self.error = True
                        self.error_msg = "Error in function_declaration"
                        return
                else:
                    self.error = True
                    self.error_msg = "Error in function_declaration"
                    return
            else:
                self.error = True
                self.error_msg = "Error in function_declaration"
                return
        else:
            self.error = True
            self.error_msg = "Error in function_declaration"
            return
        return
    
    
    ## use Denotion semantics to define your selection statement 
    def conditional_statement(self):
        if self.token.token_type == 20:
            self.match(20)
            if self.token.token_type == 20:
                self.expression()
                if self.token.token_type == 20:
                    self.match(20)
                    if self.token.token_type == 20:
                        self.code_block()
                        if self.token.token_type == 20:
                            self.match(20)
                            if self.token.token_type == 20:
                                self.code_block()
                            else:
                                self.error = True
                                self.error_msg = "Error in conditional_statement"
                                return
                        else:
                            self.error = True
                            self.error_msg = "Error in conditional_statement"
                            return
                    else:
                        self.error = True
                        self.error_msg = "Error in conditional_statement"
                        return
                else:
                    self.error = True
                    self.error_msg = "Error in conditional_statement"
                    return
            else:
                self.error = True
                self.error_msg = "Error in conditional_statement"
                return
        else:
            self.error = True
            self.error_msg = "Error in conditional_statement"
            return
        return
    
    ## use Denotion semantics to define your loop statement
    def loop_statement(self):
        if self.token.token_type == 20:
            self.match(20)
            if self.token.token_type == 20:
                self.expression()
                if self.token.token_type == 20:
                    self.match(20)
                    if self.token.token_type == 20:
                        self.code_block()
                    else:
                        self.error = True
                        self.error_msg = "Error in loop_statement"
                        return
                else:
                    self.error = True
                    self.error_msg = "Error in loop_statement"
                    return
            else:
                self.error = True
                self.error_msg = "Error in loop_statement"
                return
        else:
            self.error = True
            self.error_msg = "Error in loop_statement"
            return
        return
    
    ## use Denotion semantics to define your print statement
    def Expr_statement(self):
        if self.token.token_type == 20:
            self.expression()
        elif self.token.token_type == 20:
            self.match(20)
        else:
            self.error = True
            self.error_msg = "Error in Expr_statement"
            return
        return
    
    ## use Denotion semantics to redifine your Expr statement so it can return a Boolean solution
    def expression_prime(self):
        if self.token.token_type == 20:
            self.addop()
            self.term()
            self.expression_prime()
        elif self.token.token_type == 20:
            self.match(20)
        else:
            self.error = True
            self.error_msg = "Error in expression_prime"
            return
        return
    
    ## Define the attribute grammar for your assignment statement, make sure to use Denotion semantics
    
    def assignment_statement(self): ## use String + String does concatenation
        if self.token.token_type == 20:
            ## make an assignment statment  String '+' Strign does concatenation
            self.variable_identifier()
            ## String '*' Natural repeats the Natural
            ## String '*' String does concatenation  
            if self.token.token_type == 20:
            ## Assign bool to natural is allowed
                self.match(20)
            ## Assign char to natural is allowed
                self.expression()
            else:
                self.error = True
                self.error_msg = "Error in assignment_statement"
                return
            
        else:
            self.error = True
            self.error_msg = "Error in assignment_statement"
            return
        return
    
    ## Define the attribute grammar for your function call statement, make sure to use Denotion semantics
    def function_call_statement(self):
        if self.token.token_type == 20:
            self.function_identifier()
            if self.token.token_type == 20:
                self.match(20)
                if self.token.token_type == 20:
                    self.expression_list()
                    if self.token.token_type == 20:
                        self.match(20)
                    else:
                        self.error = True
                        self.error_msg = "Error in function_call_statement"
                        return
                else:
                    self.error = True
                    self.error_msg = "Error in function_call_statement"
                    return
            else:
                self.error = True
                self.error_msg = "Error in function_call_statement"
                return
        else:
            self.error = True
            self.error_msg = "Error in function_call_statement"
            return
        return
    
    
## Choose 3 syntactically valid assignment statments with at least 7 tokens to show these rules failing or passing semantic rules

    
    def test(self):
        self.token = self.lexer.get_next_token()
        self.program()
        if self.error:
            print(self.error_msg)
        else:
            print("Success")
            
    def test2(self):
        self.token = self.lexer.get_next_token()
        self.function_declaration()
        if self.error:
            print(self.error_msg)
        else:
            print("Success")
            
    def test3(self):
        self.token = self.lexer.get_next_token()
        self.conditional_statement()
        if self.error:
            print(self.error_msg)
        else:
            print("Success")
            
    def test4(self):
        self.token = self.lexer.get_next_token()
        self.loop_statement()
        if self.error:
            print(self.error_msg)
        else:
            print("Success")
            
            ## test case
    def test5(self):
        self.token = self.lexer.get_next_token()
        self.Expr_statement()
        if self.error:
            print(self.error_msg)
        else:
            print("Success")

    
    
    
    
## Axiomatic Semantics(find the weakest precondition):

##a.
## test case: a = 2 * (b - 1) - 1 {a > 0}
## weakest precondition: a > 0
## strongest postcondition: a > 0
## test case: a = 2 * (b - 1) - 1 {a < 0}
## weakest precondition: a < 0
## strongest postcondition: a < 0

##b.
## test case: if (x < y)
## weakest precondition: x < y
## strongest postcondition: x < y
## test case: if (x > y)
## weakest precondition: x > y
## strongest postcondition: x > y

##c.
## test case: y = a * 2 * (b - 1) - 1
## weakest precondition: a > 0
## strongest postcondition: a > 0
## test case: y = a * 2 * (b - 1) - 1
## weakest precondition: a < 0
## strongest postcondition: a < 0

##d.
## test case: a = 3 * (2 * b + a);
## weakest precondition: b > 5
## strongest postcondition: b > 5
## test case: a = 3 * (2 * b + a);
## weakest precondition: b < 5
## strongest postcondition: b < 5

## Axiomatic Semantics(find the strongest postcondition):

#a 
##a = 2 * (b - 1) - 1 {a > 0}


##b.
##if (x < y)
##x = x + 1
##else
##x = 3 * x
##{x < 0}

##c.
##y = a * 2 * (b - 1) - 1
##if (x < y)
##x = y + 1
##else
##x = 3 * x
##{x < 0}

##d.
##a = 3 * (2 * b + a);
##b = 2 * a - 1
##{b > 5}

## Lexer class


##def test1():
  ##  lexer = Lexer("test1.txt")
    ##parser = Parser(lexer)
    ##parser.test()

##def test2():
  ##  lexer = Lexer("test2.txt")
    ##parser = Parser(lexer)
    ##parser.test2()
    
##def test3():
  ##  lexer = Lexer("test3.txt")
    ##parser = Parser(lexer)
    ##parser.test3()
    
##def test4():
  ##  lexer = Lexer("test4.txt")
    ##parser = Parser(lexer)
    ##arser.test4()
    