# Generated from BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#var_decl.
    def enterVar_decl(self, ctx:BKITParser.Var_declContext):
        pass

    # Exit a parse tree produced by BKITParser#var_decl.
    def exitVar_decl(self, ctx:BKITParser.Var_declContext):
        pass


    # Enter a parse tree produced by BKITParser#var_elm.
    def enterVar_elm(self, ctx:BKITParser.Var_elmContext):
        pass

    # Exit a parse tree produced by BKITParser#var_elm.
    def exitVar_elm(self, ctx:BKITParser.Var_elmContext):
        pass


    # Enter a parse tree produced by BKITParser#var_list.
    def enterVar_list(self, ctx:BKITParser.Var_listContext):
        pass

    # Exit a parse tree produced by BKITParser#var_list.
    def exitVar_list(self, ctx:BKITParser.Var_listContext):
        pass


    # Enter a parse tree produced by BKITParser#var_id.
    def enterVar_id(self, ctx:BKITParser.Var_idContext):
        pass

    # Exit a parse tree produced by BKITParser#var_id.
    def exitVar_id(self, ctx:BKITParser.Var_idContext):
        pass


    # Enter a parse tree produced by BKITParser#array.
    def enterArray(self, ctx:BKITParser.ArrayContext):
        pass

    # Exit a parse tree produced by BKITParser#array.
    def exitArray(self, ctx:BKITParser.ArrayContext):
        pass


    # Enter a parse tree produced by BKITParser#array2.
    def enterArray2(self, ctx:BKITParser.Array2Context):
        pass

    # Exit a parse tree produced by BKITParser#array2.
    def exitArray2(self, ctx:BKITParser.Array2Context):
        pass


    # Enter a parse tree produced by BKITParser#array_elm_id.
    def enterArray_elm_id(self, ctx:BKITParser.Array_elm_idContext):
        pass

    # Exit a parse tree produced by BKITParser#array_elm_id.
    def exitArray_elm_id(self, ctx:BKITParser.Array_elm_idContext):
        pass


    # Enter a parse tree produced by BKITParser#function.
    def enterFunction(self, ctx:BKITParser.FunctionContext):
        pass

    # Exit a parse tree produced by BKITParser#function.
    def exitFunction(self, ctx:BKITParser.FunctionContext):
        pass


    # Enter a parse tree produced by BKITParser#para_decl.
    def enterPara_decl(self, ctx:BKITParser.Para_declContext):
        pass

    # Exit a parse tree produced by BKITParser#para_decl.
    def exitPara_decl(self, ctx:BKITParser.Para_declContext):
        pass


    # Enter a parse tree produced by BKITParser#para_list.
    def enterPara_list(self, ctx:BKITParser.Para_listContext):
        pass

    # Exit a parse tree produced by BKITParser#para_list.
    def exitPara_list(self, ctx:BKITParser.Para_listContext):
        pass


    # Enter a parse tree produced by BKITParser#func_body.
    def enterFunc_body(self, ctx:BKITParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by BKITParser#func_body.
    def exitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        pass


    # Enter a parse tree produced by BKITParser#func_call.
    def enterFunc_call(self, ctx:BKITParser.Func_callContext):
        pass

    # Exit a parse tree produced by BKITParser#func_call.
    def exitFunc_call(self, ctx:BKITParser.Func_callContext):
        pass


    # Enter a parse tree produced by BKITParser#assign.
    def enterAssign(self, ctx:BKITParser.AssignContext):
        pass

    # Exit a parse tree produced by BKITParser#assign.
    def exitAssign(self, ctx:BKITParser.AssignContext):
        pass


    # Enter a parse tree produced by BKITParser#return_stm.
    def enterReturn_stm(self, ctx:BKITParser.Return_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#return_stm.
    def exitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#if_stm.
    def enterIf_stm(self, ctx:BKITParser.If_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#if_stm.
    def exitIf_stm(self, ctx:BKITParser.If_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#for_stm.
    def enterFor_stm(self, ctx:BKITParser.For_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#for_stm.
    def exitFor_stm(self, ctx:BKITParser.For_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#while_stm.
    def enterWhile_stm(self, ctx:BKITParser.While_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#while_stm.
    def exitWhile_stm(self, ctx:BKITParser.While_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#do_while.
    def enterDo_while(self, ctx:BKITParser.Do_whileContext):
        pass

    # Exit a parse tree produced by BKITParser#do_while.
    def exitDo_while(self, ctx:BKITParser.Do_whileContext):
        pass


    # Enter a parse tree produced by BKITParser#break_stm.
    def enterBreak_stm(self, ctx:BKITParser.Break_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#break_stm.
    def exitBreak_stm(self, ctx:BKITParser.Break_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#continue_stm.
    def enterContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        pass

    # Exit a parse tree produced by BKITParser#continue_stm.
    def exitContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        pass


    # Enter a parse tree produced by BKITParser#int_cor.
    def enterInt_cor(self, ctx:BKITParser.Int_corContext):
        pass

    # Exit a parse tree produced by BKITParser#int_cor.
    def exitInt_cor(self, ctx:BKITParser.Int_corContext):
        pass


    # Enter a parse tree produced by BKITParser#float_cor.
    def enterFloat_cor(self, ctx:BKITParser.Float_corContext):
        pass

    # Exit a parse tree produced by BKITParser#float_cor.
    def exitFloat_cor(self, ctx:BKITParser.Float_corContext):
        pass


    # Enter a parse tree produced by BKITParser#string_cor.
    def enterString_cor(self, ctx:BKITParser.String_corContext):
        pass

    # Exit a parse tree produced by BKITParser#string_cor.
    def exitString_cor(self, ctx:BKITParser.String_corContext):
        pass


    # Enter a parse tree produced by BKITParser#bool_cor.
    def enterBool_cor(self, ctx:BKITParser.Bool_corContext):
        pass

    # Exit a parse tree produced by BKITParser#bool_cor.
    def exitBool_cor(self, ctx:BKITParser.Bool_corContext):
        pass


    # Enter a parse tree produced by BKITParser#int_exp.
    def enterInt_exp(self, ctx:BKITParser.Int_expContext):
        pass

    # Exit a parse tree produced by BKITParser#int_exp.
    def exitInt_exp(self, ctx:BKITParser.Int_expContext):
        pass


    # Enter a parse tree produced by BKITParser#int_exp2.
    def enterInt_exp2(self, ctx:BKITParser.Int_exp2Context):
        pass

    # Exit a parse tree produced by BKITParser#int_exp2.
    def exitInt_exp2(self, ctx:BKITParser.Int_exp2Context):
        pass


    # Enter a parse tree produced by BKITParser#float_exp.
    def enterFloat_exp(self, ctx:BKITParser.Float_expContext):
        pass

    # Exit a parse tree produced by BKITParser#float_exp.
    def exitFloat_exp(self, ctx:BKITParser.Float_expContext):
        pass


    # Enter a parse tree produced by BKITParser#float_exp2.
    def enterFloat_exp2(self, ctx:BKITParser.Float_exp2Context):
        pass

    # Exit a parse tree produced by BKITParser#float_exp2.
    def exitFloat_exp2(self, ctx:BKITParser.Float_exp2Context):
        pass


    # Enter a parse tree produced by BKITParser#exp.
    def enterExp(self, ctx:BKITParser.ExpContext):
        pass

    # Exit a parse tree produced by BKITParser#exp.
    def exitExp(self, ctx:BKITParser.ExpContext):
        pass


    # Enter a parse tree produced by BKITParser#bool_exp.
    def enterBool_exp(self, ctx:BKITParser.Bool_expContext):
        pass

    # Exit a parse tree produced by BKITParser#bool_exp.
    def exitBool_exp(self, ctx:BKITParser.Bool_expContext):
        pass


    # Enter a parse tree produced by BKITParser#bool_exp2.
    def enterBool_exp2(self, ctx:BKITParser.Bool_exp2Context):
        pass

    # Exit a parse tree produced by BKITParser#bool_exp2.
    def exitBool_exp2(self, ctx:BKITParser.Bool_exp2Context):
        pass


    # Enter a parse tree produced by BKITParser#statement.
    def enterStatement(self, ctx:BKITParser.StatementContext):
        pass

    # Exit a parse tree produced by BKITParser#statement.
    def exitStatement(self, ctx:BKITParser.StatementContext):
        pass



del BKITParser