puppet file creating a school file in tmp folder 
file {'/tmp/school':
  sure    =>   'present',
  mode    =>   '0744',
  owner   =>   'www-data',
  group   =>   'www-data',
  content =>   'I love Puppet'
}
