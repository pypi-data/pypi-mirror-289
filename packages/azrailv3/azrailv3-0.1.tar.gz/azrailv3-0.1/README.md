# azrailv3

A module to bypass reCAPTCHA v3 challenges.

## Installation

You can install the package via pip:

```bash
pip install azrailv3


from azrailv3.bypass import ReCaptchaV3Bypass

url = "https://example.com"
bypasser = ReCaptchaV3Bypass(url)
gtk_token = bypasser.bypass()
print(gtk_token)