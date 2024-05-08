# puppet file to to correct a typo in a PHP configuration file that's causing an error apache causing error

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin']
}
