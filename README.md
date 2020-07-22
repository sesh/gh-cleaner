Clean up your public Github repositories...

...and by clean up I mean **delete** (or make private).

- Makes repositories that you own, are older than 365 days and have less than 3 stars private
- Removes public forks that you own, have less than 3 stars and haven't been pushed to for 365 days


### Usage

Create a Personal Access Token with repo and delete_repo scopes.

```
export GITHUB_TOKEN=<token>
python3 gh_clean.py
```

Pagination is not implemented, so you may need to run this more than once to get all of your repositories.
