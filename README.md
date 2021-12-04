# Sean carving python implementation
Sean carving is an algorithm that can be used to resize images. But instead of cropping and squezing images, it removes blank spaces in thhe images and bring important objects closer.

This Implementation of Sean carving implementation discussed in [this paper](https://www.researchgate.net/publication/215721610_Seam_Carving_for_Content-Aware_Image_Resizing)

### Original image (width - 807px)
![Original image (width - 807px)](/sample.jpg)

### Resized image (width - 600px)
![Resized image (width - 600px)](/sample.jpg_result.jpg)

## Future plans
My plan is to implement this algorithm in c++ and optimize the code. Currently python implementation takes a long time to process, even for medium sized images. And may be compile it in webassembly and deploy it as a web apps.