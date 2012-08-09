var DisplayNames = {
  pyflakes: {
    total:                    'Total',
    UnusedImport:             'Unused import',
    RedefinedWhileUnused:     'Redefined while unused',
    ImportShadowedByLoopVar:  'Import shadowed by loop var',
    ImportStarUsed:           'Import * used',
    UndefinedName:            'Undefined name',
    UndefinedExport:          'Undefined export',
    UndefinedLocal:           'Undefined local',
    DuplicateArgument:        'Duplicate argument',
    Redefined:                'Redefined',
    LateFutureImport:         'Late future import',
    UnusedVariable:           'Unused variable'
  },

  pep8: {
    total: 'Total',
    E101: 'Indentation contains mixed spaces and tabs',
    E111: 'Indentation is not a multiple of four',
    E112: 'Expected an indented block',
    E113: 'Unexpected indentation',
    E121: 'Indentation is not a multiple of four',
    E122: 'Missing indentation or outdented',
    E123: 'Cloding bracket does not match indentation of opening backet\'s line',
    E124: 'Closing bracket does not match visual indentation',
    E125: 'Continuation line does not distinguish itself from next logical line',
    E126: 'Over-indented for hanging indent',
    E127: 'Over-indented for visual indent',
    E128: 'Continuation line under-indented for visual indent',
    E201: 'Whitespace after character',
    E202: 'Whitespace before character',
    E203: 'Whitespace before character',
    E211: 'Whitespace before character',
    E221: 'Multiple spaces before operator',
    E222: 'Multiple spaces after operator',
    E223: 'Tab before operator',
    E224: 'Tab after operator',
    E225: 'Missing whitespace around operator',
    E231: 'Missing whitespace after character',
    E241: 'Multiple spaces after character',
    E251: 'No spaces around keyword / parameter equals',
    E261: 'At least two spaces before inline comment',
    E262: 'Inline comment should start with #',
    E242: 'Tab after character',
    E271: 'Multiple spaces after keyword',
    E272: 'Multiple spaces before keyword',
    E273: 'Tab after keyword',
    E274: 'Tab before keyword',
    E301: 'Expected 1 blank line, found 0',
    E302: 'Expected 2 blank lines, found other',
    E303: 'Too many blank lines',
    E304: 'Blank lines found after function decorator',
    E401: 'Multiple imports on one line',
    E501: 'Line too long',
    E502: 'The backslash is redundant between brackets',
    E701: 'Multiple statements on one line (colon)',
    E702: 'Multiple statements on one line (semicolon)',
    E711: 'Use "is" or "is not" when comparing to singletons',
    E712: 'Use "is" or "is not" when comparing to singletons',
    E721: 'Do not compare types, use isinstance()',
    E901: 'Syntax error',
    E902: 'Syntax error',
    W191: 'Indentation contains tabs',
    W291: 'Trailing whitespace',
    W292: 'No newline at end of file',
    W293: 'Blank line contains whitespace',
    W391: 'Blank line at end of file',
    W601: 'has_key() is deprecated, use "in"',
    W602: 'Deprecated form of raising exception',
    W603: '<> is deprecated, use !=',
    W604: 'Backticks are deprecated, use repr()'
  }
}