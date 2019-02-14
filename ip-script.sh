#!/bin/bash

#Get the ip addres and puts it on file 
vagrant ssh gitlab -c "ip addr show" | grep "inet*.10" && echo $date | awk '{ print $2 }'>> ~/project/cicd-Project/ip-addresses.txt
vagrant ssh jenkins -c "ip addr show" | grep "inet*.10" && echo $date | awk '{ print $2 }'>> ~/project/cicd-Project/ip-addresses.txt
vagrant ssh vault -c "ip addr show" | grep "inet*.10" && echo $date | awk '{ print $2 }'>> ~/project/cicd-Project/ip-addresses.txt
vagrant ssh rocket -c "ip addr show" | grep "inet*.10" && echo $date | awk '{ print $2 }'>> ~/project/cicd-Project/ip-addresses.txt
vagrant ssh production -c "ip addr show" | grep "inet*.10" && echo $date | awk '{ print $2 }'>> ~/project/cicd-Project/ip-addresses.txt
vagrant ssh preprod -c "ip addr show" | grep "inet*.10" && echo $date | awk '{ print $2 }'>> ~/project/cicd-Project/ip-addresses.txt

