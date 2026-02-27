#!/bin/bash

echo "🌿 Starting Touch Grass Installation..."

# --- NEW: Anti-Sudo Guardrail ---
if [ "$EUID" -eq 0 ]; then
    echo "❌ ERROR: Put the sudo away!"
    echo "Running this as root changes your \$HOME directory to /root."
    echo "Please run this script normally (./install.sh) so it installs to your personal user folder."
    exit 1
fi
# --------------------------------

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="$HOME/.touch-grass"

mkdir -p "$INSTALL_DIR"
echo "📂 Vault ready at $INSTALL_DIR"

echo "🚚 Moving files..."
cp -f "$SCRIPT_DIR"/*.[pP][yY] "$INSTALL_DIR/" 2>/dev/null
cp -f "$SCRIPT_DIR"/*.[mM][pP]4 "$INSTALL_DIR/" 2>/dev/null
cp -f "$SCRIPT_DIR"/*.[mM][pP]3 "$INSTALL_DIR/" 2>/dev/null

if ! ls "$INSTALL_DIR"/*.py 1> /dev/null 2>&1; then
    echo "❌ Error: Python script didn't make it to the vault."
    exit 1
fi

echo "✅ Files successfully installed."

if [ -n "$ZSH_VERSION" ] || [ -f "$HOME/.zshrc" ]; then
    RC_FILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ] || [ -f "$HOME/.bashrc" ]; then
    RC_FILE="$HOME/.bashrc"
else
    RC_FILE="$HOME/.profile"
fi

if grep -q "TOUCH GRASS TERMINAL TRIGGERS" "$RC_FILE"; then
    echo "⚠️  Triggers already exist in $RC_FILE. Skipping injection."
    echo "🎉 Reinstall complete! Your files have been refreshed."
    exit 0
fi

echo "💉 Injecting terminal triggers..."
cat << 'EOF' >> "$RC_FILE"

# ==========================================
# 🌿 TOUCH GRASS TERMINAL TRIGGERS 🌿
# ==========================================
TOUCH_GRASS_SCRIPT=$(ls $HOME/.touch-grass/*.py | head -n 1)

alias tg="python3 $TOUCH_GRASS_SCRIPT"
alias gut="echo 'Did you mean git? Go touch some grass first.' && python3 $TOUCH_GRASS_SCRIPT"

git() {
    if [ "$1" = "push" ]; then
        command git "$@"
        if [ $? -eq 0 ]; then
            python3 $TOUCH_GRASS_SCRIPT
        fi
    else
        command git "$@"
    fi
}
EOF

echo "✅ Successfully injected triggers into $RC_FILE!"
echo "🎉 Installation complete. Restart your terminal or run: source $RC_FILE"