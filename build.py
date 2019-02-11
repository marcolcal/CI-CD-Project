import os

def run(host,cmd):
    print host, cmd
    res = os.system('ssh deploy@{} "{}"'.format(host,cmd))
    if res!=0:
        raise "Error when running cmd!"


def main():
    print os.environ.get('GIT_BRANCH')
    if os.environ.get('GIT_BRANCH')=='origin/master':
        host='production-server.com'
    else:
        host='stage-server.com'
        
    run(host, "sudo rm -rf /home/deploy/html")
    os.system('scp -r $WORKSPACE deploy@{}:/home/deploy/html'.format(host))
    run(host, "rm -rf /home/deploy/html/.git")
    run(host, "sudo chown -R www-data:www-data /home/deploy/html")
    run(host, "sudo cp -R /home/deploy/html /var/www/")

if __name__ == '__main__':
    main()
