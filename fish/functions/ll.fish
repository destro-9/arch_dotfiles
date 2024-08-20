function ll --wraps='ls -l' --wraps='ls -al' --description 'alias ll=ls -al'
  ls -al $argv; 
end
