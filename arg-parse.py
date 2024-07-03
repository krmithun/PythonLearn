import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-du", "--depot-username", help="Depot Username",
                        dest="depot_username", required=True)
    parser.add_argument("-dp", "--depot-password", help="Depot Password",
                        dest="depot_password", required=True)
    parser.add_argument("-si", "--sddc-ip", help="Sddc Username",
                        dest="sddc_ip", default="192.168.10.100")
    parser.add_argument("-su", "--sddc-username", help="Sddc Username",
                        dest="sddc_username", default="admin")
    parser.add_argument("-sp", "--sddc-password", help="Sddc Password",
                        dest="sddc_password", default="Vmware")
    args = parser.parse_args()

    print(args.depot_username, args.depot_password,
          args.sddc_username, args.sddc_password, args.sddc_ip)