import anvil

mobile_funcs=[]
pc_funcs={}

original_open=anvil.open_form

def on_mobile(func):
    mobile_funcs.append(func)
    def inner(self):
        print('LOL')
    return inner
    
def on_pc(func):
    func_form=func.__module__.split('.')[-1]
    pc_funcs[func_form]=func

def new_open_form(form,*args,**kwargs):
    print('New Open Form')
    original_open(form,*args,**kwargs)

def raise_all_mobile():
    for i in mobile_funcs:
        i()