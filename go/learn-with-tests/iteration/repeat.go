package iteration

// Repeat repeats the provided character, char, amt times.
func Repeat(char string, amt int) string {
	var repeated string

	for i := 0; i < amt; i++ {
		repeated += char
	}

	return repeated
}
