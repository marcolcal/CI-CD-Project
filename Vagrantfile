Vagrant.configure("2") do |config|
     
   config.vm.box = "bento/centos-7.6"
   
   #$script = <<-SCRIPT
   #  sudo yum install epel-release -y
   #  sudo yum install ansible -y
   #SCRIPT


   config.vm.define "gitlab" do |gitlab|
     gitlab.vm.hostname = "gitlab-server.com"
     config.vm.network "private_network", ip: "10.0.5.5"
     config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   config.vm.define "jenkins" do |jenkins|
     jenkins.vm.hostname = "jenkins-server.com"
     config.vm.network "private_network", ip: "10.0.5.10"
     #config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   config.vm.define "ansible" do |ansible|
     ansible.vm.hostname = "ansible-server.com"
     config.vm.network "private_network", ip: "10.0.5.15"
     config.vm.provision "shell", inline: $script
     config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   config.vm.define "hashicorp" do |hashicorp|
     hashicorp.vm.hostname = "hashicorp-server.com"
     config.vm.network "private_network", ip: "10.0.5.20"
     config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end
 
   config.vm.define "rocket" do |rocket|
     rocket.vm.hostname = "rocketchat-server.com"
     config.vm.network "private_network", ip: "10.0.5.25"
     config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   config.vm.define "production" do |production|
     production.vm.hostname = "production-server.com"
     config.vm.network "private_network", ip: "10.0.5.30"
     config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   config.vm.define "preprod" do |preprod|
     preprod.vm.hostname = "preprod-server.com"
     config.vm.network "private_network", ip: "10.0.5.35"
     config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end 


end
