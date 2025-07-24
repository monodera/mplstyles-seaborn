# Codecov Integration Setup

This document provides step-by-step instructions for enabling dynamic coverage badges through Codecov integration.

## Prerequisites

- Repository owner/admin access to `monodera/mplstyles-seaborn`
- GitHub CLI (`gh`) installed and authenticated
- Web browser access

## Setup Instructions

### 1. Register Repository with Codecov

1. **Visit Codecov**: Go to https://codecov.io/
2. **Sign in**: Click "Sign up with GitHub" and authorize access
3. **Add Repository**: 
   - Click "Add new repository" or go to https://codecov.io/gh
   - Search for `monodera/mplstyles-seaborn`
   - Click "Setup repo" to enable integration
4. **Get Upload Token**:
   - Navigate to Settings > Repository > monodera/mplstyles-seaborn
   - Copy the "Repository Upload Token" (UUID format)

### 2. Configure GitHub Secrets

**Option A: Using GitHub CLI (Recommended)**
```bash
# Set secret interactively (paste token when prompted)
gh secret set CODECOV_TOKEN

# Verify the secret was set
gh secret list
```

**Option B: Using GitHub Web Interface**
1. Go to https://github.com/monodera/mplstyles-seaborn/settings/secrets/actions
2. Click "New repository secret"
3. Name: `CODECOV_TOKEN`
4. Value: (paste the token from step 1.4)
5. Click "Add secret"

### 3. Update README Badge

Once setup is complete, replace the static coverage badge in README.md:

**From:**
```markdown
[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](#testing)
```

**To:**
```markdown
[![codecov](https://codecov.io/gh/monodera/mplstyles-seaborn/branch/main/graph/badge.svg)](https://codecov.io/gh/monodera/mplstyles-seaborn)
```

### 4. Test Integration

1. **Trigger CI**: Push a commit or create a pull request
2. **Check Actions**: Verify "Upload coverage to Codecov" step succeeds
3. **Verify Badge**: The Codecov badge should show actual coverage percentage
4. **View Reports**: Visit https://codecov.io/gh/monodera/mplstyles-seaborn for detailed reports

## Configuration Files

The repository already includes:

- **`.github/workflows/test.yml`**: CI workflow with Codecov upload
- **`codecov.yml`**: Coverage configuration with 100% target
- **`pyproject.toml`**: Coverage reporting settings

## Verification Commands

```bash
# Check if secret is configured
gh secret list | grep CODECOV_TOKEN

# View recent workflow runs
gh run list --workflow=Tests

# Check specific run details
gh run view [RUN_ID] --log
```

## Troubleshooting

### Common Issues

1. **"Token not found" error**:
   - Verify the token was copied correctly
   - Ensure the secret name is exactly `CODECOV_TOKEN`

2. **"Repository not found" error**:
   - Check that the repository was properly added to Codecov
   - Verify the repository slug in the workflow file

3. **Upload fails**:
   - Check that the coverage.xml file is generated
   - Verify the file path in the workflow matches the actual location

### Debug Information

Enable verbose logging by checking the workflow logs:
```bash
gh run view --log | grep -A5 -B5 "codecov"
```

## Benefits After Setup

- **Dynamic Badges**: Real-time coverage percentage
- **PR Integration**: Coverage changes shown in pull requests  
- **Detailed Reports**: File and function-level coverage analysis
- **Historical Tracking**: Coverage trends over time
- **Quality Gates**: Automatic failure if coverage drops below target

## Support

- **Codecov Documentation**: https://docs.codecov.com/
- **GitHub Actions Integration**: https://github.com/codecov/codecov-action
- **Repository Issues**: https://github.com/monodera/mplstyles-seaborn/issues