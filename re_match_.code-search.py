# Query: re.match(
# ContextLines: 1

1953 results - 1013 files

dist-packages\portfolio_system_tests\legacy_core_infra_nx\setup_upgrade\test_upgrade_scon.py:
  591      def is_cvm(unique_id):
  592:         return any((re.match('catfish-(.+)-cvm', unique_id),
  593:                     re.match('cluster-(.+)panther(.+)-cvm', unique_id)))
  594  

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_rsyslog.py:
  1053          pattern = format_name["pattern"]
  1054:         if re.match(pattern, data_part) is None:
  1055              assert False, \

  1255      if elements == 'priority':
  1256:         if re.match(format_names['priority'],
  1257                      data['priority']) is None:

  1263          time_date = data['time_date']
  1264:         if re.match(pattern, time_date) is None:
  1265              assert False, '{} does not match correct ' \

  1272          pattern = r'.*[a-zA-SU-Y].*'
  1273:         if re.match(pattern, timezone) is not None:
  1274              assert False, 'timestamp cannot contain ' \

  1283          part_date = parts[0]
  1284:         if re.match(pattern, part_date) is None:
  1285              assert False, \

  1319      structured_data = syslog_message_parts[appliance_type]['structured_data']
  1320:     if re.match(pattern, structured_data) is None:
  1321          assert False, "structured data does " \

  1331                r'\d{2}Z? [A-Z0-9]+ ([a-z]+|-) (\d+|-) (\d+|-)$'
  1332:     if re.match(pattern, text_string) is None:
  1333          assert False, "{} format is not " \

  1419      logger.debug("DEBUG: rsyslog status is [%s]", output)
  1420:     matched = re.match(r".*Active:([^\)]*\)).*", output, re.DOTALL)
  1421      result = ""

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_static_config.py:
  106      for i in splits:
  107:         if re.match(vp2, i):
  108              results.append(i)

  381              # looking for things like eth0, eth1.1, em0: followed by space.
  382:             devmatch = re.match(r'([a-z0-9_.-]+):*\s+(.+)',
  383                                  line, re.IGNORECASE)

  397                  mask = maskmatch.group(1).encode('utf8', 'ignore')
  398:                 if re.match('0x', mask):
  399                      # mask is in HEX, split and convert it.

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_stats_report_during_config_change.py:
  240      active_nodes = {}
  241:     if not re.match('catfish', resource_cvm.uniqueid):
  242          active_nodes = get_active_nodes(cvm=machine["cvm"])

  272          svm_timezone_prev = {}
  273:         if not re.match('catfish', resource_cvm.uniqueid):
  274              for node in resource_svm:

  338          svm_timezone_next = {}
  339:         if not re.match('catfish', resource_cvm.uniqueid):
  340              for node in resource_svm:

  359  
  360:         if not re.match('catfish', resource_cvm.uniqueid):
  361              for key, value in svm_timezone_next.iteritems():

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\connection_resource.py:
  764      """Get the service status."""
  765:     matched = re.match(r".*Active:([^\)]*\)).*", result, re.DOTALL)
  766      result = ""

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\redis_key_value_getter.py:
  40          logger.debug("Line [%s]", line)
  41:         match = re.match(r'.*{}.*'.format(status_key), line)
  42          if match:
  43              ospf_individual_key = line
  44:         match = re.match(r'.*versioned{}.*'.format(status_key), line)
  45          if match:

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\flows_performance\test_flows_perf.py:
  228          for pattern in patterns:
  229:             if re.match(pattern, line):
  230                  logger.info(line)

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\conftest.py:
   99              if 'Chassis Part Number' in fru.keys():
  100:                 if re.match("TP[12]U", fru['Chassis Part Number']):
  101                      return '2'

  123              if 'Chassis Part Number' in fru.keys():
  124:                 if re.match("TP[12]U", fru['Chassis Part Number']):
  125                      return 'Tarpan'
  126:                 elif re.match("Bluefin", fru['Chassis Part Number']):
  127                      return 'Bluefin'

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_external.py:
  29              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  30:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  31              assert fru['Board Mfg'] == 'RIOS'
  32:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  33              assert fru['Product Manufacturer'] == 'Riverbed'
  34              assert fru['Product Name'] == 'SteelFusion Edge'
  35:             # assert re.match('Bluefin [12]U', fru['Product Part Number'])
  36      except AssertionError as e:

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_ipmb.py:
  34              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  35:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  36:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  37              assert fru['Product Manufacturer'] == 'Riverbed'
  38              assert fru['Product Name'] == 'SteelFusion Edge'
  39:             # assert re.match('Bluefin [12]U', fru['Product Part Number'])
  40      except AssertionError as e:

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_local.py:
  29              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  30:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  31              assert fru['Board Mfg'] == 'RIOS'
  32:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  33              assert fru['Product Manufacturer'] == 'Riverbed'

dist-packages\portfolio_system_tests\legacy_core_pq_system_tests\core_pq_system_tests\ci_cd\test_devpi_server.py:
  348      """Upload packages to index."""
  349:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  350                         package_name)

  368      """Push packages to index."""
  369:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  370                         package_name)

  385      """Update a package."""
  386:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  387                         package_name)

  420      """Delete a package."""
  421:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  422                         package_name)

dist-packages\portfolio_system_tests\legacy_environment_templates_tests\system_tests\test_parallel_traffic_pload.py:
  100      """
  101:     server_match = re.match(r'server(\d).*', host.uniqueid)
  102      if server_match and server_match.group(1) != '1':

  104          return None
  105:     branch_match = re.match(r'.*([-\d])', host.uniqueid)
  106      if not branch_match:

dist-packages\portfolio_system_tests\legacy_environment_templates_tests\system_tests\test_traffic_pload.py:
  82      """
  83:     server_match = re.match(r'server(\d).*', host.uniqueid)
  84      if server_match and server_match.group(1) != '1':

  86          return None
  87:     branch_match = re.match(r'.*([-\d])', host.uniqueid)
  88      if not branch_match:

dist-packages\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_path_selection_customer_issues.py:
  459                                        ' | grep psic_pttcp_conn_count')
  460:     if not re.match(".*psic_pttcp_conn_count 0.*", result):
  461          raise VerificationError(description="psic_pttcp_conn_count is NOT 0",

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover_CF3.py:
  238              dct_variables['zone_ip'] = zone_network.netv4
  239:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  240                           str(dct_variables['zone_ip']))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover.py:
  240              dct_variables['zone_ip'] = zone_network.netv4
  241:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  242                           str(dct_variables['zone_ip']))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch_CF3.py:
  138              dct_variables['zone_ip'] = zone_network.netv4
  139:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  140                           str(dct_variables['zone_ip']))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch.py:
  138              dct_variables['zone_ip'] = zone_network.netv4
  139:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  140                           str(dct_variables['zone_ip']))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\Dual_Hub\test_branch2_switches_comes_back.py:
  168          for uplink in UPLINKS:
  169:             if (re.match(branch_uplink.name,
  170                           uplink['uplink_name'],

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\Dual_Hub\test_dual_hub_leaf_branch_switch.py:
  168          for uplink in UPLINKS:
  169:             if (re.match(branch_uplink.name,
  170                           uplink['uplink_name'],

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_add_delete_wan_branch_uplink_CF3.py:
  179      for branch in branch_list:
  180:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  181              uplink_list = test_objects.scm_actor.get_site_uplinks(

  183              for uplink in uplink_list:
  184:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  185                      # assign Uplink details before delete

  245      for branch in branch_list:
  246:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  247              uplink_list = test_objects.scm_actor.get_site_uplinks(

  249              for uplink in uplink_list:
  250:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  251                      # Moving into Internet WAN before deleting 

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_add_delete_wan_branch_uplink.py:
  177      for branch in branch_list:
  178:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  179              uplink_list = test_objects.scm_actor.get_site_uplinks(

  181              for uplink in uplink_list:
  182:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  183                      # assign Uplink details before delete

  248      for branch in branch_list:
  249:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  250              uplink_list = test_objects.scm_actor.get_site_uplinks(

  252              for uplink in uplink_list:
  253:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  254                      # Remove WAN Uplink

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch_CF3.py:
  186  
  187:         if re.match("Established", state, flags=re.IGNORECASE):
  188              state_regex = r'^\d+'

  199                      status = bgp_neigh['state/pfxrcd']
  200:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  201                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  267              dct_variables['zone_ip'] = zone_network.netv4
  268:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  269                           str(dct_variables['zone_ip']))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch.py:
  186  
  187:         if re.match("Established", state, flags=re.IGNORECASE):
  188              state_regex = r'^\d+'

  199                      status = bgp_neigh['state/pfxrcd']
  200:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  201                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  267              dct_variables['zone_ip'] = zone_network.netv4
  268:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  269                           str(dct_variables['zone_ip']))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone_CF3.py:
  248              zone_ip = zone_network.netv4
  249:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  250                           str(zone_ip))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone.py:
  249              zone_ip = zone_network.netv4
  250:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  251                           str(zone_ip))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_uplink_wantype.py:
  312                  # Example:NEW_WAN_NAME='WAN2_Uplink',uplink.name='WAN2_Uplink'
  313:                 if re.match(old_uplink_name,
  314                              uplink.name, flags=re.IGNORECASE):

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_wan_uplink_ipaddress.py:
  102      # Regular expression that matches the ip address
  103:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  104                   str(branch2_tep_wan.cidr))

  233      for uplink in uplink_list:
  234:         if re.match(uplink.name, wan_uplink_name, flags=re.IGNORECASE):
  235              # Update IPV4 address of branch2 WAN uplink

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_as_mismatch.py:
  147              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  148:             assert(not re.match(r'^Established', state)), msg.format(state,
  149                                                                       neigh_ip)

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_nondefaults.py:
  149              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  150:             assert(re.match(r'^Established', state)), msg.format(state,
  151                                                                   neigh_ip)

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_match.py:
  182              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  183:             assert(re.match(r'^Established', state)), msg.format(state,
  184                                                                   neigh_ip)

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_mismatch.py:
  161                  "Actual state is {}. Expected is not 'Established' for i.f. {}"
  162:             assert(not re.match(r'^Established', state)), msg.format(state,
  163                                                                       neigh_ip)

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_peering.py:
  140                      status = bgp_neigh['state/pfxrcd']
  141:                     if not re.match(r'^\d+', status):
  142                          logger.info("BGP connection for " + str(neigh.cidr.ip))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_states_dynamic_changes.py:
  146  
  147:         if re.match("Established", state, flags=re.IGNORECASE):
  148              state_regex = r'^\d+'

  159                      status = bgp_neigh['state/pfxrcd']
  160:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  161                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  178          for interface in tep_resource.interfaces:
  179:             if re.match('^tunnel', interface.device):
  180                  ip, mask = str(interface.cidr).split('/')

  194      # Regular expression that matches the ip address
  195:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)", ip_with_mask)
  196  

  208      # Regular expression that matches the ip address
  209:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
  210  

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_ibgp_peering_on_wdr1_fails.py:
  210          bgp_summary[router_name.hostname] = wdr_obj.get_bgp_summary()
  211:         if re.match("Established", state, flags=re.IGNORECASE):
  212              state_regex = r'^\d+'

  222                      status = bgp_neigh['state/pfxrcd']
  223:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  224                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  240          router_name = dict['router']
  241:         if re.match(router_name.hostname, 'wdr1', re.IGNORECASE):
  242              wdr_obj = NetDevice.get(router_name)

  259          router_name = router._resource.hostname
  260:         if re.match(router_name, 'wdr1', re.IGNORECASE):
  261              neighbor_list = wdr_neighbor_list[router_name]

  277              router_name = router._resource.hostname
  278:             if re.match(router_name, 'wdr1', re.IGNORECASE):
  279                  neighbor_list = wdr_neighbor_list[router_name]

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_route_injection.py:
   91                      status = bgp_neigh['state/pfxrcd']
   92:                     if not re.match(r'\d+', status):
   93                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  113          for interface in tep_resource.interfaces:
  114:             if re.match('^tunnel', interface.device):
  115                  ip, mask = str(interface.cidr).split('/')

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_subnet_splitting.py:
  192          bgp_summary = wdr_obj.get_bgp_summary()
  193:         if re.match("Established", state, flags=re.IGNORECASE):
  194              state_regex = r'^\d+'

  204                      status = bgp_neigh['state/pfxrcd']
  205:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  206                          logger.info("BGP connection for " + str(neigh.cidr.ip))

dist-packages\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_hostlabel.py:
  145              """
  146:             regex = re.match(r'(.*)init client(.*)', line)
  147              if regex:

dist-packages\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_inpath_rules.py:
  296          for line in f:
  297:             matchsplice = re.match(r'(.*)init client(.*)dst(.*)',
  298                                     line)

  308                  nextline = next(f)
  309:                 matchsplice = re.match(r'(.*)' + port + '}(.*)', nextline)
  310                  if matchsplice:

dist-packages\portfolio_system_tests\legacy_shsaas_tests\tools\common.py:
  38      """Check if input is a valid IPv4 or subnetted IPv4 address."""
  39:     ip_match = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/\d{1,2})?$", line)  # noqa
  40      if not ip_match:

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
   58              x = x + 1
   59:             if re.match(r'Stack not found', delete_status):
   60                  print("Stack {0} deleted successfully".format(stack_name))

   72              x = x + 1
   73:             if re.match(r'Stack not found', delete_status):
   74                  print("Stack {0} deleted successfully".format(

  104          delete_status = delete_stack(args.stack_name)
  105:         if re.match(r'Stack not found', delete_status):
  106              print("Stack {0} deleted successfully".format(args.stack_name))

  127                  delete_status = delete_stack(stack[1])
  128:                 if re.match(r'Stack not found', delete_status):
  129                      print("Stack {0} deleted successfully".format(stack[1]))

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\syslog.py:
  414  
  415:     match = re.match(pattern_priority, part1[0].strip())
  416      assert match is not None, (

  420  
  421:     match = re.match(kwargs['serial'], part1[2].strip())
  422      assert match is not None, (

  426  
  427:     match = re.match(pattern_scm_info, splitted_line[1])
  428      assert match is not None, (

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_default_route_originate.py:
  385              if num + 2 <= len(list1):
  386:                 regex_output = re.match("^O\s+(0.0.0.0\/0).+", route)  # noqa
  387                  if regex_output:

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_static_routing.py:
  284          if num < len(static_list):
  285:             regex_output = re.match(r"^S\W+(\d+.\d+.\d+.\d)", route)
  286              if regex_output:

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_new_zone_discovery.py:
  53      zone_ip = zone_network.netv4
  54:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  55                   str(zone_ip))

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_route_peering.py:
  41          for element in split_output:
  42:             if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]",
  43                              element):

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\test_leaf_mode.py:
  95              # Look for the right route chain
  96:             if re.match(site['chain'], chain):
  97                  for line in chain.split('\n'):

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
  936                  key = STT_TOOL_PARAMS[key]
  937:             if(re.match('.$', key)):
  938                  str_param = f'-{key} {val}' if val else f'-{key}'

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\scc_configs.py:
  110              rule_num_pattern = r".*/rule/([0-9]+)$"
  111:             enable_match = re.match(enable_pattern, node_info['path'])
  112:             rule_num_match = re.match(rule_num_pattern, node_info['path'])
  113              if enable_match or rule_num_match:

dist-packages\portfolio_system_tests\spoon_tests\libs\configure.py:
  1741          for line in config:
  1742:             if re.match(r".*/rule/([0-9]+)$", line.strip()):
  1743                  num_inpath_rules += 1

  1779              # using an mdreq command
  1780:             src_match = re.match(src_pattern, node_name)
  1781:             dst_match = re.match(dst_pattern, node_name)
  1782:             hst_match = re.match(hst_pattern, node_name)
  1783              if src_match:

dist-packages\portfolio_system_tests\spoon_tests\libs\resources.py:
  189              for ipport in ipports:
  190:                 match = re.match(ipport_pattern, ipport)
  191                  if not match:

  396          node_names = [n['name'] for n in cvm_running_nodes]
  397:         if not re.match(".*vsh.*", "".join(node_names)):
  398              raise RuntimeError("No VSH node yet.")

  427              match = m.string[m.start():m.end()]
  428:             if re.match(ssh_prompts[0], match):
  429                  sync_channel.send("yes\n")

  470  
  471:         if re.match(login_matches[0], match):
  472              logger.debug("Got the initial configuration wizard.")

  483          match = m.string[m.start():m.end()]
  484:         addr_match = re.match(patt, match)
  485          primary_addr = addr_match.group(1)

dist-packages\portfolio_system_tests\spoon_tests\libs\verification.py:
  109      for line in file_contents:
  110:         if re.match(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line) and \
  111             re.search(r'ERR(OR)?\]', line):

  143      for line in log_file:
  144:         if re.match(r'^\d+-\d+-\d+', line):
  145              if currDict:

dist-packages\portfolio_system_tests\tiramisu\shminstaller.py:
  237          match_lines = [
  238:             re.match(r'(?P<pid>\d+)', line) for line in out.splitlines()
  239          ]

dist-packages\pq_core\communication\parsers.py:
  1369                  else:
  1370:                     match = re.match(r'(\d+)', str(value))
  1371                      if match:

  1800  
  1801:         m = re.match(r"\+?\s*(.*) {", line)
  1802          if m is not None:

dist-packages\pq_core\communication\cli\__init__.py:
  551          if output and self.CLI_ERROR_PROMPT and \
  552:                 re.match(self.CLI_ERROR_PROMPT, output):
  553              if error_expected:

dist-packages\pq_core\communication\cli\ftos_cli.py:
  95  
  96:             if re.match(self.CLI_ERROR_PROMPT, match_res.string):
  97                  raise exceptions.CLIError(

dist-packages\pq_core\communication\cli\quagga_cli.py:
  69  
  70:             if re.match(self.CLI_ERROR_PROMPT, match_res.string):
  71                  raise exceptions.CLIError(

dist-packages\pq_core\communication\cli\vyatta_cli.py:
  119  
  120:                 if re.match(self.CLI_ERROR_PROMPT, match_res.string):
  121                      raise exceptions.CLIError(

dist-packages\pq_core\lab\container.py:
  210                  if strict is not True:
  211:                     if re.match(value, test_value):
  212                          results[k_dict] = v_dict

dist-packages\pq_core\lab\interface.py:
  390          test_ip = str(self._cidr.ip)
  391:         if re.match(r'(\d+)\.\1\.\1\.\1', test_ip) or test_ip in INVALID_IPS:
  392              # if the ip address is something like '0.0.0.0' or '1.1.1.1' or

dist-packages\pq_core\lab\query.py:
  156                  if strict is not True:
  157:                     if re.match(value, test_value):
  158                          results.append(opt)

dist-packages\pq_core\lab\chassis\physical.py:
  278                       command, self._term_srv, output)
  279:         match = re.match(r'\s*(\d+) unauth.*pmshell -l ' + port_str, output)
  280          if match:

dist-packages\pq_core\lab\netdevice\vyatta.py:
  2230          for line in output.splitlines():
  2231:             line_result = bgp_re.match(line)
  2232              line_dict = {}

dist-packages\pq_core\lab\netdevice\dummynet\__init__.py:
  395              for file_name in file_list:
  396:                 result = re.match(r'pipe_(?P<pipe_num>\d+)', file_name)
  397                  if result:

dist-packages\pq_core\lab\orchestrator\vlab.py:
  511          if physical_model:
  512:             match = PRODUCT_HINT_RE.match(physical_model)
  513              serial_number = match and match.groups(1)[0]

  520          # Steelhead fallback
  521:         if qa_type and STEELHEAD_RE.match(qa_type):
  522              return STEELHEAD_HINT

  878          """Convert VLAB physical model to appliance model string."""
  879:         matched = re.match(r'([A-Z]+)-(\d+)-([A-Z0-9]+)', physical_model)
  880          if matched:

  894          """Get model family name from model string e.g. CX570 -> CX."""
  895:         family = re.match(r'([A-Z]+)[^A-Z]+', model)
  896          if family:

dist-packages\pq_core\lab\os\networking\__init__.py:
   83              # looking for things like eth0, eth1.1, em0: followed by space.
   84:             devmatch = re.match(r'([a-z0-9_.-]+):*\s+(.+)',
   85                                  line, re.IGNORECASE)

  103                  mask = maskmatch.group(1)
  104:                 if re.match('0x', mask):
  105                      # mask is in HEX, split and convert it.

dist-packages\pq_core\lab\os\networking\ipfw.py:
  57                   r'(?P<queue>\d+)\s+sl\.(plr\s+(?P<plr>\d+\.\d+))*\s+')
  58:         parts = re.match(regex, pipe_string)
  59          if parts:

dist-packages\pq_core\runtime\heartbeat_pytest.py:
  85      for pattern in __IGNORE_TEST_REPORTING__:
  86:         if re.match(pattern, report.location[0]):
  87              return

dist-packages\pq_fwk\build.py:
  731      #  build id is something like: #39
  732:     rel_match = re.match(r'[\d*\.]*\d+', version_info['product release'])
  733      if not rel_match:

dist-packages\pq_lib\data.py:
  60              self._path = None
  61:         elif re.match(r'\\', path) or re.match(r'\S:', path):
  62              # Assume windows if back slashes or starts with <drive-letter>:

dist-packages\pq_lib\tools\apache.py:
  234          for line in output.splitlines():
  235:             m = ps_re.match(line)
  236              if m is not None:

dist-packages\pq_lib\tools\bind9.py:
   86          for line in output.splitlines():
   87:             match = re.match(r'zone "(\S+)"', line)
   88              if match:

   91  
   92:             match = re.match(r'\s+file "(\S+)"', line)
   93              if match and current_zone:

  108              if zone.name == ".":
  109:                 match = re.match(r"(.+)\.\\" + zone.name, name)
  110              else:
  111:                 match = re.match(r"(.+)\." + zone.name, name)
  112              if match:

dist-packages\pq_lib\tools\curl_loader.py:
  215                      continue
  216:                 process_match = process_re.match(line)
  217                  self._pid = process_match.group(1)

  291              logger.debug('looking for %s in %s', process_re.pattern, line)
  292:             process_match = process_re.match(line)
  293              if process_match is not None:

  453          batch_name_re = re.compile(r'BATCH_NAME\s*=\s*(.*)')
  454:         batch_name_match = batch_name_re.match(batch_name_line)
  455          if batch_name_match is None:

  464          cycles_num_re = re.compile(r'CYCLES_NUM\s*=\s*(.*)')
  465:         cycles_num_match = cycles_num_re.match(cycles_num_line)
  466          if cycles_num_match is None:

dist-packages\pq_lib\tools\curl.py:
  233          for line in output.splitlines():
  234:             m = ps_re.match(line)
  235              if m is not None:

dist-packages\pq_lib\tools\dhcpd.py:
  139                  for regex, var in regexes.items():
  140:                     match = re.match(regex, line)
  141                      if match:

  145                  # We're starting a new lease entry.
  146:                 match = re.match(r'lease (\S+) {', line)
  147                  if match:

  173              for regex, var in regexes.items():
  174:                 match = re.match(regex, line)
  175                  if match:

  179              option_regex = r'\s+option "?(\S+)"? (\S+)"?;'
  180:             match = re.match(option_regex, line)
  181              if match:

  211          for line in output.splitlines():
  212:             match = re.match(option_regex, line)
  213              if match:

dist-packages\pq_lib\tools\dnsname.py:
  52          # If the name is an ip, return immediately
  53:         if re.match(IPV4_REGEX, name):
  54              return name

dist-packages\pq_lib\tools\http_client.py:
  188                  logger.debug(f'looking for "{resource_re.pattern}" in {line}')
  189:                 mymatch = resource_re.match(line)
  190                  if mymatch is not None:

  233          for line in output.splitlines():
  234:             m = ps_re.match(line)
  235              if m is not None:

dist-packages\pq_lib\tools\http_server.py:
  224                               line)
  225:                 mymatch = remote_resource_re.match(line)
  226                  if mymatch is not None:

dist-packages\pq_lib\tools\interface_tools.py:
  309              # looking for things like eth0, eth1.1, em0: followed by space.
  310:             devmatch = re.match(r'([a-z0-9_.-]+):*\s+(.+)',
  311                                  line, re.IGNORECASE)

  329                  mask = maskmatch.group(1)
  330:                 if re.match('0x', mask):
  331                      # mask is in HEX, split and convert it.

dist-packages\pq_lib\tools\iperf.py:
  588          for line in out:
  589:             mymatch = re.match(reg_exp, line)
  590  

  627                               line)
  628:                 mymatch = server_re.match(line)
  629                  if mymatch is not None:

  682                               line)
  683:                 mymatch = client_re.match(line)
  684                  if mymatch is not None:

dist-packages\pq_lib\tools\ipfw.py:
  68                   r'(?P<queue>\d+)\s+sl\.(plr\s+(?P<plr>\d+\.\d+))*\s+')
  69:         parts = re.match(regex, pipe_string)
  70          if parts:

dist-packages\pq_lib\tools\moh_load.py:
  330                               line)
  331:                 mymatch = remote_resource_re.match(line)
  332                  if mymatch is not None:

dist-packages\pq_lib\tools\netstat.py:
  363              logger.debug('looking for "%s" in %s', regex, line)
  364:             mymatch = re.match(regex, line)
  365              if mymatch is not None:

  396              logger.debug('looking for "%s" in %s', regex, line)
  397:             mymatch = re.match(regex, line)
  398              if mymatch is not None:

  431              logger.debug('looking for "%s" to not be in %s', regex, line)
  432:             mymatch = re.match(regex, line)
  433              if mymatch is not None:

dist-packages\pq_lib\tools\nfs_standalone.py:
  237                  # Line must have content
  238:                 not re.match(r'^\s*$', line.strip()) and (
  239                      # Skip comment lines

dist-packages\pq_lib\tools\openssl_traffic.py:
  219                  re_ip = "^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$"
  220:                 if not re.match(re_ip, ssl_serv_ip):
  221                      raise ValueError('You must specify a valid server IP')

  259                  re_ip = "^[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}$"
  260:                 if not re.match(re_ip, ssl_serv_ip):
  261                      raise ValueError('You must specify a valid server IP')

  633                               line)
  634:                 mymatch = pid_from_ps_l_re.match(line)
  635                  if mymatch is not None:

dist-packages\pq_lib\tools\outlook.py:
  131                                             log_cmd=False, log_output=False)
  132:             match_obj = re.match(r'Outlook\.Application\.(\d+)',
  133                                   output.strip())

dist-packages\pq_lib\tools\pload.py:
  586              for line in out:
  587:                 mymatch = remote_resource_re.match(line)
  588                  if mymatch is not None:

  645              for line in out:
  646:                 mymatch = resource_re.match(line)
  647                  if mymatch is not None:

dist-packages\pq_lib\tools\s_server.py:
  418          for line in output.splitlines():
  419:             m = ps_re.match(line)
  420              if m is not None:

dist-packages\pq_lib\tools\sp_load.py:
  189                               line)
  190:                 mymatch = remote_resource_re.match(line)
  191                  if mymatch is not None:

  247                               line)
  248:                 mymatch = resource_re.match(line)
  249                  if mymatch is not None:

dist-packages\pq_lib\tools\top.py:
  159                          users = re.search(r'\d+ user', line).group()
  160:                         top_dict[keyname]['users'] = int(re.match(r'\d+',
  161                                                           users).group())
  162                          up_time = re.search(r'\d+ days', line).group()
  163:                         top_dict[keyname]['up_time'] = int(re.match(r'\d+',
  164                                                             up_time).group())

dist-packages\pq_lib\tools\trace.py:
  131                                   line)
  132:                     mymatch = resource_re.match(line)
  133                      if mymatch is not None:

dist-packages\pq_lib\traffic\__init__.py:
  68          for line in lines:
  69:             test_m = re.match(reg_exp, line)
  70  

dist-packages\pq_lib\traffic\pload.py:
  308          for line in out:
  309:             mymatch = re.match(reg_exp, line)
  310  

  343              for line in out:
  344:                 mymatch = server_re.match(line)
  345                  if mymatch is not None:

  411              for line in out:
  412:                 mymatch = client_re.match(line)
  413                  if mymatch is not None:

dist-packages\pq_lib\utils\dns_conf_builder.py:
  93              if zone.name == ".":
  94:                 match = re.match(r"(.+)\.\\" + zone.name, name)
  95              else:
  96:                 match = re.match(r"(.+)\." + zone.name, name)
  97              if match:

dist-packages\pq_orclib\config_utilities\__init__.py:
  37              else:
  38:                 config_match = re.match(regex, line)
  39                  if config_match:

dist-packages\pq_orclib\o365d\__init__.py:
  135                  """
  136:                 regex = re.match(r'(.*)init client(.*)', line)
  137                  if regex:

  147  
  148:                 matchsplice = re.match(r'(.*)init client(.*)dst(.*)',
  149                                         line)

  157                      nextline = next(f)
  158:                     matchsplice = re.match(r'(.*)' + port + '}(.*)', nextline)
  159                      if matchsplice:

dist-packages\pq_orclib\panther\__init__.py:
  315          # Regular expression that matches the network address and prefix
  316:         m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)", network)
  317  

dist-packages\pq_orclib\sc_configurator\appliance_setup.py:
  155          code_key = None
  156:         matched = re.match(r'^CX(\d+)[LMH]?$', model, re.I)
  157          if matched:

  330          # setup vSH for devices that support it
  331:         if re.match(r'^CX(570|770|3070)H?$', node_record.model, re.I):
  332              sh_mac = hyp_shell.exec_command(

dist-packages\pq_orclib\scc_configuration\__init__.py:
  44      version = version.replace('rbt_sh', '').strip()
  45:     exact_version = re.match(r'\d+.\d+.\d+', version).group(0)
  46      # Base url.

  51      # Look in major folder.
  52:     if re.match(r'\d+.\d+.0$', version):
  53          url = base_url + '/major/ga/' + build.strip('#') + last_part

  56      # Look in major mainline folder.
  57:     if re.match(r'\d+.\d+.0+-mainline', version):
  58          url = base_url + '/major/mainline/' + build.strip('#') + last_part

  61      # Look in point folder.
  62:     if re.match(r'\d+.\d+.\d+$', version):
  63          url = base_url + '/point/' + version + \

dist-packages\venv\Lib\site-packages\autopep8.py:
  1072          # Handle very easy "not" special cases.
  1073:         if re.match(r'^\s*if [\w."\'\[\]]+ == False:$', target):
  1074              self.source[line_index] = re.sub(r'if ([\w."\'\[\]]+) == False:',
  1075                                               r'if not \1:', target, count=1)
  1076:         elif re.match(r'^\s*if [\w."\'\[\]]+ != True:$', target):
  1077              self.source[line_index] = re.sub(r'if ([\w."\'\[\]]+) != True:',

  1090              if center.strip() == '==':
  1091:                 if re.match(r'\bTrue\b', right):
  1092                      new_right = re.sub(r'\bTrue\b *', '', right, count=1)
  1093              elif center.strip() == '!=':
  1094:                 if re.match(r'\bFalse\b', right):
  1095                      new_right = re.sub(r'\bFalse\b *', '', right, count=1)

  1322          next_line_indent = 0
  1323:         m = re.match(r'\s*', next_line)
  1324          if m:

  3260          return line[:max_line_length] + '\n'
  3261:     elif last_comment and re.match(r'\s*#+\s*\w+', line):
  3262          split_lines = textwrap.wrap(line.lstrip(' \t#'),

  3752      for attribute in dir(instance):
  3753:         code = re.match('fix_([ew][0-9][0-9][0-9])', attribute)
  3754          if code:

  3870          # Avoid breaking at unary operators.
  3871:         if re.match(r'.*[(\[{]\s*[\-\+~]$', current_line.rstrip('\\ ')):
  3872              rank += 1000
  3873  
  3874:         if re.match(r'.*lambda\s*\*$', current_line.rstrip('\\ ')):
  3875              rank += 1000

dist-packages\venv\Lib\site-packages\pycodestyle.py:
  1059              yield 0, "E402 module level import not at top of file"
  1060:     elif re.match(DUNDER_REGEX, line):
  1061          return

dist-packages\venv\Lib\site-packages\pyparsing.py:
  2730          if self.re:
  2731:             result = self.re.match(instring,loc)
  2732              if not result:

  2852      def parseImpl( self, instring, loc, doActions=True ):
  2853:         result = self.re.match(instring,loc)
  2854          if not result:

  2994      def parseImpl( self, instring, loc, doActions=True ):
  2995:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2996          if not result:

dist-packages\venv\Lib\site-packages\_distutils_hack\__init__.py:
  35      warnings.warn("Setuptools is replacing distutils.")
  36:     mods = [name for name in sys.modules if re.match(r'distutils\b', name)]
  37      for name in mods:

dist-packages\venv\Lib\site-packages\_pytest\pytester.py:
  1735          __tracebackhide__ = True
  1736:         self._match_lines_random(lines2, lambda name, pat: bool(re.match(pat, name)))
  1737  

  1800              lines2,
  1801:             lambda name, pat: bool(re.match(pat, name)),
  1802              "re.match",

  1887          self._no_match_line(
  1888:             pat, lambda name, pat: bool(re.match(pat, name)), "re.match"
  1889          )

dist-packages\venv\Lib\site-packages\_pytest\mark\expression.py:
  90              else:
  91:                 match = re.match(r"(:?\w|:|\+|-|\.|\[|\])+", input[pos:])
  92                  if match:

dist-packages\venv\Lib\site-packages\astroid\brain\brain_gi.py:
  33          # Check if this is a valid name in python
  34:         if not re.match(_identifier_re, name):
  35              continue

dist-packages\venv\Lib\site-packages\cffi\api.py:
  760          import re
  761:         match = re.match(r'\s*\n', pysource)
  762          if match:

  764          lines = pysource.splitlines() or ['']
  765:         prefix = re.match(r'\s*', lines[0]).group()
  766          for i in range(1, len(lines)):

dist-packages\venv\Lib\site-packages\cffi\cparser.py:
  350          msg = str(e)
  351:         match = re.match(r"%s:(\d+):" % (CDEF_SOURCE_STRING,), msg)
  352          if match:

dist-packages\venv\Lib\site-packages\docutils\statemachine.py:
    12  - `StateWS`, a state superclass for use with `StateMachineWS`
    13: - `SearchStateMachine`, uses `re.search()` instead of `re.match()`
    14: - `SearchStateMachineWS`, uses `re.search()` instead of `re.match()`
    15  - `ViewList`, extends standard Python lists.

  1041  
  1042:     Changes regular expression matching, from the default `re.match()`
  1043      (succeeds only if the pattern matches at the start of `self.line`) to

  1060  class SearchStateMachine(_SearchOverride, StateMachine):
  1061:     """`StateMachine` which uses `re.search()` instead of `re.match()`."""
  1062      pass

  1065  class SearchStateMachineWS(_SearchOverride, StateMachineWS):
  1066:     """`StateMachineWS` which uses `re.search()` instead of `re.match()`."""
  1067      pass

dist-packages\venv\Lib\site-packages\docutils\parsers\rst\states.py:
  2193          for i, line in enumerate(arg_block):
  2194:             if re.match(Body.patterns['field_marker'], line):
  2195                  opt_block = arg_block[i:]

dist-packages\venv\Lib\site-packages\docutils\parsers\rst\directives\__init__.py:
  234      """
  235:     match = re.match(r'^([0-9.]+) *(%s)$' % '|'.join(units), argument)
  236      try:

dist-packages\venv\Lib\site-packages\docutils\writers\_html_base.py:
  935                  if att_name in atts:
  936:                     match = re.match(r'([0-9.]+)(\S*)$', atts[att_name])
  937                      assert match

  943              if att_name in atts:
  944:                 if re.match(r'^[0-9.]+$', atts[att_name]):
  945                      # Interpret unitless values as pixels.

dist-packages\venv\Lib\site-packages\docutils\writers\latex2e\__init__.py:
  2345                               ' option `pxunit` will be removed.')
  2346:         match = re.match(r'(\d*\.?\d*)\s*(\S*)', length_str)
  2347          if not match:

dist-packages\venv\Lib\site-packages\funcsigs\__init__.py:
  269              name = str(name)
  270:             if kind != _POSITIONAL_ONLY and not re.match(r'[a-z_]\w*$', name, re.I):
  271                  msg = '{0!r} is not a valid parameter name'.format(name)

dist-packages\venv\Lib\site-packages\git\config.py:
  315              # is it a section header?
  316:             mo = self.SECTCRE.match(line.strip())
  317              if not is_multi_line and mo:

  333              elif not is_multi_line:
  334:                 mo = self.OPTCRE.match(line)
  335                  if mo:

dist-packages\venv\Lib\site-packages\hpe3parclient\ssh.py:
  238          command_string = ' '.join(cmd)
  239:         if re.match('|'.join(tpd_commands), command_string):
  240              escp_command_string = command_string.replace('"', '\\"')

  283          """
  284:         if re.match('|'.join(tpd_commands), cmd):
  285              cmd = 'Tpd::rtpd "' + cmd.replace('"', '\\"') + '"'

  360              # Check for matching quotes on the ends
  361:             is_quoted = re.match('^(?P<quote>[\'"])(?P<quoted>.*)(?P=quote)$',
  362                                   arg)

  366                  if quoted:
  367:                     if (re.match('[\'"]', quoted) or
  368                              re.search('[^\\\\][\'"]', quoted)):

dist-packages\venv\Lib\site-packages\jinja2\utils.py:
  277          head, middle, tail = "", word, ""
  278:         match = re.match(r"^([(<]|&lt;)+", middle)
  279  

  309  
  310:         if _http_re.match(middle):
  311              if middle.startswith("https://") or middle.startswith("http://"):

  320  
  321:         elif middle.startswith("mailto:") and _email_re.match(middle[7:]):
  322              middle = f'<a href="{middle}">{middle[7:]}</a>'

  327              and ":" not in middle
  328:             and _email_re.match(middle)
  329          ):

dist-packages\venv\Lib\site-packages\jsonschema\_format.py:
  163          return True
  164:     if not _ipv4_re.match(instance):
  165          return False

  183          return True
  184:     if not _host_name_re.match(instance):
  185          return False

dist-packages\venv\Lib\site-packages\openpyxl\formatting\rule.py:
  33          if value is not None and isinstance(value, basestring):
  34:             ref = COORD_RE.match(value)
  35          if instance.type == "formula" or ref:

dist-packages\venv\Lib\site-packages\openpyxl\formula\tokenizer.py:
  167          self.items.append(Token(' ', Token.WSPACE))
  168:         return self.WSPACE_RE.match(self.formula[self.offset:]).end()
  169  

  280                  and len(self.token) >= 1
  281:                 and self.SN_RE.match("".join(self.token))):
  282              self.token.append(curr_char)

  402          if func:
  403:             assert re.match('.+\\(|\\)', value)
  404              type_ = Token.FUNC

dist-packages\venv\Lib\site-packages\openpyxl\formula\translate.py:
  112          ws_part, range_str = cls.strip_ws_name(range_str)
  113:         match = cls.ROW_RANGE_RE.match(range_str)  # e.g. `3:4`
  114          if match is not None:

  116                      + cls.translate_row(match.group(2), rdelta))
  117:         match = cls.COL_RANGE_RE.match(range_str)  # e.g. `A:BC`
  118          if match is not None:

  129                  for piece in range_str.split(':'))
  130:         match = cls.CELL_REF_RE.match(range_str)
  131          if match is None:  # Must be a named range

