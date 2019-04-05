import datetime
import shlex
import shutil
import subprocess
from pathlib import Path

timestamp = datetime.datetime.now().strftime('%y%m%dT%H%M')
for notebook in Path('.').glob('*.ipynb'):
    notebook_stem = notebook.stem
    if not notebook_stem.endswith('-custom'):
        dst = notebook_stem + f'{timestamp}-custom.ipynb'
        shutil.copy(notebook, dst)

cmd = 'git checkout -- .'
subprocess.run(shlex.split(cmd))

cmd = 'git pull'
subprocess.run(shlex.split(cmd))
