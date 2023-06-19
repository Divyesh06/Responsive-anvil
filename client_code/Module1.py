import anvil

mobile_funcs={}
pc_funcs={}

original_open=anvil.open_form

def on_mobile(func):
    func_form=func.__module__.split('.')[-1]
    mobile_funcs[func_form]=func

def on_pc(func):
    func_form=func.__module__.split('.')[-1]
    pc_funcs[func_form]=func

def new_open_form(form,*args,**kwargs):
    print('New Open Form')
    original_open(form,*args,**kwargs)

def raise_all_mobile():
    all_mobile_funcs=mobile_funcs.values()
    for i in all_mobile_funcs:
        i()