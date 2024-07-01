# Query: re.findall
# ContextLines: 1

713 results - 382 files

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_check_clock_ram_cpu.py:
  119                                  cvm_mem = cvm_output['memory']['used']
  120:                                 result = re.findall('.+%', mem_load)
  121                                  scm_mem_load = int(

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_cli.py:
  925              output = config.verify_sys_dump()
  926:             sys_dump_files = re.findall('case.+.tgz', output)
  927              output_sys_dump = cvm_shell.exec_command(

  930                  timeout=600)
  931:             cvm_sys_dump_files = re.findall(
  932                  'sysdump-cvm.+.tgz', output_sys_dump)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_connectivity.py:
  652              output = config.verify_sys_dump()
  653:             sys_dump_files = re.findall('case.+.tgz', output)
  654              output_sys_dump = cvm_shell.exec_command(

  656                  format(sys_dump_files[0]), timeout=600)
  657:             cvm_sys_dump_files = re.findall(
  658                  'sysdump-cvm.+.tgz', output_sys_dump)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_orchestration_agent.py:
  718      flow_rules = set(
  719:         re.findall(
  720              r'ingress=[\d\s]+egress=\d+',

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_rsyslog.py:
   996      parts_text = re.split(r'\[.*\]', data)
   997:     parts_bracket = re.findall(r'\[.*\]', data)
   998      assert len(parts_text) == 2, \

  1032                r' site-name="' + site_name + '" prefix="' + prefix + '"'
  1033:     x = re.findall(pattern, data)
  1034      if x is None:

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\connection_resource.py:
  184      result = cvm_shell.exec_command('journalctl --disk-usage')
  185:     mem = re.findall(r'\d.+M', result)
  186      output = mem[0].split('M')

dist-packages\portfolio_system_tests\legacy_gluon\libs\__init__.py:
  242      # This assumes the header names have no spaces in them
  243:     header_blocks = re.findall(r'\S+\s+(?=\S|$)', header)
  244      headers = [block.strip() for block in header_blocks]

dist-packages\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_collision_wanopt_stale_entry.py:
  433      # connection trace is the one which is newly created.
  434:     syn_dif_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  435      assert(str(SYN_SAME_SEQ) not in syn_dif_seq[-1]), \

  739          src_ip, HTTP_SRC_PORT, dst_ip, HTTP_DST_PORT)
  740:     syn_same_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  741      # Remove the loadbalance rule from ICs.

dist-packages\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_ic_owned_conn_reuse.py:
  349          var = ic.read_text_file(FILE_ORIG)
  350:         new_var = re.findall(r'id="\d{2,}"', var)
  351          new_vars = '{0}' .format(new_var[0]) + \

dist-packages\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_path_selection_customer_issues.py:
  343      #  connection trace is the one which is newly created.
  344:     syn_dif_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  345      assert (str(SYN_SAME_SEQ) not in syn_dif_seq[-1]), \

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_brownfield_sites_1Panther_CF3_ha_gateway.py:
  381      # Configuring the inteceptor interfaces.
  382:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  383                           str(test_objects.int_if1.cidr))

  391                                  int_if1.inpath.inpath_gateway)
  392:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  393                           str(test_objects.int_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_brownfield_sites_3Panther_CF3_ha_gateway.py:
  420      # Configuring the inteceptor interfaces.
  421:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  422                           str(test_objects.int_if1.cidr))

  430                                  int_if1.inpath.inpath_gateway)
  431:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  432                           str(test_objects.int_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_single_panther_catfish_L2_ha_gateway.py:
  328      # Configuring the inteceptor interfaces.
  329:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(test_objects.int_if1.cidr))

  338                                  int_if1.inpath.inpath_gateway)
  339:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  340                           str(test_objects.int_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_single_panther_catfish_L3_ha_gateway.py:
  374      # Configuring the inteceptor interfaces.
  375:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  376                           str(test_objects.int_if1.cidr))

  384                                  int_if1.inpath.inpath_gateway)
  385:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  386                           str(test_objects.int_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_catfish_on_branch2.py:
  328      # Configuring the inteceptor interfaces.
  329:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(int_if1.cidr))

  337                                  ip_address=int_if1.inpath.inpath_gateway)
  338:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  339                           str(int_if2.cidr))

  368      # Configuring the IC1 inpath1 interface.
  369:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  370                                   str(phy_int1_if1.cidr))

  383      # Configuring the IC1 inpath2 interface.
  384:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  385                                   str(phy_int1_if2.cidr))

  426      # Configuring the IC2 inpath1 interface.
  427:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  428                                   str(phy_int2_if1.cidr))

  441      # Configuring the IC2 inpath2 interface.
  442:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  443                                   str(phy_int2_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_L3_single_catfish.py:
  319      # Configuring the inteceptor interfaces.
  320:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  321                           str(int_if1.cidr))

  328                                  ip_address=int_if1.inpath.inpath_gateway)
  329:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(int_if2.cidr))

  359      # Configuring the IC1 inpath1 interface.
  360:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  361                                   str(phy_int1_if1.cidr))

  374      # Configuring the IC1 inpath2 interface.
  375:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  376                                   str(phy_int1_if2.cidr))

  417      # Configuring the IC2 inpath1 interface.
  418:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  419                                   str(phy_int2_if1.cidr))

  432      # Configuring the IC2 inpath2 interface.
  433:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  434                                   str(phy_int2_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_single_panther.py:
  266      # Configuring the inteceptor interfaces.
  267:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  268                           str(test_objects.int_if1.cidr))

  276                                  int_if1.inpath.inpath_gateway)
  277:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  278                           str(test_objects.int_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways.py:
  330      # Configuring the inteceptor interfaces.
  331:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  332                           str(int_if1.cidr))

  339                                  ip_address=int_if1.inpath.inpath_gateway)
  340:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  341                           str(int_if2.cidr))

  370      # Configuring the IC1 inpath1 interface.
  371:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  372                                   str(phy_int1_if1.cidr))

  385      # Configuring the IC1 inpath2 interface.
  386:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  387                                   str(phy_int1_if2.cidr))

  428      # Configuring the IC2 inpath1 interface.
  429:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  430                                   str(phy_int2_if1.cidr))

  443      # Configuring the IC2 inpath2 interface.
  444:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  445                                   str(phy_int2_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_split_site.py:
  325      # Configuring the inteceptor interfaces.
  326:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  327                           str(int_if1.cidr))

  334                                  ip_address=int_if1.inpath.inpath_gateway)
  335:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  336                           str(int_if2.cidr))

  365      # Configuring the IC1 inpath1 interface.
  366:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  367                                   str(phy_int1_if1.cidr))

  380      # Configuring the IC1 inpath2 interface.
  381:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  382                                   str(phy_int1_if2.cidr))

  423      # Configuring the IC2 inpath1 interface.
  424:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  425                                   str(phy_int2_if1.cidr))

  438      # Configuring the IC2 inpath2 interface.
  439:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  440                                   str(phy_int2_if2.cidr))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_dc_uplink.py:
  266          else:
  267:             dc_uplinks_teps['Internet'] = re.findall(r'[0-9]+(?:\.[0-9]+){3}',
  268                                                       dc_uplink.net)

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_change_panther_db_address.py:
  272      old_sd_wan = resources.ic1_model.show_sd_wan().raw
  273:     old_sd_wan_addr_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  274                                        str(old_sd_wan))

dist-packages\portfolio_system_tests\legacy_shsaas_tests\tests\SH\sepia\conftest.py:
  110      result = client_shell.exec_command(cmd, error_expected=True)
  111:     return (len(re.findall("[0-9]+", result)))
  112  

  189              match = "TCP_MISS/200 [0-9]* GET " + url
  190:         if (len(re.findall(match, result)) < 1):
  191              raise VerificationError(

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_manage_appliances.py:
  192      group_info = resources.scc_actor.model.show_cmc_group(group=group).raw
  193:     lines = re.findall(r'.*/.*', group_info)
  194      return [i.split()[0] for i in lines]

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
  50          for x in range(1, 10):
  51:             subnet = re.findall(subnet_regex, delete_status)[0]
  52              port_id = commands.getoutput(

  66          for x in range(1, 10):
  67:             router_subnet = re.findall(router_regex, delete_status)[0]
  68              cmd = 'neutron router-update %s --routes action=clear' % (

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\populate_networks_subnets_images.py:
  75      site_id = all_sites[site]
  76:     branch_number = re.findall(r"[0-9]+$", site)[0]
  77      image_name = "vgw" + branch_number + "_pod" + str(pod) + "_image"

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\scale2_appliance_health_report.py:
  169      else:
  170:         node_memory_usage = re.findall(r'[0-9]+%', node_memory_string)[0]
  171      node_configuration = node['state']

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\script_appliance_health_report.py:
  182      else:
  183:         node_memory_usage = re.findall(r'[0-9]+%', node_memory_string)[0]
  184      node_configuration = node['state']

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\appliance.py:
  410              break
  411:         if (len(re.findall('inet6 addr', interface[1]))) > 1:
  412              interface[1] = interface[1]. \

  454      if pattern:
  455:         return re.findall(pattern, if_names)
  456      return if_names.split('\n')

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\traffic.py:
  104                            min_poll_interval=5):
  105:         accepted_flows = re.findall(r'Accepted: \d+', output)
  106          no_of_flows = [int(flow.split()[1]) for flow in accepted_flows]

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler_client.py:
  70      try:
  71:         client_ip = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', response)[0])
  72      except IndexError:
  73          response = request_new_ip(mgmt_ip, interface, dh_request)
  74:         client_ip = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', response)[0])
  75      find_mac = re.compile('([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
  76:     client_mac = (re.findall(find_mac, response)[0])
  77      if ipaddress.ip_address(client_ip):

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler.py:
  310  
  311:     split_var = re.findall(r'\s(\bZscaler\s\bCloud):', header)
  312      paragraph = header.split(split_var[0])[2]

  315          header_city = \
  316:             re.findall(r'\s[A-Z]*[a-z]*\s[A-Z]+[a-z]+\s[IV, III, II]*',
  317                         paragraph)[0].strip()
  318      else:
  319:         header_city = re.findall(r'[A-Z]*[a-z]*\s[A-Z]+[a-z]+\s[IV, III, II]*',
  320                                   paragraph)[0].strip()
  321:     header_cloud = re.findall(r'\s(\bzscalertwo).', paragraph)[0]
  322  

dist-packages\portfolio_system_tests\legacy_test_steelbranch\tests\performance\test_pload_http_performance.py:
  42      data = []
  43:     rows = re.findall(pattern, output)
  44      for row in rows:

  52      pattern = (r'.*::.* = .*')
  53:     row = re.findall(pattern, output)
  54      data = row[0].split('=')[1].split(':')[1]

  70          output = monitor_setup.shell.exec_command(cmd)
  71:         rows = re.findall(pattern, output)
  72  

dist-packages\portfolio_system_tests\legacy_test_steelbranch\tests\physical\uplinks\test_backup_uplink.py:
  105      cmd = node_shell.exec_command('traceroute 8.8.8.8 -m 1')
  106:     default_route = re.findall(r'\(([^)]+)', cmd)
  107      return default_route[1]

dist-packages\portfolio_system_tests\legacy_test_steelbranch\tests\wan_uplink_failover\test_uplink_ping_interval.py:
  153      for line in lines:
  154:         matches.append(re.findall(r'\d{2}:\d{2}\.\d{2}', line)[0])
  155          # 09:21:58.379343 IP 8.8.8.8 > 192.168.0.10: ICMP echo reply

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_zebos_config_check_bgp.py:
  48                  'remote-as' in line.strip():
  49:             gw_output['neighbor_ips'].append(re.findall(
  50                  r'[0-9]+(?:\.[0-9]+){3}', line)[0])
  51:             gw_output['neighbor_as'].append(re.findall(
  52                  r'remote-as (\w+)', line)[0])

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\test_bgp_ha_uplink.py:
  88          version = OS.get(gateway).shell.exec_command('imish -e "show ip bgp"')
  89:         zebos_version = re.findall(r"\d\.\d.\d", version)[0]
  90          logger.info("ZebOS-XP version is {}".format(zebos_version))

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_zebos_config_change.py:
  38                  re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  39:             gw_output['network'].append(re.findall(
  40                  r'[0-9]+(?:\.[0-9]+){3}', line)[0])
  41:             gw_output['area'].append(re.findall(
  42                  r'[0-9]+(?:\.[0-9]+){3}', line)[1])

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_remote_site_ospf_learning.py:
  36      for line in route.splitlines()[1:]:
  37:         if re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line):
  38              gw_output_routes.append(
  39:                 re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line)[0])
  40      return gw_output_routes

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\ospf_routemap\test_remote_site_states.py:
  35      for line in route.splitlines()[1:]:
  36:         if re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line):
  37              gw_output_routes.append(
  38:                 re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line)[0])
  39      return gw_output_routes

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\helpers\utils.py:
  171      route_op = container_shell.exec_command("vtysh -c 'show ip route'")
  172:     found = re.findall(r'(\d+\.\d+\.\d+\.\d+\/\d+)\s.+\s(\d+\.\d+\.\d+\.\d+)',
  173                         route_op)

dist-packages\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\openstack-tests\openstack_ops.py:
  114          if output[0]:
  115:             available_volume_ids_list = re.findall(r'\w+-\w+-\w+-\w+-\w+', output[1])
  116          else:

dist-packages\portfolio_system_tests\legacy_vsh_tests\provisioning\get_build_from_deliverable.py:
  19      data = json.loads(resp.text)
  20:     int_array = re.findall(r'\d+', data["build"]["name"])
  21      print(str(int_array[-1]))

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\conftest.py:
  314          if (get_peer_ip):
  315:             peer_ip = re.findall(r'\d+\.\d+\.\d+\.\d+', output.raw)
  316              assert (len(peer_ip) == 1)

  880          if windows:
  881:             return re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  882                                output)[1]

  892          output = client_sh.exec_command("nslookup public.boxcloud.com")
  893:         return re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  894                            output)[1]

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\komodo\test_unsuccessful_edit_deployment.py:
  106                         "to support the number of users")
  107:             if not(re.findall(pattern, res.text)):
  108                  raise VerificationError(

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\truk\test_cfe_load_balancing.py:
  24      result = output.raw
  25:     m = re.findall(r'\(.*\)', result)
  26      if (len(m) != len(output.parsed_as_key_val)):
  27          raise ValueError("ZAK Peer Port numbers mismatch found")
  28:     ports = re.findall(r'\d+', m[0])
  29      assert (len(ports) == 2)

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
  1625              try:
  1626:                 find = re.findall(r'STACK TRACE.*', output, re.MULTILINE)
  1627                  assert(len(find) == 0)

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\shm_tests\shm_helper.py:
  222                  "nslookup rvbd496-my.sharepoint.com")
  223:             dest_ip = re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  224                                   output)[1]

  227                  "nslookup public.boxcloud.com")
  228:             dest_ip = re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  229                                   output)[1]

dist-packages\portfolio_system_tests\spoon_tests\libs\configure.py:
  112                  model_str = show_version['product model']
  113:                 model_str = re.findall(r'\((.*)\)', model_str)[0]
  114                  cache['version'] = LegacyVersion(version)

