# Increase the USER LIMIT of the default file
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/8192/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}