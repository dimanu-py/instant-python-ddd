#!/usr/bin/env sh
# Install the latest instant-python (ipy) release binary for the current platform.
#
# Usage:
#
#   curl -LsSf https://raw.githubusercontent.com/dimanu-py/instant-python/main/scripts/install.sh | sh
#
# Overridable via env vars:
#   IPY_BIN_DIR   install destination directory (default: $HOME/.local/bin)
set -eu

REPO="dimanu-py/instant-python"
BIN_DIR="${IPY_BIN_DIR:-$HOME/.local/bin}"
DEST="$BIN_DIR/ipy"

# --- detect platform -> release target triple --------------------------------
detect_target() {
  os="$(uname -s)"
  arch="$(uname -m)"
  case "$os-$arch" in
    Darwin-arm64)              target="aarch64-apple-darwin" ;;
    Linux-x86_64)              target="x86_64-unknown-linux-gnu" ;;
    Linux-aarch64|Linux-arm64) target="aarch64-unknown-linux-gnu" ;;
    *)
      echo "ipy: no prebuilt binary for $os-$arch." >&2
      echo "ipy: install via pipx or pip instead - see https://dimanu-py.github.io/instant-python/getting_started/installation/" >&2
      exit 1
      ;;
  esac
}

# --- download the matching release asset --------------------------------------
download_binary() {
  destination="$1"

  echo "ipy: downloading latest release for $target ..." >&2
  curl -fsSL -o "$destination" "https://github.com/$REPO/releases/latest/download/ipy-$target"
}

# --- move the binary into place and make it executable ------------------------
install_binary() {
  source="$1"

  echo "ipy: installing to $DEST ..." >&2
  mkdir -p "$BIN_DIR"
  mv "$source" "$DEST"
  chmod +x "$DEST"
}

# macOS: clear quarantine (no-op if absent) and ad-hoc sign so Gatekeeper allows it.
macos_allow_execution() {
  if [ "$os" = "Darwin" ]; then
    xattr -d com.apple.quarantine "$DEST" 2>/dev/null || true
    codesign --force --deep --sign - "$DEST"
  fi
}

verify_installation() {
  "$DEST" --version
}

# Warn the user if the install directory isn't already on their PATH.
warn_if_not_on_path() {
  case ":$PATH:" in
    *":$BIN_DIR:"*) ;;
    *)
      echo "" >&2
      echo "ipy: installed to $DEST, but $BIN_DIR is not on your PATH." >&2
      echo "ipy: add this to your shell profile: export PATH=\"$BIN_DIR:\$PATH\"" >&2
      ;;
  esac
}

main() {
  tmp="$(mktemp -d)"
  trap 'rm -rf "$tmp"' EXIT
  download="$tmp/ipy"

  detect_target
  download_binary "$download"
  install_binary "$download"
  macos_allow_execution
  verify_installation
  warn_if_not_on_path
}

main "$@"
