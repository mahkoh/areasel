def FlagsForFile(filename):
  return {
    'flags': [ '-Wall',
               '-Wpedantic',
               '-Werror',
               '-std=c99',
             ],
    'do_cache': True
  }
