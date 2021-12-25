import PyInstaller.__main__
import os
    
PyInstaller.__main__.run([  
     'name-%s%' % 'add2vals.py',
     '--onefile',
     '--windowed',
     os.path.join('/sources/', 'add2vals.py'), """your script and path to the script"""                                        
])

