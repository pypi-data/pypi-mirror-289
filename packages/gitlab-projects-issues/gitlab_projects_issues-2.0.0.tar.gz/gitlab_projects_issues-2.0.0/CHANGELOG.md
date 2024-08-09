# Changelog

<a name="2.0.0"></a>
## [2.0.0](https://gitlab.com/AdrianDC/gitlab-projects-issues/compare/1.0.5...2.0.0) (2024-08-08)

### 🛡️ Security

- **🚨 BREAKING CHANGE 🚨 -** **cli:** acquire tokens only from environment variables ([ca80cfe](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/ca80cfe398875e043f6b266af7c812a718bfd7d3))

### ✨ Features

- **🚨 BREAKING CHANGE 🚨 -** **cli:** refactor CLI into simpler GitLab URL bound parameters ([f589c8d](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/f589c8d8948d73770c0ccb12276a18fe78af568f))
- **cli:** add tool identifier header with name and version ([ffb86e6](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/ffb86e6bafb5066c599fb99f6e4f7656b55bccb6))
- **cli:** implement '.python-gitlab.cfg' GitLab configurations files ([e87a3c7](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/e87a3c714a62cb8118cfaa6fc80991ed13a6fdc0))
- **cli, argparse:** implement environment variables helpers ([74acb0e](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/74acb0e85713aff9e51b1733fc3b5016ea6c1750))
- **cli, gitlab:** implement CI job token and public authentications ([57b7253](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/57b7253e275c86e6a3e6d26a1eb5b234d5b034f9))
- **main:** document '--default-estimate' metavar as 'ESTIMATE' ([d5a46d8](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/d5a46d861bd183a15465efa3416f4210b9a45761))

### 🐛 Bug Fixes

- **environments:** add missing ':' to the README help description ([7e05429](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/7e05429536b559ee26219e5893bde94ce5550054))

### 📚 Documentation

- **cliff:** document 'security(...)' first in changelog ([e0e2b46](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/e0e2b4690aa005e3116b8e92119c193e9c28a6e4))
- **readme:** document '~/.python-gitlab.cfg' configuration file ([d9b5954](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/d9b59541ab07de337e16d0ceed249a1f8a91b201))

### ⚙️ Cleanups

- **cli/main:** minor codestyle improvement of 'import argparse' ([33e608b](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/33e608b23e4365e88a086bb74931f251a0493a0f))
- **types:** cleanup inconsistent '()' over base classes ([a0eaa89](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/a0eaa898e8d8a8830223213c619d6ba4a168a0a0))

### 🚀 CI

- **gitlab-ci:** migrate from 'git-chglog' to 'git-cliff' ([79b29f0](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/79b29f070d81d5fafcdefe8478e8c331e7a76b08))
- **gitlab-ci:** bind '.docker/config.json' for local test builds ([5ac41d5](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/5ac41d57fff03095b4a63650e9b039d6605759f1))


<a name="1.0.5"></a>
## [1.0.5](https://gitlab.com/AdrianDC/gitlab-projects-issues/compare/1.0.4...1.0.5) (2024-07-14)

### 🐛 Bug Fixes

- **entrypoint:** initialize for issues without assignee and milestone ([f3692b8](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/f3692b8a8cad3d84c52eedbf572d6d11f04730b5))


<a name="1.0.4"></a>
## [1.0.4](https://gitlab.com/AdrianDC/gitlab-projects-issues/compare/1.0.3...1.0.4) (2024-07-14)

### 🐛 Bug Fixes

- **entrypoint:** avoid failures upon issues without milestones ([57c8dc6](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/57c8dc614371486c5dcb40a79ca7f6f24f5b42ed))


<a name="1.0.3"></a>
## [1.0.3](https://gitlab.com/AdrianDC/gitlab-projects-issues/compare/1.0.2...1.0.3) (2024-06-10)

### 📚 Documentation

- **readme:** improve milestones statistics outputs example ([decf7f4](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/decf7f42d9cdc534d41fec89ee098327d36f6c43))

### 🚀 CI

- **gitlab-ci:** install 'coreutils' in the deployed container image ([4946bdb](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/4946bdb226d33806634c6438461b92e7395770ca))
- **gitlab-ci:** use 'buildah' instead of 'docker' to pull images ([0b969b9](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/0b969b9f742a9a450f11aa45d7807ceee41dd723))


<a name="1.0.2"></a>
## [1.0.2](https://gitlab.com/AdrianDC/gitlab-projects-issues/compare/1.0.1...1.0.2) (2024-06-01)

### 🚀 CI

- **gitlab-ci:** set '/bin/sh' as 'CMD' rather than 'ENTRYPOINT' ([5e742d8](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/5e742d8d9b1cae59891d5048b422ad50db04131d))


<a name="1.0.1"></a>
## [1.0.1](https://gitlab.com/AdrianDC/gitlab-projects-issues/compare/1.0.0...1.0.1) (2024-06-01)

### 📚 Documentation

- **chglog:** add 'ci' as 'CI' configuration for 'CHANGELOG.md' ([29f0b43](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/29f0b43b95d49ee2f53ea07129ef675e8cbb57ed))
- **readme:** update 'README.md' for 'gitlab-projects-issues' ([4fb7d02](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/4fb7d024b45ae68112eac54e5b864f4099d9649a))

### 🚀 CI

- **gitlab-ci:** change commit messages to tag name ([8f8016f](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/8f8016f2c9f03d72afadc62a25109c42d2222dd3))


<a name="1.0.0"></a>
## [1.0.0](https://gitlab.com/AdrianDC/gitlab-projects-issues/commits/1.0.0) (2024-06-01)

### ✨ Features

- **gitlab-projects-issues:** initial sources implementation ([f1cc034](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/f1cc03421e051da80b4d2d1b9227fe03f05a66a7))

### 🚀 CI

- **gitlab-ci:** use 'CI_DEFAULT_BRANCH' to access 'develop' branch ([bae1c08](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/bae1c0826a97aca9805df868f11d08b480901bf2))
- **gitlab-ci:** rehost 'docker:latest' image in 'images' job ([c4cfc9a](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/c4cfc9aa78e408586247741944cd00c85cb3f20a))
- **gitlab-ci:** rehost 'quay.io/buildah/stable:latest' image ([100c069](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/100c069e5f4220f4ebfe9d12dcbb7d863665489e))
- **gitlab-ci:** implement 'deploy:container' release container image ([d3eae88](https://gitlab.com/AdrianDC/gitlab-projects-issues/commit/d3eae8870274a333768078e5fbd7f192fa717bd6))


