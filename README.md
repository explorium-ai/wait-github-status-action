# Wait for a Github Check/Status action

This action will wait for the result of a Check or a Status in a PR. Checks and Statuses are defined in different API endpoints in Github api, thus to encompass all runs in a PR you have to combine both to include also external checks like CI/CD tools.
## Inputs

```yaml
name:
  description: 'The name of the check (eg. Lint, pr-head, Test, etc.)'
  required: true
  default: ''
strict:
  description: 'Fail the job if the check failed itself.'
  required: false
  default: 'true'
timeout:
  description: 'If not empty, wait for that amount of seconds before failing.'
  required: false
  default: ''  
seconds:
  description: 'Time to wait between each API wait poll check.'
  required: false
  default: '10'    
token:
  description: 'Github API token'
  required: true
  default: ''       
sha:
  description: 'You must insert the sha of the PR'
  required: true
  default: ${{ github.event.pull_request.head.sha }}    
```

## Outputs

## `result`

The result of the Status/Check Run

## Example usage

```yaml
uses: explorium-ai/wait-github-status-action@v1.0.2
with:
  name: lint
  token: ${{ secrets.GITHUB_TOKEN }}
  sha: ${{ github.event.pull_request.head.sha }} # Must
```
