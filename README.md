# Sean Carving for Content-Aware Image Resizing Python Implementation
Sean carving is an algorithm that can be used to resize images. But instead of cropping or squeezing images, it removes blank spaces and brings important objects closer.

Based Sean carving Algorithm discussed in [this research paper](https://www.researchgate.net/publication/215721610_Seam_Carving_for_Content-Aware_Image_Resizing)

### Original image (width - 807px)
![Original image (width - 807px)](/sample.jpg)

### Resized image (width - 600px)
![Resized image (width - 600px)](/sample.jpg_result.jpg)

## Future plans
My plan is to implement this algorithm in c++ and optimize the code. Currently python implementation takes a long time to process, even for medium sized images. And may be compile it in webassembly and deploy it as a web apps.
