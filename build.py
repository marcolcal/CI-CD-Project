        
    run(host, "sudo rm -rf /home/deploy/html")
    os.system('scp -r $WORKSPACE deploy@{}:/home/deploy/html'.format(host))
    run(host, "rm -rf /home/deploy/html/.git")
    run(host, "sudo chown -R www-data:www-data /home/deploy/html")
    run(host, "sudo cp -R /home/deploy/html /var/www/")

if __name__ == '__main__':
    main()
