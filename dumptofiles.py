import os
import subprocess

def dump(ob, fs_path):
    if ob.meta_type == 'Folder':
        print '====', repr(ob), 'to', fs_path
        subprocess.check_call(['mkdir', '-p', fs_path])
        for sub_ob in ob.objectValues():
            dump(sub_ob, fs_path + '/' + sub_ob.getId())

    elif ob.meta_type == 'Script (Python)':
        print '[py]', repr(ob), fs_path
        with open(fs_path + '.py', 'wb') as f:
            f.write("# Script (Python)\n")
            f.write("# %s\n" % '/'.join(ob.getPhysicalPath()))
            f.write("# params: %r\n" % ob._params)
            f.write(ob.document_src())

    elif ob.meta_type in ['DTML Document', 'DTML Method']:
        print '[dtml]', repr(ob), fs_path
        with open(fs_path + '.html', 'wb') as f:
            f.write("# %s\n" % ob.meta_type)
            f.write("# %s\n" % '/'.join(ob.getPhysicalPath()))
            f.write(ob.document_src())

    elif ob.meta_type in ['Page Template']:
        print '[zpt]', repr(ob), fs_path
        with open(fs_path + '.html', 'wb') as f:
            f.write("# %s\n" % ob.meta_type)
            f.write("# %s\n" % '/'.join(ob.getPhysicalPath()))
            f.write(ob.document_src())

    elif ob.meta_type == 'Z SQL Method':
        print '[sql]', repr(ob), fs_path
        with open(fs_path + '.sql', 'wb') as f:
            f.write("-- %s\n" % ob.meta_type)
            f.write("-- %s\n" % '/'.join(ob.getPhysicalPath()))
            #f.write("-- params: %r\n" % ob._arg._data)
            f.write(ob.document_src())

    elif ob.meta_type in ['File', 'External Method']:
        print '[xxx]', repr(ob), fs_path
        with open(fs_path + '.txt', 'wb') as f:
            f.write("-- %s\n" % ob.meta_type)
            f.write("-- %s\n" % '/'.join(ob.getPhysicalPath()))

    else:
        print "???", ob.meta_type
