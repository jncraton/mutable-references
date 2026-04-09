# Mutable References

![Parallel resistors](https://upload.wikimedia.org/wikipedia/commons/0/09/Resistors_in_parallel.svg)

This lab explores the dangers of mutable references in Python and the correct use of optional and named parameters.

## Learning Outcomes

After completing this lab, learners will be able to:

1. Explain how Python passes object references to functions and why mutable defaults are dangerous
2. Identify and fix bugs caused by shared mutable default arguments
3. Implement recursive algorithms to compute total resistance of series and parallel resistor networks
4. Use optional and named parameters correctly

## Usage

Run the automated tests with:

```
make test
```

The tests will fail until the tasks below are completed.

## Testing

The repository contains a single Python file `resistors.py` with built-in tests. Running `python3 resistors.py` or `make test` executes the tests.

## Tasks

1. Fix the creation functions `make_series` and `make_parallel`
2. Implement `total_resistance(network)` to return the total resistance of the network as a float. Series resistances add; parallel resistances combine as the reciprocal of the sum of reciprocals
3. Ensure `total_resistance` accepts the optional named parameter `round_digits` which controls rounding of the returned value when provided

## Resources

- [Why are default values shared between objects?](https://docs.python.org/3/faq/programming.html#why-are-default-values-shared-between-objects)
- [Series and parallel resistor formulas](https://en.wikipedia.org/wiki/Series_and_parallel_circuits)
