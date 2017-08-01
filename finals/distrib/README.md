## Challenge Enviroment

### About

Our platform will run your team's patched binary (and the original unpatched binary) within a specific Docker container environment. For some challenges, the particular environment may affect the exploit.

To verify that your exploit script will succeed when run on our platform, you should test it against the binary when it's running in the challenge environment.

### Pre-requisites

* Some Linux host that can run the latest Docker CE. We've tested things on a fresh ubuntu-16.04.2-server-amd64 box.

### Setup

1. [Install the latest Docker CE on some Linux host](https://docs.docker.com/engine/installation/linux/ubuntu/).
2. Run `start.sh` for usage instructions. It will download the challenge environment image on first run.

## Example exploit and exploitable

An example exploit and its corresponding exploitable is provided as part of this distribution.

An example of exploit execution in the challenge environment is `exploit.py localhost 1337` and thus, 
it is important to ensure that your exploit script accept these two arguments.
