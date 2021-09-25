package main

import "fmt"

const spanish = "spanish"
const french = "french"
const englishHelloPrefix = "Hello, "
const spanishHelloPrefix = "Hola, "
const frenchHelloPrefix = "Bonjour, "

func Hello(name string, language string) string {
	switch language {
	case spanish:
		if name == "" {
			name = "Mundo"
		}

		return spanishHelloPrefix + name
	case french:
		if name == "" {
			name = "Mundouoi"
		}

		return frenchHelloPrefix + name
	default:
		if name == "" {
			name = "World"
		}
		return englishHelloPrefix + name
	}
}

func main() {
	fmt.Println(Hello("world", "english"))
}
