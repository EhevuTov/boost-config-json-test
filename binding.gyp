{
  "targets": [
  {
  'target_name': 'boost-config-test',
  'type': 'executable',
  'cflags_cc+': ['-frtti', '-fexceptions'],
      'cflags_cc+': ['-fno-strict-aliasing', '-arch i386'],
      'cflags_cc+': ['-g', '-O2', '-Udarwin12', '-Ddarwin12=darwin12'],
  'defines': [
    'NDEBUG',
    'USE_THREADS',
  ],
  'sources': [
    'boost-config-test.cc',
  ],
  'library_dirs': [
    '/usr/local/lib',
  ],
  'include_dirs': [
    '/usr/local/include',
  ],
  'conditions': [
    ['OS=="mac"', {
      'cflags_cc+': ['-frtti', '-fexceptions'],
      'cflags_cc+': ['-g', '-O2', '-Udarwin12', '-Ddarwin12=darwin12'],
      'libraries': [
        '-lboost_system-mt',
      ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_RTTI': 'YES',
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'OTHER_CFLAGS': [
          '-arch i386',
        ],
      }
    }
    ],
    ['OS=="linux" or OS=="freebsd"', {
      'libraries': [
        '-lboost_system',
      ],
    }
    ],
  ],
  'test': 0,
  }
]
}
