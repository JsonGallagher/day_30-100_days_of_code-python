print("30 days down - What did you think?")
print()

for i in range(1, 31):
  thought = input(f"Day {i}: \n")
  reply = f"You thought Day {i} was:"
  print(f"{reply:^50}")
  print(f"{thought:^50}")
  print()