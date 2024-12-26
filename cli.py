import os
import fire
from funcs.tree import tree
from pathlib import Path



class Lab:

    def __init__(self):
        self.lab = None
        self.readme = None
        self.path = 'C:\\Users\\User\\vscode_project\\labs\\labs'

    def list(self):
        print('Available: ')
        p = Path(self.path)
        tree(p, level=2)

    def run(self, n):
        print(f'Lab{n} is running...\n')
        print('Result:\n', os.popen(f'python {self.path}\\lab{n}\\lab.py').read())


if __name__ == '__main__':
    fire.Fire(Lab)




