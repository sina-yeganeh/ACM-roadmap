def binary_search(lst: list, target: int, start: int, end: int):
  if start > end:
    return -1
  
  mid = (start + end) // 2

  if lst[mid] == target:
    return mid
  elif lst[mid] > target:
    end = mid - 1
  else:
    start = mid + 1

  return binary_search(lst, target, start, end)

if __name__ == "__main__":
  sorted_list = [1, 5, 7, 19, 27, 31, 45, 63, 90]
  print(binary_search(
    sorted_list,
    7,
    0,
    len(sorted_list) - 1
  ))