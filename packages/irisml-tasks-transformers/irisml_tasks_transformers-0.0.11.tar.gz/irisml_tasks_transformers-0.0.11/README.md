# irisml-tasks-transformers

This is a MLTest task package for Huggingface's transformers package.

For the detail of IrisML framework, visit [irisml repository](https://github.com/microsoft/irisml)

# Tasks
## create_transformers_model
Create a model using transformers library. Currently only CLIPModel is supported.
```python
class Config:
    name: str
    pretrained: bool = False

class Outputs:
    model: torch.nn.Module
```

## create_transformers_tokenizer
Create a tokenizer using transformers library.
```python
class Config:
    name: str

class Outputs:
    tokenizer: typing.Callable
```
