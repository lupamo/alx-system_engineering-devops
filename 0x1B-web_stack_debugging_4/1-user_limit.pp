# increasing the hard limit
exec {'increasing hard limit at holberton',
  command => "sed i '/^holberton hard/s/5/50000' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

# increasing soft limit
exec {'increasing soft limit',
  command => 'sed -i "/^holberton soft/s/4/50000" /etc/security/limiys.conf',
  path    => '/usr/local/bin/:/bin/'
}
