Vagrant.configure("2") do |config|
     
   config.vm.box = "bento/centos-7.6"
   
   #$script = <<-SCRIPT
   #  sudo yum install epel-release -y
   #  sudo yum install ansible -y
   #SCRIPT

   $scriptGit = <<-SCRIPT
     sudo yum install curl -y
     sudo yum install policycoreutils-python -y
     sudo yum install openssh-server -y
     sudo yum install postfix -y
     sudo systemctl start postfix
     sudo systemctl enable postfix
   SCRIPT

   config.vm.define "gitlab" do |gitlab|
     gitlab.vm.hostname = "gitlab-server.com"
     #gitlab.vm.network "public_network", bridge: 'en0: Wi-Fi(AirPort)', ip: "10.0.5.5" 
     gitlab.vm.network "public_network", bridge: 'en0: Wi-Fi(AirPort)'
      config.vm.provision "shell", inline: $scriptGit
     #config.vm.network "private_network", ip: "10.0.5.5"
     #config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   config.vm.define "jenkins" do |jenkins|
     jenkins.vm.hostname = "jenkins-server.com"
     jenkins.vm.network "public_network", bridge: 'eth0: Wi-Fi(AirPort)'

     #jenkins.vm.network "private_network", ip: "10.0.5.10"
     #jenkins.vm.provision "ansible" do |ans| 
     #	ans.playbook = "jenkins.yml"
     #  ans.tags = "execute"
     #end
     #config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   #config.vm.define "ansible" do |ansible|
   #  ansible.vm.hostname = "ansible-server.com"
   #  config.vm.network "private_network", ip: "10.0.5.15"
   #  config.vm.provision "shell", inline: $script
   #  config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   #end

   config.vm.define "vault" do |vault|
     vault.vm.hostname = "vault-server.com" 
     vault.vm.network "public_network", bridge: 'eth0: Wi-Fi(AirPort)'
     #config.vm.network "private_network", ip: "10.0.5.20"
     #config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end
 
   config.vm.define "rocket" do |rocket|
     rocket.vm.hostname = "rocketchat-server.com"
     rocket.vm.network "public_network", bridge: 'eth0: Wi-Fi(AirPort)'
     #config.vm.network "private_network", ip: "10.0.5.25"
     #config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   config.vm.define "production" do |production|
     production.vm.hostname = "production-server.com"
     production.vm.network "public_network", bridge: 'eth0: Wi-Fi(AirPort)'
     #config.vm.network "private_network", ip: "10.0.5.30"
     #config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end

   config.vm.define "preprod" do |preprod|
     preprod.vm.hostname = "preprod-server.com"
     preprod.vm.network "public_network", bridge: 'eth0: Wi-Fi(AirPort)'
     #config.vm.network "private_network", ip: "10.0.5.35"
     #config.vm.network :forwarded_port, guest: 22, host: 2222, host_ip: "0.0.0.0", id: "ssh", auto_correct: true
   end 


end
