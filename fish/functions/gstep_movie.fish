function gstep_movie --wraps='gammastep -c .config/hypr/gammastep/gammas_conf1.ini & disown' --description 'alias gs_movie=gammastep -c .config/hypr/gammastep/gammas_conf1.ini & disown'
    gammastep -c .config/hypr/gammastep/gammas_conf1.ini & disown $argv

end
