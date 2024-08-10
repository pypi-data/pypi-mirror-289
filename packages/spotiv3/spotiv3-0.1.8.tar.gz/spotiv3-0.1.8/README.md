# Spotiv3

A Python module for bypassing reCAPTCHA v3.

## Installation

You can install this package via pip:

```python
from spotiv3 import RecaptchaV3

recaptcha = RecaptchaV3()
token = recaptcha.recaptchav3_bypass()
print("Bypassed RecaptchaV3:", token)