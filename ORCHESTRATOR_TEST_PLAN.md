# Orchestrator End-to-End Test Plan

## Overview

This document describes the test plan for validating the self-reflexive-orchestrator's autonomous development capabilities.

## Test Repository

**Repository**: `justin4957/orchestrator-test-app`
**Purpose**: Simple Python calculator app with progressive feature additions

## Test Issues Created

### Issue #1: Add Power Operation (Low Complexity: 3/10)
- **Type**: Enhancement
- **Label**: `bot-approved`, `enhancement`
- **Tests**: Basic mathematical operation implementation
- **Expected**: Orchestrator should claim, implement, create PR, pass CI, and merge

### Issue #2: Add Square Root Operation (Low-Medium Complexity: 4/10)
- **Type**: Enhancement
- **Label**: `bot-approved`, `enhancement`
- **Tests**: Implementation with error handling (negative numbers)
- **Expected**: Proper error handling and edge case tests

### Issue #3: Improve Error Messages (Low Complexity: 3/10)
- **Type**: Bug fix
- **Label**: `bot-approved`, `bug`
- **Tests**: String formatting and test updates
- **Expected**: Existing tests should be updated to match new error messages

### Issue #4: Add Calculation History (Medium Complexity: 6/10)
- **Type**: Enhancement
- **Label**: `bot-approved`, `enhancement`
- **Tests**: Internal state management, data structures
- **Expected**: More complex implementation with timestamp handling

## Orchestrator Configuration

**Config File**: `self-reflexive-orchestrator-standalone/config/test-app-config.yaml`

Key settings for testing:
- **Mode**: `supervised` (requires approval for merges)
- **Poll Interval**: 60 seconds (faster feedback)
- **Max Concurrent**: 1 (sequential processing for clearer debugging)
- **Auto-merge**: false (manual verification)
- **Code Review**: Disabled initially (can be enabled later)
- **Daily Cost Limit**: $10 (prevent runaway costs)

## Running the Test

### 1. Prerequisites

```bash
cd /Users/coolbeans/Development/dev/self-reflexive-orchestrator-standalone
source venv/bin/activate
```

Ensure environment variables are set:
- `GITHUB_TOKEN`: GitHub personal access token with repo permissions
- `ANTHROPIC_API_KEY`: Anthropic API key for Claude

### 2. Validate Configuration

```bash
python -m src.cli validate-config --config config/test-app-config.yaml
```

### 3. Start Orchestrator

```bash
python -m src.cli start --config config/test-app-config.yaml --mode supervised
```

### 4. Monitor Progress

In a separate terminal:

```bash
# Watch orchestrator status
python -m src.cli status --config config/test-app-config.yaml

# View logs
tail -f logs/test-app-orchestrator.log

# View audit trail
tail -f logs/test-app-audit.log
```

### 5. Check GitHub Activity

Monitor the test repository:
- Issue assignments
- Pull request creation
- CI/CD runs
- Code review comments (if multi-agent-coder enabled)

## Expected Workflow for Each Issue

1. **Issue Detection**
   - Orchestrator polls repository
   - Detects issue with `bot-approved` label
   - Analyzes complexity

2. **Issue Claiming**
   - Assigns issue to orchestrator
   - Adds comment with implementation plan

3. **Implementation**
   - Creates feature branch
   - Implements solution
   - Runs local tests
   - Commits changes

4. **PR Creation**
   - Creates pull request
   - Includes detailed description
   - Links to original issue

5. **CI Monitoring**
   - Watches GitHub Actions workflow
   - Analyzes test failures if any
   - Auto-fixes if possible

6. **Code Review** (if enabled)
   - Runs multi-agent-coder review
   - Addresses feedback
   - Pushes updates

7. **Merge Approval**
   - Requests human approval (supervised mode)
   - Merges upon approval
   - Closes issue

## Success Criteria

### For Each Issue:
- ✅ Issue is automatically claimed
- ✅ Implementation matches acceptance criteria
- ✅ All tests pass in CI
- ✅ PR description is clear and comprehensive
- ✅ Code follows project style (flake8, mypy pass)
- ✅ Issue is properly closed after merge

### Overall System:
- ✅ No unhandled exceptions in orchestrator logs
- ✅ All safety mechanisms trigger appropriately
- ✅ Audit trail is complete and accurate
- ✅ Cost tracking stays within limits
- ✅ State management works correctly

## Failure Scenarios to Document

Track any issues encountered:

### Orchestrator Bugs
- Configuration parsing errors
- GitHub API integration issues
- State machine problems
- Unexpected exceptions

### Feature Requests
- Missing configuration options
- Desired behavior not supported
- UX improvements for CLI
- Better error messages

### Enhancement Opportunities
- Performance optimizations
- Better logging/debugging
- Improved AI prompting
- Multi-agent-coder integration improvements

## Documentation Process

For each bug or enhancement identified:

1. **Create Issue in self-reflexive-orchestrator-standalone**
   ```bash
   gh issue create --repo justin4957/self-reflexive-orchestrator-standalone \
     --title "Bug: [Description]" \
     --label "bug" \
     --body "[Detailed description with reproduction steps]"
   ```

2. **Include**:
   - Clear reproduction steps
   - Expected vs actual behavior
   - Relevant log excerpts
   - Configuration used
   - Environment details

## Advanced Testing (Phase 2)

Once basic testing is complete:

1. **Enable Multi-Agent Code Review**
   - Update config: `code_review.require_approval: true`
   - Test review feedback processing

2. **Test Autonomous Mode**
   - Update config: `mode: autonomous`
   - Monitor with no human intervention

3. **Test Roadmap Generation**
   - Enable: `roadmap.enabled: true`
   - Validate proposed features
   - Test issue creation from roadmap

4. **Stress Testing**
   - Increase: `max_concurrent: 3`
   - Create multiple issues simultaneously
   - Test parallel processing

5. **Failure Recovery**
   - Intentionally create failing tests
   - Test auto-fix attempts
   - Validate rollback mechanisms

## Metrics to Collect

- Time from issue creation to PR creation
- Time from PR creation to merge
- Number of auto-fix attempts needed
- API cost per issue
- Success rate (% of issues completed)
- Types of failures encountered

## Test Completion Checklist

- [ ] All 4 test issues processed
- [ ] Configuration validated
- [ ] Orchestrator runs without crashes
- [ ] Audit logs are complete
- [ ] GitHub PRs created and merged
- [ ] All tests pass in CI
- [ ] Bugs documented in GitHub issues
- [ ] Enhancements documented in GitHub issues
- [ ] Test results documented in summary report
- [ ] Recommendations for improvements compiled

## Next Steps After Testing

1. Review all created GitHub issues
2. Prioritize bugs vs enhancements
3. Create roadmap for orchestrator improvements
4. Document lessons learned
5. Update orchestrator documentation based on findings
