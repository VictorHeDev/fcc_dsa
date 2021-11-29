def sum(numbers):
  total = 0
  for number in numbers:
    total += number
  return total

# print(sum([1, 2, 7, 9]))

def recursive_sum(numbers):
  if len(numbers) == 1:
    return numbers[0]

  remaining_sum = recursive_sum(numbers[1:])
  return numbers[0] + remaining_sum

print(recursive_sum([1, 2, 7, 9]))