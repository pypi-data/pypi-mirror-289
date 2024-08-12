import streamlit.components.v1 as components
import os

# _RELEASE = False

# if not _RELEASE:
#     _component_func = components.declare_component(
#         "st_txt_copybutton",
#         url="http://localhost:3000",
#     )
# else:
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/build")
_component_func = components.declare_component("st_txt_copybutton", path=build_dir)

def txt_copy(label: str, text_to_copy: str, key=None):
    component_value = _component_func(label=label, text_to_copy=text_to_copy, key=key, default=None)
    return component_value