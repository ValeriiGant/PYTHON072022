import views
import calc

def calc(a: int, b: int, operation: str) ->float:
    a=view.input_num ()
    b=view.input_num ()
    operation = view.input_num ()
    match operation:
        case "+":
            return calc.sum (a,b)