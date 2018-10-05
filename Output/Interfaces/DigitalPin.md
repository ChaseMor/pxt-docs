# DigitalPin

|Function Name| Description|
|:---|:---|
|onEvent(event: PinEvent, body: () => void): void; |Register code to run when a pin event occurs. |
|digitalWrite(value: boolean): void; |Set a pin or connector value to either 0 or 1.@param name pin to write to@param value value to set on the pin|
|setPull(pull: PinPullMode): void; |Set the pull direction of this pin.@param name pin to set the pull mode on@param pull one of the mbed pull configurations: PullUp, PullDown, PullNone|
|pushButton(): Button; |Get the push button (connected to GND) for given pin|
|pulseIn(value: PulseValue, maxDuration?: int32): int32; |Return the duration of a pulse in microseconds@param name the pin which measures the pulse@param value the value of the pulse (default high)@param maximum duration in micro-seconds|
|digitalRead(): boolean; |Read a pin or connector as either 0 or 1@param name pin to read from|
|onPulsed(pulse: PulseValue, body: () => void): void; |Make this pin a digital input, and create events where the timestamp is the durationthat this pin was either ``high`` or ``low``.|
