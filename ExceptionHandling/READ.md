

Exception Handling in Python | Python for AI #67


# Exception Handling in Python
- There are 2 stages where error may happen in a program

        - During compliation -> Syntax Error
        - During execution -> Exceptions 

## Syntax Error 

- Something in the program is not written according to the program grammar.
- Error is raised by the interpreter / compiler
- You can solve it by rectifying the program


## Exception 
- if things go wrong during the execution of the program(runtime). It generally happens when something unforeseen has happened
- Exception are rised by python runtime (runtime error)
- You have to takle is on the fly

#### Examples:
- Memory overflow
- Divide by - -> logical error
- Database error

<br>
<hr>
- why is it important to handle exceptions?
- How to handle exception - > Try except block
<br>
 - load big data is your system it will show error | it is runtime error 
 - you connect data base of sql . sql server connection is error. your program is good but connection is error it is called runtime error.
- there are somthing going on, but cod is good.
- you will see error message of name and line (ZeroDivisionError: division by zero) | it will break the security  so we need custome message 
- I don't want to show these kind of message. I will write my custom message.

- code:
```
try:
    with open("files/sample4.txt", 'r') as f:  
        read = f.read()
        print(read)
except:
    print("File not found")
```