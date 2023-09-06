from pathlib import Path

path = Path('D:\Movies')
for file in path.glob('*'):
    print(file)