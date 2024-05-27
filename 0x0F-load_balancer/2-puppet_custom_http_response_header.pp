# Installs a Nginx server with custome HTTP header

# Update server
exec { 'apt-get-update':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}

# Install Nginx
package { 'nginx':
  ensure   => present,
  provider => 'apt',
}

# Custom Nginx response header (X-Served-By: hostname)
file_line { 'X-Served-By':
  ensure => 'present',
  line   => 'add_header X-Served-By: $hostname',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
}

# Start Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => 'Package[nginx]',
}
