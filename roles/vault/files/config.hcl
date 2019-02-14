storage "consul" {
  address = "127.0.0.1:8500"
  path    = "vault/"
}

listener "tcp" {
 address     = "10.0.0.199:8200"
 tls_disable = 1
}

ui = true
