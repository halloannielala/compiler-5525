class Live_vars:
    def __init__(self, before, after):
        self.before = before
        self.after = after
    def add_before(self, vars):
        self.before = self.before | vars

    def add_after(self, vars):
        self.after = self.after | vars

    def __str__(self):
        return '('+ str(self.before)+','+str(self.after)+')'
class ColorTable:
    def __init__(self, graph):
        self.tbl = {}
        for key in graph:
            if key == 'eax':
                self.tbl[key] = 3
            elif key == 'ecx':
                self.tbl[key] = 4
            elif key == 'edx':
                self.tbl[key] = 5
            else:
                self.tbl[key] = -1
    def get_color(self,node):
        return self.tbl[node]

    def set_color(self,node,color):
        self.tbl[node] = color


class X86Arg:
    def __str__(self):
        return self.mnemonic()
    
class Const86(X86Arg):
    def __init__(self, value):
        self.value = value
    def mnemonic(self):
        return '$' + str(self.value)

class Reg86(X86Arg):
    def __init__(self, register):
        self.register = register
    def mnemonic(self):
        return '%' + self.register

class Mem86(X86Arg):
    def __init__(self, offset, register):
        self.offset = offset
        self.register = register
    def mnemonic(self):
        return ('-%d(%s)' % (self.offset, self.register.mnemonic()))

class Var(X86Arg):
    def  __init__(self, name, color):
        self.name = name
        self.color = color
    def mnemonic(self):
        return '' + self.name
    
class X86Inst:
    def __str__(self):
        return self.mnemonic()

class Push86(X86Inst):
    def __init__(self, value):
        self.value = value
    def mnemonic(self):
        return 'pushl ' + self.value.mnemonic() 

class Move86(X86Inst):
    def __init__(self, value, target):
        self.value = value
        self.target = target
    def mnemonic(self):
        return ('movl %s, %s' % (self.value.mnemonic(), self.target.mnemonic()))

class Sub86(X86Inst):
    def __init__(self, value, target):
        self.value = value
        self.target = target
    def mnemonic(self):
        return ('subl %s, %s' % (self.value.mnemonic(), self.target.mnemonic()))

class Add86(X86Inst):
    def __init__(self, value, target):
        self.value = value
        self.target = target
    def mnemonic(self):
        return ('addl %s, %s' % (self.value.mnemonic(), self.target.mnemonic()))

class Neg86(X86Inst):
    def __init__(self, target):
        self.target = target
    def mnemonic(self):
        return 'negl ' + self.target.mnemonic()

class Call86(X86Inst):
    def __init__(self, function):
        self.function = function
    def mnemonic(self):
        return 'call ' + self.function

class Leave86(X86Inst):
    def mnemonic(self):
        return 'leave'

class Ret86(X86Inst):
    def mnemonic(self):
        return 'ret'