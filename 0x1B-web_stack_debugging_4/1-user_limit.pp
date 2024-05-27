# Puppet file to increase user limit.


# Increase hard file limit for Holberton user.
exec { 'increase-file-hard-limit':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin/',
}


# Increase soft file limit for Holberton user.
exec { 'increase file limit':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',
}
