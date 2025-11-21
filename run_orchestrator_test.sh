#!/bin/bash
# Helper script to run orchestrator tests

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ORCHESTRATOR_DIR="$SCRIPT_DIR/../self-reflexive-orchestrator-standalone"
CONFIG_FILE="$ORCHESTRATOR_DIR/config/test-app-config.yaml"

echo "========================================="
echo "Orchestrator Test Runner"
echo "========================================="
echo ""

# Check if orchestrator directory exists
if [ ! -d "$ORCHESTRATOR_DIR" ]; then
    echo "❌ Error: self-reflexive-orchestrator-standalone directory not found"
    echo "Expected at: $ORCHESTRATOR_DIR"
    exit 1
fi

# Check if config exists
if [ ! -f "$CONFIG_FILE" ]; then
    echo "❌ Error: Configuration file not found"
    echo "Expected at: $CONFIG_FILE"
    exit 1
fi

# Check environment variables
if [ -z "$GITHUB_TOKEN" ]; then
    echo "❌ Error: GITHUB_TOKEN environment variable not set"
    exit 1
fi

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "❌ Error: ANTHROPIC_API_KEY environment variable not set"
    exit 1
fi

echo "✅ Environment variables configured"
echo ""

# Navigate to orchestrator directory
cd "$ORCHESTRATOR_DIR"

# Activate virtual environment
if [ ! -d "venv" ]; then
    echo "❌ Error: Virtual environment not found in orchestrator directory"
    echo "Run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

echo "Activating virtual environment..."
source venv/bin/activate

# Validate configuration
echo "Validating configuration..."
python3 -m src.cli -c "$CONFIG_FILE" validate-config
echo ""

# Show current issues
echo "Current test issues:"
gh issue list --repo justin4957/orchestrator-test-app --label "bot-approved"
echo ""

# Start orchestrator
echo "========================================="
echo "Starting Orchestrator in Supervised Mode"
echo "========================================="
echo ""
echo "The orchestrator will:"
echo "  1. Poll for issues with 'bot-approved' label"
echo "  2. Analyze and claim issues"
echo "  3. Implement solutions"
echo "  4. Create pull requests"
echo "  5. Monitor CI/CD"
echo "  6. Request approval for merges"
echo ""
echo "Monitor logs in another terminal:"
echo "  tail -f $ORCHESTRATOR_DIR/logs/test-app-orchestrator.log"
echo ""
echo "Press Ctrl+C to stop"
echo ""

python3 -m src.cli -c "$CONFIG_FILE" start --mode supervised
