import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """Var: x;\nFunction: main\nBody:\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_wrong_miss_close(self):
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_var_decl(self):
        input = """Var: x=34,b[47][22],d[3]={3,2,7};\nFunction: main\nBody:\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_var_decl2(self):
        input = """Var: x=3e22,b[47][22],d[3]={3.3,2.,7e-10};\nFunction: main\nBody:\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_array(self):
        input = """Var: x[3]={3.323,2.,7e-10};\nFunction: main\nBody:\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_wrong_array(self):
        input = """Var: x[3]={3.323,2,7e-10};"""
        expect = "Error on line 1 col 17: 2"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_func_decl(self):
        input = 'Function: main\nBody:\nEndBody.'
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_para_decl(self):
        input = 'Function: foo\nParameter: a,b\nBody:\nEndBody.\nFunction: main\nBody:\nEndBody.'
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_assign(self):
        input = "Function: main\nBody:\na = 12 * 3;\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))
    
    def test_int_assign(self):
        input = "Function: main\nBody:\na = (12+x) % k[45] * 3;\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_int_assign2(self):
        input = "Function: main\nBody:\na = (12+x) % k[45] * int_of_string(a[323][23*44]);\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))
    
    def test_float_assign(self):
        input = "Function: main\nBody:\na = (12. +. x) \\. k[45] *. 3.e-23;\nEndBody."
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_string_assign(self):
        input = """Function: main\nBody:\na = "bai kho qua thay oi";\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_string_assign_with_escape(self):
        input = """Function: main\nBody:\na = "bai kho qua thay oi\\t";\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))
    
    def test_string_assign_with_escape2(self):
        input = """Function: main\nBody:\na = "T noi voi no: '"danh nhao ko m?'"";\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_if_stm(self):
        input = """Function: main\nBody:\nIf n>=3 Then a=b+c; EndIf.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_if_stm2(self):
        input = """Function: main\nBody:\nIf m==a && k=/=2.0 Then a=b+c; EndIf.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_else_stm(self):
        input = """Function: main\nBody:\nIf m==a && k=/=2.0 Then a=b+c;\nElse a=0;\nEndIf.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_elseif_stm(self):
        input = """Function: main\nBody:\nIf m==a && k=/=2.0 Then a=b+c;\nElseIf a==b Then a="bao h moi xong bai :((";\nEndIf.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_for_stm(self):
        input = """Function: main\nBody:\nFor (i=0,i<.34.11*.33.,-2) Do\na[i]=i+1;\nEndFor.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))

    def test_for_stm2(self):
        input = """Function: main\nBody:\nFor (i=0,True,433-65) Do\na[i]=i+1;\nEndFor.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_wrong_for(self):
        input = """Function: main\nBody:\nFor (i=0.32,True,4) Do\na[i]=i+1;\nEndFor.\nEndBody."""
        expect = "Error on line 3 col 7: 0.32"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_if_in_for(self):
        input = """Function: main\nBody:\nFor (i=0,True,4) Do\nIf b==i+8 Then a[i]=i+1;\nElse Break;\nEndIf.\nEndFor.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_if_in_for2(self):
        input = """Function: main\nBody:\nFor (i=0,True,4) Do\nIf b==i+8 Then If a<=2*i Then Break;\nEndIf.\nElse Break;\nEndIf.\nEndFor.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_while(self):
        input = """Function: main\nBody:\nWhile a==0 Do\nb[0]=False;\nEndWhile.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_while_in_for(self):
        input = """Function: main\nBody:\nFor (i=0,True,4) Do\nWhile a==0 Do\nb[0]=False;\nEndWhile.\nEndFor.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_while2(self):
        input = """Function: main\nBody:\nWhile a==0 && b<8 Do\ncdm[0]=False;\nEndWhile.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_dowhile(self):
        input = """Function: main\nBody:\nDo\ncdm[0]=False;\nWhile a==0 && b<8\nEndDo.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_while3(self):
        input = """Function: main\nBody:\nWhile a==0 && b<8 Do\ncdm[0]=False;\nIf sad Then Break; EndIf.\nEndWhile.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_cor(self):
        input = """Function: main\nBody:\na=int_of_string("323");\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_cor2(self):
        input = """Function: main\nBody:\na=int_of_float(32e22);\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_cor3(self):
        input = """Function: main\nBody:\na=int_of_string(323);\nEndBody."""
        expect = "Error on line 3 col 16: 323"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_cor4(self):
        input = """Function: main\nBody:\na=int_of_float(32e22);\nb=float_of_int(a);\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_cor5(self):
        input = """Function: main\nBody:\na=string_of_int(444-132*d[32]);\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_cor6(self):
        input = """Function: main\nBody:\na=string_of_float(43.\\.122e-1);\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))

    def test_cor7(self):
        input = """Function: main\nBody:\na=string_of_bool(True);\nb=string_of_bool(False);\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_cor8(self):
        input = """Function: main\nBody:\nnarutoooooooooo=bool_of_string("Sasukeeeeeeeeeee");\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_print(self):
        input = """Function: main\nBody:\nprint("Tao se tro thanh Hokageee");\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_print2(self):
        input = """Function: main\nBody:\nprint("Tao se tro thanh Vua hai taccc"); printLn();\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_print3(self):
        input = """Function: main\nBody:\nprint("Hay nho lay ten ta, nguoi se tro thanh vua hai tac: "); read();\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_print4(self):
        input = """Function: main\nBody:\nprintStrLn("Ui doi oi game de vai");\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_print5(self):
        input = """Function: main\nBody:\nprint(lol[3]);\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_print6(self):
        input = """Function: main\nBody:\nprintStrLn("NARUTOOOOOOOO");\nprintStrLn("PAPASUKEEEEEEEE");\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_cmt(self):
        input = """**San pham nay khong phai la thuoc va khong co tac dung thay the thuoc chua benh**\nFunction: main\nBody:\nprintStrLn("NARUTOOOOOOOO");\nprintStrLn("PAPASUKEEEEEEEE");\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_wrong_cmt(self):
        input = """**San pham nay khong phai la thuoc va khong co tac dung thay the thuoc chua benh\nFunction: main\nBody:\nprintStrLn("NARUTOOOOOOOO");\nprintStrLn("PAPASUKEEEEEEEE");\nEndBody."""
        expect = "Error on line 1 col 0: *"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_program(self):
        input = """**San pham nay khong phai la thuoc va khong co tac dung thay the thuoc chua benh**\nFunction: main\nBody:\nprintStrLn("ZAWARUDOOO");\nIf jonathan Then printStrLn("MUDAMUDAMUDAMUDA");\nElse printStrLn("KONO DIO DA");\nEndIf.\nEndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))