def make_resistor(value):
    """Create a resistor descriptor.

    >>> make_resistor(100)
    {'type': 'R', 'value': 100.0}

    >>> make_resistor(1/2)
    {'type': 'R', 'value': 0.5}
    """
    return {"type": "R", "value": float(value)}


def make_series(components=[]):
    """Create a series network descriptor.

    Default components list must be fresh for each call.

    >>> s1 = make_series()
    >>> s1
    {'type': 'S', 'components': []}
    >>> s1['components'].append(make_resistor(10))
    >>> s2 = make_series()
    >>> s2
    {'type': 'S', 'components': []}
    """
    return {"type": "S", "components": components}


def make_parallel(components=[]):
    """Create a parallel network descriptor.

    Default components list must be fresh for each call.

    >>> p1 = make_parallel()
    >>> p1
    {'type': 'P', 'components': []}
    >>> p1['components'].append(make_resistor(20))
    >>> p2 = make_parallel()
    >>> p2
    {'type': 'P', 'components': []}
    """
    return {"type": "P", "components": components}


def compute_series(components):
    """Compute total resistance for series components.

    Components may be resistors or nested networks.

    >>> compute_series([make_resistor(1)])
    1.0

    >>> compute_series([make_resistor(10), make_resistor(20)])
    30.0
    """
    return 0.0


def compute_parallel(components):
    """Compute total resistance for parallel components.

    Returns float('inf') for an open circuit (no conductance).

    >>> compute_parallel([make_resistor(2), make_resistor(2)])
    1.0

    >>> compute_parallel([make_resistor(12), make_resistor(24)])
    8.0
    """
    return 0.0


def total_resistance(network):
    """Compute total resistance of a network.

    The function dispatches to compute_series and compute_parallel.
    If round_digits is not None the final result is rounded.

    >>> total_resistance(make_resistor(1/3))
    0.33

    >>> total_resistance(make_resistor(1/3), round_digits=1)
    0.3

    >>> total_resistance(make_resistor(1/3), round_digits=2)
    0.33

    >>> series = make_series([make_resistor(10), make_resistor(20)])
    >>> total_resistance(series)
    30.0
    >>> parallel = make_parallel([make_resistor(12), make_resistor(24)])
    >>> total_resistance(parallel)
    8.0
    >>> nested = make_series([series, parallel])
    >>> total_resistance(nested)
    38.0
    """
    return 0.0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
