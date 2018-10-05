# Array

|Function Name| Description|
|:---|:---|
|every(callbackfn: (value: T, index: number) => boolean): boolean; |Tests whether all elements in the array pass the test implemented by the provided function.@param callbackfn A function that accepts up to two arguments. The every method calls the callbackfn function one time for each element in the array.|
|filter(callbackfn: (value: T, index: number) => boolean): T[]; |Return the elements of an array that meet the condition specified in a callback function.@param callbackfn A function that accepts up to two arguments. The filter method calls the callbackfn function one time for each element in the array.|
|forEach(callbackfn: (value: T, index: number) => void): void; |Call a defined callback function on each element of an array.@param callbackfn A function that accepts up to two arguments. The forEach method calls the callbackfn function one time for each element in the array.|
|get(index: number): T; |Get the value at a particular index@param index the zero-based position in the list of the item, eg: 0|
|indexOf(item: T, fromIndex?: number): number; |Return the index of the first occurrence of a value in an array.@param item The value to locate in the array.@param fromIndex The array index at which to begin the search. If fromIndex is omitted, the search starts at index 0.|
|insertAt(index: number, value: T): void; |Insert the value at a particular index, increases length by 1@param index the zero-based position in the list to insert the value, eg: 0@param the value to insert, eg: 0|
|join(sep: string): string; |joins all elements of an array into a string and returns this string.@param sep the string separator|
|length: number; |Get or set the length of an array. This number is one more than the index of the last element the array.|
|map<U>(callbackfn: (value: T, index: number) => U): U[]; |Call a defined callback function on each element of an array, and return an array containing the results.@param callbackfn A function that accepts up to two arguments. The map method calls the callbackfn function one time for each element in the array.|
|pop(): T; |Remove the last element from an array and return it.|
|push(item: T): void; |Append a new element to an array.@param items New elements of the Array.|
|reduce<U>(callbackfn: (previousValue: U, currentValue: T, currentIndex: number) => U, initialValue: U): U; |Call the specified callback function for all the elements in an array. The return value of the callback function is the accumulated result, and is provided as an argument in the next call to the callback function.@param callbackfn A function that accepts up to three arguments. The reduce method calls the callbackfn function one time for each element in the array.@param initialValue Initial value to start the accumulation. The first call to the callbackfn function provides this value as an argument instead of an array value.|
|removeAt(index: number): T; |   removeElement(element: T): boolean;|
|reverse(): void; |Reverse the elements in an array. The first array element becomes the last, and the last array element becomes the first.|
|set(index: number, value: T): void; |Store a value at a particular index@param index the zero-based position in the list to store the value, eg: 0@param the value to insert, eg: 0|
|shift(): T; |Remove the first element from an array and return it. This method changes the length of the array.|
|slice(start: number, end: number): T[]; |Return a section of an array.@param start The beginning of the specified portion of the array. eg: 0@param end The end of the specified portion of the array. eg: 0|
|some(callbackfn: (value: T, index: number) => boolean): boolean; |Tests whether at least one element in the array passes the test implemented by the provided function.@param callbackfn A function that accepts up to two arguments. The some method calls the callbackfn function one time for each element in the array.|
|sort(callbackfn?: (value1: T, value2: T) => number): T[]; |Sort the elements of an array in place and returns the array. The sort is not necessarily stable.@param specifies a function that defines the sort order. If omitted, the array is sorted according to the prmitive type|
|splice(start: number, deleteCount: number): void; |Remove elements from an array.@param start The zero-based location in the array from which to start removing elements. eg: 0@param deleteCount The number of elements to remove. eg: 0|
|unshift(value: T): number; |Add one element to the beginning of an array and return the new length of the array.@param element to insert at the start of the Array.|
