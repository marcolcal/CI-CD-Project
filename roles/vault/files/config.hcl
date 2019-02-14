storage "consul" {
  address = "127.0.0.1:8500"
  path    = "vault/"
}

listener "tcp" {
 address     = "10.2.3.70:8200"
 tls_disable = 1
}

ui = true
