# Configure the OS for 'holberton' to login and open a file without any error message 
exec { 'hard limit':
  command => "sed -i 's/5/5000/' /etc/security/limits.conf",
  path    => '/bin'
}
exec { 'soft limit':
  command => "sed -i 's/4/5000/' /etc/security/limits.conf",
  path    => '/bin'
}
