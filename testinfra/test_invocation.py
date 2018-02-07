#!/usr/bin/env python
# coding=utf-8
from testinfra import get_host
from testinfra.modules.command import Command

# testinfra_hosts = [ "dnet@172.17.11.141" ]
# testinfra_hosts = [ "root@172.17.12.32" , "root@172.17.11.141" ]
#
# def test_nginx_is_installed(host):
#     nginx = host.package("git")
#     assert nginx.is_installed
#     # assert nginx.version.startswith("1.2")



# def test_host_local(host):
#     assert host.file("/hdapp/scripts/").exists


# def test_get_host() :
#     host = get_host("paramiko://root@172.17.12.32", sudo=True)
#     cmd = host.run("ls -l .")
#     assert cmd.rc == 0

# def test_ansible(host) :
#     print(host.ansible("file", "path=/etc/passwd")["mode"])
#     print(host.ansible("command", "echo foo", check=False)["stdout"])

# def test_run_expect(host) :
#     cmd = host.run_expect([0 ,2 ] , "ansible --help ")

# def test_test(host) :
#     cmd = host.run_test( "ansible --help ")
#     print(cmd)

# def test_file_content(host) :
#     content = host.file("/root/.docker/config.json").content_string
#     print(content)

# def test_interface(host) :
#     Interface = host.interface("ens160").addresses
#     print(Interface)

# def test_mountpoint(host) :
#     options = host.mount_point("/hdapp").get_mountpoints()
#     assert host.mount_point("/hdapp").exists

# def test_package(host) :
#     # Test packages status and version
#     package = host.package("ansible").is_installed
#     assert package
#     version = host.package("python").version
#     assert version.startswith("2.7")


# def test_pippackage(host) :
#     packages = host.pip_package.get_packages()
#     print(packages)
#     outdated_packages = host.pip_package.get_outdated_packages()
#     print(outdated_packages)

# def test_process(host) :
#     master = host.process.filter(user="root" , comm = "python" )
#     print(master)


# def test_Facter(host) :
#     facter = host.facter()
#     print(facter)

# def test_salt(host) :
#     salt = host.salt("pkg.version", "nginx")
#     print(salt)

# def test_service(host) :
#     assert host.service("docker").is_running
#     assert host.service("firewalld").is_enabled

# def test_socket(host) :
#     # assert host.socket("tcp://8000").is_listening
#     #
#     # print(host.socket.get_listening_sockets())
#
#     print(host.socket("tcp://8000").clients)


# def test_sudo(host) :
#     with host.sudo("dnet"):
#         print(host.check_output("cp  /hdapp/test2/envfile  /hdapp/test2/envfile_bak"))

# def test_supervisor(host) :
#     gunicorn = host.supervisor("docker")
#     print(gunicorn.is_running)

# def test_sysctl(host) :
#     print(host.sysctl("kernel.osrelease"))
#     print(host.sysctl("vm.dirty_ratio"))
#
#     assert host.sysctl("vm.dirty_ratio") == 30

# def test_systeminfo(host) :
#     print(host.system_info.type)
#     print(host.system_info.release)
#     print(host.system_info.distribution)
#     print(host.system_info.codename)

def test_user(host) :
    print(host.user("root").groups)
    print(host.user("root").group)
    print(host.user("root").home)
    print(host.user("root").shell)
    # print(host.user("dnet").expiration_date)