# a procces called killmenow

exec {'pkill killmenow':
  path    => '/bin',
  command => 'pkill killmenow',
}
