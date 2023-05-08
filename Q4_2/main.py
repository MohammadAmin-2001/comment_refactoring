'''
My name is Mohammad Amin Geramimehr
My student_ID is 98521441
MY Phone numbere is 09903003723
'''






from antlr4 import *
from gen.JavaLexer import JavaLexer
import os


def main(address_input,address_output):



    file_stream = FileStream(r"" + address_input)


    if os.path.exists(address_output):
        os.remove(address_output)

    with open(address_output, 'a',encoding = 'utf-8', newline="\n") as f:
        comment_=""
        start=0
        iscommentempty=1
        lexer=JavaLexer(file_stream)
        token=lexer.nextToken()
        while token.type != token.EOF:
            text=token.text
            if token.type == lexer.COMMENT:

                if "\n" not in text:
                    iscommentempty = 0
                    text = "//"+text[2:-2]
                    comment_=text
                    start=1

                elif start == 0:
                    iscommentempty = 0
                    text = "//"+(str(text).split("\n")[0])[2:]
                    comment_ = text
                    start = 1

            elif token.type == lexer.LINE_COMMENT and start == 0:
                iscommentempty = 0
                comment_ = text
                start = 1

            elif text=="\r\n":
                comment_+=text

            elif not iscommentempty:
                    start=0
                    f.write(comment_)
                    f.write(text)
                    comment_=""
                    iscommentempty=1
            else:
                f.write(text)




            token = lexer.nextToken()



if __name__ == '__main__':
   input_address = input("Enter input address:")
   main(input_address+'.java', "Result.java")
   print("Refactoring successfully")


