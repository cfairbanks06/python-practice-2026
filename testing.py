from pathlib import Path

test = Path("~/Downloads/testing.txt").expanduser()

print(test)
print(test.with_stem("testing1"))
print(test)