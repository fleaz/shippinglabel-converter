# shippinglabel-converter

The initial reason for this project was the fact that you only get A4 labels from DHL if you are a privat customer. If
you are a business custommer you can get your shipping labels in the classic 4"x6" (100x150mm) format to print them
directly on something like a thermal label printer. Because I'm a privat customer but have such a fancy printer, I
needed a way to modify the A4 label I get from DHL and turn them into a smaller format. It's basically the same idea as
https://www.paketikett.de/, but this page is limited to only 62mm labels as output.

For ease of use this will get a simple web interface.

## Supported conversions
  * DHL Paketlabel DIN A4 -> 100x150mm

Adding more should be easy. Just open an issue and provide a sample PDF from the original format (Delete PII beforehand)
