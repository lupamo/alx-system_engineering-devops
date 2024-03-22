# installing flask using pip with a puppet file

exec {'install_flask_2_1_0':
  command => 'pip3 install Flask==2.1.0',
  path    =>   ['/usr/local/bin', '/usr/bin'],
  unless  => 'pip3 show Flask | grep "Version: 2.1.0"',
}

exec { 'install_werkzeug':
  command => 'pip3 install Werkzeug==2.3.7',
  path    => ['/usr/local/bin', '/usr/bin'],
}