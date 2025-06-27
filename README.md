# Library Management System (Frappe ERPNext v15)

A custom Frappe app to manage a simple Library Management System where Librarians can manage Articles (Books), Members, Memberships, and Transactions (Issue/Return). Built for ERPNext v15.

---

##  Features

- **Article Management**: Add, update, and manage articles (books or items).
- **Library Members**: Track library users and their membership details.
- **Memberships**: Manage subscription plans for members.
- **Transactions**: Log issue and return activity of library articles.
- **Library Settings**: Define loan period and issue limits.

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app library_management
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/library_management
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

mit
