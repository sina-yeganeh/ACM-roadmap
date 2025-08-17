t = int(input())

for _ in range(t):
  n = int(input())
  numbers = list(map(int, input().split()))

  answers = []
  max_size = 0
  for i in range(n):
    answer = []
    answer.append(numbers[i])
    for j in range(i + 1, n):
      if numbers[i] * numbers[j] > 0:
        if len(answer) >= max_size:
          max_size = len(answer)
          answers.append(answer)
        break

      answer.append(numbers[j])

  max_list = answers[0]
  for i in range(1, len(answers)):
    if sum(answers[i]) > sum(max_list):
      max_list = answers[i]

  print(sum(max_list))


