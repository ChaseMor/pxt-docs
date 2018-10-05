# pins

|Function Name| Description|
|:---|:---|
|createBuffer(size: int32): Buffer |Create a new zero-initialized buffer.@param size number of bytes in the buffer|
|i2cReadBuffer(address: int32, size: int32, repeat?: boolean): Buffer |Read `size` bytes from a 7-bit I2C `address`.|
|i2cWriteBuffer(address: int32, buf: Buffer, repeat?: boolean): int32 |Write bytes to a 7-bit I2C `address`.|
|pulseDuration(): int32 |Get the duration of the last pulse in microseconds. This function should be called from a``onPulsed`` handler.|
|spiFrequency(frequency: int32): void |Sets the SPI frequency@param frequency the clock frequency, eg: 1000000|
|spiMode(mode: int32): void |Sets the SPI mode and bits@param mode the mode, eg: 3|
|spiTransfer(command: Buffer, response: Buffer): void |Writes a given command to SPI bus, and afterwards reads the response.|
|spiWrite(value: int32): int32 |Write to the SPI slave and return the response@param value Data to be sent to the SPI slave|
