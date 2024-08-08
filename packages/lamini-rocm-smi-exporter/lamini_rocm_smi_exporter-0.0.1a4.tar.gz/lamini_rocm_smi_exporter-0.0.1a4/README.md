# rocm-smi-exporter

Export rocm-smi metrics as prometheus metrics

## Deployment

The rocm-smi-exporter is built and uploaded to pypi.
It is then deployed on the host as a systemd service.

### Build and upload pypi package

```
cd deployment

# Create virtual env
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python -m build ..

# You'll need to enter your Pypi API token
python3 -m twine upload --repository pypi ../dist/*

# Deactivate virtual env
deactivate
```

### Create systemd service

To create systemd service to running the above pip module.
The host must have `systemd` installed.

```
# Need to install the module as root in order for the systemd to pick up.
sudo pip install lamini-rocm-smi-exporter

# Copy systemd service definition file.
sudo cp lamini-rocm-smi-exporter.service /etc/systemd/system/

# Always reloading configs, see:
# https://unix.stackexchange.com/a/740098
sudo systemctl daemon-reload

# Enable and start the service so the service can be started after system (re)boot.
sudo systemctl enable lamini-rocm-smi-exporter.service
sudo systemctl status lamini-rocm-smi-exporter.service
```
![image](https://github.com/user-attachments/assets/2e963ea2-28f9-4a33-94a1-c32d5b4befb8)

```
sudo systemctl start lamini-rocm-smi-exporter.service
sudo systemctl status lamini-rocm-smi-exporter.service
```
![image](https://github.com/user-attachments/assets/f18a221b-ca2e-46d9-8663-81238185c61b)


### Stop and remove systemd service

```
# Stop the service
sudo systemctl stop lamini-rocm-smi-exporter.service

# Verify that the service is stopped
sudo systemctl status lamini-rocm-smi-exporter.service
```
![image](https://github.com/user-attachments/assets/83bd6e9f-49c4-449e-83c6-b865cead913c)

```
# Disable the service
sudo systemctl disable lamini-rocm-smi-exporter.service

# Verify that the service is disabled
sudo systemctl status lamini-rocm-smi-exporter.service
```

![image](https://github.com/user-attachments/assets/1d2bc766-d658-44a8-a31c-5151ad364f92)

```
# Remove service definition file
sudo rm /etc/systemd/system/lamini-rocm-smi-exporter.service
```

## Pants build

[Pants](https://www.pantsbuild.org/2.21/docs/introduction/welcome-to-pants)
uses explicit `BUILD` files to track source files' dependencies and builds.

Pants is hermetic, means that the entire build environment is specified in
[pants.toml](pants.toml), which is copied from
[example-python](https://github.com/pantsbuild/example-python).

## Extra

* [Add args to systemd service](https://superuser.com/a/728962)
  * The python code accepts `--port` and other arguments
  * If needed, set its value when launching systemd service
