storage "consul" {
  address = "127.0.0.1:8500"
  path    = "vault/"
}

listener "tcp" {
 address     = "192.168.56.4:8200"
 tls_disable = 1
}

ui = true
