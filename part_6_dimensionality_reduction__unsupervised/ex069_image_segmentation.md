# ex069: Image Segmentation with K-Means

### Concept
Color Segmentation: grouping pixels with similar colors. 

### Implementation
1. Reshape the image into a long list of RGB triplets (e.g., [255, 0, 0]).
2. Run K-Means with $K=8$.
3. Replace every pixel's color with the color of its cluster's centroid.
4. Reshape back to the original image dimensions.

### Result
This significantly reduces the number of colors in the image while preserving the overall structure.
