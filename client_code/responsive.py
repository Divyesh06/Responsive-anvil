from anvil.js import window

import anvil
from anvil.js import get_dom_node

def set(self, property_name, property_value,important=False):
    if important:
        priority='important'
    else:
        priority='undefined'
    get_dom_node(self).setProperty(property_name,property_value,priority)

anvil.Component.set=set
        
current_mode='mobile'
mobile_width_threshold=768
forms=[]

def form(form):
    original_init=form.__init__
    def __init__(self,**properties):
        original_init(self,**properties)
        forms.append(self)
        if current_mode=='pc':
            self.on_pc()
        else:
            self.on_mobile()

    form.__init__=__init__
    return form

def switch_to_mobile():
    global current_mode
    current_mode='mobile'
    for form in forms:
        if getattr(form,'on_mobile'):
            form.on_mobile()

def switch_to_pc():
    global current_mode
    current_mode='pc'
    for form in forms:
        if hasttr(form,'on_pc'):
            form.on_pc()

def on_resize(*args):
    if current_mode == 'mobile' and window.innerWidth>mobile_width_threshold:
        switch_to_pc()

    elif current_mode == 'pc' and window.innerWidth < mobile_width_threshold:
        switch_to_mobile()

on_resize()

window.addEventListener('resize',on_resize)