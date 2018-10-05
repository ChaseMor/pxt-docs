# Image

|Function Name| Description|
|:---|:---|
|isMono: boolean; |True iff the image is monochromatic (black and white)|
|scroll(dx: int32, dy: int32): void; |Every pixel in image is moved by (dx,dy)|
|transposed(): Image; |Returns a transposed image (with X/Y swapped)|
|flipY(): void; |Flips (mirrors) pixels vertically in the current image|
|flipX(): void; |Flips (mirrors) pixels horizontally in the current image|
|clone(): Image; |Return a copy of the current image|
|overlapsWith(other: Image, x: int32, y: int32): boolean; |Check if the current image "collides" with another|
|drawTransparentImage(from: Image, x: int32, y: int32): void; |Draw given image with transparent background on the current image|
|height: int32; |Get the height of the image|
|fill(c: int32): void; |Fill entire image with a given color|
|setPixel(x: int32, y: int32, c: int32): void; |Set pixel color|
|doubled(): Image; |Stretches the image in both directions by 100%|
|doubledY(): Image; |Stretches the image vertically by 100%|
|copyFrom(from: Image): void; |Sets all pixels in the current image from the other image, which has to be of the same size andbpp.|
|doubledX(): Image; |Stretches the image horizontally by 100%|
|getPixel(x: int32, y: int32): int32; |Get a pixel color|
|drawImage(from: Image, x: int32, y: int32): void; |Draw given image on the current image|
|width: int32; |Get the width of the image|
|replace(from: int32, to: int32): void; |Replaces one color in an image with another|
