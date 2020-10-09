import cerberus

def erros_print(v):
    if v.errors != {}:
        print(v.errors)



def create_new_account(body):
    v = cerberus.Validator()
    schema = {
            "currency" : {"type" : "string", "minlength": 3}
        }
    v.validate(body, schema)
    erros_print(v)
  

