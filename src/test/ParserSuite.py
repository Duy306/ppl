import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_var_decl(self):
        input = """Var: x=34,b[47][22],d[3]={3,2,7};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_var_decl2(self):
        input = """Var: x=3e22,b[47][22],d[3]={3.3,2.,7e-10};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_array(self):
        input = """Var: x[3]={3.323,2.,7e-10};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_wrong_array(self):
        input = """Var: x[3]={3.323,2,7e-10};"""
        expect = "Error on line 1 col 17: 2"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_func_decl(self):
        input = 'Function: foo\nBody:\nEndBody.'
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_para_decl(self):
        input = 'Function: foo\nParameter: a,b\nBody:\nEndBody.'
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_assign(self):
        input = "Function: foo\nBody:\na = 12 * 3;\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_int_assign(self):
        input = "Function: foo\nBody:\na = (12+x) % k[45] * 3;\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_int_assign2(self):
        input = "Function: foo\nBody:\na = (12+x) % k[45] * int_of_string(a[323][23*44]);\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    
    def test_float_assign(self):
        input = "Function: foo\nBody:\na = (12. +. x) \\. k[45] *. 3.e-23;\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    