# configuring ssh client using puppet

file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => '
  Host*
  IdentifyFile ~/.ssh/school
  PasswordAuthentication no'
}
