# Responsive for Anvil

A tiny package that can make responsive apps easier to build

## Clone Link

https://anvil.works/build#clone:WDRFETMX63QKCM4J=55K3VSEFL3PVEJLQJZHBLTZQ

## Usage

Add a decorator to your form

```python

from responsive import responsive

@responsive.form
class Form1(Form1Template):
     ...

```

And then, you can add two methods, to your form, on_mobile and on_pc.

```python
def on_mobile(self):
    self.label_1.spacing_above='small'
    #Any other changes to your components or general code

def on_pc(self):
    self.label_1.spacing_above='large'
    #Any other changes to your components or general code
```

That way, you can specify separate code to be run depending on whether the user is using mobile or a larger device (laptop, desktop, tablets). You can also specify the width threshold (Default is 768px)

```python
from responsive import responsive

responsive.pc_width_threshold = 600 
#Now, any device having more than 600px will be treated as PC
```

## Example App

https://anvil.works/build#clone:GWEMD2FVKV3K7WXH=O3LIKURLKDFW3Y6EP5IPSJSH%7CWDRFETMX63QKCM4J=55K3VSEFL3PVEJLQJZHBLTZQ
