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

fragment LOWER          : [a-z];
fragment UPPER          : [A-Z];
DIGIT          : [0-9];
fragment CHAR           : ~["];
fragment SING_QUOTE     : ['];
fragment DOUB_QUOTE     : ["];
fragment HEX            : '0'[xX](DIGIT|[A-F]|[a-f])+;
fragment OCTAL          : '0'[oO][0-7]+;
fragment DECIMAL        : DIGIT+;

fragment US: '_';
LB: '{';
RB: '}';
LS: '[';
RS: ']';
LP: '(';
RP: ')';
SM: ';';
CM: ',';
CL: ':';
FS: '.';

EQ : '=';

RETURN: 'return';

FLOAT_LIT: DIGIT+ ('.'? DIGIT* [Ee]'-'? DIGIT+)|FS;
INT_LIT: HEX|OCTAL|DECIMAL;
BOOL_LIT: 'True'|'False';
STRING_LIT: DOUB_QUOTE (ESCAPE_SEQUENCES | ~['"] | SING_QUOTE DOUB_QUOTE)* DOUB_QUOTE
	{
		self.text = self.text[1:-1].replace('\'"', '"')
        self.text = self.text.replace("\\'","'")
	};
fragment ESCAPE_SEQUENCES : '\\' [bfrnt'\\];

LIT: INT_LIT|FLOAT_LIT|BOOL_LIT|STRING_LIT;

FUNCTION: 'Function';
PARA: 'Parameter';
OPEN: 'Body';
CLOSE: 'EndBody';
ID: LOWER(LOWER|UPPER|US|DIGIT)* ;
KEY: UPPER(LOWER|UPPER|US|DIGIT)* ;

NEGA: '!';
LOGIC: '&&'|'||';
INT_AR_OP: '+'|'-'|'*'|'\\'|'%';
INT_RL_OP: '=='|'!='|(('<'|'>')'='?);
FLOAT_AR_OP: ('+'|'-'|'*'|'\\')FS;
FLOAT_RL_OP: (('<'|'>')'='?FS)|'=/=';

VAR: 'Var';

WS : [ \t\f\r\n]+ -> skip ; // skip spaces, tabs, newlines
//CMT: '**'(.)*'**' -> skip ;

program: (var_decl SM)? function* EOF;

var_decl: VAR CL var_list;

var_elm:    ID (EQ LIT)?
    |   ID LS DIGIT RS (EQ array2)?
    |   ID LS DIGIT RS LS DIGIT RS (EQ array)?;
var_list: var_elm (CM var_elm)*;
var_id: ID|array_elm_id;

array: LB array2 (CM array2)* RB;
array2:  LB (FLOAT_LIT (CM FLOAT_LIT)*)
        |LB (INT_LIT(CM INT_LIT)*) RB
        |LB (STRING_LIT(CM STRING_LIT)*) RB
        |LB (BOOL_LIT(CM BOOL_LIT)*) RB;
array_elm_id: ID LS int_exp RS (LS int_exp RS)?;

function: FUNCTION CL ID para_decl OPEN CL func_body CLOSE FS;

para_decl: PARA CL para_list;

para_list: var_id (CM var_id)*; 

func_body: (statement)*;

func_call: ID LP (exp (CM exp)*)? RP;

assign: var_id EQ exp|string_cor;

return_stm: RETURN exp;

if_stm: 'If' bool_exp 'Then' func_body
    ('ElseIf' bool_exp 'Then' func_body)*
    ('Else' func_body)?
    'EndIf' FS;

for_stm: 'For'(ID EQ exp CM bool_exp CM assign) 'Do'
    func_body
    'EndFor' FS;

while_stm: 'While' bool_exp 'Do' func_body 'EndWhile' FS;

do_while: 'Do' func_body 'While' bool_exp 'EndDo' FS;

break_stm: 'Break';

continue_stm: 'Continue';

int_cor:        'int_of_float' LP int_exp RP
            |   'int of string' LP STRING_LIT RP;

float_cor:      'float_of_int' LP float_exp RP
            |   'float_of_string' LP STRING_LIT RP;

string_cor:     'string_of_int' LP int_exp RP
            |   'string_of_float' LP float_exp RP
            |   'string_of_bool' LP BOOL_LIT RP;

bool_cor:       'bool_of_string' LP STRING_LIT RP;

int_exp:            int_exp2 INT_AR_OP int_exp
                |   int_exp2;

int_exp2:           LP int_exp RB
                |   INT_LIT | ID | array_elm_id | func_call | int_cor;

float_exp:          float_exp2 FLOAT_AR_OP float_exp
                |   float_exp2;

float_exp2:         LP float_exp RB
                |   FLOAT_LIT | ID | array_elm_id | func_call | float_cor;

exp:        int_exp
        |   float_exp;

bool_exp:   float_exp FLOAT_RL_OP float_exp
        |   int_exp INT_RL_OP int_exp
        |   bool_exp2 LOGIC bool_exp
        |   NEGA bool_exp2
        |   bool_exp2;
bool_exp2:  LP bool_exp RP
        |   BOOL_LIT | ID | array_elm_id | func_call | bool_cor;

statement:  (var_decl|assign|func_call|return_stm|break_stm|continue_stm)SM
            |if_stm|for_stm|while_stm|do_while;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;