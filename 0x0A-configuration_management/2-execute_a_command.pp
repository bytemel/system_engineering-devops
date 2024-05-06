<<<<<<< HEAD
# create a manifest that kills a process named killmenow
exec { 'kill':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin']
=======
# a manifest that kills a process named killmenow.

exec {  'killmenow':
  command => 'pkill -f killmenow',
  path    => ['/bin:/usr/bin'],
  onlyif  => 'pgrep -f killmenow',
>>>>>>> a41849d672782980c203ea90c992b734dd909763
}
