# Button

|Function Name| Description|
|:---|:---|
|id(): int32; |Gets the component identifier for the buton|
|isPressed(): boolean; |Check if a button is pressed or not.@param button the button to query the request|
|onEvent(ev: ButtonEvent, body: () => void): void; |Do something when a button (`A`, `B` or both `A` + `B`) is clicked, double clicked, etc...	@param button the button that needs to be clicked or used	@param event the kind of button gesture that needs to be detected	@param body code to run when the event is raised	|
|wasPressed(): boolean; |See if the button was pressed again since the last time you checked.@param button the button to query the request|
