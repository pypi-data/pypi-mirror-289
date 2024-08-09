---
tags: [gradio-custom-component, SimpleTextbox]
title: gradio_uni_view_ocl
short_description: 
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_uni_view_ocl`
<a href="https://pypi.org/project/gradio_uni_view_ocl/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_uni_view_ocl"></a>  

Python library for easily interacting with trained machine learning models

## Installation

```bash
pip install gradio_uni_view_ocl
```

## Usage

```python

import gradio as gr
from gradio_uni_view_ocl import uni_view_ocl

mol = """1a
     RDKit          3D

 27 29  0  0  1  0  0  0  0  0999 V2000
  -15.3524  -19.2206  -25.9684 C   0  0  0  0  0  0  0  0  0  0  0  0
  -14.6526  -19.7081  -27.0823 C   0  0  0  0  0  0  0  0  0  0  0  0
  -15.8555  -20.1235  -25.0241 C   0  0  0  0  0  0  0  0  0  0  0  0
  -14.4541  -21.0636  -27.2485 C   0  0  0  0  0  0  0  0  0  0  0  0
  -15.6357  -21.4854  -25.1840 C   0  0  0  0  0  0  0  0  0  0  0  0
  -15.0526  -16.9445  -26.6871 N   0  0  0  0  0  0  0  0  0  0  0  0
  -14.9347  -21.9631  -26.2988 C   0  0  0  0  0  0  0  0  0  0  0  0
  -15.2162  -15.5610  -26.5929 C   0  0  0  0  0  0  0  0  0  0  0  0
  -15.9031  -15.0059  -25.5037 C   0  0  0  0  0  0  0  0  0  0  0  0
  -15.4462  -12.8187  -26.3599 C   0  0  0  0  0  0  0  0  0  0  0  0
  -14.7773  -13.3552  -27.4525 C   0  0  0  0  0  0  0  0  0  0  0  0
  -16.0203  -13.6235  -25.3815 C   0  0  0  0  0  0  0  0  0  0  0  0
  -14.6768  -14.7359  -27.5934 C   0  0  0  0  0  0  0  0  0  0  0  0
  -16.5313  -15.9392  -24.4895 C   0  0  0  0  0  0  0  0  0  0  0  0
  -16.2584  -17.2435  -24.7671 N   0  0  0  0  0  0  0  0  0  0  0  0
  -15.5317  -17.7669  -25.8203 C   0  0  0  0  0  0  0  0  0  0  0  0
  -17.2406  -15.6098  -23.5374 O   0  0  0  0  0  0  0  0  0  0  0  0
  -14.2525  -19.0464  -27.8382 H   0  0  0  0  0  0  0  0  0  0  0  0
  -16.3981  -19.7943  -24.1510 H   0  0  0  0  0  0  0  0  0  0  0  0
  -13.8938  -21.4078  -28.1049 H   0  0  0  0  0  0  0  0  0  0  0  0
  -15.9903  -22.1635  -24.4209 H   0  0  0  0  0  0  0  0  0  0  0  0
  -14.3604  -12.6891  -28.1964 H   0  0  0  0  0  0  0  0  0  0  0  0
  -16.5458  -13.1713  -24.5494 H   0  0  0  0  0  0  0  0  0  0  0  0
  -16.7352  -17.8915  -24.1540 H   0  0  0  0  0  0  0  0  0  0  0  0
  -14.1941  -15.1755  -28.4537 H   0  0  0  0  0  0  0  0  0  0  0  0
  -15.5319  -11.7476  -26.2520 H   0  0  0  0  0  0  0  0  0  0  0  0
  -14.7660  -23.0224  -26.4244 H   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  2  0
  1  3  1  0
  1 16  1  0
  2  4  1  0
  2 18  1  0
  3  5  2  0
  3 19  1  0
  4  7  2  0
  4 20  1  0
  5  7  1  0
  5 21  1  0
  6  8  1  0
  6 16  2  0
  7 27  1  0
  8  9  2  0
  8 13  1  0
  9 12  1  0
  9 14  1  0
 10 11  1  0
 10 12  2  0
 10 26  1  0
 11 13  2  0
 11 22  1  0
 12 23  1  0
 13 25  1  0
 14 15  1  0
 14 17  2  0
 15 16  1  0
 15 24  1  0
M  END
"""

with gr.Blocks() as demo:
    # view = uni_view_ocl(smiles="[C@](S)(C)(N)O", editMode=False)
    view = uni_view_ocl(mol=mol, editMode=False, width=240, height=180)
    update_btn = gr.Button('Update')
    def update_smiles():
        return uni_view_ocl(smiles="c1cc2ccccc2cc1")
    update_btn.click(update_smiles, outputs=view)
    print_btn = gr.Button('Print')
    def print_smiles(smiles):
        print(smiles)
    print_btn.click(print_smiles, inputs=view)

if __name__ == "__main__":
    demo.launch()

```

## `uni_view_ocl`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
str | Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">default text to provide in textbox. If callable, the function will be called whenever the app loads to set the initial value of the component.</td>
</tr>

<tr>
<td align="left"><code>placeholder</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">placeholder hint to provide behind textbox.</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">component name in interface.</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will display label.</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int
```

</td>
<td align="left"><code>160</code></td>
<td align="left">minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if True, will be rendered as an editable textbox; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will be hidden.</td>
</tr>

<tr>
<td align="left"><code>rtl</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>False</code></td>
<td align="left">If True and `type` is "text", sets the direction of the text to right-to-left (cursor appears on the left of the text). Default is False, which renders cursor on the right.</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">if assigned, will be used to assume identity across a re-render. Components that have the same key across a re-render will have their value preserved.</td>
</tr>

<tr>
<td align="left"><code>width</code></td>
<td align="left" style="width: 25%;">

```python
int | str
```

</td>
<td align="left"><code>"800px"</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>height</code></td>
<td align="left" style="width: 25%;">

```python
int | str
```

</td>
<td align="left"><code>"480px"</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>smiles</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>mol</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>editMode</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `change` | Triggered when the value of the uni_view_ocl changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input. |
| `input` | This listener is triggered when the user changes the value of the uni_view_ocl. |
| `submit` | This listener is triggered when the user presses the Enter key while the uni_view_ocl is focused. |



### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As output:** Is passed, passes text value as a {str} into the function.
- **As input:** Should return, expects a {str} returned from function and sets textarea value to it.

 ```python
 def predict(
     value: str | None
 ) -> str | None:
     return value
 ```
 
