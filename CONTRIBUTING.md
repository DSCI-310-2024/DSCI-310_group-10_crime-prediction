# Feedback and Contribution

We welcome any input, feedback, bug reports, and contributions via [Our
GitHub Repository](https://github.com/DSCI-310-2024/DSCI310-group10-project).

All contributions, suggestions, and feedback you submitted are accepted under the [Project's license](./LICENSE). You represent that if you do not own copyright in the code that you have the authority to submit it under the [Project's license](./LICENSE). All feedback, suggestions, or contributions are not confidential. The Project abides by our [code of conduct](./CODE_OF_CONDUCT.md).

## How To Contribute Code

### Setting Up Your Environment

Fork the repository on GitHub and then clone the fork to your local
machine. 

```cmd
git clone https://github.com/YOUR-USERNAME/altair.git
```

To keep your fork up to date with changes in this repo,
you can [use the fetch upstream button on GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork).

Once your local environment is up-to-date, you can create a new git branch
which will contain your contribution
(always create a new branch instead of making changes to the main branch):

```cmd
git switch -c <your-branch-name>
```

With this branch checked-out, create a new conda environment with the required dependencies.

```cmd
conda env create -f environment.yml
```

Then activate the environment.

```cmd
conda activate group10_environment
```

Now you are ready to make your changes.

### Submitting Changes

When you are happy with your changes, you can commit them to your branch by running

```cmd
git add <modified-file>
git commit -m "Some descriptive message about your change"
git push origin <your-branch-name>
```

You will then need to submit a pull request (PR) on GitHub asking to merge
your example branch into the main Altair repository. For details on creating a PR see GitHub
documentation [Creating a pull
request](https://help.github.com/en/articles/creating-a-pull-request). You can
add more details about your example in the PR such as motivation for the
example or why you thought it would be a good addition.  You will get feed back
in the PR discussion if anything needs to be changed. To make changes continue
to push commits made in your local example branch to origin and they will be
automatically shown in the PR.

## Acknowledgements

This contribution guide is inspired by the guidelines provided by Altair's [CONTRIBUTING.md](https://github.com/altair-viz/altair/blob/main/CONTRIBUTING.md).