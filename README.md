# Project Manager
## About
This repository includes an example of using the MixedEmotions' orchestrator. It will launch an instance of MixedEmotions' orchestrator for each file in a given folder. The folder structure it follows is the one given by MixedEmotions' Twitter Crawler (using the project into disk version)

This repository also includes example configuration files for the orchestrator and for the docker and rest modules inside the conf folder.

## Usage

You will need a compiled version of the MixedEmotions' orchestrator. You can compile one or download the latest version from the [releases tab](https://github.com/MixedEmotions/Orchestrator/releases) in that repository. 

Edit `orchestrator_launcher.py` so it matches the routes of your configuration.
Then create a proper configuration for the MixedEmotions' Orchestrator. There is an example structure in the `conf/` folder.
There are example service configurations in the `conf/restServices` and `conf/dockerServices` folders.

## Acknowledgement

This development has been partially funded by the European Union through the MixedEmotions Project (project number H2020 655632), as part of the `RIA ICT 15 Big data and Open Data Innovation and take-up` programme.

![MixedEmotions](https://raw.githubusercontent.com/MixedEmotions/MixedEmotions/master/img/me.png) 

![EU](https://raw.githubusercontent.com/MixedEmotions/MixedEmotions/master/img/H2020-Web.png)

 http://ec.europa.eu/research/participants/portal/desktop/en/opportunities/index.html
