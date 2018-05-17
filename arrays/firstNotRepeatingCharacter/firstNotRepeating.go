func firstNotRepeatingCharacter(s string) rune {
  var hist [26]uint32
  order := make([]rune, 0, 26)

  for _, c := range s {
    if hist[c - 'a'] == 0 {
      order = append(order, c)
    }
    hist[c - 'a'] += 1
  }

  for _, c := range order {
    if hist[c - 'a'] == 1 {
      return c
    }
  }
  return '_'
}
