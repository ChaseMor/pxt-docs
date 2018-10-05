# Buffer

|Function Name| Description|
|:---|:---|
|getNumber(format: NumberFormat, offset: int32): number; |Read a number in specified format from the buffer.|
|shift(offset: int32, start?: int32, length?: int32): void; |Shift buffer left in place, with zero padding.@param offset number of bytes to shift; use negative value to shift right@param start start offset in buffer. Default is 0.@param length number of elements in buffer. If negative, length is set as the buffer length minusstart. eg: -1|
|rotate(offset: int32, start?: int32, length?: int32): void; |Rotate buffer left in place.@param offset number of bytes to shift; use negative value to shift right@param start start offset in buffer. Default is 0.@param length number of elements in buffer. If negative, length is set as the buffer length minusstart. eg: -1|
|setNumber(format: NumberFormat, offset: int32, value: number): void; |Write a number in specified format in the buffer.|
|toHex(): string; |Convert a buffer to its hexadecimal representation.|
|write(dstOffset: int32, src: Buffer): void; |Write contents of `src` at `dstOffset` in current buffer.|
|fill(value: int32, offset?: int32, length?: int32): void; |   //% property shim=BufferMethods::length   length: int32;Fill (a fragment) of the buffer with given value.|
|slice(offset?: int32, length?: int32): Buffer; |Return a copy of a fragment of a buffer.|
