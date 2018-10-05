# PwmOnlyPin

|Function Name| Description|
|:---|:---|
|analogSetPeriod(period: int32): void; |Set the Pulse-width modulation (PWM) period of the analog output. The period is in**microseconds** or `1/1000` milliseconds.If this pin is not configured as an analog output (using `analog write pin`), the operation hasno effect.@param name analog pin to set period to@param micros period in micro seconds. eg:20000|
|servoSetPulse(duration: int32): void; |Set the pin for PWM analog output, make the period be 20 ms, and set the pulse width.The pulse width is based on the value it is given **microseconds** or `1/1000` milliseconds.@param name pin name@param duration pulse duration in micro seconds, eg:1500|
|servoWrite(value?: int32): void; |Write a value to the servo to control the rotation of the shaft. On a standard servo, this willset the angle of the shaft (in degrees), moving the shaft to that orientation. On a continuousrotation servo, this will set the speed of the servo (with ``0`` being full-speed in onedirection, ``180`` being full speed in the other, and a value near ``90`` being no movement).@param name pin to write to@param value angle or rotation speed|
