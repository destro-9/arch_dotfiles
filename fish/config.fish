if status is-interactive
    # Commands to run in interactive sessions can go here
    eval "$(starship init fish)"
end
source "$HOME/.cargo/env.fish"
set MANPATH /usr/share/man
