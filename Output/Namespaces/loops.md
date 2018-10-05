# loops

|Function Name| Description|
|:---|:---|
|pause(ms: int32): void |Pause for the specified time in milliseconds@param ms how long to pause for, eg: 100, 200, 500, 1000, 2000|
|forever(a: () => void): void |Repeats the code forever in the background. On each iteration, allows other codes to run.@param body code to execute|
