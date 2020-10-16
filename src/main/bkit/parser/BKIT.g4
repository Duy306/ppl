// 1811744
grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program     : var_decl program
            | function program
            | EOF;

var_decl    : VAR CL var_list SM;

var_list    : var_elm (CM var_elm)*;
var_elm     : ID (EQ (FLOAT_LIT|INT_LIT|BOOL_LIT|STRING_LIT))?
            | ID LS INT_LIT RS (EQ array)?
            | ID LS INT_LIT RS LS INT_LIT RS (EQ array2)?;

var_id      : ID|array_elm_id;

array2          : LB array (CM array)* RB;
array           : float_array|int_array|string_array|bool_array;

float_array     : LB FLOAT_LIT (CM FLOAT_LIT)* RB;
int_array       : LB INT_LIT(CM INT_LIT)* RB;
string_array    : LB STRING_LIT(CM STRING_LIT)* RB;
bool_array      : LB BOOL_LIT(CM BOOL_LIT)* RB;

array_elm_id: ID LS int_exp RS (LS int_exp RS)?;

function    : FUNCTION CL ID para_decl? BODY CL func_body ENDBODY FS;

para_decl   : PARA CL para_list;

para_list   : var_id (CM var_id)*; 

func_body   : (statement)*;

statement   : var_decl|assign|func_call SM|return_stm
            | if_stm|for_stm|while_stm|do_while;

func_call   : ID LP (exp (CM exp)*)? RP;

assign      : var_id EQ (exp|string_cor) SM;

return_stm  : RETURN exp SM;

if_stm:     IF bool_exp THEN func_body
            (ELSEIF bool_exp THEN func_body)*
            (ELSE func_body)?
            ENDIF FS;

for_stm:    FOR(ID EQ exp CM bool_exp CM assign) DO
                (statement|break_stm|continue_stm)*
            ENDFOR FS;

while_stm:  WHILE bool_exp DO (statement|break_stm|continue_stm)* ENDWHILE FS;

do_while:   DO (statement|break_stm|continue_stm)* WHILE bool_exp ENDDO FS;

break_stm:      BREAK SM;

continue_stm:   CONTINUE SM;

int_cor     :   'int_of_float' LP float_exp RP
            |   'int_of_string' LP (STRING_LIT|var_id) RP;

float_cor   :   'float_of_int' LP int_exp RP
            |   'float_of_string' LP (STRING_LIT|var_id) RP;

string_cor  :   'string_of_int' LP int_exp RP
            |   'string_of_float' LP float_exp RP
            |   'string_of_bool' LP bool_exp RP;

bool_cor    :   'bool_of_string' LP (STRING_LIT|var_id) RP;

exp         :   float_exp
            |   int_exp;

float_exp       :   float_exp2 FLOAT_ADD_OP float_exp
                |   float_exp2;

float_exp2      :   LP float_exp RP
                |   float_exp3 FLOAT_MUL_OP float_exp
                |   float_exp3;

float_exp3      :   LP float_exp RP
                |   FLOAT_LIT | ID | array_elm_id | func_call | float_cor;

int_exp         :   int_exp2 INT_ADD_OP int_exp
                |   int_exp2;

int_exp2        :   LP int_exp RP
                |   int_exp3 INT_MUL_OP int_exp
                |   int_exp3;

int_exp3        :   LP int_exp RP
                |   INT_LIT | ID | array_elm_id | func_call | int_cor;

bool_exp    :   float_exp FLOAT_RL_OP float_exp
            |   int_exp INT_RL_OP int_exp
            |   bool_exp2 LOGIC bool_exp
            |   NEGA bool_exp2
            |   bool_exp2;

bool_exp2   :   LP bool_exp RP
            |   BOOL_LIT | ID | array_elm_id | func_call | bool_cor;

FUNCTION    : 'Function';
VAR         : 'Var';
PARA        : 'Parameter';
BODY        : 'Body';
ENDBODY     : 'EndBody';
IF          : 'If';
ELSEIF      : 'ElseIf';
ELSE        : 'Else';
THEN        : 'Then';
ENDIF       : 'EndIf';
FOR         : 'For';
DO          : 'Do';
ENDFOR      : 'EndFor';
WHILE       : 'While';
ENDWHILE    : 'EndWhile';
ENDDO       : 'EndDo';
BREAK       : 'Break';
CONTINUE    : 'Continue';
RETURN      : 'Return';

SM: ';';
CM: ',';
CL: ':';
FS: '.';
EQ : '=';

FLOAT_LIT   : DECIMAL ((DOT DIGIT* (EPS DIGIT+)?) | (EPS DIGIT+));
INT_LIT     : HEX|OCTAL|DECIMAL;
BOOL_LIT    : 'True'|'False';
STRING_LIT  : DOUB_QUOTE (ESCAPE_SEQ | CHAR | '\'' | SING_QUOTE DOUB_QUOTE)* DOUB_QUOTE
	{
		self.text = self.text[1:-1].replace('\'"', '"').replace("\\'","'")
	};

ID: LOWER(LOWER|UPPER|US|DIGIT)* ;
//KEY: UPPER(LOWER|UPPER|US|DIGIT)* ;

LB: '{';
RB: '}';
LS: '[';
RS: ']';
LP: '(';
RP: ')';

NEGA            : '!';
LOGIC           : '&&'|'||';
FLOAT_MUL_OP    : ('*'|'\\')DOT;
FLOAT_ADD_OP    : ('+'|'-')DOT;
FLOAT_RL_OP     : (('<'|'>')'='?DOT)|'=/=';
INT_MUL_OP      : '*'|'\\'|'%';
INT_ADD_OP      : '+'|'-';
INT_RL_OP       : '=='|'!='|(('<'|'>')'='?);

fragment NOT_0_DIGIT    : [1-9];
fragment DIGIT          : [0-9];
fragment LOWER          : [a-z];
fragment UPPER          : [A-Z];
fragment CHAR           : ~['"];
fragment SING_QUOTE     : '\'';
fragment DOUB_QUOTE     : '"';
fragment HEX            : '0'[xX](DIGIT|[A-F]|[a-f])+;
fragment OCTAL          : '0'[oO][0-7]+;
fragment DECIMAL        : (NOT_0_DIGIT DIGIT*)|'0';
fragment EPS            : [Ee]'-'?;
fragment US             : '_';
fragment DOT            : '.';
fragment ESCAPE_SEQ     : '\\' [bfrnt'\\];

WS      : [ \t\f\r\n]+ -> skip ;
//CMT   : '**'(.)*'**' -> skip ;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;