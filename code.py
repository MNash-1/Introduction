def multiplication_table(number, limit=10):
  """Prints the multiplication table of a given number up to a specified limit.

  Args:
    number: The number for which the multiplication table is generated.
    limit: The upper limit of the multiplication table (default is 10).
  """
  for i in range(1, limit + 1):
    print(f"{number} x {i} = {number * i}")