dist-packages\portfolio_system_tests\spoon_tests\libs\rios_pxe_install.py:
  178  
  179:         name_servers = re.findall(r'Name server: (\S+) \(configured\)', output)
  180          for name_server in name_servers:

  182  
  183:         dns_suffixes = re.findall(r'Domain name: (\S+) \(configured\)', output)
  184          for dns_suffix in dns_suffixes:

dist-packages\portfolio_system_tests\spoon_tests\libs\verification.py:
  588              min_data_redux_pcent):
  589:         percentages = re.findall(r'(\d+)%', connection_summary)
  590          if not percentages:

dist-packages\portfolio_system_tests\spoon_tests\libs\zak_log_verifier.py:
  146          if 'messages' in log_dict['name']:
  147:             match_list = re.findall(r'\d+', log_dict['name'])
  148              sh_log_branch_list.append(match_list[0])

dist-packages\portfolio_system_tests\winsec\conftest.py:
  172      actual_config = server_sh.model.show_hosts().raw
  173:     dns_servers = re.findall(
  174          r'Name server:\s+(\d+\.\d+\.\d+\.\d+)\s+', actual_config)

  178      pattern = re.compile(regex)
  179:     domains = re.findall(pattern, actual_config)
  180      for domain in domains:

dist-packages\portfolio_system_tests\winsec\tests\test_adp_upgrade_sanity.py:
  57      # build number is 9
  58:     build = re.findall(r'/(?!.*/adproxy/.*/)(\d+)', image_url).pop()
  59  

dist-packages\pq_core\lab\os\networking\ipfw.py:
  218                   r'via\s+(\S+)\n')
  219:         pipes = re.findall(regex, pipes_list)
  220          pipe_list = []

dist-packages\pq_core\runtime\json.py:
  38      data_copy = copy.copy(data)
  39:     refs = re.findall(r"\$(\w+)\$", data_copy)
  40      subs_done = []

dist-packages\pq_core\runtime\yaml.py:
  50      """Turn camel case into underscore separated."""
  51:     parts = re.findall('[A-Z][^A-Z]*', name)
  52      return '_'.join([part.lower() for part in parts])

dist-packages\pq_lib\tools\dnsname.py:
  130  
  131:         Basically ``re.findall()``, but only matches once per line, and always
  132          returns a list of matches.

dist-packages\pq_lib\tools\ipfw.py:
  229                   r'via\s+(\S+)\n')
  230:         pipes = re.findall(regex, pipes_list)
  231          pipe_list = []

dist-packages\pq_lib\tools\nfstest.py:
  220          err = ''
  221:         logfile = re.findall(r'Logfile:\s*(.*)', summary)[0]
  222          if 'ERRORS:' in summary:

dist-packages\pq_lib\tools\rsnmp.py:
  191          pattern = (r'(iso.*) = .*')
  192:         oid_output = re.findall(pattern, output_snmp_walk)
  193          if oid_output != []:

dist-packages\pq_orclib\commandserver\__init__.py:
  71          cmdsrv = self._cmdsrv.exec_command_server_command(ic, str(cmd))
  72:         match = re.findall('1 Flow entries added', cmdsrv)
  73          if not match:

dist-packages\pq_orclib\general_cmc_operations\__init__.py:
  92          showscc = sh_model.show_scc().raw
  93:         if re.findall(r'Connected', showscc) == [
  94                  'Connected', 'Connected'] and current_cmc == cmc_host:

dist-packages\pq_orclib\panther\cluster.py:
  383                          flags=re.IGNORECASE):
  384:                     if ltep[i] in re.findall(
  385                              r'[0-9]+(?:\.[0-9]+){3}',

dist-packages\venv\Lib\site-packages\chardet\charsetprober.py:
  85          # the end.
  86:         words = re.findall(b'[a-zA-Z]*[\x80-\xFF]+[a-zA-Z]*[^a-zA-Z\x80-\xFF]?',
  87                             buf)

dist-packages\venv\Lib\site-packages\dateutil\rrule.py:
  1526              lambda x: (x.upper(), x),
  1527:             re.findall('TZID=(?P<name>[^:]+):', s)
  1528          ))

dist-packages\venv\Lib\site-packages\et_xmlfile\tests\common_imports.py:
   20      l = []
   21:     for part in re.findall('([0-9]+|[^0-9.]+)', version_string):
   22          try:

  302  def unentitify(xml):
  303:     for entity_name, value in re.findall("(&#([0-9]+);)", xml):
  304          xml = xml.replace(entity_name, unichr(int(value)))

dist-packages\venv\Lib\site-packages\eventlet\support\greendns.py:
  198  
  199:         return self.LINES_RE.findall(udata)
  200  

dist-packages\venv\Lib\site-packages\fabric\operations.py:
  231                      validate += r'$'
  232:                 result = re.findall(validate, value)
  233                  if not result:

dist-packages\venv\Lib\site-packages\importlib_metadata\__init__.py:
  219          match = self.pattern.match(self.value)
  220:         return re.findall(r'\w+', match.group('extras') or '')
  221  

dist-packages\venv\Lib\site-packages\jinja2\filters.py:
  940      """Count the words in that string."""
  941:     return len(_word_re.findall(soft_str(s)))
  942  

dist-packages\venv\Lib\site-packages\jinja2\lexer.py:
  207      """
  208:     return len(newline_re.findall(value))
  209  

dist-packages\venv\Lib\site-packages\pbr\git.py:
  315          co_authors_out = _run_git_command('log', git_dir)
  316:         co_authors = re.findall('Co-authored-by:.+', co_authors_out,
  317                                  re.MULTILINE)

dist-packages\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  513      for line_number, line in lines_enum:
  514:         for env_var, var_name in ENV_VAR_RE.findall(line):
  515              value = os.getenv(var_name)

dist-packages\venv\Lib\site-packages\pip\_vendor\chardet\charsetprober.py:
  85          # the end.
  86:         words = re.findall(b'[a-zA-Z]*[\x80-\xFF]+[a-zA-Z]*[^a-zA-Z\x80-\xFF]?',
  87                             buf)

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\compat.py:
  422  
  423:             matches = cookie_re.findall(line_string)
  424              if not matches:

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  725  
  726:                 archs = re.findall(r'-arch\s+(\S+)', cflags)
  727                  archs = tuple(sorted(set(archs)))

dist-packages\venv\Lib\site-packages\pip\_vendor\html5lib\_inputstream.py:
  287      def characterErrorsUCS4(self, data):
  288:         for _ in range(len(invalid_unicode_re.findall(data))):
  289              self.errors.append("invalid-codepoint")

dist-packages\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  899          clean = []
  900:         for prop, value in re.findall(r"([-\w]+)\s*:\s*([^:;]*)", style):
  901              if not value:

dist-packages\venv\Lib\site-packages\pip\_vendor\requests\utils.py:
  455  
  456:     return (charset_re.findall(content) +
  457:             pragma_re.findall(content) +
  458:             xml_re.findall(content))
  459  

dist-packages\venv\Lib\site-packages\pyeapi\api\acl.py:
  105          response = {'standard': {}, 'extended': {}}
  106:         for acl_type, name in acl_re.findall(self.config):
  107              acl = self.get(name)

dist-packages\venv\Lib\site-packages\pyeapi\api\bgp.py:
  101          regexp = r'network (.+)/(\d+)(?: route-map (\w+))*'
  102:         matches = re.findall(regexp, config)
  103          for (prefix, mask, rmap) in matches:

  202          collection = dict()
  203:         for neighbor in re.findall(r'neighbor ([^\s]+)', config):
  204              collection[neighbor] = self.get(neighbor)

dist-packages\venv\Lib\site-packages\pyeapi\api\interfaces.py:
  110          response = dict()
  111:         for name in interfaces_re.findall(self.config):
  112              interface = self.get(name)

  668          config = self.node.enable(command, 'text')
  669:         return re.findall(r'\b(?!Peer)Ethernet[\d/]*\b',
  670                            config[0]['result']['output'])

  890      def _parse_vlans(self, config):
  891:         vlans = frozenset(re.findall(r'vxlan vlan (\d+)', config))
  892          values = dict()

dist-packages\venv\Lib\site-packages\pyeapi\api\ipinterfaces.py:
  137          response = dict()
  138:         for name in interfaces_re.findall(self.config):
  139              interface = self.get(name)

dist-packages\venv\Lib\site-packages\pyeapi\api\mlag.py:
  185          interfaces = dict()
  186:         names = re.findall(r'^interface (Po.+)$', self.config, re.M)
  187          for name in names:

dist-packages\venv\Lib\site-packages\pyeapi\api\ntp.py:
  95      def _parse_servers(self, config):
  96:         matches = re.findall(r'ntp server ([\S]+) ?(prefer)?', config, re.M)
  97          value = []

dist-packages\venv\Lib\site-packages\pyeapi\api\ospf.py:
  136          regexp = r'network (.+)/(\d+) area (\d+\.\d+\.\d+\.\d+)'
  137:         matches = re.findall(regexp, config)
  138          for (network, netmask, area) in matches:

  153          regexp = r'redistribute .*'
  154:         matches = re.findall(regexp, config)
  155          for line in matches:

dist-packages\venv\Lib\site-packages\pyeapi\api\routemaps.py:
  103          routemaps_re = re.compile(r'^route-map\s([\w-]+)\s\w+\s\d+$', re.M)
  104:         for name in routemaps_re.findall(self.config):
  105              routemap = self.get(name)

  114          entries = list()
  115:         for entry in routemap_re.findall(self.config):
  116              resource = dict()

  142          match_re = re.compile(r'^\s+match\s(.+)$', re.M)
  143:         return dict(match=match_re.findall(config))
  144  

  146          set_re = re.compile(r'^\s+set\s(.+)$', re.M)
  147:         return dict(set=set_re.findall(config))
  148  

dist-packages\venv\Lib\site-packages\pyeapi\api\staticroute.py:
  151          # Find all the ip routes in the config
  152:         matches = ROUTES_RE.findall(self.config)
  153  

dist-packages\venv\Lib\site-packages\pyeapi\api\stp.py:
  242          response = dict()
  243:         for name in interfaces_re.findall(self.config):
  244              if name[0:2] in ['Et', 'Po']:

dist-packages\venv\Lib\site-packages\pyeapi\api\switchports.py:
  114          """
  115:         values = re.findall(r'switchport trunk group ([^\s]+)', config, re.M)
  116          return dict(trunk_groups=values)

  171          response = dict()
  172:         for name in interfaces_re.findall(self.config):
  173              interface = self.get(name)

dist-packages\venv\Lib\site-packages\pyeapi\api\system.py:
  107          motd_value = login_value = None
  108:         matches = re.findall('^banner\s+(login|motd)\s?$\n(.*?)$\nEOF$\n',
  109                               self.config, re.DOTALL | re.M)

dist-packages\venv\Lib\site-packages\pyeapi\api\users.py:
  110          """
  111:         users = self.users_re.findall(self.config, re.M)
  112          resources = dict()

dist-packages\venv\Lib\site-packages\pyeapi\api\varp.py:
  161          interfaces_re = re.compile(r'^interface\s(Vlan\d+)$', re.M)
  162:         for name in interfaces_re.findall(self.config):
  163              interface_detail = self.get(name)

  198                                  re.M)
  199:         return dict(addresses=virt_ip_re.findall(config))
  200  

dist-packages\venv\Lib\site-packages\pyeapi\api\vlans.py:
  158          """
  159:         values = TRUNK_GROUP_RE.findall(config)
  160          return dict(trunk_groups=values)

  171          response = dict()
  172:         for vid in vlans_re.findall(self.config):
  173              response[vid] = self.get(vid)

dist-packages\venv\Lib\site-packages\pyeapi\api\vrfs.py:
  141          response = dict()
  142:         for vrf in vrfs_re.findall(self.config):
  143              response[vrf] = self.get(vrf)