dist-packages\venv\Lib\site-packages\openpyxl\utils\cell.py:
   44      """Convert a coordinate string like 'B12' to a tuple ('B', 12)"""
   45:     match = COORD_RE.match(coord_string.upper())
   46      if not match:

   58      """Convert a coordinate to an absolute coordinate string (B12 -> $B$12)"""
   59:     m = ABSOLUTE_RE.match(coord_string.upper())
   60      if not m:

  132      """
  133:     m = ABSOLUTE_RE.match(range_string)
  134      if not m:

  193      """
  194:     m = SHEETRANGE_RE.match(range_string)
  195      if m is None:

dist-packages\venv\Lib\site-packages\openpyxl\workbook\defined_name.py:
  139                  if part.subtype == "RANGE":
  140:                     m = SHEETRANGE_RE.match(part.value)
  141                      sheetname = m.group('notquoted') or m.group('quoted')

dist-packages\venv\Lib\site-packages\openpyxl\worksheet\worksheet.py:
  905          if rows is not None:
  906:             if not ROW_RANGE_RE.match(rows):
  907                  raise ValueError("Print title rows must be the form 1:3")

  924          if cols is not None:
  925:             if not COL_RANGE_RE.match(cols):
  926                  raise ValueError("Print title cols must be the form C:D")

dist-packages\venv\Lib\site-packages\packaging\tags.py:
  602      # uses version strings like "2.20-2014.11"). See gh-3588.
  603:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  604      if not m:

dist-packages\venv\Lib\site-packages\packaging\utils.py:
  104      # See PEP 427 for the rules on escaping the project name
  105:     if "__" in name_part or re.match(r"^[\w\d._]*$", name_part, re.UNICODE) is None:
  106          raise InvalidWheelFilename("Invalid project name: {0}".format(filename))

dist-packages\venv\Lib\site-packages\paramiko\config.py:
  139              # Parse line into key, value
  140:             match = re.match(self.SETTINGS_REGEX, line)
  141              if not match:

