# music

|Function Name| Description|
|:---|:---|
|setTone(buffer: Buffer): void |Set a source of digital sound data (PCM) for making tones.Samples are 1024 x 10bit unsigned PCM.A reference to the buffer is kept to avoid the memory overhead, so changes to the buffervalues are reflected immediately to the sound output.|
|playTone(frequency: int32, ms: int32): void |Play a tone through the speaker for some amount of time.@param frequency pitch of the tone to play in Hertz (Hz), eg: Note.C@param ms tone duration in milliseconds (ms), eg: BeatFraction.Half|
|setVolume(volume: int32): void |Set the output volume of the sound synthesizer.@param volume the volume 0...256, eg: 128|
