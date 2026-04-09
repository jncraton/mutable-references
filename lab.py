def make_resistor(value):
  return {'type': 'R', 'value': float(value)}

def make_series(components = []) :
  return {'type': 'S', 'components': components}

def make_parallel(components = []) :
  return {'type': 'P', 'components': components}

def total_resistance(network, round_digits = 6):
  """Compute total resistance recursively.

  If round_digits is not None, round the final result to that many digits.
  """
  t = network['type']
  if t == 'R':
    r = float(network['value'])
    return round(r, round_digits) if round_digits is not None else r
  elif t == 'S':
    total = 0.0
    for c in network['components']:
      total += total_resistance(c, round_digits=None)
    return round(total, round_digits) if round_digits is not None else total
  elif t == 'P':
    inv = 0.0
    for c in network['components']:
      r = total_resistance(c, round_digits=None)
      inv += 1.0 / r
    total = 1.0 / inv if inv != 0 else float('inf')
    return round(total, round_digits) if round_digits is not None else total
  else:
    raise ValueError('unknown network type: ' + str(t))

def _almost_eq(a, b, tol=1e-6):
  return abs(a - b) <= tol

def run_tests():
  # Test 1: simple resistor
  r = make_resistor(100)
  assert r['type'] == 'R' and _almost_eq(r['value'], 100.0), 'make_resistor failed'

  # Test 2: series creation should not share components between calls
  s1 = make_series()
  s1['components'].append(make_resistor(10))
  s2 = make_series()
  # s2 should be empty
  assert s2['components'] == [], 'make_series shares state between calls'

  # Test 3: parallel creation should not share components between calls
  p1 = make_parallel()
  p1['components'].append(make_resistor(20))
  p2 = make_parallel()
  assert p2['components'] == [], 'make_parallel shares state between calls'

  # Test 4: total resistance of simple series
  s = make_series([make_resistor(10), make_resistor(20)])
  tr = total_resistance(s)
  assert _almost_eq(tr, 30.0), f'series total wrong: {tr}'

  # Test 5: total resistance of simple parallel
  p = make_parallel([make_resistor(10), make_resistor(20)])
  trp = total_resistance(p, round_digits=6)
  assert _almost_eq(trp, 6.6666666), f'parallel total wrong: {trp}'

  # Test 6: nested networks
  nested = make_series([
    make_resistor(10),
    make_parallel([make_resistor(30), make_resistor(30)])
  ])
  # series: 10 + parallel(30,30) => 10 + 15 = 25
  tn = total_resistance(nested)
  assert _almost_eq(tn, 25.0), f'nested total wrong: {tn}'

  print('ALL TESTS PASSED')

if __name__ == '__main__':
  run_tests()
