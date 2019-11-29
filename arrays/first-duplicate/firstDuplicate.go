package duplicate

func firstDuplicate(a []int) int {
	for _, v := range a {
		if v < 0 {
			v = -v
		}
		if a[v-1] > 0 {
			a[v-1] = -a[v-1]
		} else {
			return v
		}
	}
	return -1
}
