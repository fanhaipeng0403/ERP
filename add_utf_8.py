# -*- coding: utf-8 -*-
import os

src_dir = './ERP'
for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith('.py'):
            with open(os.path.join(root,file),'r+') as f:
                old = f.read()
                f.seek(0)
                f.write('# -*- coding: utf-8 -*-\n')
                f.write(old)

