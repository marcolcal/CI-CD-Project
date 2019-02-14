import os

USER = 'vagrant'

def run(host,cmd):
    print host, cmd
    res = os.system('ssh {}@{} "{}"'.format(USER, host, cmd))
    if res != 0:
        raise RuntimeError("Error when running cmd!")

def main():
    print os.environ.get('GIT_BRANCH')
    if os.environ.get('GIT_BRANCH')=='origin/master':
        host='production-server.com'
    else:
        host='stage-server.com'

    run(host, "sudo rm -rf /home/{}/html".format(USER))
    os.system('scp -r $WORKSPACE {}@{}:/home/{}/html'.format(USER, host, USER))
    run(host, "rm -rf /home/{}/html/.git".format(USER))
    run(host, "sudo chown -R root:root /home/{}/html".format(USER))
    run(host, "sudo cp -R /home/{}/html /var/www/".format(USER))

if __name__ == '__main__':
    main()
