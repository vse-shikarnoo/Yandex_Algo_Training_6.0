n = int(input())
lines = [list(input()) for _ in range(n)]

i = 0
while i + 1 < len(lines):
    if lines[i] == lines[i+1]:
        lines.pop(i)
    else:
        i += 1

i = 0
while i + 1 < len(lines[0]):
    if [lines[j][i] for j in range(len(lines))] ==\
        [lines[j][i+1] for j in range(len(lines))]:
        for j in lines:
            j.pop(i)
    else:
        i += 1

while lines and set(lines[0]) == {'.'}:
  lines.pop(0)

while lines and set(lines[-1]) == {'.'}:
  lines.pop()

while lines and lines[0] and \
    set([lines[j][0] for j in range(len(lines))]) == {'.'}:
    for j in lines:
        j.pop(0)

while lines and lines[-1] and \
    set([lines[j][-1] for j in range(len(lines))]) == {'.'}:
    for j in lines:
        j.pop()

for i in range(len(lines)):
    lines[i] = ''.join(lines[i])

if lines == ['#']:
  print('I')
elif lines == ['###', '#.#', '###']:
  print('O')
elif lines == ['##', '#.', '##']:
  print('C')
elif lines == ['#.', '##']:
  print('L')
elif lines == ['#.#', '###', '#.#']:
  print('H')
elif lines == ['###', '#.#', '###', '#..']:
  print('P')
else:
  print('X')