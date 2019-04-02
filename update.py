import subprocess
import shutil
import shlex
from pathlib import Path

for notebook in Path('.').glob('*.ipynb'):
    notebook_stem = notebook.stem
    if not notebook_stem.endswith('-custom'):
        dst = notebook_stem + '-custom.ipynb'
        shutil.copy(notebook, dst)

cmd = 'git checkout -- .'
subprocess.run(shlex.split(cmd))

cmd = 'git pull'
subprocess.run(shlex.split(cmd))
