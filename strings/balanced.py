def is_balanced(text):
    val = sum([1 if c == '(' else -1 if c == ')' else 0 for c in text])
    return val == 0

def is_balanced2(text):
    stack = []
    for c in text:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

def valid_ip(ip):
    digits = ip.split('.')
    return len(digits) == 4 and \
            all([d.isdigit() and 0 <= int(d) <= 255 for d in digits])

def reverse(text):
    rev_starts = []
    chars = list(text)
    for idx, c in enumerate(chars):
        if c == '(':
            rev_starts.append(idx)
        elif c == ')':
            start = rev_starts.pop()
            chars[start:idx] = chars[start:idx][::-1]
    clean = filter(lambda c: c not in "()", chars)
    return ''.join(clean[::-1])

if __name__ == '__main__':
    print(reverse('hola')) # aloh
    print(reverse('hola(123)')) # hola321 -> 123aloh
    print(reverse('h(ola)')) # halo -> olah
    print(reverse('(ho)(la)')) # ohal -> laho
    print(reverse('(ho(la) (querido)) (am(ig)o)')) # (hoal odireuq) (amigo) -> querido laoh ogima -> amigo hoal odireuq
    print(reverse('(hola) (querido) (amigo)')) # aloh odireuq ogima -> amigo querido hola
