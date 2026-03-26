# iocx-registry-keys

A high‑performance registry key detector plugin for the `iocx` engine.

This plugin extracts:

- Registry keys (generic Windows registry paths)
- Registry values (REG_SZ, REG_DWORD, etc.)
- Persistence keys (autorun locations such as Run and RunOnce)

It is designed to be:

- Fast — sub‑millisecond detection on typical inputs
- Safe — no catastrophic backtracking, even on pathological inputs
- Accurate — clean separation between keys, values, and persistence
- Well‑tested — full unit, integration, and performance coverage

## Features

✔ Registry Key Detection

Matches Windows registry paths such as:

```
HKCU\Software\Example
HKLM\System\CurrentControlSet\Services\Tcpip
HKEY_LOCAL_MACHINE\Software\Microsoft\Windows
```

✔ Registry Value Detection

Detects common value types:

```
REG_SZ
REG_DWORD
REG_BINARY
REG_QWORD
REG_MULTI_SZ
REG_EXPAND_SZ
```

✔ Persistence Key Detection

Identifies autorun locations used by malware:

```
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
```

✔ High Performance

All detectors are optimized to avoid backtracking and scale linearly with input size.

## Installation

Install via pip:

```bash
pip install iocx-registry-keys
```

Or install in editable mode during development:

```bash
pip install -e .
```

## Usage

The plugin is automatically discovered by the `iocx` engine via entry points.

```python
from iocx import Engine

engine = Engine()
result = engine.extract("HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run")

print(result["iocs"])
```

Output:

```json
{
  "registry.persistence": [
    "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
  ],
  "registry.keys": [],
  "registry.values": []
}
```

## Development

### Install dev dependencies

```bash
make install
```

### Run tests

```bash
make test
```
```bash
make test-performance
```

### Run coverage

```bash
make test-coverage
```

### Run security checks
```bash
make security
```

This runs:

- pip-audit for dependency vulnerabilities
- bandit for static code security analysis

## Performance

This plugin includes a full performance suite under tests/performance/.

Example results on a typical machine:

```
registry-keys 1MB mixed-content:       ~0.002s
registry-values 1MB mixed-content:     ~0.001s
registry-persistence 1MB mixed-content ~0.002s
```

Pathological cases (deep nesting, repeated patterns) remain safe and predictable.

## Testing

The project includes:

- Unit tests
- Integration tests
- Performance tests
- Pathological safety tests
- 100% coverage on plugin code

Run everything:

```bash
pytest -q
```

## Contributing

Contributions are welcome.

If you want to propose changes to detection behavior (e.g., adding new persistence keys), please open a PR. Priority decisions are centrally managed by the IOCX engine, so contributors can propose category priority changes through the normal review process.
License

MIT License. See LICENSE for details