dist-packages\venv\Lib\site-packages\pbr\packaging.py:
  118          # Ignore index URL lines
  119:         if re.match(r'^\s*(-i|--index-url|--extra-index-url).*', line):
  120              continue

  139          # -e git://github.com/openstack/nova/master#egg=nova-1.2.3
  140:         if re.match(r'\s*-e\s+', line):
  141              line = re.sub(r'\s*-e\s+.*#egg=(.*)$', egg_fragment, line)

  144          # http://github.com/openstack/nova/zipball/master#egg=nova-1.2.3
  145:         elif re.match(r'\s*(https?|git(\+(https|ssh))?):', line):
  146              line = re.sub(r'\s*(https?|git(\+(https|ssh))?):.*#egg=(.*)$',

  148          # -f lines are for index locations, and don't get used here
  149:         elif re.match(r'\s*-f\s+', line):
  150              line = None

  175          # skip comments and blank lines
  176:         if re.match(r'(\s*#)|(\s*$)', line):
  177              continue
  178          # lines with -e or -f need the whole line, minus the flag
  179:         if re.match(r'\s*-[ef]\s+', line):
  180              dependency_links.append(re.sub(r'\s*-[ef]\s+', '', line))
  181          # lines that are only urls can go in unmolested
  182:         elif re.match(r'\s*(https?|git(\+(https|ssh))?):', line):
  183              dependency_links.append(line)

dist-packages\venv\Lib\site-packages\pbr\util.py:
  358                  for requirement in in_cfg_value:
  359:                     m = re.match(requirement_pattern, requirement)
  360                      requirement_package = m.group('package').strip()

  429              for requirement in requirements:
  430:                 m = re.match(requirement_pattern, requirement)
  431                  extras_value = m.group('package').strip()

dist-packages\venv\Lib\site-packages\pbr\tests\test_packaging.py:
  114          for line in gnupg_version[0].split('\n'):
  115:             gnupg_version = gnupg_version_re.match(line)
  116              if gnupg_version:

dist-packages\venv\Lib\site-packages\pexpect\pxssh.py:
  373              for line in lines:
  374:                 if not config_has_server and re.match(server_regex, line, re.IGNORECASE):
  375                      config_has_server = True

  380                      break  # we have left the relevant section
  381:                 elif config_has_server and re.match(user_regex, line, re.IGNORECASE):
  382                      server_has_username = True

dist-packages\venv\Lib\site-packages\pip\_internal\index\package_finder.py:
  533              if wheel.build_tag is not None:
  534:                 match = re.match(r'^(\d+)(.*)$', wheel.build_tag)
  535                  build_tag_groups = match.groups()

dist-packages\venv\Lib\site-packages\pip\_internal\metadata\base.py:
  98              # valid project name pattern is taken from PEP 508.
  99:             project_name_valid = re.match(
  100                  r"^([A-Z0-9]|[A-Z0-9][A-Z0-9._-]*[A-Z0-9])$",

dist-packages\venv\Lib\site-packages\pip\_internal\models\direct_url.py:
  179              return netloc
  180:         if ENV_VAR_RE.match(user_pass):
  181              return netloc

dist-packages\venv\Lib\site-packages\pip\_internal\models\wheel.py:
  26          """
  27:         wheel_info = self.wheel_file_re.match(filename)
  28          if not wheel_info:

dist-packages\venv\Lib\site-packages\pip\_internal\operations\install\wheel.py:
  356          # Delete any other versioned pip entry points
  357:         pip_ep = [k for k in console if re.match(r'pip(\d(\.\d)?)?$', k)]
  358          for k in pip_ep:

  373          easy_install_ep = [
  374:             k for k in console if re.match(r'easy_install(-\d\.\d)?$', k)
  375          ]

dist-packages\venv\Lib\site-packages\pip\_internal\req\constructors.py:
  43      # type: (str) -> Tuple[str, Optional[str]]
  44:     m = re.match(r'^(.+)(\[[^\]]+\])$', path)
  45      extras = None

dist-packages\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  459      for line_number, line in lines_enum:
  460:         if not line.endswith('\\') or COMMENT_RE.match(line):
  461:             if COMMENT_RE.match(line):
  462                  # this ensures comments are always matched later

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\scripts.py:
  332  
  333:             match = FIRST_LINE_RE.match(first_line.replace(b'\r\n', b'\n'))
  334              if match:

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\util.py:
  852      if project_name and len(filename) > len(project_name) + 1:
  853:         m = re.match(re.escape(project_name) + r'\b', filename)
  854          if m:

  875      """
  876:     m = NAME_VERSION_RE.match(p)
  877      if not m:

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\version.py:
  185      s = s.strip()
  186:     m = PEP440_VERSION_RE.match(s)
  187      if not m:

  271          # (~= 1.4.5.0) matches differently to (~= 1.4.5.0.0).
  272:         m = PEP440_VERSION_RE.match(s)      # must succeed
  273          groups = m.groups()

  629              return False
  630:         m = self.numeric_re.match(str(constraint))
  631          if not m:

  649  def is_semver(s):
  650:     return _SEMVER_RE.match(s)
  651  

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\wheel.py:
  160          else:
  161:             m = NAME_VERSION_RE.match(filename)
  162              if m:

  170                  dirname, filename = os.path.split(filename)
  171:                 m = FILENAME_RE.match(filename)
  172                  if not m:

  263      def process_shebang(self, data):
  264:         m = SHEBANG_RE.match(data)
  265          if m:

  272                  shebang_python = SHEBANG_PYTHON
  273:             m = SHEBANG_DETAIL_RE.match(shebang)
  274              if m:

  961      if sys.platform == 'darwin':
  962:         m = re.match(r'(\w+)_(\d+)_(\d+)_(\w+)$', ARCH)
  963          if m:

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  670          rel_re = re.compile(r'[\d.]+')
  671:         m = rel_re.match(release)
  672          if m:

dist-packages\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  893          # gauntlet
  894:         if not re.match(r"""^([:,;#%.\sa-zA-Z0-9!]|\w-\w|'[\s\w]+'|"[\s\w]+"|\([\d,\s]+\))*$""", style):
  895              return ''
  896:         if not re.match(r"^\s*([-\w]+\s*:[^:;]*(;\s*|$))*$", style):
  897              return ''

  908                      if keyword not in self.allowed_css_keywords and \
  909:                             not re.match(r"^(#[0-9a-fA-F]+|rgb\(\d+%?,\d*%?,?\d*%?\)?|\d{0,2}\.?\d{0,2}(cm|em|ex|in|mm|pc|pt|px|%|,|\))?)$", keyword):  # noqa
  910                          break

dist-packages\venv\Lib\site-packages\pip\_vendor\packaging\tags.py:
  602      # uses version strings like "2.20-2014.11"). See gh-3588.
  603:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  604      if not m:

dist-packages\venv\Lib\site-packages\pip\_vendor\packaging\utils.py:
  104      # See PEP 427 for the rules on escaping the project name
  105:     if "__" in name_part or re.match(r"^[\w\d._]*$", name_part, re.UNICODE) is None:
  106          raise InvalidWheelFilename("Invalid project name: {0}".format(filename))

dist-packages\venv\Lib\site-packages\pip\_vendor\pep517\in_process\_in_process.py:
  142      for path in whl_zip.namelist():
  143:         m = re.match(r'[^/\\]+-[^/\\]+\.dist-info/', path)
  144          if m:

dist-packages\venv\Lib\site-packages\pip\_vendor\requests\utils.py:
  82              test = test.replace("?", r".")      # change glob char
  83:             if re.match(test, host, re.I):
  84                  return True

dist-packages\venv\Lib\site-packages\pip\_vendor\toml\decoder.py:
  453                  else:
  454:                     if not _groupname_re.match(groups[i]):
  455                          raise TomlDecodeError("Invalid group name '" +

  730                  break
  731:             if TIME_RE.match(pair[-1]):
  732                  break

  884              return (inline_object, "inline_object")
  885:         elif TIME_RE.match(v):
  886:             h, m, s, _, ms = TIME_RE.match(v).groups()
  887              time = datetime.time(int(h), int(m), int(s), int(ms) if ms else 0)

dist-packages\venv\Lib\site-packages\pip\_vendor\toml\encoder.py:
  190              qsection = section
  191:             if not re.match(r'^[A-Za-z0-9_-]+$', section):
  192                  qsection = _dump_str(section)

dist-packages\venv\Lib\site-packages\pip\_vendor\urllib3\util\retry.py:
  354          # Whitespace: https://tools.ietf.org/html/rfc7230#section-3.2.4
  355:         if re.match(r"^\s*[0-9]+\s*$", retry_after):
  356              seconds = int(retry_after)

dist-packages\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssl_.py:
  445          hostname = hostname.decode("ascii")
  446:     return bool(IPV4_RE.match(hostname) or BRACELESS_IPV6_ADDRZ_RE.match(hostname))
  447  

dist-packages\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:
  279          if scheme in NORMALIZABLE_SCHEMES:
  280:             is_ipv6 = IPV6_ADDRZ_RE.match(host)
  281              if is_ipv6:

  294                      return host.lower()
  295:             elif not IPV4_RE.match(host):
  296                  return six.ensure_str(

  321      """Percent-encodes a request target so that there are no invalid characters"""
  322:     path, query = TARGET_RE.match(target).groups()
  323      target = _encode_invalid_chars(path, PATH_CHARS)

  360      try:
  361:         scheme, authority, path, query, fragment = URI_RE.match(url).groups()
  362          normalize_uri = scheme is None or scheme.lower() in NORMALIZABLE_SCHEMES

  367          if authority:
  368:             auth, host, port = SUBAUTHORITY_RE.match(authority).groups()
  369              if auth and normalize_uri:

dist-packages\venv\Lib\site-packages\pkg_resources\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

dist-packages\venv\Lib\site-packages\pkg_resources\_vendor\packaging\tags.py:
  504      # uses version strings like "2.20-2014.11"). See gh-3588.
  505:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  506      if not m:

dist-packages\venv\Lib\site-packages\ply\lex.py:
  319              for lexre, lexindexfunc in self.lexre:
  320:                 m = lexre.match(lexdata, lexpos)
  321                  if not m:

  842          for line in lines:
  843:             m = fre.match(line)
  844              if not m:
  845:                 m = sre.match(line)
  846              if m:

dist-packages\venv\Lib\site-packages\ply\yacc.py:
  3011                  linen += 1
  3012:                 m = fre.match(line)
  3013                  if m:

dist-packages\venv\Lib\site-packages\py\_path\svnwc.py:
  1176      # example: 2003-10-27 20:43:14 +0100 (Mon, 27 Oct 2003)
  1177:     m = re.match(r'(\d+-\d+-\d+ \d+:\d+:\d+) ([+-]\d+) .*', timestr)
  1178      if not m:

dist-packages\venv\Lib\site-packages\pycparser\ply\lex.py:
  319              for lexre, lexindexfunc in self.lexre:
  320:                 m = lexre.match(lexdata, lexpos)
  321                  if not m:

  843          for line in lines:
  844:             m = fre.match(line)
  845              if not m:
  846:                 m = sre.match(line)
  847              if m:

dist-packages\venv\Lib\site-packages\pycparser\ply\yacc.py:
  3009                  linen += 1
  3010:                 m = fre.match(line)
  3011                  if m:

dist-packages\venv\Lib\site-packages\pyeapi\client.py:
  519          self._version = str(output[0]['result']['version'])
  520:         match = re.match('[\d.\d]+', output[0]['result']['version'])
  521          if match:

dist-packages\venv\Lib\site-packages\pyeapi\api\acl.py:
  172          for item in re.finditer(r'\d+ [p|d].*$', config, re.M):
  173:             match = self.entry_re.match(item.group(0))
  174              (seq, act, anyip, host, ip, mlen, mask, log) = match.groups()

  244          for item in re.finditer(r'\d+ [p|d].*$', config, re.M):
  245:             match = self.entry_re.match(item.group(0))
  246              entry = dict()

dist-packages\venv\Lib\site-packages\pyeapi\api\interfaces.py:
  81  def isvalidinterface(value):
  82:     match = re.match(r'([EPVLM][a-z-C]+)', value)
  83      return match and match.group() in VALID_INTERFACES

dist-packages\venv\Lib\site-packages\pyeapi\api\ntp.py:
  154          """
  155:         if not name or re.match(r'^[\s]+$', name):
  156              raise ValueError('ntp server name must be specified')

dist-packages\venv\Lib\site-packages\pyeapi\api\varp.py:
  127                  # Check to see if mac_address matches expected format
  128:                 if not re.match(r'(?:[a-f0-9]{2}:){5}[a-f0-9]{2}',
  129                                  mac_address):

dist-packages\venv\Lib\site-packages\pyeapi\api\vrrp.py:
   491              cmd = "no vrrp %d ip %s" % (vrid, primary_ip)
   492:         elif re.match(r'^\d+\.\d+\.\d+\.\d+$', str(value)):
   493              cmd = "vrrp %d ip %s" % (vrid, value)

   664              if type(sec_ip) is not str or \
   665:                     not re.match(r'^\d+\.\d+\.\d+\.\d+$', sec_ip):
   666                  raise ValueError("vrrp property 'secondary_ip' must be a list "

  1063          for track in remove:
  1064:             match = re.match(r'(\S+)\s+(\S+)\s+(\S+)', track)
  1065              if match:

  1075          for track in add:
  1076:             match = re.match(r'(\S+)\s+(\S+)\s+(\S+)', track)
  1077              if match:

  1121          if not default and not disable:
  1122:             if not re.match(r'^\d+\.\d+\.\d+\.\d+$', str(value)):
  1123                  raise ValueError("vrrp property 'bfd_ip' must be "

dist-packages\venv\Lib\site-packages\pylint\gui.py:
  69          """write text to the stream"""
  70:         if re.match('^--+$', text.strip()) or re.match('^==+$', text.strip()):
  71              if self.currout:

dist-packages\venv\Lib\site-packages\pylint\checkers\python3.py:
  32          return False
  33:     if re.match('0\d+', literal):
  34          try:

dist-packages\venv\Lib\site-packages\pylint\checkers\typecheck.py:
  336              # attribute is marked as generated, stop here
  337:             if re.match(pattern, node.attrname):
  338                  return

dist-packages\venv\Lib\site-packages\pylint\test\input\func_w0405.py:
  11  __revision__ = 0
  12: _re.match('yo', '.*')
  13  

dist-packages\venv\Lib\site-packages\pyral\context.py:
  933      if ping_timeout:
  934:          result = re.match(r'^(?P<digits>\d+)$', ping_timeout)
  935           ping_timeout = result.groupdict('digits') if result else DEFAULT_PING_TIMEOUT

dist-packages\venv\Lib\site-packages\pyral\entity.py:
  858          std_av_ref_pattern = '^https?://.*/\w+/-?\d+/AllowedValues$'
  859:         mo = re.match(std_av_ref_pattern, self.AllowedValues)
  860          if not mo:

dist-packages\venv\Lib\site-packages\pyral\query_builder.py:
  252              else:
  253:                 if re.match(r'^(AND|OR)$', part, re.I):
  254                      valid_parts.append(part)

dist-packages\venv\Lib\site-packages\pyral\rallyresp.py:
  85          self.target = request_path_elements[-1]
  86:         if re.match('^\d+$', self.target):
  87              self.target = request_path_elements[-2] # this happens on request for RevisionHistory

dist-packages\venv\Lib\site-packages\pyral\restapi.py:
   801                  if (type(value) == str or type(value) == bytes) and '/' in value \
   802:                 and re.match('^\d+$', value.split('/')[-1]):
   803                      obj_list.append({"_ref" : value})  # transform to a dict instance

  1114          objectID = itemIdent  # at first assume itemIdent is the ObjectID
  1115:         if re.match('^[A-Z]{1,2}\d+$', str(itemIdent)):
  1116              fmtIdQuery = 'FormattedID = "%s"' % itemIdent

dist-packages\venv\Lib\site-packages\pysphere\ZSI\digest_auth.py:
  76      """
  77:     m = fetch_challenge.wwwauth_header_re.match(http_header)
  78      if m is None:

dist-packages\venv\Lib\site-packages\pythonwin\pywin\idle\FormatParagraph.py:
  146  def is_all_white(line):
  147:     return re.match(r"^\s*$", line) is not None
  148  
  149  def get_indent(line):
  150:     return re.match(r"^(\s*)", line).group()
  151  
  152  def get_comment_header(line):
  153:     m = re.match(r"^(\s*#*)", line)
  154      if m is None: return ""

dist-packages\venv\Lib\site-packages\pythonwin\pywin\idle\PyParse.py:
  527              i = i+1     # move beyond the =
  528:             found = re.match(r"\s*\\", str[i:endpos]) is None
  529  

dist-packages\venv\Lib\site-packages\pyVim\connect.py:
  244     try:
  245:       info = re.match(_rx, host)
  246        if info is not None:

dist-packages\venv\Lib\site-packages\requests\utils.py:
  79              test = test.replace("?", r".")      # change glob char
  80:             if re.match(test, host, re.I):
  81                  return True

dist-packages\venv\Lib\site-packages\rflint\parser\common.py:
  107          if ((len(self) > 1) and
  108:             (re.match(r'\[.*?\]', self[1]))):
  109              return True

dist-packages\venv\Lib\site-packages\rflint\parser\util.py:
  22          if flags is None:
  23:             self.result = re.match(pattern, string, flags=self.flags)
  24          else:
  25:             self.result = re.match(pattern, string)
  26          return self.result

dist-packages\venv\Lib\site-packages\rflint\rules\suiteRules.py:
  26          for table in suite.tables:
  27:             if (not re.match(r'^(settings?|metadata|(test )?cases?|(user )?keywords?|variables?)$', 
  28                               table.name, re.IGNORECASE)):

dist-packages\venv\Lib\site-packages\robot\utils\argumentparser.py:
  285          for line in usage.splitlines():
  286:             res = self._opt_line_re.match(line)
  287              if res:

dist-packages\venv\Lib\site-packages\robot\utils\error.py:
  179              return True
  180:         res = self._java_trace_re.match(line)
  181          if res is None:

  195          while lines:
  196:             if self._java_trace_re.match(lines[-1]):
  197                  lines.pop()

dist-packages\venv\Lib\site-packages\robot\utils\robottime.py:
  56  def _timer_to_secs(number):
  57:     match = _timer_re.match(number)
  58      if not match:

dist-packages\venv\Lib\site-packages\robot\utils\text.py:
  146      lines = doc.splitlines()
  147:     match = _TAGS_RE.match(lines[-1])
  148      if match:

dist-packages\venv\Lib\site-packages\selenium\webdriver\support\color.py:
  51              def match(self, pattern, str_):
  52:                 self.match_obj = re.match(pattern, str_)
  53                  return self.match_obj

dist-packages\venv\Lib\site-packages\SeleniumLibrary\locators\elementfinder.py:
  302      def _parse_locator(self, locator):
  303:         if re.match(r"\(*//", locator):
  304              return "xpath", locator

dist-packages\venv\Lib\site-packages\setuptools\dist.py:
  336      for pkgname in value:
  337:         if not re.match(r'\w+(\.\w+)*', pkgname):
  338              distutils.log.warn(

dist-packages\venv\Lib\site-packages\setuptools\package_index.py:
  173      parts = basename.split('-')
  174:     if not py_version and any(re.match(r'py\d\.\d$', p) for p in parts[2:]):
  175          # it is a bdist_dumb, not an sdist -- bail out

dist-packages\venv\Lib\site-packages\setuptools\sandbox.py:
  446          pattern_matches = (
  447:             re.match(pattern, filepath)
  448              for pattern in self._exception_patterns

dist-packages\venv\Lib\site-packages\setuptools\_distutils\ccompiler.py:
  951      for pattern, compiler in _default_compilers:
  952:         if re.match(pattern, platform) is not None or \
  953:            re.match(pattern, osname) is not None:
  954              return compiler

dist-packages\venv\Lib\site-packages\setuptools\_distutils\dist.py:
  531          command = args[0]
  532:         if not command_re.match(command):
  533              raise SystemExit("invalid command name '%s'" % command)

dist-packages\venv\Lib\site-packages\setuptools\_distutils\fancy_getopt.py:
  199              # '='.
  200:             if not longopt_re.match(long):
  201                  raise DistutilsGetoptError(

dist-packages\venv\Lib\site-packages\setuptools\_distutils\util.py:
   88          rel_re = re.compile (r'[\d.]+', re.ASCII)
   89:         m = rel_re.match(release)
   90          if m:

  249      while s:
  250:         m = _wordchars_re.match(s, pos)
  251          end = m.end()

  267              if s[end] == "'":           # slurp singly-quoted string
  268:                 m = _squote_re.match(s, end)
  269              elif s[end] == '"':         # slurp doubly-quoted string
  270:                 m = _dquote_re.match(s, end)
  271              else:

dist-packages\venv\Lib\site-packages\setuptools\_distutils\version.py:
  134      def parse (self, vstring):
  135:         match = self.version_re.match(vstring)
  136          if not match:

dist-packages\venv\Lib\site-packages\setuptools\_distutils\command\build_ext.py:
  373              if not (isinstance(ext_name, str) and
  374:                     extension_name_re.match(ext_name)):
  375                  raise DistutilsSetupError(

dist-packages\venv\Lib\site-packages\setuptools\_distutils\command\build_scripts.py:
  88  
  89:                 match = first_line_re.match(first_line)
  90                  if match:

dist-packages\venv\Lib\site-packages\setuptools\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

dist-packages\venv\Lib\site-packages\setuptools\_vendor\packaging\tags.py:
  504      # uses version strings like "2.20-2014.11"). See gh-3588.
  505:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  506      if not m:

dist-packages\venv\Lib\site-packages\setuptools\command\bdist_egg.py:
  247                      pattern = r'(?P<name>.+)\.(?P<magic>[^.]+)\.pyc'
  248:                     m = re.match(pattern, name)
  249                      path_new = os.path.join(

dist-packages\venv\Lib\site-packages\setuptools\command\egg_info.py:
  573          """
  574:         return re.match(r"standard file .*not found", msg)
  575  

  719              for line in f:
  720:                 match = re.match(r"Version:.*-r(\d+)\s*$", line)
  721                  if match:

dist-packages\venv\Lib\site-packages\test\test_HPE3ParClient_FilePersona.py:
  645          uid_match = '^[0-f]*$'
  646:         self.assertIsNotNone(re.match(uid_match, member['policyID']))
  647          ip_addr_ish = r'[0-9.]*$'
  648:         self.assertIsNotNone(re.match(ip_addr_ish, member['address']),
  649                               '%s does not look like an IP Addr.' %
  650                               member['address'])
  651:         self.assertIsNotNone(re.match(ip_addr_ish, member['prefixLen']),
  652                               '%s does not look like an IP Addr.' %

  680              uid_match = '^[\-0-f]*$'
  681:             self.assertIsNotNone(re.match(uid_match, member['uuid']))
  682              self.assertIsInstance(member['vfsName'], str)

  693          uid_match = '^[\-0-f]*$'
  694:         self.assertIsNotNone(re.match(uid_match, member['uuid']))
  695          self.assertEqual(vfsname, member['vfsName'])

  826              uid_match = '^[0-f]*$'
  827:             self.assertIsNotNone(re.match(uid_match, member['taskId']))
  828              self.assertIn(member['taskState'],

dist-packages\venv\Lib\site-packages\toml\decoder.py:
  453                  else:
  454:                     if not _groupname_re.match(groups[i]):
  455                          raise TomlDecodeError("Invalid group name '" +

  730                  break
  731:             if TIME_RE.match(pair[-1]):
  732                  break

  884              return (inline_object, "inline_object")
  885:         elif TIME_RE.match(v):
  886:             h, m, s, _, ms = TIME_RE.match(v).groups()
  887              time = datetime.time(int(h), int(m), int(s), int(ms) if ms else 0)

dist-packages\venv\Lib\site-packages\toml\encoder.py:
  190              qsection = section
  191:             if not re.match(r'^[A-Za-z0-9_-]+$', section):
  192                  qsection = _dump_str(section)

dist-packages\venv\Lib\site-packages\urllib3\util\retry.py:
  228          # Whitespace: https://tools.ietf.org/html/rfc7230#section-3.2.4
  229:         if re.match(r"^\s*[0-9]+\s*$", retry_after):
  230              seconds = int(retry_after)

dist-packages\venv\Lib\site-packages\validictory\validator.py:
  223              if patterns:
  224:                 delta = [f for f in delta if not any(re.match(p, f) for p in patterns)]
  225  

  353              for key, value in value_obj.items():
  354:                 if re.match(pattern, key):
  355                      self.__validate("_data", {"_data": value}, schema, path)

  398                  if (eachProperty not in properties and not
  399:                         any(re.match(p, eachProperty) for p in patterns)):
  400                      # If additionalProperties is the boolean value False

  530          if (isinstance(value, _str_type) and
  531:             (isinstance(pattern, _str_type) and not re.match(pattern, value)
  532               or not isinstance(pattern, _str_type) and not pattern.match(value))):

dist-packages\venv\Lib\site-packages\werkzeug\http.py:
  428          while rest:
  429:             optmatch = _option_header_piece_re.match(rest)
  430              if not optmatch:

  896      while pos < end:
  897:         match = _etag_re.match(value, pos)
  898          if match is None:

dist-packages\venv\Lib\site-packages\werkzeug\urls.py:
  478      i = url.find(s(":"))
  479:     if i > 0 and _scheme_re.match(_to_str(url[:i], errors="replace")):
  480          # make sure "iri" is not actually a port number (in which case

dist-packages\venv\Lib\site-packages\win32com\test\testall.py:
  38          last_line_pos = data.rfind("\n")
  39:         if not re.match("\[\d+ refs\]", data[last_line_pos+1:]):
  40              break

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\cli\traffic\ping.py:
   17  
   18:         p = re.match(r'^(?:le:([\w\W]+?)/)?encl:(\d+)/bay:(\d+)/port:([\w\W]+)$', source, re.I)
   19          if not p:

   36  
   37:         p = re.match(r'^(?:le:([\w\W]+?)/)?encl:(\d+)/bay:(\d+)/port:([\w\W]+)$', source, re.I)
   38          if not p:

  232  
  233:                     if re.match(r'^\d+\.\d+', target):
  234                          if self.traffic.data['platform'].lower() in ('windows'):

  241                      else:
  242:                         p = re.match(r'^(?:le:([\w\W]+?)/)?encl:(\d+)/bay:(\d+)/port:([\w\W]+)$', target, re.I)
  243                          if p:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\keywords\fusion_api.py:
  492                                  for namekey in expected[key][0].keys():
  493:                                     if (re.match(r'.*name', namekey, re.I)) and (expected[key][0][namekey] is not None):
  494                                          randomkey = namekey

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\keywords\tru.py:
  230              logger.info(stdout)
  231:         if re.match('(?i)warn', stdout):
  232              logger.warn("TRU encountered warnings.  Please see results for more information.")
  233:         if re.match('(?i)error', stdout):
  234              logger.warn("TRU encountered errors.  Please see results for more information.")

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\libs\cli\cli_base.py:
  187              stat = self.sftp.stat(remote_file_path)
  188:             if re.match('^dr.*', str(stat)):
  189                  self.download_folder_to_local(local_file_path, remote_file_path)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\business_logic\networking\logicalinterconnects.py:
  81              ic_model = ui_lib.get_text(UpdateLogicalInterconnectFirmwareElements.ID_SWITCH_FW_DETAILS % index + '/td[2]')
  82:             m = re.match(".*/.*/", installed_fw)
  83              if m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\business_logic\storage\volumes.py:
  297              for snapshot in snapshots:
  298:                 if re.match(r'^%s$' % rexg, snapshot):
  299                      return True

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\general\activity.py:
   47          actname.name = actname.name.strip()
   48:         if re.match('^#\d+$', actname.name):
   49              line_no = actname.name.replace('#', '')

  130          actname.name = actname.name.strip()
  131:         if re.match('^#\d+$', actname.name):
  132              line_no = actname.name.replace('#', '')

  207          actname.name = actname.name.strip()
  208:         if re.match('^#\d+$', actname.name):
  209              line_no = actname.name.replace('#', '')

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\networking\interconnects.py:
  1374                      match_string = ".*" + portdetail + " is (.*)"
  1375:                     m = re.match(match_string, dataarray[0])
  1376                      if m:

  1383                          for line in dataarray[19:]:
  1384:                             m = re.match("(.*)input packets", line)
  1385                              if m:

  1388  
  1389:                             m = re.match("(.*)output packets", line)
  1390                              if m:

  1393  
  1394:                             m = re.match("(.*)input error", line)
  1395                              if m:

  1397  
  1398:                             m = re.match("(.*)output error", line)
  1399                              if m:

  1568                  match_text = r".*No " + key.lower()
  1569:                 m = re.match(match_text, rowdata[1])
  1570                  if m:

  1641              if datadict['Connected To'] != "":
  1642:                 m = re.match(".* \((.*)\)", datadict['Connected To'])
  1643                  portdetail = m.group(1)

  1769          match_string = ".*" + portdetail + " is (.*)"
  1770:         m = re.match(match_string, dataarray[0])
  1771          if m:

  1775                  switchdict["State"] = "unlinked"
  1776:         m = re.match(".* (.*?), address: (.*?) ", dataarray[2])
  1777          if m:

  1787          for line in dataarray[3:]:
  1788:             m = re.match(".*Port mode is (.*)", line)
  1789              if m:

  1794                      switchdict["System Capabilities"] = "bridge,router"
  1795:             m = re.match(".* (.*) Gb/s, media type", line)
  1796              if m:

  1798                  switchdict["Speed"] = (m.group(1)).strip()
  1799:             m = re.match("(.*)input packets", line)
  1800              if m:

  1802                  switchdict["input packets"] = (m.group(1)).strip()
  1803:             m = re.match("(.*)output packets", line)
  1804              if m:

  1806                  switchdict["output packets"] = (m.group(1)).strip()
  1807:             m = re.match("(.*)input error", line)
  1808              if m:

  1812                  print m.group(1)
  1813:             m = re.match("(.*)output error", line)
  1814              if m:

  2955      client.close()
  2956:     m = re.match("\"FirmwareVersion\": \"(.*)\",", data)
  2957      if m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\networking\logicalinterconnects.py:
  871                  (ic, installed_fw, baseline_fw) = TBirdLogicalInterconnectsUpdateFirmware.get_firmware_details(index)
  872:                 m = re.match(".*/.*/", installed_fw)
  873                  if m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\networking\switches.py:
  73                      for net in network_list:
  74:                         if re.match("^[a-zA-Z]+.*", net):
  75                              vlan_list.append(net)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\common\CpqlocfgHelper.py:
  157          if check_rocommunity:
  158:             if re.match('REGEXP', rocommunity):
  159                  (str, regexp) = rocommunity.split(':')
  160:                 if item[0] == address and re.match(regexp, item[1]):
  161                      logger._debug("address %s rocommunity %s" % (item[0], item[1]))

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\servers\SHTByMezz.py:
  30          for slot, model in mezz.items():
  31:             if re.match('(Flb|Lom)', slot, re.I):
  32                  logger._log_to_console_and_log_file("\t%s expects a %s" % (slot, model))

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\workflows\ServerProfilePayload.py:
  111          if net_type in ["FibreChannel"]:
  112:             req_port = [port for port in req_port for card in cards if re.match(card + ",*", port)]
  113          if not req_port:

  252              for info in connection_list:
  253:                 con_dat = re.match("^(.*)\:\((.*)\)", info)
  254                  if not con_dat or len(con_dat.groups()) != 2:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\ACI_Istanbul\APICOperations.py:
  149          for tenant in tenants:
  150:             if re.match("FVT_TenantScale_Test\d+", str(tenant)):
  151                  tenant.mark_as_deleted()

  173          for domain in VmmDomains:
  174:             if re.match(domainname, str(domain)):
  175                  domain.mark_as_deleted()

  539                  for epg in epgs:
  540:                     if re.match("FVT_EPGScaling_Test00\d+", str(epg)):
  541                          epg.mark_as_deleted()

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\ACI_Istanbul\epg_deletion.py:
  23              for epg in epgs:
  24:                 if re.match("EPG\d+", str(epg)):
  25                      epg.mark_as_deleted()

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\DFRM\DCS\UserInputs\functions.py:
  120          logger.console("Initialized the version list")
  121:     if re.match("Smart Component for HPE Synergy 12Gb SAS Connection Module Firmware|Smart Component for HPE Synergy  D3940 Storage Module firmware", dict['name']):
  122          logger.console(dict['name'])

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Tools\Build_Data_From_OV_Resource\Build_Expected_from_Response.py:
  122              for rkey in Build_data.range_items.keys():
  123:                 if re.match(rkey, key) and expected[key] != None:
  124                      if expected[key] in Build_data.cant_range:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\_distutils_hack\__init__.py:
  30      warnings.warn("Setuptools is replacing distutils.")
  31:     mods = [name for name in sys.modules if re.match(r'distutils\b', name)]
  32      for name in mods:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\index\package_finder.py:
  535              if wheel.build_tag is not None:
  536:                 match = re.match(r'^(\d+)(.*)$', wheel.build_tag)
  537                  build_tag_groups = match.groups()

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\models\direct_url.py:
  191              return netloc
  192:         if ENV_VAR_RE.match(user_pass):
  193              return netloc

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\models\wheel.py:
  29          """
  30:         wheel_info = self.wheel_file_re.match(filename)
  31          if not wheel_info:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\operations\install\wheel.py:
  387          # Delete any other versioned pip entry points
  388:         pip_ep = [k for k in console if re.match(r'pip(\d(\.\d)?)?$', k)]
  389          for k in pip_ep:

  404          easy_install_ep = [
  405:             k for k in console if re.match(r'easy_install(-\d\.\d)?$', k)
  406          ]

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\req\constructors.py:
  59      # type: (str) -> Tuple[str, Optional[str]]
  60:     m = re.match(r'^(.+)(\[[^\]]+\])$', path)
  61      extras = None

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  482      for line_number, line in lines_enum:
  483:         if not line.endswith('\\') or COMMENT_RE.match(line):
  484:             if COMMENT_RE.match(line):
  485                  # this ensures comments are always matched later

  573          path = path.replace('\\', '/')
  574:         match = _url_slash_drive_re.match(path)
  575          if match:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\scripts.py:
  332  
  333:             match = FIRST_LINE_RE.match(first_line.replace(b'\r\n', b'\n'))
  334              if match:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\util.py:
  852      if project_name and len(filename) > len(project_name) + 1:
  853:         m = re.match(re.escape(project_name) + r'\b', filename)
  854          if m:

  875      """
  876:     m = NAME_VERSION_RE.match(p)
  877      if not m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\version.py:
  185      s = s.strip()
  186:     m = PEP440_VERSION_RE.match(s)
  187      if not m:

  271          # (~= 1.4.5.0) matches differently to (~= 1.4.5.0.0).
  272:         m = PEP440_VERSION_RE.match(s)      # must succeed
  273          groups = m.groups()

  629              return False
  630:         m = self.numeric_re.match(str(constraint))
  631          if not m:

  649  def is_semver(s):
  650:     return _SEMVER_RE.match(s)
  651  

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\wheel.py:
  160          else:
  161:             m = NAME_VERSION_RE.match(filename)
  162              if m:

  170                  dirname, filename = os.path.split(filename)
  171:                 m = FILENAME_RE.match(filename)
  172                  if not m:

  263      def process_shebang(self, data):
  264:         m = SHEBANG_RE.match(data)
  265          if m:

  272                  shebang_python = SHEBANG_PYTHON
  273:             m = SHEBANG_DETAIL_RE.match(shebang)
  274              if m:

  961      if sys.platform == 'darwin':
  962:         m = re.match(r'(\w+)_(\d+)_(\d+)_(\w+)$', ARCH)
  963          if m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  670          rel_re = re.compile(r'[\d.]+')
  671:         m = rel_re.match(release)
  672          if m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  893          # gauntlet
  894:         if not re.match(r"""^([:,;#%.\sa-zA-Z0-9!]|\w-\w|'[\s\w]+'|"[\s\w]+"|\([\d,\s]+\))*$""", style):
  895              return ''
  896:         if not re.match(r"^\s*([-\w]+\s*:[^:;]*(;\s*|$))*$", style):
  897              return ''

  908                      if keyword not in self.allowed_css_keywords and \
  909:                             not re.match(r"^(#[0-9a-fA-F]+|rgb\(\d+%?,\d*%?,?\d*%?\)?|\d{0,2}\.?\d{0,2}(cm|em|ex|in|mm|pc|pt|px|%|,|\))?)$", keyword):  # noqa
  910                          break

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\packaging\tags.py:
  504      # uses version strings like "2.20-2014.11"). See gh-3588.
  505:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  506      if not m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\pep517\_in_process.py:
  142      for path in whl_zip.namelist():
  143:         m = re.match(r'[^/\\]+-[^/\\]+\.dist-info/', path)
  144          if m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\requests\utils.py:
  82              test = test.replace("?", r".")      # change glob char
  83:             if re.match(test, host, re.I):
  84                  return True

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\toml\decoder.py:
  452                  else:
  453:                     if not _groupname_re.match(groups[i]):
  454                          raise TomlDecodeError("Invalid group name '" +

  729                  break
  730:             if TIME_RE.match(pair[-1]):
  731                  break

  879              return (inline_object, "inline_object")
  880:         elif TIME_RE.match(v):
  881:             h, m, s, _, ms = TIME_RE.match(v).groups()
  882              time = datetime.time(int(h), int(m), int(s), int(ms) if ms else 0)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\toml\encoder.py:
  190              qsection = section
  191:             if not re.match(r'^[A-Za-z0-9_-]+$', section):
  192                  qsection = _dump_str(section)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\urllib3\util\retry.py:
  251          # Whitespace: https://tools.ietf.org/html/rfc7230#section-3.2.4
  252:         if re.match(r"^\s*[0-9]+\s*$", retry_after):
  253              seconds = int(retry_after)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssl_.py:
  402          hostname = hostname.decode("ascii")
  403:     return bool(IPV4_RE.match(hostname) or BRACELESS_IPV6_ADDRZ_RE.match(hostname))
  404  

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:
  279          if scheme in NORMALIZABLE_SCHEMES:
  280:             is_ipv6 = IPV6_ADDRZ_RE.match(host)
  281              if is_ipv6:

  294                      return host.lower()
  295:             elif not IPV4_RE.match(host):
  296                  return six.ensure_str(

  321      """Percent-encodes a request target so that there are no invalid characters"""
  322:     path, query = TARGET_RE.match(target).groups()
  323      target = _encode_invalid_chars(path, PATH_CHARS)

  360      try:
  361:         scheme, authority, path, query, fragment = URI_RE.match(url).groups()
  362          normalize_uri = scheme is None or scheme.lower() in NORMALIZABLE_SCHEMES

  367          if authority:
  368:             auth, host, port = SUBAUTHORITY_RE.match(authority).groups()
  369              if auth and normalize_uri:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pkg_resources\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pkg_resources\_vendor\packaging\tags.py:
  504      # uses version strings like "2.20-2014.11"). See gh-3588.
  505:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  506      if not m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\dist.py:
  325      for pkgname in value:
  326:         if not re.match(r'\w+(\.\w+)*', pkgname):
  327              distutils.log.warn(

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\package_index.py:
  173      parts = basename.split('-')
  174:     if not py_version and any(re.match(r'py\d\.\d$', p) for p in parts[2:]):
  175          # it is a bdist_dumb, not an sdist -- bail out

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\sandbox.py:
  446          pattern_matches = (
  447:             re.match(pattern, filepath)
  448              for pattern in self._exception_patterns

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\ccompiler.py:
  951      for pattern, compiler in _default_compilers:
  952:         if re.match(pattern, platform) is not None or \
  953:            re.match(pattern, osname) is not None:
  954              return compiler

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\dist.py:
  531          command = args[0]
  532:         if not command_re.match(command):
  533              raise SystemExit("invalid command name '%s'" % command)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\fancy_getopt.py:
  199              # '='.
  200:             if not longopt_re.match(long):
  201                  raise DistutilsGetoptError(

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\util.py:
   88          rel_re = re.compile (r'[\d.]+', re.ASCII)
   89:         m = rel_re.match(release)
   90          if m:

  249      while s:
  250:         m = _wordchars_re.match(s, pos)
  251          end = m.end()

  267              if s[end] == "'":           # slurp singly-quoted string
  268:                 m = _squote_re.match(s, end)
  269              elif s[end] == '"':         # slurp doubly-quoted string
  270:                 m = _dquote_re.match(s, end)
  271              else:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\version.py:
  134      def parse (self, vstring):
  135:         match = self.version_re.match(vstring)
  136          if not match:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\command\build_ext.py:
  373              if not (isinstance(ext_name, str) and
  374:                     extension_name_re.match(ext_name)):
  375                  raise DistutilsSetupError(

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\command\build_scripts.py:
  88  
  89:                 match = first_line_re.match(first_line)
  90                  if match:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_vendor\packaging\tags.py:
  504      # uses version strings like "2.20-2014.11"). See gh-3588.
  505:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  506      if not m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\command\bdist_egg.py:
  250                      pattern = r'(?P<name>.+)\.(?P<magic>[^.]+)\.pyc'
  251:                     m = re.match(pattern, name)
  252                      path_new = os.path.join(

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\command\egg_info.py:
  568          """
  569:         return re.match(r"standard file .*not found", msg)
  570  

  714              for line in f:
  715:                 match = re.match(r"Version:.*-r(\d+)\s*$", line)
  716                  if match:

lanier-goat-development\gcli.py:
  170          """
  171:         if re.match('quit|exit|q', line.strip()):
  172              return self.do_EOF(line)

lanier-goat-development\rat.py:
  231          """
  232:         if re.match('quit|exit|q', line.strip()):
  233              return self.do_EOF(line)

lanier-goat-development\bat\test\sos.py:
  98          for line in lines:
  99:             if re.match('Log file', line):
  100                  sos_log_dir = str(line.split(' ')[-1]).split('/sos.log')[0]

lanier-goat-development\codraas\lib\utils.py:
  104                                                  timeout=120)
  105:     match = re.match(r'.*checksum\s*=\s*(\S+)\s*', out[0], re.DOTALL)
  106      if match:

lanier-goat-development\ddmbt\ddtlib.py:
  1143              # skip comments and blank lines
  1144:             if re.match(r'^\s*(#.*|\s*)$', line):
  1145                  continue

  1288      for ddmbtThread in listOfAllActivethreads:
  1289:         match = re.match(r".*(ddmbtThread_\d+),.*", str(ddmbtThread))
  1290:         ddmbtMatch = re.match(r".*(ddmbtThread_\d+).*", str(ddmbtThread))
  1291          if match:

lanier-goat-development\ddmbt\dotfile.py:
  77              lineNumber += 1
  78:             matches = nodeRe.match(line)
  79              if matches:

  81                  continue
  82:             matches = edgeRe.match(line)
  83              if matches:

lanier-goat-development\ddmbt\loganalyzer.py:
  226                      testcaseFileFd.write(line)
  227:                     match = re.match(tcEndPattern, line)
  228                      if match:

  230                  else:
  231:                     match = re.match(tcStartPattern, line)
  232                      if match:

  258                      continue
  259:             match = re.match(linesWithThreadIDsPattern, line)
  260              if match:

  363              truncateFlag = truncate
  364:             match = re.match(linesWithThreadIDsPattern, line)
  365              if match:

  469                      continue
  470:                 match = re.match(pattern2, line)
  471                  if match:

lanier-goat-development\ddmbt\mbtlib.py:
   727          pattern = '^([^#]+)#(.*)#.*$'
   728:         match = re.match(pattern, line)
   729          if match:

   864          composeString = 'None'
   865:     elif re.match(r'^(\d){1,2}$', str(compose)):
   866          composeString = str(compose)

  1061              for pattern in dummyNodePatterns:
  1062:                 if re.match(pattern, fn):
  1063                      if fn == testState.MBTEndNode:

  1079              isNode = False
  1080:             edge = re.match(edgePattern, line)
  1081              if edge:

  1086                  for pattern in dummyEdgePatterns:
  1087:                     if re.match(pattern, fn):
  1088                          skipThis = True

  1091                      continue
  1092:                 matchObj = re.match(dualEdgePattern, fn)
  1093                  if matchObj:

  1096                      for pattern in dummyNodePatterns:
  1097:                         if re.match(pattern, fn):
  1098                              if fn == testState.MBTEndNode:

  1361              if node:
  1362:                 matchObj = re.match(nodePattern1, line)
  1363                  if matchObj:

  1372                      continue
  1373:                 matchObj = re.match(nodePattern2, line)
  1374                  if matchObj:

  1380              else:  # Edge
  1381:                 matchObj = re.match(edgePattern1, line)
  1382                  if matchObj:

  1389                      continue
  1390:                 matchObj = re.match(edgePattern2, line)
  1391                  if matchObj:

  1642              continue
  1643:         result = re.match(currentPattern, line)
  1644          if result:

  2007                          continue
  2008:                     result = re.match(pattern, line)
  2009                      if result:

lanier-goat-development\dependency\centos\pycodestyle.py:
  1081              yield 0, "E402 module level import not at top of file"
  1082:     elif re.match(DUNDER_REGEX, line):
  1083          return

lanier-goat-development\dependency\centos\_distutils_hack\__init__.py:
  35      warnings.warn("Setuptools is replacing distutils.")
  36:     mods = [name for name in sys.modules if re.match(r'distutils\b', name)]
  37      for name in mods:

lanier-goat-development\dependency\centos\_pytest\pytester.py:
  1279          """
  1280:         self._match_lines_random(lines2, lambda name, pat: re.match(pat, name))
  1281  

  1337          __tracebackhide__ = True
  1338:         self._match_lines(lines2, lambda name, pat: re.match(pat, name), "re.match")
  1339  

lanier-goat-development\dependency\centos\asn1crypto\_iri.py:
  59          real_prefix = None
  60:         prefix_match = re.match('^[^:]*://', value)
  61          if prefix_match:

lanier-goat-development\dependency\centos\asn1crypto\core.py:
  2820  
  2821:         if not _OID_RE.match(value):
  2822              raise ValueError(unwrap(

lanier-goat-development\dependency\centos\asn1crypto\pem.py:
  153              # into in a parsed format above each PEM block
  154:             type_name_match = re.match(b'^(?:---- |-----)BEGIN ([A-Z0-9 ]+)(?: ----|-----)', line)
  155              if not type_name_match:

lanier-goat-development\dependency\centos\asn1crypto\x509.py:
  2864          is_ipv6 = encoded_domain_ip.find(':') != -1
  2865:         is_ipv4 = not is_ipv6 and re.match('^\\d+\\.\\d+\\.\\d+\\.\\d+$', encoded_domain_ip)
  2866          is_domain = not is_ipv6 and not is_ipv4

lanier-goat-development\dependency\centos\astroid\brain\brain_gi.py:
  46          # Check if this is a valid name in python
  47:         if not re.match(_identifier_re, name):
  48              continue

lanier-goat-development\dependency\centos\backports\configparser\__init__.py:
   439              elif c == "(":
   440:                 m = self._KEYCRE.match(rest)
   441                  if m is None:

   500              elif c == "{":
   501:                 m = self._KEYCRE.match(rest)
   502                  if m is None:

  1097                  # is it a section header?
  1098:                 mo = self.SECTCRE.match(value)
  1099                  if mo:

  1120                  else:
  1121:                     mo = self._optcre.match(value)
  1122                      if mo:

  1383          for getter in dir(self._parser):
  1384:             m = self.GETTERCRE.match(getter)
  1385              if not m or not callable(getattr(self._parser, getter)):

lanier-goat-development\dependency\centos\botocore\utils.py:
  872          return False
  873:     match = LABEL_RE.match(bucket_name)
  874      if match is None or match.end() != len(bucket_name):

lanier-goat-development\dependency\centos\bs4\builder\_html5lib.py:
  151              if isinstance(element, Doctype):
  152:                 m = doctype_re.match(element)
  153                  if m:

lanier-goat-development\dependency\centos\cassandra\metadata.py:
  1356          return False
  1357:     return valid_cql3_word_re.match(name) is not None
  1358  

lanier-goat-development\dependency\centos\cffi\api.py:
  760          import re
  761:         match = re.match(r'\s*\n', pysource)
  762          if match:

  764          lines = pysource.splitlines() or ['']
  765:         prefix = re.match(r'\s*', lines[0]).group()
  766          for i in range(1, len(lines)):

lanier-goat-development\dependency\centos\cffi\cparser.py:
  350          msg = str(e)
  351:         match = re.match(r"%s:(\d+):" % (CDEF_SOURCE_STRING,), msg)
  352          if match:

lanier-goat-development\dependency\centos\coverage\annotate.py:
  83                      covered = j >= len(missing) or missing[j] > lineno
  84:                 if self.blank_re.match(line):
  85                      dest.write(u'  ')
  86:                 elif self.else_re.match(line):
  87                      # Special logic for lines containing only 'else:'.

lanier-goat-development\dependency\centos\coverage\files.py:
  274          """Does `fpath` match one of our file name patterns?"""
  275:         return self.re.match(fpath) is not None
  276  

  421              # characters that probably mean they are editor junk.
  422:             if re.match(r"^[^.#~!$@%^&*()+=,]+\.pyw?$", filename):
  423                  yield os.path.join(dirpath, filename)

lanier-goat-development\dependency\centos\coverage\phystokens.py:
  176          enc = orig_enc[:12].lower().replace("_", "-")
  177:         if re.match(r"^utf-8($|-)", enc):
  178              return "utf-8"
  179:         if re.match(r"^(latin-1|iso-8859-1|iso-latin-1)($|-)", enc):
  180              return "iso-8859-1"

lanier-goat-development\dependency\centos\coverage\templite.py:
  260          """
  261:         if not re.match(r"[_a-zA-Z][_a-zA-Z0-9]*$", name):
  262              self._syntax_error("Not a valid name", name)

lanier-goat-development\dependency\centos\Cryptodome\SelfTest\loader.py:
  87  
  88:         res = re.match("([A-Za-z0-9]+) = ?(.*)", line)
  89          if not res:

lanier-goat-development\dependency\centos\Cryptodome\SelfTest\Hash\test_BLAKE2.py:
  282  
  283:                 res = re.match("%s:\t([0-9A-Fa-f]*)" % expected, line)
  284                  if not res:

  339                      continue
  340:                 res = re.match("digest: ([0-9A-Fa-f]*)", line)
  341                  if not res:

  384                      continue
  385:                 res = re.match(r"digest\(([0-9]+)\): ([0-9A-Fa-f]*)", line)
  386                  if not res:

lanier-goat-development\dependency\centos\Cryptodome\SelfTest\Signature\test_dss.py:
  159      if isinstance(tv, str):
  160:         res = re.match(r"\[mod = L=([0-9]+), N=([0-9]+), ([a-zA-Z0-9-]+)\]", tv)
  161          assert(res)

  197      if isinstance(tv, str):
  198:         res = re.match(r"\[mod = L=([0-9]+), N=([0-9]+), ([a-zA-Z0-9-]+)\]", tv)
  199          assert(res)

  297      if isinstance(tv, str):
  298:         res = re.match(r"\[(P-[0-9]+),(SHA-[0-9]+)\]", tv)
  299          assert res

  328      if isinstance(tv, str):
  329:         res = re.match(r"\[(P-[0-9]+),(SHA-[0-9]+)\]", tv)
  330          assert res

lanier-goat-development\dependency\centos\dill\source.py:
   97      #NOTE: should be same code different order, with different first element
   98:     _ = dict(re.match(r'([\W\D\S])(.*)', _[i]).groups() for i in range(1,len(_)))
   99:     _f = dict(re.match(r'([\W\D\S])(.*)', _f[i]).groups() for i in range(1,len(_f)))
  100      if (_.keys() == _f.keys()) and (sorted(_.values()) == sorted(_f.values())):

  858              candidate = [line for line in lines if getname(encl) in line and \
  859:                          re.match(pat, line)]
  860              if not candidate:

  864                  candidate = [line for line in lines \
  865:                              if getname(fobj) in line and re.match(pat, line)]
  866              if not len(candidate): raise TypeError('import could not be found')

  880              candidate = [line for line in lines if getname(name) in line and \
  881:                          re.match(r'.*[\w\s]=\s*'+getname(name)+r'\(', line)]
  882              if not len(candidate): raise TypeError('import could not be found')

lanier-goat-development\dependency\centos\docutils\statemachine.py:
    12  - `StateWS`, a state superclass for use with `StateMachineWS`
    13: - `SearchStateMachine`, uses `re.search()` instead of `re.match()`
    14: - `SearchStateMachineWS`, uses `re.search()` instead of `re.match()`
    15  - `ViewList`, extends standard Python lists.

  1041  
  1042:     Changes regular expression matching, from the default `re.match()`
  1043      (succeeds only if the pattern matches at the start of `self.line`) to

  1060  class SearchStateMachine(_SearchOverride, StateMachine):
  1061:     """`StateMachine` which uses `re.search()` instead of `re.match()`."""
  1062      pass

  1065  class SearchStateMachineWS(_SearchOverride, StateMachineWS):
  1066:     """`StateMachineWS` which uses `re.search()` instead of `re.match()`."""
  1067      pass

lanier-goat-development\dependency\centos\docutils\parsers\rst\states.py:
  2211          for i, line in enumerate(arg_block):
  2212:             if re.match(Body.patterns['field_marker'], line):
  2213                  opt_block = arg_block[i:]

lanier-goat-development\dependency\centos\docutils\parsers\rst\directives\__init__.py:
  232      """
  233:     match = re.match(r'^([0-9.]+) *(%s)$' % '|'.join(units), argument)
  234      try:

lanier-goat-development\dependency\centos\docutils\writers\_html_base.py:
  942                  if att_name in atts:
  943:                     match = re.match(r'([0-9.]+)(\S*)$', atts[att_name])
  944                      assert match

  950              if att_name in atts:
  951:                 if re.match(r'^[0-9.]+$', atts[att_name]):
  952                      # Interpret unitless values as pixels.

lanier-goat-development\dependency\centos\docutils\writers\latex2e\__init__.py:
  2345                               ' option `pxunit` will be removed.')
  2346:         match = re.match(r'(\d*\.?\d*)\s*(\S*)', length_str)
  2347          if not match:

lanier-goat-development\dependency\centos\flake8\utils.py:
  69          for token_re, token_name in _FILE_LIST_TOKEN_TYPES:
  70:             match = token_re.match(value, i)
  71              if match:

lanier-goat-development\dependency\centos\flask\cli.py:
  155  
  156:     match = re.match(r"^ *([^ ()]+) *(?:\((.*?) *,? *\))? *$", app_name)
  157  

lanier-goat-development\dependency\centos\future\backports\email\_encoded_words.py:
  116          # The validate kwarg to b64decode is not supported in Py2.x
  117:         if not re.match(b'^[A-Za-z0-9+/]*={0,2}$', padded_encoded):
  118              raise binascii.Error('Non-base64 digit found')

lanier-goat-development\dependency\centos\future\backports\email\feedparser.py:
  225                  continue
  226:             if not headerRE.match(line):
  227                  # If we saw the RFC defined header/body separator

  229                  # part of the body so push it back.
  230:                 if not NLCRE.match(line):
  231                      defect = errors.MissingHeaderBodySeparatorDefect()

  343                      break
  344:                 mo = boundaryre.match(line)
  345                  if mo:

  375                              continue
  376:                         mo = boundaryre.match(line)
  377                          if not mo:

lanier-goat-development\dependency\centos\future\backports\test\support.py:
   978              # Filter out the matching messages
   979:             if (re.match(msg, str(warning), re.I) and
   980                  issubclass(warning.__class__, cat)):

  1421      }
  1422:     m = re.match(r'(\d+(\.\d+)?) (K|M|G|T)b?$', limit,
  1423                   re.IGNORECASE | re.VERBOSE)

  1976                      kernel_version = platform.release()
  1977:                     m = re.match("2.6.(\d{1,2})", kernel_version)
  1978                      can = m is None or int(m.group(1)) >= 39

lanier-goat-development\dependency\centos\future\backports\urllib\request.py:
  2129          stuff = headers['www-authenticate']
  2130:         match = re.match('[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
  2131          if not match:

  2154          stuff = headers['proxy-authenticate']
  2155:         match = re.match('[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
  2156          if not match:

  2467  
  2468:         m = re.match(r"(\d+(?:\.\d+)*)(/\d+)?", value)
  2469          if m is not None:

  2547                          # See if address has a type:// prefix
  2548:                         if not re.match('^([^/:]+)://', address):
  2549                              address = '%s://%s' % (protocol, address)

  2621              for val in host:
  2622:                 if re.match(test, val, re.I):
  2623                      return 1

lanier-goat-development\dependency\centos\future\utils\__init__.py:
  262          _name_re = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*$")
  263:         return bool(_name_re.match(s))
  264  

lanier-goat-development\dependency\centos\importlib_metadata\__init__.py:
  286          for line in filter(None, lines):
  287:             section_match = re.match(r'\[(.*)\]$', line)
  288              if section_match:

  378          manifest = template.format(pattern=normalized)
  379:         return re.match(manifest, item.name, flags=re.IGNORECASE)
  380  

lanier-goat-development\dependency\centos\importlib_metadata\tests\test_api.py:
  33          assert isinstance(pkg_version, text)
  34:         assert re.match(self.version_pattern, pkg_version)
  35  

  38          assert isinstance(pkg_version, text)
  39:         assert re.match(self.version_pattern, pkg_version)
  40  

  71      def test_importlib_metadata_version(self):
  72:         assert re.match(self.version_pattern, __version__)
  73  

lanier-goat-development\dependency\centos\importlib_metadata\tests\test_main.py:
  28          assert isinstance(dist.version, text)
  29:         assert re.match(self.version_pattern, dist.version)
  30  

lanier-goat-development\dependency\centos\isort\isort.py:
  318      def _module_key(module_name, config, sub_imports=False, ignore_case=False, section_name=None):
  319:         match = re.match(r'^(\.+)\s*(.*)', module_name)
  320          if match:

lanier-goat-development\dependency\centos\isort\main.py:
  76      else:
  77:         return bool(shebang_re.match(line))
  78  

lanier-goat-development\dependency\centos\jenkinsapi\plugins.py:
  241      def __delitem__(self, shortName):
  242:         if re.match('.*@.*', shortName):
  243              real_shortName = re.compile('(.*)@(.*)').search(shortName).group(1)

lanier-goat-development\dependency\centos\jenkinsapi_tests\systests\test_jenkins_artifacts.py:
  44              log.info('Text artifact: %s', read_back_text)
  45:             assert re.match(r'^PING \S+ \(127.0.0.1\)', read_back_text) is not None
  46              assert read_back_text.endswith('ms') is True

  54              read_back_text = read_back_text.decode('ascii')
  55:             assert re.match(r'^PING \S+ \(127.0.0.1\)', read_back_text) is not None
  56              assert read_back_text.endswith('ms') is True

lanier-goat-development\dependency\centos\jinja2\utils.py:
  210      for i, word in enumerate(words):
  211:         match = _punctuation_re.match(word)
  212          if match:

  230              if '@' in middle and not middle.startswith('www.') and \
  231:                not ':' in middle and _simple_email_re.match(middle):
  232                  middle = '<a href="mailto:%s">%s</a>' % (middle, middle)

lanier-goat-development\dependency\centos\libfuturize\fixer_util.py:
  485      """
  486:     return bool(re.match(SHEBANG_REGEX, node.prefix))
  487  

  498      """
  499:     return bool(re.match(ENCODING_REGEX, node.prefix))
  500  

lanier-goat-development\dependency\centos\libfuturize\fixes\fix_bytes.py:
  20          if node.type == token.STRING:
  21:             if _literal_re.match(node.value):
  22                  new = node.clone()

lanier-goat-development\dependency\centos\libfuturize\fixes\fix_division_safe.py:
  45          # If it's a leaf, let's see if it's a numeric constant containing a '.'
  46:         return const_re.match(expr.value)
  47      elif isinstance(expr, Node):

lanier-goat-development\dependency\centos\libfuturize\fixes\fix_oldstr_wrap.py:
  31              touch_import_top(u'past.types', u'oldstr', node)
  32:             if _literal_re.match(node.value):
  33                  new = node.clone()

lanier-goat-development\dependency\centos\lxml\_elementpath.py:
  176          return select
  177:     if signature == "-" and not re.match(r"-?\d+$", predicate[0]):
  178          # [tag]

  185          return select
  186:     if signature == ".='" or (signature == "-='" and not re.match(r"-?\d+$", predicate[0])):
  187          # [.='value'] or [tag='value']

lanier-goat-development\dependency\centos\markdown\blockprocessors.py:
  217          # Get indent level
  218:         m = self.INDENT_RE.match(block)
  219          if m:

  309          """ Remove ``>`` from beginning of a line. """
  310:         m = self.RE.match(line)
  311          if line.strip() == ">":

  344      def test(self, parent, block):
  345:         return bool(self.RE.match(block))
  346  

  409          for line in block.split('\n'):
  410:             m = self.CHILD_RE.match(line)
  411              if m:

  416                      INTEGER_RE = re.compile(r'(\d+)')
  417:                     self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()
  418                  # Append to the list
  419                  items.append(m.group(3))
  420:             elif self.INDENT_RE.match(line):
  421                  # This is an indented (possibly nested) item.

  481      def test(self, parent, block):
  482:         return bool(self.RE.match(block))
  483  

lanier-goat-development\dependency\centos\markdown\postprocessors.py:
  93      def isblocklevel(self, html):
  94:         m = re.match(r'^\<\/?([^ >]+)', html)
  95          if m:

lanier-goat-development\dependency\centos\markdown\preprocessors.py:
   94      def _get_left_tag(self, block):
   95:         m = self.left_tag_re.match(block)
   96          if m:

  179          for i, item in enumerate(items):
  180:             if self.left_tag_re.match(item):
  181                  left_tag, left_index, attrs = \

  354              line = lines.pop(0)
  355:             m = self.RE.match(line)
  356              if m:

  361                      # Check next line for title
  362:                     tm = self.TITLE_RE.match(lines[0])
  363                      if tm:

lanier-goat-development\dependency\centos\markdown\extensions\abbr.py:
  49          for line in lines:
  50:             m = ABBR_REF_RE.match(line)
  51              if m:

lanier-goat-development\dependency\centos\markdown\extensions\attr_list.py:
  135                  if elem.tail:
  136:                     m = self.INLINE_RE.match(elem.tail)
  137                      if m:

lanier-goat-development\dependency\centos\markdown\extensions\def_list.py:
  41          block = raw_block[m.end():]
  42:         no_indent = self.NO_INDENT_RE.match(block)
  43          if no_indent:

lanier-goat-development\dependency\centos\markdown\extensions\footnotes.py:
  225          while True:
  226:             m = DEF_RE.match(lines[i])
  227              if m:

  259          def detab(line):
  260:             match = TABBED_RE.match(line)
  261              if match:

  270                      continue
  271:                 elif not blank_line and not DEF_RE.match(line):
  272                      # not tabbed but still part of first par.

lanier-goat-development\dependency\centos\markdown\extensions\meta.py:
  53          key = None
  54:         if lines and BEGIN_RE.match(lines[0]):
  55              lines.pop(0)

  57              line = lines.pop(0)
  58:             m1 = META_RE.match(line)
  59:             if line.strip() == '' or END_RE.match(line):
  60                  break  # blank line or end of YAML header - done

  68              else:
  69:                 m2 = META_MORE_RE.match(line)
  70                  if m2 and key:

lanier-goat-development\dependency\centos\markdown\extensions\toc.py:
  37      while id in ids or not id:
  38:         m = IDCOUNT_RE.match(id)
  39          if m:

lanier-goat-development\dependency\centos\packaging\tags.py:
  263      # uses version strings like "2.20-2014.11"). See gh-3588.
  264:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  265      if not m:

lanier-goat-development\dependency\centos\paramiko\config.py:
  139              # Parse line into key, value
  140:             match = re.match(self.SETTINGS_REGEX, line)
  141              if not match:

lanier-goat-development\dependency\centos\pbr\packaging.py:
  142          # Ignore index URL lines
  143:         if re.match(r'^\s*(-i|--index-url|--extra-index-url|--find-links).*',
  144                      line):

  172          # -f lines are for index locations, and don't get used here
  173:         if re.match(r'\s*-e\s+', line):
  174:             extract = re.match(r'\s*-e\s+(.*)$', line)
  175              line = extract.group(1)

  178              line = re.sub(r'egg=([^&]+).*$', egg_fragment, egg.fragment)
  179:         elif re.match(r'\s*-f\s+', line):
  180              line = None

  205          # skip comments and blank lines
  206:         if re.match(r'(\s*#)|(\s*$)', line):
  207              continue
  208          # lines with -e or -f need the whole line, minus the flag
  209:         if re.match(r'\s*-[ef]\s+', line):
  210              dependency_links.append(re.sub(r'\s*-[ef]\s+', '', line))
  211          # lines that are only urls can go in unmolested
  212:         elif re.match(r'^\s*(https?|git(\+(https|ssh))?|svn|hg)\S*:', line):
  213              dependency_links.append(line)

lanier-goat-development\dependency\centos\pbr\util.py:
  373                  for requirement in in_cfg_value:
  374:                     m = re.match(requirement_pattern, requirement)
  375                      requirement_package = m.group('package').strip()

  446              for requirement in requirements:
  447:                 m = re.match(requirement_pattern, requirement)
  448                  extras_value = m.group('package').strip()

lanier-goat-development\dependency\centos\pbr\tests\test_packaging.py:
  113          for line in gnupg_version[0].split('\n'):
  114:             gnupg_version = gnupg_version_re.match(line)
  115              if gnupg_version:

lanier-goat-development\dependency\centos\pexpect\pxssh.py:
  373              for line in lines:
  374:                 if not config_has_server and re.match(server_regex, line, re.IGNORECASE):
  375                      config_has_server = True

  380                      break  # we have left the relevant section
  381:                 elif config_has_server and re.match(user_regex, line, re.IGNORECASE):
  382                      server_has_username = True

lanier-goat-development\dependency\centos\pkg_resources\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

lanier-goat-development\dependency\centos\pkg_resources\_vendor\packaging\_manylinux.py:
  210      """
  211:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  212      if not m:

lanier-goat-development\dependency\centos\pkg_resources\_vendor\packaging\_musllinux.py:
  79          return None
  80:     m = re.match(r"Version (\d+)\.(\d+)", lines[1])
  81      if not m:

lanier-goat-development\dependency\centos\pkg_resources\_vendor\packaging\utils.py:
  98      # See PEP 427 for the rules on escaping the project name
  99:     if "__" in name_part or re.match(r"^[\w\d._]*$", name_part, re.UNICODE) is None:
  100          raise InvalidWheelFilename(f"Invalid project name: {filename}")

lanier-goat-development\dependency\centos\psutil\tests\__init__.py:
  1572      elif family == psutil.AF_LINK:
  1573:         assert re.match(r'([a-fA-F0-9]{2}[:|\-]?){6}', addr) is not None, addr
  1574      else:

lanier-goat-development\dependency\centos\py\_path\svnwc.py:
  1176      # example: 2003-10-27 20:43:14 +0100 (Mon, 27 Oct 2003)
  1177:     m = re.match(r'(\d+-\d+-\d+ \d+:\d+:\d+) ([+-]\d+) .*', timestr)
  1178      if not m:

lanier-goat-development\dependency\centos\pycparser\ply\lex.py:
  319              for lexre, lexindexfunc in self.lexre:
  320:                 m = lexre.match(lexdata, lexpos)
  321                  if not m:

  843          for line in lines:
  844:             m = fre.match(line)
  845              if not m:
  846:                 m = sre.match(line)
  847              if m:

lanier-goat-development\dependency\centos\pycparser\ply\yacc.py:
  3009                  linen += 1
  3010:                 m = fre.match(line)
  3011                  if m:

lanier-goat-development\dependency\centos\pyflakes\checker.py:
   593                  tp != tokenize.COMMENT or  # skip non comments
   594:                 not TYPE_COMMENT_RE.match(text) or  # skip non-type comments
   595:                 TYPE_IGNORE_RE.match(text)  # skip ignores
   596          ):

  1051              comment = comment.split(':', 1)[1].strip()
  1052:             func_match = TYPE_FUNC_RE.match(comment)
  1053              if func_match:

lanier-goat-development\dependency\centos\pylint\utils.py:
  1482              value = str(value).strip()
  1483:             if re.match(r"^([\w-]+,)+[\w-]+$", str(value)):
  1484                  separator = "\n " + " " * len(optname)

lanier-goat-development\dependency\centos\pylint\checkers\python3.py:
  50          return False
  51:     if re.match(r"0\d+", literal):
  52          try:

lanier-goat-development\dependency\centos\pylint\checkers\typecheck.py:
  837              # attribute is marked as generated, stop here
  838:             if re.match(pattern, node.attrname):
  839                  return
  840:             if re.match(pattern, node.as_string()):
  841                  return

lanier-goat-development\dependency\centos\pylint\extensions\_check_docs_utils.py:
  780      def _is_section_header(line):
  781:         return bool(re.match(r"\s*-+$", line))
  782  

lanier-goat-development\dependency\centos\pylint\test\input\func_w0405.py:
  11  __revision__ = 0
  12: _re.match('yo', '.*')
  13  

lanier-goat-development\dependency\centos\pyVim\connect.py:
  244     try:
  245:       info = re.match(_rx, host)
  246        if info is not None:

lanier-goat-development\dependency\centos\redis\client.py:
  3029          command_time, command_data = response.split(' ', 1)
  3030:         m = self.monitor_re.match(command_data)
  3031          db_id, client_info, command = m.groups()

lanier-goat-development\dependency\centos\requests\utils.py:
  89              test = test.replace("?", r".")      # change glob char
  90:             if re.match(test, host, re.I):
  91                  return True

lanier-goat-development\dependency\centos\selenium\webdriver\support\color.py:
  51              def match(self, pattern, str_):
  52:                 self.match_obj = re.match(pattern, str_)
  53                  return self.match_obj

lanier-goat-development\dependency\centos\setuptools\dist.py:
  359      for pkgname in value:
  360:         if not re.match(r'\w+(\.\w+)*', pkgname):
  361              distutils.log.warn(

lanier-goat-development\dependency\centos\setuptools\package_index.py:
  174      parts = basename.split('-')
  175:     if not py_version and any(re.match(r'py\d\.\d$', p) for p in parts[2:]):
  176          # it is a bdist_dumb, not an sdist -- bail out

lanier-goat-development\dependency\centos\setuptools\sandbox.py:
  477          pattern_matches = (
  478:             re.match(pattern, filepath) for pattern in self._exception_patterns
  479          )

lanier-goat-development\dependency\centos\setuptools\_distutils\ccompiler.py:
  958      for pattern, compiler in _default_compilers:
  959:         if re.match(pattern, platform) is not None or \
  960:            re.match(pattern, osname) is not None:
  961              return compiler

lanier-goat-development\dependency\centos\setuptools\_distutils\dist.py:
  531          command = args[0]
  532:         if not command_re.match(command):
  533              raise SystemExit("invalid command name '%s'" % command)

lanier-goat-development\dependency\centos\setuptools\_distutils\fancy_getopt.py:
  199              # '='.
  200:             if not longopt_re.match(long):
  201                  raise DistutilsGetoptError(

lanier-goat-development\dependency\centos\setuptools\_distutils\util.py:
   88          rel_re = re.compile (r'[\d.]+', re.ASCII)
   89:         m = rel_re.match(release)
   90          if m:

  317      while s:
  318:         m = _wordchars_re.match(s, pos)
  319          end = m.end()

  335              if s[end] == "'":           # slurp singly-quoted string
  336:                 m = _squote_re.match(s, end)
  337              elif s[end] == '"':         # slurp doubly-quoted string
  338:                 m = _dquote_re.match(s, end)
  339              else:

lanier-goat-development\dependency\centos\setuptools\_distutils\version.py:
  154      def parse (self, vstring):
  155:         match = self.version_re.match(vstring)
  156          if not match:

lanier-goat-development\dependency\centos\setuptools\_distutils\command\build_ext.py:
  371              if not (isinstance(ext_name, str) and
  372:                     extension_name_re.match(ext_name)):
  373                  raise DistutilsSetupError(

lanier-goat-development\dependency\centos\setuptools\_distutils\command\build_scripts.py:
  88  
  89:                 match = first_line_re.match(first_line)
  90                  if match:

lanier-goat-development\dependency\centos\setuptools\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

lanier-goat-development\dependency\centos\setuptools\_vendor\packaging\_manylinux.py:
  210      """
  211:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  212      if not m:

lanier-goat-development\dependency\centos\setuptools\_vendor\packaging\_musllinux.py:
  79          return None
  80:     m = re.match(r"Version (\d+)\.(\d+)", lines[1])
  81      if not m:

lanier-goat-development\dependency\centos\setuptools\_vendor\packaging\utils.py:
  98      # See PEP 427 for the rules on escaping the project name
  99:     if "__" in name_part or re.match(r"^[\w\d._]*$", name_part, re.UNICODE) is None:
  100          raise InvalidWheelFilename(f"Invalid project name: {filename}")

lanier-goat-development\dependency\centos\setuptools\command\bdist_egg.py:
  247                      pattern = r'(?P<name>.+)\.(?P<magic>[^.]+)\.pyc'
  248:                     m = re.match(pattern, name)
  249                      path_new = os.path.join(

lanier-goat-development\dependency\centos\setuptools\command\egg_info.py:
  574          """
  575:         return re.match(r"standard file .*not found", msg)
  576  

  747              for line in f:
  748:                 match = re.match(r"Version:.*-r(\d+)\s*$", line)
  749                  if match:

lanier-goat-development\dependency\centos\urllib3\util\retry.py:
  372          # Whitespace: https://tools.ietf.org/html/rfc7230#section-3.2.4
  373:         if re.match(r"^\s*[0-9]+\s*$", retry_after):
  374              seconds = int(retry_after)

lanier-goat-development\dependency\centos\urllib3\util\ssl_.py:
  466          hostname = hostname.decode("ascii")
  467:     return bool(IPV4_RE.match(hostname) or BRACELESS_IPV6_ADDRZ_RE.match(hostname))
  468  

lanier-goat-development\dependency\centos\urllib3\util\url.py:
  279          if scheme in NORMALIZABLE_SCHEMES:
  280:             is_ipv6 = IPV6_ADDRZ_RE.match(host)
  281              if is_ipv6:

  294                      return host.lower()
  295:             elif not IPV4_RE.match(host):
  296                  return six.ensure_str(

  321      """Percent-encodes a request target so that there are no invalid characters"""
  322:     path, query = TARGET_RE.match(target).groups()
  323      target = _encode_invalid_chars(path, PATH_CHARS)

  360      try:
  361:         scheme, authority, path, query, fragment = URI_RE.match(url).groups()
  362          normalize_uri = scheme is None or scheme.lower() in NORMALIZABLE_SCHEMES

  369              auth = auth or None
  370:             host, port = _HOST_PORT_RE.match(host_port).groups()
  371              if auth and normalize_uri:

lanier-goat-development\dependency\centos\validators\i18n\fi.py:
  43      """
  44:     if not business_id or not re.match(business_id_pattern, business_id):
  45          return False

  83  
  84:     result = re.match(ssn_pattern, ssn)
  85      if not result:

lanier-goat-development\dependency\centos\werkzeug\formparser.py:
  275      """Checks if the string given is a valid multipart boundary."""
  276:     return _multipart_boundary_re.match(boundary) is not None
  277  

lanier-goat-development\dependency\centos\werkzeug\http.py:
  414          while rest:
  415:             optmatch = _option_header_piece_re.match(rest)
  416              if not optmatch:

  758      while pos < end:
  759:         match = _etag_re.match(value, pos)
  760          if match is None:

lanier-goat-development\dependency\centos\werkzeug\urls.py:
  457      i = url.find(s(":"))
  458:     if i > 0 and _scheme_re.match(to_native(url[:i], errors="replace")):
  459          # make sure "iri" is not actually a port number (in which case

lanier-goat-development\dependency\centos\werkzeug\contrib\sessions.py:
  169          """Check if a key has the correct format."""
  170:         return _sha1_re.match(key) is not None
  171  

  307                  continue
  308:             match = filename_re.match(filename)
  309              if match is not None:

lanier-goat-development\dependency\centos\werkzeug\debug\tbtools.py:
  531              while lineno > 0:
  532:                 if _funcdef_re.match(lines[lineno].code):
  533                      break

lanier-goat-development\dependency\photon\pycodestyle.py:
  1081              yield 0, "E402 module level import not at top of file"
  1082:     elif re.match(DUNDER_REGEX, line):
  1083          return

lanier-goat-development\dependency\photon\_distutils_hack\__init__.py:
  35      warnings.warn("Setuptools is replacing distutils.")
  36:     mods = [name for name in sys.modules if re.match(r'distutils\b', name)]
  37      for name in mods:

lanier-goat-development\dependency\photon\_pytest\pytester.py:
  1279          """
  1280:         self._match_lines_random(lines2, lambda name, pat: re.match(pat, name))
  1281  

  1337          __tracebackhide__ = True
  1338:         self._match_lines(lines2, lambda name, pat: re.match(pat, name), "re.match")
  1339  

lanier-goat-development\dependency\photon\asn1crypto\_iri.py:
  59          real_prefix = None
  60:         prefix_match = re.match('^[^:]*://', value)
  61          if prefix_match:

lanier-goat-development\dependency\photon\asn1crypto\core.py:
  2820  
  2821:         if not _OID_RE.match(value):
  2822              raise ValueError(unwrap(

lanier-goat-development\dependency\photon\asn1crypto\pem.py:
  153              # into in a parsed format above each PEM block
  154:             type_name_match = re.match(b'^(?:---- |-----)BEGIN ([A-Z0-9 ]+)(?: ----|-----)', line)
  155              if not type_name_match:

lanier-goat-development\dependency\photon\asn1crypto\x509.py:
  2864          is_ipv6 = encoded_domain_ip.find(':') != -1
  2865:         is_ipv4 = not is_ipv6 and re.match('^\\d+\\.\\d+\\.\\d+\\.\\d+$', encoded_domain_ip)
  2866          is_domain = not is_ipv6 and not is_ipv4

lanier-goat-development\dependency\photon\astroid\brain\brain_gi.py:
  46          # Check if this is a valid name in python
  47:         if not re.match(_identifier_re, name):
  48              continue

lanier-goat-development\dependency\photon\backports\configparser\__init__.py:
   439              elif c == "(":
   440:                 m = self._KEYCRE.match(rest)
   441                  if m is None:

   500              elif c == "{":
   501:                 m = self._KEYCRE.match(rest)
   502                  if m is None:

  1097                  # is it a section header?
  1098:                 mo = self.SECTCRE.match(value)
  1099                  if mo:

  1120                  else:
  1121:                     mo = self._optcre.match(value)
  1122                      if mo:

  1383          for getter in dir(self._parser):
  1384:             m = self.GETTERCRE.match(getter)
  1385              if not m or not callable(getattr(self._parser, getter)):

lanier-goat-development\dependency\photon\botocore\utils.py:
  872          return False
  873:     match = LABEL_RE.match(bucket_name)
  874      if match is None or match.end() != len(bucket_name):

lanier-goat-development\dependency\photon\bs4\builder\_html5lib.py:
  151              if isinstance(element, Doctype):
  152:                 m = doctype_re.match(element)
  153                  if m:

lanier-goat-development\dependency\photon\cassandra\metadata.py:
  1356          return False
  1357:     return valid_cql3_word_re.match(name) is not None
  1358  

lanier-goat-development\dependency\photon\cffi\api.py:
  760          import re
  761:         match = re.match(r'\s*\n', pysource)
  762          if match:

  764          lines = pysource.splitlines() or ['']
  765:         prefix = re.match(r'\s*', lines[0]).group()
  766          for i in range(1, len(lines)):

lanier-goat-development\dependency\photon\cffi\cparser.py:
  350          msg = str(e)
  351:         match = re.match(r"%s:(\d+):" % (CDEF_SOURCE_STRING,), msg)
  352          if match:

lanier-goat-development\dependency\photon\coverage\annotate.py:
  83                      covered = j >= len(missing) or missing[j] > lineno
  84:                 if self.blank_re.match(line):
  85                      dest.write(u'  ')
  86:                 elif self.else_re.match(line):
  87                      # Special logic for lines containing only 'else:'.

lanier-goat-development\dependency\photon\coverage\files.py:
  274          """Does `fpath` match one of our file name patterns?"""
  275:         return self.re.match(fpath) is not None
  276  

  421              # characters that probably mean they are editor junk.
  422:             if re.match(r"^[^.#~!$@%^&*()+=,]+\.pyw?$", filename):
  423                  yield os.path.join(dirpath, filename)

lanier-goat-development\dependency\photon\coverage\phystokens.py:
  176          enc = orig_enc[:12].lower().replace("_", "-")
  177:         if re.match(r"^utf-8($|-)", enc):
  178              return "utf-8"
  179:         if re.match(r"^(latin-1|iso-8859-1|iso-latin-1)($|-)", enc):
  180              return "iso-8859-1"

lanier-goat-development\dependency\photon\coverage\templite.py:
  260          """
  261:         if not re.match(r"[_a-zA-Z][_a-zA-Z0-9]*$", name):
  262              self._syntax_error("Not a valid name", name)

lanier-goat-development\dependency\photon\Cryptodome\SelfTest\loader.py:
  87  
  88:         res = re.match("([A-Za-z0-9]+) = ?(.*)", line)
  89          if not res:

lanier-goat-development\dependency\photon\Cryptodome\SelfTest\Hash\test_BLAKE2.py:
  282  
  283:                 res = re.match("%s:\t([0-9A-Fa-f]*)" % expected, line)
  284                  if not res:

  339                      continue
  340:                 res = re.match("digest: ([0-9A-Fa-f]*)", line)
  341                  if not res:

  384                      continue
  385:                 res = re.match(r"digest\(([0-9]+)\): ([0-9A-Fa-f]*)", line)
  386                  if not res:

lanier-goat-development\dependency\photon\Cryptodome\SelfTest\Signature\test_dss.py:
  159      if isinstance(tv, str):
  160:         res = re.match(r"\[mod = L=([0-9]+), N=([0-9]+), ([a-zA-Z0-9-]+)\]", tv)
  161          assert(res)

  197      if isinstance(tv, str):
  198:         res = re.match(r"\[mod = L=([0-9]+), N=([0-9]+), ([a-zA-Z0-9-]+)\]", tv)
  199          assert(res)

  297      if isinstance(tv, str):
  298:         res = re.match(r"\[(P-[0-9]+),(SHA-[0-9]+)\]", tv)
  299          assert res

  328      if isinstance(tv, str):
  329:         res = re.match(r"\[(P-[0-9]+),(SHA-[0-9]+)\]", tv)
  330          assert res

lanier-goat-development\dependency\photon\dill\source.py:
   97      #NOTE: should be same code different order, with different first element
   98:     _ = dict(re.match(r'([\W\D\S])(.*)', _[i]).groups() for i in range(1,len(_)))
   99:     _f = dict(re.match(r'([\W\D\S])(.*)', _f[i]).groups() for i in range(1,len(_f)))
  100      if (_.keys() == _f.keys()) and (sorted(_.values()) == sorted(_f.values())):

  858              candidate = [line for line in lines if getname(encl) in line and \
  859:                          re.match(pat, line)]
  860              if not candidate:

  864                  candidate = [line for line in lines \
  865:                              if getname(fobj) in line and re.match(pat, line)]
  866              if not len(candidate): raise TypeError('import could not be found')

  880              candidate = [line for line in lines if getname(name) in line and \
  881:                          re.match(r'.*[\w\s]=\s*'+getname(name)+r'\(', line)]
  882              if not len(candidate): raise TypeError('import could not be found')

lanier-goat-development\dependency\photon\docutils\statemachine.py:
    12  - `StateWS`, a state superclass for use with `StateMachineWS`
    13: - `SearchStateMachine`, uses `re.search()` instead of `re.match()`
    14: - `SearchStateMachineWS`, uses `re.search()` instead of `re.match()`
    15  - `ViewList`, extends standard Python lists.

  1041  
  1042:     Changes regular expression matching, from the default `re.match()`
  1043      (succeeds only if the pattern matches at the start of `self.line`) to

  1060  class SearchStateMachine(_SearchOverride, StateMachine):
  1061:     """`StateMachine` which uses `re.search()` instead of `re.match()`."""
  1062      pass

  1065  class SearchStateMachineWS(_SearchOverride, StateMachineWS):
  1066:     """`StateMachineWS` which uses `re.search()` instead of `re.match()`."""
  1067      pass

lanier-goat-development\dependency\photon\docutils\parsers\rst\states.py:
  2211          for i, line in enumerate(arg_block):
  2212:             if re.match(Body.patterns['field_marker'], line):
  2213                  opt_block = arg_block[i:]

lanier-goat-development\dependency\photon\docutils\parsers\rst\directives\__init__.py:
  232      """
  233:     match = re.match(r'^([0-9.]+) *(%s)$' % '|'.join(units), argument)
  234      try:

lanier-goat-development\dependency\photon\docutils\writers\_html_base.py:
  942                  if att_name in atts:
  943:                     match = re.match(r'([0-9.]+)(\S*)$', atts[att_name])
  944                      assert match

  950              if att_name in atts:
  951:                 if re.match(r'^[0-9.]+$', atts[att_name]):
  952                      # Interpret unitless values as pixels.

lanier-goat-development\dependency\photon\docutils\writers\latex2e\__init__.py:
  2345                               ' option `pxunit` will be removed.')
  2346:         match = re.match(r'(\d*\.?\d*)\s*(\S*)', length_str)
  2347          if not match:

lanier-goat-development\dependency\photon\flake8\utils.py:
  69          for token_re, token_name in _FILE_LIST_TOKEN_TYPES:
  70:             match = token_re.match(value, i)
  71              if match:

lanier-goat-development\dependency\photon\flask\cli.py:
  155  
  156:     match = re.match(r"^ *([^ ()]+) *(?:\((.*?) *,? *\))? *$", app_name)
  157  

lanier-goat-development\dependency\photon\future\backports\email\_encoded_words.py:
  116          # The validate kwarg to b64decode is not supported in Py2.x
  117:         if not re.match(b'^[A-Za-z0-9+/]*={0,2}$', padded_encoded):
  118              raise binascii.Error('Non-base64 digit found')

lanier-goat-development\dependency\photon\future\backports\email\feedparser.py:
  225                  continue
  226:             if not headerRE.match(line):
  227                  # If we saw the RFC defined header/body separator

  229                  # part of the body so push it back.
  230:                 if not NLCRE.match(line):
  231                      defect = errors.MissingHeaderBodySeparatorDefect()

  343                      break
  344:                 mo = boundaryre.match(line)
  345                  if mo:

  375                              continue
  376:                         mo = boundaryre.match(line)
  377                          if not mo:

lanier-goat-development\dependency\photon\future\backports\test\support.py:
   978              # Filter out the matching messages
   979:             if (re.match(msg, str(warning), re.I) and
   980                  issubclass(warning.__class__, cat)):

  1421      }
  1422:     m = re.match(r'(\d+(\.\d+)?) (K|M|G|T)b?$', limit,
  1423                   re.IGNORECASE | re.VERBOSE)

  1976                      kernel_version = platform.release()
  1977:                     m = re.match("2.6.(\d{1,2})", kernel_version)
  1978                      can = m is None or int(m.group(1)) >= 39

lanier-goat-development\dependency\photon\future\backports\urllib\request.py:
  2129          stuff = headers['www-authenticate']
  2130:         match = re.match('[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
  2131          if not match:

  2154          stuff = headers['proxy-authenticate']
  2155:         match = re.match('[ \t]*([^ \t]+)[ \t]+realm="([^"]*)"', stuff)
  2156          if not match:

  2467  
  2468:         m = re.match(r"(\d+(?:\.\d+)*)(/\d+)?", value)
  2469          if m is not None:

  2547                          # See if address has a type:// prefix
  2548:                         if not re.match('^([^/:]+)://', address):
  2549                              address = '%s://%s' % (protocol, address)

  2621              for val in host:
  2622:                 if re.match(test, val, re.I):
  2623                      return 1

lanier-goat-development\dependency\photon\future\utils\__init__.py:
  262          _name_re = re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*$")
  263:         return bool(_name_re.match(s))
  264  

lanier-goat-development\dependency\photon\importlib_metadata\__init__.py:
  286          for line in filter(None, lines):
  287:             section_match = re.match(r'\[(.*)\]$', line)
  288              if section_match:

  378          manifest = template.format(pattern=normalized)
  379:         return re.match(manifest, item.name, flags=re.IGNORECASE)
  380  

lanier-goat-development\dependency\photon\importlib_metadata\tests\test_api.py:
  33          assert isinstance(pkg_version, text)
  34:         assert re.match(self.version_pattern, pkg_version)
  35  

  38          assert isinstance(pkg_version, text)
  39:         assert re.match(self.version_pattern, pkg_version)
  40  

  71      def test_importlib_metadata_version(self):
  72:         assert re.match(self.version_pattern, __version__)
  73  

lanier-goat-development\dependency\photon\importlib_metadata\tests\test_main.py:
  28          assert isinstance(dist.version, text)
  29:         assert re.match(self.version_pattern, dist.version)
  30  

lanier-goat-development\dependency\photon\isort\isort.py:
  318      def _module_key(module_name, config, sub_imports=False, ignore_case=False, section_name=None):
  319:         match = re.match(r'^(\.+)\s*(.*)', module_name)
  320          if match:

lanier-goat-development\dependency\photon\isort\main.py:
  76      else:
  77:         return bool(shebang_re.match(line))
  78  

lanier-goat-development\dependency\photon\jenkinsapi\plugins.py:
  241      def __delitem__(self, shortName):
  242:         if re.match('.*@.*', shortName):
  243              real_shortName = re.compile('(.*)@(.*)').search(shortName).group(1)

lanier-goat-development\dependency\photon\jenkinsapi_tests\systests\test_jenkins_artifacts.py:
  44              log.info('Text artifact: %s', read_back_text)
  45:             assert re.match(r'^PING \S+ \(127.0.0.1\)', read_back_text) is not None
  46              assert read_back_text.endswith('ms') is True

  54              read_back_text = read_back_text.decode('ascii')
  55:             assert re.match(r'^PING \S+ \(127.0.0.1\)', read_back_text) is not None
  56              assert read_back_text.endswith('ms') is True

lanier-goat-development\dependency\photon\jinja2\utils.py:
  210      for i, word in enumerate(words):
  211:         match = _punctuation_re.match(word)
  212          if match:

  230              if '@' in middle and not middle.startswith('www.') and \
  231:                not ':' in middle and _simple_email_re.match(middle):
  232                  middle = '<a href="mailto:%s">%s</a>' % (middle, middle)

lanier-goat-development\dependency\photon\libfuturize\fixer_util.py:
  485      """
  486:     return bool(re.match(SHEBANG_REGEX, node.prefix))
  487  

  498      """
  499:     return bool(re.match(ENCODING_REGEX, node.prefix))
  500  

lanier-goat-development\dependency\photon\libfuturize\fixes\fix_bytes.py:
  20          if node.type == token.STRING:
  21:             if _literal_re.match(node.value):
  22                  new = node.clone()

lanier-goat-development\dependency\photon\libfuturize\fixes\fix_division_safe.py:
  45          # If it's a leaf, let's see if it's a numeric constant containing a '.'
  46:         return const_re.match(expr.value)
  47      elif isinstance(expr, Node):

lanier-goat-development\dependency\photon\libfuturize\fixes\fix_oldstr_wrap.py:
  31              touch_import_top(u'past.types', u'oldstr', node)
  32:             if _literal_re.match(node.value):
  33                  new = node.clone()

lanier-goat-development\dependency\photon\lxml\_elementpath.py:
  176          return select
  177:     if signature == "-" and not re.match(r"-?\d+$", predicate[0]):
  178          # [tag]

  185          return select
  186:     if signature == ".='" or (signature == "-='" and not re.match(r"-?\d+$", predicate[0])):
  187          # [.='value'] or [tag='value']

lanier-goat-development\dependency\photon\markdown\blockprocessors.py:
  217          # Get indent level
  218:         m = self.INDENT_RE.match(block)
  219          if m:

  309          """ Remove ``>`` from beginning of a line. """
  310:         m = self.RE.match(line)
  311          if line.strip() == ">":

  344      def test(self, parent, block):
  345:         return bool(self.RE.match(block))
  346  

  409          for line in block.split('\n'):
  410:             m = self.CHILD_RE.match(line)
  411              if m:

  416                      INTEGER_RE = re.compile(r'(\d+)')
  417:                     self.STARTSWITH = INTEGER_RE.match(m.group(1)).group()
  418                  # Append to the list
  419                  items.append(m.group(3))
  420:             elif self.INDENT_RE.match(line):
  421                  # This is an indented (possibly nested) item.

  481      def test(self, parent, block):
  482:         return bool(self.RE.match(block))
  483  

lanier-goat-development\dependency\photon\markdown\postprocessors.py:
  93      def isblocklevel(self, html):
  94:         m = re.match(r'^\<\/?([^ >]+)', html)
  95          if m:

lanier-goat-development\dependency\photon\markdown\preprocessors.py:
   94      def _get_left_tag(self, block):
   95:         m = self.left_tag_re.match(block)
   96          if m:

  179          for i, item in enumerate(items):
  180:             if self.left_tag_re.match(item):
  181                  left_tag, left_index, attrs = \

  354              line = lines.pop(0)
  355:             m = self.RE.match(line)
  356              if m:

  361                      # Check next line for title
  362:                     tm = self.TITLE_RE.match(lines[0])
  363                      if tm:

lanier-goat-development\dependency\photon\markdown\extensions\abbr.py:
  49          for line in lines:
  50:             m = ABBR_REF_RE.match(line)
  51              if m:

lanier-goat-development\dependency\photon\markdown\extensions\attr_list.py:
  135                  if elem.tail:
  136:                     m = self.INLINE_RE.match(elem.tail)
  137                      if m:

lanier-goat-development\dependency\photon\markdown\extensions\def_list.py:
  41          block = raw_block[m.end():]
  42:         no_indent = self.NO_INDENT_RE.match(block)
  43          if no_indent:

lanier-goat-development\dependency\photon\markdown\extensions\footnotes.py:
  225          while True:
  226:             m = DEF_RE.match(lines[i])
  227              if m:

  259          def detab(line):
  260:             match = TABBED_RE.match(line)
  261              if match:

  270                      continue
  271:                 elif not blank_line and not DEF_RE.match(line):
  272                      # not tabbed but still part of first par.

lanier-goat-development\dependency\photon\markdown\extensions\meta.py:
  53          key = None
  54:         if lines and BEGIN_RE.match(lines[0]):
  55              lines.pop(0)

  57              line = lines.pop(0)
  58:             m1 = META_RE.match(line)
  59:             if line.strip() == '' or END_RE.match(line):
  60                  break  # blank line or end of YAML header - done

  68              else:
  69:                 m2 = META_MORE_RE.match(line)
  70                  if m2 and key:

lanier-goat-development\dependency\photon\markdown\extensions\toc.py:
  37      while id in ids or not id:
  38:         m = IDCOUNT_RE.match(id)
  39          if m:

lanier-goat-development\dependency\photon\packaging\tags.py:
  263      # uses version strings like "2.20-2014.11"). See gh-3588.
  264:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  265      if not m:

lanier-goat-development\dependency\photon\paramiko\config.py:
  139              # Parse line into key, value
  140:             match = re.match(self.SETTINGS_REGEX, line)
  141              if not match:

lanier-goat-development\dependency\photon\pexpect\pxssh.py:
  373              for line in lines:
  374:                 if not config_has_server and re.match(server_regex, line, re.IGNORECASE):
  375                      config_has_server = True

  380                      break  # we have left the relevant section
  381:                 elif config_has_server and re.match(user_regex, line, re.IGNORECASE):
  382                      server_has_username = True

lanier-goat-development\dependency\photon\pkg_resources\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

lanier-goat-development\dependency\photon\pkg_resources\_vendor\packaging\_manylinux.py:
  210      """
  211:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  212      if not m:

lanier-goat-development\dependency\photon\pkg_resources\_vendor\packaging\_musllinux.py:
  79          return None
  80:     m = re.match(r"Version (\d+)\.(\d+)", lines[1])
  81      if not m:

lanier-goat-development\dependency\photon\pkg_resources\_vendor\packaging\utils.py:
  98      # See PEP 427 for the rules on escaping the project name
  99:     if "__" in name_part or re.match(r"^[\w\d._]*$", name_part, re.UNICODE) is None:
  100          raise InvalidWheelFilename(f"Invalid project name: {filename}")

lanier-goat-development\dependency\photon\psutil\tests\__init__.py:
  1572      elif family == psutil.AF_LINK:
  1573:         assert re.match(r'([a-fA-F0-9]{2}[:|\-]?){6}', addr) is not None, addr
  1574      else:

lanier-goat-development\dependency\photon\py\_path\svnwc.py:
  1176      # example: 2003-10-27 20:43:14 +0100 (Mon, 27 Oct 2003)
  1177:     m = re.match(r'(\d+-\d+-\d+ \d+:\d+:\d+) ([+-]\d+) .*', timestr)
  1178      if not m:

lanier-goat-development\dependency\photon\pycparser\ply\lex.py:
  319              for lexre, lexindexfunc in self.lexre:
  320:                 m = lexre.match(lexdata, lexpos)
  321                  if not m:

  843          for line in lines:
  844:             m = fre.match(line)
  845              if not m:
  846:                 m = sre.match(line)
  847              if m:

lanier-goat-development\dependency\photon\pycparser\ply\yacc.py:
  3009                  linen += 1
  3010:                 m = fre.match(line)
  3011                  if m:

lanier-goat-development\dependency\photon\pyflakes\checker.py:
   593                  tp != tokenize.COMMENT or  # skip non comments
   594:                 not TYPE_COMMENT_RE.match(text) or  # skip non-type comments
   595:                 TYPE_IGNORE_RE.match(text)  # skip ignores
   596          ):

  1051              comment = comment.split(':', 1)[1].strip()
  1052:             func_match = TYPE_FUNC_RE.match(comment)
  1053              if func_match:

lanier-goat-development\dependency\photon\pylint\utils.py:
  1482              value = str(value).strip()
  1483:             if re.match(r"^([\w-]+,)+[\w-]+$", str(value)):
  1484                  separator = "\n " + " " * len(optname)

lanier-goat-development\dependency\photon\pylint\checkers\python3.py:
  50          return False
  51:     if re.match(r"0\d+", literal):
  52          try:

lanier-goat-development\dependency\photon\pylint\checkers\typecheck.py:
  837              # attribute is marked as generated, stop here
  838:             if re.match(pattern, node.attrname):
  839                  return
  840:             if re.match(pattern, node.as_string()):
  841                  return

lanier-goat-development\dependency\photon\pylint\extensions\_check_docs_utils.py:
  780      def _is_section_header(line):
  781:         return bool(re.match(r"\s*-+$", line))
  782  

lanier-goat-development\dependency\photon\pylint\test\input\func_w0405.py:
  11  __revision__ = 0
  12: _re.match('yo', '.*')
  13  

lanier-goat-development\dependency\photon\pyVim\connect.py:
  244     try:
  245:       info = re.match(_rx, host)
  246        if info is not None:

lanier-goat-development\dependency\photon\requests\utils.py:
  102              test = test.replace("?", r".")  # change glob char
  103:             if re.match(test, host, re.I):
  104                  return True

lanier-goat-development\dependency\photon\selenium\webdriver\support\color.py:
  51              def match(self, pattern, str_):
  52:                 self.match_obj = re.match(pattern, str_)
  53                  return self.match_obj

lanier-goat-development\dependency\photon\setuptools\dist.py:
  359      for pkgname in value:
  360:         if not re.match(r'\w+(\.\w+)*', pkgname):
  361              distutils.log.warn(

lanier-goat-development\dependency\photon\setuptools\package_index.py:
  174      parts = basename.split('-')
  175:     if not py_version and any(re.match(r'py\d\.\d$', p) for p in parts[2:]):
  176          # it is a bdist_dumb, not an sdist -- bail out

lanier-goat-development\dependency\photon\setuptools\sandbox.py:
  477          pattern_matches = (
  478:             re.match(pattern, filepath) for pattern in self._exception_patterns
  479          )

lanier-goat-development\dependency\photon\setuptools\_distutils\ccompiler.py:
  958      for pattern, compiler in _default_compilers:
  959:         if re.match(pattern, platform) is not None or \
  960:            re.match(pattern, osname) is not None:
  961              return compiler

lanier-goat-development\dependency\photon\setuptools\_distutils\dist.py:
  531          command = args[0]
  532:         if not command_re.match(command):
  533              raise SystemExit("invalid command name '%s'" % command)

lanier-goat-development\dependency\photon\setuptools\_distutils\fancy_getopt.py:
  199              # '='.
  200:             if not longopt_re.match(long):
  201                  raise DistutilsGetoptError(

lanier-goat-development\dependency\photon\setuptools\_distutils\util.py:
   88          rel_re = re.compile (r'[\d.]+', re.ASCII)
   89:         m = rel_re.match(release)
   90          if m:

  317      while s:
  318:         m = _wordchars_re.match(s, pos)
  319          end = m.end()

  335              if s[end] == "'":           # slurp singly-quoted string
  336:                 m = _squote_re.match(s, end)
  337              elif s[end] == '"':         # slurp doubly-quoted string
  338:                 m = _dquote_re.match(s, end)
  339              else:

lanier-goat-development\dependency\photon\setuptools\_distutils\version.py:
  154      def parse (self, vstring):
  155:         match = self.version_re.match(vstring)
  156          if not match:

lanier-goat-development\dependency\photon\setuptools\_distutils\command\build_ext.py:
  371              if not (isinstance(ext_name, str) and
  372:                     extension_name_re.match(ext_name)):
  373                  raise DistutilsSetupError(

lanier-goat-development\dependency\photon\setuptools\_distutils\command\build_scripts.py:
  88  
  89:                 match = first_line_re.match(first_line)
  90                  if match:

lanier-goat-development\dependency\photon\setuptools\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

lanier-goat-development\dependency\photon\setuptools\_vendor\packaging\_manylinux.py:
  210      """
  211:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  212      if not m:

lanier-goat-development\dependency\photon\setuptools\_vendor\packaging\_musllinux.py:
  79          return None
  80:     m = re.match(r"Version (\d+)\.(\d+)", lines[1])
  81      if not m:

lanier-goat-development\dependency\photon\setuptools\_vendor\packaging\utils.py:
  98      # See PEP 427 for the rules on escaping the project name
  99:     if "__" in name_part or re.match(r"^[\w\d._]*$", name_part, re.UNICODE) is None:
  100          raise InvalidWheelFilename(f"Invalid project name: {filename}")

lanier-goat-development\dependency\photon\setuptools\command\bdist_egg.py:
  247                      pattern = r'(?P<name>.+)\.(?P<magic>[^.]+)\.pyc'
  248:                     m = re.match(pattern, name)
  249                      path_new = os.path.join(

lanier-goat-development\dependency\photon\setuptools\command\egg_info.py:
  574          """
  575:         return re.match(r"standard file .*not found", msg)
  576  

  747              for line in f:
  748:                 match = re.match(r"Version:.*-r(\d+)\s*$", line)
  749                  if match:

lanier-goat-development\dependency\photon\urllib3\util\retry.py:
  372          # Whitespace: https://tools.ietf.org/html/rfc7230#section-3.2.4
  373:         if re.match(r"^\s*[0-9]+\s*$", retry_after):
  374              seconds = int(retry_after)

lanier-goat-development\dependency\photon\urllib3\util\ssl_.py:
  466          hostname = hostname.decode("ascii")
  467:     return bool(IPV4_RE.match(hostname) or BRACELESS_IPV6_ADDRZ_RE.match(hostname))
  468  

lanier-goat-development\dependency\photon\urllib3\util\url.py:
  279          if scheme in NORMALIZABLE_SCHEMES:
  280:             is_ipv6 = IPV6_ADDRZ_RE.match(host)
  281              if is_ipv6:

  294                      return host.lower()
  295:             elif not IPV4_RE.match(host):
  296                  return six.ensure_str(

  321      """Percent-encodes a request target so that there are no invalid characters"""
  322:     path, query = TARGET_RE.match(target).groups()
  323      target = _encode_invalid_chars(path, PATH_CHARS)

  360      try:
  361:         scheme, authority, path, query, fragment = URI_RE.match(url).groups()
  362          normalize_uri = scheme is None or scheme.lower() in NORMALIZABLE_SCHEMES

  369              auth = auth or None
  370:             host, port = _HOST_PORT_RE.match(host_port).groups()
  371              if auth and normalize_uri:

lanier-goat-development\dependency\photon\wavefront_sdk\common\application_tags.py:
  85          for key in os.environ:
  86:             if re.match(pattern, key, re.IGNORECASE):
  87                  value = os.environ[key]

lanier-goat-development\dependency\photon\werkzeug\formparser.py:
  275      """Checks if the string given is a valid multipart boundary."""
  276:     return _multipart_boundary_re.match(boundary) is not None
  277  

lanier-goat-development\dependency\photon\werkzeug\http.py:
  414          while rest:
  415:             optmatch = _option_header_piece_re.match(rest)
  416              if not optmatch:

  758      while pos < end:
  759:         match = _etag_re.match(value, pos)
  760          if match is None:

lanier-goat-development\dependency\photon\werkzeug\urls.py:
  457      i = url.find(s(":"))
  458:     if i > 0 and _scheme_re.match(to_native(url[:i], errors="replace")):
  459          # make sure "iri" is not actually a port number (in which case

lanier-goat-development\dependency\photon\werkzeug\contrib\sessions.py:
  169          """Check if a key has the correct format."""
  170:         return _sha1_re.match(key) is not None
  171  

  307                  continue
  308:             match = filename_re.match(filename)
  309              if match is not None:

lanier-goat-development\dependency\photon\werkzeug\debug\tbtools.py:
  531              while lineno > 0:
  532:                 if _funcdef_re.match(lines[lineno].code):
  533                      break

lanier-goat-development\dimension\dim_multicluster_dataplane.py:
  36      pattern = r'.*_([\d\.]+\d)\.(\d+)-esx([\d]+).*'
  37:     matcher = re.match(pattern, old_id_value)
  38      component_version = F'{matcher.group(1)}-{".".join(list(matcher.group(3)))}.{matcher.group(2)}'

lanier-goat-development\eust_lite\tests\vcqe_eust.py:
  144              for line in open(result_log_path, "r"):
  145:                 match = re.match(
  146                      r'^Test:.*Run:\s*(\d)\s*Pass:\s*(\d) '

lanier-goat-development\fractal\common\fractal_utils.py:
  800                  # If its not a numeric result code, it says None on submit
  801:                 while (re.match('[^0-9]+', str(pid_exitcode))):
  802                      time.sleep(5)

  808                      # Look for non-zero code to fail
  809:                     elif (re.match('[1-9]+', str(pid_exitcode))):
  810                          break

lanier-goat-development\fractal\test\fvt\vcqe.py:
  120              for line in open(result_log_path, "r"):
  121:                 match = re.match(
  122                      r'^Test:.*Run:\s*(\d)\s*Pass:\s*(\d) '

lanier-goat-development\framework\testmanager.py:
  453          # test_args['networks'] = [net for net in dc.network
  454:         #                          if re.match(r'net-vm-pg-', net.name)]
  455          # if not test_args['networks']:
  456          #     test_args['networks'] = [net for net in dc.network
  457:         #                              if re.match(r'VM Network', net.name)]
  458          # self.log.info('update args.vsanDatastore')

lanier-goat-development\framework\testrst.py:
   99              for key in setup_info_json:
  100:                 if re.match('esx', key, re.I):
  101                      esx = setup_info_json[key]

lanier-goat-development\gcliutils\util.py:
  135              while True:
  136:                 if not re.match(r'([\w\d]{5}-){4}[\w\d]{5}', license_key):
  137                      msg = "License is not in the correct format " \

  174              while True:
  175:                 if not re.match(r'([\w\d]{5}-){4}[\w\d]{5}', license_key):
  176                      msg = "License is not in the correct format " \

  198              while True:
  199:                 if not re.match(r'([\w\d]{5}-){4}[\w\d]{5}', license_key):
  200                      msg = "License is not in the correct format " \

lanier-goat-development\interop\interarc_vcf_bringup\host_imaging.py:
  65      via_mgmt_ip = via_ip
  66:     if not re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", via_mgmt_ip):
  67          util = VcfUtil(args)

  75          via_mgmt_ip = via_ip
  76:         if not re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", via_mgmt_ip):
  77              raise AssertionError("No ipv4 address even after restarting dhcpd")

lanier-goat-development\interop\setup\install\install_psc.py:
  53                                     vc_version + '-' + buildnumber + '.iso /' + self.directoryname
  54:         matching = re.match("(6.7.*)", self.vc_version)
  55          if (matching):

  59  
  60:         matching = re.match("(6.5.*)", self.vc_version)
  61          if (matching):

  65  
  66:         matching = re.match("(6.0.*)", self.vc_version)
  67          if (matching):

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_dedupe_comp_migrate_out_from_vsan_edge_dlr.py:
  414          for ip in ip_list:
  415:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  416                  if ip != vm_guest_ip:

  448          for ip in ip_list:
  449:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  450                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_dedupe_comp_migrate_out_from_vsan_gi.py:
  430          for ip in ip_list:
  431:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  432                  if ip != vm_guest_ip:

  464          for ip in ip_list:
  465:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  466                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_dedupe_comp_migrate_out_from_vsan_nsx_ctrl.py:
  354          for ip in ip_list:
  355:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  356                  if ip != vm_guest_ip:

  388          for ip in ip_list:
  389:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  390                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_dedupe_comp_migrate_out_from_vsan_nsx_mgr.py:
  352          for ip in ip_list:
  353:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  354                  if ip != vm_guest_ip:

  386          for ip in ip_list:
  387:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  388                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_guest_introspection_migrate_vsan.py:
  426          for ip in ip_list:
  427:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  428                  if ip != vm_guest_ip:

  460          for ip in ip_list:
  461:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  462                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_guest_introspection_on_vsan.py:
  427          for ip in ip_list:
  428:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  429                  if ip != vm_guest_ip:

  461          for ip in ip_list:
  462:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  463                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_host_reboot_nsx_controllers.py:
  512          for ip in ip_list:
  513:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  514                  if ip != vm_guest_ip:

  546          for ip in ip_list:
  547:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  548                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_host_reboot_nsx_dlr.py:
  521          for ip in ip_list:
  522:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  523                  if ip != vm_guest_ip:

  555          for ip in ip_list:
  556:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  557                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_host_reboot_nsx_edge.py:
  527          for ip in ip_list:
  528:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  529                  if ip != vm_guest_ip:

  561          for ip in ip_list:
  562:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  563                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_host_reboot_nsx_manager.py:
  480          for ip in ip_list:
  481:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  482                  if ip != vm_guest_ip:

  514          for ip in ip_list:
  515:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  516                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_nsx_components_on_vsan.py:
  388          for ip in ip_list:
  389:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  390                  if ip != vm_guest_ip:

  422          for ip in ip_list:
  423:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  424                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_nsx_controller_migrate_on_vsan.py:
  358          for ip in ip_list:
  359:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  360                  if ip != vm_guest_ip:

  392          for ip in ip_list:
  393:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  394                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_nsx_dlr_migrate_on_vsan.py:
  414          for ip in ip_list:
  415:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  416                  if ip != vm_guest_ip:

  448          for ip in ip_list:
  449:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  450                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_nsx_edge_dlr_reboot_on_vsan.py:
  390          for ip in ip_list:
  391:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  392                  if ip != vm_guest_ip:

  424          for ip in ip_list:
  425:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  426                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_nsx_edge_migrate_on_vsan.py:
  410          for ip in ip_list:
  411:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  412                  if ip != vm_guest_ip:

  444          for ip in ip_list:
  445:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  446                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_nsx_manager_migrate_on_vsan.py:
  356          for ip in ip_list:
  357:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  358                  if ip != vm_guest_ip:

  390          for ip in ip_list:
  391:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  392                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx63_vsan\interop_nsx_vsan_snapshot.py:
  391          for ip in ip_list:
  392:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  393                  if ip != vm_guest_ip:

  425          for ip in ip_list:
  426:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  427                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_dedupe_comp_migrate_out_from_vsan_edge_dlr.py:
  416              for ip in ip_list:
  417:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  418                      if ip != vm_guest_ip:

  450              for ip in ip_list:
  451:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  452                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_dedupe_comp_migrate_out_from_vsan_gi.py:
  439              for ip in ip_list:
  440:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  441                      if ip != vm_guest_ip:

  473              for ip in ip_list:
  474:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  475                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_dedupe_comp_migrate_out_from_vsan_nsx_ctrl.py:
  357              for ip in ip_list:
  358:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  359                      if ip != vm_guest_ip:

  391              for ip in ip_list:
  392:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  393                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_dedupe_comp_migrate_out_from_vsan_nsx_mgr.py:
  355              for ip in ip_list:
  356:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  357                      if ip != vm_guest_ip:

  389              for ip in ip_list:
  390:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  391                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_guest_introspection_migrate_vsan.py:
  430              for ip in ip_list:
  431:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  432                      if ip != vm_guest_ip:

  464              for ip in ip_list:
  465:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  466                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_guest_introspection_on_vsan.py:
  430              for ip in ip_list:
  431:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  432                      if ip != vm_guest_ip:

  464              for ip in ip_list:
  465:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  466                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_host_reboot_nsx_controllers.py:
  476              for ip in ip_list:
  477:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  478                      if ip != vm_guest_ip:

  510              for ip in ip_list:
  511:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  512                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_host_reboot_nsx_dlr.py:
  456              for ip in ip_list:
  457:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  458                      if ip != vm_guest_ip:

  490              for ip in ip_list:
  491:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  492                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_host_reboot_nsx_edge.py:
  462              for ip in ip_list:
  463:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  464                      if ip != vm_guest_ip:

  496              for ip in ip_list:
  497:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  498                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_host_reboot_nsx_manager.py:
  514              for ip in ip_list:
  515:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  516                      if ip != vm_guest_ip:

  548              for ip in ip_list:
  549:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  550                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_nsx_components_on_vsan.py:
  391              for ip in ip_list:
  392:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  393                      if ip != vm_guest_ip:

  425              for ip in ip_list:
  426:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  427                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_nsx_controller_migrate_on_vsan.py:
  361              for ip in ip_list:
  362:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  363                      if ip != vm_guest_ip:

  395              for ip in ip_list:
  396:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  397                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_nsx_dlr_migrate_on_vsan.py:
  418              for ip in ip_list:
  419:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  420                      if ip != vm_guest_ip:

  452              for ip in ip_list:
  453:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  454                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_nsx_edge_dlr_reboot_on_vsan.py:
  393              for ip in ip_list:
  394:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  395                      if ip != vm_guest_ip:

  427              for ip in ip_list:
  428:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  429                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_nsx_edge_migrate_on_vsan.py:
  414              for ip in ip_list:
  415:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  416                      if ip != vm_guest_ip:

  448              for ip in ip_list:
  449:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  450                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_nsx_manager_migrate_on_vsan.py:
  359              for ip in ip_list:
  360:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  361                      if ip != vm_guest_ip:

  393              for ip in ip_list:
  394:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  395                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsan\nsx64_vsan\interop_nsx_vsan_snapshot.py:
  392              for ip in ip_list:
  393:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  394                      if ip != vm_guest_ip:

  426              for ip in ip_list:
  427:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  428                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\jdeshpande\interop_dlr_edge_deletion.py:
  272          for ip in ip_list:
  273:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  274                  if ip != vm_guest_ip:

  306          for ip in ip_list:
  307:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  308                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\jdeshpande\interop_edge_ha_with_ft.py:
  236          for ip in ip_list:
  237:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  238                  if ip != vm_guest_ip:

  270          for ip in ip_list:
  271:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  272                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\jdeshpande\interop_exclusion_list_with_ft.py:
  265          for ip in ip_list:
  266:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  267                  if ip != vm_guest_ip:

  299          for ip in ip_list:
  300:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  301                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\jdeshpande\interop_guest_introspection_eam_restart.py:
  351          for ip in ip_list:
  352:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  353                  if ip != vm_guest_ip:

  385          for ip in ip_list:
  386:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  387                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\jdeshpande\interop_nsx_ctrl_xvmotion.py:
  365          for ip in ip_list:
  366:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  367                  if ip != vm_guest_ip:

  399          for ip in ip_list:
  400:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  401                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\jdeshpande\interop_security_policy_with_vm_rename.py:
  168          for ip in ip_list:
  169:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  170                  if ip != vm_guest_ip:

  201          for ip in ip_list:
  202:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  203                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\malempatin\interop_dhcp_edge_and_dlr_with_vms.py:
  293          for ip in ip_list:
  294:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  295                  if ip != vm_guest_ip:

  333          for ip in ip_list:
  334:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  335                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\Enable_Disable_Re_Enable_DRS_On_NSX_Cluster.py:
  228              for ip in ip_list:
  229:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  230                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\host_maintenance_mode_nsx_cluster.py:
  235              for ip in ip_list:
  236:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  237                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\host_maintenance_mode_nsx_controller.py:
  259              for ip in ip_list:
  260:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  261                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_EMM.py:
  210              for ip in ip_list:
  211:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  212                              ip):

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_svmotion.py:
  206              for ip in ip_list:
  207:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  208                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_vMotion_DRS.py:
  222              for ip in ip_list:
  223:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  224                      if ip != vm_guest_ip:

  526          for ip1 in ip_list1:
  527:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip1):
  528                  if ip1 != vm_guest_ip1:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_vmotion.py:
  200              for ip in ip_list:
  201:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  202                              ip):

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_xvmotion.py:
  235              for ip in ip_list:
  236:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  237                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dfw_vm_clone.py:
  217              for ip in ip_list:
  218:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  219                      if ip != vm_guest_ip:

  338          for ip in ip_list:
  339:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  340                  if ip != vm_guest_ip:

  446          for ip in ip_list:
  447:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  448                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dfw_vmnw_change.py:
  220              for ip in ip_list:
  221:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  222                      if ip != vm_guest_ip:

  396          for ip in ip_list:
  397:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  398                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dlr_ha_emm.py:
  321              for ip in ip_list:
  322:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  323                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dlr_ha_svmotion.py:
  319              for ip in ip_list:
  320:                 if re.match(
  321                      "^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dlr_ha_vmotion.py:
  321              for ip in ip_list:
  322:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  323                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_dlr_ha_xvmotion.py:
  320              for ip in ip_list:
  321:                 if re.match(
  322                      "^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mbiradar\interop_nsx_ha_host_reboot.py:
  269              for ip in ip_list:
  270:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  271                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mrangdale\interop_l2bridging_vmclone.py:
  307          src1 = vmObj.get_guest_ip(clone_vm_ref)
  308:         if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", src1) is \
  309                  None:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mrangdale\interop_vc_hostname_change_nsxp_ip.py:
  309          for ip in ip_list:
  310:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  311                  if ip != vm_guest_ip:

  343          for ip in ip_list:
  344:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  345                  if ip != vm_guest_ip:

  565          for ip in ip_list:
  566:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  567                  if ip != vm_guest_ip:

  599          for ip in ip_list:
  600:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  601                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mrangdale\interop_vc_hostname_change.py:
  291          for ip in ip_list:
  292:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  293                  if ip != vm_guest_ip:

  325          for ip in ip_list:
  326:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  327                  if ip != vm_guest_ip:

  593          for ip in ip_list:
  594:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  595                  if ip != vm_guest_ip:

  632          for ip in ip_list:
  633:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  634                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mrangdale\interop_vc_service_vpx_restart.py:
  354          for ip in ip_list:
  355:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  356                  if ip != vm_guest_ip:

  384          for ip in ip_list:
  385:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  386                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_dfw_drs.py:
  181          for ip in ip_list:
  182:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  183                  if ip != vm_guest_ip:

  221          for ip in ip_list:
  222:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  223                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_dlr_dynamic_routing_drs.py:
  292          for ip in ip_list:
  293:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  294                  if ip != vm_guest_ip:

  332          for ip in ip_list:
  333:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  334                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_dlr_eam_restart.py:
  301          for ip in ip_list:
  302:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  303                  if ip != vm_guest_ip:

  335          for ip in ip_list:
  336:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_dlr_ha_drs.py:
  295          for ip in ip_list:
  296:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                  if ip != vm_guest_ip:

  335          for ip in ip_list:
  336:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_dlr_ha_vsphere_ha.py:
  347          for ip in ip_list:
  348:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  349                  if ip != vm_guest_ip:

  387          for ip in ip_list:
  388:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  389                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_bgp_routing_edge_ft.py:
  303          for ip in ip_list:
  304:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  305                  if ip != vm_guest_ip:

  343          for ip in ip_list:
  344:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  345                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_bgp_routing_edge_svMotion.py:
  295          for ip in ip_list:
  296:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                  if ip != vm_guest_ip:

  335          for ip in ip_list:
  336:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_bgp_routing_edge_vMotion.py:
  300          for ip in ip_list:
  301:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  302                  if ip != vm_guest_ip:

  340          for ip in ip_list:
  341:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  342                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_bgp_routing_edge_xvMotion.py:
  295          for ip in ip_list:
  296:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                  if ip != vm_guest_ip:

  335          for ip in ip_list:
  336:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_bgp_routing_emm.py:
  301          for ip in ip_list:
  302:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  303                  if ip != vm_guest_ip:

  341          for ip in ip_list:
  342:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  343                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_bgp_routing_vspere_ha.py:
  314          for ip in ip_list:
  315:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  316                  if ip != vm_guest_ip:

  354          for ip in ip_list:
  355:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  356                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_edge_ft.py:
  315          for ip in ip_list:
  316:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  317                  if ip != vm_guest_ip:

  355          for ip in ip_list:
  356:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  357                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_edge_svMotion.py:
  300          for ip in ip_list:
  301:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  302                  if ip != vm_guest_ip:

  340          for ip in ip_list:
  341:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  342                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_edge_vMotion.py:
  307          for ip in ip_list:
  308:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  309                  if ip != vm_guest_ip:

  347          for ip in ip_list:
  348:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  349                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_edge_xvMotion.py:
  300          for ip in ip_list:
  301:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  302                  if ip != vm_guest_ip:

  340          for ip in ip_list:
  341:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  342                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_emm.py:
  301          for ip in ip_list:
  302:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  303                  if ip != vm_guest_ip:

  341          for ip in ip_list:
  342:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  343                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_vspere_ha.py:
  314          for ip in ip_list:
  315:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  316                  if ip != vm_guest_ip:

  354          for ip in ip_list:
  355:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  356                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_edge_ft.py:
  307          for ip in ip_list:
  308:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  309                  if ip != vm_guest_ip:

  347          for ip in ip_list:
  348:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  349                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_edge_svMotion.py:
  292          for ip in ip_list:
  293:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  294                  if ip != vm_guest_ip:

  332          for ip in ip_list:
  333:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  334                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_edge_vMotion.py:
  299          for ip in ip_list:
  300:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  301                  if ip != vm_guest_ip:

  339          for ip in ip_list:
  340:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  341                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_edge_xvMotion.py:
  292          for ip in ip_list:
  293:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  294                  if ip != vm_guest_ip:

  332          for ip in ip_list:
  333:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  334                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_emm.py:
  293          for ip in ip_list:
  294:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  295                  if ip != vm_guest_ip:

  333          for ip in ip_list:
  334:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  335                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_vspere_ha.py:
  306          for ip in ip_list:
  307:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  308                  if ip != vm_guest_ip:

  346          for ip in ip_list:
  347:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  348                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dynamic_routing_drs.py:
  300          for ip in ip_list:
  301:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  302                  if ip != vm_guest_ip:

  340          for ip in ip_list:
  341:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  342                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dynamic_routing_edge_ft.py:
  295          for ip in ip_list:
  296:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                  if ip != vm_guest_ip:

  335          for ip in ip_list:
  336:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dynamic_routing_edge_svMotion.py:
  287          for ip in ip_list:
  288:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  289                  if ip != vm_guest_ip:

  327          for ip in ip_list:
  328:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  329                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dynamic_routing_edge_vMotion.py:
  292          for ip in ip_list:
  293:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  294                  if ip != vm_guest_ip:

  332          for ip in ip_list:
  333:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  334                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dynamic_routing_edge_xvMotion.py:
  287          for ip in ip_list:
  288:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  289                  if ip != vm_guest_ip:

  327          for ip in ip_list:
  328:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  329                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dynamic_routing_emm.py:
  293          for ip in ip_list:
  294:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  295                  if ip != vm_guest_ip:

  333          for ip in ip_list:
  334:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  335                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_dynamic_routing_vspere_ha.py:
  306          for ip in ip_list:
  307:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  308                  if ip != vm_guest_ip:

  346          for ip in ip_list:
  347:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  348                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_drs.py:
  227          for ip in ip_list:
  228:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  229                  if ip != vm_guest_ip:

  267          for ip in ip_list:
  268:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  269                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_edge_svMotion.py:
  224          for ip in ip_list:
  225:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  226                  if ip != vm_guest_ip:

  261          for ip in ip_list:
  262:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  263                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_edge_vMotion.py:
  211          for ip in ip_list:
  212:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  213                  if ip != vm_guest_ip:

  244          for ip in ip_list:
  245:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  246                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_edge_xvmotion.py:
  215          for ip in ip_list:
  216:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  217                  if ip != vm_guest_ip:

  248          for ip in ip_list:
  249:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  250                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_emm.py:
  246          for ip in ip_list:
  247:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  248                  if ip != vm_guest_ip:

  280          for ip in ip_list:
  281:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  282                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_vm_clone.py:
  217          for ip in ip_list:
  218:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  219                  if ip != vm_guest_ip:

  252          for ip in ip_list:
  253:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  254                  if ip != vm_guest_ip:

  387      for ip in ip_list:
  388:         if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  389              if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_vm_ft.py:
  210          for ip in ip_list:
  211:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  212                  if ip != vm_guest_ip:

  243          for ip in ip_list:
  244:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  245                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_vm_network_change.py:
  255          for ip in ip_list:
  256:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  257                  if ip != vm_guest_ip:

  288          for ip in ip_list:
  289:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  290                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_vm_traffic.py:
  219          for ip in ip_list:
  220:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  221                  if ip != vm_guest_ip:

  252          for ip in ip_list:
  253:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  254                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_firewall_vsphere_ha.py:
  256          for ip in ip_list:
  257:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  258                  if ip != vm_guest_ip:

  290          for ip in ip_list:
  291:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  292                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_ha_drs.py:
  227          for ip in ip_list:
  228:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  229                  if ip != vm_guest_ip:

  267          for ip in ip_list:
  268:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  269                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_ha_edge_vmotion.py:
  224          for ip in ip_list:
  225:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  226                  if ip != vm_guest_ip:

  258          for ip in ip_list:
  259:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  260                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_ha_emm.py:
  228          for ip in ip_list:
  229:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  230                  if ip != vm_guest_ip:

  262          for ip in ip_list:
  263:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  264                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_ha_vsphere_ha.py:
  264          for ip in ip_list:
  265:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  266                  if ip != vm_guest_ip:

  298          for ip in ip_list:
  299:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  300                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_lb_edge_drs.py:
  185          for ip in ip_list:
  186:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  187                  if ip != vm_guest_ip:

  225          for ip in ip_list:
  226:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  227                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_lb_edge_emm.py:
  185          for ip in ip_list:
  186:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  187                  if ip != vm_guest_ip:

  225          for ip in ip_list:
  226:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  227                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_lb_edge_svMotion.py:
  186          for ip in ip_list:
  187:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  188                  if ip != vm_guest_ip:

  226          for ip in ip_list:
  227:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  228                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_lb_edge_vMotion.py:
  185          for ip in ip_list:
  186:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  187                  if ip != vm_guest_ip:

  225          for ip in ip_list:
  226:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  227                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_lb_edge_xvMotion.py:
  185          for ip in ip_list:
  186:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  187                  if ip != vm_guest_ip:

  225          for ip in ip_list:
  226:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  227                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_lb_vsphere_ha.py:
  201          for ip in ip_list:
  202:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  203                  if ip != vm_guest_ip:

  241          for ip in ip_list:
  242:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  243                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_redeploy_emm.py:
  232          for ip in ip_list:
  233:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  234                  if ip != vm_guest_ip:

  266          for ip in ip_list:
  267:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  268                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_edge_rename_xvMotion.py:
  236          for ip in ip_list:
  237:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  238                  if ip != vm_guest_ip:

  270          for ip in ip_list:
  271:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  272                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_flow_monitor_vm_drs.py:
  174          for ip in ip_list:
  175:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  176                  if ip != vm_guest_ip:

  214          for ip in ip_list:
  215:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  216                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_flow_monitor_vm_emm.py:
  176          for ip in ip_list:
  177:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  178                  if ip != vm_guest_ip:

  216          for ip in ip_list:
  217:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  218                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_flow_monitor_vm_svmotion.py:
  174          for ip in ip_list:
  175:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  176                  if ip != vm_guest_ip:

  214          for ip in ip_list:
  215:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  216                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_flow_monitor_vm_vmotion.py:
  174          for ip in ip_list:
  175:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  176                  if ip != vm_guest_ip:

  214          for ip in ip_list:
  215:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  216                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_flow_monitor_vm_xvmotion.py:
  174          for ip in ip_list:
  175:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  176                  if ip != vm_guest_ip:

  214          for ip in ip_list:
  215:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  216                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_nsx_controller_drs.py:
  181          for ip in ip_list:
  182:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  183                  if ip != vm_guest_ip:

  221          for ip in ip_list:
  222:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  223                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_nsx_host_reboot.py:
  251          for ip in ip_list:
  252:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  253                  if ip != vm_guest_ip:

  285          for ip in ip_list:
  286:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  287                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_nsx_manager_backup.py:
  315          for ip in ip_list:
  316:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  317                  if ip != vm_guest_ip:

  349          for ip in ip_list:
  350:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  351                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\msrinivasssa\interop_security_policy_vm_drs.py:
  178          for ip in ip_list:
  179:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  180                  if ip != vm_guest_ip:

  218          for ip in ip_list:
  219:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  220                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\jdeshpande\interop_dlr_edge_deletion.py:
  274              for ip in ip_list:
  275:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  276                      if ip != vm_guest_ip:

  308              for ip in ip_list:
  309:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  310                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\jdeshpande\interop_edge_ha_with_ft.py:
  238              for ip in ip_list:
  239:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  240                      if ip != vm_guest_ip:

  272              for ip in ip_list:
  273:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  274                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\jdeshpande\interop_exclusion_list_with_ft.py:
  267              for ip in ip_list:
  268:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  269                      if ip != vm_guest_ip:

  301              for ip in ip_list:
  302:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  303                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\jdeshpande\interop_guest_introspection_eam_restart.py:
  352              for ip in ip_list:
  353:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  354                      if ip != vm_guest_ip:

  386              for ip in ip_list:
  387:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  388                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\jdeshpande\interop_nsx_ctrl_xvmotion.py:
  367              for ip in ip_list:
  368:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  369                      if ip != vm_guest_ip:

  401              for ip in ip_list:
  402:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  403                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\jdeshpande\interop_security_policy_with_vm_rename.py:
  170              for ip in ip_list:
  171:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  172                      if ip != vm_guest_ip:

  203              for ip in ip_list:
  204:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  205                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\malempatin\interop_dhcp_edge_and_dlr_with_vms.py:
  295              for ip in ip_list:
  296:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                      if ip != vm_guest_ip:

  335              for ip in ip_list:
  336:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\Enable_Disable_Re_Enable_DRS_On_NSX_Cluster.py:
  234              for ip in ip_list:
  235:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  236                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\host_maintenance_mode_nsx_cluster.py:
  239              for ip in ip_list:
  240:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  241                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\host_maintenance_mode_nsx_controller.py:
  263              for ip in ip_list:
  264:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  265                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_EMM.py:
  215              for ip in ip_list:
  216:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  217                              ip):

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_svmotion.py:
  211              for ip in ip_list:
  212:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  213                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_vMotion_DRS.py:
  228              for ip in ip_list:
  229:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  230                      if ip != vm_guest_ip:

  537          for ip1 in ip_list1:
  538:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip1):
  539                  if ip1 != vm_guest_ip1:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_vmotion.py:
  205              for ip in ip_list:
  206:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  207                              ip):

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dfw_rule_l3_validation_with_xvmotion.py:
  240              for ip in ip_list:
  241:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  242                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dfw_vm_clone.py:
  218              for ip in ip_list:
  219:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  220                      if ip != vm_guest_ip:

  339          for ip in ip_list:
  340:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  341                  if ip != vm_guest_ip:

  447          for ip in ip_list:
  448:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  449                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dfw_vmnw_change.py:
  219              for ip in ip_list:
  220:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  221                      if ip != vm_guest_ip:

  395          for ip in ip_list:
  396:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  397                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dlr_ha_emm.py:
  320              for ip in ip_list:
  321:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  322                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dlr_ha_svmotion.py:
  319              for ip in ip_list:
  320:                 if re.match(
  321                      "^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dlr_ha_vmotion.py:
  320              for ip in ip_list:
  321:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  322                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_dlr_ha_xvmotion.py:
  320              for ip in ip_list:
  321:                 if re.match(
  322                      "^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mbiradar\interop_nsx_ha_host_reboot.py:
  277              for ip in ip_list:
  278:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  279                              ip):

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mrangdale\interop_l2bridging_vmclone.py:
  307          #     src1 = vmObj.get_guest_ip(clone_vm_ref)
  308:         #     if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", src1) is \
  309          #             None:

  320              args.rt.comment("VM IP is :{}".format(src1))
  321:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  322                          src1):

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mrangdale\interop_vc_hostname_change_nsxp_ip.py:
  311              for ip in ip_list:
  312:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  313                      if ip != vm_guest_ip:

  345              for ip in ip_list:
  346:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  347                      if ip != vm_guest_ip:

  577              for ip in ip_list:
  578:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  579                      if ip != vm_guest_ip:

  611              for ip in ip_list:
  612:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  613                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mrangdale\interop_vc_hostname_change.py:
  293              for ip in ip_list:
  294:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  295                      if ip != vm_guest_ip:

  327              for ip in ip_list:
  328:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  329                      if ip != vm_guest_ip:

  605              for ip in ip_list:
  606:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  607                      if ip != vm_guest_ip:

  644              for ip in ip_list:
  645:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  646                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mrangdale\interop_vc_service_vpx_restart.py:
  354              for ip in ip_list:
  355:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  356                      if ip != vm_guest_ip:

  384              for ip in ip_list:
  385:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  386                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_dfw_drs.py:
  184              for ip in ip_list:
  185:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  186                      if ip != vm_guest_ip:

  224              for ip in ip_list:
  225:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  226                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_dlr_dynamic_routing_drs.py:
  295              for ip in ip_list:
  296:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                      if ip != vm_guest_ip:

  335              for ip in ip_list:
  336:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_dlr_eam_restart.py:
  302              for ip in ip_list:
  303:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  304                      if ip != vm_guest_ip:

  336              for ip in ip_list:
  337:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  338                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_dlr_ha_drs.py:
  298              for ip in ip_list:
  299:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  300                      if ip != vm_guest_ip:

  338              for ip in ip_list:
  339:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  340                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_dlr_ha_vsphere_ha.py:
  354              for ip in ip_list:
  355:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  356                      if ip != vm_guest_ip:

  394              for ip in ip_list:
  395:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  396                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_bgp_routing_edge_ft.py:
  299              for ip in ip_list:
  300:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  301                      if ip != vm_guest_ip:

  339              for ip in ip_list:
  340:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  341                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_bgp_routing_edge_svMotion.py:
  298              for ip in ip_list:
  299:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  300                      if ip != vm_guest_ip:

  338              for ip in ip_list:
  339:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  340                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_bgp_routing_edge_vMotion.py:
  296              for ip in ip_list:
  297:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  298                      if ip != vm_guest_ip:

  336              for ip in ip_list:
  337:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  338                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_bgp_routing_edge_xvMotion.py:
  298              for ip in ip_list:
  299:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  300                      if ip != vm_guest_ip:

  338              for ip in ip_list:
  339:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  340                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_bgp_routing_emm.py:
  297              for ip in ip_list:
  298:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  299                      if ip != vm_guest_ip:

  337              for ip in ip_list:
  338:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  339                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_bgp_routing_vspere_ha.py:
  316              for ip in ip_list:
  317:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  318                      if ip != vm_guest_ip:

  356              for ip in ip_list:
  357:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  358                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_edge_ft.py:
  317              for ip in ip_list:
  318:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  319                      if ip != vm_guest_ip:

  357              for ip in ip_list:
  358:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  359                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_edge_svMotion.py:
  304              for ip in ip_list:
  305:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  306                      if ip != vm_guest_ip:

  344              for ip in ip_list:
  345:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  346                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_edge_vMotion.py:
  303              for ip in ip_list:
  304:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  305                      if ip != vm_guest_ip:

  343              for ip in ip_list:
  344:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  345                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_edge_xvMotion.py:
  302              for ip in ip_list:
  303:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  304                      if ip != vm_guest_ip:

  342              for ip in ip_list:
  343:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  344                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_emm.py:
  303              for ip in ip_list:
  304:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  305                      if ip != vm_guest_ip:

  343              for ip in ip_list:
  344:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  345                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_bgp_routing_vspere_ha.py:
  322              for ip in ip_list:
  323:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  324                      if ip != vm_guest_ip:

  362              for ip in ip_list:
  363:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  364                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_edge_ft.py:
  309              for ip in ip_list:
  310:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  311                      if ip != vm_guest_ip:

  349              for ip in ip_list:
  350:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  351                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_edge_svMotion.py:
  295              for ip in ip_list:
  296:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                      if ip != vm_guest_ip:

  335              for ip in ip_list:
  336:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_edge_vMotion.py:
  295              for ip in ip_list:
  296:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                      if ip != vm_guest_ip:

  335              for ip in ip_list:
  336:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_edge_xvMotion.py:
  295              for ip in ip_list:
  296:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                      if ip != vm_guest_ip:

  335              for ip in ip_list:
  336:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_emm.py:
  295              for ip in ip_list:
  296:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  297                      if ip != vm_guest_ip:

  335              for ip in ip_list:
  336:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  337                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dlr_dynamic_routing_vspere_ha.py:
  314              for ip in ip_list:
  315:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  316                      if ip != vm_guest_ip:

  354              for ip in ip_list:
  355:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  356                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dynamic_routing_drs.py:
  298              for ip in ip_list:
  299:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  300                      if ip != vm_guest_ip:

  338              for ip in ip_list:
  339:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  340                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dynamic_routing_edge_ft.py:
  291              for ip in ip_list:
  292:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  293                      if ip != vm_guest_ip:

  331              for ip in ip_list:
  332:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  333                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dynamic_routing_edge_svMotion.py:
  290              for ip in ip_list:
  291:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  292                      if ip != vm_guest_ip:

  330              for ip in ip_list:
  331:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  332                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dynamic_routing_edge_vMotion.py:
  288              for ip in ip_list:
  289:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  290                      if ip != vm_guest_ip:

  328              for ip in ip_list:
  329:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  330                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dynamic_routing_edge_xvMotion.py:
  290              for ip in ip_list:
  291:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  292                      if ip != vm_guest_ip:

  330              for ip in ip_list:
  331:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  332                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dynamic_routing_emm.py:
  289              for ip in ip_list:
  290:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  291                      if ip != vm_guest_ip:

  329              for ip in ip_list:
  330:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  331                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_dynamic_routing_vspere_ha.py:
  309              for ip in ip_list:
  310:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  311                      if ip != vm_guest_ip:

  349              for ip in ip_list:
  350:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  351                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_drs.py:
  229              for ip in ip_list:
  230:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  231                      if ip != vm_guest_ip:

  269              for ip in ip_list:
  270:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  271                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_edge_svMotion.py:
  228              for ip in ip_list:
  229:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  230                      if ip != vm_guest_ip:

  265              for ip in ip_list:
  266:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  267                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_edge_vMotion.py:
  214              for ip in ip_list:
  215:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  216                      if ip != vm_guest_ip:

  247              for ip in ip_list:
  248:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  249                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_edge_xvmotion.py:
  216              for ip in ip_list:
  217:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  218                      if ip != vm_guest_ip:

  249              for ip in ip_list:
  250:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  251                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_emm.py:
  242              for ip in ip_list:
  243:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  244                      if ip != vm_guest_ip:

  276              for ip in ip_list:
  277:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  278                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_vm_clone.py:
  222              for ip in ip_list:
  223:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  224                      if ip != vm_guest_ip:

  257              for ip in ip_list:
  258:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  259                      if ip != vm_guest_ip:

  403          for ip in ip_list:
  404:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  405                  if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_vm_ft.py:
  213              for ip in ip_list:
  214:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  215                      if ip != vm_guest_ip:

  246              for ip in ip_list:
  247:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  248                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_vm_network_change.py:
  253              for ip in ip_list:
  254:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  255                      if ip != vm_guest_ip:

  286              for ip in ip_list:
  287:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  288                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_vm_traffic.py:
  220              for ip in ip_list:
  221:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  222                      if ip != vm_guest_ip:

  253              for ip in ip_list:
  254:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  255                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_firewall_vsphere_ha.py:
  265              for ip in ip_list:
  266:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  267                      if ip != vm_guest_ip:

  299              for ip in ip_list:
  300:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  301                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_ha_drs.py:
  229              for ip in ip_list:
  230:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  231                      if ip != vm_guest_ip:

  269              for ip in ip_list:
  270:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  271                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_ha_edge_vmotion.py:
  227              for ip in ip_list:
  228:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  229                      if ip != vm_guest_ip:

  261              for ip in ip_list:
  262:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  263                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_ha_emm.py:
  230              for ip in ip_list:
  231:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  232                      if ip != vm_guest_ip:

  264              for ip in ip_list:
  265:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  266                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_ha_vsphere_ha.py:
  273              for ip in ip_list:
  274:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  275                      if ip != vm_guest_ip:

  307              for ip in ip_list:
  308:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  309                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_lb_edge_drs.py:
  186              for ip in ip_list:
  187:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  188                      if ip != vm_guest_ip:

  226              for ip in ip_list:
  227:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  228                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_lb_edge_emm.py:
  187              for ip in ip_list:
  188:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  189                      if ip != vm_guest_ip:

  227              for ip in ip_list:
  228:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  229                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_lb_edge_svMotion.py:
  186              for ip in ip_list:
  187:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  188                      if ip != vm_guest_ip:

  226              for ip in ip_list:
  227:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  228                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_lb_edge_vMotion.py:
  185              for ip in ip_list:
  186:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  187                      if ip != vm_guest_ip:

  225              for ip in ip_list:
  226:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  227                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_lb_edge_xvMotion.py:
  185              for ip in ip_list:
  186:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  187                      if ip != vm_guest_ip:

  225              for ip in ip_list:
  226:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  227                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_lb_vsphere_ha.py:
  208              for ip in ip_list:
  209:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  210                      if ip != vm_guest_ip:

  248              for ip in ip_list:
  249:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  250                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_redeploy_emm.py:
  231              for ip in ip_list:
  232:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  233                      if ip != vm_guest_ip:

  265              for ip in ip_list:
  266:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  267                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_edge_rename_xvMotion.py:
  241              for ip in ip_list:
  242:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  243                      if ip != vm_guest_ip:

  275              for ip in ip_list:
  276:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  277                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_flow_monitor_vm_drs.py:
  173              for ip in ip_list:
  174:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  175                      if ip != vm_guest_ip:

  213              for ip in ip_list:
  214:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  215                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_flow_monitor_vm_emm.py:
  174              for ip in ip_list:
  175:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  176                      if ip != vm_guest_ip:

  214              for ip in ip_list:
  215:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  216                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_flow_monitor_vm_svmotion.py:
  172              for ip in ip_list:
  173:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  174                      if ip != vm_guest_ip:

  212              for ip in ip_list:
  213:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  214                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_flow_monitor_vm_vmotion.py:
  172              for ip in ip_list:
  173:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  174                      if ip != vm_guest_ip:

  212              for ip in ip_list:
  213:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  214                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_flow_monitor_vm_xvmotion.py:
  172              for ip in ip_list:
  173:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  174                      if ip != vm_guest_ip:

  212              for ip in ip_list:
  213:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  214                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_nsx_controller_drs.py:
  182              for ip in ip_list:
  183:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  184                      if ip != vm_guest_ip:

  222              for ip in ip_list:
  223:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  224                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_nsx_host_reboot.py:
  260              for ip in ip_list:
  261:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  262                      if ip != vm_guest_ip:

  294              for ip in ip_list:
  295:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  296                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_nsx_manager_backup.py:
  318              for ip in ip_list:
  319:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  320                      if ip != vm_guest_ip:

  352              for ip in ip_list:
  353:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  354                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\msrinivasssa\interop_security_policy_vm_drs.py:
  175              for ip in ip_list:
  176:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  177                      if ip != vm_guest_ip:

  215              for ip in ip_list:
  216:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  217                      if ip != vm_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_cdo_emm.py:
  317          for ip in ip_list:
  318:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  319                  if ip != vm1_guest_ip:

  336          for ip in ip_list:
  337:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  338                  if ip != vm2_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_cdo_vmotion.py:
  310          for ip in ip_list:
  311:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  312                  if ip != vm1_guest_ip:

  329          for ip in ip_list:
  330:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  331                  if ip != vm2_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_cdo_vsphere_ha.py:
  330          for ip in ip_list:
  331:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  332                  if ip != vm1_guest_ip:

  349          for ip in ip_list:
  350:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  351                  if ip != vm2_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_dfw_l7_emm.py:
  223          for ip in ip_list:
  224:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  225                  if ip != vm1_guest_ip:

  244          for ip in ip_list:
  245:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  246                  if ip != vm2_guest_ip:

  265          for ip in ip_list:
  266:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  267                  if ip != vm3_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_dfw_l7_vmotion.py:
  214          for ip in ip_list:
  215:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  216                  if ip != vm1_guest_ip:

  235          for ip in ip_list:
  236:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  237                  if ip != vm2_guest_ip:

  256          for ip in ip_list:
  257:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  258                  if ip != vm3_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_dfw_l7_vsphere_ha.py:
  245          for ip in ip_list:
  246:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  247                  if ip != vm1_guest_ip:

  266          for ip in ip_list:
  267:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  268                  if ip != vm2_guest_ip:

  287          for ip in ip_list:
  288:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  289                  if ip != vm3_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_le_ge_emm.py:
  410          for ip in ip_list:
  411:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  412                  if ip != vm1_guest_ip:

  429          for ip in ip_list:
  430:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  431                  if ip != vm2_guest_ip:

  448          for ip in ip_list:
  449:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  450                  if ip != vm3_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_le_ge_ha_vsphere_ha.py:
  432          for ip in ip_list:
  433:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  434                  if ip != vm1_guest_ip:

  453          for ip in ip_list:
  454:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  455                  if ip != vm2_guest_ip:

  472          for ip in ip_list:
  473:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  474                  if ip != vm3_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_le_ge_vm_nw_change.py:
  442          for ip in ip_list:
  443:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  444                  if ip != vm1_guest_ip:

  463          for ip in ip_list:
  464:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  465                  if ip != vm2_guest_ip:

  482          for ip in ip_list:
  483:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  484                  if ip != vm3_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_le_ge_vmotion.py:
  402          for ip in ip_list:
  403:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  404                  if ip != vm1_guest_ip:

  421          for ip in ip_list:
  422:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  423                  if ip != vm2_guest_ip:

  440          for ip in ip_list:
  441:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  442                  if ip != vm3_guest_ip:

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\savaliyaa\interop_le_ge_vsphere_ha.py:
  466          for ip in ip_list:
  467:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  468                  if ip != vm1_guest_ip:

  487          for ip in ip_list:
  488:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  489                  if ip != vm2_guest_ip:

  508          for ip in ip_list:
  509:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  510                  if ip != vm3_guest_ip:

lanier-goat-development\interop\test\nsxt_vsphere\interop_port_mirror_cases.py:
  346              for ip in ip_list:
  347:                 if re.match(
  348                          "^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):

lanier-goat-development\interop\test\nsxt_vsphere\interop_dfw_test_suite\interop_switching_profile_switch_security.py:
  122              args.rt.comment("VM IP is :{}".format(vm1_ip))
  123:             if not re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  124                              vm1_ip):

  162              args.rt.comment("VM IP is :{}".format(vm1_ip))
  163:             if not re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  164                              vm1_ip):

  193              args.rt.comment("VM IP is :{}".format(vm1_ip))
  194:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  195                          vm1_ip):

lanier-goat-development\interop\test\nsxt_vsphere\interop_dhcp_server_test_suite\interop_dhcp_reboot.py:
  114          args.rt.comment("VM IP is :{}".format(edge_vm_ip))
  115:         if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  116                      edge_vm_ip):

lanier-goat-development\interop\test\nsxt_vsphere\interop_port_mirror_test_suite\interop_switching_profile_port_mirroring_vmotion.py:
  69              args.rt.comment("VM IP is :{}".format(vm1_ip))
  70:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  71                          vm1_ip):

lanier-goat-development\interop\test\nsxt_vsphere\interop_traceflow_test_suite\interop_svmotion_traceflow.py:
  130              args.rt.comment("VM IP is :{}".format(vm1_ip))
  131:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", vm1_ip):
  132                  get_guest_ip = True

  212                  args.rt.comment("VM IP is :{}".format(vm1_ip))
  213:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  214                              vm1_ip):

lanier-goat-development\interop\test\nsxt_vsphere\nsxt24_policy\dhcp_server\dhcp_reboot.py:
  122          args.rt.comment("VM IP is :{}".format(edge_vm_ip))
  123:         if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  124                      edge_vm_ip):

lanier-goat-development\interop\test\nsxt_vsphere\nsxt24_policy\segment_profile\security_profile_vmotion.py:
   91          if vm3_ip:
   92:             has_ip4_ip = re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,"
   93                                    r"3})$", vm3_ip)

  109          if vm3_ip:
  110:             has_ip4_ip = re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,"
  111                                    r"3})$", vm3_ip)

lanier-goat-development\interop\test\nsxt_vsphere\nsxt3\wcp\disable_wcp.py:
  164      harbor_vm_list = [
  165:         x for x in all_vms if re.match(HARBOR_VM_REGEX, x)]
  166      obj.args.log.info("before disable harbor_vm_list :%s" % harbor_vm_list)

lanier-goat-development\kb\edge_cluster\IKB-78635\cleaner\edge_cluster_cleaner.py:
  1352                  ((seg["path"] in self.t0SegPaths) or
  1353:                  re.match(segRegex, seg["display_name"])))
  1354  

  1377              lambda tz:
  1378:                 (re.match(edgeTzRegex, tz["display_name"])))
  1379  

  1398                  ((prof["resource_type"] == "UplinkHostSwitchProfile") and
  1399:                  re.match(uplinkProfileRegex, prof["display_name"])))
  1400  

  1474              if ((pg.key in self.edgePortgroupMobIds) or
  1475:                     re.match(externalPortgroupRegex, pg.name)):
  1476                  pgName = pg.name

  1501              if ((rp._moId in self.edgeResourcePoolMobIds) or
  1502:                     re.match(externalResourcePoolRegex, rp.name)):
  1503                  if (self.args.verbose and

lanier-goat-development\nsx\features\multi_az.py:
  367              if "\\" in ele:
  368:                 match = re.match(re_patterns.find_string_from_digit, ele)
  369                  if match:

lanier-goat-development\nsx\nsx_utils\comm_utils.py:
  1655                  args.log.info("default route found is={} ".format(item))
  1656:                 m = re.match('(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*', item)
  1657                  # item=default          0.0.0.0          10.46.46.6       vmk0

  1661                  args.log.info("not a default route found is={} ".format(item))
  1662:                 m = re.match('(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*', item)
  1663                  # item=10.46.35.0       255.255.255.0    10.46.40.1       vmk0

  1724              # vmk_ip = item.split(" ")[3]
  1725:             m = re.match('(\S*)\s*(\S*)\s*(\S*)\s*(\S*)\s*', item)
  1726              vmk_ip = m.group(4)

  2147                  args.log.info("eth0 ip found = {}".format(line.split(" ")))
  2148:                 m = re.match('\s*inet\s*(\S*)\s.*', line)
  2149                  ip = m.group(1)

  2352          for root, dirs, files in os.walk(mypath):
  2353:             for file in [x for x in files if re.match(pattern, x)]:
  2354                  results_file = (os.path.join(root, file))

lanier-goat-development\nsx\onprem\tests\nsxv\test_l2vpn.py:
  209                      args.log.info("entry={}".format(entry))
  210:                     port_id = re.match(',\s*(\d+)\s*.*', entry).group(1)
  211                      args.log.info("port_id={}".format(port_id))

  251              ps_list_output = paramiko_obj_onprem_l2vpn_vm.executecmd(ps_list, sudo=True)
  252:             match_groups = re.match('[a-z|A-Z]+\s*(\d+)\s*.*', ps_list_output[0]).groups()
  253              args.log.info("match_groups={}".format(match_groups))
  254:             ps_id = re.match('[a-z|A-Z]+\s*(\d+)\s*.*', ps_list_output[0]).group(1)
  255              args.log.info("ps_id={}".format(ps_id))

lanier-goat-development\packages\storage_bundle\storage\api_client.py:
  282              if klass.startswith('list['):
  283:                 sub_kls = re.match('list\[(.*)\]', klass).group(1)
  284                  return [self.__deserialize(sub_data, sub_kls)

  287              if klass.startswith('dict('):
  288:                 sub_kls = re.match('dict\(([^,]*), (.*)\)', klass).group(2)
  289                  return {k: self.__deserialize(v, sub_kls)

lanier-goat-development\ratutils\util.py:
  305              for vmref in all_vm_ref:
  306:                 if re.match(glob_trans(parse.regexp), vmref.name,
  307                              re.M | re.U | re.I):

  453              for vmref in all_vm_ref:
  454:                 if re.match(glob_trans(parse.regexp), vmref.name,
  455                              re.M | re.U | re.I):

lanier-goat-development\ratutils\vm.py:
  601                          continue
  602:                     elif parse.regexp and not re.match(
  603                          glob_trans(parse.regexp), vmref.name,

lanier-goat-development\sddcmanager\ems\test\verifyvsanpolicy.py:
  42      for line in lines:
  43:         if re.match(r'Policy Class|------', line, re.M | re.I):
  44              continue

  55                  continue
  56:             if re.match(r'\w\d', word, re.M | re.I) or ' ' in word or not word:
  57                  continue

lanier-goat-development\setup\test\configurecbvia.py:
  36              for ip in net.ipAddress:
  37:                 if re.match('^%s$' % cb_ipaddr, ip):
  38                      found = True

lanier-goat-development\skyscraper\test\parallel_loop.py:
  308              args.log.debug(line.strip(os.linesep))
  309:             if re.match("(.*)%s(.*)" % "Racetrack URL:", line):
  310                  args.rt.info(line.strip())

lanier-goat-development\support\gobuild\scripts\msys-translation-shim.py:
  18          # Translate: GOBUILD_X_ROOT=C:/foo/... => GOBUILD_X_ROOT=/c/foo/...
  19:         m = re.match('^(GOBUILD_\w+_ROOT)=(\w):/(.+)$', arg)
  20          if m:

lanier-goat-development\testvpx\test\vsan\fvt\test\e2e\policy\vm.py:
  786      for fil in fileList:
  787:         if re.match(combined, fil):
  788              remoteFilePath = os.path.join(fromPath, fil)

lanier-goat-development\utils\nimbus.py:
  579              for vmref in vmrefs:
  580:                 if re.match('Ubuntu64-template', vmref.name):
  581                      vmref_clone = vmref

lanier-goat-development\utils\testbed.py:
  1993                  for n in destination.parent.network:
  1994:                     if re.match(network, n.name):
  1995                          self.args.rt.info('Using network: %s' % n.name)

lanier-goat-development\utils\util.py:
  2574              self.args.networks = [net for net in self.args.dcRef.network
  2575:                                   if re.match(r'net-vm-pg-', net.name)]
  2576              if not self.args.networks:
  2577                  self.args.networks = [net for net in self.args.dcRef.network
  2578:                                       if re.match(r'VM Network', net.name)]
  2579          if not hasattr(self.args, 'hostVmknics') or not self.args.hostVmknics:

lanier-goat-development\utils\vm.py:
  1131                          continue
  1132:                     if ip_address and not re.match('^%s$' % ip_address, ip):
  1133                          self.args.log.debug(

  1141                          continue
  1142:                     if re.match('^%s$' % port_group, network):
  1143                          if ip_address:

  1155                          continue
  1156:                     if re.match('^%s$' % port_group, network):
  1157                          if ip_address:

lanier-goat-development\utils\bringup\utils\setup_actions\install_testcerts.py:
  22          for file_name in files:
  23:             if re.match(file_matching_regex, file_name):
  24                  return directory + "/{0}".format(file_name)

lanier-goat-development\utils\interop\multisite_util.py:
   35          for ip in all_ips:
   36:             if re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
   37                          ip):

   49          for ip in all_ips:
   50:             if re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
   51                          ip):

   97              for ip in dest_guest_ip_list:
   98:                 if re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
   99                              ip):

  138          for ip in dest_guest_ip_list:
  139:             if re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  140                          ip):

lanier-goat-development\utils\interop\nsxt24utils.py:
  594              for ip in all_ips:
  595:                 if re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  596                              ip):

  654          for ip in all_ips:
  655:             if re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  656                          ip):

  687                                                               dest_ip))
  688:         is_ipv4 = re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  689                             dest_ip)

  807                  for ip in dest_guest_ip_list:
  808:                     if re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  809                                  ip):

  861              for ip in dest_guest_ip_list:
  862:                 if re.match(r"^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  863                              ip):

lanier-goat-development\utils\interop\vra_utils.py:
  416              for ip in all_ip_address:
  417:                 if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$",
  418                              ip):

  452          for ip in all_ip_address:
  453:             if re.match("^(\d{0,3})\.(\d{0,3})\.(\d{0,3})\.(\d{0,3})$", ip):
  454                  vm_guest_ip = ip

lanier-goat-development\utils\skyscraper\ec2util.py:
  338              descr = key_info.get('KeyMetadata').get('Description')
  339:             m = re.match(pattern, descr)
  340              if not m:

lanier-goat-development\utils\vcf\ovfhelper.py:
  382                      for ip in net.ipAddress:
  383:                         if re.match('^%s$' % self.cb_ipaddr, ip):
  384                              found = True

lanier-goat-development\utils\vcf\ems\domainmanagerbase.py:
  3170          """
  3171:         if re.match(IPV4_PATTERN, esxi_list[0]) is None:
  3172              return "hostName"

lanier-goat-development\utils\vcf\vlcm\personality_util.py:
  319              for line in file.readlines():
  320:                 if esxi_build_number in line and re.match(BUILD_REGEX, line):
  321:                     result = re.match(BUILD_REGEX, line)
  322                      new_esxi_build_version = result.group(2)

lanier-goat-development\vc\test\verifyvsanpolicy.py:
  41      for line in lines:
  42:         if re.match(r'Policy Class|------', line, re.M | re.I):
  43              continue

  54                  continue
  55:             if re.match(r'\w\d', word, re.M | re.I) or ' ' in word or not word:
  56                  continue

lanier-goat-development\vcf\lcmtestrunner.py:
  53                  line = line.strip()
  54:                 matchobj = re.match('Apache Maven (\d)\.(.*)', line, re.I |
  55                                      re.M)

lanier-goat-development\vcf\autojsonutil\autojsoncreationutil.py:
   558                                                           'VSAN').lower()
   559:             assert re.match('nfs|vsan|vvol|vmfs', storage_type, re.I), \
   560                  "specify the proper storage type"

  1320  
  1321:             assert re.match('nfs|vsan|vvol', storage_type, re.I), "specify the proper storage type"
  1322              if storage_type == 'vvol':

lanier-goat-development\vcf\domainmanager\test\add_license.py:
  30          lic_type = 'PURCHASED'
  31:     elif re.match('PURCHASED|OEM', args.extra_test_args.get('license-type')):
  32          args.rt.info("Given License Type is valid")

  36  
  37:     if re.match('VCENTER|NSX|VROPS|VSAN|SDDC_MANAGER|VRA|ESXI|WCP',
  38                  args.extra_test_args.get('product-type')):

lanier-goat-development\vcf\hostsscaling\datastoreopsonhost.py:
  720      operation = args.extra_test_args.get('operation', 'create')
  721:     if not re.match(r'(create|delete)', operation, re.I | re.M):
  722          raise AssertionError('Please provide valid operation')

lanier-goat-development\vcf\hostsscaling\standardportgroupops.py:
  375      operation = args.extra_test_args.get('operation', 'create')
  376:     if not re.match(r'(create|delete)', operation, re.I | re.M):
  377          raise AssertionError('Please provide valid operation')

lanier-goat-development\vcf\licensemanagement\test\delete_license_v1.py:
  32              lic_type = 'PURCHASED'
  33:         elif re.match('PURCHASED|OEM', args.extra_test_args.get('license-type')):
  34              args.rt.info("Given License Type is valid")

  38  
  39:         if re.match('VCENTER|NSX|VROPS|VSAN|SDDC_MANAGER|VRA|ESXI',
  40                      args.extra_test_args.get('product-type')):

lanier-goat-development\vcf\licensemanagement\test\delete_license.py:
  27          lic_type = 'PURCHASED'
  28:     elif re.match('PURCHASED|OEM', args.extra_test_args.get('license-type')):
  29          args.rt.info("Given License Type is valid")

  33  
  34:     if re.match('VCENTER|NSX|VROPS|VSAN|SDDC_MANAGER|VRA|ESXI', args.extra_test_args.get('product-type')):
  35          args.rt.info("Given Product Type is valid")

lanier-goat-development\vcf\pipeline\tools\remove_stale_vm.py:
  183              elif ln.startswith('l'):
  184:                 found_match = re.match(r'.*\s\d{2}:\d{2}\s(.*)\s->\s(.*)', ln)
  185                  if found_match:

lanier-goat-development\vcps_maas\test\fvt\vcqe.py:
  117              for line in open(result_log_path, "r"):
  118:                 match = re.match(
  119                      r'^Test:.*Run:\s*(\d)\s*Pass:\s*(\d) '

lanier-goat-development\vcqe\update_dwh.py:
  77                  for line in open(abs_file_path, "r"):
  78:                     match = re.match(
  79                          r'^Test:.*Run:\s*(\d)\s*Pass:\s*(\d) '

lanier-goat-development\vcqe\vcqe.py:
  187              for line in open(result_log_path, "r"):
  188:                 match = re.match(
  189                      r'^Test:.*Run:\s*(\d)\s*Pass:\s*(\d) '

lanier-goat-development\via\test\configureserver.py:
  244                  # return CN=esxi-1.vrack.vsphere.local/unstructuredName=1593127904
  245:                 m = re.match(patrn, outs[0])
  246                  if m:

lanier-goat-development\vmc\configure_lcm_bifrost.py:
  88      for cluster in cluster_refs:
  89:         match = re.match("Cluster*-1", cluster.name)
  90          if match:

lanier-goat-development\vmc\configure_load_and_deploy_workloads.py:
  304          for cluster in cluster_refs:
  305:             match = re.match("Cluster*-1", cluster.name)
  306              if match:

lanier-goat-development\vmc\configure_vm_group.py:
  406              for cluster in cluster_refs:
  407:                 match = re.match("Cluster*-1", cluster.name)
  408                  if match:

lanier-goat-development\vmc\create_anti_affinity_rule.py:
  48      for vm_obj in vm_list:
  49:         match_suffix = re.match(vm_prefix, vm_obj.name)
  50          if match_suffix:

lanier-goat-development\vmc\deploy_dfw_workloads.py:
  735          for cluster in cluster_refs:
  736:             match = re.match("Cluster*-1", cluster.name)
  737              if match:

lanier-goat-development\vmc\nfs_inventory.py:
  531          for cluster in cluster_refs:
  532:             match = re.match("Cluster*-1", cluster.name)
  533              if match:

lanier-goat-development\vmc\unmount_nfs_datastore.py:
  73              for cluster in cluster_refs:
  74:                 match = re.match("Cluster*-1", cluster.name)
  75                  if match:

lanier-goat-development\vmc\patch\usecases\create_nat_rule_workload.py:
  60                  continue
  61:             match_suffix = re.match(new_vm_prefix, vms_x.name)
  62              if match_suffix:

lanier-goat-development\vmc\patch\usecases\vm_io_op.py:
  114          for rpool in resourcePool:
  115:             match_suffix = re.match("Compute-ResourcePool", rpool.name)
  116              if match_suffix:

  119          for datastore_x in cluster_x.datastore:
  120:             match_suffix = re.match("WorkloadDatastore", datastore_x.name)
  121              if match_suffix:

  139  
  140:                 match_suffix = re.match(new_vm_prefix, vms_x.name)
  141                  if match_suffix:

  203                  ip_list.append(vms_x.guest.ipAddress)
  204:                 match_suffix = re.match(new_vm_prefix, vms_x.name)
  205                  if match_suffix:

  262                  ip_list.append(vms_x.guest.ipAddress)
  263:                 match_suffix = re.match(new_vm_prefix, vms_x.name)
  264                  if match_suffix:

  315                  ip_list.append(vms_x.guest.ipAddress)
  316:                 match_suffix = re.match(new_vm_prefix, vms_x.name)
  317                  if match_suffix:

lanier-goat-development\vmc\pipeline\poweron_management_vms.py:
   40              if "This virtual machine might have been moved or copied" in out[0]:
   41:                 z = re.match(
   42                      "Virtual machine message (\d+)",

  126              continue
  127:         z = re.match("(\d+)\s+(\S+)\s+", line)
  128          if z:

lanier-goat-development\vmc\pvt\install_petronas_vibs.py:
  63      for file_name in files:
  64:         if re.match(build_number, file_name):
  65              return "/tmp/{0}".format(file_name)

lanier-goat-development\vmc\pvt\install_testcerts.py:
  40      for file_name in files:
  41:         if re.match(build_number, file_name):
  42              return "/tmp/{0}".format(file_name)

lanier-goat-development\vmc\pvt\setup_httpd.py:
  23          line = line.strip()
  24:         m = re.match(r'^Listen 80$', line)
  25          if m:

lanier-goat-development\vmc\upgrade\storage_policy\vm.py:
  717      for fil in fileList:
  718:         if re.match(combined, fil):
  719              remoteFilePath = os.path.join(fromPath, fil)

lanier-goat-development\vxrack\test\verify_vxmanager_deployed_in_WLD.py:
  48              for vmref in all_vmrefs:
  49:                 obj = re.match(r'rack-(\d+)-vxmanager-(\d+)-(.*)', vmref.name)
  50                  if obj:

lanier-goat-development\vxrack\test\verify_vxmanager_inventory_in_WLD.py:
  51              for vmref in all_vmrefs:
  52:                 obj = re.match(r'rack-(\d+)-vxmanager-(\d+)-(.*)', vmref.name)
  53                  if obj:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\setup_upgrade\test_upgrade_scon.py:
  591      def is_cvm(unique_id):
  592:         return any((re.match('catfish-(.+)-cvm', unique_id),
  593:                     re.match('cluster-(.+)panther(.+)-cvm', unique_id)))
  594  

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_rsyslog.py:
  1053          pattern = format_name["pattern"]
  1054:         if re.match(pattern, data_part) is None:
  1055              assert False, \

  1255      if elements == 'priority':
  1256:         if re.match(format_names['priority'],
  1257                      data['priority']) is None:

  1263          time_date = data['time_date']
  1264:         if re.match(pattern, time_date) is None:
  1265              assert False, '{} does not match correct ' \

  1272          pattern = r'.*[a-zA-SU-Y].*'
  1273:         if re.match(pattern, timezone) is not None:
  1274              assert False, 'timestamp cannot contain ' \

  1283          part_date = parts[0]
  1284:         if re.match(pattern, part_date) is None:
  1285              assert False, \

  1319      structured_data = syslog_message_parts[appliance_type]['structured_data']
  1320:     if re.match(pattern, structured_data) is None:
  1321          assert False, "structured data does " \

  1331                r'\d{2}Z? [A-Z0-9]+ ([a-z]+|-) (\d+|-) (\d+|-)$'
  1332:     if re.match(pattern, text_string) is None:
  1333          assert False, "{} format is not " \

  1419      logger.debug("DEBUG: rsyslog status is [%s]", output)
  1420:     matched = re.match(r".*Active:([^\)]*\)).*", output, re.DOTALL)
  1421      result = ""

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_static_config.py:
  106      for i in splits:
  107:         if re.match(vp2, i):
  108              results.append(i)

  381              # looking for things like eth0, eth1.1, em0: followed by space.
  382:             devmatch = re.match(r'([a-z0-9_.-]+):*\s+(.+)',
  383                                  line, re.IGNORECASE)

  397                  mask = maskmatch.group(1).encode('utf8', 'ignore')
  398:                 if re.match('0x', mask):
  399                      # mask is in HEX, split and convert it.

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_stats_report_during_config_change.py:
  240      active_nodes = {}
  241:     if not re.match('catfish', resource_cvm.uniqueid):
  242          active_nodes = get_active_nodes(cvm=machine["cvm"])

  272          svm_timezone_prev = {}
  273:         if not re.match('catfish', resource_cvm.uniqueid):
  274              for node in resource_svm:

  338          svm_timezone_next = {}
  339:         if not re.match('catfish', resource_cvm.uniqueid):
  340              for node in resource_svm:

  359  
  360:         if not re.match('catfish', resource_cvm.uniqueid):
  361              for key, value in svm_timezone_next.iteritems():

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\connection_resource.py:
  764      """Get the service status."""
  765:     matched = re.match(r".*Active:([^\)]*\)).*", result, re.DOTALL)
  766      result = ""

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\redis_key_value_getter.py:
  40          logger.debug("Line [%s]", line)
  41:         match = re.match(r'.*{}.*'.format(status_key), line)
  42          if match:
  43              ospf_individual_key = line
  44:         match = re.match(r'.*versioned{}.*'.format(status_key), line)
  45          if match:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\flows_performance\test_flows_perf.py:
  228          for pattern in patterns:
  229:             if re.match(pattern, line):
  230                  logger.info(line)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\conftest.py:
   99              if 'Chassis Part Number' in fru.keys():
  100:                 if re.match("TP[12]U", fru['Chassis Part Number']):
  101                      return '2'

  123              if 'Chassis Part Number' in fru.keys():
  124:                 if re.match("TP[12]U", fru['Chassis Part Number']):
  125                      return 'Tarpan'
  126:                 elif re.match("Bluefin", fru['Chassis Part Number']):
  127                      return 'Bluefin'

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_external.py:
  29              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  30:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  31              assert fru['Board Mfg'] == 'RIOS'
  32:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  33              assert fru['Product Manufacturer'] == 'Riverbed'
  34              assert fru['Product Name'] == 'SteelFusion Edge'
  35:             # assert re.match('Bluefin [12]U', fru['Product Part Number'])
  36      except AssertionError as e:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_ipmb.py:
  34              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  35:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  36:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  37              assert fru['Product Manufacturer'] == 'Riverbed'
  38              assert fru['Product Name'] == 'SteelFusion Edge'
  39:             # assert re.match('Bluefin [12]U', fru['Product Part Number'])
  40      except AssertionError as e:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_local.py:
  29              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  30:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  31              assert fru['Board Mfg'] == 'RIOS'
  32:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  33              assert fru['Product Manufacturer'] == 'Riverbed'

portfolio-system-tests\new\portfolio_system_tests\legacy_core_pq_system_tests\core_pq_system_tests\ci_cd\test_devpi_server.py:
  348      """Upload packages to index."""
  349:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  350                         package_name)

  368      """Push packages to index."""
  369:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  370                         package_name)

  385      """Update a package."""
  386:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  387                         package_name)

  420      """Delete a package."""
  421:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  422                         package_name)

portfolio-system-tests\new\portfolio_system_tests\legacy_environment_templates_tests\system_tests\test_parallel_traffic_pload.py:
  100      """
  101:     server_match = re.match(r'server(\d).*', host.uniqueid)
  102      if server_match and server_match.group(1) != '1':

  104          return None
  105:     branch_match = re.match(r'.*([-\d])', host.uniqueid)
  106      if not branch_match:

portfolio-system-tests\new\portfolio_system_tests\legacy_environment_templates_tests\system_tests\test_traffic_pload.py:
  82      """
  83:     server_match = re.match(r'server(\d).*', host.uniqueid)
  84      if server_match and server_match.group(1) != '1':

  86          return None
  87:     branch_match = re.match(r'.*([-\d])', host.uniqueid)
  88      if not branch_match:

portfolio-system-tests\new\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_path_selection_customer_issues.py:
  459                                        ' | grep psic_pttcp_conn_count')
  460:     if not re.match(".*psic_pttcp_conn_count 0.*", result):
  461          raise VerificationError(description="psic_pttcp_conn_count is NOT 0",

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover_CF3.py:
  238              dct_variables['zone_ip'] = zone_network.netv4
  239:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  240                           str(dct_variables['zone_ip']))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover.py:
  240              dct_variables['zone_ip'] = zone_network.netv4
  241:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  242                           str(dct_variables['zone_ip']))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch_CF3.py:
  138              dct_variables['zone_ip'] = zone_network.netv4
  139:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  140                           str(dct_variables['zone_ip']))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch.py:
  138              dct_variables['zone_ip'] = zone_network.netv4
  139:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  140                           str(dct_variables['zone_ip']))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\Dual_Hub\test_branch2_switches_comes_back.py:
  168          for uplink in UPLINKS:
  169:             if (re.match(branch_uplink.name,
  170                           uplink['uplink_name'],

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\Dual_Hub\test_dual_hub_leaf_branch_switch.py:
  168          for uplink in UPLINKS:
  169:             if (re.match(branch_uplink.name,
  170                           uplink['uplink_name'],

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_add_delete_wan_branch_uplink_CF3.py:
  179      for branch in branch_list:
  180:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  181              uplink_list = test_objects.scm_actor.get_site_uplinks(

  183              for uplink in uplink_list:
  184:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  185                      # assign Uplink details before delete

  245      for branch in branch_list:
  246:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  247              uplink_list = test_objects.scm_actor.get_site_uplinks(

  249              for uplink in uplink_list:
  250:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  251                      # Moving into Internet WAN before deleting 

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_add_delete_wan_branch_uplink.py:
  177      for branch in branch_list:
  178:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  179              uplink_list = test_objects.scm_actor.get_site_uplinks(

  181              for uplink in uplink_list:
  182:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  183                      # assign Uplink details before delete

  248      for branch in branch_list:
  249:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  250              uplink_list = test_objects.scm_actor.get_site_uplinks(

  252              for uplink in uplink_list:
  253:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  254                      # Remove WAN Uplink

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch_CF3.py:
  186  
  187:         if re.match("Established", state, flags=re.IGNORECASE):
  188              state_regex = r'^\d+'

  199                      status = bgp_neigh['state/pfxrcd']
  200:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  201                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  267              dct_variables['zone_ip'] = zone_network.netv4
  268:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  269                           str(dct_variables['zone_ip']))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch.py:
  186  
  187:         if re.match("Established", state, flags=re.IGNORECASE):
  188              state_regex = r'^\d+'

  199                      status = bgp_neigh['state/pfxrcd']
  200:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  201                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  267              dct_variables['zone_ip'] = zone_network.netv4
  268:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  269                           str(dct_variables['zone_ip']))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone_CF3.py:
  248              zone_ip = zone_network.netv4
  249:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  250                           str(zone_ip))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone.py:
  249              zone_ip = zone_network.netv4
  250:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  251                           str(zone_ip))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_uplink_wantype.py:
  312                  # Example:NEW_WAN_NAME='WAN2_Uplink',uplink.name='WAN2_Uplink'
  313:                 if re.match(old_uplink_name,
  314                              uplink.name, flags=re.IGNORECASE):

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_wan_uplink_ipaddress.py:
  102      # Regular expression that matches the ip address
  103:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  104                   str(branch2_tep_wan.cidr))

  233      for uplink in uplink_list:
  234:         if re.match(uplink.name, wan_uplink_name, flags=re.IGNORECASE):
  235              # Update IPV4 address of branch2 WAN uplink

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_as_mismatch.py:
  147              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  148:             assert(not re.match(r'^Established', state)), msg.format(state,
  149                                                                       neigh_ip)

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_nondefaults.py:
  149              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  150:             assert(re.match(r'^Established', state)), msg.format(state,
  151                                                                   neigh_ip)

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_match.py:
  182              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  183:             assert(re.match(r'^Established', state)), msg.format(state,
  184                                                                   neigh_ip)

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_mismatch.py:
  161                  "Actual state is {}. Expected is not 'Established' for i.f. {}"
  162:             assert(not re.match(r'^Established', state)), msg.format(state,
  163                                                                       neigh_ip)

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_peering.py:
  140                      status = bgp_neigh['state/pfxrcd']
  141:                     if not re.match(r'^\d+', status):
  142                          logger.info("BGP connection for " + str(neigh.cidr.ip))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_states_dynamic_changes.py:
  146  
  147:         if re.match("Established", state, flags=re.IGNORECASE):
  148              state_regex = r'^\d+'

  159                      status = bgp_neigh['state/pfxrcd']
  160:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  161                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  178          for interface in tep_resource.interfaces:
  179:             if re.match('^tunnel', interface.device):
  180                  ip, mask = str(interface.cidr).split('/')

  194      # Regular expression that matches the ip address
  195:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)", ip_with_mask)
  196  

  208      # Regular expression that matches the ip address
  209:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
  210  

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_ibgp_peering_on_wdr1_fails.py:
  210          bgp_summary[router_name.hostname] = wdr_obj.get_bgp_summary()
  211:         if re.match("Established", state, flags=re.IGNORECASE):
  212              state_regex = r'^\d+'

  222                      status = bgp_neigh['state/pfxrcd']
  223:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  224                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  240          router_name = dict['router']
  241:         if re.match(router_name.hostname, 'wdr1', re.IGNORECASE):
  242              wdr_obj = NetDevice.get(router_name)

  259          router_name = router._resource.hostname
  260:         if re.match(router_name, 'wdr1', re.IGNORECASE):
  261              neighbor_list = wdr_neighbor_list[router_name]

  277              router_name = router._resource.hostname
  278:             if re.match(router_name, 'wdr1', re.IGNORECASE):
  279                  neighbor_list = wdr_neighbor_list[router_name]

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_route_injection.py:
   91                      status = bgp_neigh['state/pfxrcd']
   92:                     if not re.match(r'\d+', status):
   93                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  113          for interface in tep_resource.interfaces:
  114:             if re.match('^tunnel', interface.device):
  115                  ip, mask = str(interface.cidr).split('/')

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_subnet_splitting.py:
  192          bgp_summary = wdr_obj.get_bgp_summary()
  193:         if re.match("Established", state, flags=re.IGNORECASE):
  194              state_regex = r'^\d+'

  204                      status = bgp_neigh['state/pfxrcd']
  205:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  206                          logger.info("BGP connection for " + str(neigh.cidr.ip))

portfolio-system-tests\new\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_hostlabel.py:
  145              """
  146:             regex = re.match(r'(.*)init client(.*)', line)
  147              if regex:

portfolio-system-tests\new\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_inpath_rules.py:
  296          for line in f:
  297:             matchsplice = re.match(r'(.*)init client(.*)dst(.*)',
  298                                     line)

  308                  nextline = next(f)
  309:                 matchsplice = re.match(r'(.*)' + port + '}(.*)', nextline)
  310                  if matchsplice:

portfolio-system-tests\new\portfolio_system_tests\legacy_shsaas_tests\tools\common.py:
  38      """Check if input is a valid IPv4 or subnetted IPv4 address."""
  39:     ip_match = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/\d{1,2})?$", line)  # noqa
  40      if not ip_match:

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
   58              x = x + 1
   59:             if re.match(r'Stack not found', delete_status):
   60                  print("Stack {0} deleted successfully".format(stack_name))

   72              x = x + 1
   73:             if re.match(r'Stack not found', delete_status):
   74                  print("Stack {0} deleted successfully".format(

  104          delete_status = delete_stack(args.stack_name)
  105:         if re.match(r'Stack not found', delete_status):
  106              print("Stack {0} deleted successfully".format(args.stack_name))

  127                  delete_status = delete_stack(stack[1])
  128:                 if re.match(r'Stack not found', delete_status):
  129                      print("Stack {0} deleted successfully".format(stack[1]))

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\syslog.py:
  414  
  415:     match = re.match(pattern_priority, part1[0].strip())
  416      assert match is not None, (

  420  
  421:     match = re.match(kwargs['serial'], part1[2].strip())
  422      assert match is not None, (

  426  
  427:     match = re.match(pattern_scm_info, splitted_line[1])
  428      assert match is not None, (

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_default_route_originate.py:
  385              if num + 2 <= len(list1):
  386:                 regex_output = re.match("^O\s+(0.0.0.0\/0).+", route)  # noqa
  387                  if regex_output:

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_static_routing.py:
  284          if num < len(static_list):
  285:             regex_output = re.match(r"^S\W+(\d+.\d+.\d+.\d)", route)
  286              if regex_output:

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_new_zone_discovery.py:
  53      zone_ip = zone_network.netv4
  54:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  55                   str(zone_ip))

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_route_peering.py:
  41          for element in split_output:
  42:             if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]",
  43                              element):

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\test_leaf_mode.py:
  95              # Look for the right route chain
  96:             if re.match(site['chain'], chain):
  97                  for line in chain.split('\n'):

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
  936                  key = STT_TOOL_PARAMS[key]
  937:             if(re.match('.$', key)):
  938                  str_param = f'-{key} {val}' if val else f'-{key}'

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\scc_configs.py:
  110              rule_num_pattern = r".*/rule/([0-9]+)$"
  111:             enable_match = re.match(enable_pattern, node_info['path'])
  112:             rule_num_match = re.match(rule_num_pattern, node_info['path'])
  113              if enable_match or rule_num_match:

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\configure.py:
  1741          for line in config:
  1742:             if re.match(r".*/rule/([0-9]+)$", line.strip()):
  1743                  num_inpath_rules += 1

  1779              # using an mdreq command
  1780:             src_match = re.match(src_pattern, node_name)
  1781:             dst_match = re.match(dst_pattern, node_name)
  1782:             hst_match = re.match(hst_pattern, node_name)
  1783              if src_match:

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\resources.py:
  189              for ipport in ipports:
  190:                 match = re.match(ipport_pattern, ipport)
  191                  if not match:

  396          node_names = [n['name'] for n in cvm_running_nodes]
  397:         if not re.match(".*vsh.*", "".join(node_names)):
  398              raise RuntimeError("No VSH node yet.")

  427              match = m.string[m.start():m.end()]
  428:             if re.match(ssh_prompts[0], match):
  429                  sync_channel.send("yes\n")

  470  
  471:         if re.match(login_matches[0], match):
  472              logger.debug("Got the initial configuration wizard.")

  483          match = m.string[m.start():m.end()]
  484:         addr_match = re.match(patt, match)
  485          primary_addr = addr_match.group(1)

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\verification.py:
  109      for line in file_contents:
  110:         if re.match(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line) and \
  111             re.search(r'ERR(OR)?\]', line):

  143      for line in log_file:
  144:         if re.match(r'^\d+-\d+-\d+', line):
  145              if currDict:

portfolio-system-tests\new\portfolio_system_tests\tiramisu\shminstaller.py:
  237          match_lines = [
  238:             re.match(r'(?P<pid>\d+)', line) for line in out.splitlines()
  239          ]

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\setup_upgrade\test_upgrade_scon.py:
  591      def is_cvm(unique_id):
  592:         return any((re.match('catfish-(.+)-cvm', unique_id),
  593:                     re.match('cluster-(.+)panther(.+)-cvm', unique_id)))
  594  

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_rsyslog.py:
  1053          pattern = format_name["pattern"]
  1054:         if re.match(pattern, data_part) is None:
  1055              assert False, \

  1255      if elements == 'priority':
  1256:         if re.match(format_names['priority'],
  1257                      data['priority']) is None:

  1263          time_date = data['time_date']
  1264:         if re.match(pattern, time_date) is None:
  1265              assert False, '{} does not match correct ' \

  1272          pattern = r'.*[a-zA-SU-Y].*'
  1273:         if re.match(pattern, timezone) is not None:
  1274              assert False, 'timestamp cannot contain ' \

  1283          part_date = parts[0]
  1284:         if re.match(pattern, part_date) is None:
  1285              assert False, \

  1319      structured_data = syslog_message_parts[appliance_type]['structured_data']
  1320:     if re.match(pattern, structured_data) is None:
  1321          assert False, "structured data does " \

  1331                r'\d{2}Z? [A-Z0-9]+ ([a-z]+|-) (\d+|-) (\d+|-)$'
  1332:     if re.match(pattern, text_string) is None:
  1333          assert False, "{} format is not " \

  1419      logger.debug("DEBUG: rsyslog status is [%s]", output)
  1420:     matched = re.match(r".*Active:([^\)]*\)).*", output, re.DOTALL)
  1421      result = ""

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_static_config.py:
  106      for i in splits:
  107:         if re.match(vp2, i):
  108              results.append(i)

  381              # looking for things like eth0, eth1.1, em0: followed by space.
  382:             devmatch = re.match(r'([a-z0-9_.-]+):*\s+(.+)',
  383                                  line, re.IGNORECASE)

  397                  mask = maskmatch.group(1).encode('utf8', 'ignore')
  398:                 if re.match('0x', mask):
  399                      # mask is in HEX, split and convert it.

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_stats_report_during_config_change.py:
  240      active_nodes = {}
  241:     if not re.match('catfish', resource_cvm.uniqueid):
  242          active_nodes = get_active_nodes(cvm=machine["cvm"])

  272          svm_timezone_prev = {}
  273:         if not re.match('catfish', resource_cvm.uniqueid):
  274              for node in resource_svm:

  338          svm_timezone_next = {}
  339:         if not re.match('catfish', resource_cvm.uniqueid):
  340              for node in resource_svm:

  359  
  360:         if not re.match('catfish', resource_cvm.uniqueid):
  361              for key, value in svm_timezone_next.iteritems():

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\connection_resource.py:
  764      """Get the service status."""
  765:     matched = re.match(r".*Active:([^\)]*\)).*", result, re.DOTALL)
  766      result = ""

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\redis_key_value_getter.py:
  40          logger.debug("Line [%s]", line)
  41:         match = re.match(r'.*{}.*'.format(status_key), line)
  42          if match:
  43              ospf_individual_key = line
  44:         match = re.match(r'.*versioned{}.*'.format(status_key), line)
  45          if match:

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\flows_performance\test_flows_perf.py:
  228          for pattern in patterns:
  229:             if re.match(pattern, line):
  230                  logger.info(line)

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\conftest.py:
   99              if 'Chassis Part Number' in fru.keys():
  100:                 if re.match("TP[12]U", fru['Chassis Part Number']):
  101                      return '2'

  123              if 'Chassis Part Number' in fru.keys():
  124:                 if re.match("TP[12]U", fru['Chassis Part Number']):
  125                      return 'Tarpan'
  126:                 elif re.match("Bluefin", fru['Chassis Part Number']):
  127                      return 'Bluefin'

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_external.py:
  29              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  30:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  31              assert fru['Board Mfg'] == 'RIOS'
  32:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  33              assert fru['Product Manufacturer'] == 'Riverbed'
  34              assert fru['Product Name'] == 'SteelFusion Edge'
  35:             # assert re.match('Bluefin [12]U', fru['Product Part Number'])
  36      except AssertionError as e:

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_ipmb.py:
  34              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  35:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  36:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  37              assert fru['Product Manufacturer'] == 'Riverbed'
  38              assert fru['Product Name'] == 'SteelFusion Edge'
  39:             # assert re.match('Bluefin [12]U', fru['Product Part Number'])
  40      except AssertionError as e:

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_local.py:
  29              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  30:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  31              assert fru['Board Mfg'] == 'RIOS'
  32:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  33              assert fru['Product Manufacturer'] == 'Riverbed'

portfolio-system-tests\portfolio_system_tests\legacy_core_pq_system_tests\core_pq_system_tests\ci_cd\test_devpi_server.py:
  348      """Upload packages to index."""
  349:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  350                         package_name)

  368      """Push packages to index."""
  369:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  370                         package_name)

  385      """Update a package."""
  386:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  387                         package_name)

  420      """Delete a package."""
  421:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  422                         package_name)

portfolio-system-tests\portfolio_system_tests\legacy_environment_templates_tests\system_tests\test_parallel_traffic_pload.py:
  100      """
  101:     server_match = re.match(r'server(\d).*', host.uniqueid)
  102      if server_match and server_match.group(1) != '1':

  104          return None
  105:     branch_match = re.match(r'.*([-\d])', host.uniqueid)
  106      if not branch_match:

portfolio-system-tests\portfolio_system_tests\legacy_environment_templates_tests\system_tests\test_traffic_pload.py:
  82      """
  83:     server_match = re.match(r'server(\d).*', host.uniqueid)
  84      if server_match and server_match.group(1) != '1':

  86          return None
  87:     branch_match = re.match(r'.*([-\d])', host.uniqueid)
  88      if not branch_match:

portfolio-system-tests\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_path_selection_customer_issues.py:
  459                                        ' | grep psic_pttcp_conn_count')
  460:     if not re.match(".*psic_pttcp_conn_count 0.*", result):
  461          raise VerificationError(description="psic_pttcp_conn_count is NOT 0",

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover_CF3.py:
  238              dct_variables['zone_ip'] = zone_network.netv4
  239:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  240                           str(dct_variables['zone_ip']))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover.py:
  240              dct_variables['zone_ip'] = zone_network.netv4
  241:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  242                           str(dct_variables['zone_ip']))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch_CF3.py:
  138              dct_variables['zone_ip'] = zone_network.netv4
  139:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  140                           str(dct_variables['zone_ip']))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch.py:
  138              dct_variables['zone_ip'] = zone_network.netv4
  139:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  140                           str(dct_variables['zone_ip']))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\Dual_Hub\test_branch2_switches_comes_back.py:
  168          for uplink in UPLINKS:
  169:             if (re.match(branch_uplink.name,
  170                           uplink['uplink_name'],

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\Dual_Hub\test_dual_hub_leaf_branch_switch.py:
  168          for uplink in UPLINKS:
  169:             if (re.match(branch_uplink.name,
  170                           uplink['uplink_name'],

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_add_delete_wan_branch_uplink_CF3.py:
  179      for branch in branch_list:
  180:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  181              uplink_list = test_objects.scm_actor.get_site_uplinks(

  183              for uplink in uplink_list:
  184:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  185                      # assign Uplink details before delete

  245      for branch in branch_list:
  246:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  247              uplink_list = test_objects.scm_actor.get_site_uplinks(

  249              for uplink in uplink_list:
  250:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  251                      # Moving into Internet WAN before deleting 

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_add_delete_wan_branch_uplink.py:
  177      for branch in branch_list:
  178:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  179              uplink_list = test_objects.scm_actor.get_site_uplinks(

  181              for uplink in uplink_list:
  182:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  183                      # assign Uplink details before delete

  248      for branch in branch_list:
  249:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  250              uplink_list = test_objects.scm_actor.get_site_uplinks(

  252              for uplink in uplink_list:
  253:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  254                      # Remove WAN Uplink

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch_CF3.py:
  186  
  187:         if re.match("Established", state, flags=re.IGNORECASE):
  188              state_regex = r'^\d+'

  199                      status = bgp_neigh['state/pfxrcd']
  200:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  201                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  267              dct_variables['zone_ip'] = zone_network.netv4
  268:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  269                           str(dct_variables['zone_ip']))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch.py:
  186  
  187:         if re.match("Established", state, flags=re.IGNORECASE):
  188              state_regex = r'^\d+'

  199                      status = bgp_neigh['state/pfxrcd']
  200:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  201                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  267              dct_variables['zone_ip'] = zone_network.netv4
  268:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  269                           str(dct_variables['zone_ip']))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone_CF3.py:
  248              zone_ip = zone_network.netv4
  249:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  250                           str(zone_ip))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone.py:
  249              zone_ip = zone_network.netv4
  250:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  251                           str(zone_ip))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_uplink_wantype.py:
  312                  # Example:NEW_WAN_NAME='WAN2_Uplink',uplink.name='WAN2_Uplink'
  313:                 if re.match(old_uplink_name,
  314                              uplink.name, flags=re.IGNORECASE):

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_wan_uplink_ipaddress.py:
  102      # Regular expression that matches the ip address
  103:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  104                   str(branch2_tep_wan.cidr))

  233      for uplink in uplink_list:
  234:         if re.match(uplink.name, wan_uplink_name, flags=re.IGNORECASE):
  235              # Update IPV4 address of branch2 WAN uplink

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_as_mismatch.py:
  147              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  148:             assert(not re.match(r'^Established', state)), msg.format(state,
  149                                                                       neigh_ip)

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_nondefaults.py:
  149              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  150:             assert(re.match(r'^Established', state)), msg.format(state,
  151                                                                   neigh_ip)

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_match.py:
  182              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  183:             assert(re.match(r'^Established', state)), msg.format(state,
  184                                                                   neigh_ip)

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_mismatch.py:
  161                  "Actual state is {}. Expected is not 'Established' for i.f. {}"
  162:             assert(not re.match(r'^Established', state)), msg.format(state,
  163                                                                       neigh_ip)

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_peering.py:
  140                      status = bgp_neigh['state/pfxrcd']
  141:                     if not re.match(r'^\d+', status):
  142                          logger.info("BGP connection for " + str(neigh.cidr.ip))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_states_dynamic_changes.py:
  146  
  147:         if re.match("Established", state, flags=re.IGNORECASE):
  148              state_regex = r'^\d+'

  159                      status = bgp_neigh['state/pfxrcd']
  160:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  161                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  178          for interface in tep_resource.interfaces:
  179:             if re.match('^tunnel', interface.device):
  180                  ip, mask = str(interface.cidr).split('/')

  194      # Regular expression that matches the ip address
  195:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)", ip_with_mask)
  196  

  208      # Regular expression that matches the ip address
  209:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
  210  

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_ibgp_peering_on_wdr1_fails.py:
  210          bgp_summary[router_name.hostname] = wdr_obj.get_bgp_summary()
  211:         if re.match("Established", state, flags=re.IGNORECASE):
  212              state_regex = r'^\d+'

  222                      status = bgp_neigh['state/pfxrcd']
  223:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  224                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  240          router_name = dict['router']
  241:         if re.match(router_name.hostname, 'wdr1', re.IGNORECASE):
  242              wdr_obj = NetDevice.get(router_name)

  259          router_name = router._resource.hostname
  260:         if re.match(router_name, 'wdr1', re.IGNORECASE):
  261              neighbor_list = wdr_neighbor_list[router_name]

  277              router_name = router._resource.hostname
  278:             if re.match(router_name, 'wdr1', re.IGNORECASE):
  279                  neighbor_list = wdr_neighbor_list[router_name]

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_route_injection.py:
   91                      status = bgp_neigh['state/pfxrcd']
   92:                     if not re.match(r'\d+', status):
   93                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  113          for interface in tep_resource.interfaces:
  114:             if re.match('^tunnel', interface.device):
  115                  ip, mask = str(interface.cidr).split('/')

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_subnet_splitting.py:
  192          bgp_summary = wdr_obj.get_bgp_summary()
  193:         if re.match("Established", state, flags=re.IGNORECASE):
  194              state_regex = r'^\d+'

  204                      status = bgp_neigh['state/pfxrcd']
  205:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  206                          logger.info("BGP connection for " + str(neigh.cidr.ip))

portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_hostlabel.py:
  145              """
  146:             regex = re.match(r'(.*)init client(.*)', line)
  147              if regex:

portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_inpath_rules.py:
  296          for line in f:
  297:             matchsplice = re.match(r'(.*)init client(.*)dst(.*)',
  298                                     line)

  308                  nextline = next(f)
  309:                 matchsplice = re.match(r'(.*)' + port + '}(.*)', nextline)
  310                  if matchsplice:

portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tools\common.py:
  38      """Check if input is a valid IPv4 or subnetted IPv4 address."""
  39:     ip_match = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/\d{1,2})?$", line)  # noqa
  40      if not ip_match:

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
   58              x = x + 1
   59:             if re.match(r'Stack not found', delete_status):
   60                  print("Stack {0} deleted successfully".format(stack_name))

   72              x = x + 1
   73:             if re.match(r'Stack not found', delete_status):
   74                  print("Stack {0} deleted successfully".format(

  104          delete_status = delete_stack(args.stack_name)
  105:         if re.match(r'Stack not found', delete_status):
  106              print("Stack {0} deleted successfully".format(args.stack_name))

  127                  delete_status = delete_stack(stack[1])
  128:                 if re.match(r'Stack not found', delete_status):
  129                      print("Stack {0} deleted successfully".format(stack[1]))

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\syslog.py:
  414  
  415:     match = re.match(pattern_priority, part1[0].strip())
  416      assert match is not None, (

  420  
  421:     match = re.match(kwargs['serial'], part1[2].strip())
  422      assert match is not None, (

  426  
  427:     match = re.match(pattern_scm_info, splitted_line[1])
  428      assert match is not None, (

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_default_route_originate.py:
  385              if num + 2 <= len(list1):
  386:                 regex_output = re.match("^O\s+(0.0.0.0\/0).+", route)  # noqa
  387                  if regex_output:

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_static_routing.py:
  284          if num < len(static_list):
  285:             regex_output = re.match(r"^S\W+(\d+.\d+.\d+.\d)", route)
  286              if regex_output:

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_new_zone_discovery.py:
  53      zone_ip = zone_network.netv4
  54:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  55                   str(zone_ip))

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_route_peering.py:
  41          for element in split_output:
  42:             if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]",
  43                              element):

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\test_leaf_mode.py:
  95              # Look for the right route chain
  96:             if re.match(site['chain'], chain):
  97                  for line in chain.split('\n'):

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
  936                  key = STT_TOOL_PARAMS[key]
  937:             if(re.match('.$', key)):
  938                  str_param = f'-{key} {val}' if val else f'-{key}'

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\scc_configs.py:
  110              rule_num_pattern = r".*/rule/([0-9]+)$"
  111:             enable_match = re.match(enable_pattern, node_info['path'])
  112:             rule_num_match = re.match(rule_num_pattern, node_info['path'])
  113              if enable_match or rule_num_match:

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\configure.py:
  1741          for line in config:
  1742:             if re.match(r".*/rule/([0-9]+)$", line.strip()):
  1743                  num_inpath_rules += 1

  1779              # using an mdreq command
  1780:             src_match = re.match(src_pattern, node_name)
  1781:             dst_match = re.match(dst_pattern, node_name)
  1782:             hst_match = re.match(hst_pattern, node_name)
  1783              if src_match:

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\resources.py:
  189              for ipport in ipports:
  190:                 match = re.match(ipport_pattern, ipport)
  191                  if not match:

  396          node_names = [n['name'] for n in cvm_running_nodes]
  397:         if not re.match(".*vsh.*", "".join(node_names)):
  398              raise RuntimeError("No VSH node yet.")

  427              match = m.string[m.start():m.end()]
  428:             if re.match(ssh_prompts[0], match):
  429                  sync_channel.send("yes\n")

  470  
  471:         if re.match(login_matches[0], match):
  472              logger.debug("Got the initial configuration wizard.")

  483          match = m.string[m.start():m.end()]
  484:         addr_match = re.match(patt, match)
  485          primary_addr = addr_match.group(1)

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\verification.py:
  109      for line in file_contents:
  110:         if re.match(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line) and \
  111             re.search(r'ERR(OR)?\]', line):

  143      for line in log_file:
  144:         if re.match(r'^\d+-\d+-\d+', line):
  145              if currDict:

portfolio-system-tests\portfolio_system_tests\tiramisu\shminstaller.py:
  237          match_lines = [
  238:             re.match(r'(?P<pid>\d+)', line) for line in out.splitlines()
  239          ]

ProjectVee\venv\Lib\site-packages\_distutils_hack\__init__.py:
  30      warnings.warn("Setuptools is replacing distutils.")
  31:     mods = [name for name in sys.modules if re.match(r'distutils\b', name)]
  32      for name in mods:

ProjectVee\venv\Lib\site-packages\pip\_internal\index\package_finder.py:
  535              if wheel.build_tag is not None:
  536:                 match = re.match(r'^(\d+)(.*)$', wheel.build_tag)
  537                  build_tag_groups = match.groups()

ProjectVee\venv\Lib\site-packages\pip\_internal\models\direct_url.py:
  191              return netloc
  192:         if ENV_VAR_RE.match(user_pass):
  193              return netloc

ProjectVee\venv\Lib\site-packages\pip\_internal\models\wheel.py:
  29          """
  30:         wheel_info = self.wheel_file_re.match(filename)
  31          if not wheel_info:

ProjectVee\venv\Lib\site-packages\pip\_internal\operations\install\wheel.py:
  387          # Delete any other versioned pip entry points
  388:         pip_ep = [k for k in console if re.match(r'pip(\d(\.\d)?)?$', k)]
  389          for k in pip_ep:

  404          easy_install_ep = [
  405:             k for k in console if re.match(r'easy_install(-\d\.\d)?$', k)
  406          ]

ProjectVee\venv\Lib\site-packages\pip\_internal\req\constructors.py:
  59      # type: (str) -> Tuple[str, Optional[str]]
  60:     m = re.match(r'^(.+)(\[[^\]]+\])$', path)
  61      extras = None

ProjectVee\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  482      for line_number, line in lines_enum:
  483:         if not line.endswith('\\') or COMMENT_RE.match(line):
  484:             if COMMENT_RE.match(line):
  485                  # this ensures comments are always matched later

  573          path = path.replace('\\', '/')
  574:         match = _url_slash_drive_re.match(path)
  575          if match:

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\scripts.py:
  332  
  333:             match = FIRST_LINE_RE.match(first_line.replace(b'\r\n', b'\n'))
  334              if match:

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\util.py:
  852      if project_name and len(filename) > len(project_name) + 1:
  853:         m = re.match(re.escape(project_name) + r'\b', filename)
  854          if m:

  875      """
  876:     m = NAME_VERSION_RE.match(p)
  877      if not m:

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\version.py:
  185      s = s.strip()
  186:     m = PEP440_VERSION_RE.match(s)
  187      if not m:

  271          # (~= 1.4.5.0) matches differently to (~= 1.4.5.0.0).
  272:         m = PEP440_VERSION_RE.match(s)      # must succeed
  273          groups = m.groups()

  629              return False
  630:         m = self.numeric_re.match(str(constraint))
  631          if not m:

  649  def is_semver(s):
  650:     return _SEMVER_RE.match(s)
  651  

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\wheel.py:
  160          else:
  161:             m = NAME_VERSION_RE.match(filename)
  162              if m:

  170                  dirname, filename = os.path.split(filename)
  171:                 m = FILENAME_RE.match(filename)
  172                  if not m:

  263      def process_shebang(self, data):
  264:         m = SHEBANG_RE.match(data)
  265          if m:

  272                  shebang_python = SHEBANG_PYTHON
  273:             m = SHEBANG_DETAIL_RE.match(shebang)
  274              if m:

  961      if sys.platform == 'darwin':
  962:         m = re.match(r'(\w+)_(\d+)_(\d+)_(\w+)$', ARCH)
  963          if m:

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  670          rel_re = re.compile(r'[\d.]+')
  671:         m = rel_re.match(release)
  672          if m:

ProjectVee\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  893          # gauntlet
  894:         if not re.match(r"""^([:,;#%.\sa-zA-Z0-9!]|\w-\w|'[\s\w]+'|"[\s\w]+"|\([\d,\s]+\))*$""", style):
  895              return ''
  896:         if not re.match(r"^\s*([-\w]+\s*:[^:;]*(;\s*|$))*$", style):
  897              return ''

  908                      if keyword not in self.allowed_css_keywords and \
  909:                             not re.match(r"^(#[0-9a-fA-F]+|rgb\(\d+%?,\d*%?,?\d*%?\)?|\d{0,2}\.?\d{0,2}(cm|em|ex|in|mm|pc|pt|px|%|,|\))?)$", keyword):  # noqa
  910                          break

ProjectVee\venv\Lib\site-packages\pip\_vendor\packaging\tags.py:
  504      # uses version strings like "2.20-2014.11"). See gh-3588.
  505:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  506      if not m:

ProjectVee\venv\Lib\site-packages\pip\_vendor\pep517\_in_process.py:
  142      for path in whl_zip.namelist():
  143:         m = re.match(r'[^/\\]+-[^/\\]+\.dist-info/', path)
  144          if m:

ProjectVee\venv\Lib\site-packages\pip\_vendor\requests\utils.py:
  82              test = test.replace("?", r".")      # change glob char
  83:             if re.match(test, host, re.I):
  84                  return True

ProjectVee\venv\Lib\site-packages\pip\_vendor\toml\decoder.py:
  452                  else:
  453:                     if not _groupname_re.match(groups[i]):
  454                          raise TomlDecodeError("Invalid group name '" +

  729                  break
  730:             if TIME_RE.match(pair[-1]):
  731                  break

  879              return (inline_object, "inline_object")
  880:         elif TIME_RE.match(v):
  881:             h, m, s, _, ms = TIME_RE.match(v).groups()
  882              time = datetime.time(int(h), int(m), int(s), int(ms) if ms else 0)

ProjectVee\venv\Lib\site-packages\pip\_vendor\toml\encoder.py:
  190              qsection = section
  191:             if not re.match(r'^[A-Za-z0-9_-]+$', section):
  192                  qsection = _dump_str(section)

ProjectVee\venv\Lib\site-packages\pip\_vendor\urllib3\util\retry.py:
  251          # Whitespace: https://tools.ietf.org/html/rfc7230#section-3.2.4
  252:         if re.match(r"^\s*[0-9]+\s*$", retry_after):
  253              seconds = int(retry_after)

ProjectVee\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssl_.py:
  402          hostname = hostname.decode("ascii")
  403:     return bool(IPV4_RE.match(hostname) or BRACELESS_IPV6_ADDRZ_RE.match(hostname))
  404  

ProjectVee\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:
  279          if scheme in NORMALIZABLE_SCHEMES:
  280:             is_ipv6 = IPV6_ADDRZ_RE.match(host)
  281              if is_ipv6:

  294                      return host.lower()
  295:             elif not IPV4_RE.match(host):
  296                  return six.ensure_str(

  321      """Percent-encodes a request target so that there are no invalid characters"""
  322:     path, query = TARGET_RE.match(target).groups()
  323      target = _encode_invalid_chars(path, PATH_CHARS)

  360      try:
  361:         scheme, authority, path, query, fragment = URI_RE.match(url).groups()
  362          normalize_uri = scheme is None or scheme.lower() in NORMALIZABLE_SCHEMES

  367          if authority:
  368:             auth, host, port = SUBAUTHORITY_RE.match(authority).groups()
  369              if auth and normalize_uri:

ProjectVee\venv\Lib\site-packages\pkg_resources\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

ProjectVee\venv\Lib\site-packages\pkg_resources\_vendor\packaging\tags.py:
  504      # uses version strings like "2.20-2014.11"). See gh-3588.
  505:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  506      if not m:

ProjectVee\venv\Lib\site-packages\setuptools\dist.py:
  325      for pkgname in value:
  326:         if not re.match(r'\w+(\.\w+)*', pkgname):
  327              distutils.log.warn(

ProjectVee\venv\Lib\site-packages\setuptools\package_index.py:
  173      parts = basename.split('-')
  174:     if not py_version and any(re.match(r'py\d\.\d$', p) for p in parts[2:]):
  175          # it is a bdist_dumb, not an sdist -- bail out

ProjectVee\venv\Lib\site-packages\setuptools\sandbox.py:
  446          pattern_matches = (
  447:             re.match(pattern, filepath)
  448              for pattern in self._exception_patterns

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\ccompiler.py:
  951      for pattern, compiler in _default_compilers:
  952:         if re.match(pattern, platform) is not None or \
  953:            re.match(pattern, osname) is not None:
  954              return compiler

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\dist.py:
  531          command = args[0]
  532:         if not command_re.match(command):
  533              raise SystemExit("invalid command name '%s'" % command)

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\fancy_getopt.py:
  199              # '='.
  200:             if not longopt_re.match(long):
  201                  raise DistutilsGetoptError(

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\util.py:
   88          rel_re = re.compile (r'[\d.]+', re.ASCII)
   89:         m = rel_re.match(release)
   90          if m:

  249      while s:
  250:         m = _wordchars_re.match(s, pos)
  251          end = m.end()

  267              if s[end] == "'":           # slurp singly-quoted string
  268:                 m = _squote_re.match(s, end)
  269              elif s[end] == '"':         # slurp doubly-quoted string
  270:                 m = _dquote_re.match(s, end)
  271              else:

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\version.py:
  134      def parse (self, vstring):
  135:         match = self.version_re.match(vstring)
  136          if not match:

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\command\build_ext.py:
  373              if not (isinstance(ext_name, str) and
  374:                     extension_name_re.match(ext_name)):
  375                  raise DistutilsSetupError(

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\command\build_scripts.py:
  88  
  89:                 match = first_line_re.match(first_line)
  90                  if match:

ProjectVee\venv\Lib\site-packages\setuptools\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

ProjectVee\venv\Lib\site-packages\setuptools\_vendor\packaging\tags.py:
  504      # uses version strings like "2.20-2014.11"). See gh-3588.
  505:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  506      if not m:

ProjectVee\venv\Lib\site-packages\setuptools\command\bdist_egg.py:
  250                      pattern = r'(?P<name>.+)\.(?P<magic>[^.]+)\.pyc'
  251:                     m = re.match(pattern, name)
  252                      path_new = os.path.join(

ProjectVee\venv\Lib\site-packages\setuptools\command\egg_info.py:
  568          """
  569:         return re.match(r"standard file .*not found", msg)
  570  

  714              for line in f:
  715:                 match = re.match(r"Version:.*-r(\d+)\s*$", line)
  716                  if match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\setup_upgrade\test_upgrade_scon.py:
  591      def is_cvm(unique_id):
  592:         return any((re.match('catfish-(.+)-cvm', unique_id),
  593:                     re.match('cluster-(.+)panther(.+)-cvm', unique_id)))
  594  

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_rsyslog.py:
  1053          pattern = format_name["pattern"]
  1054:         if re.match(pattern, data_part) is None:
  1055              assert False, \

  1255      if elements == 'priority':
  1256:         if re.match(format_names['priority'],
  1257                      data['priority']) is None:

  1263          time_date = data['time_date']
  1264:         if re.match(pattern, time_date) is None:
  1265              assert False, '{} does not match correct ' \

  1272          pattern = r'.*[a-zA-SU-Y].*'
  1273:         if re.match(pattern, timezone) is not None:
  1274              assert False, 'timestamp cannot contain ' \

  1283          part_date = parts[0]
  1284:         if re.match(pattern, part_date) is None:
  1285              assert False, \

  1319      structured_data = syslog_message_parts[appliance_type]['structured_data']
  1320:     if re.match(pattern, structured_data) is None:
  1321          assert False, "structured data does " \

  1331                r'\d{2}Z? [A-Z0-9]+ ([a-z]+|-) (\d+|-) (\d+|-)$'
  1332:     if re.match(pattern, text_string) is None:
  1333          assert False, "{} format is not " \

  1419      logger.debug("DEBUG: rsyslog status is [%s]", output)
  1420:     matched = re.match(r".*Active:([^\)]*\)).*", output, re.DOTALL)
  1421      result = ""

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_static_config.py:
  106      for i in splits:
  107:         if re.match(vp2, i):
  108              results.append(i)

  381              # looking for things like eth0, eth1.1, em0: followed by space.
  382:             devmatch = re.match(r'([a-z0-9_.-]+):*\s+(.+)',
  383                                  line, re.IGNORECASE)

  397                  mask = maskmatch.group(1).encode('utf8', 'ignore')
  398:                 if re.match('0x', mask):
  399                      # mask is in HEX, split and convert it.

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_stats_report_during_config_change.py:
  240      active_nodes = {}
  241:     if not re.match('catfish', resource_cvm.uniqueid):
  242          active_nodes = get_active_nodes(cvm=machine["cvm"])

  272          svm_timezone_prev = {}
  273:         if not re.match('catfish', resource_cvm.uniqueid):
  274              for node in resource_svm:

  338          svm_timezone_next = {}
  339:         if not re.match('catfish', resource_cvm.uniqueid):
  340              for node in resource_svm:

  359  
  360:         if not re.match('catfish', resource_cvm.uniqueid):
  361              for key, value in svm_timezone_next.iteritems():

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\connection_resource.py:
  764      """Get the service status."""
  765:     matched = re.match(r".*Active:([^\)]*\)).*", result, re.DOTALL)
  766      result = ""

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\redis_key_value_getter.py:
  40          logger.debug("Line [%s]", line)
  41:         match = re.match(r'.*{}.*'.format(status_key), line)
  42          if match:
  43              ospf_individual_key = line
  44:         match = re.match(r'.*versioned{}.*'.format(status_key), line)
  45          if match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\flows_performance\test_flows_perf.py:
  228          for pattern in patterns:
  229:             if re.match(pattern, line):
  230                  logger.info(line)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\conftest.py:
   99              if 'Chassis Part Number' in fru.keys():
  100:                 if re.match("TP[12]U", fru['Chassis Part Number']):
  101                      return '2'

  123              if 'Chassis Part Number' in fru.keys():
  124:                 if re.match("TP[12]U", fru['Chassis Part Number']):
  125                      return 'Tarpan'
  126:                 elif re.match("Bluefin", fru['Chassis Part Number']):
  127                      return 'Bluefin'

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_external.py:
  29              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  30:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  31              assert fru['Board Mfg'] == 'RIOS'
  32:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  33              assert fru['Product Manufacturer'] == 'Riverbed'
  34              assert fru['Product Name'] == 'SteelFusion Edge'
  35:             # assert re.match('Bluefin [12]U', fru['Product Part Number'])
  36      except AssertionError as e:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_ipmb.py:
  34              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  35:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  36:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  37              assert fru['Product Manufacturer'] == 'Riverbed'
  38              assert fru['Product Name'] == 'SteelFusion Edge'
  39:             # assert re.match('Bluefin [12]U', fru['Product Part Number'])
  40      except AssertionError as e:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_local.py:
  29              assert fru['Chassis Type'] == 'Rack Mount Chassis'
  30:             assert re.match('(Bluefin )?[12]U', fru['Chassis Part Number'])
  31              assert fru['Board Mfg'] == 'RIOS'
  32:             assert re.match('(Bluefin )?[12]U', fru['Board Part Number'])
  33              assert fru['Product Manufacturer'] == 'Riverbed'

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_pq_system_tests\core_pq_system_tests\ci_cd\test_devpi_server.py:
  348      """Upload packages to index."""
  349:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  350                         package_name)

  368      """Push packages to index."""
  369:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  370                         package_name)

  385      """Update a package."""
  386:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  387                         package_name)

  420      """Delete a package."""
  421:     mymatch = re.match(r'(?P<package>.*)-(?P<version>\d+\.\d+\.[\d|dev\d]+$)',
  422                         package_name)

sc\portfolio-system-tests\portfolio_system_tests\legacy_environment_templates_tests\system_tests\test_parallel_traffic_pload.py:
  100      """
  101:     server_match = re.match(r'server(\d).*', host.uniqueid)
  102      if server_match and server_match.group(1) != '1':

  104          return None
  105:     branch_match = re.match(r'.*([-\d])', host.uniqueid)
  106      if not branch_match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_environment_templates_tests\system_tests\test_traffic_pload.py:
  82      """
  83:     server_match = re.match(r'server(\d).*', host.uniqueid)
  84      if server_match and server_match.group(1) != '1':

  86          return None
  87:     branch_match = re.match(r'.*([-\d])', host.uniqueid)
  88      if not branch_match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_ic_tests\tests\PathSelection\test_path_selection_customer_issues.py:
  459                                        ' | grep psic_pttcp_conn_count')
  460:     if not re.match(".*psic_pttcp_conn_count 0.*", result):
  461          raise VerificationError(description="psic_pttcp_conn_count is NOT 0",

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover_CF3.py:
  238              dct_variables['zone_ip'] = zone_network.netv4
  239:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  240                           str(dct_variables['zone_ip']))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover.py:
  240              dct_variables['zone_ip'] = zone_network.netv4
  241:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  242                           str(dct_variables['zone_ip']))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch_CF3.py:
  138              dct_variables['zone_ip'] = zone_network.netv4
  139:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  140                           str(dct_variables['zone_ip']))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch.py:
  138              dct_variables['zone_ip'] = zone_network.netv4
  139:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  140                           str(dct_variables['zone_ip']))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\Dual_Hub\test_branch2_switches_comes_back.py:
  168          for uplink in UPLINKS:
  169:             if (re.match(branch_uplink.name,
  170                           uplink['uplink_name'],

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\Dual_Hub\test_dual_hub_leaf_branch_switch.py:
  168          for uplink in UPLINKS:
  169:             if (re.match(branch_uplink.name,
  170                           uplink['uplink_name'],

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_add_delete_wan_branch_uplink_CF3.py:
  179      for branch in branch_list:
  180:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  181              uplink_list = test_objects.scm_actor.get_site_uplinks(

  183              for uplink in uplink_list:
  184:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  185                      # assign Uplink details before delete

  245      for branch in branch_list:
  246:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  247              uplink_list = test_objects.scm_actor.get_site_uplinks(

  249              for uplink in uplink_list:
  250:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  251                      # Moving into Internet WAN before deleting 

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_add_delete_wan_branch_uplink.py:
  177      for branch in branch_list:
  178:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  179              uplink_list = test_objects.scm_actor.get_site_uplinks(

  181              for uplink in uplink_list:
  182:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  183                      # assign Uplink details before delete

  248      for branch in branch_list:
  249:         if re.match(branch.name, SITE, flags=re.IGNORECASE):
  250              uplink_list = test_objects.scm_actor.get_site_uplinks(

  252              for uplink in uplink_list:
  253:                 if re.match(uplink.name, UPLINK_NAME, flags=re.IGNORECASE):
  254                      # Remove WAN Uplink

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch_CF3.py:
  186  
  187:         if re.match("Established", state, flags=re.IGNORECASE):
  188              state_regex = r'^\d+'

  199                      status = bgp_neigh['state/pfxrcd']
  200:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  201                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  267              dct_variables['zone_ip'] = zone_network.netv4
  268:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  269                           str(dct_variables['zone_ip']))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch.py:
  186  
  187:         if re.match("Established", state, flags=re.IGNORECASE):
  188              state_regex = r'^\d+'

  199                      status = bgp_neigh['state/pfxrcd']
  200:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  201                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  267              dct_variables['zone_ip'] = zone_network.netv4
  268:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  269                           str(dct_variables['zone_ip']))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone_CF3.py:
  248              zone_ip = zone_network.netv4
  249:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  250                           str(zone_ip))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone.py:
  249              zone_ip = zone_network.netv4
  250:             m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  251                           str(zone_ip))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_uplink_wantype.py:
  312                  # Example:NEW_WAN_NAME='WAN2_Uplink',uplink.name='WAN2_Uplink'
  313:                 if re.match(old_uplink_name,
  314                              uplink.name, flags=re.IGNORECASE):

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_wan_uplink_ipaddress.py:
  102      # Regular expression that matches the ip address
  103:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  104                   str(branch2_tep_wan.cidr))

  233      for uplink in uplink_list:
  234:         if re.match(uplink.name, wan_uplink_name, flags=re.IGNORECASE):
  235              # Update IPV4 address of branch2 WAN uplink

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_as_mismatch.py:
  147              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  148:             assert(not re.match(r'^Established', state)), msg.format(state,
  149                                                                       neigh_ip)

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_nondefaults.py:
  149              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  150:             assert(re.match(r'^Established', state)), msg.format(state,
  151                                                                   neigh_ip)

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_match.py:
  182              msg = "Actual state is {}. Expected is 'Established' for i.f. {}"
  183:             assert(re.match(r'^Established', state)), msg.format(state,
  184                                                                   neigh_ip)

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_mismatch.py:
  161                  "Actual state is {}. Expected is not 'Established' for i.f. {}"
  162:             assert(not re.match(r'^Established', state)), msg.format(state,
  163                                                                       neigh_ip)

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_peering.py:
  140                      status = bgp_neigh['state/pfxrcd']
  141:                     if not re.match(r'^\d+', status):
  142                          logger.info("BGP connection for " + str(neigh.cidr.ip))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_states_dynamic_changes.py:
  146  
  147:         if re.match("Established", state, flags=re.IGNORECASE):
  148              state_regex = r'^\d+'

  159                      status = bgp_neigh['state/pfxrcd']
  160:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  161                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  178          for interface in tep_resource.interfaces:
  179:             if re.match('^tunnel', interface.device):
  180                  ip, mask = str(interface.cidr).split('/')

  194      # Regular expression that matches the ip address
  195:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)", ip_with_mask)
  196  

  208      # Regular expression that matches the ip address
  209:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
  210  

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_ibgp_peering_on_wdr1_fails.py:
  210          bgp_summary[router_name.hostname] = wdr_obj.get_bgp_summary()
  211:         if re.match("Established", state, flags=re.IGNORECASE):
  212              state_regex = r'^\d+'

  222                      status = bgp_neigh['state/pfxrcd']
  223:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  224                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  240          router_name = dict['router']
  241:         if re.match(router_name.hostname, 'wdr1', re.IGNORECASE):
  242              wdr_obj = NetDevice.get(router_name)

  259          router_name = router._resource.hostname
  260:         if re.match(router_name, 'wdr1', re.IGNORECASE):
  261              neighbor_list = wdr_neighbor_list[router_name]

  277              router_name = router._resource.hostname
  278:             if re.match(router_name, 'wdr1', re.IGNORECASE):
  279                  neighbor_list = wdr_neighbor_list[router_name]

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_route_injection.py:
   91                      status = bgp_neigh['state/pfxrcd']
   92:                     if not re.match(r'\d+', status):
   93                          logger.info("BGP connection for " + str(neigh.cidr.ip))

  113          for interface in tep_resource.interfaces:
  114:             if re.match('^tunnel', interface.device):
  115                  ip, mask = str(interface.cidr).split('/')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_subnet_splitting.py:
  192          bgp_summary = wdr_obj.get_bgp_summary()
  193:         if re.match("Established", state, flags=re.IGNORECASE):
  194              state_regex = r'^\d+'

  204                      status = bgp_neigh['state/pfxrcd']
  205:                     if not re.match(state_regex, status, flags=re.IGNORECASE):
  206                          logger.info("BGP connection for " + str(neigh.cidr.ip))

sc\portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_hostlabel.py:
  145              """
  146:             regex = re.match(r'(.*)init client(.*)', line)
  147              if regex:

sc\portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_inpath_rules.py:
  296          for line in f:
  297:             matchsplice = re.match(r'(.*)init client(.*)dst(.*)',
  298                                     line)

  308                  nextline = next(f)
  309:                 matchsplice = re.match(r'(.*)' + port + '}(.*)', nextline)
  310                  if matchsplice:

sc\portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tools\common.py:
  38      """Check if input is a valid IPv4 or subnetted IPv4 address."""
  39:     ip_match = re.match("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(/\d{1,2})?$", line)  # noqa
  40      if not ip_match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
   58              x = x + 1
   59:             if re.match(r'Stack not found', delete_status):
   60                  print("Stack {0} deleted successfully".format(stack_name))

   72              x = x + 1
   73:             if re.match(r'Stack not found', delete_status):
   74                  print("Stack {0} deleted successfully".format(

  104          delete_status = delete_stack(args.stack_name)
  105:         if re.match(r'Stack not found', delete_status):
  106              print("Stack {0} deleted successfully".format(args.stack_name))

  127                  delete_status = delete_stack(stack[1])
  128:                 if re.match(r'Stack not found', delete_status):
  129                      print("Stack {0} deleted successfully".format(stack[1]))

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\syslog.py:
  414  
  415:     match = re.match(pattern_priority, part1[0].strip())
  416      assert match is not None, (

  420  
  421:     match = re.match(kwargs['serial'], part1[2].strip())
  422      assert match is not None, (

  426  
  427:     match = re.match(pattern_scm_info, splitted_line[1])
  428      assert match is not None, (

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_default_route_originate.py:
  385              if num + 2 <= len(list1):
  386:                 regex_output = re.match("^O\s+(0.0.0.0\/0).+", route)  # noqa
  387                  if regex_output:

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_static_routing.py:
  284          if num < len(static_list):
  285:             regex_output = re.match(r"^S\W+(\d+.\d+.\d+.\d)", route)
  286              if regex_output:

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_new_zone_discovery.py:
  53      zone_ip = zone_network.netv4
  54:     m = re.match(r"(\d+)\.(\d+)\.(\d+)\.(\d+)\/(\d+)",
  55                   str(zone_ip))

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_route_peering.py:
  41          for element in split_output:
  42:             if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]",
  43                              element):

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\test_leaf_mode.py:
  95              # Look for the right route chain
  96:             if re.match(site['chain'], chain):
  97                  for line in chain.split('\n'):

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
  936                  key = STT_TOOL_PARAMS[key]
  937:             if(re.match('.$', key)):
  938                  str_param = f'-{key} {val}' if val else f'-{key}'

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\scc_configs.py:
  110              rule_num_pattern = r".*/rule/([0-9]+)$"
  111:             enable_match = re.match(enable_pattern, node_info['path'])
  112:             rule_num_match = re.match(rule_num_pattern, node_info['path'])
  113              if enable_match or rule_num_match:

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\configure.py:
  1741          for line in config:
  1742:             if re.match(r".*/rule/([0-9]+)$", line.strip()):
  1743                  num_inpath_rules += 1

  1779              # using an mdreq command
  1780:             src_match = re.match(src_pattern, node_name)
  1781:             dst_match = re.match(dst_pattern, node_name)
  1782:             hst_match = re.match(hst_pattern, node_name)
  1783              if src_match:

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\resources.py:
  189              for ipport in ipports:
  190:                 match = re.match(ipport_pattern, ipport)
  191                  if not match:

  396          node_names = [n['name'] for n in cvm_running_nodes]
  397:         if not re.match(".*vsh.*", "".join(node_names)):
  398              raise RuntimeError("No VSH node yet.")

  427              match = m.string[m.start():m.end()]
  428:             if re.match(ssh_prompts[0], match):
  429                  sync_channel.send("yes\n")

  470  
  471:         if re.match(login_matches[0], match):
  472              logger.debug("Got the initial configuration wizard.")

  483          match = m.string[m.start():m.end()]
  484:         addr_match = re.match(patt, match)
  485          primary_addr = addr_match.group(1)

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\verification.py:
  109      for line in file_contents:
  110:         if re.match(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line) and \
  111             re.search(r'ERR(OR)?\]', line):

  143      for line in log_file:
  144:         if re.match(r'^\d+-\d+-\d+', line):
  145              if currDict:

sc\portfolio-system-tests\portfolio_system_tests\tiramisu\shminstaller.py:
  237          match_lines = [
  238:             re.match(r'(?P<pid>\d+)', line) for line in out.splitlines()
  239          ]

VCMGUIAUTO_FF\venv\Lib\site-packages\cffi\api.py:
  760          import re
  761:         match = re.match(r'\s*\n', pysource)
  762          if match:

  764          lines = pysource.splitlines() or ['']
  765:         prefix = re.match(r'\s*', lines[0]).group()
  766          for i in range(1, len(lines)):

VCMGUIAUTO_FF\venv\Lib\site-packages\cffi\cparser.py:
  319          msg = str(e)
  320:         match = re.match(r"%s:(\d+):" % (CDEF_SOURCE_STRING,), msg)
  321          if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\paramiko\config.py:
  139              # Parse line into key, value
  140:             match = re.match(self.SETTINGS_REGEX, line)
  141              if not match:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\index\package_finder.py:
  535              if wheel.build_tag is not None:
  536:                 match = re.match(r'^(\d+)(.*)$', wheel.build_tag)
  537                  build_tag_groups = match.groups()

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\models\direct_url.py:
  191              return netloc
  192:         if ENV_VAR_RE.match(user_pass):
  193              return netloc

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\models\wheel.py:
  29          """
  30:         wheel_info = self.wheel_file_re.match(filename)
  31          if not wheel_info:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\operations\install\wheel.py:
  519          # Delete any other versioned pip entry points
  520:         pip_ep = [k for k in console if re.match(r'pip(\d(\.\d)?)?$', k)]
  521          for k in pip_ep:

  536          easy_install_ep = [
  537:             k for k in console if re.match(r'easy_install(-\d\.\d)?$', k)
  538          ]

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\req\constructors.py:
  61      # type: (str) -> Tuple[str, Optional[str]]
  62:     m = re.match(r'^(.+)(\[[^\]]+\])$', path)
  63      extras = None

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  474      for line_number, line in lines_enum:
  475:         if not line.endswith('\\') or COMMENT_RE.match(line):
  476:             if COMMENT_RE.match(line):
  477                  # this ensures comments are always matched later

  563          path = path.replace('\\', '/')
  564:         match = _url_slash_drive_re.match(path)
  565          if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\toml.py:
  343                  else:
  344:                     if not _groupname_re.match(groups[i]):
  345                          raise TomlDecodeError("Invalid group name '" +

  916          qsection = section
  917:         if not re.match(r'^[A-Za-z0-9_-]+$', section):
  918              if '"' in section:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\scripts.py:
  329  
  330:             match = FIRST_LINE_RE.match(first_line.replace(b'\r\n', b'\n'))
  331              if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\util.py:
  852      if project_name and len(filename) > len(project_name) + 1:
  853:         m = re.match(re.escape(project_name) + r'\b', filename)
  854          if m:

  875      """
  876:     m = NAME_VERSION_RE.match(p)
  877      if not m:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\version.py:
  185      s = s.strip()
  186:     m = PEP440_VERSION_RE.match(s)
  187      if not m:

  271          # (~= 1.4.5.0) matches differently to (~= 1.4.5.0.0).
  272:         m = PEP440_VERSION_RE.match(s)      # must succeed
  273          groups = m.groups()

  629              return False
  630:         m = self.numeric_re.match(str(constraint))
  631          if not m:

  649  def is_semver(s):
  650:     return _SEMVER_RE.match(s)
  651  

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\wheel.py:
  159          else:
  160:             m = NAME_VERSION_RE.match(filename)
  161              if m:

  169                  dirname, filename = os.path.split(filename)
  170:                 m = FILENAME_RE.match(filename)
  171                  if not m:

  260      def process_shebang(self, data):
  261:         m = SHEBANG_RE.match(data)
  262          if m:

  269                  shebang_python = SHEBANG_PYTHON
  270:             m = SHEBANG_DETAIL_RE.match(shebang)
  271              if m:

  947      if sys.platform == 'darwin':
  948:         m = re.match(r'(\w+)_(\d+)_(\d+)_(\w+)$', ARCH)
  949          if m:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  670          rel_re = re.compile(r'[\d.]+')
  671:         m = rel_re.match(release)
  672          if m:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  873          # gauntlet
  874:         if not re.match(r"""^([:,;#%.\sa-zA-Z0-9!]|\w-\w|'[\s\w]+'|"[\s\w]+"|\([\d,\s]+\))*$""", style):
  875              return ''
  876:         if not re.match(r"^\s*([-\w]+\s*:[^:;]*(;\s*|$))*$", style):
  877              return ''

  888                      if keyword not in self.allowed_css_keywords and \
  889:                             not re.match(r"^(#[0-9a-fA-F]+|rgb\(\d+%?,\d*%?,?\d*%?\)?|\d{0,2}\.?\d{0,2}(cm|em|ex|in|mm|pc|pt|px|%|,|\))?)$", keyword):  # noqa
  890                          break

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\packaging\tags.py:
  492      # uses version strings like "2.20-2014.11"). See gh-3588.
  493:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  494      if not m:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\pep517\_in_process.py:
  142      for path in whl_zip.namelist():
  143:         m = re.match(r'[^/\\]+-[^/\\]+\.dist-info/', path)
  144          if m:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\requests\utils.py:
  82              test = test.replace("?", r".")      # change glob char
  83:             if re.match(test, host, re.I):
  84                  return True

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\toml\decoder.py:
  397                  else:
  398:                     if not _groupname_re.match(groups[i]):
  399                          raise TomlDecodeError("Invalid group name '" +

  806              return (inline_object, "inline_object")
  807:         elif TIME_RE.match(v):
  808:             h, m, s, _, ms = TIME_RE.match(v).groups()
  809              time = datetime.time(int(h), int(m), int(s), int(ms) if ms else 0)

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\toml\encoder.py:
  170              qsection = section
  171:             if not re.match(r'^[A-Za-z0-9_-]+$', section):
  172                  if '"' in section:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\urllib3\util\retry.py:
  250          # Whitespace: https://tools.ietf.org/html/rfc7230#section-3.2.4
  251:         if re.match(r"^\s*[0-9]+\s*$", retry_after):
  252              seconds = int(retry_after)

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\urllib3\util\ssl_.py:
  395          hostname = hostname.decode("ascii")
  396:     return bool(IPV4_RE.match(hostname) or BRACELESS_IPV6_ADDRZ_RE.match(hostname))
  397  

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:
  279          if scheme in NORMALIZABLE_SCHEMES:
  280:             is_ipv6 = IPV6_ADDRZ_RE.match(host)
  281              if is_ipv6:

  294                      return host.lower()
  295:             elif not IPV4_RE.match(host):
  296                  return six.ensure_str(

  321      """Percent-encodes a request target so that there are no invalid characters"""
  322:     path, query = TARGET_RE.match(target).groups()
  323      target = _encode_invalid_chars(path, PATH_CHARS)

  360      try:
  361:         scheme, authority, path, query, fragment = URI_RE.match(url).groups()
  362          normalize_uri = scheme is None or scheme.lower() in NORMALIZABLE_SCHEMES

  367          if authority:
  368:             auth, host, port = SUBAUTHORITY_RE.match(authority).groups()
  369              if auth and normalize_uri:

VCMGUIAUTO_FF\venv\Lib\site-packages\pkg_resources\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

VCMGUIAUTO_FF\venv\Lib\site-packages\pycparser\ply\lex.py:
  319              for lexre, lexindexfunc in self.lexre:
  320:                 m = lexre.match(lexdata, lexpos)
  321                  if not m:

  843          for line in lines:
  844:             m = fre.match(line)
  845              if not m:
  846:                 m = sre.match(line)
  847              if m:

VCMGUIAUTO_FF\venv\Lib\site-packages\pycparser\ply\yacc.py:
  3009                  linen += 1
  3010:                 m = fre.match(line)
  3011                  if m:

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\libraries\BuiltIn.py:
  1949                      'STARTS': lambda s, p: s.startswith(p),
  1950:                     'REGEXP': lambda s, p: re.match(p, s) is not None}
  1951          prefixes = tuple(prefix + ':' for prefix in matchers)

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\utils\argumentparser.py:
  230          for line in usage.splitlines():
  231:             res = self._opt_line_re.match(line)
  232              if res:

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\utils\error.py:
  205              return True
  206:         res = self._java_trace_re.match(line)
  207          if res is None:

  221          while lines:
  222:             if self._java_trace_re.match(lines[-1]):
  223                  lines.pop()

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\utils\etreewrapper.py:
  94      def _find_encoding(self, source):
  95:         match = re.match("\s*<\?xml .*encoding=(['\"])(.*?)\\1.*\?>", source)
  96          return match.group(2) if match else 'UTF-8'

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\utils\platform.py:
  20  
  21: java_match = re.match(r'java(\d+)\.(\d+)\.(\d+)', sys.platform)
  22  if java_match:

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\utils\robottime.py:
  56  def _timer_to_secs(number):
  57:     match = _timer_re.match(number)
  58      if not match:

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\utils\text.py:
  152      lines = doc.splitlines()
  153:     match = _TAGS_RE.match(lines[-1])
  154      if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\selenium\webdriver\support\color.py:
  51              def match(self, pattern, str_):
  52:                 self.match_obj = re.match(pattern, str_)
  53                  return self.match_obj

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\dist.py:
  327      for pkgname in value:
  328:         if not re.match(r'\w+(\.\w+)*', pkgname):
  329              distutils.log.warn(

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\package_index.py:
  173      parts = basename.split('-')
  174:     if not py_version and any(re.match(r'py\d\.\d$', p) for p in parts[2:]):
  175          # it is a bdist_dumb, not an sdist -- bail out

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\sandbox.py:
  442          pattern_matches = (
  443:             re.match(pattern, filepath)
  444              for pattern in self._exception_patterns

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\_vendor\pyparsing.py:
  2708          if self.re:
  2709:             result = self.re.match(instring,loc)
  2710              if not result:

  2813      def parseImpl( self, instring, loc, doActions=True ):
  2814:         result = self.re.match(instring,loc)
  2815          if not result:

  2928      def parseImpl( self, instring, loc, doActions=True ):
  2929:         result = instring[loc] == self.firstQuoteChar and self.re.match(instring,loc) or None
  2930          if not result:

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\_vendor\packaging\tags.py:
  311      # uses version strings like "2.20-2014.11"). See gh-3588.
  312:     m = re.match(r"(?P<major>[0-9]+)\.(?P<minor>[0-9]+)", version_str)
  313      if not m:

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\command\bdist_egg.py:
  256                      pattern = r'(?P<name>.+)\.(?P<magic>[^.]+)\.pyc'
  257:                     m = re.match(pattern, name)
  258                      path_new = os.path.join(

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\command\egg_info.py:
  567          """
  568:         return re.match(r"standard file .*not found", msg)
  569  

  713              for line in f:
  714:                 match = re.match(r"Version:.*-r(\d+)\s*$", line)
  715                  if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\urllib3\util\retry.py:
  251          # Whitespace: https://tools.ietf.org/html/rfc7230#section-3.2.4
  252:         if re.match(r"^\s*[0-9]+\s*$", retry_after):
  253              seconds = int(retry_after)

VCMGUIAUTO_FF\venv\Lib\site-packages\urllib3\util\ssl_.py:
  402          hostname = hostname.decode("ascii")
  403:     return bool(IPV4_RE.match(hostname) or BRACELESS_IPV6_ADDRZ_RE.match(hostname))
  404  

VCMGUIAUTO_FF\venv\Lib\site-packages\urllib3\util\url.py:
  279          if scheme in NORMALIZABLE_SCHEMES:
  280:             is_ipv6 = IPV6_ADDRZ_RE.match(host)
  281              if is_ipv6:

  294                      return host.lower()
  295:             elif not IPV4_RE.match(host):
  296                  return six.ensure_str(

  321      """Percent-encodes a request target so that there are no invalid characters"""
  322:     path, query = TARGET_RE.match(target).groups()
  323      target = _encode_invalid_chars(path, PATH_CHARS)

  360      try:
  361:         scheme, authority, path, query, fragment = URI_RE.match(url).groups()
  362          normalize_uri = scheme is None or scheme.lower() in NORMALIZABLE_SCHEMES

  367          if authority:
  368:             auth, host, port = SUBAUTHORITY_RE.match(authority).groups()
  369              if auth and normalize_uri:
