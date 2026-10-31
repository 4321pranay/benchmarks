# Ceph — placeholder

No questions yet. Add them as `eval.jsonl` in this directory, in the format described in the
[root README](../../README.md#record-format), then run `python3 validate.py` from the repo root.

- **Product id:** `ceph`
- **Priority:** high — explains production incidents
- **Reference docs:**
  - https://docs.ceph.com/en/latest/rados/operations/health-checks/
  - https://docs.ceph.com/en/latest/rados/troubleshooting/
  - https://docs.ceph.com/en/latest/mgr/prometheus/
  - https://docs.ceph.com/en/latest/radosgw/
  - https://docs.ceph.com/en/latest/rbd/
  - https://docs.ceph.com/en/latest/cephfs/

Narrowed to what explains incidents: health-check codes, troubleshooting, `ceph_*` metric names, and the RGW / RBD / CephFS access paths. Docs are versioned per release name (`/en/squid/`, `/en/reef/`), not per deployment.
