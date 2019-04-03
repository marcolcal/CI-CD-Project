Vagrant.configure("2") do |config|
     
   config.vm.box = "centos/7"
   
   #$script = <<-SCRIPT
   #  sudo yum install epel-release -y
   #  sudo yum install ansible -y
   #SCRIPT

   $scriptGit = <<-SCRIPT
     sudo yum update -y
     #sudo rpm -i package-1.2.3.rpm
     #sudo yum install curl -y
     sudo yum install policycoreutils-python -y
     sudo yum install openssh-server -y
     sudo systemctl enable sshd
     sudo systemctl start sshd
     sudo yum install postfix -y
     sudo systemctl enable postfix
     sudo systemctl start postfix
   SCRIPT

   $scriptJen = <<-SCRIPT
     sudo yum update -y
     sudo yum install wget -y
     sudo yum install java-1.8.0-openjdk-devel -y
     #sudo yum localinstall package-1.2.3.rpm 
     #sudo rpm -i package-1.2.3.rpm
     sudo yum install git -y 
   SCRIPT

   $scriptVault = <<-SCRIPT
     sudo yum update -y
     sudo yum install wget -y
     sudo yum install unzip -y
     sudo yum install libcap2-bin
     #sudo rpm -i package-1.2.3.rpm 
   SCRIPT

   $scriptRocket = <<-SCRIPT
     sudo yum update -y
    # sudo rpm -i package-1.2.3.rpm
     sudo echo -e "[mongodb-org-3.6]\nname=MongoDB Repository\nbaseurl=https://repo.mongodb.org/yum/redhat/7/mongodb-org/3.6/x86_64/\ngpgcheck=1\nenabled=1\ngpgkey=https://www.mongodb.org/static/pgp/server-3.6.asc" | sudo tee /etc/yum.repos.d/mongodb-org-3.6.repo
     sudo yum install -y curl && curl -sL https://rpm.nodesource.com/setup_8.x | sudo bash -
     sudo yum install -y gcc-c++ make mongodb-org nodejs
     sudo yum install -y epel-release && sudo yum install -y GraphicsMagick
     sudo npm install -g inherits n && sudo n 8.11.3 
   SCRIPT


   $scriptProd = <<-SCRIPT
   sudo yum update -y
   #sudo rpm -i package-1.2.3.rpm
   sudo yum install httpd -y
   sudo yum enable httpd -y
   SCRIPT


   $scriptPreprod = <<-SCRIPT
   sudo yum update -y
   #sudo rpm -i package-1.2.3.rpm
   sudo yum install httpd -y
   sudo yum enable httpd -y
   SCRIPT
   
   config.vm.define "gitlab" do |gitlab|
     gitlab.vm.hostname = "gitlab-server.com"
     config.vm.network "private_network", ip: "192.168.56.2"
     gitlab.vm.provider :virtualbox do |v|
       v.customize ["modifyvm", :id, "--memory", "2048"]
       v.customize ["modifyvm", :id, "--cpus", "1"]
     end 
     gitlab.vm.provision "shell", inline: $scriptGit
     gitlab.vm.provision "ansible" do |ans| 
       ans.playbook = "roles/gitlab.yml"
       #ans.tags = "gitlab_server"
     end
   end

   config.vm.define "jenkins" do |jenkins|
     jenkins.vm.hostname = "jenkins-server.com"
     config.vm.network "private_network", ip: "192.168.56.3"
     jenkins.vm.provider :virtualbox do |j|
       j.customize ["modifyvm", :id, "--memory", "2048"]
       j.customize ["modifyvm", :id, "--cpus", "1"]
     end
     jenkins.vm.provision "shell", inline: $scriptJen
     jenkins.vm.provision "ansible" do |ans| 
       ans.playbook = "roles/jenkins.yml"
     #  ans.tags = "jenkins_server"
     end
   end

   config.vm.define "vault" do |vault|
     vault.vm.hostname = "vault-server.com" 
     config.vm.network "private_network", ip: "192.168.56.4"
     vault.vm.provision "shell", inline: $scriptVault
     vault.vm.provision "ansible" do |ans| 
        ans.playbook = "roles/vault.yml"
        ans.limit = "all"
     #  ans.tags = "vault_server"
     end
   end
 
   config.vm.define "rocket" do |rocket|
     rocket.vm.hostname = "rocketchat-server.com"
     config.vm.network "private_network", ip: "192.168.56.5" 
     rocket.vm.provision "shell", inline: $scriptRocket
     #rocket.vm.provision "ansible" do |ans| 
     #  ans.playbook = "main.yml"
     #  ans.tags = "rocket_server"
     #end
   end

   config.vm.define "production" do |production|
     production.vm.hostname = "production-server.com"
     config.vm.network "private_network", ip: "192.168.56.6" 
     production.vm.provision "shell", inline: $scriptProd
     #production.vm.provision "ansible" do |ans| 
     #  ans.playbook = "main.yml"
     #  ans.tags = "production_server"
     #end
   end

   config.vm.define "preprod" do |preprod|
     preprod.vm.hostname = "preprod-server.com"
     config.vm.network "private_network", ip: "192.168.56.7" 
     preprod.vm.provision "shell", inline: $scriptPreprod
     preprod.vm.provision "ansible" do |ans| 
       ans.playbook = "roles/preprod.yml"
     #  ans.tags = "preprod_server"
     end
   end 


end
