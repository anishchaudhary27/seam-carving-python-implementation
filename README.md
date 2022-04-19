# Seam Carving for Content-Aware Image Resizing Python Implementation
Seam carving is an algorithm that can be used to resize images. But instead of cropping or squeezing images, it removes blank spaces and brings important objects closer.

Based on Seam carving Algorithm discussed in [this paper](https://www.researchgate.net/publication/215721610_Seam_Carving_for_Content-Aware_Image_Resizing)

### Original image (width - 807px)
![Original image (width - 807px)](/sample.jpg)

### Resized image (width - 600px)
![Resized image (width - 680px)](/sample_result.jpg)

## Future plans
My plan is to implement this algorithm in c++ and optimize the code. Currently python implementation takes a long time to process an image (even for a medium sized image). And then compile it into webassembly and release as a npm package.
