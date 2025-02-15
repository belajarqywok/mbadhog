func isValid(s string) bool {
  	// Mapping bracket pairs
	bracketMap := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}

	// Stack buat nyimpen karakter pembuka
	stack := []rune{}

 	 // nilai s = "[()]"
	for _, char := range s {
		// Jika karakter adalah closing bracket
		// iter 1 -> [ -> open: kosong, found: false; stack -> []
		// iter 2 -> ( -> open: kosong, found: false; stack -> ["["]
		// iter 3 -> ) -> open: "(", found: true; stack -> ["[", "("]
		if open, found := bracketMap[char]; found {
			// Cek apakah stack kosong atau top-nya bukan pasangan yang sesuai
			// iter 3 -> stack[len(stack) - 1] = stack[2 - 1] = "(" == open "(" -> cocok
			// iter 4 -> stack[len(stack) - 1] = stack[1 - 1] = "[" == open "[" -> cocok
			if len(stack) == 0 || stack[len(stack)-1] != open {
				return false
			}
			// Pop dari stack
			// iter 3 -> stack = stack[:len(stack)-1] = stack[:2 - 1]; stack sebelum pop ["[", "("] -> setelah pop ["["]
			// iter 4 -> stack = stack[:len(stack)-1] = stack[:1 - 1]; stack sebelum pop ["["] -> setelah pop []
			stack = stack[:len(stack)-1]
		} else {
			// Jika karakter adalah opening bracket, push ke stack
			// iter 1 -> "[" masuk -> stack jadi ["["]
			// iter 2 -> "(" masuk -> stack jadi ["[", "("]
			stack = append(stack, char)
		}
	}

	// Kalau stack kosong di akhir, berarti valid
	// karena sisa [], berarti len(stack) = 0; berarti true
	return len(stack) == 0
}
