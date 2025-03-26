function gstep_xtreme --wraps='gammastep -c ~/.config/hypr/gammastep/gammas_conf2.ini' --description 'alias gstep_xtreme=gammastep -c ~/.config/hypr/gammastep/gammas_conf2.ini'
    gammastep -c ~/.config/hypr/gammastep/gammas_conf2.ini $argv & disown

end
