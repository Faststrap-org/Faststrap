# Faststrap Doctor CLI

Use `faststrap doctor` to detect common setup and integration issues.

## Install / entrypoint

After installing a version that includes CLI scripts:

```bash
faststrap doctor
```

## Scan custom path

```bash
faststrap doctor --path .
```

## Checks currently included

- Import source shadowing (site-packages vs local source confusion).
- Potential `/static` mount conflicts with `mount_assets(...)`.
- `toast_response(...)` usage without `ToastContainer(...)`.
- Basic preset misuse detection patterns.

## Exit behavior

- Exit `0`: no issues found.
- Exit `1`: one or more warnings detected.

## Typical workflow

1. Run `faststrap doctor`.
2. Fix reported issues.
3. Re-run until status is clean.

