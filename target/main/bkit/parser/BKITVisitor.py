# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_decl.
    def visitVar_decl(self, ctx:BKITParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_elm.
    def visitVar_elm(self, ctx:BKITParser.Var_elmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_list.
    def visitVar_list(self, ctx:BKITParser.Var_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var_id.
    def visitVar_id(self, ctx:BKITParser.Var_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array2.
    def visitArray2(self, ctx:BKITParser.Array2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array_elm_id.
    def visitArray_elm_id(self, ctx:BKITParser.Array_elm_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#function.
    def visitFunction(self, ctx:BKITParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_decl.
    def visitPara_decl(self, ctx:BKITParser.Para_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#para_list.
    def visitPara_list(self, ctx:BKITParser.Para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_body.
    def visitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#func_call.
    def visitFunc_call(self, ctx:BKITParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign.
    def visitAssign(self, ctx:BKITParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stm.
    def visitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stm.
    def visitIf_stm(self, ctx:BKITParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stm.
    def visitFor_stm(self, ctx:BKITParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stm.
    def visitWhile_stm(self, ctx:BKITParser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while.
    def visitDo_while(self, ctx:BKITParser.Do_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stm.
    def visitBreak_stm(self, ctx:BKITParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stm.
    def visitContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_cor.
    def visitInt_cor(self, ctx:BKITParser.Int_corContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_cor.
    def visitFloat_cor(self, ctx:BKITParser.Float_corContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#string_cor.
    def visitString_cor(self, ctx:BKITParser.String_corContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_cor.
    def visitBool_cor(self, ctx:BKITParser.Bool_corContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_exp.
    def visitInt_exp(self, ctx:BKITParser.Int_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#int_exp2.
    def visitInt_exp2(self, ctx:BKITParser.Int_exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_exp.
    def visitFloat_exp(self, ctx:BKITParser.Float_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#float_exp2.
    def visitFloat_exp2(self, ctx:BKITParser.Float_exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_exp.
    def visitBool_exp(self, ctx:BKITParser.Bool_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#bool_exp2.
    def visitBool_exp2(self, ctx:BKITParser.Bool_exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)



del BKITParser