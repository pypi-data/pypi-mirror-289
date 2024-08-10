# devwer

`devwer` is a Python package to calculate Word Error Rate (WER) for Nepali language text.

## Installation

You can install the package using pip:

```
pip install devwer
```

## Usage

```python
from devwer import DevWordErrorRate

reference_sentence = "नेपाली भाषा धेरै मीठो छ।"
hypothesis_sentence = "नेपाली भाषा धेरै मिठो छ।"
dwer_calculator = DevWordErrorRate()
wer = dwer_calculator.wer(reference_sentence, hypothesis_sentence)
print(f"Word Error Rate: {wer:.2f}")
```

## License

This project is licensed under the MIT License.
