        Changelog of Arnold
===================

0.1.13 (2024-08-09)
-------------------

- Update requirements in setup.py.


0.1.12 (2024-08-09)
-------------------

- Add six to requirements, as g.c.logging needs it but doesn't install it.


0.1.11 (2024-08-09)
-------------------

- Pin google-auth-oauthlib.


0.1.10 (2024-08-09)
-------------------

- Use new gitlab runner

- Add renovate for dependency checks

- Dependency upgrades


0.1.9 (2023-02-20)
------------------

- Dependency upgrades.


0.1.8 (2022-08-30)
------------------

- Dependency upgrades.

- Show unit test coverage


0.1.7 (2022-07-01)
------------------

- Upgrade requirements & requirements-tst.


0.1.6 (2022-04-04)
------------------

- Upgrade requirements

- Add interface to google.cloud.logging.Client

- Fix new pylint issues


0.1.5 (2022-01-18)
------------------

- Upgraded all google.cloud (related) packages; better loose requirements in setup.py.


0.1.4 (2021-12-22)
------------------

- added and pinned more google.cloud dependencies to requirements.txt

0.1.3 (2021-12-13)
------------------

- Upgraded google-cloud-logging to 1.15.1


0.1.2 (2020-04-23)
------------------

- Allow to pass either a logger instance or a string to find a logger by name


0.1.1 (2020-04-22)
------------------

- Don't fail when unable to find logger by name, but create a new one.


0.1.0 (2020-04-21)
------------------

- Released first working version.
