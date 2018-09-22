# hostname_viewer

View all hostnames in an IP range.

## Demo server

* https://hostname-viewer.theel0ja.info/
* https://hostname-viewer.theel0ja.info/api/get_by_ipblock?block=95.216.11.0/30

## Setup

```bash
virtualenv venv
source venv/bin/activate
pip install netaddr
pip install Flask
```

### Run

```bash
sudo -u www-data uwsgi --ini uwsgi.ini
```

## Dependencies

```bash
pip install netaddr
pip install Flask
```
