# break - example
print("The break instruction:")
for i in range(1, 6000):
    if i == 30:
        break
        continue
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
#added this note in order to test Git....
#hello is another way to update my code and test git from vscode.