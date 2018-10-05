# String

|Function Name| Description|
|:---|:---|
|charAt(index: number): string; |Return the character at the specified index.@param index The zero-based index of the desired character.|
|charCodeAt(index: number): number; |   length: number;Return the Unicode value of the character at the specified location.@param index The zero-based index of the desired character. If there is no character at the specified index, NaN is returned.|
|compare(that: string): number; |See how the order of characters in two strings is different (in ASCII encoding).@param that String to compare to target string|
|concat(other: string): string; |Returns a string that contains the concatenation of two or more strings.@param other The string to append to the end of the string.|
|includes(searchValue: string, start?: number): boolean; |Determines whether a string contains the characters of a specified string.@param searchValue the text to find@param start optional start index for the search|
|indexOf(searchValue: string, start?: number): number; |   isEmpty(): boolean;Returns the position of the first occurrence of a specified value in a string.@param searchValue the text to find@param start optional start index for the search|
|substr(start: number, length?: number): string; |Return a substring of the current string.@param start first character index; can be negative from counting from the end, eg:0@param length number of characters to extract|
