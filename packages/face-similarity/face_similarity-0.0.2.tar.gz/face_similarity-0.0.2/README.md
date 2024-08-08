# Person Image Verification Package

## Overview
The Person Image Verification Package allows users to upload a document containing an image of a person and an original image of a person. It then determines whether the person in both images is the same or different. This package leverages advanced image processing and machine learning techniques to provide accurate results.
A package to compare face similarity using HOG features and cosine similarity.

## Features
- Image Upload: Upload any document containing an image of a person.
- Original Image Comparison: Upload an original image of the person for comparison.
- Verification: Determine whether the person in both images is the same or different.
- Easy Integration: Simple and straightforward integration into any project.

## Installation
`pip install Face_Similarity`

## Example Usage
```python
from face_similarity.similarity import compare_faces

image_path_1 = 'path/to/Document_image.jpg'
image_path_2 = 'path/to/original_image.jpg'

result = compare_faces(image_path_1, image_path_2)
print(result)

