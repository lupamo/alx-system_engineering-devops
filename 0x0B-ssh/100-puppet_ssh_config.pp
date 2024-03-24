# configuring ssh client using puppet

class file_config {
  include stdlib
  file_line {'Password auth turn off':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}

file_line {'checking file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
}

