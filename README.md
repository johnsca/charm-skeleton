# Skeleton Charm using Operators Framework

To prepare this charm for deployment, run the following to install the
framework in to the `lib/` directory:

```
pip install -t lib/ https://github.com/canonical/operator
```

You can then deploy the charm:

```
juju deploy .
```

You can sync subsequent changes from the framework by running the `pip`
command again with `--upgrade`.