dist-packages\venv\Lib\site-packages\pyeapi\api\vrrp.py:
  199          # a set of the unique vrid numbers
  200:         match = set(re.findall(r'^\s+(?:no |)vrrp (\d+)', config, re.M))
  201          if not match:

  241          # Find the available interfaces
  242:         interfaces = re.findall(r'^interface\s(\S+)', self.config, re.M)
  243  

  282      def _parse_secondary_ip(self, config, vrid):
  283:         matches = re.findall(r'^\s+vrrp %s ip (\d+\.\d+\.\d+\.\d+) '
  284                               r'secondary$' % vrid, config, re.M)

  333      def _parse_track(self, config, vrid):
  334:         matches = re.findall(r'^\s+vrrp %s track (\S+) '
  335                               r'(decrement|shutdown)(?:( \d+$|$))' %

dist-packages\venv\Lib\site-packages\pylint\checkers\spelling.py:
  148              # Skip words with digits.
  149:             if len(re.findall(r"\d", word)) > 0:
  150                  continue

  153              # they are probaly class names.
  154:             if (len(re.findall("[A-Z]", word)) > 0 and
  155:                     len(re.findall("[a-z]", word)) > 0 and
  156                      len(word) > 2):

dist-packages\venv\Lib\site-packages\pylint\extensions\check_docs.py:
  246              # Sphinx type declarations
  247:             params_with_type += re.findall(
  248                  self.re_sphinx_type_in_docstring, doc)

dist-packages\venv\Lib\site-packages\pythonwin\pywin\idle\AutoExpand.py:
  61          before = self.text.get("1.0", "insert wordstart")
  62:         wbefore = re.findall(r"\b" + word + r"\w+\b", before)
  63          del before
  64          after = self.text.get("insert wordend", "end")
  65:         wafter = re.findall(r"\b" + word + r"\w+\b", after)
  66          del after

dist-packages\venv\Lib\site-packages\pythonwin\pywin\scintilla\view.py:
  464  			try:
  465: 				l = re.findall(r"\b"+left+"\.\w+",text)
  466  			except re.error:

dist-packages\venv\Lib\site-packages\requests\utils.py:
  442  
  443:     return (charset_re.findall(content) +
  444:             pragma_re.findall(content) +
  445:             xml_re.findall(content))
  446  

dist-packages\venv\Lib\site-packages\rflint\rules\otherRules.py:
  41          if match:
  42:             count = len(re.findall(r'\n', match.group(0)))
  43              if count > self.max_allowed:

dist-packages\venv\Lib\site-packages\test\HPE3ParMockServer_flask.py:
  671  def _parse_query(query):
  672:     wwns = re.findall("wwn==([0-9A-Z]*)", query)
  673:     iqns = re.findall("name==([\w.:-]*)", query)
  674      parsed_query = {"wwns": wwns, "iqns": iqns}

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\cli\oa\oa_operation.py:
  119          output = out.stdout
  120:         index = re.findall("Record\[\d+\]", output)
  121          count = 0

  123          for i in range(len(index)):
  124:             ind = re.findall("\[\d+\]", index[i])
  125              ind1 = str(ind)

  128              output2 = out2.stdout
  129:             if re.findall("SSO Server record deleted", output2):
  130                  logger.debug("Successfully deleted the certificate")

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\cli\traffic\vsp.py:
  152  
  153:         items = re.findall(r'\d+\:\s([\-\w]+)(?:\.(\d+)@\w+)?\:\s[\w\W]*?link\/[\s\w]+((?:\w{2}\:){5}\w{2})\sbrd\s(?:\w{2}\:){5}\w{2}(?:\s*inet\s((?:\d{1,3}\.){3}\d{1,3})\/(\d{1,2})\sbrd\s((?:\d{1,3}\.){3}\d{1,3}))?', ip_address_output, re.I)
  154          if not items:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\performance\listener.py:
  789              if 'URL' in mess:
  790:                 match = re.findall(
  791                      'URL\s+([A-Z]+)\s\https:\/\/([^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})',

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\business_logic\servers\serverprofiles.py:
  5202          name = ui_lib.get_text(GeneralServerProfilesElements.LocalStorage.LogicalJbod.ID_TEXT_ZONED_HARD_DRIVE_NAME % (mezzID, drivename, drivenumber), timeout, fail_if_false)
  5203:         hdd_number = re.findall(r'\d+', name.split(',')[2])
  5204          logger.info("hdd number is %s" % hdd_number)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\business_logic\storage\volumes.py:
   276          '''
   277:         name_variables = re.findall(r'\{(.*?)\}', name)
   278          if len(name_variables) > 0:

  1125          logger.debug("input name '%s'" % name)
  1126:         name_variables = re.findall(r'\{(.*?)\}', name)
  1127          ui_lib.wait_for_element_and_click(CreateVolumeSnapshotElements.ID_INPUT_NAME, timeout, fail_if_false)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\servers\serverhardware.py:
  2070              import re
  2071:             appliance_url = re.findall(r'^https://[\d.]*', s2l._current_browser().get_current_url())[0]
  2072              # s2l = ui_lib.get_s2l()

  2161              import re
  2162:             appliance_url = re.findall(r'^https://[\d.]*', s2l._current_browser().get_current_url())[0]
  2163              # s2l = ui_lib.get_s2l()

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\ACI_Istanbul\APICOperations.py:
    66              error = ["Could not login to APIC."]
    67:             error += re.findall("text\":\"(.*)\"", res.content)
    68              raise Exception(" ".join(error))

  2137              error = ["Could not login to APIC."]
  2138:             error += re.findall("text\":\"(.*)\"", res.content)
  2139              raise Exception(" ".join(error))

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\DEA\HAL\util\gen_help_oracle.py:
  34  
  35:     cmds = re.findall('^\s+([\w\-]+)\s+\w',help_msg,re.M)
  36      return cmds

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\Mellanox\Manganese_L2_features\backping.py:
  257          if iLO_details['type'] == 'Gen10':
  258:             adapter_name = re.findall(".*Name----(PCIe.*)C:", output)
  259              adapter_names.append(adapter_name[0])

  261          if iLO_details['type'] == 'Gen9':
  262:             adapter_name = re.findall(".*Name----(Ethernet.*)C:", output)
  263              adapter_names.append(adapter_name[0])

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\Mellanox\Manganese_L2_features\Server_Operation_Factory_Reset.py:
  143      print strout
  144:     cmd = re.findall(r'(.\\disk.*.dat)', strout)
  145:     fileout = re.findall(r'([0-9][0-9]-.*.txt)', strout)
  146      print cmd

  149          if not fileout:
  150:             return str(re.findall(r'(.Drive.*.!)', strout)[0]), fileout, None
  151          if fileout[0]:

  172      print strout
  173:     cmd = re.findall(r'(.\\disk.*.dat)', strout)
  174:     exeout = re.findall(r'(Test .*.ms)', strout)
  175      print cmd

  530          if iLO_details['type'] == 'Gen10':
  531:             adapter_name = re.findall(".*Name----(PCIe.*)C:", output)
  532              adapter_names.append(adapter_name[0])

  534          if iLO_details['type'] == 'Gen9':
  535:             adapter_name = re.findall(".*Name----(Ethernet.*)C:", output)
  536              adapter_names.append(adapter_name[0])

  637          print "1st output %s " % output
  638:         bond = re.findall("Connection\\s+.*(bond-\\w+).*\\s+", output)
  639          print "bond name %s " % bond

  649              print "2nd output %s " % output
  650:             bond_slave_connection_names = re.findall("Connection\\s+.*\'(bond-\\w+.*)\'.*\\s+", output)
  651              print "bond slave names name %s " % bond_slave_connection_names

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\Mellanox\Manganese_L2_features\server_operations_Telemetry.py:
   740          for line in lines:
   741:             match = re.findall(r"\w+-\w+-\w+-\w+-\w+-\w+", line)
   742              if match != []:

  1002          if iLO_details['type'] == 'Gen10':
  1003:             adapter_name = re.findall(".*Name----(PCIe.*)C:", output)
  1004              adapter_names.append(adapter_name[0])

  1006          if iLO_details['type'] == 'Gen9':
  1007:             adapter_name = re.findall(".*Name----(Ethernet.*)C:", output)
  1008              adapter_names.append(adapter_name[0])

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\Mellanox\Manganese_L2_features\ServerOperations_IGMP.py:
  339          print (ip_list_new)
  340:         data_ip = re.findall(r"\d+\.\d+\.\d+\.", IP)
  341          print (data_ip)
  342          for IPS in ip_list_new:
  343:             a = re.findall(r"\d+\.\d+\.\d+\.", IPS)
  344              if a == data_ip:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\Mellanox\Manganese_L2_features\ServerOperations_Storm_Control.py:
  255          print (ip_list_new)
  256:         data_ip = re.findall(r"\d+\.\d+\.\d+\.", IP)
  257          print (data_ip)
  258          for IPS in ip_list_new:
  259:             a = re.findall(r"\d+\.\d+\.\d+\.", IPS)
  260              if a == data_ip:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Tools\performance\listener.py:
  608              if 'URL' in mess:
  609:                 match = re.findall(
  610                      'URL\s([A-Z]+)\s\https:\/\/([^\s\.]+\.[^\s]{2,}|www\.[^\s]+\.[^\s]{2,})',

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  536      for line_number, line in lines_enum:
  537:         for env_var, var_name in ENV_VAR_RE.findall(line):
  538              value = os.getenv(var_name)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\chardet\charsetprober.py:
  85          # the end.
  86:         words = re.findall(b'[a-zA-Z]*[\x80-\xFF]+[a-zA-Z]*[^a-zA-Z\x80-\xFF]?',
  87                             buf)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\compat.py:
  422  
  423:             matches = cookie_re.findall(line_string)
  424              if not matches:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  725  
  726:                 archs = re.findall(r'-arch\s+(\S+)', cflags)
  727                  archs = tuple(sorted(set(archs)))

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\html5lib\_inputstream.py:
  287      def characterErrorsUCS4(self, data):
  288:         for _ in range(len(invalid_unicode_re.findall(data))):
  289              self.errors.append("invalid-codepoint")

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  899          clean = []
  900:         for prop, value in re.findall(r"([-\w]+)\s*:\s*([^:;]*)", style):
  901              if not value:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\requests\utils.py:
  449  
  450:     return (charset_re.findall(content) +
  451:             pragma_re.findall(content) +
  452:             xml_re.findall(content))
  453  

lanier-goat-development\dependency\centos\botocore\serialize.py:
  472          encoded_params = {}
  473:         for template_param in re.findall(r'{(.*?)}', uri_template):
  474              if template_param.endswith('+'):

lanier-goat-development\dependency\centos\botocore\vendored\requests\utils.py:
  302  
  303:     return (charset_re.findall(content) +
  304:             pragma_re.findall(content) +
  305:             xml_re.findall(content))
  306  

lanier-goat-development\dependency\centos\bs4\builder\__init__.py:
  196                      if isinstance(value, str):
  197:                         values = nonwhitespace_re.findall(value)
  198                      else:

lanier-goat-development\dependency\centos\bs4\builder\_html5lib.py:
  208              if not isinstance(value, list):
  209:                 value = nonwhitespace_re.findall(value)
  210          self.element[name] = value

lanier-goat-development\dependency\centos\chardet\charsetprober.py:
  85          # the end.
  86:         words = re.findall(b'[a-zA-Z]*[\x80-\xFF]+[a-zA-Z]*[^a-zA-Z\x80-\xFF]?',
  87                             buf)

lanier-goat-development\dependency\centos\coverage\phystokens.py:
  209  
  210:         matches = COOKIE_RE.findall(line_string)
  211          if not matches:

lanier-goat-development\dependency\centos\coverage\xmlreport.py:
  234              hollow_line = re.sub(rx_attrs, u"☺", line)
  235:             attrs = sorted(re.findall(rx_attr, line))
  236              new_line = hollow_line.replace(u"☺", "".join(attrs))

lanier-goat-development\dependency\centos\dateutil\rrule.py:
  1629              lambda x: (x.upper(), x),
  1630:             re.findall('TZID=(?P<name>[^:]+):', s)
  1631          ))

lanier-goat-development\dependency\centos\isort\isort.py:
  1053      for line_number, line in enumerate(lines, 1):
  1054:         groups = re.findall(pattern, line)
  1055          if groups:

lanier-goat-development\dependency\centos\jinja2\filters.py:
  637      """Count the words in that string."""
  638:     return len(_word_re.findall(s))
  639  

lanier-goat-development\dependency\centos\jinja2\lexer.py:
  192      """
  193:     return len(newline_re.findall(value))
  194  

lanier-goat-development\dependency\centos\lxml\_elementpath.py:
  77      parsing_attribute = False
  78:     for token in xpath_tokenizer_re.findall(pattern):
  79          ttype, tag = token

lanier-goat-development\dependency\centos\lxml\html\diff.py:
  719  
  720:     words = split_words_re.findall(text)
  721      return words

lanier-goat-development\dependency\centos\Naked\toolshed\ink.py:
  43              match_pat = self.odel + r'(.*?)' + self.cdel
  44:         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
  45          return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)

lanier-goat-development\dependency\centos\Naked\toolshed\c\ink.c:
  1318   *             match_pat = self.odel + r'(.*?)' + self.cdel             # <<<<<<<<<<<<<<
  1319:  *         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
  1320   *         return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)

  1340   *             match_pat = self.odel + r'(.*?)' + self.cdel
  1341:  *         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)             # <<<<<<<<<<<<<<
  1342   *         return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)

  1366   *             match_pat = self.odel + r'(.*?)' + self.cdel
  1367:  *         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
  1368   *         return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)             # <<<<<<<<<<<<<<

lanier-goat-development\dependency\centos\Naked\toolshed\c\ink.pyx:
  44              match_pat = self.odel + r'(.*?)' + self.cdel
  45:         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
  46          return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)

lanier-goat-development\dependency\centos\pbr\git.py:
  322          co_authors_out = _run_git_command('log', git_dir)
  323:         co_authors = re.findall('Co-authored-by:.+', co_authors_out,
  324                                  re.MULTILINE)

lanier-goat-development\dependency\centos\psutil\_psaix.py:
  514              raise NoSuchProcess(self.pid, self._name)
  515:         procfiles = re.findall(r"(\d+): S_IFREG.*\s*.*name:(.*)\n", stdout)
  516          retlist = []

lanier-goat-development\dependency\centos\psutil\_pslinux.py:
  1929              # The code below will not crash though and will result to 0.
  1930:             uss = sum(map(int, _private_re.findall(smaps_data))) * 1024
  1931:             pss = sum(map(int, _pss_re.findall(smaps_data))) * 1024
  1932:             swap = sum(map(int, _swap_re.findall(smaps_data))) * 1024
  1933              return (uss, pss, swap)

  2030          data = self._read_status_file()
  2031:         ctxsw = _ctxsw_re.findall(data)
  2032          if not ctxsw:

  2046          data = self._read_status_file()
  2047:         return int(_num_threads_re.findall(data)[0])
  2048  

  2100              data = self._read_status_file()
  2101:             match = _re.findall(data)
  2102              if match:

  2246          data = self._read_status_file()
  2247:         real, effective, saved = _uids_re.findall(data)[0]
  2248          return _common.puids(int(real), int(effective), int(saved))

  2252          data = self._read_status_file()
  2253:         real, effective, saved = _gids_re.findall(data)[0]
  2254          return _common.pgids(int(real), int(effective), int(saved))

lanier-goat-development\dependency\centos\psutil\tests\test_bsd.py:
  143                      self.assertEqual(stats.mtu,
  144:                                      int(re.findall(r'mtu (\d+)', out)[0]))
  145  

lanier-goat-development\dependency\centos\psutil\tests\test_linux.py:
   649          fields = psutil.cpu_times()._fields
   650:         kernel_ver = re.findall(r'\d+\.\d+\.\d+', os.uname()[2])[0]
   651          kernel_ver_info = tuple(map(int, kernel_ver.split('.')))

   987                  self.assertEqual(stats.mtu,
   988:                                  int(re.findall(r'(?i)MTU[: ](\d+)', out)[0]))
   989  

  1004              ret['packets_recv'] = int(
  1005:                 re.findall(r'RX packets[: ](\d+)', out)[0])
  1006              ret['packets_sent'] = int(
  1007:                 re.findall(r'TX packets[: ](\d+)', out)[0])
  1008:             ret['errin'] = int(re.findall(r'errors[: ](\d+)', out)[0])
  1009:             ret['errout'] = int(re.findall(r'errors[: ](\d+)', out)[1])
  1010:             ret['dropin'] = int(re.findall(r'dropped[: ](\d+)', out)[0])
  1011:             ret['dropout'] = int(re.findall(r'dropped[: ](\d+)', out)[1])
  1012              ret['bytes_recv'] = int(
  1013:                 re.findall(r'RX (?:packets \d+ +)?bytes[: ](\d+)', out)[0])
  1014              ret['bytes_sent'] = int(
  1015:                 re.findall(r'TX (?:packets \d+ +)?bytes[: ](\d+)', out)[0])
  1016              return ret

lanier-goat-development\dependency\centos\psutil\tests\test_osx.py:
  203      #     out = out.replace('vm.swapusage: ', '')
  204:     #     total, used, free = re.findall('\d+.\d+\w', out)
  205      #     psutil_smem = psutil.swap_memory()

  220                  self.assertEqual(stats.mtu,
  221:                                  int(re.findall(r'mtu (\d+)', out)[0]))
  222  

lanier-goat-development\dependency\centos\pylint\extensions\_check_docs_utils.py:
  374  
  375:         params_with_type.update(re.findall(self.re_type_in_docstring, self.doc))
  376          return params_with_doc, params_with_type

lanier-goat-development\dependency\centos\redis\client.py:
  3031          db_id, client_info, command = m.groups()
  3032:         command = ' '.join(self.command_re.findall(command))
  3033          command = command.replace('\\"', '"').replace('\\\\', '\\')

lanier-goat-development\dependency\centos\requests\utils.py:
  484  
  485:     return (charset_re.findall(content) +
  486:             pragma_re.findall(content) +
  487:             xml_re.findall(content))
  488  

lanier-goat-development\dependency\photon\botocore\serialize.py:
  472          encoded_params = {}
  473:         for template_param in re.findall(r'{(.*?)}', uri_template):
  474              if template_param.endswith('+'):

lanier-goat-development\dependency\photon\botocore\vendored\requests\utils.py:
  302  
  303:     return (charset_re.findall(content) +
  304:             pragma_re.findall(content) +
  305:             xml_re.findall(content))
  306  

lanier-goat-development\dependency\photon\bs4\builder\__init__.py:
  196                      if isinstance(value, str):
  197:                         values = nonwhitespace_re.findall(value)
  198                      else:

lanier-goat-development\dependency\photon\bs4\builder\_html5lib.py:
  208              if not isinstance(value, list):
  209:                 value = nonwhitespace_re.findall(value)
  210          self.element[name] = value

lanier-goat-development\dependency\photon\chardet\charsetprober.py:
  85          # the end.
  86:         words = re.findall(b'[a-zA-Z]*[\x80-\xFF]+[a-zA-Z]*[^a-zA-Z\x80-\xFF]?',
  87                             buf)

lanier-goat-development\dependency\photon\coverage\phystokens.py:
  209  
  210:         matches = COOKIE_RE.findall(line_string)
  211          if not matches:

lanier-goat-development\dependency\photon\coverage\xmlreport.py:
  234              hollow_line = re.sub(rx_attrs, u"☺", line)
  235:             attrs = sorted(re.findall(rx_attr, line))
  236              new_line = hollow_line.replace(u"☺", "".join(attrs))

lanier-goat-development\dependency\photon\dateutil\rrule.py:
  1629              lambda x: (x.upper(), x),
  1630:             re.findall('TZID=(?P<name>[^:]+):', s)
  1631          ))

lanier-goat-development\dependency\photon\isort\isort.py:
  1053      for line_number, line in enumerate(lines, 1):
  1054:         groups = re.findall(pattern, line)
  1055          if groups:

lanier-goat-development\dependency\photon\jinja2\filters.py:
  637      """Count the words in that string."""
  638:     return len(_word_re.findall(s))
  639  

lanier-goat-development\dependency\photon\jinja2\lexer.py:
  192      """
  193:     return len(newline_re.findall(value))
  194  

lanier-goat-development\dependency\photon\lxml\_elementpath.py:
  77      parsing_attribute = False
  78:     for token in xpath_tokenizer_re.findall(pattern):
  79          ttype, tag = token

lanier-goat-development\dependency\photon\lxml\html\diff.py:
  719  
  720:     words = split_words_re.findall(text)
  721      return words

lanier-goat-development\dependency\photon\Naked\toolshed\ink.py:
  43              match_pat = self.odel + r'(.*?)' + self.cdel
  44:         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
  45          return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)

lanier-goat-development\dependency\photon\Naked\toolshed\c\ink.c:
  1318   *             match_pat = self.odel + r'(.*?)' + self.cdel             # <<<<<<<<<<<<<<
  1319:  *         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
  1320   *         return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)

  1340   *             match_pat = self.odel + r'(.*?)' + self.cdel
  1341:  *         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)             # <<<<<<<<<<<<<<
  1342   *         return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)

  1366   *             match_pat = self.odel + r'(.*?)' + self.cdel
  1367:  *         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
  1368   *         return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)             # <<<<<<<<<<<<<<

lanier-goat-development\dependency\photon\Naked\toolshed\c\ink.pyx:
  44              match_pat = self.odel + r'(.*?)' + self.cdel
  45:         var_list = re.findall(match_pat, template_text) #generate a list that contains the capture group from the matches (i.e. the variables in the template)
  46          return set(var_list) # remove duplicate entries by converting to set (and lookup speed improvement from hashing)

lanier-goat-development\dependency\photon\psutil\_psaix.py:
  514              raise NoSuchProcess(self.pid, self._name)
  515:         procfiles = re.findall(r"(\d+): S_IFREG.*\s*.*name:(.*)\n", stdout)
  516          retlist = []

lanier-goat-development\dependency\photon\psutil\_pslinux.py:
  1929              # The code below will not crash though and will result to 0.
  1930:             uss = sum(map(int, _private_re.findall(smaps_data))) * 1024
  1931:             pss = sum(map(int, _pss_re.findall(smaps_data))) * 1024
  1932:             swap = sum(map(int, _swap_re.findall(smaps_data))) * 1024
  1933              return (uss, pss, swap)

  2030          data = self._read_status_file()
  2031:         ctxsw = _ctxsw_re.findall(data)
  2032          if not ctxsw:

  2046          data = self._read_status_file()
  2047:         return int(_num_threads_re.findall(data)[0])
  2048  

  2100              data = self._read_status_file()
  2101:             match = _re.findall(data)
  2102              if match:

  2246          data = self._read_status_file()
  2247:         real, effective, saved = _uids_re.findall(data)[0]
  2248          return _common.puids(int(real), int(effective), int(saved))

  2252          data = self._read_status_file()
  2253:         real, effective, saved = _gids_re.findall(data)[0]
  2254          return _common.pgids(int(real), int(effective), int(saved))

lanier-goat-development\dependency\photon\psutil\tests\test_bsd.py:
  143                      self.assertEqual(stats.mtu,
  144:                                      int(re.findall(r'mtu (\d+)', out)[0]))
  145  

lanier-goat-development\dependency\photon\psutil\tests\test_linux.py:
   649          fields = psutil.cpu_times()._fields
   650:         kernel_ver = re.findall(r'\d+\.\d+\.\d+', os.uname()[2])[0]
   651          kernel_ver_info = tuple(map(int, kernel_ver.split('.')))

   987                  self.assertEqual(stats.mtu,
   988:                                  int(re.findall(r'(?i)MTU[: ](\d+)', out)[0]))
   989  

  1004              ret['packets_recv'] = int(
  1005:                 re.findall(r'RX packets[: ](\d+)', out)[0])
  1006              ret['packets_sent'] = int(
  1007:                 re.findall(r'TX packets[: ](\d+)', out)[0])
  1008:             ret['errin'] = int(re.findall(r'errors[: ](\d+)', out)[0])
  1009:             ret['errout'] = int(re.findall(r'errors[: ](\d+)', out)[1])
  1010:             ret['dropin'] = int(re.findall(r'dropped[: ](\d+)', out)[0])
  1011:             ret['dropout'] = int(re.findall(r'dropped[: ](\d+)', out)[1])
  1012              ret['bytes_recv'] = int(
  1013:                 re.findall(r'RX (?:packets \d+ +)?bytes[: ](\d+)', out)[0])
  1014              ret['bytes_sent'] = int(
  1015:                 re.findall(r'TX (?:packets \d+ +)?bytes[: ](\d+)', out)[0])
  1016              return ret

lanier-goat-development\dependency\photon\psutil\tests\test_osx.py:
  203      #     out = out.replace('vm.swapusage: ', '')
  204:     #     total, used, free = re.findall('\d+.\d+\w', out)
  205      #     psutil_smem = psutil.swap_memory()

  220                  self.assertEqual(stats.mtu,
  221:                                  int(re.findall(r'mtu (\d+)', out)[0]))
  222  

lanier-goat-development\dependency\photon\pylint\extensions\_check_docs_utils.py:
  374  
  375:         params_with_type.update(re.findall(self.re_type_in_docstring, self.doc))
  376          return params_with_doc, params_with_type

lanier-goat-development\dependency\photon\requests\utils.py:
  501      return (
  502:         charset_re.findall(content)
  503:         + pragma_re.findall(content)
  504:         + xml_re.findall(content)
  505      )

lanier-goat-development\ecosys\veeam\test\deploy_veeam_vm.py:
  289      else:
  290:         veeam_ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', out)
  291          veeam_ip = veeam_ip[0]

lanier-goat-development\goatrest\gaasservice\gaaswebservice.py:
  190              # Use existing uid if provided
  191:             uid = re.findall('-x uuid=[\\w-]*', data.get('test-args', ''))
  192              if uid:

  318              # Use existing uid if provided
  319:             uid = re.findall('-x uuid=[\\w-]*', data.get('test-args', ''))
  320              if uid:

lanier-goat-development\goatrest\gaasservice\testexecutor.py:
  117          # Check for key in extra args
  118:         values = re.findall(r'-x {}=\S*'.format(key), self.args, re.I)
  119          if values:

  121          # Check for key in gOAT command line
  122:         values = re.findall(r'--{} \S*'.format(key), self.args, re.I)
  123          if values:

lanier-goat-development\interop\interarc_vcf_bringup\create_glcm_custom_build.py:
  98          #     import re
  99:         #     build = re.findall(r'Build (\d+) queued', err)
  100          #     buildnumber = build[0]

lanier-goat-development\interop\interarc_vcf_bringup\vcf_custom_builds_generator.py:
  379      import re
  380:     build = re.findall(r'Build (\d+) queued', err)
  381      return build[0]

  502              import re
  503:             build = re.findall(r'Build (\d+) queued', err)
  504              buildnumber = build[0]

lanier-goat-development\interop\setup\configure\vc_initial_configuration.py:
  271              password=esxi_password)
  272:         vmnics = re.findall(r'vSwitch0.*(vmnic\d+)'.format(), out[0])
  273          if len(vmnics) == 1:

lanier-goat-development\interop\setup\install\install_vidm.py:
  215                  delete_after_upload=False)  # TODO Undo this Change later
  216:             self.args.version = re.findall(r"\d+\.\d+\.\d", local_file_path)[0]
  217              self.args.rt.comment('Version is %s' % self.args.version)

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_vmknic_ip_change.py:
  116          constants.ESX_HOST_USR, constants.ESX_HOST_PASSWORD, 120, max_retry=3)
  117:     if re.findall('\\b0% packet loss\\b', out[0]):
  118          args.rt.comment("VMK Ping successful.")

  127  
  128:     if re.findall('\\b0% packet loss\\b', out[0]):
  129          args.rt.comment("VMK Ping successful.")

  157          constants.ESX_HOST_USR, constants.ESX_HOST_PASSWORD, 120, max_retry=3)
  158:     if re.findall('\\b0% packet loss\\b', out[0]):
  159          args.rt.comment("VMK Ping successful after IP change. Test Passed.")

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_vmknic_ip_change.py:
  112              constants.ESX_HOST_USR, constants.ESX_HOST_PASSWORD, 120, max_retry=3)
  113:         if re.findall('\\b0% packet loss\\b', out[0]):
  114              args.rt.comment("VMK Ping successful.")

  123  
  124:         if re.findall('\\b0% packet loss\\b', out[0]):
  125              args.rt.comment("VMK Ping successful.")

  153              constants.ESX_HOST_USR, constants.ESX_HOST_PASSWORD, 120, max_retry=3)
  154:         if re.findall('\\b0% packet loss\\b', out[0]):
  155              args.rt.comment("VMK Ping successful after IP change. Test Passed.")

lanier-goat-development\interop\test\nsxt_vsphere\nsxt24_policy\pnic_wf_cases.py:
  583              password=esxi_password)
  584:         dvsports = re.findall(r'(DvsPortset-\d+).*vmk0', out[0])
  585          dvsport = str(dvsports[0]).strip() if dvsports else None
  586          self.args.log.info("found %s with vmk0 in \n%s" % (dvsports, out[0]))
  587:         vmnics = re.findall(r'{}.*(vmnic\d+)'.format(dvsport), out[0])
  588          if len(vmnics) == 1:

lanier-goat-development\interop\test\pks\verify_vsphere_ha_on_k8s.py:
  263          response = pks_utils.cmd_on_pod(app_2_pod_name[0], cmd)
  264:         status = re.findall('\\b0% packet loss\\b', response)
  265          args.rt.verify_fatal(status[0], "0% packet loss",

  283          response = pks_utils.cmd_on_pod(app_3_pod_name[0], cmd)
  284:         status = re.findall('\\b0% packet loss\\b', response)
  285          args.rt.verify_fatal(status[0], "0% packet loss",

  305          response = pks_utils.cmd_on_pod(app_2_pod_name[0], cmd)
  306:         status = re.findall('\\b0% packet loss\\b', response)
  307          args.rt.verify_fatal(status[0], "0% packet loss",

  309          response = pks_utils.cmd_on_pod(app_3_pod_name[0], cmd)
  310:         status = re.findall('\\b100% packet loss\\b', response)
  311          args.rt.verify_fatal(status[0], "100% packet loss",

  381          response = pks_utils.cmd_on_pod(app_2_pod_name[0], cmd)
  382:         status = re.findall('\\b0% packet loss\\b', response)
  383          args.rt.verify_fatal(status[0], "0% packet loss",

  385          response = pks_utils.cmd_on_pod(app_3_pod_name[0], cmd)
  386:         status = re.findall('\\b100% packet loss\\b', response)
  387          args.rt.verify_fatal(status[0], "100% packet loss",

lanier-goat-development\nsx\nsx_t\conftest.py:
  902      for line in routes_str:
  903:         if re.findall(IPV4_IP_REGEX, line):
  904              vdr_d_routes.add(line.replace(',', ''))

  918      for line in routes_str:
  919:         if re.findall(IPV4_IP_REGEX, line) and ('local' in line):
  920              local_advertised_routes.append(line.split()[1])

lanier-goat-development\nsx\nsx_utils\comm_utils.py:
  678      ip_str = args.opts.setupInfo["vcenter"]["ip"]
  679:     vc_ip = re.findall(re_patterns.find_ip_from_string_pattern, ip_str)
  680      ip = vc_ip[0].replace("-", ".")

lanier-goat-development\nsx\nsx_utils\esxi_process_check.py:
  75              if "Vdr Name:" in each_line:
  76:                 dlr = re.findall(re_patterns.dlr_name_on_esxi, each_line)
  77                  if dlr:

lanier-goat-development\utils\datastore.py:
  273                              cmd.format(disk['Name'])], esx_host, esx_user, esx_pwd)
  274:                         disk['Size(MB)'] = re.findall(r'\d+', out[0])[0]
  275                      if int(disk['IsSSD']):

lanier-goat-development\utils\esx.py:
  1098              password=esxi_password)
  1099:         dvsports = re.findall(r'(DvsPortset-\d+).*%s' % vmk, out[0])
  1100          dvsport = str(dvsports[0]).strip() if dvsports else None
  1101          self.args.log.info("found %s with vmk0 in \n%s" % (dvsports, out[0]))
  1102:         vmnics = re.findall(r'{}.*(vmnic\d+)'.format(dvsport), out[0])
  1103          return vmnics

lanier-goat-development\utils\pod_parser.py:
  37                  "vmware.pod_telemetry Telemetry data: ")[1]
  38:             patterns = re.findall(pattern_x, telemetric_dat_json)
  39              if patterns.__len__() > 0:

lanier-goat-development\utils\bringup\utils\iso\cb_utils.py:
   78              pattern = "((\\d+\\.?){2,5}(\\w+)?[\\.-]\\d+)"
   79:             version_new = re.findall(pattern, iso_name)[0][0]
   80              version_new = self.fix_version_format(version_new)

  159          version_pattern = r'\/nsx-lcp-(.*)\.zip$'
  160:         file_version = re.findall(version_pattern, nsx_lcp_path)
  161          original_version = file_version[0]

  259              pattern = "((\\d+\\.?){3,5}[\\.-]\\d+)"
  260:             esx_version_old = re.findall(pattern, esx_encap_name)[0][0]
  261              esx_version_old = self.fix_version_format(esx_version_old)

lanier-goat-development\utils\bringup\utils\setup_actions\download_testcerts.py:
  73  
  74:     matches = re.findall(r"(?=\d\.?){3}(\d+)-encap\.zip", output)
  75      args.log.debug("Match object: {}".format(matches))

lanier-goat-development\utils\interop\interoputils.py:
  3236              self.args.log.info(output)
  3237:             status = re.findall('\\b0% packet loss\\b', output.decode('utf-8'))
  3238              if status:

  5470                  try:
  5471:                     pkt_loss = re.findall(r'(\d*)% packet loss', line)
  5472                      pkt_loss = ''.join(pkt_loss)

lanier-goat-development\utils\interop\nsxtutils.py:
  552              self.args.log.info(output)
  553:             status = re.findall('\\b0% packet loss\\b', output)
  554              if status:

lanier-goat-development\utils\interop\tools_utils.py:
  727          regex = r'Ethernet adapter ([\d|\D]+?):[\d|\D]+?%s' % partial_ip
  728:         adapter_matches = re.findall(regex, stdouts[0], re.DOTALL)
  729          self.args.log.info("adapter_matches : %s" % adapter_matches)

lanier-goat-development\utils\via\base.py:
  85                  # sddc-manager-2.2.0-5044317.iso
  86:                 build_number = re.findall('\d+', iso)
  87                  if build_number:

lanier-goat-development\vc\test\verify_entries_in_unboundconf.py:
  30      allvms = vcenter_login.get_all_vms()
  31:     pscvms = re.findall(r'psc-.', str(allvms), re.I)
  32      pschostname = [x + '.' + domain for x in pscvms]

lanier-goat-development\vcf\assessment\assessment_sos_helper.py:
  386          """
  387:         result = re.findall(OUTPUT_FILES_REGEX, text, re.MULTILINE)
  388          # Remove whitespaces

lanier-goat-development\vcf\assessment\test\assessment_base.py:
  311                          error_text += line
  312:                         if not line or len(re.findall(r"\b\w*Error:\b", line)) > 0:
  313                              break

lanier-goat-development\vcf\passwordscanner\GetCredentials.py:
  56  pattern = '"password":"(.*?)","'
  57: res = re.findall(pattern, responseText)
  58  unique_res = []

lanier-goat-development\vmc\PodManager.py:
  1838          # parse the name of the file
  1839:         data = re.findall(
  1840              r"[\d][.][\d][.][\d]-[\d]*[-][\w-]*[.][\w]*[<]", data)

  2172                      telemetric_dat_json = telemetric_dat
  2173:                     patterns = re.findall(pattern_x, telemetric_dat_json)
  2174                      if patterns.__len__() > 0:

lanier-goat-development\vmc\set_content_library.py:
  36      # Thumbprint
  37:     thumb_md5 = ':'.join(re.findall(
  38          '..', hashlib.md5(der_cert_bin).hexdigest()))
  39:     thumb_sha1 = ':'.join(re.findall(
  40          '..', hashlib.sha1(der_cert_bin).hexdigest()))
  41:     thumb_sha256 = ':'.join(re.findall(
  42          '..', hashlib.sha256(der_cert_bin).hexdigest()))

lanier-goat-development\vmc\common_utils\edge_failover.py:
  61      data = active_edge['params']['SCRIPTDATA']['data']
  62:     node_uid = re.findall("\"node_uuid\"\:\"([0-9a-zA-Z\-]+)\",", data)[0]
  63      args.rt.log.info("Got active edge: " + node_uid)

lanier-goat-development\vmc\negative\leaf_node\nsxt_ui_leaf\nsxt_leaf_service.py:
  602      string = urlpath.read().decode('utf-8')
  603:     file_name = re.findall("nsx_policy[a-zA-Z0-9_.-]*.cub", string)[0]
  604      file_ext = file_name[file_name.rfind('.'):]

lanier-goat-development\vmc\pod\helper\generic_helper.py:
  553                  try:
  554:                     pkt_loss = re.findall(r'(\d*\.?\d+|\d+)% packet loss', line)
  555                      pkt_loss = ''.join(pkt_loss)

lanier-goat-development\vmc\pod\pre_check\PreCheckHelper.py:
  302                      check_ids[message_id] = check_ids.get(message_id) or any(
  303:                         re.findall(success_message_pattern, msg, re.I) for msg in messages_to_check)
  304  

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_check_clock_ram_cpu.py:
  119                                  cvm_mem = cvm_output['memory']['used']
  120:                                 result = re.findall('.+%', mem_load)
  121                                  scm_mem_load = int(

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_cli.py:
  925              output = config.verify_sys_dump()
  926:             sys_dump_files = re.findall('case.+.tgz', output)
  927              output_sys_dump = cvm_shell.exec_command(

  930                  timeout=600)
  931:             cvm_sys_dump_files = re.findall(
  932                  'sysdump-cvm.+.tgz', output_sys_dump)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_connectivity.py:
  652              output = config.verify_sys_dump()
  653:             sys_dump_files = re.findall('case.+.tgz', output)
  654              output_sys_dump = cvm_shell.exec_command(

  656                  format(sys_dump_files[0]), timeout=600)
  657:             cvm_sys_dump_files = re.findall(
  658                  'sysdump-cvm.+.tgz', output_sys_dump)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_orchestration_agent.py:
  718      flow_rules = set(
  719:         re.findall(
  720              r'ingress=[\d\s]+egress=\d+',

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_rsyslog.py:
   996      parts_text = re.split(r'\[.*\]', data)
   997:     parts_bracket = re.findall(r'\[.*\]', data)
   998      assert len(parts_text) == 2, \

  1032                r' site-name="' + site_name + '" prefix="' + prefix + '"'
  1033:     x = re.findall(pattern, data)
  1034      if x is None:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\connection_resource.py:
  184      result = cvm_shell.exec_command('journalctl --disk-usage')
  185:     mem = re.findall(r'\d.+M', result)
  186      output = mem[0].split('M')

portfolio-system-tests\new\portfolio_system_tests\legacy_gluon\libs\__init__.py:
  242      # This assumes the header names have no spaces in them
  243:     header_blocks = re.findall(r'\S+\s+(?=\S|$)', header)
  244      headers = [block.strip() for block in header_blocks]

portfolio-system-tests\new\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_collision_wanopt_stale_entry.py:
  433      # connection trace is the one which is newly created.
  434:     syn_dif_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  435      assert(str(SYN_SAME_SEQ) not in syn_dif_seq[-1]), \

  739          src_ip, HTTP_SRC_PORT, dst_ip, HTTP_DST_PORT)
  740:     syn_same_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  741      # Remove the loadbalance rule from ICs.

portfolio-system-tests\new\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_ic_owned_conn_reuse.py:
  349          var = ic.read_text_file(FILE_ORIG)
  350:         new_var = re.findall(r'id="\d{2,}"', var)
  351          new_vars = '{0}' .format(new_var[0]) + \

portfolio-system-tests\new\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_path_selection_customer_issues.py:
  343      #  connection trace is the one which is newly created.
  344:     syn_dif_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  345      assert (str(SYN_SAME_SEQ) not in syn_dif_seq[-1]), \

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_brownfield_sites_1Panther_CF3_ha_gateway.py:
  381      # Configuring the inteceptor interfaces.
  382:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  383                           str(test_objects.int_if1.cidr))

  391                                  int_if1.inpath.inpath_gateway)
  392:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  393                           str(test_objects.int_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_brownfield_sites_3Panther_CF3_ha_gateway.py:
  420      # Configuring the inteceptor interfaces.
  421:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  422                           str(test_objects.int_if1.cidr))

  430                                  int_if1.inpath.inpath_gateway)
  431:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  432                           str(test_objects.int_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_single_panther_catfish_L2_ha_gateway.py:
  328      # Configuring the inteceptor interfaces.
  329:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(test_objects.int_if1.cidr))

  338                                  int_if1.inpath.inpath_gateway)
  339:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  340                           str(test_objects.int_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_single_panther_catfish_L3_ha_gateway.py:
  374      # Configuring the inteceptor interfaces.
  375:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  376                           str(test_objects.int_if1.cidr))

  384                                  int_if1.inpath.inpath_gateway)
  385:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  386                           str(test_objects.int_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_catfish_on_branch2.py:
  328      # Configuring the inteceptor interfaces.
  329:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(int_if1.cidr))

  337                                  ip_address=int_if1.inpath.inpath_gateway)
  338:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  339                           str(int_if2.cidr))

  368      # Configuring the IC1 inpath1 interface.
  369:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  370                                   str(phy_int1_if1.cidr))

  383      # Configuring the IC1 inpath2 interface.
  384:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  385                                   str(phy_int1_if2.cidr))

  426      # Configuring the IC2 inpath1 interface.
  427:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  428                                   str(phy_int2_if1.cidr))

  441      # Configuring the IC2 inpath2 interface.
  442:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  443                                   str(phy_int2_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_L3_single_catfish.py:
  319      # Configuring the inteceptor interfaces.
  320:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  321                           str(int_if1.cidr))

  328                                  ip_address=int_if1.inpath.inpath_gateway)
  329:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(int_if2.cidr))

  359      # Configuring the IC1 inpath1 interface.
  360:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  361                                   str(phy_int1_if1.cidr))

  374      # Configuring the IC1 inpath2 interface.
  375:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  376                                   str(phy_int1_if2.cidr))

  417      # Configuring the IC2 inpath1 interface.
  418:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  419                                   str(phy_int2_if1.cidr))

  432      # Configuring the IC2 inpath2 interface.
  433:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  434                                   str(phy_int2_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_single_panther.py:
  266      # Configuring the inteceptor interfaces.
  267:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  268                           str(test_objects.int_if1.cidr))

  276                                  int_if1.inpath.inpath_gateway)
  277:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  278                           str(test_objects.int_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways.py:
  330      # Configuring the inteceptor interfaces.
  331:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  332                           str(int_if1.cidr))

  339                                  ip_address=int_if1.inpath.inpath_gateway)
  340:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  341                           str(int_if2.cidr))

  370      # Configuring the IC1 inpath1 interface.
  371:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  372                                   str(phy_int1_if1.cidr))

  385      # Configuring the IC1 inpath2 interface.
  386:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  387                                   str(phy_int1_if2.cidr))

  428      # Configuring the IC2 inpath1 interface.
  429:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  430                                   str(phy_int2_if1.cidr))

  443      # Configuring the IC2 inpath2 interface.
  444:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  445                                   str(phy_int2_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_split_site.py:
  325      # Configuring the inteceptor interfaces.
  326:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  327                           str(int_if1.cidr))

  334                                  ip_address=int_if1.inpath.inpath_gateway)
  335:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  336                           str(int_if2.cidr))

  365      # Configuring the IC1 inpath1 interface.
  366:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  367                                   str(phy_int1_if1.cidr))

  380      # Configuring the IC1 inpath2 interface.
  381:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  382                                   str(phy_int1_if2.cidr))

  423      # Configuring the IC2 inpath1 interface.
  424:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  425                                   str(phy_int2_if1.cidr))

  438      # Configuring the IC2 inpath2 interface.
  439:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  440                                   str(phy_int2_if2.cidr))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_dc_uplink.py:
  266          else:
  267:             dc_uplinks_teps['Internet'] = re.findall(r'[0-9]+(?:\.[0-9]+){3}',
  268                                                       dc_uplink.net)

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_change_panther_db_address.py:
  272      old_sd_wan = resources.ic1_model.show_sd_wan().raw
  273:     old_sd_wan_addr_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  274                                        str(old_sd_wan))

portfolio-system-tests\new\portfolio_system_tests\legacy_shsaas_tests\tests\SH\sepia\conftest.py:
  110      result = client_shell.exec_command(cmd, error_expected=True)
  111:     return (len(re.findall("[0-9]+", result)))
  112  

  189              match = "TCP_MISS/200 [0-9]* GET " + url
  190:         if (len(re.findall(match, result)) < 1):
  191              raise VerificationError(

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_manage_appliances.py:
  192      group_info = resources.scc_actor.model.show_cmc_group(group=group).raw
  193:     lines = re.findall(r'.*/.*', group_info)
  194      return [i.split()[0] for i in lines]

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
  50          for x in range(1, 10):
  51:             subnet = re.findall(subnet_regex, delete_status)[0]
  52              port_id = commands.getoutput(

  66          for x in range(1, 10):
  67:             router_subnet = re.findall(router_regex, delete_status)[0]
  68              cmd = 'neutron router-update %s --routes action=clear' % (

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\populate_networks_subnets_images.py:
  75      site_id = all_sites[site]
  76:     branch_number = re.findall(r"[0-9]+$", site)[0]
  77      image_name = "vgw" + branch_number + "_pod" + str(pod) + "_image"

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\scale2_appliance_health_report.py:
  169      else:
  170:         node_memory_usage = re.findall(r'[0-9]+%', node_memory_string)[0]
  171      node_configuration = node['state']

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\script_appliance_health_report.py:
  182      else:
  183:         node_memory_usage = re.findall(r'[0-9]+%', node_memory_string)[0]
  184      node_configuration = node['state']

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\appliance.py:
  410              break
  411:         if (len(re.findall('inet6 addr', interface[1]))) > 1:
  412              interface[1] = interface[1]. \

  454      if pattern:
  455:         return re.findall(pattern, if_names)
  456      return if_names.split('\n')

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\traffic.py:
  104                            min_poll_interval=5):
  105:         accepted_flows = re.findall(r'Accepted: \d+', output)
  106          no_of_flows = [int(flow.split()[1]) for flow in accepted_flows]

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler_client.py:
  70      try:
  71:         client_ip = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', response)[0])
  72      except IndexError:
  73          response = request_new_ip(mgmt_ip, interface, dh_request)
  74:         client_ip = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', response)[0])
  75      find_mac = re.compile('([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
  76:     client_mac = (re.findall(find_mac, response)[0])
  77      if ipaddress.ip_address(client_ip):

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler.py:
  310  
  311:     split_var = re.findall(r'\s(\bZscaler\s\bCloud):', header)
  312      paragraph = header.split(split_var[0])[2]

  315          header_city = \
  316:             re.findall(r'\s[A-Z]*[a-z]*\s[A-Z]+[a-z]+\s[IV, III, II]*',
  317                         paragraph)[0].strip()
  318      else:
  319:         header_city = re.findall(r'[A-Z]*[a-z]*\s[A-Z]+[a-z]+\s[IV, III, II]*',
  320                                   paragraph)[0].strip()
  321:     header_cloud = re.findall(r'\s(\bzscalertwo).', paragraph)[0]
  322  

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\tests\performance\test_pload_http_performance.py:
  42      data = []
  43:     rows = re.findall(pattern, output)
  44      for row in rows:

  52      pattern = (r'.*::.* = .*')
  53:     row = re.findall(pattern, output)
  54      data = row[0].split('=')[1].split(':')[1]

  70          output = monitor_setup.shell.exec_command(cmd)
  71:         rows = re.findall(pattern, output)
  72  

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\tests\physical\uplinks\test_backup_uplink.py:
  105      cmd = node_shell.exec_command('traceroute 8.8.8.8 -m 1')
  106:     default_route = re.findall(r'\(([^)]+)', cmd)
  107      return default_route[1]

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\tests\wan_uplink_failover\test_uplink_ping_interval.py:
  153      for line in lines:
  154:         matches.append(re.findall(r'\d{2}:\d{2}\.\d{2}', line)[0])
  155          # 09:21:58.379343 IP 8.8.8.8 > 192.168.0.10: ICMP echo reply

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_zebos_config_check_bgp.py:
  48                  'remote-as' in line.strip():
  49:             gw_output['neighbor_ips'].append(re.findall(
  50                  r'[0-9]+(?:\.[0-9]+){3}', line)[0])
  51:             gw_output['neighbor_as'].append(re.findall(
  52                  r'remote-as (\w+)', line)[0])

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\test_bgp_ha_uplink.py:
  88          version = OS.get(gateway).shell.exec_command('imish -e "show ip bgp"')
  89:         zebos_version = re.findall(r"\d\.\d.\d", version)[0]
  90          logger.info("ZebOS-XP version is {}".format(zebos_version))

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_zebos_config_change.py:
  38                  re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  39:             gw_output['network'].append(re.findall(
  40                  r'[0-9]+(?:\.[0-9]+){3}', line)[0])
  41:             gw_output['area'].append(re.findall(
  42                  r'[0-9]+(?:\.[0-9]+){3}', line)[1])

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_remote_site_ospf_learning.py:
  36      for line in route.splitlines()[1:]:
  37:         if re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line):
  38              gw_output_routes.append(
  39:                 re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line)[0])
  40      return gw_output_routes

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\ospf_routemap\test_remote_site_states.py:
  35      for line in route.splitlines()[1:]:
  36:         if re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line):
  37              gw_output_routes.append(
  38:                 re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line)[0])
  39      return gw_output_routes

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\helpers\utils.py:
  171      route_op = container_shell.exec_command("vtysh -c 'show ip route'")
  172:     found = re.findall(r'(\d+\.\d+\.\d+\.\d+\/\d+)\s.+\s(\d+\.\d+\.\d+\.\d+)',
  173                         route_op)

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\openstack-tests\openstack_ops.py:
  114          if output[0]:
  115:             available_volume_ids_list = re.findall(r'\w+-\w+-\w+-\w+-\w+', output[1])
  116          else:

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\provisioning\get_build_from_deliverable.py:
  19      data = json.loads(resp.text)
  20:     int_array = re.findall(r'\d+', data["build"]["name"])
  21      print(str(int_array[-1]))

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\conftest.py:
  314          if (get_peer_ip):
  315:             peer_ip = re.findall(r'\d+\.\d+\.\d+\.\d+', output.raw)
  316              assert (len(peer_ip) == 1)

  880          if windows:
  881:             return re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  882                                output)[1]

  892          output = client_sh.exec_command("nslookup public.boxcloud.com")
  893:         return re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  894                            output)[1]

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\komodo\test_unsuccessful_edit_deployment.py:
  106                         "to support the number of users")
  107:             if not(re.findall(pattern, res.text)):
  108                  raise VerificationError(

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\truk\test_cfe_load_balancing.py:
  24      result = output.raw
  25:     m = re.findall(r'\(.*\)', result)
  26      if (len(m) != len(output.parsed_as_key_val)):
  27          raise ValueError("ZAK Peer Port numbers mismatch found")
  28:     ports = re.findall(r'\d+', m[0])
  29      assert (len(ports) == 2)

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
  1625              try:
  1626:                 find = re.findall(r'STACK TRACE.*', output, re.MULTILINE)
  1627                  assert(len(find) == 0)

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\shm_tests\shm_helper.py:
  222                  "nslookup rvbd496-my.sharepoint.com")
  223:             dest_ip = re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  224                                   output)[1]

  227                  "nslookup public.boxcloud.com")
  228:             dest_ip = re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  229                                   output)[1]

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\configure.py:
  112                  model_str = show_version['product model']
  113:                 model_str = re.findall(r'\((.*)\)', model_str)[0]
  114                  cache['version'] = LegacyVersion(version)

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\rios_pxe_install.py:
  178  
  179:         name_servers = re.findall(r'Name server: (\S+) \(configured\)', output)
  180          for name_server in name_servers:

  182  
  183:         dns_suffixes = re.findall(r'Domain name: (\S+) \(configured\)', output)
  184          for dns_suffix in dns_suffixes:

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\verification.py:
  588              min_data_redux_pcent):
  589:         percentages = re.findall(r'(\d+)%', connection_summary)
  590          if not percentages:

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\zak_log_verifier.py:
  146          if 'messages' in log_dict['name']:
  147:             match_list = re.findall(r'\d+', log_dict['name'])
  148              sh_log_branch_list.append(match_list[0])

portfolio-system-tests\new\portfolio_system_tests\winsec\conftest.py:
  172      actual_config = server_sh.model.show_hosts().raw
  173:     dns_servers = re.findall(
  174          r'Name server:\s+(\d+\.\d+\.\d+\.\d+)\s+', actual_config)

  178      pattern = re.compile(regex)
  179:     domains = re.findall(pattern, actual_config)
  180      for domain in domains:

portfolio-system-tests\new\portfolio_system_tests\winsec\tests\test_adp_upgrade_sanity.py:
  57      # build number is 9
  58:     build = re.findall(r'/(?!.*/adproxy/.*/)(\d+)', image_url).pop()
  59  

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_check_clock_ram_cpu.py:
  119                                  cvm_mem = cvm_output['memory']['used']
  120:                                 result = re.findall('.+%', mem_load)
  121                                  scm_mem_load = int(

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_cli.py:
  925              output = config.verify_sys_dump()
  926:             sys_dump_files = re.findall('case.+.tgz', output)
  927              output_sys_dump = cvm_shell.exec_command(

  930                  timeout=600)
  931:             cvm_sys_dump_files = re.findall(
  932                  'sysdump-cvm.+.tgz', output_sys_dump)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_connectivity.py:
  652              output = config.verify_sys_dump()
  653:             sys_dump_files = re.findall('case.+.tgz', output)
  654              output_sys_dump = cvm_shell.exec_command(

  656                  format(sys_dump_files[0]), timeout=600)
  657:             cvm_sys_dump_files = re.findall(
  658                  'sysdump-cvm.+.tgz', output_sys_dump)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_orchestration_agent.py:
  718      flow_rules = set(
  719:         re.findall(
  720              r'ingress=[\d\s]+egress=\d+',

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_rsyslog.py:
   996      parts_text = re.split(r'\[.*\]', data)
   997:     parts_bracket = re.findall(r'\[.*\]', data)
   998      assert len(parts_text) == 2, \

  1032                r' site-name="' + site_name + '" prefix="' + prefix + '"'
  1033:     x = re.findall(pattern, data)
  1034      if x is None:

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\connection_resource.py:
  184      result = cvm_shell.exec_command('journalctl --disk-usage')
  185:     mem = re.findall(r'\d.+M', result)
  186      output = mem[0].split('M')

portfolio-system-tests\portfolio_system_tests\legacy_gluon\libs\__init__.py:
  242      # This assumes the header names have no spaces in them
  243:     header_blocks = re.findall(r'\S+\s+(?=\S|$)', header)
  244      headers = [block.strip() for block in header_blocks]

portfolio-system-tests\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_collision_wanopt_stale_entry.py:
  433      # connection trace is the one which is newly created.
  434:     syn_dif_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  435      assert(str(SYN_SAME_SEQ) not in syn_dif_seq[-1]), \

  739          src_ip, HTTP_SRC_PORT, dst_ip, HTTP_DST_PORT)
  740:     syn_same_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  741      # Remove the loadbalance rule from ICs.

portfolio-system-tests\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_ic_owned_conn_reuse.py:
  349          var = ic.read_text_file(FILE_ORIG)
  350:         new_var = re.findall(r'id="\d{2,}"', var)
  351          new_vars = '{0}' .format(new_var[0]) + \

portfolio-system-tests\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_path_selection_customer_issues.py:
  343      #  connection trace is the one which is newly created.
  344:     syn_dif_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  345      assert (str(SYN_SAME_SEQ) not in syn_dif_seq[-1]), \

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_brownfield_sites_1Panther_CF3_ha_gateway.py:
  381      # Configuring the inteceptor interfaces.
  382:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  383                           str(test_objects.int_if1.cidr))

  391                                  int_if1.inpath.inpath_gateway)
  392:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  393                           str(test_objects.int_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_brownfield_sites_3Panther_CF3_ha_gateway.py:
  420      # Configuring the inteceptor interfaces.
  421:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  422                           str(test_objects.int_if1.cidr))

  430                                  int_if1.inpath.inpath_gateway)
  431:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  432                           str(test_objects.int_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_single_panther_catfish_L2_ha_gateway.py:
  328      # Configuring the inteceptor interfaces.
  329:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(test_objects.int_if1.cidr))

  338                                  int_if1.inpath.inpath_gateway)
  339:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  340                           str(test_objects.int_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_single_panther_catfish_L3_ha_gateway.py:
  374      # Configuring the inteceptor interfaces.
  375:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  376                           str(test_objects.int_if1.cidr))

  384                                  int_if1.inpath.inpath_gateway)
  385:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  386                           str(test_objects.int_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_catfish_on_branch2.py:
  328      # Configuring the inteceptor interfaces.
  329:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(int_if1.cidr))

  337                                  ip_address=int_if1.inpath.inpath_gateway)
  338:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  339                           str(int_if2.cidr))

  368      # Configuring the IC1 inpath1 interface.
  369:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  370                                   str(phy_int1_if1.cidr))

  383      # Configuring the IC1 inpath2 interface.
  384:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  385                                   str(phy_int1_if2.cidr))

  426      # Configuring the IC2 inpath1 interface.
  427:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  428                                   str(phy_int2_if1.cidr))

  441      # Configuring the IC2 inpath2 interface.
  442:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  443                                   str(phy_int2_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_L3_single_catfish.py:
  319      # Configuring the inteceptor interfaces.
  320:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  321                           str(int_if1.cidr))

  328                                  ip_address=int_if1.inpath.inpath_gateway)
  329:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(int_if2.cidr))

  359      # Configuring the IC1 inpath1 interface.
  360:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  361                                   str(phy_int1_if1.cidr))

  374      # Configuring the IC1 inpath2 interface.
  375:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  376                                   str(phy_int1_if2.cidr))

  417      # Configuring the IC2 inpath1 interface.
  418:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  419                                   str(phy_int2_if1.cidr))

  432      # Configuring the IC2 inpath2 interface.
  433:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  434                                   str(phy_int2_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_single_panther.py:
  266      # Configuring the inteceptor interfaces.
  267:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  268                           str(test_objects.int_if1.cidr))

  276                                  int_if1.inpath.inpath_gateway)
  277:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  278                           str(test_objects.int_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways.py:
  330      # Configuring the inteceptor interfaces.
  331:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  332                           str(int_if1.cidr))

  339                                  ip_address=int_if1.inpath.inpath_gateway)
  340:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  341                           str(int_if2.cidr))

  370      # Configuring the IC1 inpath1 interface.
  371:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  372                                   str(phy_int1_if1.cidr))

  385      # Configuring the IC1 inpath2 interface.
  386:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  387                                   str(phy_int1_if2.cidr))

  428      # Configuring the IC2 inpath1 interface.
  429:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  430                                   str(phy_int2_if1.cidr))

  443      # Configuring the IC2 inpath2 interface.
  444:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  445                                   str(phy_int2_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_split_site.py:
  325      # Configuring the inteceptor interfaces.
  326:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  327                           str(int_if1.cidr))

  334                                  ip_address=int_if1.inpath.inpath_gateway)
  335:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  336                           str(int_if2.cidr))

  365      # Configuring the IC1 inpath1 interface.
  366:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  367                                   str(phy_int1_if1.cidr))

  380      # Configuring the IC1 inpath2 interface.
  381:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  382                                   str(phy_int1_if2.cidr))

  423      # Configuring the IC2 inpath1 interface.
  424:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  425                                   str(phy_int2_if1.cidr))

  438      # Configuring the IC2 inpath2 interface.
  439:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  440                                   str(phy_int2_if2.cidr))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_dc_uplink.py:
  266          else:
  267:             dc_uplinks_teps['Internet'] = re.findall(r'[0-9]+(?:\.[0-9]+){3}',
  268                                                       dc_uplink.net)

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_change_panther_db_address.py:
  272      old_sd_wan = resources.ic1_model.show_sd_wan().raw
  273:     old_sd_wan_addr_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  274                                        str(old_sd_wan))

portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\sepia\conftest.py:
  110      result = client_shell.exec_command(cmd, error_expected=True)
  111:     return (len(re.findall("[0-9]+", result)))
  112  

  189              match = "TCP_MISS/200 [0-9]* GET " + url
  190:         if (len(re.findall(match, result)) < 1):
  191              raise VerificationError(

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_manage_appliances.py:
  192      group_info = resources.scc_actor.model.show_cmc_group(group=group).raw
  193:     lines = re.findall(r'.*/.*', group_info)
  194      return [i.split()[0] for i in lines]

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
  50          for x in range(1, 10):
  51:             subnet = re.findall(subnet_regex, delete_status)[0]
  52              port_id = commands.getoutput(

  66          for x in range(1, 10):
  67:             router_subnet = re.findall(router_regex, delete_status)[0]
  68              cmd = 'neutron router-update %s --routes action=clear' % (

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\populate_networks_subnets_images.py:
  75      site_id = all_sites[site]
  76:     branch_number = re.findall(r"[0-9]+$", site)[0]
  77      image_name = "vgw" + branch_number + "_pod" + str(pod) + "_image"

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\scale2_appliance_health_report.py:
  169      else:
  170:         node_memory_usage = re.findall(r'[0-9]+%', node_memory_string)[0]
  171      node_configuration = node['state']

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\script_appliance_health_report.py:
  182      else:
  183:         node_memory_usage = re.findall(r'[0-9]+%', node_memory_string)[0]
  184      node_configuration = node['state']

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\appliance.py:
  410              break
  411:         if (len(re.findall('inet6 addr', interface[1]))) > 1:
  412              interface[1] = interface[1]. \

  454      if pattern:
  455:         return re.findall(pattern, if_names)
  456      return if_names.split('\n')

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\traffic.py:
  104                            min_poll_interval=5):
  105:         accepted_flows = re.findall(r'Accepted: \d+', output)
  106          no_of_flows = [int(flow.split()[1]) for flow in accepted_flows]

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler_client.py:
  70      try:
  71:         client_ip = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', response)[0])
  72      except IndexError:
  73          response = request_new_ip(mgmt_ip, interface, dh_request)
  74:         client_ip = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', response)[0])
  75      find_mac = re.compile('([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
  76:     client_mac = (re.findall(find_mac, response)[0])
  77      if ipaddress.ip_address(client_ip):

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler.py:
  310  
  311:     split_var = re.findall(r'\s(\bZscaler\s\bCloud):', header)
  312      paragraph = header.split(split_var[0])[2]

  315          header_city = \
  316:             re.findall(r'\s[A-Z]*[a-z]*\s[A-Z]+[a-z]+\s[IV, III, II]*',
  317                         paragraph)[0].strip()
  318      else:
  319:         header_city = re.findall(r'[A-Z]*[a-z]*\s[A-Z]+[a-z]+\s[IV, III, II]*',
  320                                   paragraph)[0].strip()
  321:     header_cloud = re.findall(r'\s(\bzscalertwo).', paragraph)[0]
  322  

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\tests\performance\test_pload_http_performance.py:
  42      data = []
  43:     rows = re.findall(pattern, output)
  44      for row in rows:

  52      pattern = (r'.*::.* = .*')
  53:     row = re.findall(pattern, output)
  54      data = row[0].split('=')[1].split(':')[1]

  70          output = monitor_setup.shell.exec_command(cmd)
  71:         rows = re.findall(pattern, output)
  72  

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\tests\physical\uplinks\test_backup_uplink.py:
  105      cmd = node_shell.exec_command('traceroute 8.8.8.8 -m 1')
  106:     default_route = re.findall(r'\(([^)]+)', cmd)
  107      return default_route[1]

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\tests\wan_uplink_failover\test_uplink_ping_interval.py:
  153      for line in lines:
  154:         matches.append(re.findall(r'\d{2}:\d{2}\.\d{2}', line)[0])
  155          # 09:21:58.379343 IP 8.8.8.8 > 192.168.0.10: ICMP echo reply

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_zebos_config_check_bgp.py:
  48                  'remote-as' in line.strip():
  49:             gw_output['neighbor_ips'].append(re.findall(
  50                  r'[0-9]+(?:\.[0-9]+){3}', line)[0])
  51:             gw_output['neighbor_as'].append(re.findall(
  52                  r'remote-as (\w+)', line)[0])

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\test_bgp_ha_uplink.py:
  88          version = OS.get(gateway).shell.exec_command('imish -e "show ip bgp"')
  89:         zebos_version = re.findall(r"\d\.\d.\d", version)[0]
  90          logger.info("ZebOS-XP version is {}".format(zebos_version))

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_zebos_config_change.py:
  38                  re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  39:             gw_output['network'].append(re.findall(
  40                  r'[0-9]+(?:\.[0-9]+){3}', line)[0])
  41:             gw_output['area'].append(re.findall(
  42                  r'[0-9]+(?:\.[0-9]+){3}', line)[1])

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_remote_site_ospf_learning.py:
  36      for line in route.splitlines()[1:]:
  37:         if re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line):
  38              gw_output_routes.append(
  39:                 re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line)[0])
  40      return gw_output_routes

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\ospf_routemap\test_remote_site_states.py:
  35      for line in route.splitlines()[1:]:
  36:         if re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line):
  37              gw_output_routes.append(
  38:                 re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line)[0])
  39      return gw_output_routes

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\helpers\utils.py:
  171      route_op = container_shell.exec_command("vtysh -c 'show ip route'")
  172:     found = re.findall(r'(\d+\.\d+\.\d+\.\d+\/\d+)\s.+\s(\d+\.\d+\.\d+\.\d+)',
  173                         route_op)

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\openstack-tests\openstack_ops.py:
  114          if output[0]:
  115:             available_volume_ids_list = re.findall(r'\w+-\w+-\w+-\w+-\w+', output[1])
  116          else:

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\provisioning\get_build_from_deliverable.py:
  19      data = json.loads(resp.text)
  20:     int_array = re.findall(r'\d+', data["build"]["name"])
  21      print(str(int_array[-1]))

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\conftest.py:
  314          if (get_peer_ip):
  315:             peer_ip = re.findall(r'\d+\.\d+\.\d+\.\d+', output.raw)
  316              assert (len(peer_ip) == 1)

  880          if windows:
  881:             return re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  882                                output)[1]

  892          output = client_sh.exec_command("nslookup public.boxcloud.com")
  893:         return re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  894                            output)[1]

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\komodo\test_unsuccessful_edit_deployment.py:
  106                         "to support the number of users")
  107:             if not(re.findall(pattern, res.text)):
  108                  raise VerificationError(

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\truk\test_cfe_load_balancing.py:
  24      result = output.raw
  25:     m = re.findall(r'\(.*\)', result)
  26      if (len(m) != len(output.parsed_as_key_val)):
  27          raise ValueError("ZAK Peer Port numbers mismatch found")
  28:     ports = re.findall(r'\d+', m[0])
  29      assert (len(ports) == 2)

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
  1625              try:
  1626:                 find = re.findall(r'STACK TRACE.*', output, re.MULTILINE)
  1627                  assert(len(find) == 0)

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\shm_tests\shm_helper.py:
  222                  "nslookup rvbd496-my.sharepoint.com")
  223:             dest_ip = re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  224                                   output)[1]

  227                  "nslookup public.boxcloud.com")
  228:             dest_ip = re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  229                                   output)[1]

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\configure.py:
  112                  model_str = show_version['product model']
  113:                 model_str = re.findall(r'\((.*)\)', model_str)[0]
  114                  cache['version'] = LegacyVersion(version)

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\rios_pxe_install.py:
  178  
  179:         name_servers = re.findall(r'Name server: (\S+) \(configured\)', output)
  180          for name_server in name_servers:

  182  
  183:         dns_suffixes = re.findall(r'Domain name: (\S+) \(configured\)', output)
  184          for dns_suffix in dns_suffixes:

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\verification.py:
  588              min_data_redux_pcent):
  589:         percentages = re.findall(r'(\d+)%', connection_summary)
  590          if not percentages:

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\zak_log_verifier.py:
  146          if 'messages' in log_dict['name']:
  147:             match_list = re.findall(r'\d+', log_dict['name'])
  148              sh_log_branch_list.append(match_list[0])

portfolio-system-tests\portfolio_system_tests\winsec\conftest.py:
  172      actual_config = server_sh.model.show_hosts().raw
  173:     dns_servers = re.findall(
  174          r'Name server:\s+(\d+\.\d+\.\d+\.\d+)\s+', actual_config)

  178      pattern = re.compile(regex)
  179:     domains = re.findall(pattern, actual_config)
  180      for domain in domains:

portfolio-system-tests\portfolio_system_tests\winsec\tests\test_adp_upgrade_sanity.py:
  57      # build number is 9
  58:     build = re.findall(r'/(?!.*/adproxy/.*/)(\d+)', image_url).pop()
  59  

ProjectVee\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  536      for line_number, line in lines_enum:
  537:         for env_var, var_name in ENV_VAR_RE.findall(line):
  538              value = os.getenv(var_name)

ProjectVee\venv\Lib\site-packages\pip\_vendor\chardet\charsetprober.py:
  85          # the end.
  86:         words = re.findall(b'[a-zA-Z]*[\x80-\xFF]+[a-zA-Z]*[^a-zA-Z\x80-\xFF]?',
  87                             buf)

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\compat.py:
  422  
  423:             matches = cookie_re.findall(line_string)
  424              if not matches:

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  725  
  726:                 archs = re.findall(r'-arch\s+(\S+)', cflags)
  727                  archs = tuple(sorted(set(archs)))

ProjectVee\venv\Lib\site-packages\pip\_vendor\html5lib\_inputstream.py:
  287      def characterErrorsUCS4(self, data):
  288:         for _ in range(len(invalid_unicode_re.findall(data))):
  289              self.errors.append("invalid-codepoint")

ProjectVee\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  899          clean = []
  900:         for prop, value in re.findall(r"([-\w]+)\s*:\s*([^:;]*)", style):
  901              if not value:

ProjectVee\venv\Lib\site-packages\pip\_vendor\requests\utils.py:
  449  
  450:     return (charset_re.findall(content) +
  451:             pragma_re.findall(content) +
  452:             xml_re.findall(content))
  453  

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_check_clock_ram_cpu.py:
  119                                  cvm_mem = cvm_output['memory']['used']
  120:                                 result = re.findall('.+%', mem_load)
  121                                  scm_mem_load = int(

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_cli.py:
  925              output = config.verify_sys_dump()
  926:             sys_dump_files = re.findall('case.+.tgz', output)
  927              output_sys_dump = cvm_shell.exec_command(

  930                  timeout=600)
  931:             cvm_sys_dump_files = re.findall(
  932                  'sysdump-cvm.+.tgz', output_sys_dump)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_connectivity.py:
  652              output = config.verify_sys_dump()
  653:             sys_dump_files = re.findall('case.+.tgz', output)
  654              output_sys_dump = cvm_shell.exec_command(

  656                  format(sys_dump_files[0]), timeout=600)
  657:             cvm_sys_dump_files = re.findall(
  658                  'sysdump-cvm.+.tgz', output_sys_dump)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_orchestration_agent.py:
  718      flow_rules = set(
  719:         re.findall(
  720              r'ingress=[\d\s]+egress=\d+',

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_rsyslog.py:
   996      parts_text = re.split(r'\[.*\]', data)
   997:     parts_bracket = re.findall(r'\[.*\]', data)
   998      assert len(parts_text) == 2, \

  1032                r' site-name="' + site_name + '" prefix="' + prefix + '"'
  1033:     x = re.findall(pattern, data)
  1034      if x is None:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\connection_resource.py:
  184      result = cvm_shell.exec_command('journalctl --disk-usage')
  185:     mem = re.findall(r'\d.+M', result)
  186      output = mem[0].split('M')

sc\portfolio-system-tests\portfolio_system_tests\legacy_gluon\libs\__init__.py:
  242      # This assumes the header names have no spaces in them
  243:     header_blocks = re.findall(r'\S+\s+(?=\S|$)', header)
  244      headers = [block.strip() for block in header_blocks]

sc\portfolio-system-tests\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_collision_wanopt_stale_entry.py:
  433      # connection trace is the one which is newly created.
  434:     syn_dif_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  435      assert(str(SYN_SAME_SEQ) not in syn_dif_seq[-1]), \

  739          src_ip, HTTP_SRC_PORT, dst_ip, HTTP_DST_PORT)
  740:     syn_same_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  741      # Remove the loadbalance rule from ICs.

sc\portfolio-system-tests\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_ic_owned_conn_reuse.py:
  349          var = ic.read_text_file(FILE_ORIG)
  350:         new_var = re.findall(r'id="\d{2,}"', var)
  351          new_vars = '{0}' .format(new_var[0]) + \

sc\portfolio-system-tests\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_path_selection_customer_issues.py:
  343      #  connection trace is the one which is newly created.
  344:     syn_dif_seq = re.findall(r'(?<=Syn#: )\d+', str(result))
  345      assert (str(SYN_SAME_SEQ) not in syn_dif_seq[-1]), \

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_brownfield_sites_1Panther_CF3_ha_gateway.py:
  381      # Configuring the inteceptor interfaces.
  382:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  383                           str(test_objects.int_if1.cidr))

  391                                  int_if1.inpath.inpath_gateway)
  392:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  393                           str(test_objects.int_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_brownfield_sites_3Panther_CF3_ha_gateway.py:
  420      # Configuring the inteceptor interfaces.
  421:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  422                           str(test_objects.int_if1.cidr))

  430                                  int_if1.inpath.inpath_gateway)
  431:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  432                           str(test_objects.int_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_single_panther_catfish_L2_ha_gateway.py:
  328      # Configuring the inteceptor interfaces.
  329:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(test_objects.int_if1.cidr))

  338                                  int_if1.inpath.inpath_gateway)
  339:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  340                           str(test_objects.int_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_single_panther_catfish_L3_ha_gateway.py:
  374      # Configuring the inteceptor interfaces.
  375:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  376                           str(test_objects.int_if1.cidr))

  384                                  int_if1.inpath.inpath_gateway)
  385:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  386                           str(test_objects.int_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_catfish_on_branch2.py:
  328      # Configuring the inteceptor interfaces.
  329:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(int_if1.cidr))

  337                                  ip_address=int_if1.inpath.inpath_gateway)
  338:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  339                           str(int_if2.cidr))

  368      # Configuring the IC1 inpath1 interface.
  369:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  370                                   str(phy_int1_if1.cidr))

  383      # Configuring the IC1 inpath2 interface.
  384:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  385                                   str(phy_int1_if2.cidr))

  426      # Configuring the IC2 inpath1 interface.
  427:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  428                                   str(phy_int2_if1.cidr))

  441      # Configuring the IC2 inpath2 interface.
  442:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  443                                   str(phy_int2_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_L3_single_catfish.py:
  319      # Configuring the inteceptor interfaces.
  320:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  321                           str(int_if1.cidr))

  328                                  ip_address=int_if1.inpath.inpath_gateway)
  329:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  330                           str(int_if2.cidr))

  359      # Configuring the IC1 inpath1 interface.
  360:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  361                                   str(phy_int1_if1.cidr))

  374      # Configuring the IC1 inpath2 interface.
  375:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  376                                   str(phy_int1_if2.cidr))

  417      # Configuring the IC2 inpath1 interface.
  418:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  419                                   str(phy_int2_if1.cidr))

  432      # Configuring the IC2 inpath2 interface.
  433:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  434                                   str(phy_int2_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways_single_panther.py:
  266      # Configuring the inteceptor interfaces.
  267:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  268                           str(test_objects.int_if1.cidr))

  276                                  int_if1.inpath.inpath_gateway)
  277:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  278                           str(test_objects.int_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_gateways.py:
  330      # Configuring the inteceptor interfaces.
  331:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  332                           str(int_if1.cidr))

  339                                  ip_address=int_if1.inpath.inpath_gateway)
  340:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  341                           str(int_if2.cidr))

  370      # Configuring the IC1 inpath1 interface.
  371:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  372                                   str(phy_int1_if1.cidr))

  385      # Configuring the IC1 inpath2 interface.
  386:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  387                                   str(phy_int1_if2.cidr))

  428      # Configuring the IC2 inpath1 interface.
  429:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  430                                   str(phy_int2_if1.cidr))

  443      # Configuring the IC2 inpath2 interface.
  444:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  445                                   str(phy_int2_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\test_configure_cc_with_split_site.py:
  325      # Configuring the inteceptor interfaces.
  326:     int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  327                           str(int_if1.cidr))

  334                                  ip_address=int_if1.inpath.inpath_gateway)
  335:     int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  336                           str(int_if2.cidr))

  365      # Configuring the IC1 inpath1 interface.
  366:     phy_ic1_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  367                                   str(phy_int1_if1.cidr))

  380      # Configuring the IC1 inpath2 interface.
  381:     phy_ic1_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  382                                   str(phy_int1_if2.cidr))

  423      # Configuring the IC2 inpath1 interface.
  424:     phy_ic2_int1_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  425                                   str(phy_int2_if1.cidr))

  438      # Configuring the IC2 inpath2 interface.
  439:     phy_ic2_int2_ip = re.findall(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  440                                   str(phy_int2_if2.cidr))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_dc_uplink.py:
  266          else:
  267:             dc_uplinks_teps['Internet'] = re.findall(r'[0-9]+(?:\.[0-9]+){3}',
  268                                                       dc_uplink.net)

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_change_panther_db_address.py:
  272      old_sd_wan = resources.ic1_model.show_sd_wan().raw
  273:     old_sd_wan_addr_list = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
  274                                        str(old_sd_wan))

sc\portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\sepia\conftest.py:
  110      result = client_shell.exec_command(cmd, error_expected=True)
  111:     return (len(re.findall("[0-9]+", result)))
  112  

  189              match = "TCP_MISS/200 [0-9]* GET " + url
  190:         if (len(re.findall(match, result)) < 1):
  191              raise VerificationError(

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_manage_appliances.py:
  192      group_info = resources.scc_actor.model.show_cmc_group(group=group).raw
  193:     lines = re.findall(r'.*/.*', group_info)
  194      return [i.split()[0] for i in lines]

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
  50          for x in range(1, 10):
  51:             subnet = re.findall(subnet_regex, delete_status)[0]
  52              port_id = commands.getoutput(

  66          for x in range(1, 10):
  67:             router_subnet = re.findall(router_regex, delete_status)[0]
  68              cmd = 'neutron router-update %s --routes action=clear' % (

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\populate_networks_subnets_images.py:
  75      site_id = all_sites[site]
  76:     branch_number = re.findall(r"[0-9]+$", site)[0]
  77      image_name = "vgw" + branch_number + "_pod" + str(pod) + "_image"

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\scale2_appliance_health_report.py:
  169      else:
  170:         node_memory_usage = re.findall(r'[0-9]+%', node_memory_string)[0]
  171      node_configuration = node['state']

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\script_appliance_health_report.py:
  182      else:
  183:         node_memory_usage = re.findall(r'[0-9]+%', node_memory_string)[0]
  184      node_configuration = node['state']

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\appliance.py:
  410              break
  411:         if (len(re.findall('inet6 addr', interface[1]))) > 1:
  412              interface[1] = interface[1]. \

  454      if pattern:
  455:         return re.findall(pattern, if_names)
  456      return if_names.split('\n')

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\traffic.py:
  104                            min_poll_interval=5):
  105:         accepted_flows = re.findall(r'Accepted: \d+', output)
  106          no_of_flows = [int(flow.split()[1]) for flow in accepted_flows]

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler_client.py:
  70      try:
  71:         client_ip = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', response)[0])
  72      except IndexError:
  73          response = request_new_ip(mgmt_ip, interface, dh_request)
  74:         client_ip = (re.findall(r'[0-9]+(?:\.[0-9]+){3}', response)[0])
  75      find_mac = re.compile('([0-9a-f]{2}(?::[0-9a-f]{2}){5})', re.IGNORECASE)
  76:     client_mac = (re.findall(find_mac, response)[0])
  77      if ipaddress.ip_address(client_ip):

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler.py:
  310  
  311:     split_var = re.findall(r'\s(\bZscaler\s\bCloud):', header)
  312      paragraph = header.split(split_var[0])[2]

  315          header_city = \
  316:             re.findall(r'\s[A-Z]*[a-z]*\s[A-Z]+[a-z]+\s[IV, III, II]*',
  317                         paragraph)[0].strip()
  318      else:
  319:         header_city = re.findall(r'[A-Z]*[a-z]*\s[A-Z]+[a-z]+\s[IV, III, II]*',
  320                                   paragraph)[0].strip()
  321:     header_cloud = re.findall(r'\s(\bzscalertwo).', paragraph)[0]
  322  

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\tests\performance\test_pload_http_performance.py:
  42      data = []
  43:     rows = re.findall(pattern, output)
  44      for row in rows:

  52      pattern = (r'.*::.* = .*')
  53:     row = re.findall(pattern, output)
  54      data = row[0].split('=')[1].split(':')[1]

  70          output = monitor_setup.shell.exec_command(cmd)
  71:         rows = re.findall(pattern, output)
  72  

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\tests\physical\uplinks\test_backup_uplink.py:
  105      cmd = node_shell.exec_command('traceroute 8.8.8.8 -m 1')
  106:     default_route = re.findall(r'\(([^)]+)', cmd)
  107      return default_route[1]

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\tests\wan_uplink_failover\test_uplink_ping_interval.py:
  153      for line in lines:
  154:         matches.append(re.findall(r'\d{2}:\d{2}\.\d{2}', line)[0])
  155          # 09:21:58.379343 IP 8.8.8.8 > 192.168.0.10: ICMP echo reply

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_zebos_config_check_bgp.py:
  48                  'remote-as' in line.strip():
  49:             gw_output['neighbor_ips'].append(re.findall(
  50                  r'[0-9]+(?:\.[0-9]+){3}', line)[0])
  51:             gw_output['neighbor_as'].append(re.findall(
  52                  r'remote-as (\w+)', line)[0])

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\test_bgp_ha_uplink.py:
  88          version = OS.get(gateway).shell.exec_command('imish -e "show ip bgp"')
  89:         zebos_version = re.findall(r"\d\.\d.\d", version)[0]
  90          logger.info("ZebOS-XP version is {}".format(zebos_version))

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_zebos_config_change.py:
  38                  re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  39:             gw_output['network'].append(re.findall(
  40                  r'[0-9]+(?:\.[0-9]+){3}', line)[0])
  41:             gw_output['area'].append(re.findall(
  42                  r'[0-9]+(?:\.[0-9]+){3}', line)[1])

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_remote_site_ospf_learning.py:
  36      for line in route.splitlines()[1:]:
  37:         if re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line):
  38              gw_output_routes.append(
  39:                 re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line)[0])
  40      return gw_output_routes

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\ospf_routemap\test_remote_site_states.py:
  35      for line in route.splitlines()[1:]:
  36:         if re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line):
  37              gw_output_routes.append(
  38:                 re.findall(r'[0-9]+(?:\.[0-9]+){3}/24', line)[0])
  39      return gw_output_routes

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\helpers\utils.py:
  171      route_op = container_shell.exec_command("vtysh -c 'show ip route'")
  172:     found = re.findall(r'(\d+\.\d+\.\d+\.\d+\/\d+)\s.+\s(\d+\.\d+\.\d+\.\d+)',
  173                         route_op)

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\openstack-tests\openstack_ops.py:
  114          if output[0]:
  115:             available_volume_ids_list = re.findall(r'\w+-\w+-\w+-\w+-\w+', output[1])
  116          else:

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\provisioning\get_build_from_deliverable.py:
  19      data = json.loads(resp.text)
  20:     int_array = re.findall(r'\d+', data["build"]["name"])
  21      print(str(int_array[-1]))

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\conftest.py:
  314          if (get_peer_ip):
  315:             peer_ip = re.findall(r'\d+\.\d+\.\d+\.\d+', output.raw)
  316              assert (len(peer_ip) == 1)

  880          if windows:
  881:             return re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  882                                output)[1]

  892          output = client_sh.exec_command("nslookup public.boxcloud.com")
  893:         return re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  894                            output)[1]

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\komodo\test_unsuccessful_edit_deployment.py:
  106                         "to support the number of users")
  107:             if not(re.findall(pattern, res.text)):
  108                  raise VerificationError(

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\truk\test_cfe_load_balancing.py:
  24      result = output.raw
  25:     m = re.findall(r'\(.*\)', result)
  26      if (len(m) != len(output.parsed_as_key_val)):
  27          raise ValueError("ZAK Peer Port numbers mismatch found")
  28:     ports = re.findall(r'\d+', m[0])
  29      assert (len(ports) == 2)

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
  1625              try:
  1626:                 find = re.findall(r'STACK TRACE.*', output, re.MULTILINE)
  1627                  assert(len(find) == 0)

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\shm_tests\shm_helper.py:
  222                  "nslookup rvbd496-my.sharepoint.com")
  223:             dest_ip = re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  224                                   output)[1]

  227                  "nslookup public.boxcloud.com")
  228:             dest_ip = re.findall("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*",
  229                                   output)[1]

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\configure.py:
  112                  model_str = show_version['product model']
  113:                 model_str = re.findall(r'\((.*)\)', model_str)[0]
  114                  cache['version'] = LegacyVersion(version)

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\rios_pxe_install.py:
  178  
  179:         name_servers = re.findall(r'Name server: (\S+) \(configured\)', output)
  180          for name_server in name_servers:

  182  
  183:         dns_suffixes = re.findall(r'Domain name: (\S+) \(configured\)', output)
  184          for dns_suffix in dns_suffixes:

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\verification.py:
  588              min_data_redux_pcent):
  589:         percentages = re.findall(r'(\d+)%', connection_summary)
  590          if not percentages:

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\zak_log_verifier.py:
  146          if 'messages' in log_dict['name']:
  147:             match_list = re.findall(r'\d+', log_dict['name'])
  148              sh_log_branch_list.append(match_list[0])

sc\portfolio-system-tests\portfolio_system_tests\winsec\conftest.py:
  172      actual_config = server_sh.model.show_hosts().raw
  173:     dns_servers = re.findall(
  174          r'Name server:\s+(\d+\.\d+\.\d+\.\d+)\s+', actual_config)

  178      pattern = re.compile(regex)
  179:     domains = re.findall(pattern, actual_config)
  180      for domain in domains:

sc\portfolio-system-tests\portfolio_system_tests\winsec\tests\test_adp_upgrade_sanity.py:
  57      # build number is 9
  58:     build = re.findall(r'/(?!.*/adproxy/.*/)(\d+)', image_url).pop()
  59  

VCMGUIAUTO_FF\VC_Test\Scripts\AddServerProfile.py:
  23          output=stdout.read()
  24:         if re.findall("Name[ ]+:[ ]+[A-Za-z_.]+", str(output)):
  25              return "PASS"

VCMGUIAUTO_FF\VC_Test\Scripts\VCMPythonScripts.py:
   48      #Domain Name       : VCDVT-ENC-165_vc_domain
   49:     x = re.findall("Domain Name[ ]+:[ ]+([A-Za-z-_0-9.]+)", str(output))
   50      if x == 0:

   66      output=stdout.read()
   67:     state=re.findall("Power[ ]+:[ ]+([A-Za-z]+)", str(output))
   68      status=state[0]

   84      output=stdout.read()
   85:     state=re.findall("Power[ ]+:[ ]+([A-Za-z]+)", str(output))
   86      if len(state)>0:

  158      out=stdout.read()
  159:     lst= re.findall(r'Address [SE][a-zA-Z: ]+([0-9A-F-]+)', str(out))
  160      if lst[0]==startmac and lst[1]==endmac:

  172      out=stdout.read()
  173:     lst= re.findall(r'([0-9A-F]+-[0-9A-F]+-[0-9A-F]+-[0-9A-F]+-[0-9A-F]+-[0-9A-F]+)', str(out))
  174      if len(lst)>0:

  187      print (out)
  188:     lst= re.findall('Role[ :]+Primary.*?IPv6 Address[ :]+([a-zA-Z:0-9]+)',str(out))
  189      if len(lst)>0:

  202      output = output.decode('ISO-8859-1')
  203:     x = re.findall("([A-Za-z0-9_]+)[ ]+Enet", str(output))
  204      return x

  278      if type=="Factory-Default":
  279:         lst= re.findall('WWN Address Type : ([A-Za-z-]+)',str(out))
  280          if len(lst)>0:

  287      if type=="User-Defined":
  288:         lst= re.findall('WWN Address Type : ([A-Za-z-]+)',str(out))
  289          if len(lst)>0:
  290              if lst[0]=="User-Defined":
  291:                 startwwn=re.findall('WWN Address Type : User-Defined.*?Start    : ([a-zA-Z:0-9]+)',str(out),re.DOTALL)
  292:                 endwwn=re.findall('WWN Address Type : User-Defined.*?End      : ([a-zA-Z:0-9]+)',str(out),re.DOTALL)
  293                  if len(startwwn)>0 and len(endwwn)>0:

  302      if type=="VC-Defined":
  303:         lst= re.findall('WWN Address Type : ([A-Za-z-]+)',str(out))
  304          print (lst[0])

  306              if lst[0]=="VC-Defined":
  307:                 startwwn=re.findall('WWN Address Type : VC-Defined.*?Start    : ([a-zA-Z:0-9]+)',str(out),re.DOTALL)
  308:                 endwwn=re.findall('WWN Address Type : VC-Defined.*?End      : ([a-zA-Z:0-9]+)',str(out),re.DOTALL)
  309                  if len(startwwn)>0 and len(endwwn)>0:

  326          out=stdout.read()
  327:         lst=re.findall('SUCCESS: Domain settings modified',str(out))
  328          if len(lst[0])>0:

  336          print(out)
  337:         lst=re.findall('SUCCESS: Domain settings modified',str(out))
  338          if len(lst[0])>0:

  346          print(out)
  347:         lstvc=re.findall('SUCCESS: Domain settings modified',str(out))
  348          if len(lstvc[0])>0:

  351              out=stdout.read()
  352:             lst= re.findall('WWN Address Type : ([A-Za-z-]+)',str(out))
  353              print(out)

  356                  if lst[0]=="VC-Defined":
  357:                     startwwn=re.findall('WWN Address Type : VC-Defined.*?Start    : ([a-zA-Z:0-9]+)',str(out),re.DOTALL)
  358                      print(startwwn)
  359:                     endwwn=re.findall('WWN Address Type : VC-Defined.*?End      : ([a-zA-Z:0-9]+)',str(out),re.DOTALL)
  360                      print(endwwn)

  376      print(out)
  377:     lst= re.findall(r'([0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+:).*?([0-9A-F]+:[0-9A-F]+:[0-9A-F]+:[0-9A-F]+)', str(out),re.DOTALL)
  378      if len(lst)>0:

  426      print(out)
  427:     lst= re.findall(r'SUCCESS: Profile copied', str(out))
  428      if len(lst)>0:

  450      print("Output:",output)
  451:     if re.findall("ERROR: No profiles exist", str(output)):
  452          return "PASS"

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  526      for line_number, line in lines_enum:
  527:         for env_var, var_name in ENV_VAR_RE.findall(line):
  528              value = os.getenv(var_name)

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\chardet\charsetprober.py:
  85          # the end.
  86:         words = re.findall(b'[a-zA-Z]*[\x80-\xFF]+[a-zA-Z]*[^a-zA-Z\x80-\xFF]?',
  87                             buf)

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\compat.py:
  422  
  423:             matches = cookie_re.findall(line_string)
  424              if not matches:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  725  
  726:                 archs = re.findall(r'-arch\s+(\S+)', cflags)
  727                  archs = tuple(sorted(set(archs)))

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\html5lib\_inputstream.py:
  293      def characterErrorsUCS4(self, data):
  294:         for _ in range(len(invalid_unicode_re.findall(data))):
  295              self.errors.append("invalid-codepoint")

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  879          clean = []
  880:         for prop, value in re.findall(r"([-\w]+)\s*:\s*([^:;]*)", style):
  881              if not value:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\requests\utils.py:
  449  
  450:     return (charset_re.findall(content) +
  451:             pragma_re.findall(content) +
  452:             xml_re.findall(content))
  453  

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\libdocpkg\model.py:
  54      def _create_toc(self, doc):
  55:         entries = re.findall(r'^\s*=\s+(.+?)\s+=\s*$', doc, flags=re.MULTILINE)
  56          if self.inits:

VCMGUIAUTO_FF\venv\Lib\site-packages\SeleniumLibrary\__init__.py:
  503          toc = ['== Table of contents ==', '']
  504:         all_match = re.findall(r'(^\=\s)(.+)(\s\=$)', intro, re.MULTILINE)
  505          for match in all_match:
