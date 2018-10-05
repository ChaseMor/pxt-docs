# control

|Function Name| Description|
|:---|:---|
|__log(text: string): void ||
|allocateNotifyEvent(): int32 |Allocates the next user notification event|
|createBuffer(size: int32): Buffer |Create a new zero-initialized buffer.@param size number of bytes in the buffer|
|deviceDalVersion(): string |Determine the version of system software currently running.|
|deviceSerialNumber(): int32 |Derive a unique, consistent serial number of this device from internal data.|
|dmesgPtr(str: string, ptr: Object): void |   function dmesg(s: string): void;|
|internalOnEvent(src: int32, value: int32, handler: () => void, flags?: int32): void |Used internally|
|millis(): int32 |Gets the number of milliseconds elapsed since power on.|
|raiseEvent(src: int32, value: int32): void |Announce that an event happened to registered handlers.@param src ID of the MicroBit Component that generated the event@param value Component specific code indicating the cause of the event.|
|reset(): void |Reset the device.|
|runInParallel(a: () => void): void |Run other code in the parallel.|
|waitForEvent(src: int32, value: int32): void |Blocks the calling thread until the specified event is raised.|
|waitMicros(micros: int32): void |Block the current fiber for the given microseconds@param micros number of micro-seconds to wait. eg: 4|
