# Query: re.search(
# ContextLines: 1

4299 results - 1237 files

dist-packages\portfolio_system_tests\gelato\setup_collector_simulator_pair.py:
  109          res = shell.exec_command('virsh net-dhcp-leases default')
  110:         vm_ip_search = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
  111          if not vm_ip_search:

dist-packages\portfolio_system_tests\gelato\setup_collector_simulator_stack.py:
  86          res = shell.exec_command('virsh net-dhcp-leases default')
  87:         vm_ip_search = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
  88          if not vm_ip_search:

dist-packages\portfolio_system_tests\legacy_core_infra_nx\NX_Manufacture\utils.py:
   98      one, two = os.path.split(component)
   99:     build_number = re.search(name + "-(.*?)-(.*?).noarch.rpm", two).group(2)
  100      number = ": " + str(build_number)
  101  
  102:     version = re.search(name + "-(.*?)-(.*?).noarch.rpm", two).group(1)
  103      version = ": " + str(version)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\NX_Manufacture\vm.py:
  100              vm_create_node_image_name = \
  101:                 re.search(r'(.*)\s+:\s+' + vm_product_name,
  102                            line).group(1).strip()

  174      try:
  175:         image_name = re.search(r'\|\s+' + vm_node_name + r"\s+\|\s+(.*?)\|",
  176                                 buf).group(1).strip()

dist-packages\portfolio_system_tests\legacy_core_infra_nx\setup_upgrade\test_upgrade_scon.py:
  126      print(univ_op)
  127:     latest_build_tag = re.search('binary_builds.*browse/(.+)', univ_op).\
  128          group(1)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_cli.py:
   64      str_pattern = 'challenge generate(.*){}'.format(dut_serialno)
   65:     match = re.search(str_pattern, cmd_op)
   66      if match:

  475                                      replace("rvbd-testuser@", "root@")
  476:                                 match = re.search('ProxyCommand=nc -X '
  477                                                    'connect -x (.*):', val).\

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_connectivity.py:
  185              val = tunnel['ssh_help']
  186:             match = re.search(
  187                  'ProxyCommand=nc -X connect -x (.*):',

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_diverter.py:
  149      dns_output = cvm_shell.exec_command('nslookup ' + remote_host)
  150:     filter_host_ip = re.search('Address: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', # noqa
  151                                 dns_output)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_oa_cdl_update.py:
  747                                                      new_cdl_file)
  748:             match = re.search(error_msg, output.strip())
  749              if not match:

  759                                                      new_cdl_file)
  760:             match = re.search(error_msg, output.strip())
  761              if not match:

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_ssh_tunnel.py:
  86                              val = tunnel['ssh_help']
  87:                             match = re.search('ProxyCommand=nc -X connect '
  88                                                '-x (.*):', val).group(1)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_static_config.py:
  389                  continue
  390:             ipmatch = re.search(r'inet\s(?:addr:)*(\S+)', line)
  391              if ipmatch:

  394  
  395:             maskmatch = re.search(r'Mask:*\s*(\S+)', line, re.IGNORECASE)
  396              if maskmatch:

  405  
  406:             ipv6match = re.search(
  407                  r'inet6\saddr:\s([a-fA-F0-9:]+)/*(\S+)', line)

  413  
  414:             ethmatch = re.search(r'(?:(?:ether)|(?:HWaddr))\s(?:addr:)*(\S+)',
  415                                   line)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_tcpdump_on_cli.py:
  105      if state == 'RUNNING':
  106:         match = re.search(tcpdump_running_exp_str, output)
  107          if match:

  112      else:
  113:         match = re.search(tcpdump_not_running_exp_str, output)
  114          if match:

  208          logger.info("output of tcpdump command: {}".format(tcpdump_output))
  209:         match = re.search(exp_result, tcpdump_output)
  210          tcpdump_file = match.group(0)

  257              tcpdump_output = cli_instance.exec_command(tcpdump_cmd1)
  258:             match = re.search(exp_result, tcpdump_output)
  259              tcpdump_file = match.group(0)

  326          output = cli_instance.exec_command(tcpdump_stop_cmd)
  327:         match = re.search(tcpdump_stop_exp_result, output)
  328          if match:

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\test_troubleshoot_tool.py:
   92          data = troubleshoot_info.split('\n')
   93:         match = re.search(exp_result, data[-1])
   94          troubleshoot_tar = match.group(0)

  146              data = troubleshoot_info.split('\n')
  147:             match = re.search(exp_result, data[-2])
  148              troubleshoot_tar = match.group(0)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\nodes.py:
  661  
  662:         match = re.search(exp_result, data[-1])
  663          troubleshoot_tar = match.group(0)

dist-packages\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\site_dns_lib.py:
  248      most_recent_content = lease_file_op.split("lease {")[-1]
  249:     m = re.search("option domain-name-servers (.*);", most_recent_content)
  250      if m:

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_external.py:
  47          for fru in fru_list:
  48:             assert re.search("CXA-00[57]70-B020", fru['Chassis Part Number'])
  49              assert fru['Board Mfg'] == 'Advantech'

  51              assert fru['Product Name'] == 'DTATA'
  52:             assert re.search("FWA-3250-RB0[23]E?", fru['Product Part Number'])
  53      except AssertionError as e:

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_local.py:
  46          for fru in fru_list:
  47:             assert re.search("CXA-00[57]70-B020", fru['Chassis Part Number'])
  48              assert fru['Board Mfg'] == 'Advantech'

  50              assert fru['Product Name'] == 'DTATA'
  51:             assert re.search("FWA-3250-RB0[23]E?", fru['Product Part Number'])
  52      except AssertionError as e:

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_external.py:
   26      try:
   27:         assert re.search(r"\d+", info_dict['Record Count']), \
   28              info_dict['Record Count']
   29:         assert re.search(r"\d+ bytes", info_dict['Free Space']), \
   30              info_dict['Free Space']

   56          for op in status_list:
   57:             if re.search(("fan", op[0].lower()) and
   58                           op[1].lower() != 'no reading'):
   59:                 assert re.search(r"\d+ RPM", op[1]), op
   60      except AssertionError as e:

   70          for op in status_list:
   71:             if re.search(("temp", op[0].lower()) and
   72                           op[1].lower() != 'no reading'):
   73:                 assert re.search(r"\d+ degrees C", op[1]), op
   74      except AssertionError as e:

   84          for op in status_list:
   85:             if re.search(("hdd", op[0].lower()) and
   86                           op[1].lower() != 'no reading'):
   87:                 assert re.search(r"\d+ degrees C", op[1]), op
   88      except AssertionError as e:

   98          for op in status_list:
   99:             if re.search(("cpu_dimm*", op[0].lower()) and
  100                           op[1].lower() != 'no reading'):
  101:                 assert re.search(r"\d+ degrees C", op[1]), op
  102:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  103:                 assert re.search(r"^\d+\.?\d* Volts", op[1]), op
  104      except AssertionError as e:

  114          for op in status_list:
  115:             if re.search("power", op[0].lower()):
  116:                 assert re.search(r"\d+ Watts", op[1]), op
  117      except AssertionError as e:

  142                  assert op[2] == 'ok', op
  143:                 if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  144:                     assert re.search(r"\d+ degrees C", op[4]), op
  145      except AssertionError as e:

  156              assert op[2] == 'ok'
  157:             assert re.search(r"\d+\.\d+ Volts", op[4]), op
  158      except AssertionError as e:

  169              assert op[2] == 'ok'
  170:             assert re.search(r"\d+ RPM", op[4]), op
  171      except AssertionError as e:

  182              assert op[2] == 'ok'
  183:             if re.search(r"PSU\d+ Status", op[0]):
  184                  assert op[4].lower() == 'presence detected'
  185:             elif re.search(r"PSU\d+ Power", op[0]):
  186:                 assert re.search(r"\d+ Watts", op[4])
  187      except AssertionError as e:

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_ipmb.py:
   44      try:
   45:         assert re.search(r'\d+', info_dict['Record Count']), \
   46              info_dict['Record Count']
   47:         assert re.search(r'\d+ bytes', info_dict['Free Space']), \
   48              info_dict['Free Space']

   63          for op in status_list:
   64:             if re.search("fan", op[0].lower()) and op[1] != 'no reading':
   65:                 assert re.search(r'\d+ RPM', op[1]), op
   66      except AssertionError as e:

   79          for op in status_list:
   80:             if re.search("temp", op[0].lower()) and op[1] != 'no reading':
   81:                 assert re.search(r'\d+ degrees C', op[1]), op
   82      except AssertionError as e:

   95          for op in status_list:
   96:             if re.search("hdd", op[0].lower()) and op[1] != 'no reading':
   97:                 assert re.search(r"\d+ degrees C", op[1]), op
   98      except AssertionError as e:

  111          for op in status_list:
  112:             if re.search(("cpu_dimm*", op[0].lower()) and
  113                           op[1].lower() != 'no reading'):
  114:                 assert re.search(r"\d+ degrees C", op[1]), op
  115:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  116:                 assert re.search(r"^\d+\.?\d* Volts", op[1]), op
  117      except AssertionError as e:

  130          for op in status_list:
  131:             if re.search("power", op[0].lower()) and op[1] != 'no reading':
  132:                 assert re.search(r"\d+ Watts", op[1]), op
  133      except AssertionError as e:

  165                      assert op[2] == 'ok', op
  166:                     if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  167:                         assert re.search(r"\d+ degrees C", op[4]), op
  168          except AssertionError as e:

  186                  assert op[2] == 'ok'
  187:                 assert re.search(r"\d+\.\d+ Volts", op[4]), op
  188          except AssertionError as e:

  205                  assert op[2] == 'ok'
  206:                 assert re.search(r"\d+ RPM", op[4]), op
  207          except AssertionError as e:

  224                  assert op[2] == 'ok'
  225:                 if re.search(r"PSU\d+ Status", op[0]):
  226                      assert op[4].lower() == 'presence detected'
  227:                 elif re.search(r"PSU\d+ Power", op[0]):
  228:                     assert re.search(r"\d+ Watts", op[4])
  229          except AssertionError as e:

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_local.py:
   39      try:
   40:         assert re.search(r'\d+', info_dict['Record Count']), \
   41              info_dict['Record Count']
   42:         assert re.search(r'\d+ bytes', info_dict['Free Space']), \
   43              info_dict['Free Space']

   55          for op in status_list:
   56:             if re.search("fan", op[0].lower()) and op[1] != 'no reading':
   57:                 assert re.search(r'\d+ RPM', op[1]), op
   58      except AssertionError as e:

   68          for op in status_list:
   69:             if re.search(("temp", op[0].lower()) and
   70                           op[1].lower() != 'no reading'):
   71:                 assert re.search(r'\d+ degrees C', op[1]), op
   72      except AssertionError as e:

   82          for op in status_list:
   83:             if re.search("hdd", op[0].lower()) and op[1] != 'no reading':
   84:                 assert re.search(r'\d+ degrees C', op[1]), op
   85      except AssertionError as e:

   95          for op in status_list:
   96:             if re.search(("cpu_dimm*", op[0].lower()) and
   97                           op[1].lower() != 'no reading'):
   98:                 assert re.search(r'\d+ degrees C', op[1]), op
   99:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  100:                 assert re.search(r'^\d+\.?\d* Volts', op[1]), op
  101      except AssertionError as e:

  111          for op in status_list:
  112:             if re.search("power", op[0].lower()) and op[1] != 'no reading':
  113:                 assert re.search(r'\d+ Watts', op[1]), op
  114      except AssertionError as e:

  139                  assert op[2] == 'ok', op
  140:                 if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  141:                     assert re.search(r'\d+ degrees C', op[4]), op
  142      except AssertionError as e:

  154                  assert op[2] == 'ok', op
  155:                 assert re.search(r'\d+\.\d+ Volts', op[4]), op
  156      except AssertionError as e:

  167              assert op[2] == 'ok', op
  168:             assert re.search(r'\d+ RPM', op[4]), op
  169      except AssertionError as e:

  180              assert op[2] == 'ok', op
  181:             if re.search(r'PSU\d+ Status', op[0]):
  182                  assert op[4].lower() == 'presence detected'
  183:             elif re.search(r'PSU\d+ Power', op[0]):
  184:                 assert re.search(r'\d+ Watts', op[4])
  185      except AssertionError as e:

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_external.py:
   81          assert sel_info_dict['Entries'] == '3'
   82:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   83              sel_info_dict['Version']
   84:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   85              sel_info_dict['Entries']
   86:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
   87              sel_info_dict['Free Space']
   88:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
   89              sel_info_dict['Percent Used']

  102          assert sel_info_dict['Entries'] == '3'
  103:         assert re.search(r"^1.5", sel_info_dict['Version']), \
  104              sel_info_dict['Version']
  105:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  106              sel_info_dict['Entries']
  107:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  108              sel_info_dict['Free Space']
  109:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  110              sel_info_dict['Percent Used']

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_ipmb.py:
   94          assert sel_info_dict['Entries'] == '3'
   95:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   96              sel_info_dict['Version']
   97:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   98              sel_info_dict['Entries']
   99:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  100              sel_info_dict['Free Space']
  101:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  102              sel_info_dict['Percent Used']

  117          assert sel_info_dict['Entries'] == '3'
  118:         assert re.search(r"^1.5", sel_info_dict['Version']), \
  119              sel_info_dict['Version']
  120:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  121              sel_info_dict['Entries']
  122:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  123              sel_info_dict['Free Space']
  124:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  125              sel_info_dict['Percent Used']

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_local.py:
   90              assert sel_info_dict['Entries'] == '3'
   91:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   92              sel_info_dict['Version']
   93:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   94              sel_info_dict['Entries']
   95:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
   96              sel_info_dict['Free Space']
   97:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
   98              sel_info_dict['Percent Used']

  114              assert sel_info_dict['Entries'] == '4'
  115:         assert re.search("^1.5", sel_info_dict['Version']), \
  116              sel_info_dict['Version']
  117:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  118              sel_info_dict['Entries']
  119:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  120              sel_info_dict['Free Space']
  121:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  122              sel_info_dict['Percent Used']

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_set_ip_source.py:
  100          assert ip_dict['ip_source'] == 'dhcp'
  101:         assert re.search(r"(\d+\.){3}\d+", ip_dict['ip_source']), \
  102              ip_dict['ip_source']
  103:         assert re.search(r"(\d+\.){3}\d+", ip_dict['subnet_mask']), \
  104              ip_dict['subnet_mask']
  105:         assert re.search(r"(\d+\.){3}\d+", ip_dict['gateway']), \
  106              ip_dict['gateway']

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc_stress\test_bmc_stress_rios_power_cycle.py:
  141      proc_ipmi_stats = shell.exec_command(cmd)
  142:     if (re.search(r'sent_ipmb_command_errs:\s+\d{1,3}\s+',
  143                    proc_ipmi_stats) and
  144:             re.search(r'sent_lan_command_errs:\s+\d{1,3}\s+',
  145                        proc_ipmi_stats) and
  146:             re.search(r'retransmitted_lan_commands:\s+\d{1,3}\s+',
  147                        proc_ipmi_stats) and
  148:             re.search(r'timed_out_lan_commands:\s+\d{1,3}\s+',
  149                        proc_ipmi_stats) and
  150:             re.search(r'sent_lan_responses:\s+\d{1,3}\s+',
  151                        proc_ipmi_stats) and
  152:             re.search(r'handled_lan_responses:\s+\d{1,3}\s+',
  153                        proc_ipmi_stats) and
  154:             re.search(r'invalid_lan_responses:\s+\d{1,3}\s+',
  155                        proc_ipmi_stats) and
  156:             re.search(r'unhandled_lan_responses:\s+\d{1,3}\s+',
  157                        proc_ipmi_stats)):

  242          box_type = ipmitool_rios_lan.run("fru list")
  243:         if(re.search("2U", box_type)):
  244              logger.info("##### BLUEFIN-2U #########")

  262                                   "169.254.0.101"]
  263:         elif(re.search("1U", box_type)):
  264              logger.info("##### BLUEFIN-1U #########")

  328          mc_info = ipmitool_rios_lan.run("mc info")
  329:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  330          mc_info_status["rios_aux"][0] = mc_info_status["rios_aux"][0] + 1

  348          mc_info = ipmitool_rios.run("mc info")
  349:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  350          mc_info_status["rios_local"][0] = mc_info_status["rios_local"][0] + 1

  369          mc_info = ipmitool_vsp_lan.run("mc info")
  370:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  371          mc_info_status["vsp_aux"][0] = mc_info_status["vsp_aux"][0] + 1

  389          mc_info = ipmitool_vsp.run("mc info")
  390:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  391          mc_info_status["vsp_ipmb"][0] = mc_info_status["vsp_ipmb"][0] + 1

  412          for op in status_list:
  413:             if (re.search("no reading", op[1]) or
  414:                     re.search("Not Readable", op[1])):
  415                  assert op[2] == "ns", op

  438          for op in status_list:
  439:             if (re.search("no reading", op[1]) or
  440:                     re.search("Not Readable", op[1])):
  441                  assert op[2] == "ns", op

  466          for op in status_list:
  467:             if (re.search("no reading", op[1]) or
  468:                     re.search("Not Readable", op[1])):
  469                  assert op[2] == "ns", op

  494          for op in status_list:
  495:             if (re.search("no reading", op[1]) or
  496:                     re.search("Not Readable", op[1])):
  497                  assert op[2] == "ns", op

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc_stress\test_bmc_stress.py:
  137      proc_ipmi_stats = shell.exec_command(cmd)
  138:     if (re.search(r'sent_ipmb_command_errs:\s+\d{1,3}\s+',
  139                    proc_ipmi_stats) and
  140:             re.search(r'sent_lan_command_errs:\s+\d{1,3}\s+',
  141                        proc_ipmi_stats) and
  142:             re.search(r'retransmitted_lan_commands:\s+\d{1,3}\s+',
  143                        proc_ipmi_stats) and
  144:             re.search(r'timed_out_lan_commands:\s+\d{1,3}\s+',
  145                        proc_ipmi_stats) and
  146:             re.search(r'sent_lan_responses:\s+\d{1,3}\s+',
  147                        proc_ipmi_stats) and
  148:             re.search(r'handled_lan_responses:\s+\d{1,3}\s+',
  149                        proc_ipmi_stats) and
  150:             re.search(r'invalid_lan_responses:\s+\d{1,3}\s+',
  151                        proc_ipmi_stats) and
  152:             re.search(r'unhandled_lan_responses:\s+\d{1,3}\s+',
  153                        proc_ipmi_stats)):

  237          box_type = ipmitool_rios_lan.run("fru list")
  238:         if(re.search("2U", box_type)):
  239              logger.info("##### BLUEFIN-2U #########")

  257                                   "169.254.0.101"]
  258:         elif(re.search("1U", box_type)):
  259              logger.info("##### BLUEFIN-1U #########")

  354              mc_info = ipmitool_rios_lan.run("mc info")
  355:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  356              mc_info_status["rios_aux"][0] = mc_info_status["rios_aux"][0] + 1

  374              mc_info = ipmitool_rios.run("mc info")
  375:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  376              mc_info_status["rios_local"][0] = \

  397              mc_info = ipmitool_vsp_lan.run("mc info")
  398:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  399              mc_info_status["vsp_aux"][0] = mc_info_status["vsp_aux"][0] + 1

  417              mc_info = ipmitool_vsp.run("mc info")
  418:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  419              mc_info_status["vsp_ipmb"][0] = mc_info_status["vsp_ipmb"][0] + 1

  440              for op in status_list:
  441:                 if (re.search("no reading", op[1]) or
  442:                         re.search("Not Readable", op[1])):
  443                      assert op[2] == "ns", op

  466              for op in status_list:
  467:                 if (re.search("no reading", op[1]) or
  468:                         re.search("Not Readable", op[1])):
  469                      assert op[2] == "ns", op

  496              for op in status_list:
  497:                 if (re.search("no reading", op[1]) or
  498:                         re.search("Not Readable", op[1])):
  499                      assert op[2] == "ns", op

  524              for op in status_list:
  525:                 if (re.search("no reading", op[1]) or
  526:                         re.search("Not Readable", op[1])):
  527                      assert op[2] == "ns", op

dist-packages\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\hwtool\tests_hwtool.py:
  1173          logger.info("Actual Output: [" + actual_output + "]")
  1174:         elements = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)", actual_output)
  1175          # Validating CPU core count

  1265              # Verifying Slots
  1266:             elements = re.search(r"Slot\s+(\d+):\s\.{10}\s([^,]*),\s(.*)",
  1267                                   line)

  1275                  # Verifying Hardware revision
  1276:                 elements = re.search(r"Hardware revision:\s+([\d\D]+)", line)
  1277                  if elements is not None:

  1279                  else:
  1280:                     elements = re.search(r"Mainboard:\s[^,]*,\s(.*)", line)
  1281                      if elements is not None:

  1338              system_section = section
  1339:     elements = re.search(r".*Product\s*:\s*(.*)", system_section)
  1340      actual_motherboard_number = elements.group(1)

  1445          for line in lines:
  1446:             if re.search(r"disk.*", line) is not None:
  1447                  elements = line.split()

  1458          for line in lines:
  1459:             if re.search(r"\w", line):
  1460                  elements = line.split()

dist-packages\portfolio_system_tests\legacy_exchange_tests\tests\test_allocation_health.py:
   64  
   65:         match = re.search(r'received, (?P<loss>\d+.*)\s*% packet loss,',
   66                            output)

  145                r'\s*% loss\)')
  146:     match = re.search(target, output)
  147      if not match:

dist-packages\portfolio_system_tests\legacy_exchange_tests\tests\test_smoke_mess.py:
  38      ITEMS_RE = r'ItemsInFolder\s+-------------\s+(?P<items>\d+)'
  39:     match = re.search(ITEMS_RE, output)
  40      return int(match.group('items'))

dist-packages\portfolio_system_tests\legacy_gluon\libs\__init__.py:
  360      # Example: "hostname":"XNCC58DC4E4D4408",
  361:     sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  362      if not sobj:

dist-packages\portfolio_system_tests\legacy_gluon\tests\test_firewall_rules_after_failover_vgw.py:
  127      regex = re.escape(str1) + r'\n(.*)$'
  128:     sobj1 = re.search(regex, output, re.MULTILINE | re.DOTALL)
  129      if sobj1:

  182      # Format of uptime: 35d  0h  54m
  183:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  184      if not sobj:

dist-packages\portfolio_system_tests\legacy_gluon\tests\test_firewall_rules_after_reboot_vgw.py:
  126      regex = re.escape(str1) + r'\n(.*)$'
  127:     sobj1 = re.search(regex, output, re.MULTILINE | re.DOTALL)
  128      if sobj1:

  191          # Example: "hostname":"XNCC58DC4E4D4408",
  192:         sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  193          if not sobj:

  223      # Format of uptime: 35d  0h  54m
  224:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  225      if not sobj:

dist-packages\portfolio_system_tests\legacy_gluon\tests\test_internet_and_site_to_site.py:
  123      # Example: "hostname":"XNCC58DC4E4D4408",
  124:     sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  125      if not sobj:

  363      # Resolving facebook.com (facebook.com)... 31.13.90.36, 2a03..
  364:     sobj = re.search(r'\(facebook\.com\)\.\.\.\s+(.*),', lines[2])
  365      if sobj:

  407      # Resolving youtube.com (youtube.com)... 216.58.194.206, 2607
  408:     sobj = re.search(r'\(youtube\.com\)\.\.\.\s+(.*),', lines[2])
  409      if sobj:

  450      # Format of uptime: 35d  0h  54m
  451:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  452      if not sobj:

dist-packages\portfolio_system_tests\legacy_gluon\tests\test_overnight_failover_pingpong.py:
  78  
  79:     match = re.search(r'(?<=\()\S+?(?=\) port \d+)', output)
  80      if match:

dist-packages\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\conftest.py:
  397  
  398:     if re.search("different_unique_ib_ob", test_case):
  399          logger.info("[INFO]: cleanup after different_unique_ib_ob")

  496          for line in profile_data.raw.split("\n"):
  497:             result = re.search(r"(\*\w+\*)\s+\d+\s+(\d+)\s+(\d+)",
  498                                 profile_data.raw)

  518      """
  519:     if re.search("same_default_ib_ob", test_case):
  520          init_qos_device_configurator.config.manage_sites(7)
  521          init_qos_device_configurator.config.manage_sites(8)
  522:     elif re.search("unique_ib_default_ob", test_case):
  523          init_qos_device_configurator.config.manage_sites(7)
  524:     elif re.search("default_ib_unique_ob", test_case):
  525          init_qos_device_configurator.config.manage_sites(8)
  526:     elif re.search("different_unique_ib_ob", test_case):
  527          init_qos_device_configurator.config.manage_profiles(9)

  549  
  550:     if re.search("same_default|default_ob", test_case):
  551:         if re.search("^.*DSCP_P$", test_case):
  552              init_qos_device_configurator.config.manage_classes(21)
  553  
  554:         if re.search("^.*DSCP_L$", test_case):
  555              init_qos_device_configurator.config.manage_classes(38)
  556  
  557:         if re.search("^.*DSCP_R$", test_case):
  558              init_qos_device_configurator.config.manage_rules(3)
  559  
  560:         if re.search("^.*DSCP_PL$", test_case):
  561              init_qos_device_configurator.config.manage_classes(21)

  563  
  564:         if re.search("^.*DSCP_PR$", test_case):
  565              init_qos_device_configurator.config.manage_classes(21)

  567  
  568:         if re.search("^.*DSCP_LR$", test_case):
  569              init_qos_device_configurator.config.manage_classes(38)

  571  
  572:         if re.search("^.*DSCP_PLR$", test_case):
  573              init_qos_device_configurator.config.manage_classes(21)

  577      else:
  578:         if re.search("^.*DSCP_P$", test_case):
  579              init_qos_device_configurator.config.manage_classes(26)
  580  
  581:         if re.search("^.*DSCP_L$", test_case):
  582              init_qos_device_configurator.config.manage_classes(34)
  583  
  584:         if re.search("^.*DSCP_R$", test_case):
  585              init_qos_device_configurator.config.manage_rules(5)
  586  
  587:         if re.search("^.*DSCP_PL$", test_case):
  588              init_qos_device_configurator.config.manage_classes(26)

  590  
  591:         if re.search("^.*DSCP_PR$", test_case):
  592              init_qos_device_configurator.config.manage_classes(26)

  594  
  595:         if re.search("^.*DSCP_LR$", test_case):
  596              init_qos_device_configurator.config.manage_classes(34)

  598  
  599:         if re.search("^.*DSCP_PLR$", test_case):
  600              init_qos_device_configurator.config.manage_classes(26)

  622  
  623:     if re.search("same_default|default_ob", test_case):
  624:         if re.search("^.*DSCP_P$", test_case):
  625              init_qos_device_configurator.config.manage_classes(25)
  626  
  627:         if re.search("^.*DSCP_L$", test_case):
  628              init_qos_device_configurator.config.manage_classes(39)
  629  
  630:         if re.search("^.*DSCP_R$", test_case):
  631              init_qos_device_configurator.config.manage_rules(4)
  632  
  633:         if re.search("^.*DSCP_PL$", test_case):
  634              init_qos_device_configurator.config.manage_classes(25)

  636  
  637:         if re.search("^.*DSCP_PR$", test_case):
  638              init_qos_device_configurator.config.manage_classes(25)

  640  
  641:         if re.search("^.*DSCP_LR$", test_case):
  642              init_qos_device_configurator.config.manage_classes(39)

  644  
  645:         if re.search("^.*DSCP_PLR$", test_case):
  646              init_qos_device_configurator.config.manage_classes(25)

  650      else:
  651:         if re.search("^.*DSCP_P$", test_case):
  652              init_qos_device_configurator.config.manage_classes(30)
  653  
  654:         if re.search("^.*DSCP_L$", test_case):
  655              init_qos_device_configurator.config.manage_classes(35)
  656  
  657:         if re.search("^.*DSCP_R$", test_case):
  658              init_qos_device_configurator.config.manage_rules(6)
  659  
  660:         if re.search("^.*DSCP_PL$", test_case):
  661              init_qos_device_configurator.config.manage_classes(30)

  663  
  664:         if re.search("^.*DSCP_PR$", test_case):
  665              init_qos_device_configurator.config.manage_classes(30)

  667  
  668:         if re.search("^.*DSCP_LR$", test_case):
  669              init_qos_device_configurator.config.manage_classes(35)

  671  
  672:         if re.search("^.*DSCP_PLR$", test_case):
  673              init_qos_device_configurator.config.manage_classes(30)

dist-packages\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_inbound_qos_dscp_full_combinations.py:
   89      try:
   90:         if re.search("same_default|default_ob", test_case):
   91              init_qos_device_configurator.config.manage_classes(37)
   92  
   93:             if re.search("unique_ib_default_ob", test_case):
   94                  qos = init_qos_device_configurator.config.\

  119  
  120:             if re.search("^.*DSCP_P$", test_case):
  121                  expected_ob_qos_dscp = 0
  122  
  123:             if re.search("^.*DSCP_L$", test_case):
  124                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  125  
  126:             if re.search("^.*DSCP_R$", test_case):
  127                  expected_ob_qos_dscp = default_outbound_dscp_rule
  128  
  129:             if re.search("^.*DSCP_PL$", test_case):
  130                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  131  
  132:             if re.search("^.*DSCP_PR$", test_case):
  133                  expected_ob_qos_dscp = default_outbound_dscp_rule
  134  
  135:             if re.search("^.*DSCP_LR$", test_case):
  136                  expected_ob_qos_dscp = default_outbound_dscp_rule
  137  
  138:             if re.search("^.*DSCP_PLR$", test_case):
  139                  expected_ob_qos_dscp = default_outbound_dscp_rule

  143  
  144:             if re.search("default_ib_unique_ob", test_case):
  145                  qos = init_qos_device_configurator.config.\

  148  
  149:             elif re.search("different_unique_ib_ob", test_case):
  150                  qos = init_qos_device_configurator.config.\

  175  
  176:             if re.search("^.*DSCP_P$", test_case):
  177                  expected_ob_qos_dscp = 0
  178  
  179:             if re.search("^.*DSCP_L$", test_case):
  180                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  181  
  182:             if re.search("^.*DSCP_R$", test_case):
  183                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  184  
  185:             if re.search("^.*DSCP_PL$", test_case):
  186                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  187  
  188:             if re.search("^.*DSCP_PR$", test_case):
  189                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  190  
  191:             if re.search("^.*DSCP_LR$", test_case):
  192                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  193  
  194:             if re.search("^.*DSCP_PLR$", test_case):
  195                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  281  
  282:         if re.search("same_default|default_ob", test_case):
  283              init_qos_device_configurator.config.manage_rules(7)

dist-packages\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_outbound_qos_dscp_full_combinations.py:
   89      try:
   90:         if re.search("same_default|default_ob", test_case):
   91              init_qos_device_configurator.config.manage_classes(37)

  113  
  114:             if re.search("^.*DSCP_P$", test_case):
  115                  expected_ob_qos_dscp = 0
  116  
  117:             if re.search("^.*DSCP_L$", test_case):
  118                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  119  
  120:             if re.search("^.*DSCP_R$", test_case):
  121                  expected_ob_qos_dscp = default_outbound_dscp_rule
  122  
  123:             if re.search("^.*DSCP_PL$", test_case):
  124                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  125  
  126:             if re.search("^.*DSCP_PR$", test_case):
  127                  expected_ob_qos_dscp = default_outbound_dscp_rule
  128  
  129:             if re.search("^.*DSCP_LR$", test_case):
  130                  expected_ob_qos_dscp = default_outbound_dscp_rule
  131  
  132:             if re.search("^.*DSCP_PLR$", test_case):
  133                  expected_ob_qos_dscp = default_outbound_dscp_rule

  158  
  159:             if re.search("^.*DSCP_P$", test_case):
  160                  expected_ob_qos_dscp = 0
  161  
  162:             if re.search("^.*DSCP_L$", test_case):
  163                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  164  
  165:             if re.search("^.*DSCP_R$", test_case):
  166                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  167  
  168:             if re.search("^.*DSCP_PL$", test_case):
  169                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  170  
  171:             if re.search("^.*DSCP_PR$", test_case):
  172                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  173  
  174:             if re.search("^.*DSCP_LR$", test_case):
  175                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  176  
  177:             if re.search("^.*DSCP_PLR$", test_case):
  178                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  250  
  251:         if re.search("same_default|default_ob", test_case):
  252              init_qos_device_configurator.config.manage_rules(7)

dist-packages\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_qos_device_all_classification.py:
  213      """
  214:     if re.search('-sh', test_case):
  215          check_qos_on_IC = 0

  217  
  218:     elif re.search('-ic', test_case):
  219          check_qos_on_IC = 1

  224  
  225:     if re.search('-IN', test_case):
  226          QoS_Flags = 1

  233  
  234:     elif re.search('-OUT', test_case):
  235          QoS_Flags = 0

  242  
  243:     if re.search('-UniqueSite', test_case):
  244          is_UniqueSite = 1

  247  
  248:     elif re.search('-DefaultSite', test_case):
  249          is_UniqueSite = 0

  294      try:
  295:         if re.search('same_unique_ib_ob', test_case):
  296              # The same unique profile is used for Inbound and outbound.

  309  
  310:         elif re.search('same_default_ib_ob', test_case):
  311              # Default profile is used for both Inbound and outbound traffic.

  325  
  326:         elif re.search('default_ib_unique_ob', test_case):
  327              # Default profile is used for inbound and

  342  
  343:         elif re.search('unique_ib_default_ob', test_case):
  344              # Default profile is used for outbound and

  358  
  359:         elif re.search('different_unique_ib_ob', test_case):
  360              # Different unique profiles for outbound and inbound traffic.

  431              # Checking for optimized or passthrough traffic
  432:             if re.search('-noOpt', test_case):
  433                  verify_opt(sh_resource=test_objects.client_sh,

  439  
  440:             elif re.search('-Opt', test_case):
  441                  verify_opt(sh_resource=test_objects.client_sh,

dist-packages\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_qos_dscp_full_combinations.py:
   88      try:
   89:         if re.search("same_default|default_ob", test_case):
   90              init_qos_device_configurator.config.manage_classes(37)
   91  
   92:             if re.search("unique_ib_default_ob", test_case):
   93                  qos = init_qos_device_configurator.config.\

  123  
  124:             if re.search("^.*DSCP_P$", test_case):
  125                  expected_ob_qos_dscp = 0
  126  
  127:             if re.search("^.*DSCP_L$", test_case):
  128                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  129  
  130:             if re.search("^.*DSCP_R$", test_case):
  131                  expected_ob_qos_dscp = default_outbound_dscp_rule
  132  
  133:             if re.search("^.*DSCP_PL$", test_case):
  134                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  135  
  136:             if re.search("^.*DSCP_PR$", test_case):
  137                  expected_ob_qos_dscp = default_outbound_dscp_rule
  138  
  139:             if re.search("^.*DSCP_LR$", test_case):
  140                  expected_ob_qos_dscp = default_outbound_dscp_rule
  141  
  142:             if re.search("^.*DSCP_PLR$", test_case):
  143                  expected_ob_qos_dscp = default_outbound_dscp_rule

  147  
  148:             if re.search("default_ib_unique_ob", test_case):
  149                  qos = init_qos_device_configurator.config.\

  152  
  153:             elif re.search("different_unique_ib_ob", test_case):
  154                  qos = init_qos_device_configurator.config.\

  184  
  185:             if re.search("^.*DSCP_P$", test_case):
  186                  expected_ob_qos_dscp = 0
  187  
  188:             if re.search("^.*DSCP_L$", test_case):
  189                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  190  
  191:             if re.search("^.*DSCP_R$", test_case):
  192                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  193  
  194:             if re.search("^.*DSCP_PL$", test_case):
  195                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  196  
  197:             if re.search("^.*DSCP_PR$", test_case):
  198                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  199  
  200:             if re.search("^.*DSCP_LR$", test_case):
  201                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  202  
  203:             if re.search("^.*DSCP_PLR$", test_case):
  204                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  300  
  301:         if re.search("same_default|default_ob", test_case):
  302              init_qos_device_configurator.config.manage_rules(7)

dist-packages\portfolio_system_tests\legacy_netint_tests\tests\legacy\Securetransport\sectp_ms2_nat_integ.py:
  31      """
  32:     m = re.search(r"Runner - Tests planned:\s+(\d+)", log)
  33      planned_tc = m.group(1)
  34:     m = re.search(r"Runner - Tests passed:\s+(\d+)", log)
  35      passed_tc = m.group(1)

  47      """
  48:     match = re.search(r"1 passed in (\d+)", log)
  49      if match:

dist-packages\portfolio_system_tests\legacy_ns\service_chain_manager\service_chain_manager\test\orclibs\traffic_parser.py:
  51      hwaddr = None
  52:     eth_match = re.search(r'(ether|HWaddr)\s(?:addr:)*(\S+)', output)
  53      if eth_match:

dist-packages\portfolio_system_tests\legacy_ns_tests\ibt\tests\Guest_Zone_Support\test_local_internet_breakout.py:
  79      for line in output_lines:
  80:         maskmatch = re.search(r'\s' + interface, line, re.IGNORECASE)
  81          if maskmatch:

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\cf3\DHCP_DNS\test_DHCP_relay_via_overlay_to_DC.py:
   90      for zone in zones:
   91:         if re.search(site_1['name'], zone.site):
   92              branch_net = zone.networks[0]

  130          for zone in zones:
  131:             if re.search(site_1['name'], zone.site):
  132                  configurator.scm_actor.config.change_network(

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\cf3\QoS\test_aggregate_traffic_with_mixed_traffic_class.py:
  115      for line in output.split("\n"):
  116:         bandwidth = re.search(r'\d+\.\d+mbps', line)
  117          if not bandwidth:

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_add_new_tep_ips_in_dc_uplinks.py:
  205          for dcuplink in dc_old_wan_teps:
  206:             if re.search('Internet', dcuplink):
  207                  public_ipv4 = str(resources.dc_public.cidr.ip)

  266          for dcuplink in dc_old_wan_teps:
  267:             if re.search('Internet', dcuplink):
  268                  public_ipv4 = str(resources.dc_public.cidr.ip)

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_data_ports_poweroff_update.py:
  215      for port in data_ports:
  216:         if re.search('PORT3', port.id, flags=re.IGNORECASE) or \
  217:                 re.search('PORT4', port.id, flags=re.IGNORECASE):
  218              resources.scm_actor.change_port(

  226          for port in data_ports:
  227:             if re.search('PORT3', port.id, flags=re.IGNORECASE) or \
  228:                     re.search('PORT4', port.id, flags=re.IGNORECASE):
  229                  resources.scm_actor.change_port(

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover_CF3.py:
  235      for zone in zone_list:
  236:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  237              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  251      for uplink in uplink_list:
  252:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  253:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  254                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  379          for zone in zones_list:
  380:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  381                  obj_added_zone = zone

  399                  for custom_app in custom_apps:
  400:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  401                                   flags=re.IGNORECASE):

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover.py:
  237      for zone in zone_list:
  238:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  239              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  253      for uplink in uplink_list:
  254:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  255:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  256                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  388          for zone in zones_list:
  389:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  390                  obj_added_zone = zone

  408                  for custom_app in custom_apps:
  409:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  410                                   flags=re.IGNORECASE):

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_leaf_site_checking_in_site_pool.py:
  440      for site in sites_lists:
  441:         if re.search('HQ', site.name):
  442              hq_site_name = site.name

  467          for dc_uplink in dc_uplinks:
  468:             if re.search(INTERNET,
  469                           dc_uplink.wan,

  709          for dc_uplink in dc_uplinks:
  710:             if re.search(INTERNET,
  711                           dc_uplink.wan,

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch_CF3.py:
  135      for zone in zone_list:
  136:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  137              zone_network = scm_actor.get_network(zone.networks[0])

  146      for uplink in uplink_list:
  147:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  148:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  149                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  176          for zone in zones_list:
  177:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  178                  obj_added_zone = zone

  192                  for custom_app in custom_apps:
  193:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  194                                   flags=re.IGNORECASE):

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch.py:
  135      for zone in zone_list:
  136:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  137              zone_network = scm_actor.get_network(zone.networks[0])

  146      for uplink in uplink_list:
  147:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  148:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  149                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  176          for zone in zones_list:
  177:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  178                  obj_added_zone = zone

  192                  for custom_app in custom_apps:
  193:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  194                                   flags=re.IGNORECASE):

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_size_change_for_site_moves.py:
  445      for site in sites_lists:
  446:         if re.search('HQ', site.name):
  447              hq_site_name = site.name

  473          for dc_uplink in dc_uplinks:
  474:             if re.search(INTERNET,
  475                           dc_uplink.wan,

  758          for dc_uplink in dc_uplinks:
  759:             if re.search(INTERNET,
  760                           dc_uplink.wan,

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch_CF3.py:
  264      for zone in zone_list:
  265:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  266              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  280      for uplink in uplink_list:
  281:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  282:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  283                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  402          for zone in zones_list:
  403:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  404                  obj_added_zone = zone

  422                  for custom_app in custom_apps:
  423:                     if re.search('CAT_CUSTOM_UDP',
  424                                   custom_app.name,

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch.py:
  264      for zone in zone_list:
  265:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  266              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  280      for uplink in uplink_list:
  281:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  282:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  283                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  403          for zone in zones_list:
  404:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  405                  obj_added_zone = zone

  423                  for custom_app in custom_apps:
  424:                     if re.search(
  425                          'CAT_CUSTOM_UDP',

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_dc_uplink.py:
  259      for dc_uplink in dc_uplinks:
  260:         if re.search(WAN,
  261                       dc_uplink.wan,

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_wan_CF3.py:
  304      for zone in zone_list:
  305:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  306              zone_obj = copy.copy(zone)

  317      for uplink in uplink_list:
  318:         if re.search(WAN, uplink.wan, flags=re.IGNORECASE):
  319              branch_name = test_objects.scm_actor.get_site(

  457          for wan_data in wans:
  458:             if re.search(WAN, wan_data.name, flags=re.IGNORECASE):
  459                  wan_id = wan_data.id

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_wan.py:
  308      for uplink in uplink_list:
  309:         if re.search(WAN, uplink.wan, flags=re.IGNORECASE):
  310              branch_name = test_objects.scm_actor.get_site(

  440          for wan_data in wans:
  441:             if re.search(WAN, wan_data.name, flags=re.IGNORECASE):
  442                  wan_id = wan_data.id

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone_CF3.py:
  193      output = shell.exec_command("cat /var/last_received_cdl.yaml")
  194:     match = re.search('subnet: ' + ipv4, output, flags=re.IGNORECASE)
  195      if match:

  209          output = shell.exec_command("ip rule list")
  210:         match = re.search(ipv4, output)
  211          if match:

  244      for zone in zone_list:
  245:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  246              # Getting old zone ip

  378          for custom_app in custom_apps:
  379:             if re.search('CAT_CUSTOM_UDP', custom_app.name,
  380                           flags=re.IGNORECASE):

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone.py:
  195      output = shell.exec_command("cat /var/last_received_cdl.yaml")
  196:     match = re.search('subnet: ' + ipv4, output, flags=re.IGNORECASE)
  197      if match:

  209          output = shell.exec_command("ip rule list")
  210:         match = re.search(ipv4, output)
  211          if match:

  245      for zone in zone_list:
  246:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  247              # Getting old zone ip

  379          for custom_app in custom_apps:
  380:             if re.search(
  381                  'CAT_CUSTOM_UDP',

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_uplink_wantype.py:
  357          # Example old_wan_name='Wan1',dc_uplink.wan='wan-Wan1-e63d40e499c3f0ab'
  358:         if re.search(old_wan_name,
  359                       dc_uplink.wan,

  395          # path_rule.path_preference[0]='wan-Wan1-e63d40e499c3f0ab'
  396:         if re.search(wan_name,
  397                       path_rule.path_preference[0],

  439          # Example uplink.name: "Wan1_Uplink"
  440:         if re.search(r'\bWan1_Uplink\b',
  441                       uplink.name,

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_wan_uplink_ipaddress.py:
  284      for uplink in uplink_list:
  285:         if re.search(WAN, uplink.name, flags=re.IGNORECASE):
  286              return uplink.name

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_zone_for_branch.py:
  181              for network_obj in network_list:
  182:                 if re.search(BRANCH, network_obj.site):
  183                      return network_obj

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_change_panther_db_address.py:
  147      for route in ic_ip_routes:
  148:         if re.search(network, route):
  149              flag = True

  161      for route in ic_ip_routes:
  162:         if re.search(network, route):
  163              flag = False

  279      for cluster_obj in clusters:
  280:         if re.search('Cluster1', cluster_obj.name, flags=re.IGNORECASE):
  281              old_proxy_ip = cluster_obj.proxy_ip

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_check_route_table.py:
  115      for route in ic_ip_routes:
  116:         if re.search(network, route):
  117              flag = True

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_int_service_restart.py:
  166      result = ic.show_info().raw
  167:     if re.search(status, str(result), flags=re.IGNORECASE):
  168          flag = True

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_modify_branch_subnet.py:
  207              for network_obj in network_list:
  208:                 if re.search(BRANCH, network_obj.site):
  209                      return network_obj

  225      for route in ic_ip_routes:
  226:         if re.search(network, route):
  227              flag = True

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\services\test_symmetrical_nat_port_dynamic_change.py:
  139      for uplink in uplink_list:
  140:         if re.search(r'\bWan1_Uplink\b',
  141                       uplink.name,

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_as_mismatch.py:
  126              shell.exec_command("grep remote_as /var/last_received_cdl.yaml")
  127:         hold = re.search('remote_as: 200', output)
  128          logger.info(output)

  167      logger.info(output)
  168:     holdtime = re.search('remote_as: 100', output)
  169      assert holdtime

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_nondefaults.py:
  124              "grep hold_time /var/last_received_cdl.yaml")
  125:         hold = re.search('hold_time: 10', output)
  126          logger.info(output)

  129              "grep keepalive_time /var/last_received_cdl.yaml")
  130:         keep = re.search('keepalive_time: 80', output)
  131          assert keep

  171      logger.info(output)
  172:     holdtime = re.search('hold_time: 60', output)
  173      assert holdtime

  175          "grep keepalive_time /var/last_received_cdl.yaml")
  176:     keep = re.search('keepalive_time: 180', output)
  177      assert keep

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_match.py:
  163              "grep password /var/last_received_cdl.yaml")
  164:         pword = re.search('password: thepassword', output)
  165          logger.info(output)

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_mismatch.py:
  139              "grep password /var/last_received_cdl.yaml")
  140:         pword = re.search('password: password', output)
  141          logger.info(output)

  189      logger.info(output)
  190:     pword = re.search('password: null', output)
  191      assert pword

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_ibgp_peering_on_wdr1_fails.py:
  327      for network in networks:
  328:         if not re.search('HQ', network.site):
  329              network_list.append(network.netv4)

  335          for subnet in subnet_splitted_list:
  336:             if not re.search(str(subnet), network, re.IGNORECASE):
  337                  higher_subnet_list.append(str(subnet))

dist-packages\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_subnet_splitting.py:
  227      for cluster_obj in clusters:
  228:         if re.search('Cluster1', cluster_obj.name, flags=re.IGNORECASE):
  229              cluster_id = cluster_obj.id

  288      for network in networks:
  289:         if not re.search('HQ', network.site):
  290              network_list.append(network.netv4)

  296          for subnet in subnet_splitted_list:
  297:             if not re.search(str(subnet), network, re.IGNORECASE):
  298                  higher_subnet_list.append(str(subnet))

dist-packages\portfolio_system_tests\legacy_scm_tests\legacy_tests\test_gw_via_rest\test_gw_via_rest.py:
  114      for uplink in uplinks:
  115:         if re.search('Internet', uplink.wan):
  116              continue

  204          uplink = scm_actor.config.get_uplink(uplink_id)
  205:         if re.search('Internet', uplink.wan):
  206              continue

dist-packages\portfolio_system_tests\legacy_shm_tests\shm_helper.py:
  122              # command output
  123:             app_content = re.search(search_pattern, cmd_output, re.DOTALL) \
  124                  .group(1).strip()

  142                  application_map['dest_port'] = int(dest[1])
  143:                 application_map['app_id'] = int(re.search(".*snoopy_app="
  144                                                  "(\\d+)", app).group(1)

  274              # from command output
  275:             status = re.search(search_pattern, cmd_output) \
  276                  .group(1).strip()

  302              # from command output
  303:             policy = re.search(search_pattern, cmd_output) \
  304                  .group(1).strip()

  379              wait_until_complete(timeout=WAIT_900_SECS)
  380:         result = re.search("\\[PASS\\]:", cmd_output)
  381  

  424          search_pattern = r'{(.*?)}'
  425:         product_code = re.search(search_pattern, cmd_output, re.DOTALL) \
  426              .group(1).strip()

  441          try:
  442:             return re.search(search_pattern, cmd_output, re.DOTALL) \
  443                  .group(1).strip()

dist-packages\portfolio_system_tests\legacy_shm_tests\zak\tests\conftest.py:
  180          try:
  181:             frmt_op = re.search(r"(.*?)Aliases", output,
  182                                  re.DOTALL).group(1).strip()

  187  
  188:         m = re.search("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*$", output)
  189          return (m.group(1))

dist-packages\portfolio_system_tests\legacy_shsaas_tests\tests\portal\test_allsaas_sku.py:
   63          portal_sca.action.add_platform_to_sku(SKU, 'noexist')
   64:     assert re.search("404", str(err404.value)) is not None
   65      with pytest.raises(VerificationError):

   78          portal_sca.action.add_platform_to_sku('noexist', PLATFORM)
   79:     assert re.search("404", str(err404.value)) is not None
   80      with pytest.raises(UnexpectedOutput) as another404:
   81          portal_sca.verification.verify_platforms_sku('noexist', PLATFORM)
   82:     assert re.search("404", str(another404.value)) is not None
   83  

   94          portal_sca.verification.verify_platforms_sku('nonexist', [PLATFORM])
   95:     assert re.search("404", str(err404.value)) is not None
   96  

  107          portal_sca.action.delete_platform_from_sku('noexist', PLATFORM)
  108:     assert re.search("404", str(err404.value)) is not None
  109  

  122              portal_sca.action.delete_platform_from_sku(SKU, valid_platform)
  123:         assert re.search("404", str(err404.value)) is not None
  124  

dist-packages\portfolio_system_tests\legacy_shsaas_tests\tests\portal\test_platforms.py:
  243                                         test_params.send_beta_fields)
  244:     assert re.search("400", str(err400.value)) is not None
  245  

  373              test_params.send_beta_fields)
  374:     assert re.search("400", str(err400.value)) is not None
  375  

dist-packages\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_hostlabel.py:
  228              # Extract class b address from resolved ips
  229:             subnet_extract = re.search(r"(^\d{1,3}\.\d{1,3})*",
  230                                         ip_address)

dist-packages\portfolio_system_tests\legacy_shsaas_tests\tests\SH\sepia\conftest.py:
   88      # get the md5 checksum value
   89:     checksum = re.search(r'([0-9a-fA-F]+)\s+', output)
   90      if (not checksum):

   98      # extract the filename from url for checksum
   99:     match_obj = re.search("//.*/(.*)$", url)
  100      server_file = SERVER_FILE_LOCATION + match_obj.group(1)

  136                  # Extract class A address from resolved ips
  137:                 subnet_extract = re.search(r"(^\d{1,3}\.)",
  138                                             ip_address)

dist-packages\portfolio_system_tests\legacy_ssi_tests\scripts\connect_to_scc.py:
   61          cmc_version_string = cmc_cli.exec_command('show info')
   62:         cmc_version = re.search(
   63              r'Version:.*',

   65                  'Version:', '').strip(r' \n\r\t')
   66:         steelhead_string = re.search(r'Steelheads.*\n\n\n',
   67                                       output,

   74          for steelhead in steelheads:
   75:             serial = re.search(r'Steelhead \w*', steelhead).\
   76                  group(0).replace('Steelhead ', '')
   77  
   78:             hostname = re.search(
   79                  r'\(.* /', steelhead).group(0).strip(r'(/ \n\t\r')
   80  
   81:             ip_addr = re.search(r'\d+\.\d+\.\d+\.\d+', steelhead).group(0)
   82  
   83:             ver_string = re.search(r'Version:.*', steelhead).\
   84                  group(0).replace('Version:', '').strip(r' \n\t\r')
   85:             version = re.search(r'\d+\.\d+\.\d+', ver_string).group(0)
   86  

   89                  ocs_connectivity = False
   90:                 connectivity = re.search(r'Connected:.*', steelhead).\
   91                      group(0).replace('Connected:', '').strip(r' \n\t\r')

   96                  ocs_connectivity = False
   97:                 connectivity = re.search(
   98                      r'SSH connection:.*', steelhead).group(0).\

  101                      gcl_connectivity = True
  102:                 connectivity = re.search(
  103                      r'HTTPS connection:.*', steelhead).group(0).\

  107  
  108:             build_no = re.search(r'#\d+', ver_string).group(0)
  109  
  110:             model = re.search(r'Model:.*', steelhead).\
  111                  group(0).replace('Model:', '').strip(r' \n\t\r')

  165      output = appl_cli.exec_command("show info")
  166:     serial = re.search(
  167          r'Serial:.*', output).group(0).replace('Serial:', '').strip(r' \n\t\r')

  169      output = appl_cli.exec_command("show cmc")
  170:     line = re.search(r'CMC hostname:.*', output).group(0)
  171      try:
  172:         current_cmc = re.search(r'\d+\.\d+\.\d+\.\d+', line).group(0)
  173      except Exception:

  257          output = appl_cli.exec_command("show cmc")
  258:         managed = re.search(r'Managed by CMC:.*', output).group(0).\
  259              replace('Managed by CMC:', '').strip(r' \n\t\r')
  260:         next_msg = re.search(r'Seconds until next message is sent:.*', output)
  261:         line = re.search(r'CMC hostname:.*', output).group(0)
  262          current_cmc_host = re.sub(

  266  
  267:         current_cmc_ip = re.search(r'\d+\.\d+\.\d+\.\d+',
  268                                     line).group(0).strip(r' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\scripts\install_image.py:
  63      for line in pipe.stdout:
  64:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  65                  is not None):

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\conftest.py:
  169          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  170:         serial = re.search(r'Serial:.*', info_string).group(0).\
  171              replace('Serial:', '').strip(' \n\t\r')

  186          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  187:         serial = re.search(r'Serial:.*', info_string).group(0).\
  188              replace('Serial:', '').strip(' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_hostsettings_policy_push.py:
  111      # verifing the primary and secondary dns server
  112:     sh_dns_names = re.search(r'Name server: .*\n.*\n', sh_dns_settings). \
  113          group(0).replace('Name server: ', '').strip(' \n\t\r').split('\n')

  123          model.show_web().raw
  124:     sh_proxy = re.search(r'Network Proxy:.*\n.*\n.*', sh_proxy_settings). \
  125          group(0).replace('Network Proxy:', '').strip(' \n\t\r').split('\n')
  126:     sh_proxy_name = re.search(r'Address:.*', sh_proxy[0]).group(0). \
  127          replace('Address:', '').strip(' \n\t\r')

  129          assert False, " The web proxy is not added in sh "
  130:     sh_port = re.search(r'Port:.*', sh_proxy[1]).group(0). \
  131          replace('Port:', '').strip(' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_inpath_mgmt_policy_push.py:
  123      # Verifying ipv4 inpath settings
  124:     sh_inpath_ip4 = re.search(r'IP address:.*', sh_inpath_settings).group(0).\
  125          replace('IP address:', '').strip(' \n\r\t')

  127          assert False, " IPv4 Address is not added in sh "
  128:     sh_inpath_mask = re.search(r'Netmask:.*', sh_inpath_settings).\
  129          group(0).replace('Netmask:', '').strip(' \n\r\t')

  132      # Verifying ipv6 inpath settings
  133:     sh_inpath_ip6 = re.search(
  134          r'IPv6 address:.*',

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_manage_appliances.py:
  102          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  103:         serial = re.search(r'Serial:.*', info_string).\
  104              group(0).replace('Serial:', '').strip(' \n\t\r')

  276      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  277:     serial = re.search(r'Serial:.*', info_string).\
  278          group(0).replace('Serial:', '').strip(' \n\t\r')

  317              appliance['hostname']].model.show_info().raw
  318:         health = re.search(r'Status:.*', info_text).group(0).\
  319              replace('Status:', '').strip(' \n\t\r')

  339              appliance['hostname']].model.show_info().raw
  340:         health = re.search(r'Status:.*', info_text).group(0).\
  341              replace('Status:', '').strip(' \n\t\r')

  369      info_string_1 = resources.sh_actors[sh1.hostname].model.show_info().raw
  370:     serial_1 = re.search(r'Serial:.*', info_string_1).group(0).\
  371          replace('Serial:', '').strip(' \n\t\r')

  382      info_string_2 = resources.sh_actors[sh2.hostname].model.show_info().raw
  383:     serial_2 = re.search(r'Serial:.*', info_string_2).group(0).\
  384          replace('Serial:', '').strip(' \n\t\r')

  447      info_string = resources.sh_actors[sh1.hostname].model.show_info().raw
  448:     serial = re.search(r'Serial:.*', info_string).group(0).\
  449          replace('Serial:', '').strip(' \n\t\r')

  464      status = resources.scc_actor.model.show_cmc_op_history().raw
  465:     assert 'failed' == re.search(r' *Unlock Vault *\w* *', status).\
  466          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  472      status = resources.scc_actor.model.show_cmc_op_history().raw
  473:     assert 'failed' == re.search(r' *Unlock Vault *\w* *', status).\
  474          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  480      status = resources.scc_actor.model.show_cmc_op_history().raw
  481:     assert 'success' == re.search(r' *Unlock Vault *\w* *', status).\
  482          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  518          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  519:         serial = re.search(r'Serial:.*', info_string).\
  520              group(0).replace('Serial:', '').strip(' \n\t\r')

  557          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  558:         serial = re.search(r'Serial:.*', info_string).\
  559              group(0).replace('Serial:', '').strip(' \n\t\r')

  610      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  611:     serial = re.search(r'Serial:.*', info_string).\
  612          group(0).replace('Serial:', '').strip(' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_ntp_over_ipv6.py:
  48          req_ntp_servers_parsed = \
  49:             re.search(r'NTP servers:.*\n\n',
  50                        req_ntp_servers,

  76      # Get current scc date from datetme string.
  77:     current_scc_date = re.search(
  78          r'Date: .*', scc_date_time_str).\

  80      # Get current scc time from datetme string.
  81:     current_scc_time = re.search(
  82          r'Time: .*', scc_date_time_str).\

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_ntp_policy_push.py:
  106          model.show_ntp().raw
  107:     sh_ntp_servers = re.search(
  108          r'NTP servers:.*\n.*\n.*\n.*',

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_operation_history.py:
   55      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   56:     serial = re.search(r'Serial:.*', info_string).\
   57          group(0).replace('Serial:', '').strip(' \n\t\r')

  111      op_history = resources.scc_actor.model.show_cmc_op_history().raw
  112:     assert 'rbm_user' in re.search(r'\n\n.*', op_history).\
  113          group(0), 'policy push operation is logged using a different user'

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_policy_push_for_non_admin_connected_appliances.py:
   93      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   94:     serial = re.search(r'Serial:.*', info_string).\
   95          group(0).replace('Serial:', '').strip(' \n\t\r')

  202      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  203:     serial = re.search(r'Serial:.*', info_string).\
  204          group(0).replace('Serial:', '').strip(' \n\t\r')

  312      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  313:     serial = re.search(r'Serial:.*', info_string).\
  314          group(0).replace('Serial:', '').strip(' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_scc_external_backup.py:
  316      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  317:     serial = re.search(r'Serial:.*', info_string).\
  318          group(0).replace('Serial:', '').strip(' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_smtp_policy_push.py:
  104          model.show_email().raw
  105:     sh_smtp_name = re.search(r'Mail hub:.*', sh_email_settings).group(0).\
  106          replace('Mail hub:', '').strip(' \n\r\t')

  108          assert False, " smtp server is not added in sh "
  109:     sh_smtp_port = re.search(r'Mail hub port:.*', sh_email_settings).\
  110          group(0).replace('Mail hub port:', '').strip(' \n\r\t')

  114      for item in ['Event emails', 'Failure emails']:
  115:         sh_emails = re.search(r'' + item + '.*\n.*\n.*\n.*\n',
  116                                sh_email_settings).group(0)
  117:         sh_is_enabled = re.search(r'Enabled:.*', sh_emails).\
  118              group(0).replace('Enabled:', '').strip(' \n\r\t')

  120              assert False, sh_emails + " is not enabled "
  121:         sh_recipients = re.search(r'Recipients:.*\n.*', sh_emails).\
  122              group(0).replace('Recipients:', '').strip(' \n\r\t').split(',')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_appliance_backup_restore.py:
  67          result = resources.sh_actors[sh.hostname].model.show_banner().raw
  68:         MOTD = re.search(
  69              r'MOTD:.*', result).group(0).replace('MOTD:', '').strip(' \n\r\t')

  83          result = resources.sh_actors[sh.hostname].model.show_banner().raw
  84:         MOTD = re.search(
  85              r'MOTD:.*', result).group(0).replace('MOTD:', '').strip(' \n\r\t')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_appliance_inventory.py:
   41          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   42:         serial = re.search(r'Serial:.*', info_string).group(0).\
   43              replace('Serial:', '').strip(' \n\t\r')

  123          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  124:         serial = re.search(r'Serial:.*', info_string).\
  125              group(0).replace('Serial:', '').strip(' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_generic_infrastructure_framework.py:
  125          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  126:         serial = re.search(r'Serial:.*', info_string).\
  127              group(0).replace('Serial:', '').strip(' \n\t\r')

  140          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  141:         serial = re.search(r'Serial:.*', info_string).\
  142              group(0).replace('Serial:', '').strip(' \n\t\r')

  161          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  162:         serial = re.search(r'Serial:.*', info_string).\
  163              group(0).replace('Serial:', '').strip(' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_kvm_cmc_installation.py:
  178          self.kvm_host.expect(self.kvm_scc_name + r' \(config\) #')
  179:         primary_hw_address = re.search(
  180              r'HW address:.*',

  198          self.kvm_host.expect(self.FOLDER_PROMPT)
  199:         licence1 = re.search(r'\r\n.*\r\n',
  200                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  202          self.kvm_host.expect(self.FOLDER_PROMPT)
  203:         licence2 = re.search(r'\r\n.*\r\n',
  204                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  206          self.kvm_host.expect(self.FOLDER_PROMPT)
  207:         licence3 = re.search(r'\r\n.*\r\n',
  208                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  226          self.kvm_host.expect(self.kvm_scc_name + r' \(config\) #')
  227:         self.aux_ip_address = re.search(
  228              r'IP address:.*',

  233          file.close()
  234:         aux_net_mask = re.search(
  235              r'Netmask:.*',

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_physical_cmc_installation.py:
  62      for line in pipe.stdout:
  63:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  64                  is not None):

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_scc_secure_transport.py:
  182          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  183:         serial = re.search(r'Serial:.*', info_string).\
  184              group(0).replace('Serial:', '').strip(' \n\t\r')

  200          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  201:         serial = re.search(r'Serial:.*', info_string).\
  202              group(0).replace('Serial:', '').strip(' \n\t\r')

  219          resources.client_sh.hostname].model.show_info().raw
  220:     serial = re.search(r'Serial:.*', info_string).\
  221          group(0).replace('Serial:', '').strip(' \n\t\r')

  241      # Get current scc date from datetme string.
  242:     current_scc_date = re.search(
  243          r'Date: .*', current_scc_time_str).\

  245      # Get current scc time from datetme string.
  246:     current_scc_time = re.search(
  247          r'Time: .*', current_scc_time_str).\

  280      # Get current scc date from datetme string.
  281:     current_scc_date = re.search(
  282          r'Date: .*', current_scc_time_str).\

  284      # Get current scc time from datetme string.
  285:     current_scc_time = re.search(
  286          r'Time: .*', current_scc_time_str).group(0).\

  339          resources.client_sh.hostname].model.show_info().raw
  340:     serial = re.search(r'Serial:.*', info_string).\
  341          group(0).replace('Serial:', '').strip(' \n\t\r')

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_stats_operation.py:
   71          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   72:         serial = re.search(r'Serial:.*', info_string).\
   73              group(0).replace('Serial:', '').strip(' \n\t\r')

  117      # Get current scc date from datetme string.
  118:     current_scc_date = re.search(
  119          r'Date: .*', current_scc_time_str).\

  121      # Get current scc time from datetme string.
  122:     current_scc_time = re.search(
  123          r'Time: .*', current_scc_time_str).\

  156      # Get current scc date from datetme string.
  157:     current_scc_date = re.search(
  158          r'Date: .*', current_scc_time_str).\

  160      # Get current scc time from datetme string.
  161:     current_scc_time = re.search(
  162          r'Time: .*', current_scc_time_str).\

  200      # Get current scc date from datetme string.
  201:     current_scc_date = re.search(
  202          r'Date: .*', current_scc_time_str).\

  204      # Get current scc time from datetme string.
  205:     current_scc_time = re.search(
  206          r'Time: .*', current_scc_time_str).\

dist-packages\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_virtual_cmc_installation.py:
  61      for line in pipe.stdout:
  62:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  63                  is not None):

dist-packages\portfolio_system_tests\legacy_steelconnect_performance\scaleperf_qa\libs\QAPerf.py:
   422                  first_run and not bi_directional:
   423:             if re.search('tx', key):
   424                  interfaces_keys.extend([key])
   425:             elif re.search('rx', key):
   426                  interfaces_keys.extend([key])

   470                              tx_data = re.compile(r'TX\sbytes:(\d+)')
   471:                             if re.search(rx_data, inter):
   472:                                 data1 = re.search(rx_data, inter)
   473                                  interface[ser + '_rx_data'] = data1.group(1)
   474:                             if re.search(tx_data, inter):
   475:                                 data2 = re.search(tx_data, inter)
   476                                  interface[ser + '_tx_data'] = data2.group(1)

   650              location = data_col + str(row)
   651:             temp = re.search(r'(\d+.*\d*)\s+\w', ws[location].value)
   652              record_tput = temp.group(1)

   694              break
   695:         # if not re.search('.+bits/sec', line):
   696          #     continue
   697  
   698:         # rate_found = re.search('Bytes\s+(\d+.*\d*)\s+(\wbits/sec)', line)
   699:         rate_found = re.search(pattern, line)
   700          if rate_found:

   750  
   751:         rate_found = re.search(pattern, line)
   752          if rate_found:

   895      for line in output_server.splitlines():
   896:         if re.search(r'iperf\s+.+', line):
   897:             output_server_new = re.search(r'(iperf\s+.+)', line)
   898              output_server = output_server_new.group(0)
   899      for line in output_client.splitlines():
   900:         if re.search(r'iperf\s+.+', line):
   901:             output_client_new = re.search(r'(iperf\s+.+)', line)
   902              output_client = output_client_new.group(0)

   927  
   928:         if re.search(r'8\.\d\.\d\.\s+Ethernet\s+Frame\s+Rates', row) or found:
   929              found = True
   930:             if re.search(
   931                      r'\d+\.*\d*\',\s+\'(\d+,*\d*\.*\d*)\',\s+\''
   932                      r'(\d*,*\d+\.*\d*)\'', row):
   933:                 data_new = re.search(
   934                      r'\d+\.*\d*\',\s+\'(\d+,*\d*\.*\d*)\',\s+\''

   941  
   942:         if re.search(r'8\.\d\.\d\.\d\.\sEthernet\s+Frame\s+Rates:\s1', row) \
   943                  and data_count:

  1800      regex = re.compile(r'(\w+)\s*(\d+)/(\d+)')
  1801:     if re.search(regex, untagged):
  1802:         untagged_data = re.search(regex, untagged)
  1803          slot = untagged_data.group(2)

  2250              break
  2251:         if re.search(pattern_loss, line):
  2252:             drop_rate = re.search(pattern_loss, line)
  2253              percent = float(drop_rate.group(1))
  2254              total_percent += percent
  2255:         if re.search(pattern_rate, line):
  2256:             rec_rate = re.search(pattern_rate, line)
  2257              rate_int = float(rec_rate.group(1))

  2316              break
  2317:         if re.search(pattern, line):
  2318              total_checked_count += 1
  2319:             drop_rate = re.search(pattern, line)
  2320              total_bytes = drop_rate.group(1)

  2327              total_percent += percent
  2328:         if re.search(pattern_sum, line):
  2329              sum_count += 1
  2330:             sum_rate = re.search(pattern_sum, line)
  2331              sum_int = float(sum_rate.group(2))

  2354      """
  2355:     rate = re.search(r'-B\s*(\d+)(\w{1,2})', client_opt)
  2356      old_rate = rate.group(1) + rate.group(2)

  2376      """
  2377:     rate = re.search(r'-b\s*(\d+)(\w{1,3})', client_opt)
  2378      old_rate = rate.group(1) + rate.group(2)

  2403      """
  2404:     rate = re.search(r'-b\s*(\d+)', bw_rate)
  2405      client_opt_rate = str(int(rate.group(1)))

  3176  
  3177:         if re.search(pattern, line):
  3178:             found = re.search(pattern, line)
  3179              new_rate = str(float(found.group(1)) * REDUCE_TRAFFIC_80_PERCENT)

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\add_additional_outbound_rules.py:
  75          total_rule_count += 1
  76:         m = re.search(r'Pod(\d+)_vgw_branch(\d+)_obrule(\d+)', rule['name'])
  77          if m:

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\add_additional_trafficpath_rules.py:
  78          total_rule_count += 1
  79:         m = re.search(r'Pod(\d+)_vgw_branch(\d+)_tpr(\d+)', rule['name'])
  80          if m:

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
  46      """
  47:     if (re.search(
  48          r'One or more ports have an IP allocation from this subnet',

  63      # the router UUID first and then deleting the stack
  64:     elif (re.search(
  65            r'it is required by one or more routes', delete_status)):

dist-packages\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\test_system_info_from_scm.py:
  216      for line in f:
  217:         if re.search(r'runsv nginx', line):
  218              process_data = line.split()

  229      for line in f:
  230:         if re.search(r'runsv postgresql', line):
  231              process_data = line.split()

  242      for line in f:
  243:         if re.search(r'runsv redis', line):
  244              process_data = line.split()

  255      for line in f:
  256:         if re.search(r'mojo/Cc.pl\b\s.*hydra.*', line):
  257              process_data = line.split()

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\devices_cli.py:
  185          'ifconfig | grep ' + interface)
  186:     mac_address = re.search("HWaddr {}".format(
  187          mac_pattern), mac_details).group(1)

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\syslog.py:
  177      pat = r"prefix=\W+{}\W+".format(prefix)
  178:     match = re.search(pat, conf)
  179      assert match is not None, "prefix {} not found in gw rsyslog config file" \

  342      for line in lines:
  343:         if re.search(msg, line) and re.search(prefix, line) and \
  344:                 re.search("<{}>".format(priority), line) and \
  345:                 re.search(serial, line):
  346              LOGGER.info("LOG message '{}' with prefix '{}', priority '{}',"

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\traffic.py:
  177      ping_result = shell.exec_command('ping {} -c {}'.format(host, count))
  178:     host_ip = re.search(
  179          r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', ping_result).group(0)

  264          cmd, curl_command_result))
  265:     http_status = re.search("HTTP/1.1 ([0-9]{3})", curl_command_result).group(
  266          1)

dist-packages\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler_client.py:
  106      ping_result = shell_default_ns(mgmt_ip, ping)
  107:     loss = re.search('([0-9]{1,3})%', ping_result).group(1)
  108      # Be more sloppy for low ping intervals, since first ping may fail

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\disjoint_wan\test_route_propagation.py:
  104      for line in tunnels:
  105:         match = re.search(r"vti(\d+\_\d+\_\d+).*remote\s"
  106                            r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

  293          # Check learned routes on CGW
  294:         if re.search(r"123\.123\.123\.0", cgw_routes):
  295              criteria += 1

  334          # Check learned routes on CGW
  335:         if re.search(r"123\.123\.123\.0", cgw_routes):
  336              fail_msg += "Route to 123.123.123.0 not retracted from CGW: "

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\disjoint_wan\helpers\utils.py:
  157      for tunnel in tunnels:
  158:         vti = re.search(r'(vti\d+_\d+_\d+)', tunnel)
  159          if vti:

  161  
  162:         remote = re.search(r'remote (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  163                             tunnel)

  167  
  168:         local = re.search(r'local (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  169                            tunnel)

  202          for line in conf:
  203:             if re.search(r"X.*{}".format(vti), line):
  204                  found += 1

  206              if found:
  207:                 check_line = re.search(
  208                      r".*checkip.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

  231      for line in lines:
  232:         top = re.search(
  233              r"^[\*\s][>\s][i\s]" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" +

  237              r"([\d\s]*)i?", line)
  238:         alt = re.search(
  239              r"^[\*\s][>\s][i\s]" + r"\s{17}" +

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_bgp_neighbor.py:
  37      for line in lines:
  38:         top = re.search(
  39              r"^[\*\s][>\s][i\s]\s" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" +

  42              r"([\d\s]*)[i\?]?", line)
  43:         alt = re.search(
  44              r"^[\*\s][>\s][i\s]" + r"\s+" +

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_default_route_originate.py:
   98      list_client = output.split('\n')
   99:     regex = re.search("\Send:\W+(\d+)\W+Recv:\W+(\d+)", list_client[0])  # noqa
  100      if regex:

  109      list_server = output.split('\n')
  110:     regex_server = re.search("Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)", list_server[0])  # noqa
  111      if regex_server:

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_dynamicrouting_bgp_bandwidth_limit.py:
  65      server_log = open(traffic.server_log_file, 'r').read()
  66:     bandwidth = re.search(r'(.\w?) Mbits/sec', server_log).group()
  67      bandwidth = bandwidth.replace('Mbits/sec', '').strip()

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_pqps.py:
  112      list_client = output.split('\n')
  113:     regex = re.search("\Send:\W+(\d+)\W+Recv:\W+(\d+)", list_client[0])  # noqa
  114      if regex:

  123      list_server = output.split('\n')
  124:     regex_server = re.search("Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)", list_server[0])  # noqa
  125      if regex_server:

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_static_routing.py:
  106      list_client = output.split('\n')
  107:     regex = re.search(r"\Send:\W+(\d+)\W+Recv:\W+(\d+)",
  108                        list_client[0])

  118      list_server = output.split('\n')
  119:     regex_server = re.search(r"Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)",
  120                               list_server[0])

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_zebos_config_check_bgp.py:
  44          elif line.strip().startswith('network') and \
  45:                 re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  46              gw_output['networks'].append(line.replace('network', '').strip())

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\conftest.py:
  119              ipPattern = re.compile(r'[0-9]+(?:\.[0-9]+){3}')
  120:             route = re.search(ipPattern, line).group()
  121              if route:

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\test_dynamic_routingwithha_gateway_link_failure.py:
  57      output = gw_shell.exec_command('imish -e "show ip route"')
  58:     if not re.search(zone_ip, output):
  59          pytest.fail("Zone ip is not present on the BGP route")
  60:     match = re.search(r'Total number of prefixes (\d+)', output)
  61      if match and int(match.group(1)) != 1:

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_new_zone_discovery.py:
  154      for element in gw_output.splitlines():
  155:         if re.search(network_ip, element):
  156              return True

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_remove_interface_from_area.py:
  105      for network in networks:
  106:         if re.search("discovered", network.name, re.IGNORECASE):
  107              count += 1

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_route_peering.py:
  46  
  47:             if re.search("Full", element):
  48                  ospf_neighbors.append(ip_address)

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_zebos_config_change.py:
  37          if line.strip().startswith('network') and \
  38:                 re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  39              gw_output['network'].append(re.findall(

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\ospf_multi_lan\test_traffic.py:
   47          for interface in if_op:
   48:             if re.search("192.168.15", if_op[interface]['addr']):
   49                  disabled_ints[router] = interface

  106      for interface in if_op:
  107:         if re.search("192.168.15", if_op[interface]['addr']):
  108              break

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\test_leaf_mode.py:
  97                  for line in chain.split('\n'):
  98:                     route = re.search('set-device ' + vti, line)
  99                      if route:

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\helpers\utils.py:
  31      for tunnel in tunnels:
  32:         vti = re.search(r'(vti\d+_\d+_\d+)', tunnel)
  33          if vti:

  35  
  36:         remote = re.search(r'remote (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  37                             tunnel)

  41  
  42:         local = re.search(r'local (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  43                            tunnel)

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\2gw_sh-1catfish-1gw\test_optimized_path_selection.py:
  175          for custom_app in custom_app_list:
  176:             if re.search("TCP_APP", custom_app.name, flags=re.IGNORECASE):
  177                  resources.org_obj.custom_app_management(

  189      for custom_app in custom_app_list:
  190:         if re.search("TCP_APP", custom_app.name, flags=re.IGNORECASE):
  191              custom_app_obj = custom_app

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\helpers\utils.py:
   138                  m = \
   139:                     re.search(r'(O\>\*|O\s\s)\s'
   140                                r'(\d+\.\d+\.\d+\.\d+\/\d+).*%s' % interface,

   142              else:
   143:                 m = re.search(r'(O\>\*|O\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)',
   144                                line)
   145          elif specific_route.lower() == 'bgp':
   146:             m = re.search(r'(B\>\*|B\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   147          elif specific_route.lower() == 'static':
   148:             m = re.search(r'(S\>\*|S\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   149          elif specific_route.lower() == 'connected':
   150:             m = re.search(r'(C\>\*|C\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   151          else:
   152:             m = re.search(r'(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   153          if m:

   202              if aspath is not None:
   203:                 m = re.search(r'(\d+\s\d+\s\d+)', line)
   204              else:
   205:                 m = re.search(r'(\d{5}\s\d{4})', line)
   206              if m is not None:

   356      for route in route_op.split("OSPF external")[1].split("\n"):
   357:         ips = re.search(r'(\d+\.\d+\.\d+\.\d+\/\d+)', route)
   358          metric_value = re.\
   359              search(r'((\[\d+\]|\[\d+/0\]|\[\d+/\d+\])\s\w+:\s\d+)', route)
   360:         type_route = re.search(r'(E\d)', route)
   361          if ips:

   902      ospf_int_output = container_shell.exec_command(cmd1)
   903:     cost = re.search(r'Cost: (\d+)', ospf_int_output)
   904:     priority = re.search(r'Priority (\d+)', ospf_int_output)
   905:     hello = re.search(r'Hello (\d+)', ospf_int_output)
   906:     dead = re.search(r'Dead (\d+)', ospf_int_output)
   907      return (cost.group(1), priority.group(1), hello.group(1), dead.group(1))

  1126      routes_info = container_shell.exec_command(cmd)
  1127:     routes_ip_info = map(lambda y: re.search(r'\s.(\d*.\d*.\d*.\d*)\s', y).
  1128                           group(0).strip(), routes_info.

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\upgrade\test_upgrade.py:
  125      print(univ_op)
  126:     latest_build_tag = re.search('binary_builds.*browse/(.+)', univ_op).\
  127          group(1)

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ospf_bgp_trio\test_ospf_failures.py:
  46      for network in networks:
  47:         if re.search("Discovered", network.name):
  48              count += 1

dist-packages\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ospf_bgp_trio\test_ospf_remove_interface_from_area.py:
  151      for network in networks:
  152:         if re.search("discovered", network.name, re.IGNORECASE):
  153              count += 1

dist-packages\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_hardware_spec_activate.py:
   70                                                          timeout=180)
   71:                     result = re.search(r'Stopped', result)
   72                      if result:

  121                                                      timeout=180)
  122:                 result = re.search(r'Healthy', result)
  123                  if result:

dist-packages\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability_client_sh.py:
  148          # The model extracted is in this form "VCX (VCX10)"
  149:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  150          sh_model_found = sh_model_detected.group(1)

dist-packages\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability_server_sh.py:
  158          # The model extracted is in this form "VCX (VCX10)"
  159:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  160          sh_model_found = sh_model_detected.group(1)

dist-packages\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability.py:
  189          # The model extracted is in this form "VCX (VCX10)"
  190:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  191          sh_model_found = sh_model_detected.group(1)

dist-packages\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_volume_size.py:
  160          # The model extracted is in this form "VCX (VCX10)"
  161:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  162          sh_model_found = sh_model_detected.group(1)

dist-packages\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\openstack-tests\openstack_ops.py:
  50              for stack_name in self.stack_name_list:
  51:                 search_string=re.search(r'jenkins-Axel-VSH-CAT-\d+_\w+',stack_name)
  52                  if search_string != None:

dist-packages\portfolio_system_tests\legacy_vsh_tests\provisioning\test_user_data.py:
  360                  if "Model" in line:
  361:                     m = re.search(r"\(([A-Za-z0-9_]+)\)", line)
  362                      print("Found Model: " + m.group(1))

  485      if(not invalid):
  486:         assert re.search(re.escape(expression),show_run)
  487      else:
  488:         assert re.search(re.escape(log_expression),show_rsisinit_log)
  489:         assert not re.search(re.escape(expression),show_run)
  490  

dist-packages\portfolio_system_tests\legacy_webcache_tests\http_server_allocation.py:
  317              cli_result = Model.get(fe).show_info()
  318:             if re.search("Service needs a 'restart'", cli_result.raw, re.I):
  319                  fes_to_restart.append(fe)

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\auditoperations.py:
   53      for line in zfile:
   54:         m = re.search(r"Created key with name='([^']+)' .* operation='Create"
   55                        " root CA", line)

   65      for line in zfile:
   66:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
   67                        "keyvault for user operation='Create root CA for "

   79      for line in zfile:
   80:         m = re.search(r"Create root CA for org=([^\s]+) CN=(.*) completed by "
   81                        "user='([^']*)' with signing key name='([^']+)'", line)

   92      for line in zfile:
   93:         m = re.search("-BEGIN CERTIFICATE-.*", line)
   94          if m:

  107      for line in zfile:
  108:         m = re.search(r"Created key with name='([^']+)' .* operation="
  109                        "'Create and activate root CA", line)

  120      for line in zfile:
  121:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
  122                        "keyvault for user operation='Create and activate root "

  134      for line in zfile:
  135:         m = re.search(r"Create and activate root CA for org=([^\\s]+) CN=(.*)"
  136                        "completed by user='([^']*)' with signing key name="

  148      for line in zfile:
  149:         m = re.search("-BEGIN CERTIFICATE-", line)
  150          if m:

  164      for line in zfile:
  165:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Signed digest='([^']+)' "
  166                        "using key='([^']+)' from keyvault for user operation="

  180      for line in zfile:
  181:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Sign peering cert request for CN="
  182                        "([^']+) from requestor=([^\\s]+) completed", line)

  193      for line in zfile:
  194:         m = re.search("-BEGIN CERTIFICATE-", line)
  195          if m:

  209      for line in zfile:
  210:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Signed digest='([^']+)' using "
  211                        "key='([^']+)' from keyvault for user operation="

  225      for line in zfile:
  226:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Sign proxy cert request for "
  227                        "CN=([^']+) from requestor=([^\\s]+) completed", line)

  238      for line in zfile:
  239:         m = re.search(".*-BEGIN CERTIFICATE-.*", line)
  240          if m:

  253      for line in zfile:
  254:         m = re.search(r"Created key with name='([^']+)' .* operation="
  255                        "'Create intermediate CA CSR", line)

  265      for line in zfile:
  266:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
  267                        "keyvault for user operation='Create intermediate CA "

  279      for line in zfile:
  280:         m = re.search(r"Create intermediate CA CSR for org=([^\s]+) CN=(.*) "
  281                        "completed by user='([^']*)' with signing key name="

  293      for line in zfile:
  294:         m = re.search("-BEGIN CERTIFICATE-", line)
  295          if m:

  308      for line in zfile:
  309:         m = re.search(r".*Retrieved public key with name='([^']+)' .* "
  310                        "operation='Delete CSR", line)

  321      for line in zfile:
  322:         m = re.search(r"Deleted key='([^']+)' from keyvault for user operation"
  323                        "='Delete CSR for org=([^\\s]+) CN=([^']+)", line)

  333      for line in zfile:
  334:         m = re.search(r"Delete CSR for org=([^\s]+) CN=(.*) completed by user="
  335                        "'([^']*)' with signing key name='([^']+)'.*", line)

  350      for line in zfile:
  351:         m = re.search(r"Retrieved public key with name='([^']+)' .* "
  352                        "operation='Delete CA", line)

  363      for line in zfile:
  364:         m = re.search(r"Deleted key='([^']+)' from keyvault for user operation"
  365                        "='Delete CA for org=([^\\s]+) CN=([^']+)", line)

  375      for line in zfile:
  376:         m = re.search(r"Delete CA for org=([^\s]+) CN=(.*) completed by user"
  377                        "='([^']+)' with signing key name '([^']+)'", line)

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\azure_helper.py:
  282          pip_id = nic_params.ip_configurations[0].public_ip_address.id
  283:         pip_name = re.search(r'[^/]*$', pip_id).group(0)
  284          public_ip_address = \

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\conftest.py:
   308          output = automodel.show_peers(online_only=True)
   309:         m = re.search("Connected appliances:\\s+(\\d+)", output.raw)
   310          no_of_peers = int(m.group(1))

   318          zak_serial_no = get_zak_serial_no(scm_actor)
   319:         if (re.search(zak_serial_no, output.raw)):
   320              return 1

   414              azure_helper = AzureHelper()
   415:             zaksh_name = re.search(r'([^\s]+)', zaksh_data).group()
   416              zaksh_nic_ids = azure_helper.get_vm_nic_ids(rg, zaksh_name)
   417:             nic_name = re.search(r'[^/]*$', zaksh_nic_ids[0]).group(0)
   418              pip = azure_helper.get_nic_public_ip(rg, nic_name)

   780          output = zaksh_shell.exec_command(cmd)
   781:         curr_log = re.search(r'(\S+) file', output).group(1)
   782          logger.info(f"Current ZAKSH log level: {curr_log}")

   883          else:
   884:             m = re.search("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*$",
   885                            output)

  1173          output = automodel.show_peers(online_only=True)
  1174:         if (re.search("No connected peer", output.raw)):
  1175              return 1
  1176:         m = re.search("Connected appliances:\\s+(\\d+)", output.raw)
  1177          no_of_peers = int(m.group(1))

  1429                                    allocation=Allocation())
  1430:         zaksh_ip = re.search('(?<=\[)[^]]+(?=\])', zak_sh_data).group()  # noqa
  1431          admin_cidr = ipaddress.ip_interface(str(zaksh_ip + "/0"))

  2013              raise ValueError("There is no application token")
  2014:         app_token = re.search("(^\\S*)", value).group(0)
  2015          return app_token

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\vanautu\test_cfe_lb_none.py:
  28      assert("GLB Secondary Ports" not in output.keys())
  29:     lb_ports = re.search("(\\d+)-(\\d+)", output['load balancer port range'])
  30      port1 = int(lb_ports.group(1))

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\misc_scripts\docker_remove_oldimage.py:
  17  for line in output.splitlines():
  18:     m = re.search("quay.*bamboo.*\\s+(\\S+)\\s+(\\d+)\\s+(hours|days) ago",
  19                    line)

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
   456              try:
   457:                 lb_ip = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',
   458                                    output).group(0)

   491          assert(vm_info is not None)
   492:         output = re.search('{.*}', vm_info)
   493          assert(output)

   642          challenge_str = actor.model.cli_challenge_generate().raw
   643:         token_obj = re.search(r'Generated challenge: (.*)', challenge_str)
   644          if token_obj:

   651          output = local_shell.exec_command(cmd, timeout=TIMEOUT)
   652:         response_obj = re.search(r'cli challenge response (.*)', output)
   653          if response_obj:

   787              app_restrict_flag = \
   788:                 re.search(r'app_restriction_enable=(\S+)', out).group(1)
   789              logger.info(f"Current app restriction: {app_restrict_flag}")

   798              out = ssh_shell.exec_command(cmd)
   799:             curr_log = re.search(r'(\S+) file', out).group(1)
   800              logger.info(f"Current log level: {curr_log}")

   816                  copy_util.copy_from_host(zaksh, "/dumps/", cert_path)
   817:                 cert_file = re.search(r'[^/]*$', cert_path).group(0)
   818                  cmd = (f"sudo cp /dumps/{cert_file} /var/opt/rbt/ssl/ca/; "

  1138              output_expected=True)
  1139:         if re.search(r'active', output):
  1140              return True

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\csh_data_disks_operations.py:
  96      output = perfHelper.execute_shell_cmds_csh(csh, [cmd])
  97:     num_disks = re.search(r"(.*)$", output.decode("utf-8")).group(0)
  98      log.info(f"Number of data disks attached to CSH: {num_disks}")

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\setup_clients_servers.py:
   88          output = shell.exec_command(cmd, output_expected=True)
   89:     version = re.search(r'(\d+.\d+)', output)
   90      if version:

  171          with open('60-static.yaml', 'w') as infile:
  172:             match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}', eth0_ip).group(0)
  173              infile.write(NETPLAN.format(eth0_ip, match))

  176                      str(actor_client.resource.interfaces[f'test{eth}'].cidr.ip)
  177:                 match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}', eth_ip).group(0)
  178                  infile.write(ETH.format(eth, eth_ip, match, eth))

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\zak_cluster.py:
   67      zaksh_ip = \
   68:         re.search(r'(?<=\[)[^]]+(?=\])', zaksh_data).group()
   69      admin_cidr = ipaddress.ip_interface(str(zaksh_ip + "/0"))

  143          zahsh_name = \
  144:             re.search(r'([^\s]+)', zaksh_data).group()
  145          zaksh_resource = create_zaksh_resource(zaksh_data,

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\zaksh_setup\azure_helper.py:
  2685          for vm_nic in vm_nics_list:
  2686:             if re.search('-ul2', vm_nic.name):
  2687                  all_vm_resources["nic_uplink2"] = vm_nic.name

  2691                      all_vm_resources["subnet_uplink2"] = subnet
  2692:             elif re.search('-ul', vm_nic.name):
  2693                  all_vm_resources["nic_uplink"] = vm_nic.name

  2697                      all_vm_resources["subnet_uplink"] = subnet
  2698:             if re.search('-dl', vm_nic.name):
  2699                  all_vm_resources["nic_downlink"] = vm_nic.name

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\shm_tests\shm_helper.py:
   75          cmd_output = self.client_shell.exec_command(cmd)
   76:         status = re.search(search_pattern, cmd_output)
   77          if status:

  155          cmd_output = self.client_shell.exec_command(cmd)
  156:         app_content = re.search(search_pattern, cmd_output, re.DOTALL)
  157          if app_content:

  170              application_map['dest_port'] = int(dest[1])
  171:             application_map['app_id'] = int(re.search(".*snoopy_app="
  172                                                        "(\\d+)", app).group(1)

dist-packages\portfolio_system_tests\legacy_zaksh_tests\tests\zak_sh_troubleshoot\test_zaksh_nic_nw_acceleration.py:
   85              output = zak_sh_shell.exec_command(cmd, output_expected=True)
   86:             ipv4_address = re.search(r'inet \d+.\d+.\d+.\d+', output)
   87              assert(ipv4_address is None)

   91              output = zak_sh_shell.exec_command(cmd, output_expected=True)
   92:             ipv4_address = re.search(r'inet \d+.\d+.\d+.\d+', output)
   93              if (ipv4_address is None):

  107              assert(output is not None)
  108:             maxconn = re.search(r'net.core.somaxconn = \d+', output)
  109              fo.write("\nsomaxconn {} ".format(maxconn.group(0)))
  110:             tcpmem = re.search(r'net.ipv4.tcp_mem = \d+\s+\d+\s+\d+', output)
  111              fo.write("\ntcp_mem {} ".format(tcpmem.group(0)))
  112:             port_range = re.search(r'net.ipv4.ip_local_port_range = \d+\s+\d+',
  113                                     output)

dist-packages\portfolio_system_tests\spoon_tests\libs\configure.py:
  1768              node_name = name.strip()
  1769:             all_match = re.search(r"value: (.*) \((.*)\)", value)
  1770              if not all_match:

dist-packages\portfolio_system_tests\spoon_tests\libs\connectivity.py:
  61                  loss_re = re.compile(r'(\d*)%(?: packet)? loss')
  62:                 tx_search = tx_re.search(line)
  63:                 rx_search = rx_re.search(line)
  64:                 loss_search = loss_re.search(line)
  65                  if tx_search is not None:

  73                      r'(\d*.\d*)/(\d*.\d*)/(\d*.\d*)(?:/\d*.\d*)? ms')
  74:                 rtt_search = rtt_re.search(line)
  75                  if rtt_search is None:

dist-packages\portfolio_system_tests\spoon_tests\libs\exchange_load.py:
  221      client_resource = allocation.resources[client]
  222:     branch_suffix = re.search(r"([-]\d+)", client).group(0)
  223      sh_name = 'steelhead' + branch_suffix

dist-packages\portfolio_system_tests\spoon_tests\libs\sharepoint_load.py:
  186      client_resource = allocation.resources[client]
  187:     branch_suffix = re.search(r"([-]\d+)", client).group(0)
  188      sh_name = 'steelhead' + branch_suffix

  192  
  193:     client_suffix = re.search(r"([-]\d+)+", client)
  194      file_prefix, file_suffix = file_name.split('.')

dist-packages\portfolio_system_tests\spoon_tests\libs\verification.py:
  110          if re.match(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line) and \
  111:            re.search(r'ERR(OR)?\]', line):
  112              # Get time stamp
  113:             split = re.search(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line).group(0)
  114              date = split[1:]

  130      for line in file_contents:
  131:         if re.search(r'ERR(OR)?\]', line):
  132              error_list.append(line)

dist-packages\portfolio_system_tests\spoon_tests\libs\wget_load.py:
  195      else:
  196:         branch_suffix = re.search(r"([-]\d+)", client).group(0)
  197          sh_name = 'steelhead' + branch_suffix

dist-packages\portfolio_system_tests\tiramisu\test_functional_sanity_win.py:
  105  
  106:     match = re.search(r'\((?P<ip>.*?)\) port \d+', output)
  107      if match:

dist-packages\portfolio_system_tests\winsec\conftest.py:
   79      # the lost percentage values.
   80:     results = re.search(r'Lost\s+=\s+(\d+)', ping_results)
   81      if results:

  902      # Matching to 'EncryptData\s+:\s+{True|False}'
  903:     enc_status = re.search(r'EncryptData\s+:\s+(\w+)',
  904                             smb_server._exec_cmd(get_cmd)).group(1)

dist-packages\pq_core\communication\channel.py:
  203          for pattern in match_res:
  204:             match = re.search(pattern, data)
  205              if match:

dist-packages\pq_core\communication\parsers.py:
   162  
   163:     lines = (x for x in input_string.splitlines() if re.search(r'\w', x))
   164  

   326      for line in lines:
   327:         match = re.search(r'^(\s+\d{1,3}\s+|def\s+)', line)
   328          if match:

  1363              for key, value in connections.items():
  1364:                 match = re.search(r'(\d+)\s+(\d+)\s+(\d+)', str(value))
  1365                  if match:

  1463      for line in lines:
  1464:         if (re.search(":", line)):
  1465              key, value = line.split(':', 1)

  1467              sub_dic1[key] = value.strip()
  1468:             if (re.search(":", line)):
  1469                  list1 = []

  1485              sub_dic1.update(sub_dic2)
  1486:         elif (re.search(r"\.", line)):
  1487              pass

  1692          for item in items:
  1693:             if (re.search(":", item)):
  1694                  key, value = item.split(':', 1)

  1849      def _extract_one_regex_parser(input_string):
  1850:         m = re.search(regex, input_string)
  1851  

dist-packages\pq_core\communication\powershell.py:
  154                  matched = pattern.search(output) if hasattr(pattern, 'match') \
  155:                     else re.search(pattern, output)
  156                  if matched:

dist-packages\pq_core\communication\wafl.py:
  157              if any(k for k, v in kwargs.items()
  158:                    if k in proc and (proc[k] == v or re.search(v, proc[k]))):
  159                  matched_procs.append(proc)

dist-packages\pq_core\communication\cli\cli_result.py:
  554  
  555:         lines = (x for x in self._raw.splitlines() if re.search(r'\w', x))
  556  

  928          for line in lines:
  929:             match = re.search(r'^(\s+\d{1,3}\s+|def\s+)', line)
  930              if match:

dist-packages\pq_core\fwk\factory.py:
  129      # number, which will be in the form of 9_2_0
  130:     version_match = re.search(r'(\d+\.\d+\.\d+).*', build_info.version_string)
  131      version = version_match.group(1).replace('.', '_')

dist-packages\pq_core\lab\query.py:
  1036          smc_uid_regex = r'smc\d+'
  1037:         return self.findall(lambda r: re.search(smc_uid_regex, r.uniqueid))
  1038  

  1044          return next(
  1045:             self.ifind(lambda r: re.search(smc_uid_regex, r.uniqueid)),
  1046              None)

dist-packages\pq_core\lab\netdevice\vyatta.py:
  1740          for line in output.splitlines():
  1741:             neighbor_here = re.search(r'BGP neighbor is ([\d\w.]+)', line)
  1742              if neighbor_here:
  1743                  neighbor = neighbor_here.group(1)
  1744:                 remote_phrase = re.search(r'remote AS ([\d\w.]+)', line)
  1745                  if remote_phrase and neighbor == my_ip:

  1764          for line in text.splitlines():
  1765:             flag_here = re.search(flag, line)
  1766              if not found_flag and flag_here:

  1771                  # if we hit a line beginning with 'Total', exit
  1772:                 starts_with_total = re.search('^Total', line)
  1773                  if starts_with_total:

  1777                  else:
  1778:                     contains_num = re.search(r'\d', line)
  1779                      if contains_num:

  1878              # is this the start of data for a new neighbor?
  1879:             start_stop_now = re.search(start_stop_pat, line)
  1880              if start_stop_now:

  1891              for key, pattern in searchpat.items():
  1892:                 found = re.search(pattern, line)
  1893                  if found:
  1894                      result[key] = found.group(1)
  1895:             if re.search('BGP neighbor is', line):
  1896                  found_neighbor = True

  1919          for line in output.splitlines():
  1920:             if re.search('^BGP', line):
  1921:                 fields = re.search(r'([\d+]) entries', line)
  1922                  if fields.group(1):

dist-packages\pq_core\lab\netdevice\ios\router.py:
  1206              # is this the start of data for a new neighbor?
  1207:             start_stop_now = re.search(start_stop_pat, line)
  1208              if start_stop_now:

  1219              for key, pattern in searchpat.items():
  1220:                 found = re.search(pattern, line)
  1221                  if found:
  1222                      result[key] = found.group(1)
  1223:             if re.search('BGP neighbor is', line):
  1224                  found_neighbor = True

  1239          for line in text.splitlines():
  1240:             flag_here = re.search(flag, line)
  1241              if not found_flag and flag_here:

  1246                  # is this line actually a neighbor?
  1247:                 starts_with_num = re.search(r'^\d', line)
  1248                  if starts_with_num:

dist-packages\pq_core\lab\os\networking\__init__.py:
   72          # Check for vyatta jail and break out of it.
   73:         if re.search(r'Invalid command', output):
   74              cmd = '/sbin/ifconfig %s' % name

   91                  continue
   92:             ipmatch = re.search(r'inet\s(?:addr:)*(\S+)', line)
   93              # NOTE: the 'group()' calls used to call .decode('utf8', 'ignore')

  100  
  101:             maskmatch = re.search(r'Mask:*\s*(\S+)', line, re.IGNORECASE)
  102              if maskmatch:

  111  
  112:             ipv6match = re.search(
  113                  r'inet6\saddr:\s([a-fA-F0-9:]+)/*(\S+)', line)

  117  
  118:             ethmatch = re.search(r'(?:(?:ether)|(?:HWaddr))\s(?:addr:)*(\S+)',
  119                                   line)

dist-packages\pq_core\lab\os\networking\tc.py:
   93              for prop in props:
   94:                 matchobj = re.search(prop.regex, lines[prop.line])
   95                  if matchobj is None:

  104              rate_re = r'rate (\S+)'
  105:             matchobj = re.search(rate_re, lines[2])
  106              if matchobj is None:

dist-packages\pq_core\lab\os\posix\__init__.py:
  645  
  646:             if re.search(r'No such file or directory', ls_info, re.IGNORECASE):
  647                  raise os_error(errno.ENOENT, ls_info)
  648:             if re.search(r'Permission denied', ls_info, re.IGNORECASE):
  649                  raise os_error(errno.EACCES, ls_info)

  748          for line in output.splitlines():
  749:             result = re.search(regex, line)
  750              if result:

dist-packages\pq_lib\tools\curl_loader.py:
  209              for line in reversed(out):  # Reversed: new processes at the bottom
  210:                 command_search = command_re.search(line)
  211                  if command_search is None:

  658              key, value = stat.split(':')
  659:             match = re.search(value_rgx, value)
  660              if match:

  732              for line in text_to_parse.splitlines():
  733:                 match = total_re.search(line)
  734                  if match:

  742  
  743:                 match = stats_re.search(line)
  744                  if match:

dist-packages\pq_lib\tools\curl.py:
  187          for line in array:
  188:             if re.search(cmd, line):
  189:                 mymatch = re.search(r'^\w+\s+(\d+)', line)
  190                  if mymatch:

  292              except ShellError as err:
  293:                 if re.search('No such process', str(err)):
  294                      pass

dist-packages\pq_lib\tools\dnsname.py:
   72              #
   73:             match = re.search(
   74                  r'Address:\s+({})\s*$'.format(IPV4_REGEX), lookup_output,

  135          for line in lines:
  136:             match = re.search(regex, line, *args, **kwargs)
  137              if match:

dist-packages\pq_lib\tools\docker.py:
  313  
  314:         join_command = re.search(r'docker swarm .*', output)
  315          if not join_command:

dist-packages\pq_lib\tools\interface_tools.py:
  297          # Check for vyatta jail and break out of it.
  298:         if re.search(r'Invalid command', output):
  299              cmd = '/sbin/ifconfig %s' % name

  317                  continue
  318:             ipmatch = re.search(r'inet\s(?:addr:)*(\S+)', line)
  319              # NOTE: the 'group()' calls used to call .decode('utf8', 'ignore')

  326  
  327:             maskmatch = re.search(r'Mask:*\s*(\S+)', line, re.IGNORECASE)
  328              if maskmatch:

  337  
  338:             ipv6match = re.search(
  339                  r'inet6\saddr:\s([a-fA-F0-9:]+)/*(\S+)', line)

  343  
  344:             ethmatch = re.search(r'(?:(?:ether)|(?:HWaddr))\s(?:addr:)*(\S+)',
  345                                   line)

dist-packages\pq_lib\tools\ipmitool.py:
  169          for line in result_list:
  170:             if re.search("IP Address Source", line):
  171                  ip_addr_dict['ip_source'] = 'static' if \

  173                      else 'dhcp'
  174:             if re.search(r'^IP Address\s+:', line):
  175                  ip_addr_dict['ip_addr'] = line.split(":")[1].strip()
  176:             if re.search("Subnet Mask", line):
  177                  ip_addr_dict['subnet_mask'] = line.split(":")[1].strip()
  178:             if re.search("Default Gateway IP", line):
  179                  ip_addr_dict['gateway'] = line.split(":")[1].strip()

  390              for field in fru_details:
  391:                 if re.search(":", field):
  392                      key, value = field.split(":", 1)

  460  
  461:         elif re.search("^looptest", option):
  462              sol_looptest_dict = {}

  464              for line in op_list:
  465:                 reobj = re.search(r'(\d+).*\n.*\[(.*)\.', line)
  466                  if reobj:

dist-packages\pq_lib\tools\nfs_standalone.py:
  107              result = shell.exec_command('yum --version nfs')
  108:             searchobj = re.search(r'Installed:\s+rpm.*$', result, re.M)
  109              return (searchobj is not None)

  128          if result:
  129:             searchobj1 = re.search(r'rpc\.mountd.*is (.*)\n', result, re.M)
  130:             searchobj2 = re.search(r'nfsd.*is (.*)\n', result, re.M)
  131              if not (searchobj1 and searchobj2):

  314              except ShellError as e:
  315:                 searchobj1 = re.search(r'umount: .*?: not mounted', str(e), re.M) # noqa
  316:                 searchobj2 = re.search(r'umount: .*?: not found', str(e), re.M)
  317                  if not (searchobj1 or searchobj2):

dist-packages\pq_lib\tools\openssl_traffic.py:
  281          """
  282:         match = re.search(re_string, in_data, re_flags)
  283          if match:

  709          else:
  710:             session_id = re.search(r"Session-ID:\s([0-9A-F]*)",
  711                                     str(client_output))

  735          else:
  736:             cipher = re.search(r"CIPHER\s+is\s+([0-9A-Z-]*)",
  737                                 str(in_data), re.IGNORECASE)

dist-packages\pq_lib\tools\openssl.py:
  65          """
  66:         match = re.search(re_string, in_data, re_flags)
  67          if match:

dist-packages\pq_lib\tools\pload.py:
  766              line = outputlines.pop(0)
  767:             match = re.search(interval_rgx, line)
  768              if match:

  786          for line in outputlines:
  787:             match = re.search(tstamp_rgx, line)
  788              if match:

  794                      # extract time from timestamp
  795:                     sub_match = re.search(time_rgx, timestamp)
  796                      starttime = self._time_to_seconds(sub_match.group('time'))
  797                      starttime = starttime - runtime
  798:             match = re.search(data_rgx, line)
  799              if match:

  822          sec_rgx = r'\s*(?P<seconds>\d+)\s+sec'
  823:         match = re.search(sec_rgx, runtime_str)
  824          if match:

  830                      r'(?P<hour>\d\d):(?P<min>\d\d):(?P<sec>\d\d)')
  831:         match = re.search(dhms_rgx, runtime_str)
  832          if match:

  839          hms_rgx = r'\s*(?P<hour>\d\d):(?P<min>\d\d):(?P<sec>\d\d)'
  840:         match = re.search(hms_rgx, runtime_str)
  841          if match:

  847          ms_rgx = r'\s*(?P<min>\d\d):(?P<sec>\d\d)'
  848:         match = re.search(ms_rgx, runtime_str)
  849          if match:

dist-packages\pq_lib\tools\posix_tools.py:
  482              logger.debug('searching for "%s" in %s', regex, line)
  483:             result = re.search(regex, line)
  484              if result:

  673  
  674:             if re.search(r'No such file or directory', ls_info, re.IGNORECASE):
  675                  raise os_error(errno.ENOENT, ls_info)
  676:             if re.search(r'Permission denied', ls_info, re.IGNORECASE):
  677                  raise os_error(errno.EACCES, ls_info)

dist-packages\pq_lib\tools\psql.py:
  57              if '-[ RECORD' in line:
  58:                 my_match = re.search(r'\[ RECORD \d+ \]', line)
  59                  if my_match:

dist-packages\pq_lib\tools\rrdtool.py:
  415                 r'(?P<title3>\w+)\s+(?P<title4>\w+)\s*$')
  416:         match = re.search(reg, lines[0])
  417          assert match

  432          for line in lines:
  433:             match = re.search(reg, line)
  434              if not match:

dist-packages\pq_lib\tools\s_server.py:
  251              except ShellError as err:
  252:                 if re.search('No such process', str(err)):
  253                      pass

  290          except ShellError as err:
  291:             if re.search('No such file', str(err)):
  292                  output = ""

  313          except ShellError as err:
  314:             if re.search('No such file', str(err)):
  315                  pass

  389          for line in array:
  390:             if re.search(cmd, line):
  391:                 mymatch = re.search(r'^\w+\s+(\d+)', line)
  392                  if mymatch:

dist-packages\pq_lib\tools\stt.py:
  478                               line)
  479:                 my_match = match_re.search(line)
  480                  if my_match is not None:

dist-packages\pq_lib\tools\tc.py:
  606              for prop in props:
  607:                 matchobj = re.search(prop.regex, lines[prop.line])
  608                  if matchobj is None:

  618              rate_re = r'rate (\S+)'
  619:             matchobj = re.search(rate_re, lines[2])
  620              if matchobj is None:

dist-packages\pq_lib\tools\top.py:
  148                  # Ex: u'682044k used' will be splitted as u'used' and 682044
  149:                 value = re.search(r'(\d+)k*\s+(\w+)', i)
  150                  top_dict[key][value.group(2)] = int(value.group(1))

  155                  for line in output[0].split('\n'):
  156:                     if re.search('top - ', line):
  157                          top_dict[keyname]['time'] = time.strftime(
  158:                             re.search(r'\d+:\d+:\d+', line).group())
  159:                         users = re.search(r'\d+ user', line).group()
  160                          top_dict[keyname]['users'] = int(re.match(r'\d+',
  161                                                           users).group())
  162:                         up_time = re.search(r'\d+ days', line).group()
  163                          top_dict[keyname]['up_time'] = int(re.match(r'\d+',

  167          top_output.append(top_dict)
  168:         columns = re.search('.*PID.*', output[1]) if len(output) > 1 else None
  169          if not columns:

  184                  processes[proc_details['pid']] = proc_details
  185:             elif re.search('.*PID.*', line):
  186                  proc_parse_start = True

dist-packages\pq_lib\tools\valgrind.py:
  145          result = self._os.shell.exec_command(command=cmd, output_expected=True)
  146:         res = re.search('a memory error', result)
  147          assert res

  317              for line in result.splitlines():
  318:                 if re.search(r' 0 bytes', line):
  319                      continue

dist-packages\pq_lib\tools\vsftp.py:
   48                                                    output_expected=True)
   49:         if re.search("Ubuntu", output):
   50              self._set_annonymous_user_permission(device='Ubuntu')

   59                  cmd, output_expected=True)
   60:             version = re.search(r"(\d+.\d+)", version_output)
   61              version = float(version.group(1))

   84                     r'Starting vsftpd for vsftpd:.*OK.*')
   85:             if not re.search("Starting FTP server.*done", output, re.DOTALL)\
   86:                     and not re.search("^vsftpd start/running*",
   87                                        output, re.MULTILINE)\
   88:                     and not re.search(reg, str(output)):
   89                  raise UnexpectedOutput(

  154      # Parse output
  155:     if not re.search("^Starting vsftpd.* OK ", output, re.MULTILINE):
  156          raise UnexpectedOutput(cmd, output,

dist-packages\pq_lib\tools\wget.py:
  133          for line in array:
  134:             if re.search(cmd, line):
  135:                 mymatch = re.search(r'^\w+\s+(\d+)', line)
  136                  if mymatch:

  176              except ShellError as err:
  177:                 if re.search('No such process', str(err)):
  178                      pass

dist-packages\pq_lib\traffic\pload.py:
  503              line = outputlines.pop(0)
  504:             match = re.search(interval_rgx, line)
  505              if match:

  522          for line in outputlines:
  523:             match = re.search(tstamp_rgx, line)
  524              if match:

  532                      starttime = starttime - runtime
  533:             match = re.search(data_rgx, line)
  534              if match:

  556          sec_rgx = r'\s*(?P<seconds>\d+)\s+sec'
  557:         match = re.search(sec_rgx, runtime_str)
  558          if match:

  564                      r'(?P<hour>\d\d):(?P<min>\d\d):(?P<sec>\d\d)')
  565:         match = re.search(dhms_rgx, runtime_str)
  566          if match:

  573          hms_rgx = r'\s*(?P<hour>\d\d):(?P<min>\d\d):(?P<sec>\d\d)'
  574:         match = re.search(hms_rgx, runtime_str)
  575          if match:

  581          ms_rgx = r'\s*(?P<min>\d\d):(?P<sec>\d\d)'
  582:         match = re.search(ms_rgx, runtime_str)
  583          if match:

dist-packages\pq_lib\traffic\test\regexp-1:
  5  
  6: x = re.search("Location: * ", txt)

dist-packages\pq_orclib\access_token_utilities\__init__.py:
  64      output = cli.exec_cmd("show papi rest access_codes")
  65:     match = re.search("No access codes", output)
  66      if match:

  72          output = cli.exec_cmd("show papi rest access_codes")
  73:     match = re.search('Code: (.*)\n?', output)
  74      if match:

dist-packages\pq_orclib\general_cmc_operations\__init__.py:
  45      output = sh_model.show_info().raw
  46:     serial = re.search(
  47          r'Serial:.*', output).group(0).replace('Serial:', '').strip(' \n\t\r')

  80      output = sh_model.show_cmc().raw
  81:     managed = re.search(r'Managed by CMC:.*', output).group(0).\
  82          replace('Managed by CMC:', '').strip(' \n\t\r')
  83:     next_msg = re.search(r'Seconds until next message is sent:.*', output)
  84:     line = re.search(r'CMC hostname:.*', output).group(0)
  85      current_cmc = re.sub(

dist-packages\pq_orclib\o365d\__init__.py:
   64                  # Extract class b address from resolved ips
   65:                 subnet_extract = re.search(r"(^\d{1,3}\.\d{1,3})*",
   66                                             ip_address)

  557                  # Look for line starting with domain-label
  558:                 if re.search(r'\s+domain-label "%s"'
  559                               % dl['domain_label'], line):

  564                          # if not found raise exception
  565:                         if not re.search(r'\%s' % dn, line):
  566                              raise Exception('Failed to find %s in '

  571                      # Look for string starting with in-path rule...dst-domain.'
  572:                     if re.search(r'\s+in-path rule %s(.*) dst-domain "%s"' %
  573                                   (rule_type, dl['domain_label']), line):

  604                  # Search for pattern SAAS_RU_PASSTHRU 1
  605:                 if re.search(r'(.*)SAAS_RU_PASSTHRU NONE 1(.*)', line):
  606                      dl['found'] = True

  634                  # Look for line starting with domain-label
  635:                 if re.search(r'\s+host-label "%s" hostname'
  636                               % hl['host_label'], line):

  641                      # if not found raise exception
  642:                     if not re.search(r'\"%s"' % hn, line):
  643                          raise Exception('Failed to find hostname %s in '

  645                                          ' %s' % (hn, line))
  646:                 if re.search(r'\s+host-label "%s" subnet'
  647                               % hl['host_label'], line):
  648:                     if not re.search(r'\"%s"' % str(hl['subnet']), line):
  649                          raise Exception('Failed to find %s in '

  654                      # Look for string starting with in-path rule...dst-domain.'
  655:                     if re.search(r'\s+in-path rule %s(.*) dst-host "%s"' %
  656                                   (rule_type, hl['host_label']), line):

dist-packages\pq_orclib\ocs\__init__.py:
  321      for line in file_contents:
  322:         matching_string = re.search(r'%s'
  323                                      % (pattern), line)

dist-packages\pq_orclib\panther\__init__.py:
  196          for zone in zones:
  197:             if not re.search(r'(HQ|Branch1)', zone.site, flags=re.IGNORECASE):
  198                  zone_site = zone.site

  249          for item in org_network_list:
  250:             if re.search(subnet_name, item.id, flags=re.IGNORECASE):
  251                  logger.debug("Removing Network \'%s\' from %s", item.id,

dist-packages\pq_orclib\panther\cluster.py:
  379              for org_dc_uplink in org_dc_uplinks:
  380:                 if re.search(
  381                          wan_type,

dist-packages\pq_orclib\query_api\jira_query.py:
  219                  # Format: 2021-02-08T15:25:02.656Z
  220:                 match = re.search(r"startDate=\d+-(\d+-\d+)T", raw_info)
  221                  result_info['begin'] = match.group(1)
  222              if raw_info.startswith('endDate='):
  223:                 match = re.search(r"endDate=\d+-(\d+-\d+)T", raw_info)
  224                  result_info['end'] = match.group(1)

  227                  # EHB sprints look like Sprint 123: 12/1 - 12/8
  228:                 match_ehb = re.search(r"Sprint (\d+): \d+/\d+ - \d+/\d+",
  229                                        sprint_info)

dist-packages\pq_orclib\sc_configurator\appliance_setup.py:
  53          'print \'Firmware version: \' + getFirmwareVersion()"')
  54:     return re.search(r'Firmware version: ((\d*\.)+\d*-.+)', f_version).group(1)
  55  

dist-packages\pq_orclib\sc_configurator\management_configurator.py:
  514              re.compile(r'CN={0}, OU=(?P<realm_id>\S+)'.format(certlink_id))
  515:         match = realm_pat_re.search(cert_contents)
  516          if not match:

dist-packages\pq_orclib\static_routing\__init__.py:
  23      result = actor.model.show_interfaces(interface_name=interface).raw
  24:     searchobj = re.search(r'IP address:\s+(\S+)$', result, re.M)
  25      if not searchobj:

dist-packages\pq_orclib\vm_deploy\__init__.py:
  122      """Search for a particular regex and return the first group."""
  123:     m = re.search(regex, string, re.M | re.S)
  124      if m:

  213          # Get the section where the networks are listed
  214:         res = re.search(r'Networks:\n(.*)\nVirtual Machines', out, re.M | re.S)
  215          if not res:

dist-packages\venv\Lib\site-packages\hpilo.py:
  332              # Seen on ilo3 with corrupt filesystem
  333:             body = re.search('<body>(.*)</body>', data, flags=re.DOTALL).group(1)
  334              body = re.sub('<[^>]*>', '', body).strip()

  337              raise IloError(body)
  338:         self.cookie = re.search('Set-Cookie: *(.*)', data).group(1)
  339          self._debug(2, "Cookie: %s" % self.cookie)

dist-packages\venv\Lib\site-packages\virtualenv.py:
  1295              del os.environ["__PYVENV_LAUNCHER__"]
  1296:         if re.search(r"/Python(?:-32|-64)*$", py_executable):
  1297              # The name of the python executable is not quite what

dist-packages\venv\Lib\site-packages\_pytest\pastebin.py:
  86          return "bad response: %s" % exc_info
  87:     m = re.search(r'href="/raw/(\w+)"', response)
  88      if m:

dist-packages\venv\Lib\site-packages\_pytest\_code\code.py:
  659              msg += " Did you mean to `re.escape()` the regex?"
  660:         assert re.search(regexp, str(self.value)), msg.format(regexp, str(self.value))
  661          # Return True to allow for "assert excinfo.match()".

dist-packages\venv\Lib\site-packages\click\shell_completion.py:
  307          )
  308:         match = re.search(r"^(\d+)\.(\d+)\.\d+", output.stdout.decode())
  309  

dist-packages\venv\Lib\site-packages\docker\models\images.py:
  288              if 'stream' in chunk:
  289:                 match = re.search(
  290                      r'(^Successfully built |sha256:)([0-9a-f]+)$',

  385              if 'stream' in chunk:
  386:                 match = re.search(
  387                      r'(^Loaded image ID: |^Loaded image: )(.+)$',

dist-packages\venv\Lib\site-packages\docutils\statemachine.py:
    12  - `StateWS`, a state superclass for use with `StateMachineWS`
    13: - `SearchStateMachine`, uses `re.search()` instead of `re.match()`
    14: - `SearchStateMachineWS`, uses `re.search()` instead of `re.match()`
    15  - `ViewList`, extends standard Python lists.

  1043      (succeeds only if the pattern matches at the start of `self.line`) to
  1044:     `re.search()` (succeeds if the pattern matches anywhere in `self.line`).
  1045      When subclassing a `StateMachine`, list this class **first** in the

  1060  class SearchStateMachine(_SearchOverride, StateMachine):
  1061:     """`StateMachine` which uses `re.search()` instead of `re.match()`."""
  1062      pass

  1065  class SearchStateMachineWS(_SearchOverride, StateMachineWS):
  1066:     """`StateMachineWS` which uses `re.search()` instead of `re.match()`."""
  1067      pass

dist-packages\venv\Lib\site-packages\docutils\parsers\rst\states.py:
  406          data = '\n'.join(lines).rstrip()
  407:         if re.search(r'(?<!\\)(\\\\)*::$', data):
  408              if len(data) == 2:

dist-packages\venv\Lib\site-packages\eventlet\green\http\cookiejar.py:
   189      else:
   190:         m = TIMEZONE_RE.search(tz)
   191          if m:

   306      # fast exit for strictly conforming string
   307:     m = STRICT_DATE_RE.search(text)
   308      if m:

   324      # loose regexp parse
   325:     m = LOOSE_HTTP_DATE_RE.search(text)
   326      if m is not None:

   367      # loose regexp parse
   368:     m = ISO_DATE_RE.search(text)
   369      if m is not None:

   441          while text:
   442:             m = HEADER_TOKEN_RE.search(text)
   443              if m:

   445                  name = m.group(1)
   446:                 m = HEADER_QUOTED_VALUE_RE.search(text)
   447                  if m:  # quoted value

   451                  else:
   452:                     m = HEADER_VALUE_RE.search(text)
   453                      if m:  # unquoted value

   493              if v is not None:
   494:                 if not re.search(r"^\w+$", v):
   495                      v = HEADER_JOIN_ESCAPE_RE.sub(r"\\\1", v)  # escape " and \

   584      #  at other uses of IPV4_RE also, if change this.
   585:     if IPV4_RE.search(text):
   586          return False

   637      """
   638:     if IPV4_RE.search(text):
   639          return False

   685      erhn = req_host = request_host(request)
   686:     if req_host.find(".") == -1 and not IPV4_RE.search(req_host):
   687          erhn = req_host + ".local"

  1108                  if (host_prefix.find(".") >= 0 and
  1109:                     not IPV4_RE.search(req_host)):
  1110                      _debug("   host prefix %s for domain %s contains a dot",

  1360              if ((cookie.value is not None) and
  1361:                 self.non_word_re.search(cookie.value) and version > 0):
  1362                  value = self.quote_re.sub(r"\\\1", cookie.value)

  1937          magic = f.readline()
  1938:         if not self.magic_re.search(magic):
  1939              msg = ("%r does not look like a Set-Cookie3 (LWP) format "

  2057          magic = f.readline()
  2058:         if not self.magic_re.search(magic):
  2059              raise LoadError(

dist-packages\venv\Lib\site-packages\fabric\io.py:
  116                          # at most 1 split !
  117:                         cr = re.search("(\r\n|\r|\n)", printable_bytes)
  118                          if cr is None:

dist-packages\venv\Lib\site-packages\git\test\test_commit.py:
  351          cmt._serialize(cstream)
  352:         assert re.search(r"^gpgsig <test\n dummy\n sig>$", cstream.getvalue().decode('ascii'), re.MULTILINE)
  353  

  363          cmt._serialize(cstream)
  364:         assert not re.search(r"^gpgsig ", cstream.getvalue().decode('ascii'), re.MULTILINE)
  365  

dist-packages\venv\Lib\site-packages\git\test\lib\asserts.py:
  53      """verify that the pattern matches the string"""
  54:     assert_not_none(re.search(pattern, string), msg)
  55  

  58      """verify that the pattern does not match the string"""
  59:     assert_none(re.search(pattern, string), msg)
  60  

dist-packages\venv\Lib\site-packages\hpe3parclient\client.py:
  4065          """
  4066:         word = re.search(search_string.strip(' ') + ' ([^ ]*)', s)
  4067          return word.groups()[0].strip(' ')

dist-packages\venv\Lib\site-packages\hpe3parclient\ssh.py:
  367                      if (re.match('[\'"]', quoted) or
  368:                             re.search('[^\\\\][\'"]', quoted)):
  369                          raise exceptions.SSHInjectionThreat(

dist-packages\venv\Lib\site-packages\jinja2\utils.py:
  287          if middle.endswith((")", ">", ".", ",", "\n", "&gt;")):
  288:             match = re.search(r"([)>.,\n]|&gt;)+$", middle)
  289  

dist-packages\venv\Lib\site-packages\jsonschema\_utils.py:
  103          if property not in properties:
  104:             if patterns and re.search(patterns, property):
  105                  continue

dist-packages\venv\Lib\site-packages\jsonschema\_validators.py:
   13          for k, v in iteritems(instance):
   14:             if re.search(pattern, k):
   15                  for error in validator.descend(

  154          validator.is_type(instance, "string") and
  155:         not re.search(patrn, instance)
  156      ):

dist-packages\venv\Lib\site-packages\openpyxl\styles\numbers.py:
  107      fmt = STRIP_RE.sub("", fmt)
  108:     return re.search("[dmhysDMHYS]", fmt) is not None
  109  

dist-packages\venv\Lib\site-packages\pabot\result_merger.py:
  94      def visit_message(self, msg):
  95:         if msg.html and re.search(r'src="([^"]+\.png)"', msg.message):
  96              parent = msg.parent

dist-packages\venv\Lib\site-packages\pbr\git.py:
  311          authors += _run_git_command(git_log_cmd, git_dir).split('\n')
  312:         authors = [a for a in authors if not re.search(ignore_emails, a)]
  313  

dist-packages\venv\Lib\site-packages\pbr\tests\test_wsgi.py:
  100          print(stdoutdata)
  101:         m = re.search(b'(http://[^:]+:\d+)/', stdoutdata)
  102          self.assertIsNotNone(m, "Regex failed to match on %s" % stdoutdata)

dist-packages\venv\Lib\site-packages\pip\_internal\wheel_builder.py:
  42      """
  43:     return bool(_egg_info_re.search(s))
  44  

dist-packages\venv\Lib\site-packages\pip\_internal\index\package_finder.py:
  212  
  213:         match = self._py_version_re.search(version)
  214          if match:

dist-packages\venv\Lib\site-packages\pip\_internal\models\link.py:
  159          # type: () -> Optional[str]
  160:         match = self._egg_fragment_re.search(self._url)
  161          if not match:

  169          # type: () -> Optional[str]
  170:         match = self._subdirectory_fragment_re.search(self._url)
  171          if not match:

  181          # type: () -> Optional[str]
  182:         match = self._hash_re.search(self._url)
  183          if match:

  189          # type: () -> Optional[str]
  190:         match = self._hash_re.search(self._url)
  191          if match:

dist-packages\venv\Lib\site-packages\pip\_internal\req\constructors.py:
  313          # Handle relative file URLs
  314:         if link.scheme == 'file' and re.search(r'\.\./', link.url):
  315              link = Link(

dist-packages\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  345                  # original file is over http
  346:                 if SCHEME_RE.search(filename):
  347                      # do a url join so relative paths work

  349                  # original file and nested file are paths
  350:                 elif not SCHEME_RE.search(req_path):
  351                      # do a join so relative paths work

dist-packages\venv\Lib\site-packages\pip\_internal\utils\encoding.py:
  29      for line in data.split(b"\n")[:2]:
  30:         if line[0:1] == b"#" and ENCODING_RE.search(line):
  31:             result = ENCODING_RE.search(line)
  32              assert result is not None

dist-packages\venv\Lib\site-packages\pip\_internal\vcs\subversion.py:
  157          elif data.startswith('<?xml'):
  158:             match = _svn_xml_url_re.search(data)
  159              if not match:

  175                  )
  176:                 match = _svn_info_xml_url_re.search(xml)
  177                  assert match is not None

dist-packages\venv\Lib\site-packages\pip\_vendor\distro.py:
   989              # If there is no version_codename, parse it from the version
   990:             codename = re.search(r'(\(\D+\))|,(\s+)?\D+', props['version'])
   991              if codename:

  1057          props = {}
  1058:         match = re.search(r'^([^\s]+)\s+([\d\.]+)', lines[0].strip())
  1059          if match:

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\manifest.py:
  291          for name in self.allfiles:
  292:             if pattern_re.search(name):
  293                  self.files.add(name)

  311          for f in list(self.files):
  312:             if pattern_re.search(f):
  313                  self.files.remove(f)

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\util.py:
  709  def get_export_entry(specification):
  710:     m = ENTRY_RE.search(specification)
  711      if not m:

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  569                  CFLAGS = _CONFIG_VARS.get('CFLAGS', '')
  570:                 m = re.search(r'-isysroot\s+(\S+)', CFLAGS)
  571                  if m is not None:

  699                  try:
  700:                     m = re.search(r'<key>ProductUserVisibleVersion</key>\s*'
  701                                    r'<string>(.*?)</string>', f.read())

dist-packages\venv\Lib\site-packages\pip\_vendor\distlib\_backport\tarfile.py:
  1402          # the translation to UTF-8 fails.
  1403:         match = re.search(br"\d+ hdrcharset=([^\n]+)\n", buf)
  1404          if match is not None:

dist-packages\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  860              if (token["name"] in self.svg_allow_local_href and
  861:                 (namespaces['xlink'], 'href') in attrs and re.search(r'^\s*[^#\s].*',
  862                                                                       attrs[(namespaces['xlink'], 'href')])):

dist-packages\venv\Lib\site-packages\pip\_vendor\urllib3\connection.py:
  206          # is broken but we don't want this method in our documentation.
  207:         match = _CONTAINS_CONTROL_CHAR_RE.search(method)
  208          if match:

dist-packages\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:
  281              if is_ipv6:
  282:                 match = ZONE_ID_RE.search(host)
  283                  if match:

  356      source_url = url
  357:     if not SCHEME_RE.search(url):
  358          url = "//" + url

dist-packages\venv\Lib\site-packages\pyeapi\client.py:
  525          # Parse out model number
  526:         match = re.search('\d\d\d\d', output[0]['result']['modelName'])
  527          if match:

  597              config = getattr(self, config)
  598:         match = re.search(regex, config, re.M)
  599          if not match:

  602  
  603:         match = re.search(r'^[^\s]', config[line_end:], re.M)
  604          if not match:

dist-packages\venv\Lib\site-packages\pyeapi\eapilib.py:
  411                  pattern = "unexpected keyword argument '(.*)'"
  412:                 match = re.search(pattern, msg)
  413                  if match:

dist-packages\venv\Lib\site-packages\pyeapi\api\acl.py:
  130                              re.M)
  131:         match = acl_re.search(self.config)
  132          if match:

dist-packages\venv\Lib\site-packages\pyeapi\api\bgp.py:
   80      def _parse_bgp_as(self, config):
   81:         match = re.search(r'^router bgp (\d+)', config)
   82          return dict(bgp_as=int(match.group(1)))

   84      def _parse_router_id(self, config):
   85:         match = re.search(r'router-id ([^\s]+)', config)
   86          value = match.group(1) if match else None

   89      def _parse_max_paths(self, config):
   90:         match = re.search(r'maximum-paths\s+(\d+)\s+ecmp\s+(\d+)', config)
   91          paths = int(match.group(1)) if match else None

  208          regexp = r'neighbor {} peer-group ([^\s]+)'.format(name)
  209:         match = re.search(regexp, config)
  210          value = match.group(1) if match else None

  214          regexp = r'neighbor {} remote-as (\d+)'.format(name)
  215:         match = re.search(regexp, config)
  216          value = match.group(1) if match else None

  225          regexp = r'(?<!no )neighbor {} shutdown'.format(name)
  226:         match = re.search(regexp, config, re.M)
  227          value = True if match else False

  231          regexp = r'neighbor {} description (.*)$'.format(name)
  232:         match = re.search(regexp, config, re.M)
  233          value = match.group(1) if match else None

  242          regexp = r'neighbor {} route-map ([^\s]+) in'.format(name)
  243:         match = re.search(regexp, config, re.M)
  244          value = match.group(1) if match else None

  248          regexp = r'neighbor {} route-map ([^\s]+) out'.format(name)
  249:         match = re.search(regexp, config, re.M)
  250          value = match.group(1) if match else None

  269      def configure(self, cmd):
  270:         match = re.search(r'router bgp (\d+)', self.config)
  271          if not match:

dist-packages\venv\Lib\site-packages\pyeapi\api\interfaces.py:
  205          value = None
  206:         match = re.search(r'description (.+)$', config, re.M)
  207          if match:

  392          value = 'off'
  393:         match = re.search(r'flowcontrol send (\w+)$', config, re.M)
  394          if match:

  409          value = 'off'
  410:         match = re.search(r'flowcontrol receive (\w+)$', config, re.M)
  411          if match:

  614          value = 0
  615:         match = re.search(r'port-channel min-links (\d+)', config)
  616          if match:

  621          value = DEFAULT_LACP_FALLBACK
  622:         match = re.search(r'lacp fallback (static|individual)', config)
  623          if match:

  628          value = DEFAULT_LACP_FALLBACK_TIMEOUT
  629:         match = re.search(r'lacp fallback timeout (\d+)', config)
  630          if match:

  650          for member in self.get_members(name):
  651:             match = re.search(r'channel-group\s\d+\smode\s(?P<value>.+)',
  652                                self.get_block('^interface %s' % member))

  665          """
  666:         grpid = re.search(r'(\d+)', name).group()
  667          command = 'show port-channel %s all-ports' % grpid

  693          commands = list()
  694:         grpid = re.search(r'(\d+)', name).group()
  695          current_members = self.get_members(name)

  728  
  729:         grpid = re.search(r'(\d+)', name).group()
  730  

  869          """
  870:         match = re.search(r'vxlan source-interface ([^\s]+)', config)
  871          value = match.group(1) if match else self.DEFAULT_SRC_INTF

  874      def _parse_multicast_group(self, config):
  875:         match = re.search(r'vxlan multicast-group '
  876                            r'([\d]{3}\.[\d]+\.[\d]+\.[\d]+)',

  885      def _parse_udp_port(self, config):
  886:         match = re.search(r'vxlan udp-port (\d+)', config)
  887          value = int(match.group(1))

  897              regexp = r'vxlan vlan {} vni (\d+)'.format(vid)
  898:             match = re.search(regexp, config)
  899              values[vid]['vni'] = match.group(1) if match else None

  901              regexp = r'vxlan vlan {} flood vtep (.*)$'.format(vid)
  902:             matches = re.search(regexp, config, re.M)
  903              flood_list = matches.group(1).split(' ') if matches else []

  908      def _parse_flood_list(self, config):
  909:         match = re.search(r'vxlan flood vtep (.+)$', config, re.M)
  910          values = list()

dist-packages\venv\Lib\site-packages\pyeapi\api\ipinterfaces.py:
   79  
   80:         if name[0:2] in ['Et', 'Po'] and not SWITCHPORT_RE.search(config,
   81                                                                    re.M):

  101          """
  102:         match = re.search(r'ip address ([^\s]+)', config)
  103          value = match.group(1) if match else None

  118          """
  119:         match = re.search(r'mtu (\d+)', config)
  120          return dict(mtu=int(match.group(1)))

dist-packages\venv\Lib\site-packages\pyeapi\api\mlag.py:
  118          """
  119:         match = re.search(r'domain-id (.+)$', config)
  120          value = match.group(1) if match else None

  132          """
  133:         match = re.search(r'local-interface (\w+)', config)
  134          value = match.group(1) if match else None

  146          """
  147:         match = re.search(r'peer-address ([^\s]+)', config)
  148          value = match.group(1) if match else None

  160          """
  161:         match = re.search(r'peer-link (\S+)', config)
  162          value = match.group(1) if match else None

  188              config = self.get_block('interface %s' % name)
  189:             match = re.search(r'mlag (\d+)', config)
  190              if match:

dist-packages\venv\Lib\site-packages\pyeapi\api\ntp.py:
  90      def _parse_source_interface(self, config):
  91:         match = re.search(r'^ntp source ([^\s]+)', config, re.M)
  92          value = match.group(1) if match else None

dist-packages\venv\Lib\site-packages\pyeapi\api\ospf.py:
   93          """
   94:         match = re.search(r'^router ospf (\d+)', config)
   95          return dict(ospf_process_id=int(match.group(1)))

  104          """
  105:         match = re.search(r'^router ospf \d+ vrf (\w+)', config)
  106          if match:

  117          """
  118:         match = re.search(r'router-id ([^\s]+)', config)
  119          value = match.group(1) if match else None

dist-packages\venv\Lib\site-packages\pyeapi\api\routemaps.py:
  150          continue_re = re.compile(r'^\s+continue\s(\d+)$', re.M)
  151:         match = continue_re.search(config)
  152          value = int(match.group(1)) if match else None

  156          desc_re = re.compile(r'^\s+description\s(.+)$', re.M)
  157:         match = desc_re.search(config)
  158          value = match.group(1) if match else None

dist-packages\venv\Lib\site-packages\pyeapi\api\switchports.py:
  101          """
  102:         value = re.search(r'switchport mode (\w+)', config, re.M)
  103          return dict(mode=value.group(1))

  127          """
  128:         value = re.search(r'switchport access vlan (\d+)', config)
  129          return dict(access_vlan=value.group(1))

  141          """
  142:         match = re.search(r'switchport trunk native vlan (\d+)', config)
  143          return dict(trunk_native_vlan=match.group(1))

  155          """
  156:         match = re.search(r'switchport trunk allowed vlan (.+)$', config, re.M)
  157          return dict(trunk_allowed_vlans=match.group(1))

dist-packages\venv\Lib\site-packages\pyeapi\api\system.py:
  81          value = 'localhost'
  82:         match = re.search(r'^hostname ([^\s]+)$', self.config, re.M)
  83          if match:

dist-packages\venv\Lib\site-packages\pyeapi\api\varp.py:
  97                                      r'((?:[a-f0-9]{2}:){5}[a-f0-9]{2})$', re.M)
  98:         mac = mac_address_re.search(self.config)
  99          mac = mac.group(1) if mac else None

dist-packages\venv\Lib\site-packages\pyeapi\api\vlans.py:
  126          """
  127:         value = NAME_RE.search(config).group('value')
  128          return dict(name=value)

  142          """
  143:         value = STATE_RE.search(config).group('value')
  144          return dict(state=value)

dist-packages\venv\Lib\site-packages\pyeapi\api\vrfs.py:
  109          """
  110:         match = RD_RE.search(config)
  111          if match:

  128          """
  129:         value = DESCRIPTION_RE.search(config).group('value')
  130          return dict(description=value)

dist-packages\venv\Lib\site-packages\pyeapi\api\vrrp.py:
  253      def _parse_enable(self, config, vrid):
  254:         match = re.search(r'^\s+vrrp %s shutdown$' % vrid, config, re.M)
  255          if match:

  259      def _parse_primary_ip(self, config, vrid):
  260:         match = re.search(r'^\s+vrrp %s ip (\d+\.\d+\.\d+\.\d+)$' %
  261                            vrid, config, re.M)

  265      def _parse_priority(self, config, vrid):
  266:         match = re.search(r'^\s+vrrp %s priority (\d+)$' % vrid, config, re.M)
  267          value = int(match.group(1)) if match else None

  270      def _parse_timers_advertise(self, config, vrid):
  271:         match = re.search(r'^\s+vrrp %s timers advertise (\d+)$' %
  272                            vrid, config, re.M)

  276      def _parse_preempt(self, config, vrid):
  277:         match = re.search(r'^\s+vrrp %s preempt$' % vrid, config, re.M)
  278          if match:

  288      def _parse_description(self, config, vrid):
  289:         match = re.search(r'^\s+vrrp %s description(.*)$' %
  290                            vrid, config, re.M)

  295      def _parse_mac_addr_adv_interval(self, config, vrid):
  296:         match = re.search(r'^\s+vrrp %s mac-address advertisement-interval '
  297                            r'(\d+)$' % vrid, config, re.M)

  301      def _parse_preempt_delay_min(self, config, vrid):
  302:         match = re.search(r'^\s+vrrp %s preempt delay minimum (\d+)$' %
  303                            vrid, config, re.M)

  307      def _parse_preempt_delay_reload(self, config, vrid):
  308:         match = re.search(r'^\s+vrrp %s preempt delay reload (\d+)$' %
  309                            vrid, config, re.M)

  313      def _parse_bfd_ip(self, config, vrid):
  314:         match = re.search(r'^\s+vrrp %s bfd ip'
  315                            r'(?: (\d+\.\d+\.\d+\.\d+)|)$' %

  321      def _parse_ip_version(self, config, vrid):
  322:         match = re.search(r'^\s+vrrp %s ip version (\d+)$' %
  323                            vrid, config, re.M)

  327      def _parse_delay_reload(self, config, vrid):
  328:         match = re.search(r'^\s+vrrp %s delay reload (\d+)$' %
  329                            vrid, config, re.M)

dist-packages\venv\Lib\site-packages\pylint\checkers\spelling.py:
  200  
  201:                 m = re.search(r"(\W|^)(%s)(\W|$)" % word, line.lower())
  202                  if m:

dist-packages\venv\Lib\site-packages\pylint\test\test_functional.py:
  171      for i, line in enumerate(stream):
  172:         match = _EXPECTED_RE.search(line)
  173          if match is None:

dist-packages\venv\Lib\site-packages\pylint\test\test_self.py:
  144          # configuration file is not found.
  145:         master = re.search("\[MASTER", output)        
  146          out = six.StringIO(output[master.start():])

dist-packages\venv\Lib\site-packages\pyral\context.py:
  248                  elif response.errors and 'ProxyError' in str(response.errors[0]):
  249:                     mo = re.search(r'ProxyError\((.+)\)$', response.errors[0])
  250                      problem = mo.groups()[0][:-1]

  604  ##
  605:         if re.search(r'project/\d+$', project_name): # is project_name really a ref string?
  606              self._currentProject = project_name

  624          """
  625:         if not re.search(r'project/\d+$', self._currentProject):
  626              return (self._currentProject, self.currentProjectRef())

  703  
  704:         if re.search(r'project/\d+$', self._currentProject):
  705              return self._currentProject

  777                  project = proj_path_leaf.Name
  778:             elif re.search('project/\d+$', project):
  779                  prj_ref = project

dist-packages\venv\Lib\site-packages\pyral\entity.py:
  256              else:
  257:                 mo = re.search(r' \'pyral.entity.(\w+)\'>', str(type(value)))
  258                  if mo:

  292              else:
  293:                 mo = re.search(r' \'pyral.entity.(\w+)\'>', str(type(value)))
  294                  if mo:

  352              else:
  353:                 mo = re.search(r' \'pyral.entity.(\w+)\'>', str(type(value)))
  354                  if mo:

  383              else:
  384:                 mo = re.search(r' \'pyral.entity.(\w+)\'>', str(type(value)))
  385                  if not mo:

  504              else:
  505:                 mo = re.search(r' \'pyral.entity.(\w+)\'>', str(type(value)))
  506                  if mo:

  671  for cls_name, cls in classes:
  672:     if cls_name not in _rally_entity_cache and re.search("^[A-Z]", cls_name):
  673          _rally_entity_cache[cls_name] = cls_name

  761          for ancestor in klass.mro():
  762:             mo = re.search(r"'pyral\.entity\.(\w+)'", str(ancestor))
  763              if mo:

dist-packages\venv\Lib\site-packages\pyral\rallyresp.py:
  338                          exception_type, value, traceback = sys.exc_info()
  339:                         exc_name = re.search("'exceptions\.(.+)'", str(exception_type)).group(1)
  340                          problem = '%s: %s for response from request to get next data page for %s' % (exc_name, value, self.target)

dist-packages\venv\Lib\site-packages\pysphere\ZSI\digest_auth.py:
  81      d = dict(challenge=m.groups()[0])
  82:     m = fetch_challenge.auth_param_re.search(http_header)
  83      while m is not None:

  85          d[k.lower()] = v[1:-1]
  86:         m = fetch_challenge.auth_param_re.search(http_header, m.end())
  87           

dist-packages\venv\Lib\site-packages\pysphere\ZSI\wstools\MIMEAttachment.py:
  104          cre = re.compile('^--' + re.escape(b) + '(--)?$', re.MULTILINE)
  105:         if not cre.search(text):
  106              break

dist-packages\venv\Lib\site-packages\redfish\ris\ris.py:
  425  
  426:                 found = re.search(typeregex, fullpath)
  427                  if found:

  470                              dictcopy = item.resp.dict
  471:                             listmatch = re.search('[[][0-9]+[]]', itempath)
  472  

  517                          schemapath = schemapath.replace('/$ref', '')
  518:                         if re.search('\[\d]', schemapath):
  519                              schemapath = schemapath.translate(None, '[]')

dist-packages\venv\Lib\site-packages\rflint\rules\otherRules.py:
  39  
  40:         match=re.search(r'(\s*)$', robot_file.raw_text)
  41          if match:

dist-packages\venv\Lib\site-packages\robot\libraries\BuiltIn.py:
  1167          """
  1168:         res = re.search(pattern, string)
  1169          if res is None:

  1182          """
  1183:         if re.search(pattern, string) is not None:
  1184              raise AssertionError(self._get_string_msg(string, pattern, msg,

dist-packages\venv\Lib\site-packages\robot\libraries\DateTime.py:
  568          input_format = self._remove_f_from_format(input_format)
  569:         match = re.search('\d+$', ts)
  570          if not match:

dist-packages\venv\Lib\site-packages\selenium\webdriver\firefox\firefox_profile.py:
  230                  for usr in f:
  231:                     matches = re.search(PREF_RE, usr)
  232                      try:

dist-packages\venv\Lib\site-packages\SeleniumLibrary\locators\elementfinder.py:
   98              return [locator]
   99:         match = self._split_re.search(locator)
  100          if not match:

  106              locator = locator[span[1] :]
  107:             match = self._split_re.search(locator)
  108          parts.append(locator)

dist-packages\venv\Lib\site-packages\serial\tools\list_ports_windows.py:
  213              if szHardwareID_str.startswith('USB'):
  214:                 m = re.search(r'VID_([0-9a-f]{4})(&PID_([0-9a-f]{4}))?(&MI_(\d{2}))?(\\(\w+))?', szHardwareID_str, re.I)
  215                  if m:

  251              elif szHardwareID_str.startswith('FTDIBUS'):
  252:                 m = re.search(r'VID_([0-9a-f]{4})\+PID_([0-9a-f]{4})(\+(\w+))?', szHardwareID_str, re.I)
  253                  if m:

dist-packages\venv\Lib\site-packages\setuptools\package_index.py:
  849                  # Check for a subversion index page
  850:                 if re.search(r'<title>([^- ]+ - )?Revision \d+:', line):
  851                      # it's a subversion index page:

dist-packages\venv\Lib\site-packages\setuptools\_distutils\filelist.py:
  215          for name in self.allfiles:
  216:             if pattern_re.search(name):
  217                  self.debug_print(" adding " + name)

  235          for i in range(len(self.files)-1, -1, -1):
  236:             if pattern_re.search(self.files[i]):
  237                  self.debug_print(" removing " + self.files[i])

dist-packages\venv\Lib\site-packages\setuptools\_distutils\msvc9compiler.py:
  722                  r""".*?(?:/>|</assemblyIdentity>)""", re.DOTALL)
  723:             if re.search(pattern, manifest_buf) is None:
  724                  return None

dist-packages\venv\Lib\site-packages\setuptools\_distutils\unixccompiler.py:
  290              cflags = sysconfig.get_config_var('CFLAGS')
  291:             m = re.search(r'-isysroot\s*(\S+)', cflags)
  292              if m is None:

dist-packages\venv\Lib\site-packages\setuptools\command\easy_install.py:
  2121          """
  2122:         has_path_sep = re.search(r'[\\/]', name)
  2123          if has_path_sep:

dist-packages\venv\Lib\site-packages\test\test_HPE3ParClient_FilePersona.py:
  156          for line in result:
  157:             if re.search(expected, line):
  158                  break

dist-packages\venv\Lib\site-packages\werkzeug\_internal.py:
  358      while 0 <= i < n:
  359:         o_match = _octal_re.search(b, i)
  360:         q_match = _quote_re.search(b, i)
  361          if not o_match and not q_match:

  386      while i < n:
  387:         match = _cookie_re.search(b + b";", i)
  388          if not match:

dist-packages\venv\Lib\site-packages\werkzeug\debug\__init__.py:
  86              ).communicate()[0]
  87:             match = re.search(b'"serial-number" = <([^>]+)', dump)
  88  

dist-packages\venv\Lib\site-packages\werkzeug\sansio\multipart.py:
  143          if self.state == State.PREAMBLE:
  144:             match = self.preamble_re.search(self.buffer)
  145              if match is not None:

  154          elif self.state == State.PART:
  155:             match = BLANK_LINE_RE.search(self.buffer)
  156              if match is not None:

  189              else:
  190:                 match = self.boundary_re.search(self.buffer)
  191                  if match is not None:

fc-tests\fc-tests\em_cli.py:
   111      try:
   112:         m = re.search(r"HTTP/1\.1 (\d+)", resp)
   113          return int(m.group(1))

   738  
   739:             m = re.search(r"X-Auth-Token: (\S+)", header)
   740              self._session_token = m.group(1)
   741:             m = re.search(r"Location: (\S+)", header)
   742              self._session_uri = m.group(1)

  1581          header = EM_CONTEXT.curl(uri, "GET")[1]
  1582:         m = re.search(r"ETag: \"(\S+)\"", header)
  1583          if not m:

  1639          resp = EM_CONTEXT.curl("/rest/v1", "GET")[0]
  1640:         m = re.search(r"ThisEnclosureManager.+?href\": \"(.+?)\"", resp)
  1641          this_em_uri = m.group(1)

  2053  
  2054:         m = re.search(r"^\S+:\/\/\S+\/(\S+)$", img)
  2055          if m:

  2074              try:
  2075:                 m = re.search(r"(\S+\/\.hpsetup)", buf)
  2076                  inst = m.group(1)
  2077              except:
  2078:                 m = re.search(r"(\S+\/\.setup)", buf)
  2079                  inst = m.group(1)
  2080:             m = re.search(r"(\S+\.tars)", buf)
  2081              img = m.group(1)

fc-tests\fc-tests\latest-mani-jenkins-backup\em_cli.py:
    75      try:
    76:         m = re.search(r"HTTP/1\.1 (\d+)", resp)
    77          return int(m.group(1))

   301  
   302:             m = re.search(r"X-Auth-Token: (\S+)", header)
   303              self._session_token = m.group(1)
   304:             m = re.search(r"Location: (\S+)", header)
   305              self._session_uri = m.group(1)

   940          header = EM_CONTEXT.curl(uri, "GET")[1]
   941:         m = re.search(r"ETag: \"(\S+)\"", header)
   942          if not m:

   989          resp = EM_CONTEXT.curl("/rest/v1", "GET")[0]
   990:         m = re.search(r"ThisEnclosureManager.+?href\": \"(.+?)\"", resp)
   991          this_em_uri = m.group(1)

  1267  
  1268:         m = re.search(r"^\S+:\/\/\S+\/(\S+)$", img)
  1269          if m:

  1288              try:
  1289:                 m = re.search(r"(\S+\/\.hpsetup)", buf)
  1290                  inst = m.group(1)
  1291              except:
  1292:                 m = re.search(r"(\S+\/\.setup)", buf)
  1293                  inst = m.group(1)
  1294:             m = re.search(r"(\S+\.tars)", buf)
  1295              img = m.group(1)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\cli\oa\oa_operation.py:
  21              else:
  22:                 if re.search(r'Successfully reset the E-Fuse for device bay %s' % bay.number, output):
  23                      logger.info("'RESET SERVER %s' successfully performed on enclosure '%s' bay '%s'" % (bay.number, encl.name, bay.number), also_console=True)

  34                          else:
  35:                             if re.search(r'Product Name: %s' % bay.ProductName, output):
  36                                  logger.info("'SHOW SERVER INFO %s' successfully got 'Product Name: %s' on enclosure '%s' bay '%s'" % (bay.number, bay.ProductName, encl.name, bay.number), also_console=True)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\cli\oneview\fusion_operation.py:
   72          else:
   73:             if re.search(spp_file_name, output):
   74                  logger.debug("SPP file <%s> already exists in appliance's local directory, will check md5 first" % spp_file_name)

   82                  else:
   83:                     if re.search(spp_file_md5, output):
   84                          logger.debug("existed SPP iso file <%s> validate successfully" % spp_file_name)

  117                  else:
  118:                     if re.search(spp_file_md5, output):
  119                          logger.debug("successfully downloaded SPP iso file <%s>" % spp_file_name)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\cli\traffic\ping.py:
  285          try:
  286:             m = re.search(r'(\d{1,2}[/|-]\d{1,2}[/|-]\d{4}\s*\d{1,2}:\d{1,2}:\d{1,2}(?:.\d{2,3})?)', line)  # 04/09/2017  0:18:06
  287              if m:

  298                      return False
  299:             m = re.search(r'(\d{1,2}[/|-]\d{1,2}[/|-]\d{2}\s*\d{1,2}:\d{1,2}:\d{1,2}(?:.\d{2,3})?)', line)
  300              if m:

  454                          file_content = File.readlines()
  455:                         if not re.search(r'\w', file_content[-1], re.I):
  456                              file_content.pop()

  459                              line = self._format_line(line)
  460:                             if line.startswith('ping') or 'Pinging' in line or 'bytes of data' in line or not re.search('[a-z]', line, re.IGNORECASE):
  461                                  continue

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\cli\traffic\vsp.py:
  160  
  161:             if re.search(r'lo|virb', item[0], re.I):
  162                  continue

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\keywords\fusion_api.py:
  252                  pattern = re.compile(str(valDict[key]))
  253:                 # if not re.search(str(valDict[key]), str(respDict[key])):
  254                  # t = re.compile('(?i)Warning|Unknown|Terminated|Killed|Error|Completed')
  255  
  256:                 if not re.search(pattern, str(respDict[key])):
  257  

  575                                  for j in xrange(0, len(response[key])):
  576:                                     if re.search(exp, response[key][j], re.M | re.I):
  577                                          logger.info(("%sfound item in list: [%s]" % (tabs, exp)), also_console=False)

  594                                  for j in xrange(0, len(response[key])):
  595:                                     if re.search('/rest/', response[key][j]):
  596                                          resp = self.fusion_api_get_resource(str(response[key][j]))

  659              if key in response:
  660:                 if (isinstance(response[key], str) or isinstance(response[key], unicode)) and re.search(r'/rest/', response[key], re.I):
  661                      words = expected[key].split(":")

  691                      if compare_as_regex:
  692:                         found = re.search(exp_name, response[key], re.M | re.I)
  693                          msg = "[" + key + "] " + exp_name + " vs " + response[key]

  758                      response_key = response[key] if isinstance(response[key], unicode) else str(response[key])
  759:                     found = re.search(pattern, response_key, re.M | re.I)
  760                      msg = "[" + key + "] " + pattern + " vs " + response_key

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\keywords\scale\wf_deploy_os.py:
  56          ilo = dict()
  57:         token = re.search('(?<=sessionkey=)\S*$', r['remoteConsoleUrl'])
  58  

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\performance\listener.py:
  817                          test_results.append('response_body is %s \n' % body)
  818:                     location = re.search(
  819                          '"location": "(\/[a-z,0-9,/]+[A-Z,0-9,-]+)',
  820                          mess)
  821:                     created = re.search(
  822                          '"created": "([0-9+,0-9,-]+T[0-9,0-9,:]+.[0-9]+Z)',
  823                          mess)
  824:                     modified = re.search(
  825                          '"modified": "([0-9+,0-9,-]+T[0-9,0-9,:]+.[0-9]+Z)',
  826                          mess)
  827:                     category = re.search('"category":\s"([a-z]+)"', mess)
  828                      if 'category' in response_body and response_body[

  920  
  921:                     task_percent = re.search(
  922                          '"computedPercentComplete":\s([0-9]+)',

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\business_logic\base.py:
   687          """
   688:         m = re.search(r"^id=(.*)", select_id.replace(' ', ''))
   689          if m is not None:

   758  
   759:         m = re.search(r"^id=(.*)", input_id.replace(' ', ''))
   760          if m is not None:

  1057  
  1058:         m = re.search(r"^(?<!\\)/(.+)(?<!\\)/([i]*)$", expect_value.strip())
  1059  

  1101          logger.debug("verifying that '%s' should NOT contain '%s' ..." % (item_name, excluded_value))
  1102:         m = re.search(r"^(?<!\\)/(.+)(?<!\\)/([i]*)$", excluded_value.strip())
  1103  

  1453          # get tableid if in format 'id=xyz'
  1454:         search_res = re.search(r"^id=(.*)", formid.replace(' ', ''))
  1455          if search_res is not None:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\business_logic\settings\addressandidentifiers.py:
   86          logger.debug("getting ID part of locator '{}'".format(idlocator))
   87:         search_result = re.search(r"^id=(.*)", idlocator.replace(' ', ''))
   88          if search_result is not None:

  264          logger.debug("Expanding all Collapsible in dialog")
  265:         search_result = re.search(r"^xpath=(.*)", locator)
  266          if search_result is not None:

  302          logger.debug("Getting associated object visible count")
  303:         search_result = re.search(r"^xpath=(.*)", locator)
  304          if search_result is not None:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\facilities\racks.py:
   87              rack_name = selenium2lib.get_table_cell(FusionRacksPage.ID_RACK_LIST_TABLE, i, 2)
   88:             if name_pattern is not None and re.search(name_pattern, rack_name) is None:
   89                  continue

  429      server_slot = selenium2lib.get_element_attribute(FusionRacksPage.ID_SERVER_NAME_IN_RACK % server.name)
  430:     slot_no = re.search(r'Slots (\d+):\d+', server_slot).group(1)
  431  

  887          server_slot = selenium2lib.get_element_attribute(FusionRacksPage.ID_ATTR_TITLE_PDU % pdu.pduip)
  888:         slot_no = re.search(r'Slots \d+:(\d+)', server_slot).group(1)
  889          if slot_no != pdu.row:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\mantra\utils\mantraUtils.py:
  80              for line in tempfile:
  81:                 fileInMemory = re.search("(BL.*.-)", line)
  82                  if fileInMemory:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\networking\interconnects.py:
  1330  
  1331:                         m = re.search("Transmitted errors (.*)", dataP)
  1332                          if m:

  1334  
  1335:                         m = re.search("Received errors (.*)", dataP)
  1336                          if m:

  1342                              continue
  1343:                         m = re.search("input packets (.*)", dataP)
  1344                          if m:
  1345                              datadict["input packets"] = m.group(1).strip()
  1346:                         m = re.search("output packets (.*)", dataP)
  1347                          if m:

  1619                      ''' Store output and input packets'''
  1620:                     m = re.search("input packets (.*)", dataP)
  1621                      if m:
  1622                          datadict["input packets"] = m.group(1).strip()
  1623:                     m = re.search("output packets (.*)", dataP)
  1624                      if m:

  3574          data = data.strip()
  3575:         m = re.search('Firmware Version: (.*)', data)
  3576          if m:

  3586          data = data.strip()
  3587:         m = re.search('Firmware Version: (.*)', data)
  3588          if m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\networking\logicalinterconnectgroups.py:
  4977                              logger.info(i)
  4978:                             if re.search(i, dot1p_priority_ui):
  4979                                  if dot1p_priority_ui != besteffort_fcoe_priority[0] and dot1p_priority_ui != besteffort_fcoe_priority[1]:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\networking\logicalinterconnects.py:
   990                          import re
   991:                         pm = re.search('Select at least one interconnect for activation', eth_unselect_error_msg)
   992                          if pm:

  1027  
  1028:                             pm = re.search('Select at least one interconnect for activation', fc_unselect_error_msg)
  1029                              if pm:

  1046                              delay_fc_error_msg = ui_lib.get_text(FusionLogicalInterconnectsPage.ID_FC_empt_del_err)
  1047:                             pmeth = re.search('This field is required', delay_eth_error_msg)
  1048:                             pmfc = re.search('This field is required', delay_fc_error_msg)
  1049                              if pmeth:

  3336                              logger.info(i)
  3337:                             if re.search(i, dot1p_priority_ui):
  3338                                  if dot1p_priority_ui != besteffort_fcoe_priority[0] and dot1p_priority_ui != besteffort_fcoe_priority[1]:

  4132                          import re
  4133:                         pattern_match = re.search('Select at least one interconnect for activation', eth_unselect_error_msg)
  4134                          if pattern_match:

  4160  
  4161:                             pattern_match = re.search('Select at least one interconnect for activation', fc_unselect_error_msg)
  4162                              if pattern_match:

  4176                              result = C7000LogicalInterconnectsUpdateFirmware.get_error_message_from_activation()
  4177:                             error_eth = re.search('This field is required', str(result['delay_eth_error_msg']))
  4178:                             error_fc = re.search('This field is required', str(result['delay_fc_error_msg']))
  4179                              if error_eth:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\networking\logicalswitches.py:
  851              data = _get_switch_data(primary_ip, user_name, password, "show interface mgmt0")
  852:             m = re.search("Hardware: GigabitEthernet, address.*: .*", data)
  853              mac = m.group()

  859          data = _get_switch_data(primary_ip, user_name, password, "show vpc brief")
  860:         domainid = re.search("vPC domain id.*: .*", data)
  861          id = domainid.group()

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\servers\enclosures.py:
  1789  
  1790:         if re.search(expected_txt, msg[1]) is None:
  1791              ui_lib.fail_test("Error message doesn't contains expected text. Expected text: %s" % expected_txt)

  4993  
  4994:             ovpm = re.search('No update required. Selected firmware is already installed for the Onboard Administrator', neg_msg)
  4995              if ovpm:

  5021  
  5022:             ovpm = re.search('No update required. Selected firmware is already installed for the Onboard Administrator', neg_msg)
  5023              if ovpm:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\servers\logicalenclosures.py:
  2325                          action_status_time = ui_lib.get_text(FusionLogicalEnclosuresPage.ID_STATUS_BAR)
  2326:                         A_status_time = re.search('Completed\d+\w\d+s', action_status_time)
  2327                          if A_status_time:

  2329                              Completewithtime = A_status_time.group()
  2330:                             ActualTimeTaken = re.search('\d+\w+', Completewithtime)
  2331                              CompletedTimeonly = ActualTimeTaken.group()

  2634              if hasattr(switch_obj, "intentEdit"):  # since we donot check this attr for "Synergy 40Gb F8 Switch", no error is thrown
  2635:                 if re.search(switch_obj.intentEdit, iblrow_data):
  2636  
  2637:                     logger.info(" %s Matches expected %s." % (re.search(switch_obj.intentEdit, iblrow_data).group(), switch_obj.intentEdit))
  2638                  else:

  2642  
  2643:             if re.search(switch_obj.icmModel, iblrow_data):
  2644:                 logger.info(" ICM Found %s is same as expected %s" % (re.search(switch_obj.icmModel, iblrow_data).group(), switch_obj.icmModel))
  2645              else:

  2647  
  2648:             if re.search(switch_obj.logicalInterconnectEdit, iblrow_data):
  2649:                 logger.info(" ICM Found %s is same as expected.%s" % (re.search(switch_obj.logicalInterconnectEdit, iblrow_data).group(), switch_obj.logicalInterconnect))
  2650              else:

  2786              li_data = TBirdVerifyLogicalEnclosures.get_le_interconnect_bay_licensing_editpanel_Baydata(icm_obj.enclosure, icm_obj.bay, timeout=20)
  2787:             if re.search(icm_obj.icmModel, li_data):
  2788:                 logger.info(" ICM Found %s is same as expected %s" % (re.search(icm_obj.icmModel, li_data).group(), icm_obj.icmModel))
  2789              else:

  2791  
  2792:             if re.search(icm_obj.logicalInterconnectEdit, li_data):
  2793:                 logger.info(" ICM Found %s is same as expected.%s" % (re.search(icm_obj.logicalInterconnectEdit, li_data).group(), icm_obj.logicalInterconnect))
  2794              else:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\FusionLibrary\ui\settings\settings.py:
  896  #         if getattr(lic, 'licensepath', '') != '':
  897: #             if re.search(r'noiLO_\d+\.dat$', lic.licensepath):
  898  #                 logger._log_to_console_and_log_file("check for the existence of HP OneView w/o iLO license")
  899  #                 strlicense = "HP OneView w/o iLO"
  900: #             elif re.search(r'\d+\.dat$', lic.licensepath):
  901  #                 logger._log_to_console_and_log_file("check for the existence of HP OneView license ")

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\activity\ActivityHelpers.py:
   32      if taskState != '':
   33:         if re.search(task_tree['resource']['taskState'], taskState):
   34              nodes.append(task_tree['resource'])

   53      for task in task_list:
   54:         if re.search(task['taskState'], taskState):
   55              for taskError in task['taskErrors']:

   57                      for nestedError in taskError['nestedErrors']:
   58:                         if re.search(errorMessage, nestedError['message']):
   59                              found = True
   60                  else:
   61:                     if re.search(errorMessage, taskError['message']):
   62                          found = True

   74      for task in task_list:
   75:         if re.search(task['taskState'], taskState):
   76              for taskError in task['taskErrors']:

  130      # Convert timeout to seconds if passed in as minutes: 10m.
  131:     if re.search(r'm', timeout, re.I):
  132          logger._log_to_console_and_log_file(

  135  
  136:     if re.search(r'm', interval, re.I):
  137          logger._log_to_console_and_log_file(

  246  
  247:                 if re.search(expected_error_message, actMessage):
  248                      logger.warn(

  288              # Exit loop if taskState PASS
  289:             if re.search(PASS, taskState):
  290                  logger._log_to_console_and_log_file(

  296              # Exit loop if taskState BREAK_LOOP_IF
  297:             if re.search(BREAK_LOOP_IF, taskState):
  298                  logger._log_to_console_and_log_file(

  475      """
  476:     if isinstance(event, dict) and re.search('Event', event['type']):
  477          check = 'FAIL'

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\common\CpqlocfgHelper.py:
  123          logger._debug("Security name %s" % e.attrib['VALUE'])
  124:         if re.search(user, e.attrib['VALUE']):
  125              check = True

  141      for e in tree.iter():
  142:         if re.search('SNMP_ADDRESS', e.tag):
  143              fields = e.tag.split('_')

  146                  # change IPv6 address format
  147:                 if re.search(r':', ip):
  148                      ip = re.sub(r'(:0){2,}', ':', ip)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\common\RisHelpers.py:
  461      """
  462:     if isinstance(profile, dict) and re.search('ServerProfile', profile['type']):
  463          BuiltIn().log('Checking mpsettings local accounts for profile %s' % profile['name'], console=True)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\networking\NetworkingHelpers.py:
  125          ic_uri = response['members'][0]['uri']
  126:         rtn = re.search('[\w\d]{8}-[\w\d]{4}-[\w\d]{4}-[\w\d]{4}-[\w\d]{12}', ic_uri)
  127          ic_uuid = rtn.group(0)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\oa\CompareCLP.py:
  70          # split into sections.  match '-' line so we don't have a hardcoded length of '-'.
  71:         eListMatchObj = re.search('(-+)', expect)
  72:         aListMatchObj = re.search('(-+)', actual)
  73          eList = expect.split(eListMatchObj.group(1))

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\oa\OaHelpers.py:
   67              for line in output_string.split('\n'):
   68:                 if re.search('0x', line):
   69                      fields = line.split()

   88      for snmp_user in snmp_users:
   89:         if re.search(user, snmp_user):
   90              check = True

  183                  line = line.strip()
  184:                 if re.search('^[\d\w-]*\\.[\d\w-]*\\.', line):
  185                      fields = line.split()

  235                  else:
  236:                     if fields[0] == destination and re.search(user, fields[1]):
  237                          check = True

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\servers\ProfileHelpers.py:
   46      """
   47:     if isinstance(spt, dict) and re.search('ServerProfileTemplate', spt['type']):
   48          lookup_ATAI = False

   50              for va in spt['sanStorage']['volumeAttachments']:
   51:                 if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
   52                      lookup_ATAI = True

   63                      for va in vas:
   64:                         if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
   65:                             rtn = re.search("^(SPTVAID):(\d*)$", va['associatedTemplateAttachmentId'])
   66                              spt_va_id = int(rtn.group(2))

  123      """
  124:     if isinstance(profile, dict) and re.search('ServerProfile', profile['type']):
  125          lookup_ATAI = False

  127              for va in profile['sanStorage']['volumeAttachments']:
  128:                 if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
  129                      lookup_ATAI = True

  144                          for va in vas:
  145:                             if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
  146:                                 rtn = re.search("^(SPTVAID):(\d*)$", va['associatedTemplateAttachmentId'])
  147                                  spt_va_id = int(rtn.group(2))

  205      """
  206:     if isinstance(profile, dict) and re.search('ServerProfile', profile['type']):
  207          lookup_ATAI = False

  209              for va in profile['sanStorage']['volumeAttachments']:
  210:                 if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
  211                      lookup_ATAI = True

  224                      for va in vas:
  225:                         if 'associatedTemplateAttachmentId' in va and va['associatedTemplateAttachmentId'] is not None and re.search("^SPTVAID", va['associatedTemplateAttachmentId']):
  226:                             rtn = re.search("^(SPTVAID):(\d*)$", va['associatedTemplateAttachmentId'])
  227                              spt_va_id = int(rtn.group(2))

  254      """
  255:     if isinstance(profile, dict) and re.search('ServerProfile', profile['type']):
  256          logger._log_to_console_and_log_file('Verifying volume attachments for profile %s' % profile['name'])

  268                      volume_name = volume_attachment['volumeName'] if volume_attachment['volumeUri'] is None else volume_attachment['volumeUri']
  269:                     if re.search(':', volume_name):
  270                          start = volume_name.index(':')

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\servers\server_profile.txt:
  1220      \    ${ca_name} =  Get From Dictionary  ${os_ca}  name
  1221:     \    ${regex_match} =  Evaluate  re.search(r'networkuri', '${ca_name}', re.I)    re
  1222      \    Run Keyword If  '${regex_match}' == 'None'  continue For Loop

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\settings\TrapListener.py:
  36          log_file.write("%s actual data size: %s\n" % (str(datetime.now()), len(data)))
  37:         if isinstance(data, (str, unicode)) and re.search(args.validate_string, data) and len(data) > args.data_size:
  38              # write PASS to the status file

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Resources\api\storage\StorageHelpers.py:
   97      """
   98:     if isinstance(svas, dict) and re.search('StorageVolumeAttachment', svas['type']):
   99          logger._log_to_console_and_log_file("The argument svas is SVA DTO.  Convert to list.")

  102          raise AssertionError("The argument svas %s is an empty list" % svas)
  103:     elif isinstance(svas, list) and isinstance(svas[0], dict) and re.search('StorageVolumeAttachment', svas[0]['type']):
  104          logger._log_to_console_and_log_file("The argument svas is a list of SVA DTO")

  145                      BuiltIn().log("Storage System port %s has mode %s, connectionState %s, and status %s" % (resp_port['name'], resp_port['mode'], resp_port['connectionState'], resp_port['status']), console=True)
  146:                     if (resp_port['mode'] != 'Managed') or (resp_port['connectionState'] != 'Connected') or (not re.search('OK|WARNING', resp_port['status'])):
  147                          check = 'FAIL'

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\ACI_Istanbul\APICOperations.py:
  616                                  if domType == 'vmmDomP':
  617:                                     domName = re.search(
  618                                          '.*vmmp-VMware/dom-(\w+)',

  663                                  if domType == 'vmmDomP':
  664:                                     domName = re.search(
  665                                          '.*vmmp-VMware/dom-(\w+)',

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\ACI_Istanbul\data_disable_autoremediate2_native.py:
   989      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
   990:     result = re.search(tenant_uri_regex, uri)
   991      tenant_Id = result.group(1)

  1055      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  1056:     result = re.search(tenant_uri_regex, uri)
  1057      tenant_Id = result.group(1)

  1129      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  1130:     result = re.search(tenant_uri_regex, uri)
  1131      tenant_Id = result.group(1)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\ACI_Istanbul\data_disable_autoremediate2.py:
   931      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
   932:     result = re.search(tenant_uri_regex, uri)
   933      tenant_Id = result.group(1)

   997      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
   998:     result = re.search(tenant_uri_regex, uri)
   999      tenant_Id = result.group(1)

  1071      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  1072:     result = re.search(tenant_uri_regex, uri)
  1073      tenant_Id = result.group(1)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\ACI_Istanbul\data_var_75562.py:
  740      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  741:     result = re.search(tenant_uri_regex, uri)
  742      tenant_Id = result.group(1)

  802      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  803:     result = re.search(tenant_uri_regex, uri)
  804      tenant_Id = result.group(1)

  872      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  873:     result = re.search(tenant_uri_regex, uri)
  874      tenant_Id = result.group(1)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\ACI_Istanbul\OVF75562_data_variable.py:
  1326      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  1327:     result = re.search(tenant_uri_regex, uri)
  1328      tenant_Id = result.group(1)

  1392      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  1393:     result = re.search(tenant_uri_regex, uri)
  1394      tenant_Id = result.group(1)

  1466      tenant_uri_regex = '/rest/fabric-managers/.*/tenants/(.*)'
  1467:     result = re.search(tenant_uri_regex, uri)
  1468      tenant_Id = result.group(1)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\DEA\HAL\resources\variables.py:
  547              # Find 'MgmtIP' followed by the IPv6 address.
  548:             matches = re.search(r'MgmtIP:\s*(\S*:\S*:\S*:\S*:\S*:\S*)', output, re.MULTILINE)
  549              if matches:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\DEA\tests\PE-Test-OV-Deploy\resources\variables.py:
  408              # Find 'MgmtIP' followed by the IPv6 address.
  409:             matches = re.search(r'MgmtIP:\s*(\S*:\S*:\S*:\S*:\S*:\S*)', output, re.MULTILINE)
  410              if matches:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\DFRM\DCS\UserInputs\remotelogin.py:
  45              elif index == 2:
  46:                 if re.search("All keys were skipped because they already exist on the remote system",
  47                               child.before) is not None:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\Mellanox\Manganese_L2_features\ServerOperations_IGMP.py:
  431                      if adapter in line:
  432:                         pat_out = re.search(r'(\w+-\w+-\w+-\w+-\w+-\w+)', line)
  433                          print ("pat out is %s" % pat_out.group(1))

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\tests\Mellanox\Manganese_L2_features\ServerOperations_Storm_Control.py:
  225                      if adapter in line:
  226:                         pat_out = re.search(r'(\w+-\w+-\w+-\w+-\w+-\w+)', line)
  227                          print "pat out is %s" % pat_out.group(1)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Tools\Build_Fusion_API_Documentation.py:
  28  def sort_by_keyword(kw):
  29:     matchObj = re.search("html>(\w.*)</a", kw)
  30      if (not matchObj):

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Tools\Build_Data_From_OV_Resource\Build_Data_Dict.py:
  86                  if isinstance(response[key], str) or isinstance(response[key], unicode):
  87:                     matchObj = re.search(r'/rest/(.*)/', response[key], re.I)
  88                      if matchObj:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Tools\Build_Data_From_OV_Resource\Build_Expected_from_Response.py:
  58              if isinstance(response[key], str) or isinstance(response[key], unicode):
  59:                 matchObj = re.search(r'/rest/(.*?)/', response[key], re.I)
  60                  if matchObj:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Tools\Build_Data_From_OV_Resource\Build_Initial_Template.py:
  47              if isinstance(response[key], str) or isinstance(response[key], unicode):
  48:                 # matchObj = re.search(r'(/rest/.*)', response[key], re.I)
  49                  # if matchObj:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\Tools\performance\listener.py:
  634                      test_results.append('response_body is %s \n' % body)
  635:                 location = re.search(
  636                      '"location": "(\/[a-z,0-9,/]+[A-Z,0-9,-]+)',
  637                      mess)
  638:                 created = re.search(
  639                      '"created": "([0-9+,0-9,-]+T[0-9,0-9,:]+.[0-9]+Z)',
  640                      mess)
  641:                 modified = re.search(
  642                      '"modified": "([0-9+,0-9,-]+T[0-9,0-9,:]+.[0-9]+Z)',
  643                      mess)
  644:                 category = re.search('"category":\s"([a-z]+)"', mess)
  645                  if 'category' in response_body and response_body[

  737  
  738:                 task_percent = re.search(
  739                      '"computedPercentComplete":\s([0-9]+)',

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\wheel_builder.py:
  42      """
  43:     return bool(_egg_info_re.search(s))
  44  

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\index\package_finder.py:
  223  
  224:         match = self._py_version_re.search(version)
  225          if match:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\models\link.py:
  162          # type: () -> Optional[str]
  163:         match = self._egg_fragment_re.search(self._url)
  164          if not match:

  172          # type: () -> Optional[str]
  173:         match = self._subdirectory_fragment_re.search(self._url)
  174          if not match:

  184          # type: () -> Optional[str]
  185:         match = self._hash_re.search(self._url)
  186          if match:

  192          # type: () -> Optional[str]
  193:         match = self._hash_re.search(self._url)
  194          if match:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\req\constructors.py:
  332          # Handle relative file URLs
  333:         if link.scheme == 'file' and re.search(r'\.\./', link.url):
  334              link = Link(

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  356                  # original file is over http
  357:                 if SCHEME_RE.search(filename):
  358                      # do a url join so relative paths work

  360                  # original file and nested file are paths
  361:                 elif not SCHEME_RE.search(req_path):
  362                      # do a join so relative paths work

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\utils\encoding.py:
  33      for line in data.split(b'\n')[:2]:
  34:         if line[0:1] == b'#' and ENCODING_RE.search(line):
  35:             result = ENCODING_RE.search(line)
  36              assert result is not None

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_internal\vcs\subversion.py:
  151          elif data.startswith('<?xml'):
  152:             match = _svn_xml_url_re.search(data)
  153              if not match:

  168                  )
  169:                 url = _svn_info_xml_url_re.search(xml).group(1)
  170                  revs = [

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distro.py:
   989              # If there is no version_codename, parse it from the version
   990:             codename = re.search(r'(\(\D+\))|,(\s+)?\D+', props['version'])
   991              if codename:

  1057          props = {}
  1058:         match = re.search(r'^([^\s]+)\s+([\d\.]+)', lines[0].strip())
  1059          if match:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\manifest.py:
  291          for name in self.allfiles:
  292:             if pattern_re.search(name):
  293                  self.files.add(name)

  311          for f in list(self.files):
  312:             if pattern_re.search(f):
  313                  self.files.remove(f)

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\util.py:
  709  def get_export_entry(specification):
  710:     m = ENTRY_RE.search(specification)
  711      if not m:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  569                  CFLAGS = _CONFIG_VARS.get('CFLAGS', '')
  570:                 m = re.search(r'-isysroot\s+(\S+)', CFLAGS)
  571                  if m is not None:

  699                  try:
  700:                     m = re.search(r'<key>ProductUserVisibleVersion</key>\s*'
  701                                    r'<string>(.*?)</string>', f.read())

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\distlib\_backport\tarfile.py:
  1402          # the translation to UTF-8 fails.
  1403:         match = re.search(br"\d+ hdrcharset=([^\n]+)\n", buf)
  1404          if match is not None:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  860              if (token["name"] in self.svg_allow_local_href and
  861:                 (namespaces['xlink'], 'href') in attrs and re.search(r'^\s*[^#\s].*',
  862                                                                       attrs[(namespaces['xlink'], 'href')])):

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\urllib3\connection.py:
  191          """Send a request to the server"""
  192:         match = _CONTAINS_CONTROL_CHAR_RE.search(method)
  193          if match:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:
  281              if is_ipv6:
  282:                 match = ZONE_ID_RE.search(host)
  283                  if match:

  356      source_url = url
  357:     if not SCHEME_RE.search(url):
  358          url = "//" + url

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\package_index.py:
  843                  # Check for a subversion index page
  844:                 if re.search(r'<title>([^- ]+ - )?Revision \d+:', line):
  845                      # it's a subversion index page:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\filelist.py:
  215          for name in self.allfiles:
  216:             if pattern_re.search(name):
  217                  self.debug_print(" adding " + name)

  235          for i in range(len(self.files)-1, -1, -1):
  236:             if pattern_re.search(self.files[i]):
  237                  self.debug_print(" removing " + self.files[i])

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\msvc9compiler.py:
  722                  r""".*?(?:/>|</assemblyIdentity>)""", re.DOTALL)
  723:             if re.search(pattern, manifest_buf) is None:
  724                  return None

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\_distutils\unixccompiler.py:
  290              cflags = sysconfig.get_config_var('CFLAGS')
  291:             m = re.search(r'-isysroot\s*(\S+)', cflags)
  292              if m is None:

FusionLibrary-rel-5.20\FusionLibrary-rel-5.20\venv\Lib\site-packages\setuptools\command\easy_install.py:
  2095          """
  2096:         has_path_sep = re.search(r'[\\/]', name)
  2097          if has_path_sep:

lanier-goat-development\rat.py:
  249  if __name__ == '__main__':
  250:     if 'NIMBUS' in os.environ and re.search(
  251              '1|true|yes', os.environ['NIMBUS'], re.I):

lanier-goat-development\ratrest.py:
  22  
  23: if 'NIMBUS' in os.environ and re.search('1|true|yes', os.environ['NIMBUS'], re.I):
  24      phy = False

lanier-goat-development\autotriage\base.py:
  144          overall_exceptions = []
  145:         test_rst_log_file = bool(re.search('test-rst.log', filename))
  146          with open(filename) as f:

  165              for line in f:
  166:                 if not found_exception and re.search(PATTERN, line):
  167                      found_exception = True
  168:                     if re.search(PYTHON_PATTERN, line):
  169                          python_exception = True

  173                          python_exception_str += line
  174:                     elif re.search(JAVA_PATTERN, line):
  175                          java_exception = True

  179                          java_exception_str += line
  180:                     elif re.search(RUBY_PATTERN, line):
  181                          ruby_exception = True

  184                              ruby_exception_str += previous
  185:                     elif re.search(VMODL_PATTERN, line):
  186                          vmodl_exception = True

  209  
  210:                         if test_rst_log_file and re.search(
  211                                  REMOTE_TEST_PATERN, line):
  212                              data = re.split('] ', line)[-1]
  213:                         elif test_rst_log_file and re.search('^\d+', line):
  214                              # Test executed on local system, but still has

  217                              data = re.split('] ', line)[1]
  218:                         if not re.search('^ ', data):
  219                              # If the log line starts without space, consider

  228                          java_exception_str += line
  229:                         if re.search('^\d+', line):
  230                              # Java log that have date time

  238                          vmodl_exception_str += line
  239:                         if re.search('^\d+', line):
  240                              # Vmodl log that have date time

  250                          # exception
  251:                         if not re.search('/', line):
  252                              ruby_exceptions.append(ruby_exception_str)

  257                              found_exception = False
  258:                 # if re.search('^\d+', line):
  259                  if begin_gmt_date.search(line):

  347                  self.log.debug('%s - %s - %s' % (
  348:                     filename, name, re.search(filename, name)))
  349:                 if re.search(filename, name):
  350                      # Return absolute filename with path

  356          self.log.debug('Extract %s in %s' % (filename, destination))
  357:         if re.search('\.tgz$', filename):
  358              # Filename ending with tgz, ignore any errors with file extraction

  362              return destination
  363:         elif re.search('\.gz$', filename):
  364              # Filename ending with gz

  370              return os.path.join(destination, base)
  371:         elif re.search('zip$', filename):
  372              # Filename ending with zip

lanier-goat-development\autotriage\test\vcf_testbed_summary.py:
  39          matchobj = \
  40:             re.search(r'(Logs : (.*)|Health Check : (.*)|Summary : (.*))', out,
  41                        re.M)

lanier-goat-development\bat\ems\dmpipeline.py:
   62  
   63:     if not ('exclude-components' in args.extra_test_args and re.search(
   64              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

  204  
  205:     if not ('exclude-components' in args.extra_test_args and re.search(
  206              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\bat\ems\dmpipelineonenode.py:
  39  
  40:     if not ('exclude-components' in args.extra_test_args and re.search(
  41              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\bat\ems\end2endtest.py:
  66  
  67:     if not ('exclude-components' in args.extra_test_args and re.search(
  68              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\bat\ems\negativeworkflow.py:
  59  
  60:     if not ('exclude-components' in args.extra_test_args and re.search(
  61              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\bat\ems\nfs_domain_test.py:
  75  
  76:     if not ('exclude-components' in args.extra_test_args and re.search(
  77              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\bat\ems\operationmanagertest.py:
  49  
  50:     if not ('exclude-components' in args.extra_test_args and re.search(
  51              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\bat\ems\pipeline2.py:
  353      args.extra_test_args['exclude-components'] = 'LogInsight'
  354:     if not ('exclude-components' in args.extra_test_args and re.search(
  355              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

  364          test_only_value = args.extra_test_args['test-only']
  365:         if re.search('all|true', test_only_value, re.I):
  366              # retrieve all test name that is listed in master TEST_NAMES list

lanier-goat-development\bat\ems\sosregression.py:
  107  
  108:     # if not ('exclude-components' in args.extra_test_args and re.search(
  109      #        'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\bat\nimbus\nimbusrun.py:
  220  
  221:     public_nimbus = re.search('public', args.nimbus, re.I)
  222      pwd = base_folder_path

  388              pattern = (r'FAIL \(|ABORT \(|TIMEOUT \(')
  389:             if not nimbus_fail and re.search(pattern, line, re.I):
  390                  if 'pexpect.exceptions.EOF' in line:

lanier-goat-development\bat\petronas\collect_sos.py:
  39          skip_sos = args.extra_test_args.get('skip-sos')
  40:         if skip_sos and re.search('Yes|True|1', skip_sos, re.I):
  41              args.rt.info('Skipping SOS Collection and Copy')

  43              sos_copy_only = args.extra_test_args.get('sos-copy-only')
  44:             if sos_copy_only and re.search('Yes|True|1', sos_copy_only,
  45                                             re.I):

lanier-goat-development\bat\petronas\petronasrun.py:
   93          setup_only = args.extra_test_args.get('setup-only', '')
   94:         if setup_only and re.search('Yes|True|1', setup_only, re.I):
   95              return

  102          bringup_only = args.extra_test_args.get('bringup-only', '')
  103:         if bringup_only and re.search('Yes|True|1', bringup_only, re.I):
  104              return

lanier-goat-development\bat\sl\physicalbat.py:
  75      setup_only = args.extra_test_args.get('setup-only', '')
  76:     if setup_only and re.search('Yes|True|1', setup_only, re.I):
  77          return

lanier-goat-development\bat\sl\physicalrun.py:
   94          args.log.debug(line.strip(os.linesep))
   95:         if not fail and re.search('FAIL \(|ABORT \(|TIMEOUT \(', line):
   96              fail = True

  103                    'No such file or directory'
  104:         if not fail and re.search(pattern, line, re.I):
  105              fail = True

lanier-goat-development\bat\test\executerecipe.py:
  413      recipe_file_format = recipe_file.split('.')[-1]
  414:     if not re.search('json|txt', recipe_file_format, re.I):
  415          raise AssertionError('Unsupported Type: %s' % recipe_file_format)

  446                          proceed_on_failure = str(variables).lower()
  447:                         if not re.search('false|true', proceed_on_failure,
  448                                           re.I):

  469          return value
  470:     return bool(re.search('true|yes|1', value, re.I))
  471  

lanier-goat-development\bat\test\sos.py:
  204              for line in out:
  205:                 temp_sos_dir = re.search('sos-[\d+-]+\d+', line)
  206                  if temp_sos_dir:

  208                      args.rt.comment(sos_log_dir)
  209:                 suc_log_line = re.search(
  210                      'Log Collection completed successfully for : '

  215                      args.rt.comment(success_log)
  216:                 fail_log_line = re.search('Operation failed for : '
  217                                            '\[''.*\]', line)

lanier-goat-development\bringup\ems\test\create_sddc_secure_group.py:
  79          status = True
  80:         if re.search(ERRORCODE_KEY, str(out)):
  81:             if not re.search(VCF_SECURE_USER_ALREADY_EXISTS, str(out)):
  82                  status = False

lanier-goat-development\bringup\ems\test\verify_drs_enabled.py:
  23      vmc_testbed = args.extra_test_args.get('vmc-testbed', None)
  24:     if vmc_testbed and re.search('Yes|True|1', vmc_testbed, re.I):
  25          vmc_testbed = True

lanier-goat-development\bringup\ems\test\verify_dvs_config.py:
  19      vmc_testbed = args.extra_test_args.get('vmc-testbed', None)
  20:     if vmc_testbed and re.search('Yes|True|1', vmc_testbed, re.I):
  21          vmc_testbed = True

lanier-goat-development\bringup\ems\test\verify_portgroup_configuration.py:
  23      vmc_testbed = args.extra_test_args.get('vmc-testbed', None)
  24:     if vmc_testbed and re.search('Yes|True|1', vmc_testbed, re.I):
  25          vmc_testbed = True

lanier-goat-development\bringup\ems\test\verify_sddc_manager_services.py:
  31      data = sddc.get_node_manager_app_status()
  32:     args.rt.verify_safely((re.search('version', str(data)) is
  33                             not None), True, 'Node Manager service '

  40      data = lcm.get_lcm_app_status()
  41:     args.rt.verify_safely((re.search('version', str(data)) is not
  42                             None), True, 'LCM service is up and '

lanier-goat-development\bringup\test\imaging.py:
  26          for bundle in bundle_list:
  27:             if bundle_build and re.search(bundle_build, bundle['version']):
  28                  # Do not upload and activate bundle, when it already exist

lanier-goat-development\bringup\test\inventorycommon.py:
    52          vmc_testbed = args.extra_test_args.get('vmc-testbed', None)
    53:         if vmc_testbed and re.search('Yes|True|1', vmc_testbed, re.I):
    54              self.vmc_testbed = True

    91              self.args.log.debug(vmref.name)
    92:             if re.search(vm_name, vmref.name, re.I):
    93                  return vmref

  1254          data = self.sddc.get_node_manager_app_status()
  1255:         self.args.rt.verify_safely((re.search('version', str(data)) is
  1256                                      not None), True, 'Node Manager service '

  1264          data = self.lcm.get_lcm_app_status()
  1265:         self.args.rt.verify_safely((re.search('version', str(data)) is not
  1266                                      None), True, 'LCM service is up and '

lanier-goat-development\bringup\test\nsx_controller_count_status_check.py:
  51          for childvm in childvms:
  52:             match = re.search(r'.*management.*', childvm.name, re.IGNORECASE)
  53              if match:

  57                  for vm in list_vms:
  58:                     match = re.search(r'.*controller.*',
  59                                        vm.name, re.IGNORECASE)

lanier-goat-development\bringup\test\slbringup.py:
   51              if out:
   52:                 if re.search('Exception', out):
   53                      raise AssertionError(
   54                          'Exception raised by swagger sdk test')
   55:                 elif re.search('COMPLETED_WITH_FAILURE', out):
   56                      raise AssertionError(

  343                  for f in files:
  344:                     if re.search('swagger-sdk-test', f) and re.search('.jar',
  345                                                                        f):

lanier-goat-development\bringup\test\validateli.py:
  19          VRM_INITIAL_IP, ROOT_USER, s.util.vrm_password)
  20:     if out[0] and not re.search('No such file or directory', out[0]):
  21          args.rt.info('New LI already exist')

lanier-goat-development\ci_pipeline\metadata_check.py:
  35          if filename.endswith('.py') and filename not in self.__ignore['files'] and \
  36:                 filename != '__init__.py' and not re.search('^.#', filename):
  37              for a_dir in self.__ignore['folders']:

  79                  for line in f:
  80:                     if re.search(r'#\s+Copyright\s+.*', line, re.I):
  81                          copyright = True
  82:                     elif re.search(r'#\s+Description:(.+)\n$', line, re.I):
  83                          description = True
  84:                     elif re.search(r'#\s+Disabled:(.+)\n$', line, re.I):
  85                          disabled = True
  86                      else:
  87:                         match = re.search(r'#\s+Group-([^:]+):(.+)\n$', line, re.I)
  88                          if match:

lanier-goat-development\ci_pipeline\unittests\ut_metadata_check.py:
  46              ex = str(ex)
  47:             no_copyright = re.search('"Copyright:" metadata not found', ex, re.I)
  48:             no_description = re.search('"Description:" metadata not found', ex, re.I)
  49:             no_group_no_disabled = re.search('needs a "Group\-\*:" or "Disabled:" metadata field',
  50                                               ex, re.I)
  51:             no_group_options = re.search('must be either "required", "optional" ,or "disabled"',
  52                                           ex, re.I)

lanier-goat-development\clone\test\clonetestbed.py:
   75      jump_vm_info = {}
   76:     public_nimbus = re.search('public', args.nimbus, re.I)
   77      # Following commands will be executed in remote Jump VM

  157          args.log.info(line.strip(os.linesep))
  158:         if not fail and re.search('FAIL \(|ABORT \(|TIMEOUT \(', line):
  159              fail = True

  165          pattern = 'Exception|Broken pipe|Connection timed out|No such file or directory|Terminated'
  166:         if not fail and re.search(pattern, line, re.I):
  167              fail = True

lanier-goat-development\clonevm\clone_vm.py:
    46              for f in os.listdir(centosdir):
    47:                 if re.search('.*\.egg', f):
    48                      sys.path.append(os.path.join(centosdir, f))

   147      # winjump
   148:     if re.search('vcf-win-', vm_name):
   149          basetype = 'windows'

   151      # linjump
   152:     elif re.search('vcf-ems-centos', vm_name):
   153          basetype = 'centos'

   155      # ad
   156:     elif re.search('vcf-dc01rpl-', vm_name):
   157          basetype = 'windows'

   159      # sql server
   160:     elif re.search('vcf-mssql-', vm_name):
   161          basetype = 'windows'

   163      # nfs server
   164:     elif re.search('vcf-nfs-server', vm_name):
   165          basetype = 'freebsd'

   167      # cloudbuilder
   168:     elif re.search(r'\.ovfVm', vm_name):
   169          basetype = 'photon'

   171      # nat for ssh/http/https
   172:     elif re.search('-vxlan-.*-gw', vm_name):
   173          basetype = 'centos'

  2912          # print('line is "%s"' % line)
  2913:         m = re.search('^[0-9]*:  *([^ ][^ ]*):', line)
  2914          if m:

  2924              nic['name'] = m.group(1).strip()
  2925:             m = re.search('^(.*)@.*$', nic['name'])
  2926              if m:

  2929          if state == 1:
  2930:             m = re.search('^ *link/ether  *(..:..:..:..:..:..) ', line)
  2931              if m:

  2935          elif state == 2:
  2936:             m = re.search(
  2937                  '^ *inet  *([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*)/([0-9]*) ', line)

  2972          # print('line is "%s"' % line)
  2973:         m = re.search(
  2974              '^default via ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*) dev (.*)$', line)

  3007          # print('line is "%s"' % line)
  3008:         m = re.search('^.*ifcfg-(.*)$', line)
  3009          if m:

  3037              # print('line is "%s"' % line)
  3038:             m = re.search('^.*ifcfg-(.*)$', line)
  3039              if m:

  3210          # print('line is "%s"' % line)
  3211:         m = re.search('^Ethernet adapter (.*):', line)
  3212          if m:

  3224          if state == 1:
  3225:             m = re.search('^ *Physical Address.*: (.*)$', line)
  3226              if m:

  3230          elif state == 2:
  3231:             m = re.search(
  3232                  '^ *DHCP Enabled.*: (.*)$', line)

  3242          elif state == 3:
  3243:             m = re.search(
  3244                  '^ *IPv4 Address.*: ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*).*$',

  3250          elif state == 4:
  3251:             m = re.search(
  3252                  '^ *Subnet Mask.*: ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*).*$',

  3258          elif state == 5:
  3259:             m = re.search(
  3260                  '^ *Default Gateway.*: ([0-9]*\.[0-9]*\.[0-9]*\.[0-9]*).*$',

  4203          for name in list(settings.db['clones'].keys()):
  4204:             if re.search(pattern, name):
  4205                  clone = settings.db['clones'][name]

  4437          vm_name = moid.GetName()
  4438:         if re.search('^.*-iclone-[0-9][0-9]*$', vm_name):
  4439              iclone_vms.append(moid)

  4853          prefix = last_esx['vmname']
  4854:         m = re.search('^(.*)\.([0-9][0-9]*)$', last_esx['vmname'])
  4855          if m:

  4862          esx_cfg['vmname'] = prefix.replace(
  4863:             re.search(r'esx.\d+', prefix).group(), 'esx.{}'.format(count))
  4864          try:

  4883                  for line in lines:
  4884:                     m = re.search('^testbed-node-name: (.*)$', line)
  4885                      if m:
  4886                          name = m.group(1).strip()
  4887:                         m = re.search('^([^0-9]*)([0-9][0-9]*)$', name)
  4888                          if m:

lanier-goat-development\clonevm\clonevm-synctimewithhost.py:
  24      for f in os.listdir(eggdir):
  25:         if re.search('.*\.egg', f):
  26              sys.path.append(os.path.join(eggdir, f))

  28      for f in os.listdir(centosdir):
  29:         if re.search('.*\.egg', f):
  30              sys.path.append(os.path.join(centosdir, f))

lanier-goat-development\codraas\demos\tests\e2edemo.py:
  341      thname = threading.currentThread().name
  342:     match = re.search(r'/Tenants/Tenant-(\d+)', thname)
  343      if match:

lanier-goat-development\codraas\lib\multitenant.py:
  136          test['testbedspec'] = None
  137:         if re.search(test_selection, test['id']):
  138              selected_tests.append(test)

lanier-goat-development\ddmbt\ddtlib.py:
  1314                  if 'testid' in test:
  1315:                     if re.search(pattern, test['testid']):
  1316                          if parameter in test:

lanier-goat-development\ddmbt\loganalyzer.py:
   42      mbtEventPattern = r'^\*\*MBT Event (\S+)  '
   43:     match = re.search(mbtFnPattern, text)
   44      if match:

   47      else:
   48:         match = re.search(mbtEventPattern, text)
   49          if match:

  239              for skipPattern in skipPatterns:
  240:                 match = re.search(skipPattern, line)
  241                  if match:

  246              for filter in filters:
  247:                 match = re.search(filter, line)
  248                  if not match:

  254                  # We want to capture exceptions
  255:                 match = re.search(exceptionPattern, line)
  256                  if match:

  277                      for th in threads:
  278:                         match = re.search(th, threadName)
  279                          if match:

  295                  # Identify threads with MBT operations
  296:                 matchmbt = re.search(mbtOpEventPattern, msg)
  297                  if matchmbt:

  448                  if mbtTestcase:
  449:                     match = re.search(patternStart, line)
  450                      if match and ignoreStart:
  451                          continue
  452:                     match = re.search(patternEnd, line)
  453                      if match and ignoreEnd:
  454                          continue
  455:                     match = re.search(patternNodeStart, line)
  456                      if match:

  458                          continue
  459:                     match = re.search(patternNodeEnd, line)
  460                      if match:

  465                      continue
  466:                 match = re.search(pattern1, line)
  467                  if match:

lanier-goat-development\ddmbt\mbtlib.py:
   152          lastLine = re.sub(r'#\d+"', '"', lastLine)
   153:         start = re.search(nodePattern, firstLine)
   154          if start:

   160              self.MBTDual = True
   161:         end = re.search(nodePattern, lastLine)
   162          if end:

  1044          # Node%%%%: 1 "Start(0)End(1)#1"
  1045:         # if re.search(composePattern,line):
  1046          #   continue

  1048          isNode = True
  1049:         node = re.search(nodePattern, line)
  1050          if node:

  1245          nodePattern = r'^(.+)\((\d+)\)$'
  1246:         node = re.search(nodePattern, name)
  1247          if node:

  1252          edgePattern = r'^(.+)\((\d+)\)$'
  1253:         edge = re.search(edgePattern, name)
  1254          if edge:

  1276      for line in lines:
  1277:         if re.search(startNodePattern, line):
  1278              newLines.append(line)

  1280              continue
  1281:         if re.search(endNodePattern, line):
  1282              newLines.append(line)

  1289          # Node%%%%: 1 "Start(0)End(1)#1"
  1290:         if re.search(composePattern, line):
  1291              continue

lanier-goat-development\ddmbt\testthreads.py:
  372      pattern = r'/ddmbtfn_.*_(\d+)$'
  373:     match = re.search(pattern, thName)
  374      if match:

  384      thName = threading.currentThread().name
  385:     match = re.search(r'/ddmbtThread_(\d+)', thName)
  386      if match:

lanier-goat-development\dependency\distro.py:
   987              # If there is no version_codename, parse it from the version
   988:             codename = re.search(r'(\(\D+\))|,(\s+)?\D+', props['version'])
   989              if codename:

  1055          props = {}
  1056:         match = re.search(r'^([^\s]+)\s+([\d\.]+)', lines[0].strip())
  1057          if match:

lanier-goat-development\dependency\racetrack.py:
  113              result = self._post('TestSetBegin.php', data)
  114:         if 'racetrack' in self.server and not re.search(r'\d+', result.text):
  115              raise AssertionError('Unable to get test set id')
  116          self.test_set_id = result.text
  117:         if re.search('Error|html', self.test_set_id, re.I):
  118              if self.logger:

  232              result = self._post('TestCaseBegin.php', data, 10)
  233:         if 'racetrack' in self.server and not re.search(r'\d+', result.text):
  234              raise AssertionError('Unable to get test case id')
  235          self.test_case_id = result.text
  236:         if re.search('Error|html', self.test_case_id, re.I):
  237              if self.logger:

  474      print(https)
  475:     if re.search('True|yes|1', https, re.I):
  476          https = True

lanier-goat-development\dependency\centos\distro.py:
   987              # If there is no version_codename, parse it from the version
   988:             codename = re.search(r'(\(\D+\))|,(\s+)?\D+', props['version'])
   989              if codename:

  1055          props = {}
  1056:         match = re.search(r'^([^\s]+)\s+([\d\.]+)', lines[0].strip())
  1057          if match:

lanier-goat-development\dependency\centos\tabulate.py:
   618      if isinstance(s, _text_type):
   619:         return bool(re.search(_multiline_codes, s))
   620      else:  # a bytestring
   621:         return bool(re.search(_multiline_codes_bytes, s))
   622  

  1273  
  1274:     has_invisible = re.search(_invisible_codes, plain_text)
  1275      enable_widechars = wcwidth is not None and WIDE_CHARS_MODE

lanier-goat-development\dependency\centos\_pytest\pastebin.py:
  70      response = urlopen(url, data=urlencode(params).encode("ascii")).read()
  71:     m = re.search(r'href="/raw/(\w+)"', response.decode("utf-8"))
  72      if m:

lanier-goat-development\dependency\centos\_pytest\_code\code.py:
  602          __tracebackhide__ = True
  603:         if not re.search(regexp, str(self.value)):
  604              assert 0, "Pattern {!r} not found in {!r}".format(regexp, str(self.value))

lanier-goat-development\dependency\centos\asn1crypto\_iri.py:
  209      escapes = []
  210:     if re.search('%[0-9a-fA-F]{2}', string):
  211          # Try to unquote any percent values, restoring them if they are not

lanier-goat-development\dependency\centos\asn1crypto\core.py:
  4587              string = str_cls(self)
  4588:             has_timezone = re.search('[-\\+]', string)
  4589  

lanier-goat-development\dependency\centos\backports\configparser\__init__.py:
  1088              # continuation line?
  1089:             first_nonspace = self.NONSPACECRE.search(line)
  1090              cur_indent_level = first_nonspace.start() if first_nonspace else 0

lanier-goat-development\dependency\centos\boto3\resources\params.py:
  127          # Is it indexing an array?
  128:         result = INDEX_RE.search(part)
  129          if result:

lanier-goat-development\dependency\centos\bs4\dammit.py:
  322          declared_encoding = None
  323:         declared_encoding_match = xml_encoding_re.search(markup, endpos=xml_endpos)
  324          if not declared_encoding_match and is_html:
  325:             declared_encoding_match = html_meta_re.search(markup, endpos=html_endpos)
  326          if declared_encoding_match is not None:

lanier-goat-development\dependency\centos\bs4\element.py:
  91      def __new__(cls, original_value):
  92:         match = cls.CHARSET_RE.search(original_value)
  93          if match is None:

lanier-goat-development\dependency\centos\click\_compat.py:
  220      def isidentifier(x):
  221:         return _identifier_re.search(x) is not None
  222  

lanier-goat-development\dependency\centos\coverage\control.py:
  487          # C code with a C file name.
  488:         if re.search(r"[/\\]Modules[/\\]pyexpat.c", filename):
  489              return nope(disp, "pyexpat lies about itself")

lanier-goat-development\dependency\centos\coverage\files.py:
  279      """Find the path separator used in this string, or os.sep if none."""
  280:     sep_match = re.search(r"[\\/]", s)
  281      if sep_match:

lanier-goat-development\dependency\centos\coverage\phystokens.py:
  292      """Return `source`, with any encoding declaration neutered."""
  293:     if COOKIE_RE.search(source):
  294          source_lines = source.splitlines(True)

lanier-goat-development\dependency\centos\docutils\statemachine.py:
    12  - `StateWS`, a state superclass for use with `StateMachineWS`
    13: - `SearchStateMachine`, uses `re.search()` instead of `re.match()`
    14: - `SearchStateMachineWS`, uses `re.search()` instead of `re.match()`
    15  - `ViewList`, extends standard Python lists.

  1043      (succeeds only if the pattern matches at the start of `self.line`) to
  1044:     `re.search()` (succeeds if the pattern matches anywhere in `self.line`).
  1045      When subclassing a `StateMachine`, list this class **first** in the

  1060  class SearchStateMachine(_SearchOverride, StateMachine):
  1061:     """`StateMachine` which uses `re.search()` instead of `re.match()`."""
  1062      pass

  1065  class SearchStateMachineWS(_SearchOverride, StateMachineWS):
  1066:     """`StateMachineWS` which uses `re.search()` instead of `re.match()`."""
  1067      pass

lanier-goat-development\dependency\centos\docutils\parsers\rst\states.py:
  406          data = '\n'.join(lines).rstrip()
  407:         if re.search(r'(?<!\\)(\\\\)*::$', data):
  408              if len(data) == 2:

lanier-goat-development\dependency\centos\future\backports\email\generator.py:
  371              cre = cls._compile_re('^--' + re.escape(b) + '(--)?$', re.MULTILINE)
  372:             if not cre.search(text):
  373                  break

lanier-goat-development\dependency\centos\future\backports\email\header.py:
  80      # If no encoding, just return the header with no charset.
  81:     if not ecre.search(header):
  82          return [(header, None)]

lanier-goat-development\dependency\centos\future\backports\email\utils.py:
  105              quotes = ''
  106:             if specialsre.search(name):
  107                  quotes = '"'

lanier-goat-development\dependency\centos\future\backports\http\cookiejar.py:
   146      else:
   147:         m = TIMEZONE_RE.search(tz)
   148          if m:

   260      # fast exit for strictly conforming string
   261:     m = STRICT_DATE_RE.search(text)
   262      if m:

   278      # loose regexp parse
   279:     m = LOOSE_HTTP_DATE_RE.search(text)
   280      if m is not None:

   321      # loose regexp parse
   322:     m = ISO_DATE_RE.search(text)
   323      if m is not None:

   395          while text:
   396:             m = HEADER_TOKEN_RE.search(text)
   397              if m:

   399                  name = m.group(1)
   400:                 m = HEADER_QUOTED_VALUE_RE.search(text)
   401                  if m:  # quoted value

   405                  else:
   406:                     m = HEADER_VALUE_RE.search(text)
   407                      if m:  # unquoted value

   447              if v is not None:
   448:                 if not re.search(r"^\w+$", v):
   449                      v = HEADER_JOIN_ESCAPE_RE.sub(r"\\\1", v)  # escape " and \

   522      #  at other uses of IPV4_RE also, if change this.
   523:     if IPV4_RE.search(text):
   524          return False

   575      """
   576:     if IPV4_RE.search(text):
   577          return False

   623      erhn = req_host = request_host(request)
   624:     if req_host.find(".") == -1 and not IPV4_RE.search(req_host):
   625          erhn = req_host + ".local"

  1052                  if (host_prefix.find(".") >= 0 and
  1053:                     not IPV4_RE.search(req_host)):
  1054                      _debug("   host prefix %s for domain %s contains a dot",

  1305              if ((cookie.value is not None) and
  1306:                 self.non_word_re.search(cookie.value) and version > 0):
  1307                  value = self.quote_re.sub(r"\\\1", cookie.value)

  1889          magic = f.readline()
  1890:         if not self.magic_re.search(magic):
  1891              msg = ("%r does not look like a Set-Cookie3 (LWP) format "

  2010          magic = f.readline()
  2011:         if not self.magic_re.search(magic):
  2012              f.close()

lanier-goat-development\dependency\centos\importlib_metadata\__init__.py:
  384          manifest = template.format(pattern=normalized)
  385:         return re.search(manifest, str(item), flags=re.IGNORECASE)
  386  

lanier-goat-development\dependency\centos\isort\isort.py:
  369                  exp = r"\b" + re.escape(splitter) + r"\b"
  370:                 if re.search(exp, line_without_comment) and not line_without_comment.strip().startswith(splitter):
  371                      line_parts = re.split(exp, line_without_comment)

lanier-goat-development\dependency\centos\isort\settings.py:
  335              check_exclude = '/' + os.path.basename(path) + check_exclude
  336:         if safety_exclude_re.search(check_exclude):
  337              return True

lanier-goat-development\dependency\centos\jenkins\__init__.py:
   496          for job in jobs:
   497:             if re.search(pattern, job['name']):
   498                  result.append(self.get_job_info(job['name'], depth=depth))

  1467                      url = executable['url']
  1468:                     m = re.search(r'/job/([^/]+)/.*', urlparse(url).path)
  1469                      job_name = m.group(1)

lanier-goat-development\dependency\centos\jenkinsapi_tests\systests\test_jenkins_matrix.py:
  24          assert run.get_upstream_build() == build
  25:         match_result = re.search(u'\xbb (.*) #\\d+$', run.name)
  26          assert match_result is not None

lanier-goat-development\dependency\centos\lxml\doctestcompare.py:
  129          return (s.startswith('<')
  130:                 and not _repr_re.search(s))
  131  

  168          want = want.replace(r'\.\.\.', '.*')
  169:         if re.search(want, got):
  170              return True

lanier-goat-development\dependency\centos\lxml\html\__init__.py:
  157          """
  158:         if not value or re.search(r'\s', value):
  159              raise ValueError("Invalid class name: %r" % value)

  171          """
  172:         if not value or re.search(r'\s', value):
  173              raise ValueError("Invalid class name: %r" % value)

  186          """
  187:         if not value or re.search(r'\s', value):
  188              raise ValueError("Invalid class name: %r" % value)

  222          """
  223:         if not value or re.search(r'\s', value):
  224              raise ValueError("Invalid class name: %r" % value)

lanier-goat-development\dependency\centos\lxml\html\_diffcommand.py:
  74      pre = post = ''
  75:     match = body_start_re.search(html)
  76      if match:

  78          html = html[match.end():]
  79:     match = body_end_re.search(html)
  80      if match:

lanier-goat-development\dependency\centos\lxml\html\diff.py:
  564      Also <ins> and <del> tags are removed.  """
  565:     match = _body_re.search(html)
  566      if match:
  567          html = html[match.end():]
  568:     match = _end_body_re.search(html)
  569      if match:

  735      trailing whitespace when appropriate.  """
  736:     if el.tail and start_whitespace_re.search(el.tail):
  737          extra = ' '

lanier-goat-development\dependency\centos\markdown\blockprocessors.py:
  281      def test(self, parent, block):
  282:         return bool(self.RE.search(block))
  283  

  285          block = blocks.pop(0)
  286:         m = self.RE.search(block)
  287          if m:

  450      def test(self, parent, block):
  451:         return bool(self.RE.search(block))
  452  

  454          block = blocks.pop(0)
  455:         m = self.RE.search(block)
  456          if m:

  505      def test(self, parent, block):
  506:         m = self.SEARCH_RE.search(block)
  507          # No atomic grouping in python so we simulate it here for performance.

lanier-goat-development\dependency\centos\markdown\treeprocessors.py:
  103          """
  104:         m = self.__placeholder_re.search(data, index)
  105          if m:

lanier-goat-development\dependency\centos\markdown\extensions\admonition.py:
  46          sibling = self.lastChild(parent)
  47:         return self.RE.search(block) or \
  48              (block.startswith(' ' * self.tab_length) and sibling is not None and

  53          block = blocks.pop(0)
  54:         m = self.RE.search(block)
  55  

lanier-goat-development\dependency\centos\markdown\extensions\attr_list.py:
   96                          # use tail of last child. no ul or ol.
   97:                         m = RE.search(elem[-1].tail)
   98                          if m:

  102                          # use tail of last child before ul or ol
  103:                         m = RE.search(elem[pos-1].tail)
  104                          if m:

  108                          # use text. ul is first child.
  109:                         m = RE.search(elem.text)
  110                          if m:

  114                      # has children. Get from tail of last child
  115:                     m = RE.search(elem[-1].tail)
  116                      if m:

  123                      # no children. Get from text.
  124:                     m = RE.search(elem.text)
  125                      if not m and elem.tag == 'td':
  126:                         m = re.search(self.BASE_RE, elem.text)
  127                      if m:

lanier-goat-development\dependency\centos\markdown\extensions\def_list.py:
  32      def test(self, parent, block):
  33:         return bool(self.RE.search(block))
  34  

  37          raw_block = blocks.pop(0)
  38:         m = self.RE.search(raw_block)
  39          terms = [l.strip() for l in

lanier-goat-development\dependency\centos\markdown\extensions\fenced_code.py:
  66          while 1:
  67:             m = self.FENCED_BLOCK_RE.search(text)
  68              if m:

lanier-goat-development\dependency\centos\Naked\templates\setup_py_file.py:
  18      'patch_regex = ' + '"""' + """patch_version\s*?=\s*?["']{1}(\d+)["']{1}""" + '"""' + '\n    ' +
  19:     """major_match = re.search(major_regex, settings_file)
  20:     minor_match = re.search(minor_regex, settings_file)
  21:     patch_match = re.search(patch_regex, settings_file)
  22      major_version = major_match.group(1)

lanier-goat-development\dependency\centos\pbr\git.py:
  318          authors += _run_git_command(git_log_cmd, git_dir).split('\n')
  319:         authors = [a for a in authors if not re.search(ignore_emails, a)]
  320  

lanier-goat-development\dependency\centos\pbr\tests\test_wsgi.py:
  100          print(stdoutdata)
  101:         m = re.search(br'(http://[^:]+:\d+)/', stdoutdata)
  102          self.assertIsNotNone(m, "Regex failed to match on %s" % stdoutdata)

lanier-goat-development\dependency\centos\psutil\_psaix.py:
  253          if p.returncode == 0:
  254:             re_result = re.search(
  255                  r"Running: (\d+) Mbps.*?(\w+) Duplex", stdout)

lanier-goat-development\dependency\centos\psutil\_pslinux.py:
  726              glob.glob("/sys/devices/system/cpu/cpu[0-9]*/cpufreq")
  727:         paths.sort(key=lambda x: int(re.search(r"[0-9]+", x).group()))
  728          ret = []

lanier-goat-development\dependency\centos\psutil\tests\__init__.py:
  628      else:
  629:         r = re.search(r"\s\d$", wv[4])
  630          if r:

lanier-goat-development\dependency\centos\psutil\tests\test_aix.py:
   27              re_pattern += r"(?P<%s>\S+)\s+" % (field,)
   28:         matchobj = re.search(re_pattern, out)
   29  

   58          # are not guaranteed to be "MB" so parsing may not be consistent
   59:         matchobj = re.search(r"(?P<space>\S+)\s+"
   60                               r"(?P<vol>\S+)\s+"

   81              re_pattern += r"(?P<%s>\S+)\s+" % (field,)
   82:         matchobj = re.search(re_pattern, out)
   83  

  108          out = sh('/usr/bin/mpstat -a')
  109:         mpstat_lcpu = int(re.search(r"lcpu=(\d+)", out).group(1))
  110          psutil_lcpu = psutil.cpu_count(logical=True)

lanier-goat-development\dependency\centos\psutil\tests\test_linux.py:
  681          ls = os.listdir("/sys/devices/system/cpu")
  682:         count = len([x for x in ls if re.search(r"cpu\d+$", x) is not None])
  683          self.assertEqual(psutil.cpu_count(), count)

  967      #         line = line.strip()
  968:     #         if re.search(r"^\d+:", line):
  969      #             found += 1

lanier-goat-development\dependency\centos\psutil\tests\test_osx.py:
   49          raise ValueError("line not found")
   50:     return int(re.search(r'\d+', line).group(0)) * getpagesize()
   51  

  227          out = sh("pmset -g batt")
  228:         percent = re.search(r"(\d+)%", out).group(1)
  229:         drawing_from = re.search("Now drawing from '([^']+)'", out).group(1)
  230          power_plugged = drawing_from == "AC Power"

lanier-goat-development\dependency\centos\pylint\checkers\spelling.py:
  330  
  331:                 m = re.search(r"(\W|^)(%s)(\W|$)" % word, line)
  332                  if m:

lanier-goat-development\dependency\centos\pylint\extensions\_check_docs_utils.py:
  673      def _parse_section(self, section_re):
  674:         section_match = section_re.search(self.doc)
  675          if section_match is None:

lanier-goat-development\dependency\centos\pylint\test\test_functional.py:
  184      for i, line in enumerate(stream):
  185:         match = _EXPECTED_RE.search(line)
  186          if match is None:

lanier-goat-development\dependency\centos\pylint\test\test_self.py:
  184          # configuration file is not found.
  185:         master = re.search(r"\[MASTER", output)
  186          out = StringIO(output[master.start() :])

lanier-goat-development\dependency\centos\pylint\test\unittest_lint.py:
  600          regexp = re.compile(re_str, re.MULTILINE)
  601:         assert re.search(regexp, output)
  602  

lanier-goat-development\dependency\centos\selenium\webdriver\firefox\firefox_profile.py:
  236                  for usr in f:
  237:                     matches = re.search(PREF_RE, usr)
  238                      try:

lanier-goat-development\dependency\centos\selenium\webdriver\support\expected_conditions.py:
  88          import re
  89:         match = re.search(self.pattern, driver.current_url)
  90  

lanier-goat-development\dependency\centos\setuptools\package_index.py:
  831                  # Check for a subversion index page
  832:                 if re.search(r'<title>([^- ]+ - )?Revision \d+:', line):
  833                      # it's a subversion index page:

lanier-goat-development\dependency\centos\setuptools\_distutils\filelist.py:
  217          for name in self.allfiles:
  218:             if pattern_re.search(name):
  219                  self.debug_print(" adding " + name)

  236          for i in range(len(self.files)-1, -1, -1):
  237:             if pattern_re.search(self.files[i]):
  238                  self.debug_print(" removing " + self.files[i])

lanier-goat-development\dependency\centos\setuptools\_distutils\msvc9compiler.py:
  722                  r""".*?(?:/>|</assemblyIdentity>)""", re.DOTALL)
  723:             if re.search(pattern, manifest_buf) is None:
  724                  return None

lanier-goat-development\dependency\centos\setuptools\_distutils\unixccompiler.py:
  287              cflags = sysconfig.get_config_var('CFLAGS')
  288:             m = re.search(r'-isysroot\s*(\S+)', cflags)
  289              if m is None:

lanier-goat-development\dependency\centos\setuptools\command\easy_install.py:
  2127          """
  2128:         has_path_sep = re.search(r'[\\/]', name)
  2129          if has_path_sep:

lanier-goat-development\dependency\centos\urllib3\connection.py:
  211          # is broken but we don't want this method in our documentation.
  212:         match = _CONTAINS_CONTROL_CHAR_RE.search(method)
  213          if match:

lanier-goat-development\dependency\centos\urllib3\util\url.py:
  281              if is_ipv6:
  282:                 match = ZONE_ID_RE.search(host)
  283                  if match:

  356      source_url = url
  357:     if not SCHEME_RE.search(url):
  358          url = "//" + url

lanier-goat-development\dependency\centos\werkzeug\_internal.py:
  301      while 0 <= i < n:
  302:         o_match = _octal_re.search(b, i)
  303:         q_match = _quote_re.search(b, i)
  304          if not o_match and not q_match:

  329      while i < n:
  330:         match = _cookie_re.search(b + b";", i)
  331          if not match:

lanier-goat-development\dependency\centos\werkzeug\useragents.py:
  96              browser = version = None
  97:         match = self._language_re.search(user_agent)
  98          if match is not None:

lanier-goat-development\dependency\centos\werkzeug\debug\__init__.py:
  102              ).communicate()[0]
  103:             match = re.search(b'"serial-number" = <([^>]+)', dump)
  104              if match is not None:

lanier-goat-development\dependency\centos\werkzeug\debug\tbtools.py:
  594              for idx, match in enumerate(_line_re.finditer(source)):
  595:                 match = _coding_re.search(match.group())
  596                  if match is not None:

lanier-goat-development\dependency\photon\distro.py:
   987              # If there is no version_codename, parse it from the version
   988:             codename = re.search(r'(\(\D+\))|,(\s+)?\D+', props['version'])
   989              if codename:

  1055          props = {}
  1056:         match = re.search(r'^([^\s]+)\s+([\d\.]+)', lines[0].strip())
  1057          if match:

lanier-goat-development\dependency\photon\tabulate.py:
   618      if isinstance(s, _text_type):
   619:         return bool(re.search(_multiline_codes, s))
   620      else:  # a bytestring
   621:         return bool(re.search(_multiline_codes_bytes, s))
   622  

  1273  
  1274:     has_invisible = re.search(_invisible_codes, plain_text)
  1275      enable_widechars = wcwidth is not None and WIDE_CHARS_MODE

lanier-goat-development\dependency\photon\_pytest\pastebin.py:
  70      response = urlopen(url, data=urlencode(params).encode("ascii")).read()
  71:     m = re.search(r'href="/raw/(\w+)"', response.decode("utf-8"))
  72      if m:

lanier-goat-development\dependency\photon\_pytest\_code\code.py:
  602          __tracebackhide__ = True
  603:         if not re.search(regexp, str(self.value)):
  604              assert 0, "Pattern {!r} not found in {!r}".format(regexp, str(self.value))

lanier-goat-development\dependency\photon\asn1crypto\_iri.py:
  209      escapes = []
  210:     if re.search('%[0-9a-fA-F]{2}', string):
  211          # Try to unquote any percent values, restoring them if they are not

lanier-goat-development\dependency\photon\asn1crypto\core.py:
  4587              string = str_cls(self)
  4588:             has_timezone = re.search('[-\\+]', string)
  4589  

lanier-goat-development\dependency\photon\backports\configparser\__init__.py:
  1088              # continuation line?
  1089:             first_nonspace = self.NONSPACECRE.search(line)
  1090              cur_indent_level = first_nonspace.start() if first_nonspace else 0

lanier-goat-development\dependency\photon\boto3\resources\params.py:
  127          # Is it indexing an array?
  128:         result = INDEX_RE.search(part)
  129          if result:

lanier-goat-development\dependency\photon\bs4\dammit.py:
  322          declared_encoding = None
  323:         declared_encoding_match = xml_encoding_re.search(markup, endpos=xml_endpos)
  324          if not declared_encoding_match and is_html:
  325:             declared_encoding_match = html_meta_re.search(markup, endpos=html_endpos)
  326          if declared_encoding_match is not None:

lanier-goat-development\dependency\photon\bs4\element.py:
  91      def __new__(cls, original_value):
  92:         match = cls.CHARSET_RE.search(original_value)
  93          if match is None:

lanier-goat-development\dependency\photon\click\_compat.py:
  220      def isidentifier(x):
  221:         return _identifier_re.search(x) is not None
  222  

lanier-goat-development\dependency\photon\coverage\control.py:
  487          # C code with a C file name.
  488:         if re.search(r"[/\\]Modules[/\\]pyexpat.c", filename):
  489              return nope(disp, "pyexpat lies about itself")

lanier-goat-development\dependency\photon\coverage\files.py:
  279      """Find the path separator used in this string, or os.sep if none."""
  280:     sep_match = re.search(r"[\\/]", s)
  281      if sep_match:

lanier-goat-development\dependency\photon\coverage\phystokens.py:
  292      """Return `source`, with any encoding declaration neutered."""
  293:     if COOKIE_RE.search(source):
  294          source_lines = source.splitlines(True)

lanier-goat-development\dependency\photon\docutils\statemachine.py:
    12  - `StateWS`, a state superclass for use with `StateMachineWS`
    13: - `SearchStateMachine`, uses `re.search()` instead of `re.match()`
    14: - `SearchStateMachineWS`, uses `re.search()` instead of `re.match()`
    15  - `ViewList`, extends standard Python lists.

  1043      (succeeds only if the pattern matches at the start of `self.line`) to
  1044:     `re.search()` (succeeds if the pattern matches anywhere in `self.line`).
  1045      When subclassing a `StateMachine`, list this class **first** in the

  1060  class SearchStateMachine(_SearchOverride, StateMachine):
  1061:     """`StateMachine` which uses `re.search()` instead of `re.match()`."""
  1062      pass

  1065  class SearchStateMachineWS(_SearchOverride, StateMachineWS):
  1066:     """`StateMachineWS` which uses `re.search()` instead of `re.match()`."""
  1067      pass

lanier-goat-development\dependency\photon\docutils\parsers\rst\states.py:
  406          data = '\n'.join(lines).rstrip()
  407:         if re.search(r'(?<!\\)(\\\\)*::$', data):
  408              if len(data) == 2:

lanier-goat-development\dependency\photon\future\backports\email\generator.py:
  371              cre = cls._compile_re('^--' + re.escape(b) + '(--)?$', re.MULTILINE)
  372:             if not cre.search(text):
  373                  break

lanier-goat-development\dependency\photon\future\backports\email\header.py:
  80      # If no encoding, just return the header with no charset.
  81:     if not ecre.search(header):
  82          return [(header, None)]

lanier-goat-development\dependency\photon\future\backports\email\utils.py:
  105              quotes = ''
  106:             if specialsre.search(name):
  107                  quotes = '"'

lanier-goat-development\dependency\photon\future\backports\http\cookiejar.py:
   146      else:
   147:         m = TIMEZONE_RE.search(tz)
   148          if m:

   260      # fast exit for strictly conforming string
   261:     m = STRICT_DATE_RE.search(text)
   262      if m:

   278      # loose regexp parse
   279:     m = LOOSE_HTTP_DATE_RE.search(text)
   280      if m is not None:

   321      # loose regexp parse
   322:     m = ISO_DATE_RE.search(text)
   323      if m is not None:

   395          while text:
   396:             m = HEADER_TOKEN_RE.search(text)
   397              if m:

   399                  name = m.group(1)
   400:                 m = HEADER_QUOTED_VALUE_RE.search(text)
   401                  if m:  # quoted value

   405                  else:
   406:                     m = HEADER_VALUE_RE.search(text)
   407                      if m:  # unquoted value

   447              if v is not None:
   448:                 if not re.search(r"^\w+$", v):
   449                      v = HEADER_JOIN_ESCAPE_RE.sub(r"\\\1", v)  # escape " and \

   522      #  at other uses of IPV4_RE also, if change this.
   523:     if IPV4_RE.search(text):
   524          return False

   575      """
   576:     if IPV4_RE.search(text):
   577          return False

   623      erhn = req_host = request_host(request)
   624:     if req_host.find(".") == -1 and not IPV4_RE.search(req_host):
   625          erhn = req_host + ".local"

  1052                  if (host_prefix.find(".") >= 0 and
  1053:                     not IPV4_RE.search(req_host)):
  1054                      _debug("   host prefix %s for domain %s contains a dot",

  1305              if ((cookie.value is not None) and
  1306:                 self.non_word_re.search(cookie.value) and version > 0):
  1307                  value = self.quote_re.sub(r"\\\1", cookie.value)

  1889          magic = f.readline()
  1890:         if not self.magic_re.search(magic):
  1891              msg = ("%r does not look like a Set-Cookie3 (LWP) format "

  2010          magic = f.readline()
  2011:         if not self.magic_re.search(magic):
  2012              f.close()

lanier-goat-development\dependency\photon\importlib_metadata\__init__.py:
  384          manifest = template.format(pattern=normalized)
  385:         return re.search(manifest, str(item), flags=re.IGNORECASE)
  386  

lanier-goat-development\dependency\photon\isort\isort.py:
  369                  exp = r"\b" + re.escape(splitter) + r"\b"
  370:                 if re.search(exp, line_without_comment) and not line_without_comment.strip().startswith(splitter):
  371                      line_parts = re.split(exp, line_without_comment)

lanier-goat-development\dependency\photon\isort\settings.py:
  335              check_exclude = '/' + os.path.basename(path) + check_exclude
  336:         if safety_exclude_re.search(check_exclude):
  337              return True

lanier-goat-development\dependency\photon\jenkinsapi_tests\systests\test_jenkins_matrix.py:
  24          assert run.get_upstream_build() == build
  25:         match_result = re.search(u'\xbb (.*) #\\d+$', run.name)
  26          assert match_result is not None

lanier-goat-development\dependency\photon\lxml\doctestcompare.py:
  129          return (s.startswith('<')
  130:                 and not _repr_re.search(s))
  131  

  168          want = want.replace(r'\.\.\.', '.*')
  169:         if re.search(want, got):
  170              return True

lanier-goat-development\dependency\photon\lxml\html\__init__.py:
  157          """
  158:         if not value or re.search(r'\s', value):
  159              raise ValueError("Invalid class name: %r" % value)

  171          """
  172:         if not value or re.search(r'\s', value):
  173              raise ValueError("Invalid class name: %r" % value)

  186          """
  187:         if not value or re.search(r'\s', value):
  188              raise ValueError("Invalid class name: %r" % value)

  222          """
  223:         if not value or re.search(r'\s', value):
  224              raise ValueError("Invalid class name: %r" % value)

lanier-goat-development\dependency\photon\lxml\html\_diffcommand.py:
  74      pre = post = ''
  75:     match = body_start_re.search(html)
  76      if match:

  78          html = html[match.end():]
  79:     match = body_end_re.search(html)
  80      if match:

lanier-goat-development\dependency\photon\lxml\html\diff.py:
  564      Also <ins> and <del> tags are removed.  """
  565:     match = _body_re.search(html)
  566      if match:
  567          html = html[match.end():]
  568:     match = _end_body_re.search(html)
  569      if match:

  735      trailing whitespace when appropriate.  """
  736:     if el.tail and start_whitespace_re.search(el.tail):
  737          extra = ' '

lanier-goat-development\dependency\photon\markdown\blockprocessors.py:
  281      def test(self, parent, block):
  282:         return bool(self.RE.search(block))
  283  

  285          block = blocks.pop(0)
  286:         m = self.RE.search(block)
  287          if m:

  450      def test(self, parent, block):
  451:         return bool(self.RE.search(block))
  452  

  454          block = blocks.pop(0)
  455:         m = self.RE.search(block)
  456          if m:

  505      def test(self, parent, block):
  506:         m = self.SEARCH_RE.search(block)
  507          # No atomic grouping in python so we simulate it here for performance.

lanier-goat-development\dependency\photon\markdown\treeprocessors.py:
  103          """
  104:         m = self.__placeholder_re.search(data, index)
  105          if m:

lanier-goat-development\dependency\photon\markdown\extensions\admonition.py:
  46          sibling = self.lastChild(parent)
  47:         return self.RE.search(block) or \
  48              (block.startswith(' ' * self.tab_length) and sibling is not None and

  53          block = blocks.pop(0)
  54:         m = self.RE.search(block)
  55  

lanier-goat-development\dependency\photon\markdown\extensions\attr_list.py:
   96                          # use tail of last child. no ul or ol.
   97:                         m = RE.search(elem[-1].tail)
   98                          if m:

  102                          # use tail of last child before ul or ol
  103:                         m = RE.search(elem[pos-1].tail)
  104                          if m:

  108                          # use text. ul is first child.
  109:                         m = RE.search(elem.text)
  110                          if m:

  114                      # has children. Get from tail of last child
  115:                     m = RE.search(elem[-1].tail)
  116                      if m:

  123                      # no children. Get from text.
  124:                     m = RE.search(elem.text)
  125                      if not m and elem.tag == 'td':
  126:                         m = re.search(self.BASE_RE, elem.text)
  127                      if m:

lanier-goat-development\dependency\photon\markdown\extensions\def_list.py:
  32      def test(self, parent, block):
  33:         return bool(self.RE.search(block))
  34  

  37          raw_block = blocks.pop(0)
  38:         m = self.RE.search(raw_block)
  39          terms = [l.strip() for l in

lanier-goat-development\dependency\photon\markdown\extensions\fenced_code.py:
  66          while 1:
  67:             m = self.FENCED_BLOCK_RE.search(text)
  68              if m:

lanier-goat-development\dependency\photon\Naked\templates\setup_py_file.py:
  18      'patch_regex = ' + '"""' + """patch_version\s*?=\s*?["']{1}(\d+)["']{1}""" + '"""' + '\n    ' +
  19:     """major_match = re.search(major_regex, settings_file)
  20:     minor_match = re.search(minor_regex, settings_file)
  21:     patch_match = re.search(patch_regex, settings_file)
  22      major_version = major_match.group(1)

lanier-goat-development\dependency\photon\psutil\_psaix.py:
  253          if p.returncode == 0:
  254:             re_result = re.search(
  255                  r"Running: (\d+) Mbps.*?(\w+) Duplex", stdout)

lanier-goat-development\dependency\photon\psutil\_pslinux.py:
  726              glob.glob("/sys/devices/system/cpu/cpu[0-9]*/cpufreq")
  727:         paths.sort(key=lambda x: int(re.search(r"[0-9]+", x).group()))
  728          ret = []

lanier-goat-development\dependency\photon\psutil\tests\__init__.py:
  628      else:
  629:         r = re.search(r"\s\d$", wv[4])
  630          if r:

lanier-goat-development\dependency\photon\psutil\tests\test_aix.py:
   27              re_pattern += r"(?P<%s>\S+)\s+" % (field,)
   28:         matchobj = re.search(re_pattern, out)
   29  

   58          # are not guaranteed to be "MB" so parsing may not be consistent
   59:         matchobj = re.search(r"(?P<space>\S+)\s+"
   60                               r"(?P<vol>\S+)\s+"

   81              re_pattern += r"(?P<%s>\S+)\s+" % (field,)
   82:         matchobj = re.search(re_pattern, out)
   83  

  108          out = sh('/usr/bin/mpstat -a')
  109:         mpstat_lcpu = int(re.search(r"lcpu=(\d+)", out).group(1))
  110          psutil_lcpu = psutil.cpu_count(logical=True)

lanier-goat-development\dependency\photon\psutil\tests\test_linux.py:
  681          ls = os.listdir("/sys/devices/system/cpu")
  682:         count = len([x for x in ls if re.search(r"cpu\d+$", x) is not None])
  683          self.assertEqual(psutil.cpu_count(), count)

  967      #         line = line.strip()
  968:     #         if re.search(r"^\d+:", line):
  969      #             found += 1

lanier-goat-development\dependency\photon\psutil\tests\test_osx.py:
   49          raise ValueError("line not found")
   50:     return int(re.search(r'\d+', line).group(0)) * getpagesize()
   51  

  227          out = sh("pmset -g batt")
  228:         percent = re.search(r"(\d+)%", out).group(1)
  229:         drawing_from = re.search("Now drawing from '([^']+)'", out).group(1)
  230          power_plugged = drawing_from == "AC Power"

lanier-goat-development\dependency\photon\pylint\checkers\spelling.py:
  330  
  331:                 m = re.search(r"(\W|^)(%s)(\W|$)" % word, line)
  332                  if m:

lanier-goat-development\dependency\photon\pylint\extensions\_check_docs_utils.py:
  673      def _parse_section(self, section_re):
  674:         section_match = section_re.search(self.doc)
  675          if section_match is None:

lanier-goat-development\dependency\photon\pylint\test\test_functional.py:
  184      for i, line in enumerate(stream):
  185:         match = _EXPECTED_RE.search(line)
  186          if match is None:

lanier-goat-development\dependency\photon\pylint\test\test_self.py:
  184          # configuration file is not found.
  185:         master = re.search(r"\[MASTER", output)
  186          out = StringIO(output[master.start() :])

lanier-goat-development\dependency\photon\pylint\test\unittest_lint.py:
  600          regexp = re.compile(re_str, re.MULTILINE)
  601:         assert re.search(regexp, output)
  602  

lanier-goat-development\dependency\photon\selenium\webdriver\firefox\firefox_profile.py:
  236                  for usr in f:
  237:                     matches = re.search(PREF_RE, usr)
  238                      try:

lanier-goat-development\dependency\photon\selenium\webdriver\support\expected_conditions.py:
  88          import re
  89:         match = re.search(self.pattern, driver.current_url)
  90  

lanier-goat-development\dependency\photon\setuptools\package_index.py:
  831                  # Check for a subversion index page
  832:                 if re.search(r'<title>([^- ]+ - )?Revision \d+:', line):
  833                      # it's a subversion index page:

lanier-goat-development\dependency\photon\setuptools\_distutils\filelist.py:
  217          for name in self.allfiles:
  218:             if pattern_re.search(name):
  219                  self.debug_print(" adding " + name)

  236          for i in range(len(self.files)-1, -1, -1):
  237:             if pattern_re.search(self.files[i]):
  238                  self.debug_print(" removing " + self.files[i])

lanier-goat-development\dependency\photon\setuptools\_distutils\msvc9compiler.py:
  722                  r""".*?(?:/>|</assemblyIdentity>)""", re.DOTALL)
  723:             if re.search(pattern, manifest_buf) is None:
  724                  return None

lanier-goat-development\dependency\photon\setuptools\_distutils\unixccompiler.py:
  287              cflags = sysconfig.get_config_var('CFLAGS')
  288:             m = re.search(r'-isysroot\s*(\S+)', cflags)
  289              if m is None:

lanier-goat-development\dependency\photon\setuptools\command\easy_install.py:
  2127          """
  2128:         has_path_sep = re.search(r'[\\/]', name)
  2129          if has_path_sep:

lanier-goat-development\dependency\photon\urllib3\connection.py:
  211          # is broken but we don't want this method in our documentation.
  212:         match = _CONTAINS_CONTROL_CHAR_RE.search(method)
  213          if match:

lanier-goat-development\dependency\photon\urllib3\util\url.py:
  281              if is_ipv6:
  282:                 match = ZONE_ID_RE.search(host)
  283                  if match:

  356      source_url = url
  357:     if not SCHEME_RE.search(url):
  358          url = "//" + url

lanier-goat-development\dependency\photon\werkzeug\_internal.py:
  301      while 0 <= i < n:
  302:         o_match = _octal_re.search(b, i)
  303:         q_match = _quote_re.search(b, i)
  304          if not o_match and not q_match:

  329      while i < n:
  330:         match = _cookie_re.search(b + b";", i)
  331          if not match:

lanier-goat-development\dependency\photon\werkzeug\useragents.py:
  96              browser = version = None
  97:         match = self._language_re.search(user_agent)
  98          if match is not None:

lanier-goat-development\dependency\photon\werkzeug\debug\__init__.py:
  102              ).communicate()[0]
  103:             match = re.search(b'"serial-number" = <([^>]+)', dump)
  104              if match is not None:

lanier-goat-development\dependency\photon\werkzeug\debug\tbtools.py:
  594              for idx, match in enumerate(_line_re.finditer(source)):
  595:                 match = _coding_re.search(match.group())
  596                  if match is not None:

lanier-goat-development\ecosys\nve\test\run_ee_test_all.py:
  36          re_str = re.compile(r'[1-9] failed')
  37:         match = re.search(re_str, out)
  38          if match:

lanier-goat-development\ecosys\nve\test\setup_ee_testbed.py:
  120          re_fail = re.compile(r'failed=1')
  121:         match = re.search(re_fail, out)
  122          if match:

lanier-goat-development\ecosys\veeam\test\veeam_backup_restore.py:
  207          if rt == 0:
  208:             running = re.search('Running', out)
  209              if not running:

lanier-goat-development\eust_lite\tests\vcqe_eust.py:
  34  
  35:     if is_pvt_run and re.search('Yes|True|1', is_pvt_run, re.I):
  36          vcqe_pvt_run = True

lanier-goat-development\failureanalyzer\failures\instantclone_failures.py:
  18          for rule in rules:
  19:             if re.search(rule['regex'], self.result['message']):
  20                  f_a = FalureAnalyzer(self.log_dir, rule)

lanier-goat-development\failureanalyzer\failures\launch_failures.py:
  18              for rule in rules:
  19:                 if (re.search(rule['regex'], self.result['output'])
  20:                         or re.search(rule['regex'], self.result['error'])):
  21                      f_a = FalureAnalyzer(self.log_dir, rule)

lanier-goat-development\failureanalyzer\failures\nimbus_failures.py:
  19          for rule in rules:
  20:             if re.search(rule['regex'], self.result['exception']):
  21                  f_a = FalureAnalyzer(self.log_dir, rule)

lanier-goat-development\fractal\common\fractal_utils.py:
  720              args.log.info('VM object: {}'.format(vmref))
  721:             search_obj = re.search(
  722                  vmname_regex, vmref.config.name, re.IGNORECASE)

lanier-goat-development\fractal\common\vm_ops.py:
  511                  if cdrom.deviceInfo and cdrom.deviceInfo.summary and \
  512:                         re.search(self.iso_filename, cdrom.deviceInfo.summary):
  513                      iso_mounted = True

lanier-goat-development\fractal\test\tpm\test_tpm_cases.py:
  313              args.rt.comment('Result : %s' % str(result))
  314:             path = re.search("\/v*.*? ", result[1][1]).group()
  315              args.rt.comment('Dump file Path: %s' % str(path))

  321              args.rt.comment('Result : %s' % str(result))
  322:             path = re.search("\/v*.*", result[1][0]).group()
  323              args.rt.comment('zdump path: %s' % str(path))

lanier-goat-development\framework\builds.py:
  84  
  85:     if re.search('true|yes|0', value, re.I) or re.search('true|yes|1', il6run, re.I):
  86          return

lanier-goat-development\framework\config.py:
  345              nimbus_location = extra_test_args.get('nimbus-location')
  346:             if nimbus_location and re.search('wdc', nimbus_location):
  347                  if opts.logDir and '/vcf/wdc/' in opts.logDir:

  541  
  542:         if not self.opts.username and not re.search('true|yes|1', il6run, re.I):
  543              # A username is required to run the Nimbus

  639          for test in self.all_tests:
  640:             if test.disabled and re.search('True|Yes|1', test.disabled, re.I):
  641                  continue

  758                  if filename.endswith('.py') and filename != '__init__.py' and \
  759:                         not re.search('^.#', filename):
  760                      test = Test(self.opts.testsDir + filename, regex)

  774                  if filename.endswith('.py') and filename != '__init__.py' and \
  775:                         not re.search('^.#', filename):
  776                      test = Test(os.path.join(path, filename), regex)

lanier-goat-development\framework\dependencysetup.py:
  249                      url = deliverable['_download_url']
  250:                     if not re.search(name, url, re.I):
  251                          continue

lanier-goat-development\framework\environment.py:
  80              if not stderr:
  81:                 if re.search('photon', stdout, re.I):
  82                      current_distro = 'photon'

  88          current_distro = 'photon'
  89:     if not re.search('centos|photon', current_distro, re.I):
  90          log.warning('Unsupported OS/Distribution: %s' % current_distro)

lanier-goat-development\framework\racetrack.py:
  241              value = self.opts.extra_test_args['use-racetrack']
  242:             if re.search('false|no', value, re.I):
  243                  msg = 'Do not use racetrack as requested'

  268                  user = environ_user
  269:             if not re.search('centos|root', environ_user, re.I):
  270                  user = environ_user

  288          if self.vcf_db:
  289:             if self.vcf_db.test_set_id and re.search(
  290                      'html', self.vcf_db.test_set_id, re.I):

  363                  environ_user = os.environ['USER']
  364:                 if not re.search('centos|root', environ_user, re.I):
  365                      user = environ_user

  389          self.opts.racetrack_url = url
  390:         if not url or re.search('Error', url, re.I):
  391              self.log.warning(url)

  481                      name, feature, description, tcms_id=tcmsid, logDir=log_dir)
  482:                 if test_case_id and re.search('html', test_case_id, re.I):
  483                      msg = 'Something went wrong with VCF Dashboard'

lanier-goat-development\framework\testmanager.py:
  101          use_existing_via = self.opts.extra_test_args.get('use-exist-via', '')
  102:         if re.search('True|Yes|1', use_existing_via, re.I) or \
  103                  self.is_cloud_builder_env():

  139          if not self.opts.physical and \
  140:                 re.search('public', self.opts.nimbus, re.I):
  141              self.log.info(

  428          if not self.opts.physical \
  429:                 and re.search('public', self.opts.nimbus, re.I):
  430              self.log.info(

  493          use_rt = self.opts.extra_test_args.get('use-racetrack', '')
  494:         if re.search('false|no|0', use_rt, re.I):
  495              use_rt = False

  498          use_vcf_db = self.opts.extra_test_args.get('use-racetrack', '')
  499:         if re.search('false|no|0', use_vcf_db, re.I):
  500              use_vcf_db = False

lanier-goat-development\framework\testprocess.py:
  302  
  303:             if not self.opts.physical and re.search('public', self.opts.nimbus,
  304                                                      re.I) and \

lanier-goat-development\goatrest\utils.py:
  389          self.log.debug(url)
  390:         url_match = re.search("^(https?|ftps?|file?)://(.+?)(/.*)$", url)
  391          protocol = url_match.group(1)

  848                  continue
  849:             if re.search('.*{}$'.format(clone_name), network.name):
  850                  portgroup = network

lanier-goat-development\goatrest\dnsservice\dnsservicehelper.py:
  229          for line in fp:
  230:             if not domain or re.search(r'zone "%s" {' % domain, line):
  231                  # For empty domain, ignore

lanier-goat-development\hack\aristainterface.py:
  26          cmd = ['enable', 'configure', iface]
  27:         if re.search('up', sys.argv[3], re.I):
  28              cmd.append('no shutdown')

lanier-goat-development\hack\bonduplink.py:
  32          if username == CUMULUS_USER or switch_type == SWITCH_CUMULUS:
  33:             if re.search('public', hack_bond_uplink, re.I):
  34                  self.args.rt.comment(

  68          if username == CUMULUS_USER or switch_type == SWITCH_CUMULUS:
  69:             if re.search('public', hack_bond_uplink, re.I):
  70                  self.switch.scp_from_cumulus_management_switch(

lanier-goat-development\hack\ciscointerface.py:
  15  
  16: if re.search('up', sys.argv[2], re.I):
  17      for port in sys.argv[1].split(','):

lanier-goat-development\hack\cumulusdhcpservice.py:
  38      for line in fp:
  39:         if re.search('^option domain-name "example.org";', line):
  40              print('domain-name found')

  42              continue
  43:         elif re.search('^default-lease-time 600;', line):
  44              print('default-lease-time found')

  46              continue
  47:         elif re.search('^max-lease-time 7200;', line):
  48              print('max-lease-time found')

  50              continue
  51:         elif re.search('^subnet 192.168.0.0', line):
  52              print('subnet 192.168.0.0 found')

lanier-goat-development\hack\dnsdb.py:
  116          for line in fp:
  117:             if not domain or re.search(r'zone "%s" {' % domain, line):
  118                  # For empty domain, ignore

  131          for line in lines:
  132:             if re.search(r'zone "." IN ', line):
  133                  # Zone end found

  148          for line in fp:
  149:             if not rr_domain or re.search(
  150                      r'zone "%s.in-addr.arpa" IN ' % rr_domain, line):

  162          for line in lines:
  163:             if re.search(r'zone "." IN ', line):
  164                  # Zone end found

  209          for line in fp:
  210:             if name in line or re.search('%s$' % ip_address, line):
  211                  msg = 'dnsdb add_dns_entry: %s found' % line

  243          for line in fp:
  244:             if name in line or re.search('%s$' % ip_address, line):
  245                  msg = 'dnsdb add_rr_dns_entry: %s found' % line

lanier-goat-development\hack\dnswebservice.py:
  227          for line in fp:
  228:             if not domain or re.search(r'zone "%s" {' % domain, line):
  229                  # For empty domain, ignore

lanier-goat-development\hack\emshack.py:
  57  
  58:         if skip or re.search('auto br-rack.%s' % vlan, line):
  59              changes_required = True

  61              continue
  62:         elif re.search('iface br-rack.%s' % vlan, line):
  63              changes_required = True

  65              continue
  66:         elif re.search('iface br-rack.3', line):
  67              print('Found iface br-rack.3')

  69              data.append(line)
  70:         elif re.search('iface br-rack.4', line):
  71              print('Found iface br-rack.4')

  73              data.append(line)
  74:         elif re.search('iface swp48', line):
  75              swp48_found = True

lanier-goat-development\hack\generatecustombundle.py:
  105          #    current_vc_version = 'VMware-VCSA-all-%s' % \
  106:         #                         re.search('\d+.', line).group()
  107          #    new_vc_version = 'VMware-VCSA-all-%s' % build_attributes['version']

lanier-goat-development\hack\hardresethostthroughipmi.py:
  65              oob_ip, username, password))
  66:         if re.search('Power is on', data, re.I):
  67              # If any server is powered on, just return

  76              oob_ip, username, password))
  77:         if re.search('Power is off', data, re.I):
  78              # If any server is powered on, just return

lanier-goat-development\hack\poweroffthroughipmi.py:
  66              oob_ip, username, password))
  67:         if re.search('Power is on', data, re.I):
  68              # If any server is powered on, just return

lanier-goat-development\hack\poweronthroughipmi.py:
  54              oob_ip, username, password))
  55:         if re.search('Power is on', data, re.I):
  56              # If any server is powered on, just return

  65              oob_ip, username, password))
  66:         if re.search('Power is off', data, re.I):
  67              # If any server is powered on, just return

lanier-goat-development\hack\setoobip.py:
  57          # Validated in Cumulus Switch ipmitool with Dell Server
  58:         if re.search('Static Address', op, re.I):
  59              print(('Already static ip: %s' % oob_ip))

lanier-goat-development\hack\setupnewli.py:
  91              VRM_INITIAL_IP, ROOT_USER, self.util.vrm_password)
  92:         if out[0] and not re.search('No such file or directory', out[0]):
  93              self.args.rt.info('New LI already exist')

lanier-goat-development\hack\uplinkhack.py:
   68                      br_data = False
   69:             elif re.search('bond10net', line, re.I):
   70                  # Required changes are already there

   74                  break
   75:         if re.search('iface swp45', line):
   76              print('Found swp45')

   78              data.append(line)
   79:         elif re.search('iface swp46', line):
   80              print('Found swp46')

   82              data.append(line)
   83:         elif re.search('^iface br-data$', line.strip()):
   84              print('Found br-data')

   88              if swp45 or swp46:
   89:                 if re.search('bridge-pvid 1', line):
   90                      actual = line

   97              if br_data:
   98:                 if re.search('bridge-ports', line):
   99                      actual = line

  106                      continue
  107:             if re.search('^auto br-data$', line):
  108                  print('Found auto br-data')

lanier-goat-development\hack\uplinkhackpublan.py:
  59                  continue
  60:         elif re.search('mstpctl-treeprio', line):
  61              print('Removing mstpctl-treeprio')
  62              continue
  63:         elif re.search('bridge-ports', line):
  64:             if re.search('swp45', line):
  65                  print('Hack already exist - swp45')

  73              continue
  74:         elif re.search('auto swp24', line):
  75              swp24 = True

lanier-goat-development\hack\vsan_cleanup.py:
   60      for device in devices:
   61:         if not re.search('^naa|NVMe|^mpx', device['Name'], re.I):
   62              print(('Device not of type NAA|NVMe|mpx: %s' % device['Name']))

  101              continue
  102:         elif not re.search('^naa|NVMe|^mpx', device['Name'], re.I):
  103              print(('Device not of type NAA|NVMe|mpx: %s' % device['Name']))

lanier-goat-development\hack\zookeeper.py:
  45      for line in fp:
  46:         if re.search('server', line) and not re.search(server, line):
  47:             if re.search('^#', line):
  48                  changes_required = False

lanier-goat-development\interop\interarc_vcf_bringup\create_glcm_custom_build.py:
  26      esx_version = build.get_build_attributes(buildinfo)['version']
  27:     esx_version = (re.search("[0-9]*[.][0-9]*[.][0-9]*", esx_version)).group()
  28      buildinfo = "%s-%s" % (args.extra_test_args.get('NSX_TRANSFORMERS_BUILDTYPE',

  33      nsx_version = build.get_build_attributes(buildinfo)['version']
  34:     nsx_version = (re.search("[0-9]*[.][0-9]*[.][0-9]*", nsx_version)).group()
  35      buildinfo = "%s-%s" % (args.extra_test_args.get('VCENTER_BUILDTYPE', json_data['VCENTER_BUILDTYPE']),

  39      vcenter_version = build.get_build_attributes(buildinfo)['version']
  40:     vcenter_version = (re.search("[0-9]*[.][0-9]*[.][0-9]*", vcenter_version)).group()
  41  

lanier-goat-development\interop\jenkins\outject_jenkins_env_var.py:
  57                  continue
  58:             space = bool(re.search(r"\s", str(v)))
  59              if space:

lanier-goat-development\interop\setup\configure\host_scratch_cofig.py:
  45          _, stdout, stderr = self._client.exec_command(curr_location)
  46:         current_value = re.search(r"(?<=value = \")[a-zA-Z0-9_/-]*",
  47                                    stdout.read().decode("utf-8")).group()

  49              "cd /vmfs/volumes/; ls -ltr '%s'" % self.esx["datastore"])
  50:         datastore_softlink = (re.search(r'(?<=-> )[a-zA-Z0-9-/]*',
  51                                          stdout.read().decode("utf-8"))).group()

lanier-goat-development\interop\setup\upgrade\upgrade_nsxt.py:
  224          # get bundle id
  225:         res = json.loads(re.search("{[\n].*[\n]}", out).group())
  226          return res['bundle_id']

lanier-goat-development\interop\ssp\sddcmanager_fileops.py:
  175      sddc_version = sddc.get_node_manager_app_running_version()
  176:     sddc_version = re.search("([0-9][.]){2}[0-9]", sddc_version).group(0)
  177      args.log.info('SDDC manager version is %s' % sddc_version)

  191          nsxt_password)
  192:     nsxt_base_version = re.search("([0-9][.]){4}[0-9]", nsxt_base_version).group(0)
  193      args.log.info('NSX-T base version is {}'.format(nsxt_base_version))

  198      nsxt_patch_version = build_api.get_deliverable("VMware-CC-upgrade-bundle")
  199:     nsxt_patch_version = re.search("([0-9][.]){4}[0-9]", nsxt_patch_version).group(0)
  200      args.log.info('NSX-T patch version is {}'.format(nsxt_patch_version))

lanier-goat-development\interop\ssp\sos_execution.py:
  34          matchobj = \
  35:             re.search(r'(Logs : (.*)|Health Check : (.*)|Summary : (.*))', out,
  36                        re.M)

lanier-goat-development\interop\ssp\update_files_in_sddc_manager.py:
  143      sddc_version = sddc.get_node_manager_app_running_version()
  144:     sddc_version = re.search("([0-9][.]){2}[0-9]", sddc_version).group(0)
  145      args.log.info('SDDC manager version is %s' % sddc_version)

  159          nsxt_password)
  160:     nsxt_base_version = re.search("([0-9][.]){4}[0-9]", nsxt_base_version).group(0)
  161      args.log.info('NSX-T base version is {}'.format(nsxt_base_version))

  166      nsxt_patch_version = build_api.get_deliverable("VMware-CC-upgrade-bundle")
  167:     nsxt_patch_version = re.search("([0-9][.]){4}[0-9]", nsxt_patch_version).group(0)
  168      args.log.info('NSX-T patch version is {}'.format(nsxt_patch_version))

lanier-goat-development\interop\ssp\util\bomaas_api.py:
  530          # _version = build.get_build_attributes(build_info)['version']
  531:         # # _version = (re.search("[0-9]*[.][0-9]*[.][0-9]*", _version)).group()
  532          # product_version = "%s-%s" % (_version, build_number)

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mrangdale\interop_l2bridging_svmotion.py:
   35          current_ds = current_ds[1].rstrip("'")
   36:         m1 = re.search('(datastore-[a-zA-Z0-9]+)', current_ds)
   37          current_ds = m1.group(0)

  329      new_ds2 = new_ds2[1]
  330:     m = re.search('(datastore-[a-zA-Z0-9]+)', new_ds2)
  331      new_ds2 = m.group(0)

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mrangdale\interop_nsx_controller_svmotion.py:
  369          new_ds = new_ds[1]
  370:         m = re.search('(datastore-[a-zA-Z0-9]+)', new_ds)
  371          new_ds = m.group(0)

  534          new_ds = new_ds[1]
  535:         m = re.search('(datastore-[a-zA-Z0-9]+)', new_ds)
  536          new_ds = m.group(0)

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mrangdale\interop_nsx_mgr_xvmotion.py:
  385      args.log.info(type(runtime_host))
  386:     m = re.search('[0-9]+(?:\.[0-9]+){3}', dest_host)
  387      dest_host = m.group(0)
  388:     runtime_host = re.search('[0-9]+(?:\.[0-9]+){3}', runtime_host)
  389      runtime_host = m.group(0)

  396      new_ds = new_ds[1]
  397:     m = re.search('(datastore-[a-zA-Z0-9]+)', new_ds)
  398      new_ds = m.group(0)
  399:     m1 = re.search('(datastore-[a-zA-Z0-9]+)', orig_ds)
  400      orig_ds = m1.group(0)

  457      current_ds = current_ds[1].rstrip("'")
  458:     m1 = re.search('(datastore-[a-zA-Z0-9]+)', current_ds)
  459      current_ds = m1.group(0)

  472      new_ds = new_ds[1]
  473:     m = re.search('(datastore-[a-zA-Z0-9]+)', new_ds)
  474      new_ds = m.group(0)

lanier-goat-development\interop\test\nsx_vsphere\nsx63_vsphere\mrangdale\interop_vc_hostname_change_nsxp_ip.py:
  41      try:
  42:         m = re.search('Name:\s+([a-zA-Z.]+)', out)
  43          hname = m.group(1)

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mrangdale\interop_l2bridging_svmotion.py:
   36          current_ds = current_ds[1].rstrip("'")
   37:         m1 = re.search('(datastore-[a-zA-Z0-9]+)', current_ds)
   38          current_ds = m1.group(0)

  331          new_ds2 = new_ds2[1]
  332:         m = re.search('(datastore-[a-zA-Z0-9]+)', new_ds2)
  333          new_ds2 = m.group(0)

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mrangdale\interop_nsx_controller_svmotion.py:
  399              new_ds = new_ds[1]
  400:             m = re.search('(datastore-[a-zA-Z0-9]+)', new_ds)
  401              new_ds = m.group(0)

  601              new_ds = new_ds[1]
  602:             m = re.search('(datastore-[a-zA-Z0-9]+)', new_ds)
  603              new_ds = m.group(0)

lanier-goat-development\interop\test\nsx_vsphere\nsx64_vsphere\mrangdale\interop_vc_hostname_change_nsxp_ip.py:
  42      try:
  43:         m = re.search('Name:\s+([a-zA-Z.]+)', out)
  44          hname = m.group(1)

lanier-goat-development\lcm\test\uploadbundles2centostemp.py:
  64          scp_cmd = CMD_SCP_LCM_UPLOAD_BUNDLES % (source_repo, username, ip)
  65:         if not re.search('glcm-bundles$', source_repo):
  66              cmds = ['rm -rf /tmp/glcm-bundles', 'mkdir -p /tmp/glcm-bundles']

lanier-goat-development\maas\networkservice\dell\dellservice.py:
  103              self.log.debug(data)
  104:             if data and re.search('Incorrect|Timeout|unreachable|Error',
  105                                    data, re.I):

lanier-goat-development\nsx\nsx_t\nsxt_utils\cluster_util.py:
  160          if vip in line and 'eni-' in line:
  161:             eni = re.search(r'eni-\s*\S*', line).group(0)
  162              break

lanier-goat-development\nsx\nsx_t\nsxt_utils\nsxt_bits_utils.py:
  52      INET_ADDR_REGEX = r'^.*?\inet addr:(d*\S*)'
  53:     ifconfig_host_ip = re.search(INET_ADDR_REGEX, ifcfg_op[2][1]).group(1)
  54      args.log.info('ifconfig o/p on {}: {}'.format(host_ip, ifconfig_host_ip))

lanier-goat-development\nsx\nsx_t\nsxt_utils\nsxt_utils.py:
  165      INET_ADDR_REGEX = r'^.*?inet addr:(d*\S*)'
  166:     ifconfig_host_ip = re.search(INET_ADDR_REGEX, ifcfg_op[2][1]).group(1)
  167      args.log.info('ifconfig o/p on {}: {}'.format(host_ip, ifconfig_host_ip))

lanier-goat-development\nsx\nsx_t\tests\upgrade\test_upgrade_config_pbvpn.py:
  235                  args.log.info(ex)
  236:                 find = re.search(".*RouteAlreadyExists.*", str(ex))
  237                  if find:

lanier-goat-development\nsx\nsx_utils\comm_utils.py:
   97          args.log.info('host object: {}'.format(each_host_obj))
   98:         search_obj = re.search(host_name_regex, each_host_obj.name,
   99                                 re.IGNORECASE)

  145              args.log.info('{}'.format(each_hosts_obj.network[network_no].name))
  146:             search_obj = re.search(network_regex, each_hosts_obj.
  147                                     network[network_no].name, re.IGNORECASE)

  205              args.log.info('VM object: {}'.format(vmref))
  206:             search_obj = re.search(vmname_regex, vmref.config.name, re.IGNORECASE)
  207              if search_obj:

  458          raise AssertionError("Pinged Failed with no output")
  459:     match = re.search(re_patterns.ping_packet_loss_percentage_pattern,
  460                        str(ping_output))

  490          return flag
  491:     match = re.search(re_patterns.ping_packet_loss_percentage_pattern,
  492                        str(ping_output))

  515          raise AssertionError("Scapy Failed with no output")
  516:     match = re.search(re_patterns.scapy_packet_hit_percentage_pattern,
  517                        str(scapy_output))

lanier-goat-development\nsx\nsx_utils\nsx_comp_api.py:
  1775              # look for matching site 'name'
  1776:             match = re.search(r'IPsec site name       : (\w+)', data)
  1777              if match.group(1) == name:

lanier-goat-development\nsx\nsx_utils\paramiko_util.py:
  234              # return flag
  235:         match = re.search(
  236              re_patterns.ping_packet_loss_percentage_pattern,

  343          return buff
  344:         # ret = re.search('(\d) done.', buff).group(1)
  345          # self.ssh.close()

  498              # return flag
  499:         match = re.search(re_patterns.ping_packet_loss_percentage_pattern,
  500                            str(ping_output))

lanier-goat-development\packages\storage_bundle\storage\rest.py:
  163                      url += '?' + urlencode(query_params)
  164:                 if re.search('json', headers['Content-Type'], re.IGNORECASE):
  165                      request_body = None

lanier-goat-development\platformservices\ems\test\get_domain_inventory_by_id.py:
  53  
  54:     if not ('exclude-components' in args.extra_test_args and re.search(
  55              'Loginsight', args.extra_test_args['exclude-components'], re.I)) \

lanier-goat-development\ratutils\vm.py:
  1066          if not os.path.exists(ovf_url):
  1067:             url_match = re.search("^(https?|ftps?|file?)://(.+?)(/.*)$",
  1068                                    ovf_url, re.I)

  1113              for filename in files:
  1114:                 if re.search('.ovf$', filename, re.I):
  1115                      ovf_url = 'file://%s' % filename

  1195              local_path = None
  1196:             if re.search('ova$', ovf_url):
  1197                  ovf_url, local_path = self._extract_ova(ovf_url)

lanier-goat-development\ratutils\vsan.py:
  170              for host in vc.get_hosts_in_vc():
  171:                 if host.name == parse.esx_host or re.search(parse.esx_host,
  172                                                              host.name, re.I):

  185                  for mnt_index, mode in enumerate(decommission_mode_name):
  186:                     if re.search(mode, parse.mode, re.I):
  187                          mnt_mode = mode

  242              for host in vc.get_hosts_in_vc():
  243:                 if host.name == parse.esx_host or re.search(parse.esx_host,
  244                                                              host.name, re.I):

  315                              for h in esx_host:
  316:                                 if re.search(h, host.name, re.I):
  317                                      esx_hosts.append(host)

  365                  if host.name == parse.esx_host.strip() or \
  366:                         re.search(parse.esx_host, host.name, re.I):
  367                      break

  444                  if host.name == parse.esx_host.strip() or \
  445:                         re.search(parse.esx_host, host.name, re.I):
  446                      esx_host = host

  516                  if host.name == parse.esx_host.strip() or \
  517:                         re.search(parse.esx_host, host.name, re.I):
  518                      esx_host = host

  638                  if host.name == parse.esx_host.strip() or \
  639:                         re.search(parse.esx_host, host.name, re.I):
  640                      esx_host = host

  700                  if host.name == parse.esx_host.strip() or \
  701:                         re.search(parse.esx_host, host.name, re.I):
  702                      esx_host = host

  801                  if host.name == parse.esx_host.strip() or \
  802:                         re.search(parse.esx_host, host.name, re.I):
  803                      esx_host = host

  839                  if host.name == parse.esx_host.strip() or \
  840:                         re.search(parse.esx_host, host.name, re.I):
  841                      esx_host = host

  957                      if host.name == parse.esx_host.strip() or \
  958:                             re.search(parse.esx_host, host.name, re.I):
  959                          esx_host = host

lanier-goat-development\sddcmanager\ems\test\nsxmgw.py:
   204              args.rt.verify_safely(failed, False, 'uplink not connected')
   205:         if not re.search(NSX_MGW_UPLINK_NAME, uplink['name']):
   206              failed = True

   229          for vnic in vnics:
   230:             if vnic['type'] == 'internal' and re.search(
   231                      NSX_MGW_DOWNLINK_NAME, vnic['name']):

   271          for vnic in vnics:
   272:             if vnic['type'] == 'internal' and re.search(
   273                      NSX_MGW_HALINK_NAME, vnic['name']):

   327              vnic = vnics[ha_interface]
   328:             if not re.search(NSX_MGW_HALINK_NAME, vnic['name']):
   329                  failed = True

  1108          for vnic in vnics:
  1109:             if vnic['type'] == 'internal' and re.search(
  1110                      NSX_MGW_DOWNLINK_NAME, vnic['name']):

lanier-goat-development\sddcmanager\ems\test\verifydvshasexpecteduplinks.py:
  40      vmc_testbed = args.extra_test_args.get('vmc-testbed', None)
  41:     if vmc_testbed and re.search('Yes|True|1', vmc_testbed, re.I):
  42          vmc_testbed = True

lanier-goat-development\sddcmanager\ems\test\verifyniocsetting.py:
  39              dvsname = dvs_spec.get('dvsName', dvs_spec.get('dvsId'))
  40:             nioc_present = re.search(r'niocspec', str(dvs_spec), re.I)
  41:             dvs_private = re.search(r'private', dvsname, re.I)
  42              if dvs_private and nioc_present:

  76              for item in i.childEntity:
  77:                 dvs_private = re.search(r'private', item.summary.name, re.I)
  78                  if isinstance(item, Vim.DistributedVirtualSwitch) \

lanier-goat-development\setup\test\backupesx.py:
  32                  for line in re.split('\r|\n', out[0]):
  33:                     if re.search('Backup :|Backup:', line):
  34                          backup_folder = line.split(':')[-1].strip()

  78          force_rm_backup = args.extra_test_args.get('force-rm-backup', 'True')
  79:         if re.search('false|no|0', force_rm_backup, re.I):
  80              force_rm_backup = False

lanier-goat-development\setup\test\configurecbvia.py:
  43              if not found and \
  44:                not re.search('cb-\d+-%s' % port_group, vm_name, re.I):
  45                  continue

lanier-goat-development\setup\test\hackuplink.py:
  17      hack_uplink = args.extra_test_args.get('hack-uplink', '')
  18:     if not re.search('true|yes|1', hack_uplink, re.I):
  19          args.rt.comment('Skip gOAT uplink hack')

  23      if not switch_type or \
  24:             not re.search('cisco|cumulus|arista', switch_type, re.I):
  25          args.rt.warning('Unsupported switch type: %s' % switch_type)

lanier-goat-development\setup\test\nimbus.py:
  130              except Exception as ex:
  131:                 if re.search('have already \\d testbeds deployed', str(ex)):
  132                      args.extra_test_args['nimbus-testbed-failure'] = str(ex)

  240          password = None
  241:         if args.nimbus and re.search('public', args.nimbus, re.I):
  242              cmd = ("scp -i '%s' -o UserKnownHostsFile=/dev/null -o "

lanier-goat-development\setup\test\petronas.py:
  93      cleanup_arg = args.extra_test_args.get('petronas-cleanup', 'Yes')
  94:     if cleanup_arg and re.search('Yes|True|1', cleanup_arg, re.I):
  95          region_found = cleanup_sddc(args, deploy_name, cmd_export_sddc_creds,

  98          cleanup_only = args.extra_test_args.get('cleanup-only', None)
  99:         if cleanup_only and re.search('Yes|True|1', cleanup_only, re.I):
  100              args.log.debug('Cleanup only flag found!!')

lanier-goat-development\setup\test\restoreesx.py:
   47          args.log.debug(glob.glob(path))
   48:         if re.search('R\d+S0|S0', switch_name):
   49              for via in via_vcf_imaging_details_json['switches']:

   91                  cmds, switch_ip, username, management_pwd)
   92:         elif re.search('R\d+S\d+', switch_name):
   93              switch_pwd = current_switch['password']

  109              arista = False
  110:             if re.search('cisco', switch_family, re.I):
  111                  fname = switch.upload_file_to_cisco_switch

  116                  change_pwd_switch = 'ciscochangepwd.py'
  117:             elif re.search('arista', switch_family, re.I):
  118                  arista = True

  312                          for v in vm_refs:
  313:                             if not re.search('SDDC Manager ', v.name, re.I):
  314                                  vm.delete_vm(v)

  416              cmds, VRM_INITIAL_IP, ROOT_USER, util.vrm_password)
  417:     if out[0] and not re.search('0 rows', out[0]):
  418          args.log.debug('Using remote cassandra data')

  476          # to DNS running in VRM VM
  477:         if not re.search('vcenter|-vc-|psc|SDDC Manager Controller', v.name, re.I):
  478              if vm.is_vm_powered_on(v):

  584              args.log.debug(switch_info)
  585:             if re.search('R\d+S0|S0', switch_info['name']):
  586                  mgmt_switch_ip = switch_info['ipAddress']

  614                  args.log.debug(switch_info)
  615:                 if re.search('R\d+S0|S0', switch_info['name']):
  616                      mgmt_switch_ip = switch_info['ipAddress']

  738              for v in vm_refs:
  739:                 if re.search('nsx', v.name, re.I):
  740                      args.log.debug('Do not change VM policy of NSX VM')

  800                  for v in vm_refs:
  801:                     if not re.search('SDDC Manager ', v.name, re.I):
  802                          args.rt.warning('Deleting VM: %s' % v.name)

  828          for switch_info in switch_passwords:
  829:             if re.search('R\d+S0|S0', switch_info['name']):
  830                  mgmt_switch_ip = switch_info['ipAddress']

lanier-goat-development\setup\test\setupenv.py:
  109              for f in folders:
  110:                 if re.search(builder, f):
  111                      folder = f

lanier-goat-development\skyscraper\test\aws_ec2_test.py:
  26      describe_ec2 = args.extra_test_args.get('describe_ec2', None)
  27:     if describe_ec2 and re.search('Yes|True|0', describe_ec2, re.I):
  28          describe_ec2_instance = True

  34      terminate_ec2 = args.extra_test_args.get('terminate_ec2', None)
  35:     if terminate_ec2 and re.search('Yes|True|1', terminate_ec2, re.I):
  36          terminate_ec2_instance = True

lanier-goat-development\skyscraper\test\cleanup_sddc.py:
  55  
  56:         if is_atlas and re.search('Yes|True|1', is_atlas, re.I):
  57              args.log.info('Deleting SDDC with name %s using Atlas API' % sddc_name)

lanier-goat-development\skyscraper\test\loop_provision_delete.py:
   84      # To Run PVT
   85:     if run_pvt_lite and re.search('No|False|0', run_pvt_lite, re.I):
   86          args.extra_test_args['run-pvt-lite'] = 'false'

   89      skip_vsphere_pvt_run = args.extra_test_args.get('skip-vsphere')
   90:     if skip_vsphere_pvt_run and re.search('Yes|True|1', skip_vsphere_pvt_run,
   91                                            re.I):

  100      for loop_count in range(loop_count_arg):
  101:         if enforce_quota_check and re.search('Yes|True|1',
  102                                               enforce_quota_check,

  118              args.rt.info('Skipping quota check')
  119:         if account_linking and re.search('Yes|True|1',
  120                                           account_linking,

  168          start_time = datetime.now()
  169:         if is_atlas and re.search('Yes|True|1', is_atlas, re.I):
  170              # Catch quota issue

  217              # Verify Deployment State for Atlas
  218:             if is_atlas and re.search('Yes|True|1', is_atlas, re.I):
  219                  deployment = atlas.get_deployment(deployment_id)

  363  
  364:         if account_linking and re.search('Yes|True|1',
  365                                           account_linking,

lanier-goat-development\skyscraper\test\parallel_loop.py:
  310                  args.rt.info(line.strip())
  311:             if not fail and re.search(r'FAIL \(|ABORT \(|TIMEOUT \(', line):
  312                  fail = True

  319                  'Exception|Connection timed out|No such file or directory'
  320:             if not fail and re.search(pattern, line, re.I):
  321                  fail = True

lanier-goat-development\skyscraper\test\provision_sddc_vmc_nimbus.py:
  43      delete_sddc = args.extra_test_args.get('delete-sddc', '')
  44:     if delete_sddc and re.search('Yes|True|1', delete_sddc, re.I):
  45          # Deleting sddc

lanier-goat-development\skyscraper\test\provision_sddc.py:
   42      delete_sddc = args.extra_test_args.get('delete-sddc', '')
   43:     if delete_sddc and re.search('Yes|True|1', delete_sddc, re.I):
   44          # Deleting sddc

   96          else:
   97:             if is_atlas and re.search('Yes|True|1', is_atlas, re.I):
   98                  atlas = Atlas(args, access_key=access_key)

  197      if (is_atlas
  198:        and re.search('Yes|True|1', is_atlas, re.I)
  199         and deployment_id is not None):

lanier-goat-development\sos\sos_base.py:
  447              self.args.log.info('error is %s' % (err))
  448:         matchObj = re.search(r'(Logs : (.*)|Health Check : (.*))', out, re.M)
  449          self.args.racetrack.verify_safely(matchObj.group(1) != '', True,
  450                                            'Able to locate logs')
  451:         matchObj2 = re.search(r'^.*(/var/tmp.*)$', matchObj.group(1))
  452          self.args.racetrack.verify_safely(matchObj2.group(1) != '', True,

  492          self.args.log.info('output is %s' % (out))
  493:         matchObj = re.search(r'(Logs : (.*)|Health Check : (.*))', out, re.M)
  494          self.args.racetrack.verify_safely(matchObj.group(1) != '', True,
  495                                            'Able to locate logs')
  496:         matchObj2 = re.search(r'^.*(/var/tmp/[a-zA-z0-9-]+).*$',
  497                                matchObj.group(1))

lanier-goat-development\testvpx\test\vsan\fvt\test\e2e\policy\vm.py:
  504  def splitURL(url):
  505:     urlMatch = re.search("^(https?|ftps?|file?)://(.+?)(/.*)$", url)
  506      protocol = urlMatch.group(1)

  805          return None
  806:     match = re.search(r'\[(.*)\] (.*)', path)
  807      if match:

  950  def ExtractDsNameFromPath(pathName):
  951:     result = re.search(r"\[([^\]\[%\\/]+?)\]", pathName)
  952      if not result:

lanier-goat-development\utils\batutils.py:
   80              physical = False
   81:             if re.search('true|yes', self.args.extra_test_args.get(
   82                      'physical-bat', 'false'), re.I) or self.args.opts.physical:

  208              user = environ_user
  209:         if not re.search('centos|root', environ_user, re.I):
  210              user = environ_user

lanier-goat-development\utils\envbundlesetup.py:
  138          vvd_bat_arg = self.args.extra_test_args.get('vvd-bat', '')
  139:         is_vvd_run = vvd_bat_arg and re.search('yes|true|1', vvd_bat_arg, re.I)
  140          deliverable_pattern = VVD_BUNDLE_PATTERN if is_vvd_run else r'(sdd\w+).*iso$'

  882              """
  883:             if rc[0] == 0 and out[0] and re.search(
  884                      'Please login as the user', out[0]):

lanier-goat-development\utils\esx.py:
  242              for each_string in path_structure_list:
  243:                 if re.search('RuntimeName', each_string, re.IGNORECASE):
  244                      path_split_list = each_string.split('=')

  257                  for each_string in path_structure_list:
  258:                     if re.search('RuntimeName', each_string, re.IGNORECASE):
  259                          path_split_list = each_string.split('=')

  415                  for mnt_index, mode in enumerate(decommission_mode_name):
  416:                     if re.search(mode, mnt_mode):
  417                          break

  459              for mnt_index, mode in enumerate(decommission_mode_name):
  460:                 if re.search(mode, mnt_mode):
  461                      break

  507                  for mnt_index, mode in enumerate(decommission_mode_name):
  508:                     if re.search(mode, mnt_mode):
  509                          break

  756          for line in lines:
  757:             if re.search('.StorageArrayType.', line, re.IGNORECASE):
  758                  path_split_list = line.split('=')

  898              # search for adapters UID beginning with fc.
  899:             result = re.search('(=fc\.)', fc)
  900              if not result:

lanier-goat-development\utils\infra_precheck.py:
  161                      continue
  162:                 if re.search('L1-L2-core', testbed, re.I):
  163                      core_not_found = False

  195                          continue
  196:                     if re.search(seq_name, testbed, re.I):
  197                          total_memory_required += (infra_json_data[testbed]["memory"] *

  233                      continue
  234:                 if re.search('L1-L2-core', testbed, re.I):
  235                      core_not_found = False

  252                          continue
  253:                     if re.search(seq_name, testbed, re.I):
  254                          total_memory_required += (infra_json_data[testbed]["memory"] *

lanier-goat-development\utils\isvmutil.py:
  34          if skip_cassandra_connection and \
  35:                 re.search('true|yes|1', skip_cassandra_connection, re.I):
  36              self.args.log.debug('Skipping cassandra connection')

  65              if not stderr:
  66:                 if re.search('photon', stdout, re.I):
  67                      current_distro = 'photon'

  72          self.args.log.debug('Current distribution: %s' % current_distro)
  73:         if not re.search('ubuntu|centos|photon|amzn', current_distro, re.I):
  74              msg = 'Unsupported OS/Distribution: %s' % current_distro

lanier-goat-development\utils\multirack.py:
  178                  self.args.log.info(line.strip(os.linesep))
  179:                 if not fail and re.search('FAIL \(|ABORT \(|TIMEOUT \(', line):
  180                      fail = True

  187                  pattern += 'No such file or directory'
  188:                 if not fail and re.search(pattern, line, re.I):
  189                      fail = True

lanier-goat-development\utils\nimbus.py:
    66              'nimbus-testbed-retry', '')
    67:         if nimbus_retry_deploy and re.search('true|yes|1', nimbus_retry_deploy,
    68                                               re.I):

   153                  for name in VMS_TO_BE_ON_SECOND_HOST:
   154:                     if re.search(name, vmref.name):
   155                          msg = 'Migrate VM: %s to ESX host: %s'

   163                  for name in VMS_TO_BE_ON_THIRD_HOST:
   164:                     if re.search(name, vmref.name):
   165                          msg = 'Migrate VM: %s to ESX host: %s'

   391      def get_esx_jump_vm_info(self):
   392:         if not re.search('public', self.args.nimbus, re.I):
   393              esx_vms = []

   397              for vmref in vmrefs:
   398:                 if re.search(r'.*-%s.esx.*' % self.unique_id, vmref.name,
   399                               re.I):
   400                      esx_vms.append(vmref)
   401:                 elif re.search(r'ubuntu.*-%s' % self.unique_id, vmref.name,
   402                                 re.I):

   598              for vmref in vmrefs:
   599:                 if re.search(clone_name, vmref.name):
   600                      if vmref.name.find('Ubuntu64') != -1:

   630                  for line in out.splitlines():
   631:                     if re.search('^On Storage:', line, re.I):
   632                          build_in_storage = line.split(':')[1]
   633:                     elif re.search('^Status:', line, re.I):
   634                          build_status = line.split(':')[1]

   863                                                          'True')
   864:             if reservation and re.search('False|No|0', reservation, re.I):
   865                  reservation = False

  1298                  pattern += 'Nimbus checker pipeline broken'
  1299:                 if self.nimbus_retry_deploy and re.search(pattern, line):
  1300                      self.args.log.error('Testbed deploy failed due to resource')

  1306                      # key pattern.  ignore this type of line.
  1307:                     if re.search("raw_text", line) is None:
  1308                          self.args.log.info('Command output: %s' % line)
  1309:                         if re.search('exception:|Error|Fault|OOM in worker', line) or \
  1310                                  start_recording:

  1313  
  1314:                     if re.search('Scheduler Job ID', line):
  1315                          self.args.log.info("Nimbus schedule queue activated.")

  1492              manager = v['annotation']['managers_chain_str']
  1493:             if not re.search('akirpekar', manager):
  1494                  self.args.log.debug('Current user not in HCIBU org')
  1495                  return False, None, None
  1496:             elif re.search('lanier-bat|svc.raas', manager) or \
  1497                      nimbus_user == 'lanier-bat' or \

  1707                  for manager, count in list(org_nimbus_exception.items()):
  1708:                     if not re.search(manager, manager_chain):
  1709                          self.args.log.debug('User {} max testbed defined by '

lanier-goat-development\utils\nsx.py:
   42          for line in fp:
   43:             if re.search(r'workflow\.recipe=', line):
   44                  t = line.split('=')

   47                  self.args.log.info('Found recipe: %s = %s' % (p, v))
   48:                 if re.search(NSX_RECIPE_SKYSCRAPER, v):
   49                      is_skyscraper = True

  329              for childvm in childvms:
  330:                 match = re.search(r'.*Management.*', childvm.name,
  331                                    re.IGNORECASE)

  334                      for vm in list_vms:
  335:                         match = re.search(r'.*controller.*', vm.name,
  336                                            re.IGNORECASE)

  398              for key in list(d.keys()):
  399:                 match = re.search(r'nsx.*controller.*anti.*affinity',
  400                                    key, re.IGNORECASE)

  435                              for vm in d[key]['member_vms']:
  436:                                 match = re.search(r'controller', vm,
  437                                                    re.IGNORECASE)

lanier-goat-development\utils\remotetest.py:
  557              value = self.args.opts.extra_test_args.get('use-racetrack')
  558:             if (not value or not re.search('false|no', value, re.I)) and \
  559                      ip not in 'localhost':

  583                      regexp = 'FAIL \(|ABORT \(|TIMEOUT \('
  584:                     if not fail and re.search(regexp, line):
  585                          fail = True

  594                              traceback_record += line
  595:                     if not test_rst_log_dir and re.search('Log file:', line):
  596                          test_rst_log_dir = str(line.split(' ')[-1]).split(

  600                      err_regexp = '(Syntax|Import|Name)Error:'
  601:                     if re.search(err_regexp, traceback_record):
  602                          # split long traceback record into several segments

  613                      pattern = 'Broken pipe|Finalize object, dead'
  614:                     if re.search(pattern, line, re.I):
  615                          self.args.log.warning(line.strip(os.linesep))

  618                      pattern += 'No such file or directory'
  619:                     if not fail and re.search(pattern, line, re.I):
  620                          fail = True

lanier-goat-development\utils\restutil.py:
  83              return headers, has_bearer
  84:         elif not re.search(r'.*/v[\d]+/.*', url, re.I):
  85              # Check if the API is versioned APIs
  86              return headers, has_bearer
  87:         elif re.search(r'nimbus|maas|gaas', url, re.I):
  88              return headers, has_bearer

  98          hostname = bringup.get_sddc_manager_host_name()
  99:         if not re.search(r'{}|{}'.format(self.sddc_ip, hostname), url):
  100              return headers, has_bearer

lanier-goat-development\utils\switch.py:
   104                  p.sendline(switch_password)
   105:             elif (i == 10 or i == 11) or (data and re.search('core dump',
   106                                                               data, re.I)):

   463                      'Arista port enable/disable script executed')
   464:                 if data and re.search(
   465                          'Incorrect|Timeout|unreachable|Assertion|core',

   469                  break
   470:             elif i == 16 or i == 17 or (data and re.search('core dump',
   471                                                             data, re.I)):

   478                  self.args.log.info('Logged in as root user, run: "%s"' % cmd)
   479:                 if cmd and re.search('arista', cmd, re.I):
   480                      self.args.log.info('enable bash here')

   854          except Exception as ex:
   855:             if re.search('Incorrect|Timeout|unreachable|core', str(ex), re.I):
   856                  raise

   883          except Exception as ex:
   884:             if re.search('Incorrect password', str(ex), re.I):
   885                  raise

   912          except Exception as ex:
   913:             if re.search('Incorrect password', str(ex), re.I):
   914                  raise

   945              """
   946:             if not re.search('bond-slaves', data):
   947                  self.args.log.error('Unable to find bond-slaves')

   952              for interface in data:
   953:                 if not interface or not re.search('swp', interface):
   954                      self.args.log.debug('Not an interface: %s' % interface)

  1106          except Exception as ex:
  1107:             if re.search('Incorrect password', str(ex), re.I):
  1108                  raise

  1139          except Exception as ex:
  1140:             if re.search('Incorrect password', str(ex), re.I):
  1141                  raise

  1236          except Exception as ex:
  1237:             if re.search('Incorrect password', str(ex), re.I):
  1238                  raise

  1271          except Exception as ex:
  1272:             if re.search('Incorrect password', str(ex), re.I):
  1273                  raise

  1396                  return False
  1397:             return bool(re.search(CUMULUS_BOND_MANAGEMENT_CHECK, data))
  1398          except AssertionError as ex:
  1399:             if re.search('Incorrect password', str(ex), re.I):
  1400                  return False

  1521              return False
  1522:         return bool(re.search(peer_alive_cmd, data, re.I))
  1523  

  1546                  time_diff = (time.time() - start_time)
  1547:                 if not output or not re.search(' 0% packet loss', output):
  1548                      msg = 'Unable to reach %s, ' % switch_ip

  1563              self.args.log.warning(traceback.format_exc())
  1564:             if re.search('Incorrect', str(ex), re.I):
  1565                  raise

  1586                      MANAGEMENT_SWITCH, VIA_DEFAULT_PASSWORD, via=True)
  1587:                 if not output or not re.search(' 0% packet loss', output):
  1588                      msg = 'Unable to reach %s, ' % switch_ip

  1600              self.args.log.error(ex)
  1601:             if re.search('Incorrect', str(ex), re.I):
  1602                  raise

lanier-goat-development\utils\testbed.py:
   146              if via_ovf_location:
   147:                 if re.search('ovf$', via_ovf_location):
   148                      self.args.log.debug(

   161              for key in list(self.args.extra_test_args.keys()):
   162:                 if re.search('rack-.-jump-vm-ip', key):
   163                      self.rack = str(key.split('-')[1])

   186          if not os.path.exists(via_ovf_location):
   187:             url_match = re.search(
   188                  "^(https?|ftps?|file?|esx)://(.+?)(/.*)$",

   294          except AssertionError as ex:
   295:             if re.search(
   296                      "Unable to connect to VC host |Invalid login to VC host ",

   399              for d in data:
   400:                 if re.search('Has VSAN partitions', d['Reason']):
   401                      raise AssertionError('%s %s' % (d['Name'], d['Reason']))

   433                  #     for disk in data:
   434:                 #         if re.search('Eligible for use by VSAN',
   435                  #  disk['State']):

   448          except AssertionError as ex:
   449:             if re.search("Unable to connect to VC host ", str(ex)):
   450                  self.args.rt.info('Connection error: %s' % ex)

   460                  return False
   461:             elif re.search("Connection refused", str(ex)):
   462                  self.args.rt.info('Socket error: %s' % ex)
   463                  return False
   464:             elif re.search("Bad authentication type", str(ex)):
   465                  # If previous cleanup was done and next imaging was halfway

   698          default_user = None
   699:         if not server_vendor or not re.search('dell|hp|quanta|cisco|lenovo',
   700                                                server_vendor, re.I):

   704              raise AssertionError(msg)
   705:         if re.search('dell', server_vendor, re.I):
   706              default_password = IPMI_DELL_PASSWORD
   707              default_user = IPMI_DELL_USER
   708:         elif re.search('hp', server_vendor, re.I):
   709              default_password = IPMI_HP_PASSWORD
   710              default_user = IPMI_HP_USER
   711:         elif re.search('quanta', server_vendor, re.I):
   712              default_password = IPMI_QUANTA_PASSWORD
   713              default_user = IPMI_QUANTA_USER
   714:         elif re.search('lenovo', server_vendor, re.I):
   715              default_user = IPMI_LENOVO_USER
   716              default_password = IPMI_LENOVO_PASSWORD
   717:         elif re.search('cisco', server_vendor, re.I):
   718              default_password = IPMI_CISCO_PASSWORD

   736          except AssertionError as ex:
   737:             if re.search('Hitting core dump', str(ex)):
   738                  self.args.log.warning('Ignore ipmitool coredump')

   758          except AssertionError as ex:
   759:             if re.search('Hitting core dump', str(ex)):
   760                  self.args.log.warning('Ignore ipmitool coredump')

   780          except AssertionError as ex:
   781:             if re.search('Hitting core dump', str(ex)):
   782                  self.args.log.warning('Ignore ipmitool coredump')

  1188          else:
  1189:             if re.search('hp', server_vendor, re.I):
  1190                  channel_info = '2'

  1202          except AssertionError as ex:
  1203:             if re.search('Hitting core dump', str(ex)):
  1204                  self.args.log.warning('Ignore ipmitool coredump')

  1382                      if rc[1] == -1 and out[1] is None and \
  1383:                        re.search('quanta', server_vendor, re.I) and i == 2:
  1384                          self.args.rt.warning(

  1386                          break
  1387:                     elif out[1] and re.search('core', out[1], re.I):
  1388                          msg = 'Core dumped executing cmd: %s' % cmd

  1391                          continue
  1392:                     elif out[1] and re.search('Assertion', out[1], re.I):
  1393                          msg = 'Assertion executing cmd: %s' % cmd

  1768              not_deleting_via_vm = True
  1769:             if re.search('true|yes',
  1770                           self.args.extra_test_args['cleanup-only-testbed'],

  1794                          vm_name = via_vm.name
  1795:                         if not re.search('via', vm_name, re.I):
  1796                              self.args.rt.warning(

  1983                  for n in destination.parent.network:
  1984:                     if not re.search('^20*', n.name):
  1985                          self.args.log.info('Using network: %s' % n.name)

  2077                  if cdrom.deviceInfo and cdrom.deviceInfo.summary and \
  2078:                         re.search(self.iso_filename, cdrom.deviceInfo.summary):
  2079                      iso_mounted = True

  2405          for vmref in vmrefs:
  2406:             if re.search('%s$' % self.unique_id, vmref.name):
  2407                  # self.args.log.info('VM name %s to move under vApp: %s'

  2437                                                                    self.unique_id))
  2438:             if re.search('public', self.args.nimbus, re.I):
  2439                  self.nim = nimbus.Nimbus(self.args, self.unique_id)

  2546              self.args.rt.info('Nimbus setup: %s' % self.args.nimbus)
  2547:             if re.search('public', self.args.nimbus, re.I):
  2548                  self.nim = nimbus.Nimbus(self.args, self.unique_id)

lanier-goat-development\utils\util.py:
   114          self.is_isvm_env = self.is_true('isvm-env')
   115:         if not self.args.opts.physical and re.search('public', self.args.opts.nimbus, re.I) and \
   116                  not self.args.opts.vcHost:

   388                  build_product = build_api.get_json_build_info()['product']
   389:                 if re.search(environment, build_product, re.I):
   390                      env = True

   419          self.args.log.debug(url)
   420:         url_match = re.search("^(https?|ftps?|file?)://(.+?)(/.*)$", url)
   421          protocol = url_match.group(1)

   475  
   476:         if not re.search(expected_build, build_product, re.I):
   477              self.args.racetrack.warning(msg)

   514              self.args.log.debug(line)
   515:             if re.search('Vmid', line):
   516                  continue

   586                  vm_id = re.split('[ ]+', o)[0]
   587:                 o = re.search('\d+', vm_id)
   588                  self.args.log.debug(vm_id)

   634              except AssertionError as ex:
   635:                 if re.search("Unable to connect to VC host ", str(ex)):
   636                      self.args.rt.warning('Connection error: %s' % ex)

   641                      continue
   642:                 elif re.search("Connection refused", str(ex)):
   643                      self.args.log.warning('Socket error: %s' % ex)
   644                      continue
   645:                 elif re.search("Authentication failed", str(ex)):
   646                      self.args.log.warning('Authentication failed: %s' % ex)
   647                      continue
   648:                 elif re.search("Bad authentication type", str(ex)):
   649                      self.args.rt.warning('Bad authentication type: %s' % ex)
   650                      continue
   651:                 elif re.search("NoValidConnectionsError", str(ex)):
   652                      self.args.rt.warning('NoValidConnectionsError: %s' % ex)

   692                      continue
   693:                 if re.search('TOR|MGMT|SPINE', d['type'], re.I):
   694:                     if re.search('MGMT', d['type'], re.I):
   695                          switch_password.append({'ipAddress': d['ip'],

   708                  else:
   709:                     if not re.search('192.168.100.', d['ip']):
   710                          continue

   851                  continue
   852:             if re.search('^127.', ip_address[1]):
   853                  self.args.log.info(

   913                      continue
   914:                 if re.search('^#', line):
   915                      # line - Comments
   916                      continue
   917:                 if not re.search('=', line):
   918                      self.args.log.warning('Looks like some buggy line: %s' % line)

   957                      'Pattern: %s unique id: %s' % (pattern, vmref.name))
   958:                 if re.search(pattern, vmref.name, re.I) and \
   959:                         re.search(vm_prefix, vmref.name, re.I):
   960                      if not check_build_number or check_build_number and \
   961:                             re.search(build_number, vmref.name, re.I):
   962                          self.args.rt.info('Found %s VM: %s' % (vm_prefix,

  1185                  self.args.log.info(line)
  1186:                 if re.search('Host *', line):
  1187                      self.args.log.info(

  1237          """
  1238:         if not self.args.opts.physical and re.search('public',
  1239                                                       self.args.nimbus,

  1888          if out[0]:
  1889:             if re.search('Received 3 response', out[0]):
  1890                  msg = 'Successfully received %s arping' % destination

  1914          self.args.log.info('JumpVM: %s, %s, %s' % (vmref.name, physical, ip))
  1915:         if not physical and not re.search('jumpvm', vmref.name, re.I):
  1916              raise VerifyFatal('Unable to find Jump VM with the name *jumpvm*')

  1919                  self.args.log.info('Jump VM IP address: %s' % ip_address)
  1920:                 if re.search(ip, ip_address):
  1921                      self.args.rt.info(

  2027                      isinstance(device, Vim.Vm.Device.VirtualE1000e):
  2028:                 if re.search('Ubuntu64', vmref.name):
  2029                      self.args.log.info('Temporary hack')

  2041                  device_change = Vim.Vm.Device.VirtualDeviceSpec()
  2042:                 if re.search(vm_prefix, vmref.name):
  2043                      self.args.log.info(

  2482              return False
  2483:         elif self.is_true('nimbus') or re.search(
  2484                  'nimbus', self.args.extra_test_args.get('environment', ''),

  2543          self.args.log.info('VC: %s' % self.args.opts.vcHost)
  2544:         if not self.args.opts.physical and re.search('public', self.args.opts.nimbus, re.I):
  2545              self.args.log.info('Ignoring VC connection for public, since not available')

  3118              return
  3119:         if re.search('^sb-', build, re.I):
  3120              self.args.rt.comment('Can not recommend Sandbox build: %s' % build)

  3129          state = data['buildstate']
  3130:         if not state or not re.search('succeeded', state):
  3131              raise AssertionError('Build state: %s' % state)

  3139              vcf_db_server = self.args.extra_test_args['vcf-server']
  3140:         if vcf_db_server and not re.search('http', vcf_db_server):
  3141              vcf_db_server = 'https://%s/recommendbuild' % vcf_db_server
  3142:         if not re.search('recommendbuild', vcf_db_server):
  3143              vcf_db_server = '%s/recommendbuild' % vcf_db_server

  3201              user = environ_user
  3202:         if not re.search('centos|root', environ_user, re.I):
  3203              user = environ_user

  3223              return
  3224:         if re.search('^sb-', build, re.I):
  3225              self.args.rt.comment('Can not recommend Sandbox build: %s' % build)

  3234          state = data['buildstate']
  3235:         if not state or not re.search('succeeded', state):
  3236              raise AssertionError('Build state: %s' % state)

  3244              vcf_db_server = self.args.extra_test_args['vcf-server']
  3245:         if vcf_db_server and not re.search('http://', vcf_db_server):
  3246              vcf_db_server = 'https://%s/batsstatus' % vcf_db_server
  3247:         if not re.search('batsstatus', vcf_db_server):
  3248              vcf_db_server = '%s/batsstatus' % vcf_db_server

  3310              user = environ_user
  3311:         if not re.search('centos|root', environ_user, re.I):
  3312              user = environ_user

  3420          for line in fp:
  3421:             if re.search('workflow.recipe=', line):
  3422                  line = line.strip()

  4039          # 1 valid special char
  4040:         if re.search('%[0-9]', password) is not None or \
  4041:                 re.search(PASSWORD_REGEX, password) is None \
  4042                  or password is None:

  4403          pattern += 'dependency-error|script-error|invalid'
  4404:         if re.search(build_status, pattern, re.I):
  4405              self.args.rt.verify_fatal(build_status, 'succeeded',

  4523              default = ''
  4524:         return bool(re.search(
  4525              'true|yes|1', str(args.extra_test_args.get(key, default)), re.I))

  4718                  self.args.rt.info('out[0]: %s' % out0)
  4719:                 dbc_abs_sos_path = os.path.join(sos_log_dir, re.search('sos[-\d]*',
  4720                                                                         out0, re.I).group())

lanier-goat-development\utils\vc.py:
  1470                              dvsconfig = item.GetConfig()
  1471:                             mgmt_pg = re.search(r'mgmt', dvsconfig.name, re.I)
  1472                              if not self.util.is_petronas_environment() and \

  1579                      for child in network.childEntity:
  1580:                         if not re.search(r'vmc.*dvs.*dvuplink.*', child.name,
  1581:                                          re.I) and re.search(r'vmc.*dvs',
  1582                                                               child.name, re.I):

  1586              for network in datacenter.networkFolder.childEntity:
  1587:                 if not re.search(r'.*rack.*dswitch.*uplink.*', network.name,
  1588:                                  re.I) and re.search(r'.*rack.*dswitch.*',
  1589                                                       network.name, re.I):

  1599                      for child in network.childEntity:
  1600:                         if re.search(r'.*dswitch.*public', child.name,
  1601                                       re.I):

  1604                                  version
  1605:                         if re.search(r'.*dswitch.*private', child.name,
  1606                                       re.I):

  1638                      for child in network.childEntity:
  1639:                         if not re.search(r'vmc.*dvs.*dvuplink.*', child.name,
  1640:                                          re.I) and re.search(r'vmc.*dvs',
  1641                                                               child.name, re.I):

  1644              for network in datacenter.networkFolder.childEntity:
  1645:                 if not re.search(r'.*rack.*dswitch.*uplink.*', network.name,
  1646:                                  re.I) and re.search(r'.*rack.*dswitch.*',
  1647                                                       network.name, re.I):

  1654                      for child in network.childEntity:
  1655:                         if re.search(r'.*dswitch.*public', child.name,
  1656                                       re.I):
  1657                              vds_public_mtu = child.config.maxMtu
  1658:                         if re.search(r'.*dswitch.*private', child.name,
  1659                                       re.I):

  1752                      #  for vmotion
  1753:                     if re.search(r'vmotion', d[dst_esx][vmk][2], re.I):
  1754                          cmds = ['vmkping ++netstack=vmotion %s -d -s %d' %

  1758                      # for vxlan
  1759:                     elif re.search(r'vxlan', d[dst_esx][vmk][2], re.I):
  1760                          cmds = ['vmkping ++netstack=vxlan %s -d -s %d' %

lanier-goat-development\utils\vm.py:
  1108              self.args.log.debug('VM name: %s %s' % (
  1109:                 vmref.name, re.search(port_group, vmref.name)))
  1110:             if partial_vm_name and re.search(partial_vm_name, vmref.name) and \
  1111:                not ip_address and port_group and re.search(port_group,
  1112                                                             vmref.name):
  1113                  matching_vmrefs.append(vmref)
  1114:             if partial_vm_name and re.search(partial_vm_name, vmref.name) and \
  1115                 not ip_address and not port_group:

  1126                      #     ip, ip_address))
  1127:                     if re.search(ip_address, ip):
  1128                          self.args.rt.info(

  1135                          continue
  1136:                     if partial_vm_name and not re.search(partial_vm_name,
  1137                                                           vmref.name):

  1150                  if not net.ipAddress and partial_vm_name:
  1151:                     if not re.search(partial_vm_name, vmref.name):
  1152                          self.args.log.debug(

  1177              # what goes in the OVF
  1178:             ovf_file.path = re.search(".*/(.*)$", url).group(1)
  1179              local_path = base_dir.replace(os.sep, "/") + "/"

  1385                          for d in destination.datastore:
  1386:                             if re.search('vsanDatastore', d.name):
  1387                                  if not jump_vmref:

  1421                                      break
  1422:                                 elif re.search('vsanDatastore', d.name):
  1423                                      deploy_vm_datastore = d

  1833          for key, value in list(dom_object.items()):
  1834:             if re.search(r'child-(\d+)', key):
  1835                  (comp_tree, raid) = self.find_all_components_and_raids(value)

lanier-goat-development\utils\vsan.py:
  347          if rcs[0] == 0 and rcs[1] == 1:  # expected rcs for enabled case
  348:             match1 = re.search(r'Performance.*service.*green.*',
  349                                 outs[0], re.I)
  350:             match2 = re.search(r'No.*such.*test.*name.*perfsvcstatus.*',
  351                                 outs[1], re.I)

  372          elif rcs[0] == 0 and rcs[1] == 0:  # expected rcs for disabled case
  373:             match1 = re.search(
  374                  r'Performance.*service.*yellow.*', outs[0], re.I)
  375:             match2 = re.search(
  376                  r'Performance.*service.*yellow.*', outs[1], re.I)

  451          if rcs[0] == 0:
  452:             match = re.search(r'sys.datastore.*=.*\/vmfs\/volumes\/vsan\:.*',
  453                                outs[0], re.I)

  628                  hostname))
  629:         hosts_membership = re.search(r'Sub-Cluster Member Count: ([\d+]*)',
  630                                       out[0], re.M | re.I)

lanier-goat-development\utils\vsphere7util.py:
  275          for file_name in nsxt_bundle_files:
  276:             if re.search("^(bundle.+)\.tar$", file_name):
  277                  bundle_file_name = file_name
  278:             if re.search("^(bundle.+)\.manifest$", file_name):
  279                  manifest_file_name = file_name
  280:             if re.search("^(bundle.+)\.manifest.sig$", file_name):
  281                  sig_file_name = file_name

lanier-goat-development\utils\ebs\ebs_utils.py:
  216  
  217:     m = re.search('%s.*vol(\S+)' % EBS_CONST.EBS_FEATURE_DEVICE_CHARS,
  218                    device_name)

  634      for expected in expected_messages:
  635:         if re.search(expected, error_message):
  636              return True

lanier-goat-development\utils\interop\nsxt24utils.py:
  1711              self.args.rt.comment('VM name: {}'.format(vmref.config.name))
  1712:             search_obj = re.search(vmname_regex, vmref.config.name, re.IGNORECASE)
  1713              if search_obj:

lanier-goat-development\utils\interop\nsxtutils.py:
  695                          remove_space = re.sub(' ', '', op[0])
  696:                         if re.search('state:Active', remove_space):
  697                              active_edge = edge

lanier-goat-development\utils\interop\tools_utils.py:
  268              raise AssertionError("`%s` returned non-zero value" % f_cmd)
  269:         matches = re.search(r'power is (\w+)', output, re.M | re.I)
  270          if matches:

lanier-goat-development\utils\lcm\bundleutil.py:
   99          for i in range(num_of_elements):
  100:             if self.bundle_elements[i]['download_software'] and re.search(
  101                      'yes|true|1', self.bundle_elements[i]['download_software'],

lanier-goat-development\utils\lcm\lcmbase.py:
  142          for file in bundle_files:
  143:             if re.search("^(bundle.+)\.tar$", file):
  144                  lcm_bundle = True
  145:             if re.search("^(bundle.+)\.manifest$", file):
  146                  manifest_file = True

  196          for file in bundle_files:
  197:             if re.search("^(bundle.+)\.tar$", file):
  198                  lcm_bundle = os.path.join(LCM_BUNDLE_PATH, file)
  199:             if re.search("^(bundle.+)\.manifest$", file):
  200                  manifest_file = os.path.join(LCM_BUNDLE_PATH, file)

lanier-goat-development\utils\sddcmanager\add_remove_host_verifications.py:
   49              raise AssertionError('Unable to find VSAN cluster state')
   50:         if re.search('Virtual SAN Clustering is not enabled', out[0]):
   51              return False

  147                  self.args.log.debug(out)
  148:                 add_host_mac_address = re.search(
  149                      r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", out)

  279          for host in node_manager_inventory['esxiHosts']:
  280:             if hostname and not re.search(host['hostName'], hostname, re.I):
  281                  self.args.log.debug(

lanier-goat-development\utils\sddcmanager\base.py:
    57          if skip_cassandra_connection and \
    58:            re.search('true|yes|1', skip_cassandra_connection, re.I):
    59              self.args.log.debug('Skipping cassandra connection')

  1099                  # ip-address can vary
  1100:                 match = re.search('^forward-addr.* (\d{1,3}\.\d{1,3}\.\d{1,'
  1101                                    '3}\.\d{1,3}$)', line, re.I)

lanier-goat-development\utils\skyscraper\atlas_base.py:
  246          sddc_type = self.args.extra_test_args.get('sddc-type')
  247:         if sddc_type and re.search('1NODE', sddc_type, re.I):
  248              sddc_type = 'OneNode'

  305          account_link_sddc_config = None
  306:         if account_linking and re.search('Yes|True|1',
  307                                           account_linking,

lanier-goat-development\utils\skyscraper\base.py:
  2358              if region_arg:
  2359:                 if re.search('london|eu-west-2|eu_west_2', region_arg, re.I):
  2360                      region = 'eu-west-2'
  2361:                 elif re.search('frankfurt|eu-central-1|eu_central_1', region_arg, re.I):
  2362                      region = 'eu-central-1'
  2363:                 elif re.search('sydney|ap-southeast-2|ap_southeast_2', region_arg, re.I):
  2364                      region = 'ap-southeast-2'
  2365:                 elif re.search('tokyo|ap-northeast-1|ap_northeast_1', region_arg, re.I):
  2366                      region = 'ap-northeast-1'
  2367:                 elif re.search('singapore|ap_southeast_1|ap-southeast-1', region_arg, re.I):
  2368                      region = 'ap-southeast-1'
  2369:                 elif re.search('canada|ca_central_1|ca-central-1', region_arg, re.I):
  2370                      region = 'ca-central-1'
  2371:                 elif re.search('paris|eu_west_3|eu-west-3', region_arg, re.I):
  2372                      region = 'eu-west-3'
  2373:                 elif re.search('stockholm|eu_north_1|eu-north-1', region_arg, re.I):
  2374                      region = 'eu-north-1'
  2375:                 elif re.search('hongkong|ap_east_1|ap-east-1', region_arg, re.I):
  2376                      region = 'ap-east-1'
  2377:                 elif re.search('osaka|ap-northeast-3|ap_northeast_3', region_arg, re.I):
  2378                      region = 'ap-northeast-3'
  2379:                 elif re.search('East|east|us-east-1', region_arg, re.I):
  2380                      region = 'us-east-1'
  2381:                 elif re.search('milan|eu-south-1|eu_south_1', region_arg, re.I):
  2382                      region = 'eu-south-1'

lanier-goat-development\utils\skyscraper\ec2util.py:
  58                  self.aws_account_region = "us-west-2"
  59:                 if re.search('East|east|us-east-1', region_arg, re.I):
  60                      self.aws_account_region = "us-east-1"
  61:                 elif re.search('london|eu-west-2|eu_west_2', region_arg, re.I):
  62                      self.aws_account_region = "eu-west-2"

lanier-goat-development\utils\skyscraper\rce.py:
  314              for data in res['_list']:
  315:                 if re.search(pod_rpm_pattern, data['_download_url'], re.I):
  316                      rpm_file = data['_download_url']

lanier-goat-development\utils\vcf\ovfhelper.py:
   90          if cb_ovf_location:
   91:             if re.search('ovf$', cb_ovf_location):
   92                  self.args.log.debug(

  124          if not os.path.exists(cb_ovf_location):
  125:             url_match = re.search(
  126                  "^(https?|ftps?|file?|esx)://(.+?)(/.*)$",

  387                              break
  388:                         elif re.search(self.cb_ipaddr, ip):
  389                              found = True

  392                      if not found and \
  393:                             not re.search(r'cb-\d+-%s' % self.port_group, vm_name, re.I):
  394                          continue

  401                                             'Cloud Builder VM powered on ?')
  402:                 if not re.search('cb-', vm_name, re.I):
  403                      self.args.rt.warning('Do not delete %s as it is not Cloud Builder' % vm_name)

lanier-goat-development\utils\vcf\util.py:
  381              rc, out, err = self.run_local_sh_cmd('ifconfig')
  382:             if not re.search(VRM_INITIAL_IP, out):
  383                  self.running_in_jump_vm = True

  445                  role = 'SPINE'
  446:             if re.search('R%s+S\d+' % rack, str(name)):
  447                  self.args.log.debug('Switch type: %s' %

  847          if out:
  848:             get_status = re.search(r'(active.*ago)\r\n', out[-1])
  849              if get_status:

lanier-goat-development\utils\vcf\ems\base.py:
  1290          for cdata in self.get_credentials():
  1291:             match = re.search('ESXI', cdata["entityType"], re.I)
  1292              if match:

  2142          for hostname in list(esx_inventory.keys()):
  2143:             if re.search('ACTIVE', esx_inventory[hostname]['status'], re.I):
  2144                  status['healthy'].append(hostname)

  2234          ceip_status = self.get_ceip_status_v1()
  2235:         match = re.search(r'ENABLE.*', ceip_status, re.I)
  2236  

  2563          self.args.rt.comment('Current Status is %s' % output)
  2564:         match = re.search(r'%s.*' % status, output, re.I)
  2565          while match:

  2570              output = self.get_ceip_status()
  2571:             match = re.search(r'%s.*' % status, output, re.I)
  2572          self.args.log.info('Status has been changed to %s' % output)

  2578          self.args.rt.comment('Current Status is %s' % output)
  2579:         match = re.search(r'%s.*' % status, output, re.I)
  2580          max_retries = 30

  2587              output = self.get_ceip_status_v1()
  2588:             match = re.search(r'%s.*' % status, output, re.I)
  2589              retries -= 1

lanier-goat-development\utils\vcf\ems\solutionsmanagerbase.py:
  888          for file in bundle_files:
  889:             if re.search("^(bundle.+)\.tar$", file):
  890                  vdi_bundle = True
  891  
  892:             if re.search("^(bundle.+)\.manifest$", file):
  893                  manifest_file = True

  957          for file in bundle_files:
  958:             if re.search("^(bundle.+)\.tar$", file):
  959                  vdi_bundle = os.path.join(VDI_PATH, file)
  960  
  961:             if re.search("^(bundle.+)\.manifest$", file):
  962                  manifest_file = os.path.join(VDI_PATH, file)

lanier-goat-development\utils\vcf\ems\util.py:
  123          if out:
  124:             get_status = re.search(r'(active.*ago)\r\n', out[-1])
  125              if get_status:

  155              for key in list(d.keys()):
  156:                 match = re.search(r'.*%s.*anti.*affinity' % component,
  157                                    key, re.IGNORECASE)

  227                              if component == 'vRLI':
  228:                                 match = re.search(r'.*loginsight.*', vm,
  229                                                    re.IGNORECASE)
  230                              else:
  231:                                 match = re.search(r'%s' % component, vm,
  232                                                    re.IGNORECASE)

  290              for childvm in childvms:
  291:                 match = re.search(r'.*Management.*', childvm.name,
  292                                    re.IGNORECASE)

  296                          if component == 'vRLI':
  297:                             match1 = re.search(r'.*loginsight.*',
  298                                                 vm.name, re.IGNORECASE)
  299                          else:
  300:                             match1 = re.search(r'.*%s.*' % component,
  301                                                 vm.name, re.IGNORECASE)

lanier-goat-development\utils\via\base.py:
   98          via_reachable = False
   99:         if not physical and re.search('public', args.nimbus, re.I):
  100              self.args.rt.info(

  134                      pattern = "^(https?|ftps?|file?|esx)://(.+?)(/.*)$"
  135:                     url_match = re.search(pattern, md5_location, re.I)
  136                      if not url_match:

  192              self.args.log.warning('No bundle build')
  193:         if self.physical or not re.search('public', args.nimbus, re.I):
  194              if not via_reachable:

  289              raise AssertionError('Unable to find cumulus switch type')
  290:         if re.search('x86_64', out[0], re.I):
  291              source_file = os.path.join(path, '..', '..', 'dependency',

  311          #                                            ROOT_USER, NIMBUS_ROOT_PWD)
  312:         # if out[0] and not re.search('No such file or directory', out[0]):
  313          #     self.args.log.info(

  324          #     return
  325:         if not self.physical and re.search('public', self.args.nimbus, re.I):
  326              if not self.nim:

  347              for vmref in vmrefs:
  348:                 if re.search(self.name, vmref.name) and re.search('esx',
  349                                                                    vmref.name):

  372          #                               '/root/via.script')
  373:         # if re.search('public', self.args.nimbus, re.I):
  374          #     self.args.rt.info('Do not setup VSAN partition for public nimbus')

  385          # for o in out[0].split('\n'):
  386:         #     if not re.search('mpx', o):
  387          #         self.args.log.info('Current line does not match: %s' % o)

lanier-goat-development\utils\via\service.py:
  182              app.logger.warning(traceback.format_exc())
  183:             if re.search('Address already in use', str(ex)) and i < 2:
  184                  # Verbose log HTTP request headers and data

lanier-goat-development\utils\via\rest\base.py:
  238                  msg = 'Power is off'
  239:             if re.search(msg, out, re.I):
  240                  self.args.log.warning('Host {0} is still {1}'.format(

lanier-goat-development\vc\test\verify_tls_version.py:
  38      if not out:
  39:         getversion = re.search(r'TLSv[0-9]+\.[0-9]+', str(out),
  40                                 re.I)

lanier-goat-development\vc\test\verify_vds_status_version.py:
  75  
  76:     if not re.search(r'green', vds_status, re.I):
  77          raise AssertionError('vDS status is not green')

lanier-goat-development\vcf\updaterpm.py:
  85              for r in rpm_list:
  86:                 start_position = re.search(r"\d", r).start() - 1
  87                  self.services.append(r[:start_position])

lanier-goat-development\vcf\artemail\saveartvac.py:
  40          self.args.physical = str(self.args.physical).lower()
  41:         if not re.search('false|true', self.args.physical, re.I):
  42              raise AssertionError('Unsupported Type: %s' % self.args.physical)

lanier-goat-development\vcf\artemail\savebringupdashboard.py:
  37          self.args.physical = str(self.args.physical).lower()
  38:         if not re.search('false|true', self.args.physical, re.I):
  39              raise AssertionError('Unsupported Type: %s' % self.args.physical)

lanier-goat-development\vcf\artemail\savedashboard.py:
  40          self.args.physical = str(self.args.physical).lower()
  41:         if not re.search('false|true', self.args.physical, re.I):
  42              raise AssertionError('Unsupported Type: %s' % self.args.physical)

lanier-goat-development\vcf\artemail\sendartmail.py:
  47          self.args.physical = str(self.args.physical).lower()
  48:         if not re.search('false|true', self.args.physical, re.I):
  49              raise AssertionError('Unsupported Type: %s' % self.args.physical)

lanier-goat-development\vcf\artemail\utils\utils.py:
  320              sys.exit(1)
  321:         if re.search('ob|sb', args.cbBuild):
  322              args.cbBuild = args.cbBuild.split('-')[-1]

lanier-goat-development\vcf\assessment\assessment_sos_helper.py:
  313      def __multiline_matcher_from_text(text: str, regex: str):
  314:         return re.search(regex, text, re.MULTILINE)
  315  

lanier-goat-development\vcf\assessment\assessment_util.py:
  251              if progress_messages:
  252:                 total_number_of_messages = re.search(match_pattern, progress_messages[0]).group(1)
  253  

  269          for message in progress_messages:
  270:             if re.search(match_pattern, message):
  271                  is_correct_format_array.append(True)

lanier-goat-development\vcf\assessment\test\assessment_app.py:
  378      def extract_status_code_from_output(self, out: str):
  379:         matcher = re.search(ECHO_SC_AFTER_CMD_REGEX, out, re.MULTILINE)
  380          if not matcher:

lanier-goat-development\vcf\assessment\test\assessment.py:
  567              GET_INSTALLED_OPERATIONS_MANAGER_RPM_INFO)
  568:         info_match = re.search(OPERATIONS_MANAGER_PACKAGE_REGEX, '\n'.join(info_output))
  569          ops_mgr_package = info_match.group(0)

lanier-goat-development\vcf\autojsonutil\autojsoncreationutil.py:
  275              domain_match = re.compile('name =\s+(\S+)\.')
  276:             matched = re.search(domain_match, out[0])
  277              if matched:

  296          ip_range_regex = re.compile('(\d+\.\d+\.\d+\.)(\d+):(\d+\.\d+\.\d+\.)(\d+)')
  297:         check_range = re.search(ip_range_regex, ip_range)
  298          assert check_range, "ip range not specified in the format start_ip:end_ip"

  730                  for each_pool in all_nw_pools:
  731:                     if re.search('L3-Pool', each_pool['name'], re.IGNORECASE):
  732                          nw_pool_ids[each_pool['id']] = each_pool['name']

lanier-goat-development\vcf\ceip\test\verify_ceip_gets_disabled_v1.py:
  45      ceip_status = sddc.get_ceip_status_v1()
  46:     match = re.search(r'ENABLED.*', ceip_status, re.I)
  47      if match:  # ceip is enabled

  54  
  55:         match = re.search(r'IN_PROGRESS.*', disable_ceip_output['status'], re.I)
  56          if match:

  64          output = sddc.wait_ceip_status_change_v1('DISABLING')
  65:         match = re.search(r'DISABLED.*', output, re.I)
  66  

  77              raise AssertionError(msg)
  78:     elif re.search(r'DISABLE.*', ceip_status, re.I):
  79          args.rt.comment('CEIP was already disabled, hence no need to enable again')

lanier-goat-development\vcf\ceip\test\verify_ceip_gets_enabled_v1.py:
  57      args.rt.comment('Now checking for "UNKNOWN" or "DISABLED" status')
  58:     match = re.search(r'UNKNOWN.*|DISABLED', ceip_status, re.I)
  59      if match:  # ceip is neither enabled nor disabled.

  65          enable_ceip_output = enable_ceip.json()
  66:         match = re.search(r'ENABLING|IN_PROGRESS',
  67                            enable_ceip_output['status'], re.I)

  75          output = sddc.wait_ceip_status_change_v1('ENABLING')
  76:         match = re.search(r'ENABLE.*', output, re.I)
  77          if match:  # ceip is enabled at top/vcf-level

  86              raise AssertionError(msg)
  87:     elif re.search(r'ENABLE.*', ceip_status, re.I):
  88          args.rt.comment('CEIP was already enabled, hence no need to enable again')

lanier-goat-development\vcf\domainmanager\test\add_cluster_delete_cluster_nsxt_wld.py:
  374          hostcommission.Run(args)
  375:         if not ('exclude-components' in args.extra_test_args and re.search(
  376                  'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\vcf\domainmanager\test\add_cluster_during_remove_host.py:
  268          if ACQUIRE_LOCK_ACTION in str(ex):
  269:             match = re.search(r'lock.*held.*by.*remov.*host', str(ex), re.I)
  270              if match:

lanier-goat-development\vcf\domainmanager\test\add_cluster_during_vidomaincreate.py:
  248          if ACQUIRE_LOCK_ACTION in str(ex):
  249:             match = re.search(r'lock.*held.*by.*creat.*domain', str(ex), re.I)
  250              if match:

lanier-goat-development\vcf\domainmanager\test\add_cluster_during_vidomaindelete.py:
  267              '''
  268:             match = re.search(r'lock.*held.*by.*delet.*domain', str(ex), re.I)
  269              if match:

lanier-goat-development\vcf\domainmanager\test\add_host_during_add_cluster.py:
  253          if ACQUIRE_LOCK_ACTION in str(ex):
  254:             match = re.search(r'lock.*held.*by.*add.*cluster', str(ex), re.I)
  255              if match:

lanier-goat-development\vcf\domainmanager\test\enable_vrli_multicluster_nsxt_wld.py:
  84  
  85:     if not ('exclude-components' in args.extra_test_args and re.search(
  86              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\vcf\domainmanager\test\pos_greenfield_nsxt_wld_lifecycle.py:
  159  
  160:     if not ('exclude-components' in args.extra_test_args and re.search(
  161              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

  537      vidomaincreate.Run(args)
  538:     if not ('exclude-components' in args.extra_test_args and re.search(
  539              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\vcf\domainmanager\test\pos_password_update_nsxtmgr.py:
  127  
  128:     if not ('exclude-components' in args.extra_test_args and re.search(
  129              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\vcf\domainmanager\test\pos_wld_vrli.py:
  71  
  72:     if not ('exclude-components' in args.extra_test_args and re.search(
  73              'Loginsight', args.extra_test_args['exclude-components'], re.I)):

lanier-goat-development\vcf\imaging\image.py:
  313                  ntp = bringup_json['ntpServers'][0]
  314:     if re.search('dell', via_conf['server_vendor'], re.I):
  315          oob_user = IPMI_DELL_USER
  316          oob_password = IPMI_DELL_PASSWORD
  317:     elif re.search('quanta', via_conf['server_vendor'], re.I):
  318          oob_user = IPMI_QUANTA_USER
  319          oob_password = IPMI_QUANTA_PASSWORD
  320:     elif re.search('hp', via_conf['server_vendor'], re.I):
  321          oob_user = IPMI_HP_USER
  322          oob_password = IPMI_HP_PASSWORD
  323:     elif re.search('lenovo', via_conf['server_vendor'], re.I):
  324          oob_user = IPMI_LENOVO_USER
  325          oob_password = IPMI_LENOVO_PASSWORD
  326:     elif re.search('cisco', via_conf['server_vendor'], re.I):
  327          oob_user = IPMI_CISCO_USER

lanier-goat-development\vcf\imaging\backend\esxi_deployment_environment_setup.py:
  264              if from_patch:
  265:                 data['_list'] = [x for x in data['_list'] if re.search(iso_regex, x['path'])]
  266                  self.log.debug("from_patch is enable : data %s" % data['_list'])

  271              for path in data['_list']:
  272:                 if re.search(iso_regex, path['path']):
  273                      url = path['_download_url']

  614                  return response
  615:         if not re.search(IP_ADDRESS_REGEX, opts.address):
  616              msg = 'Invalid IP address: %s' % opts.address

  624                  return response
  625:         if not re.search(NETMASK_REGEX, opts.netmask):
  626              msg = 'Invalid netmask: %s' % opts.netmask

  635              sys.exit(1)
  636:         if not re.search(IP_ADDRESS_REGEX, opts.gateway):
  637              msg = 'Invalid gateway: %s' % opts.gateway

  646              sys.exit(1)
  647:         if opts.dns and not re.search(IP_ADDRESS_REGEX, opts.dns):
  648              msg = 'Invalid DNS IP: %s' % opts.dns

  657              sys.exit(1)
  658:         if not re.search(MAC_ADDRESS_REGEX, opts.mac, re.IGNORECASE):
  659              msg = 'Invalid MAC address: %s' % opts.mac

  673              self.log.info('MAC address: %s' % opts.mac)
  674:         if not re.search(HOSTNAME_FORMAT, opts.hostname):
  675              msg = 'Invalid hostname: %s' % opts.hostname

lanier-goat-development\vcf\imaging\backend\vsan_cleanup.py:
   67      for device in devices:
   68:         if not re.search('^naa|NVMe|^mpx', device['Name'], re.I):
   69              print(('Device not of type NAA|NVMe|mpx: %s' % device['Name']))

  116              continue
  117:         elif not re.search('^naa|NVMe|^mpx', device['Name'], re.I):
  118              print(('Device not of type NAA|NVMe|mpx: %s' % device['Name']))

  143      data = {'error': reason, 'state': state, 'mac': mac, 'ip': ip}
  144:     if re.search('PreInstall', state, re.I):
  145          data['status'] = 'Imaging'

lanier-goat-development\vcf\networkservice\dellservice.py:
  104              self.args.log.debug(data)
  105:             if data and re.search('Incorrect|Timeout|unreachable|Error',
  106                                    data, re.I):

lanier-goat-development\vcf\networkservice\test\emsmultiracksetup.py:
  121                  self.args.log.info(line.strip(os.linesep))
  122:                 if not fail and re.search('FAIL \(|ABORT \(|TIMEOUT \(', line):
  123                      fail = True

  130                  pattern += 'No such file or directory'
  131:                 if not fail and re.search(pattern, line, re.I):
  132                      fail = True

lanier-goat-development\vcf\networkservice\test\emssetup.py:
   955              if switch_data:
   956:                 if re.search(SWITCH_DELL, switch_data, re.I):
   957                      switch_family = SWITCH_DELL

  1005                args.extra_test_args.get('rack')
  1006:     if re.search('true|yes', args.extra_test_args.get('enable-cross-rack', ''),
  1007                   re.I) and not rack:

lanier-goat-development\vcf\networkservice\test\validatenetworkconfig.py:
  200          out = out.replace("%", " percent")
  201:         if re.search(r'is down|Network is unreachable|0 packets received|'
  202                       r'failed', out, re.MULTILINE):

lanier-goat-development\vcf\nsx\cross_site_setup.py:
  266              for switch in list(all_logical_switches.keys()):
  267:                 matchObj = re.search(r'%s' % switch, pg['name'], re.I)
  268                  if matchObj:

lanier-goat-development\vcf\pipeline\bomupdate.py:
  175          for a in artifacts:
  176:             if re.search(r'%s' % filename, a['fileName']):
  177                  artifacts_download_url = build_url + 'artifact/' + a['relativePath']

lanier-goat-development\vcf\pipeline\resource_check.py:
  26          args.extra_test_args['config-json'] = nimbus_private_config
  27:         if re.search('wdc', nimbus_private_config, re.I):
  28              pod = 'WDC'
  29:         elif re.search('fujitsu', nimbus_private_config, re.I):
  30              pod = 'FUJITSU'

lanier-goat-development\vcf\pipeline\accessories\skiplevelpipelineaccessory.py:
  161              input_map, build_number, RT_JOB_ARTIFACT_NAME, JENKINS_USER, JENKINS_API_TOKEN)
  162:         racetrack_id = re.search(r'^RACETRACK_ID=(.*)\n', rt_artifact).group(1)
  163          if not racetrack_id:

lanier-goat-development\vcf\pipeline\migration\bundle_download_upload.py:
  409          try:
  410:             return re.search("\r\n(.+?)\x1b", resp[-1]).group(1) != "[]"
  411          except AttributeError:

lanier-goat-development\vcf\pipeline\migrationaccessory_helpers\non_capacity_tests.py:
  246  
  247:                 if re.search(r'UNKNOWN|DISABLED', self.helper.get_ceip_status(), re.I):
  248                      if not self.helper.args.util.is_true('skip-wf-helper'):

  264  
  265:                 if re.search(r'UNKNOWN|ENABLE', self.helper.get_ceip_status(), re.I):
  266                      if not self.helper.args.util.is_true('skip-wf-helper'):

lanier-goat-development\vcf\pipeline\tools\nimbus_utils.py:
  172                  # iclone-i-svc.maas-8779
  173:                 m = re.search("(iclone-((.+?).*))", nimbus_testbed_name)
  174                  try:

  181                      # dlaskova-197 -> maas setup name is:
  182:                     m = re.search("(.+?.*[-\d?])(.*)", nimbus_testbed_name)
  183                      try:

  222                      regex = '(.*)(iclone-(.+?.*[-\d?]))(\.)(.*)'
  223:                     m = re.search(regex, vm)
  224                      nimbus_testbed_name = m.group(2)

  231                      regex = '(.+?.*[-\d?])(\.)(.*)'
  232:                     m = re.search(regex, vm)
  233                      nimbus_testbed_name = m.group(1)

lanier-goat-development\vcf\test\addhost.py:
  397              host['ip'] = str(last_ip_address + i)
  398:             unique = int(re.search(r'\d+', fqdn).group())
  399              host['fqdn'] = fqdn.replace(str(unique), str(unique + i))

  402              if self.instant_vcf:
  403:                 host['name'] = last_esx.replace(re.search(r'esx.\d+', last_esx).group(),
  404                                                  'esx.{}'.format(unique + i - 1))

  561              raise AssertionError(err)
  562:         date_match = re.search('\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', out)
  563          date_expiry = out[date_match.start():date_match.end()]

lanier-goat-development\vcf\test\copy_soslog_to_bugzilla.py:
  30          matchobj = \
  31:             re.search(r'(Logs : (.*)|Health Check : (.*)|Summary : (.*))', out,
  32                        re.M)

lanier-goat-development\vcps_maas\common\vm_ops.py:
  503                  if cdrom.deviceInfo and cdrom.deviceInfo.summary and \
  504:                         re.search(self.iso_filename, cdrom.deviceInfo.summary):
  505                      iso_mounted = True

lanier-goat-development\vcps_maas\test\tpm\test_tpm_cases.py:
  313              args.rt.comment('Result : %s' % str(result))
  314:             path = re.search("\/v*.*? ", result[1][1]).group()
  315              args.rt.comment('Dump file Path: %s' % str(path))

  321              args.rt.comment('Result : %s' % str(result))
  322:             path = re.search("\/v*.*", result[1][0]).group()
  323              args.rt.comment('zdump path: %s' % str(path))

lanier-goat-development\vcqe\runvcqe_nsxt.py:
  23          'run-multicluster-test', None)
  24:     if is_pvt_run and re.search('Yes|True|1', is_pvt_run, re.I):
  25          remote_repo = args.opts.setupInfo['centos']

lanier-goat-development\vcqe\runvcqe.py:
  23          'run-multicluster-test', None)
  24:     if is_pvt_run and re.search('Yes|True|1', is_pvt_run, re.I):
  25          remote_repo = args.opts.setupInfo['centos']

lanier-goat-development\vcqe\runvspherelite.py:
  15      is_pvt_run = args.extra_test_args.get('pvt-run', None)
  16:     if is_pvt_run and re.search('Yes|True|1', is_pvt_run, re.I):
  17          remote_repo = args.opts.setupInfo['centos']

lanier-goat-development\vcqe\runvspheremultiaz.py:
  16      is_pvt_run = args.extra_test_args.get('pvt-run', None)
  17:     if is_pvt_run and re.search('Yes|True|1', is_pvt_run, re.I):
  18          remote_repo = args.opts.setupInfo['centos']

lanier-goat-development\vcqe\vcqe.py:
  40  
  41:     if is_pvt_run and re.search('Yes|True|1', is_pvt_run, re.I):
  42          vcqe_pvt_run = True

lanier-goat-development\vdi\base.py:
  446          """
  447:         status = bool(re.search('upload finished', req.text, re.I))
  448          self.args.rt.verify_fatal(status, True, 'Verify upload ISO/OVA')

  709                                  'skip-partial-matching-workflow']
  710:                         if re.search(
  711                                  skip_partial_matching_workflow, task_name,

lanier-goat-development\vdi\viewutil.py:
  142      def verify_vsan_enabled(self):
  143:         actual = bool(re.search('true', self.get_pool()['useVSAN'], re.I))
  144          self.args.rt.verify_safely(actual, True,

lanier-goat-development\via\test\imagingonvvdhosts.py:
  144                  msg = 'Power is off'
  145:             if re.search(msg, out, re.I):
  146                  self.log.warning('Host {0} is still {1}'.format(

lanier-goat-development\vmc\create_vms.py:
  54      for networks in cluster_config.network:
  55:         resp = re.search('sddc-cgw-network-1', networks.name)
  56          if resp:

lanier-goat-development\vmc\PodManager.py:
   853          if expected_status_code == 200:
   854:             assert (re.search(
   855                  'task-\d', data['value'])), "Expected task id but found %s" % \

   908          if expected_status_code == 200:
   909:             assert (re.search(
   910                  'task-\d', data['value'])), "Expected task id but found %s" % \

   944          if expected_status_code == 200:
   945:             assert (re.search(
   946                  'task-\d', data['value'])), "Expected task id but found %s" % \

   985          if expected_status_code == 200:
   986:             assert (re.search(
   987                  'task-\d', data['value'])), "Expected task id but found %s" % \

  1514          self.args.log.info(data)
  1515:         assert (re.search(
  1516              'task-\d', data['value'])), "Expected task id but found %s" % data[

  1537          if expected_status_code == 200:
  1538:             assert (re.search(
  1539                  'task-\d', data['value'])), "Expected task id but found %s" % \

  1559          if expected_status_code == 200:
  1560:             assert (re.search(
  1561                  'task-\d', data['value'])), "Expected a task id but found %s" % \

  1580          self.args.log.info(data)
  1581:         assert (re.search(
  1582              'task-\d', data['value'])), "Expected task id but found %s" % data[

  1603          self.args.log.info(data)
  1604:         assert (re.search(
  1605              'task-\d', data['value'])), "Expected task id but found %s" % data[

  1626          self.args.log.info(data)
  1627:         assert (re.search(
  1628              'task-\d', data['value'])), "Expected task id but found %s" % data[

  1753          if expected_status_code == 200:
  1754:             assert (re.search(
  1755                  'task-\d', data['value'])), "Expected a task id but found %s" % \

  1843                  # segregate the file name  2.1.0-8055762-internal.json
  1844:                 hardware_type = re.search(
  1845                      "[-][^\d]+[.]", type_x).group(0)[1:-1]
  1846:                 version = re.search(r"[\d].[\d].[\d][-][\d]+", type_x).group(0)
  1847                  break

  1883          self.args.log.info(data)
  1884:         assert (re.search(
  1885              'task-\d', data['value'])), "Expected task id but found %s" % data[

  1907          self.args.log.info(data)
  1908:         assert (re.search(
  1909              'task-\d', data['value'])), "Expected task id but found %s" % data[

  2039          if expected_status_code == 200:
  2040:             assert (re.search(
  2041                  'task-\d', data['value'])), "Expected task id but found %s" % \

  2070          if expected_status_code == 200:
  2071:             assert (re.search(
  2072                  'task-\d', data['value'])), "Expected task id but found %s" % \

  2445          if expected_status_code == 200:
  2446:             assert (re.search(
  2447                  'task-\d', data['value'])), "Expected task id but found %s" % \

  2772          if expected_status_code == 200:
  2773:             assert (re.search(
  2774                  'task-\d', data['value'])), "Expected task id but found %s" % \

  2802          if expected_status_code == 200:
  2803:             assert (re.search(
  2804                  'task-\d', data['value'])), "Expected task id but found %s" % \

  2886          if expected_status_code == 200:
  2887:             assert (re.search(
  2888                  'task-\d', data['value'])), "Expected task id but found %s" % \

  2921          if expected_status_code == 200:
  2922:             assert (re.search(
  2923                  'task-\d', data['value'])), "Expected task id but found %s" % \

lanier-goat-development\vmc\about\about.py:
  31              "Unexpected return code {0}, for '{1}'".format(rc, cmd))
  32:     version_build_match = re.search(
  33          r'VMware-pod-([\d.]+)-([\d.]+).x86_64', out[0])

lanier-goat-development\vmc\common_utils\buildweb_utils.py:
  30                      url = deliverable['_download_url']
  31:                     if re.search(search_build_pattern, url) is None:
  32                          continue

lanier-goat-development\vmc\common_utils\component_versions.py:
  26          return_code, out, err))
  27:     min_version = re.search(r'\d{4}', out[1]).group(0)
  28      main_version = out[0].replace("build", min_version)

  46          return_code, out, err))
  47:     current_esx_version = re.search(r'\d.\d.\d-\d.\d.\d*', out[0]).group(0)
  48      return current_esx_version

lanier-goat-development\vmc\common_utils\softwaremanifest.py:
  143              set_software_json = args.extra_test_args['set-software-json']
  144:             if re.search(r'^http', set_software_json):
  145                  set_software_json = \

lanier-goat-development\vmc\common_utils\storage_policy_utils.py:
  30          for vmref in self.vc.get_all_vmrefs():
  31:             if re.search(vm_name, vmref.name, re.I):
  32                  return vmref

lanier-goat-development\vmc\ebs\ebs_pod_base.py:
  250  def get_ebs_vol_id(device_name):
  251:     m = re.search('%s.*vol(\S+)' % 'Amazon_Elastic_Block_Store',
  252                    device_name)

  258  def get_ebs_serial_number(device_name):
  259:     m = re.search('%s.*vol(\S+)' % 'Amazon_Elastic_Block_Store',
  260                    device_name)

lanier-goat-development\vmc\negative\control_plane_stage.py:
  92          set_software_json = args.extra_test_args['set-software-json']
  93:         if re.search(r'^http', set_software_json):
  94              set_software_json = \

lanier-goat-development\vmc\negative\set_software.py:
  92          set_software_json = args.extra_test_args['set-software-json']
  93:         if re.search(r'^http', set_software_json):
  94              set_software_json = \

lanier-goat-development\vmc\negative\setsoftwarerepo\set_software_all.py:
  113          set_software_json = args.extra_test_args['set-software-json']
  114:         if re.search(r'^http', set_software_json):
  115              set_software_json = \

lanier-goat-development\vmc\negative\setsoftwarerepo\set_software_esx_only.py:
  113          set_software_json = args.extra_test_args['set-software-json']
  114:         if re.search(r'^http', set_software_json):
  115              set_software_json = \

lanier-goat-development\vmc\negative\setsoftwarerepo\set_software_nsx_only.py:
  114          set_software_json = args.extra_test_args['set-software-json']
  115:         if re.search(r'^http', set_software_json):
  116              set_software_json = \

lanier-goat-development\vmc\negative\setsoftwarerepo\set_software_pod_nsx_vc.py:
  114          set_software_json = args.extra_test_args['set-software-json']
  115:         if re.search(r'^http', set_software_json):
  116              set_software_json = \

lanier-goat-development\vmc\negative\setsoftwarerepo\set_software_pod_nsx.py:
  114          set_software_json = args.extra_test_args['set-software-json']
  115:         if re.search(r'^http', set_software_json):
  116              set_software_json = \

lanier-goat-development\vmc\negative\setsoftwarerepo\set_software_pod_only.py:
  114          set_software_json = args.extra_test_args['set-software-json']
  115:         if re.search(r'^http', set_software_json):
  116              set_software_json = \

lanier-goat-development\vmc\negative\setsoftwarerepo\set_software_vc_only.py:
  114          set_software_json = args.extra_test_args['set-software-json']
  115:         if re.search(r'^http', set_software_json):
  116              set_software_json = \

lanier-goat-development\vmc\negative\setsoftwarerepo\softwarerepo_processor.py:
  111          set_software_json = args.extra_test_args['set-software-json']
  112:         if re.search(r'^http', set_software_json):
  113              set_software_json = \

lanier-goat-development\vmc\patch\cat_pod_patcher.py:
  60          self.pod_to_remove = out[0]
  61:         self.current_pod_version = re.search(
  62              r'[0-9].[0-9].[0-9]-[0-9]+[^-.]', out[0]).group(0)

  95          """installs previous version of the pod rpm"""
  96:         current_build_no = re.search(
  97              r'[0-9]+[^-.]', self.current_pod_version).group(0)

lanier-goat-development\vmc\patch\pod_patcher.py:
  45      args.log.info('Set software payload URL is %s \n' % build_url)
  46:     target_pod_version = re.search(r'\d.\d.\d-\d*', file_name).group(0)
  47      # extract the version from the file

lanier-goat-development\vmc\patch\usecases\add_host_during_pod_patch.py:
  96          set_software_json = args.extra_test_args['set-software-json']
  97:         if re.search(r'^http', set_software_json):
  98              set_software_json = \

lanier-goat-development\vmc\patch\usecases\remove_host_during_pod_patch.py:
  96          set_software_json = args.extra_test_args['set-software-json']
  97:         if re.search(r'^http', set_software_json):
  98              set_software_json = \

lanier-goat-development\vmc\patch\usecases\workloads\pingplotter.py:
  54          try:
  55:             lossi = float(re.search("\d+(?=% packet loss)", out).group(0))
  56              pingi = float(out.split('/')[-3])

lanier-goat-development\vmc\pod\loop_provision_delete_without_account_unlinking.py:
   77      # To Run PVT
   78:     if run_pvt_lite and re.search('No|False|0', run_pvt_lite, re.I):
   79          args.extra_test_args['run-pvt-lite'] = 'false'

   82      skip_vsphere_pvt_run = args.extra_test_args.get('skip-vsphere')
   83:     if skip_vsphere_pvt_run and re.search('Yes|True|1', skip_vsphere_pvt_run,
   84                                            re.I):

   92      for loop_count in range(loop_count_arg):
   93:         if enforce_quota_check and re.search('Yes|True|1',
   94                                               enforce_quota_check,

  110              args.rt.info('Skipping quota check')
  111:         if account_linking and re.search('Yes|True|1',
  112                                           account_linking,

  153          start_time = datetime.now()
  154:         if is_atlas and re.search('Yes|True|1', is_atlas, re.I):
  155              # Catch quota issue

  202              # Verify Deployment State for Atlas
  203:             if is_atlas and re.search('Yes|True|1', is_atlas, re.I):
  204                  deployment = atlas.get_deployment(deployment_id)

  300          """
  301:         if account_linking and re.search('Yes|True|1',
  302                                           account_linking,

lanier-goat-development\vmc\pod\pod_service.py:
  105      args.log.debug(out)
  106:     if re.search('subject:', out):
  107          success.append("PASS: Found subject in server certificate.")

  110              "FAIL: Failed to find subject in server certificate, certificate details.")
  111:     if re.search('start date:', out):
  112          success.append("PASS: Found start date in server certificate.")

  115  
  116:     if re.search('expire date:', out):
  117          success.append("PASS: Found end date in server certificate.")

  120  
  121:     startdate = re.search('start date: (.*)', out).group(1)
  122:     enddate = re.search('expire date: (.*)', out).group(1)
  123      startyear = parser.parse(startdate).year

  193      args.log.debug(out)
  194:     if re.search('TLS_RSA_WITH_AES_256_GCM_SHA384',
  195                   out):

lanier-goat-development\vmc\pod\add_remove_host_cluster_regression\add_remove_host_via_pod_manager.py:
  129      if expected_status_code == 200:
  130:         assert (re.search('task-\d', data['value'])), "Expected task id but found %s" % data[
  131              'value']

lanier-goat-development\vmc\pod\bringup_regression\verify_nsx_mgmt_vms_anti_affinity_rules.py:
   42          for childvm in childvms:
   43:             match = re.search(r'.*Management.*', childvm.name,
   44                                re.IGNORECASE)

  110          for key in list(host_rules_found.keys()):  # Keys are the rule names found
  111:             match = re.search(r'nsx-unified-appliance-anti-affinity-rule.*',
  112                                key, re.IGNORECASE)

  158                          for vm in host_rules_found[key]['member_vms']:
  159:                             match = re.search(r'NSX-Manager', vm, re.IGNORECASE)
  160                              if not match:

lanier-goat-development\vmc\pod\code_coverage\pod_bringup\provision_sddc_bringup.py:
   54      delete_sddc = str(args.extra_test_args.get('delete-sddc', ''))
   55:     if delete_sddc and re.search('Yes|True|1', delete_sddc, re.I):
   56          # Deleting sddc

  106          else:
  107:             if is_atlas and re.search('Yes|True|1', is_atlas, re.I):
  108                  atlas = Atlas(args, access_key=access_key)

  239      if (is_atlas
  240:             and re.search('Yes|True|1', is_atlas, re.I)
  241              and deployment_id is not None):

lanier-goat-development\vmc\pod\helper\cleanup_all_failed_sddcs_in_org.py:
  35      is_atlas = args.extra_test_args.get('is-atlas', 0)
  36:     if is_atlas and re.search('Yes|True|1', is_atlas, re.I):
  37          delete_func = delete_sddc_via_atlas

lanier-goat-development\vmc\pod\upgrade_verifications\negative\setsoftwarerepo\set_software_all.py:
  108          set_software_json = args.extra_test_args['set-software-json']
  109:         if re.search(r'^http', set_software_json):
  110              set_software_json = \

lanier-goat-development\vmc\pod\upgrade_verifications\negative\setsoftwarerepo\set_software_esx_only.py:
  107          set_software_json = args.extra_test_args['set-software-json']
  108:         if re.search(r'^http', set_software_json):
  109              set_software_json = \

lanier-goat-development\vmc\pod\upgrade_verifications\negative\setsoftwarerepo\set_software_nsx_only.py:
  110          set_software_json = args.extra_test_args['set-software-json']
  111:         if re.search(r'^http', set_software_json):
  112              set_software_json = \

lanier-goat-development\vmc\pod\upgrade_verifications\negative\setsoftwarerepo\set_software_pod_nsx_vc.py:
  108          set_software_json = args.extra_test_args['set-software-json']
  109:         if re.search(r'^http', set_software_json):
  110              set_software_json = \

lanier-goat-development\vmc\pod\upgrade_verifications\negative\setsoftwarerepo\set_software_pod_nsx.py:
  108          set_software_json = args.extra_test_args['set-software-json']
  109:         if re.search(r'^http', set_software_json):
  110              set_software_json = \

lanier-goat-development\vmc\pod\upgrade_verifications\negative\setsoftwarerepo\set_software_pod_only.py:
  109          set_software_json = args.extra_test_args['set-software-json']
  110:         if re.search(r'^http', set_software_json):
  111              set_software_json = \

lanier-goat-development\vmc\pod\upgrade_verifications\negative\setsoftwarerepo\set_software_vc_only.py:
  108          set_software_json = args.extra_test_args['set-software-json']
  109:         if re.search(r'^http', set_software_json):
  110              set_software_json = \

lanier-goat-development\vmc\pvt\pod_utils.py:
  192          self.args.log.info(data)
  193:         assert(re.search(
  194              'task-\d', data['value'])), "Expected task id but found %s" % data['value']

lanier-goat-development\vmc\pvt\sddc_patch.py:
   99          set_software_json = args.extra_test_args['set-software-json']
  100:         if re.search(r'^http', set_software_json):
  101              set_software_json = \

lanier-goat-development\vmc\upgrade\storage_policy\vm.py:
  435  def splitURL(url):
  436:     urlMatch = re.search("^(https?|ftps?|file?)://(.+?)(/.*)$", url)
  437      protocol = urlMatch.group(1)

  736          return None
  737:     match = re.search(r'\[(.*)\] (.*)', path)
  738      if match:

  881  def ExtractDsNameFromPath(pathName):
  882:     result = re.search(r"\[([^\]\[%\\/]+?)\]", pathName)
  883      if not result:

lanier-goat-development\vmc\wcp\Wcputils.py:
  269              version_x = values["spec"]["nodeImageRef"]["name"]
  270:             match_pattern = re.search(pattern, version_x)
  271              versions.append(match_pattern.group(0))

  657          cluster_config["insecure-skip-tls-verify"] = True
  658:         match_pattern = re.search(ipv4_regex, cluster_config["server"])
  659          cluster_ip = match_pattern.group(0)

portfolio-system-tests\new\portfolio_system_tests\gelato\setup_collector_simulator_pair.py:
  109          res = shell.exec_command('virsh net-dhcp-leases default')
  110:         vm_ip_search = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
  111          if not vm_ip_search:

portfolio-system-tests\new\portfolio_system_tests\gelato\setup_collector_simulator_stack.py:
  85          res = shell.exec_command('virsh net-dhcp-leases default')
  86:         vm_ip_search = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
  87          if not vm_ip_search:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\NX_Manufacture\utils.py:
   98      one, two = os.path.split(component)
   99:     build_number = re.search(name + "-(.*?)-(.*?).noarch.rpm", two).group(2)
  100      number = ": " + str(build_number)
  101  
  102:     version = re.search(name + "-(.*?)-(.*?).noarch.rpm", two).group(1)
  103      version = ": " + str(version)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\NX_Manufacture\vm.py:
  100              vm_create_node_image_name = \
  101:                 re.search(r'(.*)\s+:\s+' + vm_product_name,
  102                            line).group(1).strip()

  174      try:
  175:         image_name = re.search(r'\|\s+' + vm_node_name + r"\s+\|\s+(.*?)\|",
  176                                 buf).group(1).strip()

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\setup_upgrade\test_upgrade_scon.py:
  126      print(univ_op)
  127:     latest_build_tag = re.search('binary_builds.*browse/(.+)', univ_op).\
  128          group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_cli.py:
   64      str_pattern = 'challenge generate(.*){}'.format(dut_serialno)
   65:     match = re.search(str_pattern, cmd_op)
   66      if match:

  475                                      replace("rvbd-testuser@", "root@")
  476:                                 match = re.search('ProxyCommand=nc -X '
  477                                                    'connect -x (.*):', val).\

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_connectivity.py:
  185              val = tunnel['ssh_help']
  186:             match = re.search(
  187                  'ProxyCommand=nc -X connect -x (.*):',

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_diverter.py:
  149      dns_output = cvm_shell.exec_command('nslookup ' + remote_host)
  150:     filter_host_ip = re.search('Address: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', # noqa
  151                                 dns_output)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_oa_cdl_update.py:
  747                                                      new_cdl_file)
  748:             match = re.search(error_msg, output.strip())
  749              if not match:

  759                                                      new_cdl_file)
  760:             match = re.search(error_msg, output.strip())
  761              if not match:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_ssh_tunnel.py:
  86                              val = tunnel['ssh_help']
  87:                             match = re.search('ProxyCommand=nc -X connect '
  88                                                '-x (.*):', val).group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_static_config.py:
  389                  continue
  390:             ipmatch = re.search(r'inet\s(?:addr:)*(\S+)', line)
  391              if ipmatch:

  394  
  395:             maskmatch = re.search(r'Mask:*\s*(\S+)', line, re.IGNORECASE)
  396              if maskmatch:

  405  
  406:             ipv6match = re.search(
  407                  r'inet6\saddr:\s([a-fA-F0-9:]+)/*(\S+)', line)

  413  
  414:             ethmatch = re.search(r'(?:(?:ether)|(?:HWaddr))\s(?:addr:)*(\S+)',
  415                                   line)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_tcpdump_on_cli.py:
  105      if state == 'RUNNING':
  106:         match = re.search(tcpdump_running_exp_str, output)
  107          if match:

  112      else:
  113:         match = re.search(tcpdump_not_running_exp_str, output)
  114          if match:

  208          logger.info("output of tcpdump command: {}".format(tcpdump_output))
  209:         match = re.search(exp_result, tcpdump_output)
  210          tcpdump_file = match.group(0)

  257              tcpdump_output = cli_instance.exec_command(tcpdump_cmd1)
  258:             match = re.search(exp_result, tcpdump_output)
  259              tcpdump_file = match.group(0)

  326          output = cli_instance.exec_command(tcpdump_stop_cmd)
  327:         match = re.search(tcpdump_stop_exp_result, output)
  328          if match:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\test_troubleshoot_tool.py:
   92          data = troubleshoot_info.split('\n')
   93:         match = re.search(exp_result, data[-1])
   94          troubleshoot_tar = match.group(0)

  146              data = troubleshoot_info.split('\n')
  147:             match = re.search(exp_result, data[-2])
  148              troubleshoot_tar = match.group(0)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\nodes.py:
  661  
  662:         match = re.search(exp_result, data[-1])
  663          troubleshoot_tar = match.group(0)

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\site_dns_lib.py:
  248      most_recent_content = lease_file_op.split("lease {")[-1]
  249:     m = re.search("option domain-name-servers (.*);", most_recent_content)
  250      if m:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_external.py:
  47          for fru in fru_list:
  48:             assert re.search("CXA-00[57]70-B020", fru['Chassis Part Number'])
  49              assert fru['Board Mfg'] == 'Advantech'

  51              assert fru['Product Name'] == 'DTATA'
  52:             assert re.search("FWA-3250-RB0[23]E?", fru['Product Part Number'])
  53      except AssertionError as e:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_local.py:
  46          for fru in fru_list:
  47:             assert re.search("CXA-00[57]70-B020", fru['Chassis Part Number'])
  48              assert fru['Board Mfg'] == 'Advantech'

  50              assert fru['Product Name'] == 'DTATA'
  51:             assert re.search("FWA-3250-RB0[23]E?", fru['Product Part Number'])
  52      except AssertionError as e:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_external.py:
   26      try:
   27:         assert re.search(r"\d+", info_dict['Record Count']), \
   28              info_dict['Record Count']
   29:         assert re.search(r"\d+ bytes", info_dict['Free Space']), \
   30              info_dict['Free Space']

   56          for op in status_list:
   57:             if re.search(("fan", op[0].lower()) and
   58                           op[1].lower() != 'no reading'):
   59:                 assert re.search(r"\d+ RPM", op[1]), op
   60      except AssertionError as e:

   70          for op in status_list:
   71:             if re.search(("temp", op[0].lower()) and
   72                           op[1].lower() != 'no reading'):
   73:                 assert re.search(r"\d+ degrees C", op[1]), op
   74      except AssertionError as e:

   84          for op in status_list:
   85:             if re.search(("hdd", op[0].lower()) and
   86                           op[1].lower() != 'no reading'):
   87:                 assert re.search(r"\d+ degrees C", op[1]), op
   88      except AssertionError as e:

   98          for op in status_list:
   99:             if re.search(("cpu_dimm*", op[0].lower()) and
  100                           op[1].lower() != 'no reading'):
  101:                 assert re.search(r"\d+ degrees C", op[1]), op
  102:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  103:                 assert re.search(r"^\d+\.?\d* Volts", op[1]), op
  104      except AssertionError as e:

  114          for op in status_list:
  115:             if re.search("power", op[0].lower()):
  116:                 assert re.search(r"\d+ Watts", op[1]), op
  117      except AssertionError as e:

  142                  assert op[2] == 'ok', op
  143:                 if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  144:                     assert re.search(r"\d+ degrees C", op[4]), op
  145      except AssertionError as e:

  156              assert op[2] == 'ok'
  157:             assert re.search(r"\d+\.\d+ Volts", op[4]), op
  158      except AssertionError as e:

  169              assert op[2] == 'ok'
  170:             assert re.search(r"\d+ RPM", op[4]), op
  171      except AssertionError as e:

  182              assert op[2] == 'ok'
  183:             if re.search(r"PSU\d+ Status", op[0]):
  184                  assert op[4].lower() == 'presence detected'
  185:             elif re.search(r"PSU\d+ Power", op[0]):
  186:                 assert re.search(r"\d+ Watts", op[4])
  187      except AssertionError as e:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_ipmb.py:
   44      try:
   45:         assert re.search(r'\d+', info_dict['Record Count']), \
   46              info_dict['Record Count']
   47:         assert re.search(r'\d+ bytes', info_dict['Free Space']), \
   48              info_dict['Free Space']

   63          for op in status_list:
   64:             if re.search("fan", op[0].lower()) and op[1] != 'no reading':
   65:                 assert re.search(r'\d+ RPM', op[1]), op
   66      except AssertionError as e:

   79          for op in status_list:
   80:             if re.search("temp", op[0].lower()) and op[1] != 'no reading':
   81:                 assert re.search(r'\d+ degrees C', op[1]), op
   82      except AssertionError as e:

   95          for op in status_list:
   96:             if re.search("hdd", op[0].lower()) and op[1] != 'no reading':
   97:                 assert re.search(r"\d+ degrees C", op[1]), op
   98      except AssertionError as e:

  111          for op in status_list:
  112:             if re.search(("cpu_dimm*", op[0].lower()) and
  113                           op[1].lower() != 'no reading'):
  114:                 assert re.search(r"\d+ degrees C", op[1]), op
  115:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  116:                 assert re.search(r"^\d+\.?\d* Volts", op[1]), op
  117      except AssertionError as e:

  130          for op in status_list:
  131:             if re.search("power", op[0].lower()) and op[1] != 'no reading':
  132:                 assert re.search(r"\d+ Watts", op[1]), op
  133      except AssertionError as e:

  165                      assert op[2] == 'ok', op
  166:                     if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  167:                         assert re.search(r"\d+ degrees C", op[4]), op
  168          except AssertionError as e:

  186                  assert op[2] == 'ok'
  187:                 assert re.search(r"\d+\.\d+ Volts", op[4]), op
  188          except AssertionError as e:

  205                  assert op[2] == 'ok'
  206:                 assert re.search(r"\d+ RPM", op[4]), op
  207          except AssertionError as e:

  224                  assert op[2] == 'ok'
  225:                 if re.search(r"PSU\d+ Status", op[0]):
  226                      assert op[4].lower() == 'presence detected'
  227:                 elif re.search(r"PSU\d+ Power", op[0]):
  228:                     assert re.search(r"\d+ Watts", op[4])
  229          except AssertionError as e:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_local.py:
   39      try:
   40:         assert re.search(r'\d+', info_dict['Record Count']), \
   41              info_dict['Record Count']
   42:         assert re.search(r'\d+ bytes', info_dict['Free Space']), \
   43              info_dict['Free Space']

   55          for op in status_list:
   56:             if re.search("fan", op[0].lower()) and op[1] != 'no reading':
   57:                 assert re.search(r'\d+ RPM', op[1]), op
   58      except AssertionError as e:

   68          for op in status_list:
   69:             if re.search(("temp", op[0].lower()) and
   70                           op[1].lower() != 'no reading'):
   71:                 assert re.search(r'\d+ degrees C', op[1]), op
   72      except AssertionError as e:

   82          for op in status_list:
   83:             if re.search("hdd", op[0].lower()) and op[1] != 'no reading':
   84:                 assert re.search(r'\d+ degrees C', op[1]), op
   85      except AssertionError as e:

   95          for op in status_list:
   96:             if re.search(("cpu_dimm*", op[0].lower()) and
   97                           op[1].lower() != 'no reading'):
   98:                 assert re.search(r'\d+ degrees C', op[1]), op
   99:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  100:                 assert re.search(r'^\d+\.?\d* Volts', op[1]), op
  101      except AssertionError as e:

  111          for op in status_list:
  112:             if re.search("power", op[0].lower()) and op[1] != 'no reading':
  113:                 assert re.search(r'\d+ Watts', op[1]), op
  114      except AssertionError as e:

  139                  assert op[2] == 'ok', op
  140:                 if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  141:                     assert re.search(r'\d+ degrees C', op[4]), op
  142      except AssertionError as e:

  154                  assert op[2] == 'ok', op
  155:                 assert re.search(r'\d+\.\d+ Volts', op[4]), op
  156      except AssertionError as e:

  167              assert op[2] == 'ok', op
  168:             assert re.search(r'\d+ RPM', op[4]), op
  169      except AssertionError as e:

  180              assert op[2] == 'ok', op
  181:             if re.search(r'PSU\d+ Status', op[0]):
  182                  assert op[4].lower() == 'presence detected'
  183:             elif re.search(r'PSU\d+ Power', op[0]):
  184:                 assert re.search(r'\d+ Watts', op[4])
  185      except AssertionError as e:

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_external.py:
   81          assert sel_info_dict['Entries'] == '3'
   82:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   83              sel_info_dict['Version']
   84:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   85              sel_info_dict['Entries']
   86:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
   87              sel_info_dict['Free Space']
   88:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
   89              sel_info_dict['Percent Used']

  102          assert sel_info_dict['Entries'] == '3'
  103:         assert re.search(r"^1.5", sel_info_dict['Version']), \
  104              sel_info_dict['Version']
  105:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  106              sel_info_dict['Entries']
  107:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  108              sel_info_dict['Free Space']
  109:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  110              sel_info_dict['Percent Used']

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_ipmb.py:
   94          assert sel_info_dict['Entries'] == '3'
   95:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   96              sel_info_dict['Version']
   97:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   98              sel_info_dict['Entries']
   99:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  100              sel_info_dict['Free Space']
  101:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  102              sel_info_dict['Percent Used']

  117          assert sel_info_dict['Entries'] == '3'
  118:         assert re.search(r"^1.5", sel_info_dict['Version']), \
  119              sel_info_dict['Version']
  120:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  121              sel_info_dict['Entries']
  122:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  123              sel_info_dict['Free Space']
  124:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  125              sel_info_dict['Percent Used']

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_local.py:
   90              assert sel_info_dict['Entries'] == '3'
   91:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   92              sel_info_dict['Version']
   93:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   94              sel_info_dict['Entries']
   95:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
   96              sel_info_dict['Free Space']
   97:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
   98              sel_info_dict['Percent Used']

  114              assert sel_info_dict['Entries'] == '4'
  115:         assert re.search("^1.5", sel_info_dict['Version']), \
  116              sel_info_dict['Version']
  117:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  118              sel_info_dict['Entries']
  119:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  120              sel_info_dict['Free Space']
  121:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  122              sel_info_dict['Percent Used']

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_set_ip_source.py:
  100          assert ip_dict['ip_source'] == 'dhcp'
  101:         assert re.search(r"(\d+\.){3}\d+", ip_dict['ip_source']), \
  102              ip_dict['ip_source']
  103:         assert re.search(r"(\d+\.){3}\d+", ip_dict['subnet_mask']), \
  104              ip_dict['subnet_mask']
  105:         assert re.search(r"(\d+\.){3}\d+", ip_dict['gateway']), \
  106              ip_dict['gateway']

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc_stress\test_bmc_stress_rios_power_cycle.py:
  141      proc_ipmi_stats = shell.exec_command(cmd)
  142:     if (re.search(r'sent_ipmb_command_errs:\s+\d{1,3}\s+',
  143                    proc_ipmi_stats) and
  144:             re.search(r'sent_lan_command_errs:\s+\d{1,3}\s+',
  145                        proc_ipmi_stats) and
  146:             re.search(r'retransmitted_lan_commands:\s+\d{1,3}\s+',
  147                        proc_ipmi_stats) and
  148:             re.search(r'timed_out_lan_commands:\s+\d{1,3}\s+',
  149                        proc_ipmi_stats) and
  150:             re.search(r'sent_lan_responses:\s+\d{1,3}\s+',
  151                        proc_ipmi_stats) and
  152:             re.search(r'handled_lan_responses:\s+\d{1,3}\s+',
  153                        proc_ipmi_stats) and
  154:             re.search(r'invalid_lan_responses:\s+\d{1,3}\s+',
  155                        proc_ipmi_stats) and
  156:             re.search(r'unhandled_lan_responses:\s+\d{1,3}\s+',
  157                        proc_ipmi_stats)):

  242          box_type = ipmitool_rios_lan.run("fru list")
  243:         if(re.search("2U", box_type)):
  244              logger.info("##### BLUEFIN-2U #########")

  262                                   "169.254.0.101"]
  263:         elif(re.search("1U", box_type)):
  264              logger.info("##### BLUEFIN-1U #########")

  328          mc_info = ipmitool_rios_lan.run("mc info")
  329:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  330          mc_info_status["rios_aux"][0] = mc_info_status["rios_aux"][0] + 1

  348          mc_info = ipmitool_rios.run("mc info")
  349:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  350          mc_info_status["rios_local"][0] = mc_info_status["rios_local"][0] + 1

  369          mc_info = ipmitool_vsp_lan.run("mc info")
  370:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  371          mc_info_status["vsp_aux"][0] = mc_info_status["vsp_aux"][0] + 1

  389          mc_info = ipmitool_vsp.run("mc info")
  390:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  391          mc_info_status["vsp_ipmb"][0] = mc_info_status["vsp_ipmb"][0] + 1

  412          for op in status_list:
  413:             if (re.search("no reading", op[1]) or
  414:                     re.search("Not Readable", op[1])):
  415                  assert op[2] == "ns", op

  438          for op in status_list:
  439:             if (re.search("no reading", op[1]) or
  440:                     re.search("Not Readable", op[1])):
  441                  assert op[2] == "ns", op

  466          for op in status_list:
  467:             if (re.search("no reading", op[1]) or
  468:                     re.search("Not Readable", op[1])):
  469                  assert op[2] == "ns", op

  494          for op in status_list:
  495:             if (re.search("no reading", op[1]) or
  496:                     re.search("Not Readable", op[1])):
  497                  assert op[2] == "ns", op

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc_stress\test_bmc_stress.py:
  137      proc_ipmi_stats = shell.exec_command(cmd)
  138:     if (re.search(r'sent_ipmb_command_errs:\s+\d{1,3}\s+',
  139                    proc_ipmi_stats) and
  140:             re.search(r'sent_lan_command_errs:\s+\d{1,3}\s+',
  141                        proc_ipmi_stats) and
  142:             re.search(r'retransmitted_lan_commands:\s+\d{1,3}\s+',
  143                        proc_ipmi_stats) and
  144:             re.search(r'timed_out_lan_commands:\s+\d{1,3}\s+',
  145                        proc_ipmi_stats) and
  146:             re.search(r'sent_lan_responses:\s+\d{1,3}\s+',
  147                        proc_ipmi_stats) and
  148:             re.search(r'handled_lan_responses:\s+\d{1,3}\s+',
  149                        proc_ipmi_stats) and
  150:             re.search(r'invalid_lan_responses:\s+\d{1,3}\s+',
  151                        proc_ipmi_stats) and
  152:             re.search(r'unhandled_lan_responses:\s+\d{1,3}\s+',
  153                        proc_ipmi_stats)):

  237          box_type = ipmitool_rios_lan.run("fru list")
  238:         if(re.search("2U", box_type)):
  239              logger.info("##### BLUEFIN-2U #########")

  257                                   "169.254.0.101"]
  258:         elif(re.search("1U", box_type)):
  259              logger.info("##### BLUEFIN-1U #########")

  354              mc_info = ipmitool_rios_lan.run("mc info")
  355:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  356              mc_info_status["rios_aux"][0] = mc_info_status["rios_aux"][0] + 1

  374              mc_info = ipmitool_rios.run("mc info")
  375:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  376              mc_info_status["rios_local"][0] = \

  397              mc_info = ipmitool_vsp_lan.run("mc info")
  398:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  399              mc_info_status["vsp_aux"][0] = mc_info_status["vsp_aux"][0] + 1

  417              mc_info = ipmitool_vsp.run("mc info")
  418:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  419              mc_info_status["vsp_ipmb"][0] = mc_info_status["vsp_ipmb"][0] + 1

  440              for op in status_list:
  441:                 if (re.search("no reading", op[1]) or
  442:                         re.search("Not Readable", op[1])):
  443                      assert op[2] == "ns", op

  466              for op in status_list:
  467:                 if (re.search("no reading", op[1]) or
  468:                         re.search("Not Readable", op[1])):
  469                      assert op[2] == "ns", op

  496              for op in status_list:
  497:                 if (re.search("no reading", op[1]) or
  498:                         re.search("Not Readable", op[1])):
  499                      assert op[2] == "ns", op

  524              for op in status_list:
  525:                 if (re.search("no reading", op[1]) or
  526:                         re.search("Not Readable", op[1])):
  527                      assert op[2] == "ns", op

portfolio-system-tests\new\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\hwtool\tests_hwtool.py:
  1173          logger.info("Actual Output: [" + actual_output + "]")
  1174:         elements = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)", actual_output)
  1175          # Validating CPU core count

  1265              # Verifying Slots
  1266:             elements = re.search(r"Slot\s+(\d+):\s\.{10}\s([^,]*),\s(.*)",
  1267                                   line)

  1275                  # Verifying Hardware revision
  1276:                 elements = re.search(r"Hardware revision:\s+([\d\D]+)", line)
  1277                  if elements is not None:

  1279                  else:
  1280:                     elements = re.search(r"Mainboard:\s[^,]*,\s(.*)", line)
  1281                      if elements is not None:

  1338              system_section = section
  1339:     elements = re.search(r".*Product\s*:\s*(.*)", system_section)
  1340      actual_motherboard_number = elements.group(1)

  1445          for line in lines:
  1446:             if re.search(r"disk.*", line) is not None:
  1447                  elements = line.split()

  1458          for line in lines:
  1459:             if re.search(r"\w", line):
  1460                  elements = line.split()

portfolio-system-tests\new\portfolio_system_tests\legacy_exchange_tests\tests\test_allocation_health.py:
   64  
   65:         match = re.search(r'received, (?P<loss>\d+.*)\s*% packet loss,',
   66                            output)

  145                r'\s*% loss\)')
  146:     match = re.search(target, output)
  147      if not match:

portfolio-system-tests\new\portfolio_system_tests\legacy_exchange_tests\tests\test_smoke_mess.py:
  38      ITEMS_RE = r'ItemsInFolder\s+-------------\s+(?P<items>\d+)'
  39:     match = re.search(ITEMS_RE, output)
  40      return int(match.group('items'))

portfolio-system-tests\new\portfolio_system_tests\legacy_gluon\libs\__init__.py:
  360      # Example: "hostname":"XNCC58DC4E4D4408",
  361:     sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  362      if not sobj:

portfolio-system-tests\new\portfolio_system_tests\legacy_gluon\tests\test_firewall_rules_after_failover_vgw.py:
  127      regex = re.escape(str1) + r'\n(.*)$'
  128:     sobj1 = re.search(regex, output, re.MULTILINE | re.DOTALL)
  129      if sobj1:

  182      # Format of uptime: 35d  0h  54m
  183:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  184      if not sobj:

portfolio-system-tests\new\portfolio_system_tests\legacy_gluon\tests\test_firewall_rules_after_reboot_vgw.py:
  126      regex = re.escape(str1) + r'\n(.*)$'
  127:     sobj1 = re.search(regex, output, re.MULTILINE | re.DOTALL)
  128      if sobj1:

  191          # Example: "hostname":"XNCC58DC4E4D4408",
  192:         sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  193          if not sobj:

  223      # Format of uptime: 35d  0h  54m
  224:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  225      if not sobj:

portfolio-system-tests\new\portfolio_system_tests\legacy_gluon\tests\test_internet_and_site_to_site.py:
  123      # Example: "hostname":"XNCC58DC4E4D4408",
  124:     sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  125      if not sobj:

  363      # Resolving facebook.com (facebook.com)... 31.13.90.36, 2a03..
  364:     sobj = re.search(r'\(facebook\.com\)\.\.\.\s+(.*),', lines[2])
  365      if sobj:

  407      # Resolving youtube.com (youtube.com)... 216.58.194.206, 2607
  408:     sobj = re.search(r'\(youtube\.com\)\.\.\.\s+(.*),', lines[2])
  409      if sobj:

  450      # Format of uptime: 35d  0h  54m
  451:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  452      if not sobj:

portfolio-system-tests\new\portfolio_system_tests\legacy_gluon\tests\test_overnight_failover_pingpong.py:
  78  
  79:     match = re.search(r'(?<=\()\S+?(?=\) port \d+)', output)
  80      if match:

portfolio-system-tests\new\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\conftest.py:
  397  
  398:     if re.search("different_unique_ib_ob", test_case):
  399          logger.info("[INFO]: cleanup after different_unique_ib_ob")

  496          for line in profile_data.raw.split("\n"):
  497:             result = re.search(r"(\*\w+\*)\s+\d+\s+(\d+)\s+(\d+)",
  498                                 profile_data.raw)

  518      """
  519:     if re.search("same_default_ib_ob", test_case):
  520          init_qos_device_configurator.config.manage_sites(7)
  521          init_qos_device_configurator.config.manage_sites(8)
  522:     elif re.search("unique_ib_default_ob", test_case):
  523          init_qos_device_configurator.config.manage_sites(7)
  524:     elif re.search("default_ib_unique_ob", test_case):
  525          init_qos_device_configurator.config.manage_sites(8)
  526:     elif re.search("different_unique_ib_ob", test_case):
  527          init_qos_device_configurator.config.manage_profiles(9)

  549  
  550:     if re.search("same_default|default_ob", test_case):
  551:         if re.search("^.*DSCP_P$", test_case):
  552              init_qos_device_configurator.config.manage_classes(21)
  553  
  554:         if re.search("^.*DSCP_L$", test_case):
  555              init_qos_device_configurator.config.manage_classes(38)
  556  
  557:         if re.search("^.*DSCP_R$", test_case):
  558              init_qos_device_configurator.config.manage_rules(3)
  559  
  560:         if re.search("^.*DSCP_PL$", test_case):
  561              init_qos_device_configurator.config.manage_classes(21)

  563  
  564:         if re.search("^.*DSCP_PR$", test_case):
  565              init_qos_device_configurator.config.manage_classes(21)

  567  
  568:         if re.search("^.*DSCP_LR$", test_case):
  569              init_qos_device_configurator.config.manage_classes(38)

  571  
  572:         if re.search("^.*DSCP_PLR$", test_case):
  573              init_qos_device_configurator.config.manage_classes(21)

  577      else:
  578:         if re.search("^.*DSCP_P$", test_case):
  579              init_qos_device_configurator.config.manage_classes(26)
  580  
  581:         if re.search("^.*DSCP_L$", test_case):
  582              init_qos_device_configurator.config.manage_classes(34)
  583  
  584:         if re.search("^.*DSCP_R$", test_case):
  585              init_qos_device_configurator.config.manage_rules(5)
  586  
  587:         if re.search("^.*DSCP_PL$", test_case):
  588              init_qos_device_configurator.config.manage_classes(26)

  590  
  591:         if re.search("^.*DSCP_PR$", test_case):
  592              init_qos_device_configurator.config.manage_classes(26)

  594  
  595:         if re.search("^.*DSCP_LR$", test_case):
  596              init_qos_device_configurator.config.manage_classes(34)

  598  
  599:         if re.search("^.*DSCP_PLR$", test_case):
  600              init_qos_device_configurator.config.manage_classes(26)

  622  
  623:     if re.search("same_default|default_ob", test_case):
  624:         if re.search("^.*DSCP_P$", test_case):
  625              init_qos_device_configurator.config.manage_classes(25)
  626  
  627:         if re.search("^.*DSCP_L$", test_case):
  628              init_qos_device_configurator.config.manage_classes(39)
  629  
  630:         if re.search("^.*DSCP_R$", test_case):
  631              init_qos_device_configurator.config.manage_rules(4)
  632  
  633:         if re.search("^.*DSCP_PL$", test_case):
  634              init_qos_device_configurator.config.manage_classes(25)

  636  
  637:         if re.search("^.*DSCP_PR$", test_case):
  638              init_qos_device_configurator.config.manage_classes(25)

  640  
  641:         if re.search("^.*DSCP_LR$", test_case):
  642              init_qos_device_configurator.config.manage_classes(39)

  644  
  645:         if re.search("^.*DSCP_PLR$", test_case):
  646              init_qos_device_configurator.config.manage_classes(25)

  650      else:
  651:         if re.search("^.*DSCP_P$", test_case):
  652              init_qos_device_configurator.config.manage_classes(30)
  653  
  654:         if re.search("^.*DSCP_L$", test_case):
  655              init_qos_device_configurator.config.manage_classes(35)
  656  
  657:         if re.search("^.*DSCP_R$", test_case):
  658              init_qos_device_configurator.config.manage_rules(6)
  659  
  660:         if re.search("^.*DSCP_PL$", test_case):
  661              init_qos_device_configurator.config.manage_classes(30)

  663  
  664:         if re.search("^.*DSCP_PR$", test_case):
  665              init_qos_device_configurator.config.manage_classes(30)

  667  
  668:         if re.search("^.*DSCP_LR$", test_case):
  669              init_qos_device_configurator.config.manage_classes(35)

  671  
  672:         if re.search("^.*DSCP_PLR$", test_case):
  673              init_qos_device_configurator.config.manage_classes(30)

portfolio-system-tests\new\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_inbound_qos_dscp_full_combinations.py:
   89      try:
   90:         if re.search("same_default|default_ob", test_case):
   91              init_qos_device_configurator.config.manage_classes(37)
   92  
   93:             if re.search("unique_ib_default_ob", test_case):
   94                  qos = init_qos_device_configurator.config.\

  119  
  120:             if re.search("^.*DSCP_P$", test_case):
  121                  expected_ob_qos_dscp = 0
  122  
  123:             if re.search("^.*DSCP_L$", test_case):
  124                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  125  
  126:             if re.search("^.*DSCP_R$", test_case):
  127                  expected_ob_qos_dscp = default_outbound_dscp_rule
  128  
  129:             if re.search("^.*DSCP_PL$", test_case):
  130                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  131  
  132:             if re.search("^.*DSCP_PR$", test_case):
  133                  expected_ob_qos_dscp = default_outbound_dscp_rule
  134  
  135:             if re.search("^.*DSCP_LR$", test_case):
  136                  expected_ob_qos_dscp = default_outbound_dscp_rule
  137  
  138:             if re.search("^.*DSCP_PLR$", test_case):
  139                  expected_ob_qos_dscp = default_outbound_dscp_rule

  143  
  144:             if re.search("default_ib_unique_ob", test_case):
  145                  qos = init_qos_device_configurator.config.\

  148  
  149:             elif re.search("different_unique_ib_ob", test_case):
  150                  qos = init_qos_device_configurator.config.\

  175  
  176:             if re.search("^.*DSCP_P$", test_case):
  177                  expected_ob_qos_dscp = 0
  178  
  179:             if re.search("^.*DSCP_L$", test_case):
  180                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  181  
  182:             if re.search("^.*DSCP_R$", test_case):
  183                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  184  
  185:             if re.search("^.*DSCP_PL$", test_case):
  186                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  187  
  188:             if re.search("^.*DSCP_PR$", test_case):
  189                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  190  
  191:             if re.search("^.*DSCP_LR$", test_case):
  192                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  193  
  194:             if re.search("^.*DSCP_PLR$", test_case):
  195                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  281  
  282:         if re.search("same_default|default_ob", test_case):
  283              init_qos_device_configurator.config.manage_rules(7)

portfolio-system-tests\new\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_outbound_qos_dscp_full_combinations.py:
   89      try:
   90:         if re.search("same_default|default_ob", test_case):
   91              init_qos_device_configurator.config.manage_classes(37)

  113  
  114:             if re.search("^.*DSCP_P$", test_case):
  115                  expected_ob_qos_dscp = 0
  116  
  117:             if re.search("^.*DSCP_L$", test_case):
  118                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  119  
  120:             if re.search("^.*DSCP_R$", test_case):
  121                  expected_ob_qos_dscp = default_outbound_dscp_rule
  122  
  123:             if re.search("^.*DSCP_PL$", test_case):
  124                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  125  
  126:             if re.search("^.*DSCP_PR$", test_case):
  127                  expected_ob_qos_dscp = default_outbound_dscp_rule
  128  
  129:             if re.search("^.*DSCP_LR$", test_case):
  130                  expected_ob_qos_dscp = default_outbound_dscp_rule
  131  
  132:             if re.search("^.*DSCP_PLR$", test_case):
  133                  expected_ob_qos_dscp = default_outbound_dscp_rule

  158  
  159:             if re.search("^.*DSCP_P$", test_case):
  160                  expected_ob_qos_dscp = 0
  161  
  162:             if re.search("^.*DSCP_L$", test_case):
  163                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  164  
  165:             if re.search("^.*DSCP_R$", test_case):
  166                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  167  
  168:             if re.search("^.*DSCP_PL$", test_case):
  169                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  170  
  171:             if re.search("^.*DSCP_PR$", test_case):
  172                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  173  
  174:             if re.search("^.*DSCP_LR$", test_case):
  175                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  176  
  177:             if re.search("^.*DSCP_PLR$", test_case):
  178                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  250  
  251:         if re.search("same_default|default_ob", test_case):
  252              init_qos_device_configurator.config.manage_rules(7)

portfolio-system-tests\new\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_qos_device_all_classification.py:
  213      """
  214:     if re.search('-sh', test_case):
  215          check_qos_on_IC = 0

  217  
  218:     elif re.search('-ic', test_case):
  219          check_qos_on_IC = 1

  224  
  225:     if re.search('-IN', test_case):
  226          QoS_Flags = 1

  233  
  234:     elif re.search('-OUT', test_case):
  235          QoS_Flags = 0

  242  
  243:     if re.search('-UniqueSite', test_case):
  244          is_UniqueSite = 1

  247  
  248:     elif re.search('-DefaultSite', test_case):
  249          is_UniqueSite = 0

  294      try:
  295:         if re.search('same_unique_ib_ob', test_case):
  296              # The same unique profile is used for Inbound and outbound.

  309  
  310:         elif re.search('same_default_ib_ob', test_case):
  311              # Default profile is used for both Inbound and outbound traffic.

  325  
  326:         elif re.search('default_ib_unique_ob', test_case):
  327              # Default profile is used for inbound and

  342  
  343:         elif re.search('unique_ib_default_ob', test_case):
  344              # Default profile is used for outbound and

  358  
  359:         elif re.search('different_unique_ib_ob', test_case):
  360              # Different unique profiles for outbound and inbound traffic.

  431              # Checking for optimized or passthrough traffic
  432:             if re.search('-noOpt', test_case):
  433                  verify_opt(sh_resource=test_objects.client_sh,

  439  
  440:             elif re.search('-Opt', test_case):
  441                  verify_opt(sh_resource=test_objects.client_sh,

portfolio-system-tests\new\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_qos_dscp_full_combinations.py:
   88      try:
   89:         if re.search("same_default|default_ob", test_case):
   90              init_qos_device_configurator.config.manage_classes(37)
   91  
   92:             if re.search("unique_ib_default_ob", test_case):
   93                  qos = init_qos_device_configurator.config.\

  123  
  124:             if re.search("^.*DSCP_P$", test_case):
  125                  expected_ob_qos_dscp = 0
  126  
  127:             if re.search("^.*DSCP_L$", test_case):
  128                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  129  
  130:             if re.search("^.*DSCP_R$", test_case):
  131                  expected_ob_qos_dscp = default_outbound_dscp_rule
  132  
  133:             if re.search("^.*DSCP_PL$", test_case):
  134                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  135  
  136:             if re.search("^.*DSCP_PR$", test_case):
  137                  expected_ob_qos_dscp = default_outbound_dscp_rule
  138  
  139:             if re.search("^.*DSCP_LR$", test_case):
  140                  expected_ob_qos_dscp = default_outbound_dscp_rule
  141  
  142:             if re.search("^.*DSCP_PLR$", test_case):
  143                  expected_ob_qos_dscp = default_outbound_dscp_rule

  147  
  148:             if re.search("default_ib_unique_ob", test_case):
  149                  qos = init_qos_device_configurator.config.\

  152  
  153:             elif re.search("different_unique_ib_ob", test_case):
  154                  qos = init_qos_device_configurator.config.\

  184  
  185:             if re.search("^.*DSCP_P$", test_case):
  186                  expected_ob_qos_dscp = 0
  187  
  188:             if re.search("^.*DSCP_L$", test_case):
  189                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  190  
  191:             if re.search("^.*DSCP_R$", test_case):
  192                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  193  
  194:             if re.search("^.*DSCP_PL$", test_case):
  195                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  196  
  197:             if re.search("^.*DSCP_PR$", test_case):
  198                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  199  
  200:             if re.search("^.*DSCP_LR$", test_case):
  201                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  202  
  203:             if re.search("^.*DSCP_PLR$", test_case):
  204                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  300  
  301:         if re.search("same_default|default_ob", test_case):
  302              init_qos_device_configurator.config.manage_rules(7)

portfolio-system-tests\new\portfolio_system_tests\legacy_netint_tests\tests\legacy\Securetransport\sectp_ms2_nat_integ.py:
  31      """
  32:     m = re.search(r"Runner - Tests planned:\s+(\d+)", log)
  33      planned_tc = m.group(1)
  34:     m = re.search(r"Runner - Tests passed:\s+(\d+)", log)
  35      passed_tc = m.group(1)

  47      """
  48:     match = re.search(r"1 passed in (\d+)", log)
  49      if match:

portfolio-system-tests\new\portfolio_system_tests\legacy_ns\service_chain_manager\service_chain_manager\test\orclibs\traffic_parser.py:
  51      hwaddr = None
  52:     eth_match = re.search(r'(ether|HWaddr)\s(?:addr:)*(\S+)', output)
  53      if eth_match:

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\ibt\tests\Guest_Zone_Support\test_local_internet_breakout.py:
  79      for line in output_lines:
  80:         maskmatch = re.search(r'\s' + interface, line, re.IGNORECASE)
  81          if maskmatch:

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\cf3\DHCP_DNS\test_DHCP_relay_via_overlay_to_DC.py:
   90      for zone in zones:
   91:         if re.search(site_1['name'], zone.site):
   92              branch_net = zone.networks[0]

  130          for zone in zones:
  131:             if re.search(site_1['name'], zone.site):
  132                  configurator.scm_actor.config.change_network(

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\cf3\QoS\test_aggregate_traffic_with_mixed_traffic_class.py:
  115      for line in output.split("\n"):
  116:         bandwidth = re.search(r'\d+\.\d+mbps', line)
  117          if not bandwidth:

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_add_new_tep_ips_in_dc_uplinks.py:
  205          for dcuplink in dc_old_wan_teps:
  206:             if re.search('Internet', dcuplink):
  207                  public_ipv4 = str(resources.dc_public.cidr.ip)

  266          for dcuplink in dc_old_wan_teps:
  267:             if re.search('Internet', dcuplink):
  268                  public_ipv4 = str(resources.dc_public.cidr.ip)

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_data_ports_poweroff_update.py:
  215      for port in data_ports:
  216:         if re.search('PORT3', port.id, flags=re.IGNORECASE) or \
  217:                 re.search('PORT4', port.id, flags=re.IGNORECASE):
  218              resources.scm_actor.change_port(

  226          for port in data_ports:
  227:             if re.search('PORT3', port.id, flags=re.IGNORECASE) or \
  228:                     re.search('PORT4', port.id, flags=re.IGNORECASE):
  229                  resources.scm_actor.change_port(

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover_CF3.py:
  235      for zone in zone_list:
  236:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  237              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  251      for uplink in uplink_list:
  252:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  253:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  254                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  379          for zone in zones_list:
  380:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  381                  obj_added_zone = zone

  399                  for custom_app in custom_apps:
  400:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  401                                   flags=re.IGNORECASE):

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover.py:
  237      for zone in zone_list:
  238:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  239              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  253      for uplink in uplink_list:
  254:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  255:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  256                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  388          for zone in zones_list:
  389:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  390                  obj_added_zone = zone

  408                  for custom_app in custom_apps:
  409:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  410                                   flags=re.IGNORECASE):

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_leaf_site_checking_in_site_pool.py:
  440      for site in sites_lists:
  441:         if re.search('HQ', site.name):
  442              hq_site_name = site.name

  467          for dc_uplink in dc_uplinks:
  468:             if re.search(INTERNET,
  469                           dc_uplink.wan,

  709          for dc_uplink in dc_uplinks:
  710:             if re.search(INTERNET,
  711                           dc_uplink.wan,

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch_CF3.py:
  135      for zone in zone_list:
  136:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  137              zone_network = scm_actor.get_network(zone.networks[0])

  146      for uplink in uplink_list:
  147:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  148:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  149                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  176          for zone in zones_list:
  177:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  178                  obj_added_zone = zone

  192                  for custom_app in custom_apps:
  193:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  194                                   flags=re.IGNORECASE):

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch.py:
  135      for zone in zone_list:
  136:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  137              zone_network = scm_actor.get_network(zone.networks[0])

  146      for uplink in uplink_list:
  147:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  148:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  149                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  176          for zone in zones_list:
  177:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  178                  obj_added_zone = zone

  192                  for custom_app in custom_apps:
  193:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  194                                   flags=re.IGNORECASE):

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_size_change_for_site_moves.py:
  445      for site in sites_lists:
  446:         if re.search('HQ', site.name):
  447              hq_site_name = site.name

  473          for dc_uplink in dc_uplinks:
  474:             if re.search(INTERNET,
  475                           dc_uplink.wan,

  758          for dc_uplink in dc_uplinks:
  759:             if re.search(INTERNET,
  760                           dc_uplink.wan,

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch_CF3.py:
  264      for zone in zone_list:
  265:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  266              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  280      for uplink in uplink_list:
  281:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  282:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  283                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  402          for zone in zones_list:
  403:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  404                  obj_added_zone = zone

  422                  for custom_app in custom_apps:
  423:                     if re.search('CAT_CUSTOM_UDP',
  424                                   custom_app.name,

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch.py:
  264      for zone in zone_list:
  265:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  266              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  280      for uplink in uplink_list:
  281:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  282:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  283                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  403          for zone in zones_list:
  404:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  405                  obj_added_zone = zone

  423                  for custom_app in custom_apps:
  424:                     if re.search(
  425                          'CAT_CUSTOM_UDP',

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_dc_uplink.py:
  259      for dc_uplink in dc_uplinks:
  260:         if re.search(WAN,
  261                       dc_uplink.wan,

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_wan_CF3.py:
  304      for zone in zone_list:
  305:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  306              zone_obj = copy.copy(zone)

  317      for uplink in uplink_list:
  318:         if re.search(WAN, uplink.wan, flags=re.IGNORECASE):
  319              branch_name = test_objects.scm_actor.get_site(

  457          for wan_data in wans:
  458:             if re.search(WAN, wan_data.name, flags=re.IGNORECASE):
  459                  wan_id = wan_data.id

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_wan.py:
  308      for uplink in uplink_list:
  309:         if re.search(WAN, uplink.wan, flags=re.IGNORECASE):
  310              branch_name = test_objects.scm_actor.get_site(

  440          for wan_data in wans:
  441:             if re.search(WAN, wan_data.name, flags=re.IGNORECASE):
  442                  wan_id = wan_data.id

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone_CF3.py:
  193      output = shell.exec_command("cat /var/last_received_cdl.yaml")
  194:     match = re.search('subnet: ' + ipv4, output, flags=re.IGNORECASE)
  195      if match:

  209          output = shell.exec_command("ip rule list")
  210:         match = re.search(ipv4, output)
  211          if match:

  244      for zone in zone_list:
  245:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  246              # Getting old zone ip

  378          for custom_app in custom_apps:
  379:             if re.search('CAT_CUSTOM_UDP', custom_app.name,
  380                           flags=re.IGNORECASE):

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone.py:
  195      output = shell.exec_command("cat /var/last_received_cdl.yaml")
  196:     match = re.search('subnet: ' + ipv4, output, flags=re.IGNORECASE)
  197      if match:

  209          output = shell.exec_command("ip rule list")
  210:         match = re.search(ipv4, output)
  211          if match:

  245      for zone in zone_list:
  246:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  247              # Getting old zone ip

  379          for custom_app in custom_apps:
  380:             if re.search(
  381                  'CAT_CUSTOM_UDP',

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_uplink_wantype.py:
  357          # Example old_wan_name='Wan1',dc_uplink.wan='wan-Wan1-e63d40e499c3f0ab'
  358:         if re.search(old_wan_name,
  359                       dc_uplink.wan,

  395          # path_rule.path_preference[0]='wan-Wan1-e63d40e499c3f0ab'
  396:         if re.search(wan_name,
  397                       path_rule.path_preference[0],

  439          # Example uplink.name: "Wan1_Uplink"
  440:         if re.search(r'\bWan1_Uplink\b',
  441                       uplink.name,

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_wan_uplink_ipaddress.py:
  284      for uplink in uplink_list:
  285:         if re.search(WAN, uplink.name, flags=re.IGNORECASE):
  286              return uplink.name

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_zone_for_branch.py:
  181              for network_obj in network_list:
  182:                 if re.search(BRANCH, network_obj.site):
  183                      return network_obj

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_change_panther_db_address.py:
  147      for route in ic_ip_routes:
  148:         if re.search(network, route):
  149              flag = True

  161      for route in ic_ip_routes:
  162:         if re.search(network, route):
  163              flag = False

  279      for cluster_obj in clusters:
  280:         if re.search('Cluster1', cluster_obj.name, flags=re.IGNORECASE):
  281              old_proxy_ip = cluster_obj.proxy_ip

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_check_route_table.py:
  115      for route in ic_ip_routes:
  116:         if re.search(network, route):
  117              flag = True

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_int_service_restart.py:
  166      result = ic.show_info().raw
  167:     if re.search(status, str(result), flags=re.IGNORECASE):
  168          flag = True

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_modify_branch_subnet.py:
  207              for network_obj in network_list:
  208:                 if re.search(BRANCH, network_obj.site):
  209                      return network_obj

  225      for route in ic_ip_routes:
  226:         if re.search(network, route):
  227              flag = True

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\services\test_symmetrical_nat_port_dynamic_change.py:
  139      for uplink in uplink_list:
  140:         if re.search(r'\bWan1_Uplink\b',
  141                       uplink.name,

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_as_mismatch.py:
  126              shell.exec_command("grep remote_as /var/last_received_cdl.yaml")
  127:         hold = re.search('remote_as: 200', output)
  128          logger.info(output)

  167      logger.info(output)
  168:     holdtime = re.search('remote_as: 100', output)
  169      assert holdtime

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_nondefaults.py:
  124              "grep hold_time /var/last_received_cdl.yaml")
  125:         hold = re.search('hold_time: 10', output)
  126          logger.info(output)

  129              "grep keepalive_time /var/last_received_cdl.yaml")
  130:         keep = re.search('keepalive_time: 80', output)
  131          assert keep

  171      logger.info(output)
  172:     holdtime = re.search('hold_time: 60', output)
  173      assert holdtime

  175          "grep keepalive_time /var/last_received_cdl.yaml")
  176:     keep = re.search('keepalive_time: 180', output)
  177      assert keep

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_match.py:
  163              "grep password /var/last_received_cdl.yaml")
  164:         pword = re.search('password: thepassword', output)
  165          logger.info(output)

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_mismatch.py:
  139              "grep password /var/last_received_cdl.yaml")
  140:         pword = re.search('password: password', output)
  141          logger.info(output)

  189      logger.info(output)
  190:     pword = re.search('password: null', output)
  191      assert pword

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_ibgp_peering_on_wdr1_fails.py:
  327      for network in networks:
  328:         if not re.search('HQ', network.site):
  329              network_list.append(network.netv4)

  335          for subnet in subnet_splitted_list:
  336:             if not re.search(str(subnet), network, re.IGNORECASE):
  337                  higher_subnet_list.append(str(subnet))

portfolio-system-tests\new\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_subnet_splitting.py:
  227      for cluster_obj in clusters:
  228:         if re.search('Cluster1', cluster_obj.name, flags=re.IGNORECASE):
  229              cluster_id = cluster_obj.id

  288      for network in networks:
  289:         if not re.search('HQ', network.site):
  290              network_list.append(network.netv4)

  296          for subnet in subnet_splitted_list:
  297:             if not re.search(str(subnet), network, re.IGNORECASE):
  298                  higher_subnet_list.append(str(subnet))

portfolio-system-tests\new\portfolio_system_tests\legacy_scm_tests\legacy_tests\test_gw_via_rest\test_gw_via_rest.py:
  114      for uplink in uplinks:
  115:         if re.search('Internet', uplink.wan):
  116              continue

  204          uplink = scm_actor.config.get_uplink(uplink_id)
  205:         if re.search('Internet', uplink.wan):
  206              continue

portfolio-system-tests\new\portfolio_system_tests\legacy_shm_tests\shm_helper.py:
  122              # command output
  123:             app_content = re.search(search_pattern, cmd_output, re.DOTALL) \
  124                  .group(1).strip()

  142                  application_map['dest_port'] = int(dest[1])
  143:                 application_map['app_id'] = int(re.search(".*snoopy_app="
  144                                                  "(\\d+)", app).group(1)

  274              # from command output
  275:             status = re.search(search_pattern, cmd_output) \
  276                  .group(1).strip()

  302              # from command output
  303:             policy = re.search(search_pattern, cmd_output) \
  304                  .group(1).strip()

  379              wait_until_complete(timeout=WAIT_900_SECS)
  380:         result = re.search("\\[PASS\\]:", cmd_output)
  381  

  424          search_pattern = r'{(.*?)}'
  425:         product_code = re.search(search_pattern, cmd_output, re.DOTALL) \
  426              .group(1).strip()

  441          try:
  442:             return re.search(search_pattern, cmd_output, re.DOTALL) \
  443                  .group(1).strip()

portfolio-system-tests\new\portfolio_system_tests\legacy_shm_tests\zak\tests\conftest.py:
  180          try:
  181:             frmt_op = re.search(r"(.*?)Aliases", output,
  182                                  re.DOTALL).group(1).strip()

  187  
  188:         m = re.search("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*$", output)
  189          return (m.group(1))

portfolio-system-tests\new\portfolio_system_tests\legacy_shsaas_tests\tests\portal\test_allsaas_sku.py:
   63          portal_sca.action.add_platform_to_sku(SKU, 'noexist')
   64:     assert re.search("404", str(err404.value)) is not None
   65      with pytest.raises(VerificationError):

   78          portal_sca.action.add_platform_to_sku('noexist', PLATFORM)
   79:     assert re.search("404", str(err404.value)) is not None
   80      with pytest.raises(UnexpectedOutput) as another404:
   81          portal_sca.verification.verify_platforms_sku('noexist', PLATFORM)
   82:     assert re.search("404", str(another404.value)) is not None
   83  

   94          portal_sca.verification.verify_platforms_sku('nonexist', [PLATFORM])
   95:     assert re.search("404", str(err404.value)) is not None
   96  

  107          portal_sca.action.delete_platform_from_sku('noexist', PLATFORM)
  108:     assert re.search("404", str(err404.value)) is not None
  109  

  122              portal_sca.action.delete_platform_from_sku(SKU, valid_platform)
  123:         assert re.search("404", str(err404.value)) is not None
  124  

portfolio-system-tests\new\portfolio_system_tests\legacy_shsaas_tests\tests\portal\test_platforms.py:
  243                                         test_params.send_beta_fields)
  244:     assert re.search("400", str(err400.value)) is not None
  245  

  373              test_params.send_beta_fields)
  374:     assert re.search("400", str(err400.value)) is not None
  375  

portfolio-system-tests\new\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_hostlabel.py:
  228              # Extract class b address from resolved ips
  229:             subnet_extract = re.search(r"(^\d{1,3}\.\d{1,3})*",
  230                                         ip_address)

portfolio-system-tests\new\portfolio_system_tests\legacy_shsaas_tests\tests\SH\sepia\conftest.py:
   88      # get the md5 checksum value
   89:     checksum = re.search(r'([0-9a-fA-F]+)\s+', output)
   90      if (not checksum):

   98      # extract the filename from url for checksum
   99:     match_obj = re.search("//.*/(.*)$", url)
  100      server_file = SERVER_FILE_LOCATION + match_obj.group(1)

  136                  # Extract class A address from resolved ips
  137:                 subnet_extract = re.search(r"(^\d{1,3}\.)",
  138                                             ip_address)

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\scripts\connect_to_scc.py:
   61          cmc_version_string = cmc_cli.exec_command('show info')
   62:         cmc_version = re.search(
   63              r'Version:.*',

   65                  'Version:', '').strip(r' \n\r\t')
   66:         steelhead_string = re.search(r'Steelheads.*\n\n\n',
   67                                       output,

   74          for steelhead in steelheads:
   75:             serial = re.search(r'Steelhead \w*', steelhead).\
   76                  group(0).replace('Steelhead ', '')
   77  
   78:             hostname = re.search(
   79                  r'\(.* /', steelhead).group(0).strip(r'(/ \n\t\r')
   80  
   81:             ip_addr = re.search(r'\d+\.\d+\.\d+\.\d+', steelhead).group(0)
   82  
   83:             ver_string = re.search(r'Version:.*', steelhead).\
   84                  group(0).replace('Version:', '').strip(r' \n\t\r')
   85:             version = re.search(r'\d+\.\d+\.\d+', ver_string).group(0)
   86  

   89                  ocs_connectivity = False
   90:                 connectivity = re.search(r'Connected:.*', steelhead).\
   91                      group(0).replace('Connected:', '').strip(r' \n\t\r')

   96                  ocs_connectivity = False
   97:                 connectivity = re.search(
   98                      r'SSH connection:.*', steelhead).group(0).\

  101                      gcl_connectivity = True
  102:                 connectivity = re.search(
  103                      r'HTTPS connection:.*', steelhead).group(0).\

  107  
  108:             build_no = re.search(r'#\d+', ver_string).group(0)
  109  
  110:             model = re.search(r'Model:.*', steelhead).\
  111                  group(0).replace('Model:', '').strip(r' \n\t\r')

  165      output = appl_cli.exec_command("show info")
  166:     serial = re.search(
  167          r'Serial:.*', output).group(0).replace('Serial:', '').strip(r' \n\t\r')

  169      output = appl_cli.exec_command("show cmc")
  170:     line = re.search(r'CMC hostname:.*', output).group(0)
  171      try:
  172:         current_cmc = re.search(r'\d+\.\d+\.\d+\.\d+', line).group(0)
  173      except Exception:

  257          output = appl_cli.exec_command("show cmc")
  258:         managed = re.search(r'Managed by CMC:.*', output).group(0).\
  259              replace('Managed by CMC:', '').strip(r' \n\t\r')
  260:         next_msg = re.search(r'Seconds until next message is sent:.*', output)
  261:         line = re.search(r'CMC hostname:.*', output).group(0)
  262          current_cmc_host = re.sub(

  266  
  267:         current_cmc_ip = re.search(r'\d+\.\d+\.\d+\.\d+',
  268                                     line).group(0).strip(r' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\scripts\install_image.py:
  63      for line in pipe.stdout:
  64:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  65                  is not None):

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\conftest.py:
  169          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  170:         serial = re.search(r'Serial:.*', info_string).group(0).\
  171              replace('Serial:', '').strip(' \n\t\r')

  186          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  187:         serial = re.search(r'Serial:.*', info_string).group(0).\
  188              replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_hostsettings_policy_push.py:
  111      # verifing the primary and secondary dns server
  112:     sh_dns_names = re.search(r'Name server: .*\n.*\n', sh_dns_settings). \
  113          group(0).replace('Name server: ', '').strip(' \n\t\r').split('\n')

  123          model.show_web().raw
  124:     sh_proxy = re.search(r'Network Proxy:.*\n.*\n.*', sh_proxy_settings). \
  125          group(0).replace('Network Proxy:', '').strip(' \n\t\r').split('\n')
  126:     sh_proxy_name = re.search(r'Address:.*', sh_proxy[0]).group(0). \
  127          replace('Address:', '').strip(' \n\t\r')

  129          assert False, " The web proxy is not added in sh "
  130:     sh_port = re.search(r'Port:.*', sh_proxy[1]).group(0). \
  131          replace('Port:', '').strip(' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_inpath_mgmt_policy_push.py:
  123      # Verifying ipv4 inpath settings
  124:     sh_inpath_ip4 = re.search(r'IP address:.*', sh_inpath_settings).group(0).\
  125          replace('IP address:', '').strip(' \n\r\t')

  127          assert False, " IPv4 Address is not added in sh "
  128:     sh_inpath_mask = re.search(r'Netmask:.*', sh_inpath_settings).\
  129          group(0).replace('Netmask:', '').strip(' \n\r\t')

  132      # Verifying ipv6 inpath settings
  133:     sh_inpath_ip6 = re.search(
  134          r'IPv6 address:.*',

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_manage_appliances.py:
  102          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  103:         serial = re.search(r'Serial:.*', info_string).\
  104              group(0).replace('Serial:', '').strip(' \n\t\r')

  276      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  277:     serial = re.search(r'Serial:.*', info_string).\
  278          group(0).replace('Serial:', '').strip(' \n\t\r')

  317              appliance['hostname']].model.show_info().raw
  318:         health = re.search(r'Status:.*', info_text).group(0).\
  319              replace('Status:', '').strip(' \n\t\r')

  339              appliance['hostname']].model.show_info().raw
  340:         health = re.search(r'Status:.*', info_text).group(0).\
  341              replace('Status:', '').strip(' \n\t\r')

  369      info_string_1 = resources.sh_actors[sh1.hostname].model.show_info().raw
  370:     serial_1 = re.search(r'Serial:.*', info_string_1).group(0).\
  371          replace('Serial:', '').strip(' \n\t\r')

  382      info_string_2 = resources.sh_actors[sh2.hostname].model.show_info().raw
  383:     serial_2 = re.search(r'Serial:.*', info_string_2).group(0).\
  384          replace('Serial:', '').strip(' \n\t\r')

  447      info_string = resources.sh_actors[sh1.hostname].model.show_info().raw
  448:     serial = re.search(r'Serial:.*', info_string).group(0).\
  449          replace('Serial:', '').strip(' \n\t\r')

  464      status = resources.scc_actor.model.show_cmc_op_history().raw
  465:     assert 'failed' == re.search(r' *Unlock Vault *\w* *', status).\
  466          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  472      status = resources.scc_actor.model.show_cmc_op_history().raw
  473:     assert 'failed' == re.search(r' *Unlock Vault *\w* *', status).\
  474          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  480      status = resources.scc_actor.model.show_cmc_op_history().raw
  481:     assert 'success' == re.search(r' *Unlock Vault *\w* *', status).\
  482          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  518          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  519:         serial = re.search(r'Serial:.*', info_string).\
  520              group(0).replace('Serial:', '').strip(' \n\t\r')

  557          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  558:         serial = re.search(r'Serial:.*', info_string).\
  559              group(0).replace('Serial:', '').strip(' \n\t\r')

  610      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  611:     serial = re.search(r'Serial:.*', info_string).\
  612          group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_ntp_over_ipv6.py:
  48          req_ntp_servers_parsed = \
  49:             re.search(r'NTP servers:.*\n\n',
  50                        req_ntp_servers,

  76      # Get current scc date from datetme string.
  77:     current_scc_date = re.search(
  78          r'Date: .*', scc_date_time_str).\

  80      # Get current scc time from datetme string.
  81:     current_scc_time = re.search(
  82          r'Time: .*', scc_date_time_str).\

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_ntp_policy_push.py:
  106          model.show_ntp().raw
  107:     sh_ntp_servers = re.search(
  108          r'NTP servers:.*\n.*\n.*\n.*',

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_operation_history.py:
   55      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   56:     serial = re.search(r'Serial:.*', info_string).\
   57          group(0).replace('Serial:', '').strip(' \n\t\r')

  111      op_history = resources.scc_actor.model.show_cmc_op_history().raw
  112:     assert 'rbm_user' in re.search(r'\n\n.*', op_history).\
  113          group(0), 'policy push operation is logged using a different user'

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_policy_push_for_non_admin_connected_appliances.py:
   93      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   94:     serial = re.search(r'Serial:.*', info_string).\
   95          group(0).replace('Serial:', '').strip(' \n\t\r')

  202      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  203:     serial = re.search(r'Serial:.*', info_string).\
  204          group(0).replace('Serial:', '').strip(' \n\t\r')

  312      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  313:     serial = re.search(r'Serial:.*', info_string).\
  314          group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_scc_external_backup.py:
  316      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  317:     serial = re.search(r'Serial:.*', info_string).\
  318          group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_smtp_policy_push.py:
  104          model.show_email().raw
  105:     sh_smtp_name = re.search(r'Mail hub:.*', sh_email_settings).group(0).\
  106          replace('Mail hub:', '').strip(' \n\r\t')

  108          assert False, " smtp server is not added in sh "
  109:     sh_smtp_port = re.search(r'Mail hub port:.*', sh_email_settings).\
  110          group(0).replace('Mail hub port:', '').strip(' \n\r\t')

  114      for item in ['Event emails', 'Failure emails']:
  115:         sh_emails = re.search(r'' + item + '.*\n.*\n.*\n.*\n',
  116                                sh_email_settings).group(0)
  117:         sh_is_enabled = re.search(r'Enabled:.*', sh_emails).\
  118              group(0).replace('Enabled:', '').strip(' \n\r\t')

  120              assert False, sh_emails + " is not enabled "
  121:         sh_recipients = re.search(r'Recipients:.*\n.*', sh_emails).\
  122              group(0).replace('Recipients:', '').strip(' \n\r\t').split(',')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_appliance_backup_restore.py:
  67          result = resources.sh_actors[sh.hostname].model.show_banner().raw
  68:         MOTD = re.search(
  69              r'MOTD:.*', result).group(0).replace('MOTD:', '').strip(' \n\r\t')

  83          result = resources.sh_actors[sh.hostname].model.show_banner().raw
  84:         MOTD = re.search(
  85              r'MOTD:.*', result).group(0).replace('MOTD:', '').strip(' \n\r\t')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_appliance_inventory.py:
   41          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   42:         serial = re.search(r'Serial:.*', info_string).group(0).\
   43              replace('Serial:', '').strip(' \n\t\r')

  123          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  124:         serial = re.search(r'Serial:.*', info_string).\
  125              group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_generic_infrastructure_framework.py:
  125          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  126:         serial = re.search(r'Serial:.*', info_string).\
  127              group(0).replace('Serial:', '').strip(' \n\t\r')

  140          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  141:         serial = re.search(r'Serial:.*', info_string).\
  142              group(0).replace('Serial:', '').strip(' \n\t\r')

  161          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  162:         serial = re.search(r'Serial:.*', info_string).\
  163              group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_kvm_cmc_installation.py:
  178          self.kvm_host.expect(self.kvm_scc_name + r' \(config\) #')
  179:         primary_hw_address = re.search(
  180              r'HW address:.*',

  198          self.kvm_host.expect(self.FOLDER_PROMPT)
  199:         licence1 = re.search(r'\r\n.*\r\n',
  200                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  202          self.kvm_host.expect(self.FOLDER_PROMPT)
  203:         licence2 = re.search(r'\r\n.*\r\n',
  204                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  206          self.kvm_host.expect(self.FOLDER_PROMPT)
  207:         licence3 = re.search(r'\r\n.*\r\n',
  208                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  226          self.kvm_host.expect(self.kvm_scc_name + r' \(config\) #')
  227:         self.aux_ip_address = re.search(
  228              r'IP address:.*',

  233          file.close()
  234:         aux_net_mask = re.search(
  235              r'Netmask:.*',

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_physical_cmc_installation.py:
  62      for line in pipe.stdout:
  63:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  64                  is not None):

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_scc_secure_transport.py:
  182          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  183:         serial = re.search(r'Serial:.*', info_string).\
  184              group(0).replace('Serial:', '').strip(' \n\t\r')

  200          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  201:         serial = re.search(r'Serial:.*', info_string).\
  202              group(0).replace('Serial:', '').strip(' \n\t\r')

  219          resources.client_sh.hostname].model.show_info().raw
  220:     serial = re.search(r'Serial:.*', info_string).\
  221          group(0).replace('Serial:', '').strip(' \n\t\r')

  241      # Get current scc date from datetme string.
  242:     current_scc_date = re.search(
  243          r'Date: .*', current_scc_time_str).\

  245      # Get current scc time from datetme string.
  246:     current_scc_time = re.search(
  247          r'Time: .*', current_scc_time_str).\

  280      # Get current scc date from datetme string.
  281:     current_scc_date = re.search(
  282          r'Date: .*', current_scc_time_str).\

  284      # Get current scc time from datetme string.
  285:     current_scc_time = re.search(
  286          r'Time: .*', current_scc_time_str).group(0).\

  339          resources.client_sh.hostname].model.show_info().raw
  340:     serial = re.search(r'Serial:.*', info_string).\
  341          group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_stats_operation.py:
   71          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   72:         serial = re.search(r'Serial:.*', info_string).\
   73              group(0).replace('Serial:', '').strip(' \n\t\r')

  117      # Get current scc date from datetme string.
  118:     current_scc_date = re.search(
  119          r'Date: .*', current_scc_time_str).\

  121      # Get current scc time from datetme string.
  122:     current_scc_time = re.search(
  123          r'Time: .*', current_scc_time_str).\

  156      # Get current scc date from datetme string.
  157:     current_scc_date = re.search(
  158          r'Date: .*', current_scc_time_str).\

  160      # Get current scc time from datetme string.
  161:     current_scc_time = re.search(
  162          r'Time: .*', current_scc_time_str).\

  200      # Get current scc date from datetme string.
  201:     current_scc_date = re.search(
  202          r'Date: .*', current_scc_time_str).\

  204      # Get current scc time from datetme string.
  205:     current_scc_time = re.search(
  206          r'Time: .*', current_scc_time_str).\

portfolio-system-tests\new\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_virtual_cmc_installation.py:
  61      for line in pipe.stdout:
  62:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  63                  is not None):

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_performance\scaleperf_qa\libs\QAPerf.py:
   422                  first_run and not bi_directional:
   423:             if re.search('tx', key):
   424                  interfaces_keys.extend([key])
   425:             elif re.search('rx', key):
   426                  interfaces_keys.extend([key])

   470                              tx_data = re.compile(r'TX\sbytes:(\d+)')
   471:                             if re.search(rx_data, inter):
   472:                                 data1 = re.search(rx_data, inter)
   473                                  interface[ser + '_rx_data'] = data1.group(1)
   474:                             if re.search(tx_data, inter):
   475:                                 data2 = re.search(tx_data, inter)
   476                                  interface[ser + '_tx_data'] = data2.group(1)

   650              location = data_col + str(row)
   651:             temp = re.search(r'(\d+.*\d*)\s+\w', ws[location].value)
   652              record_tput = temp.group(1)

   694              break
   695:         # if not re.search('.+bits/sec', line):
   696          #     continue
   697  
   698:         # rate_found = re.search('Bytes\s+(\d+.*\d*)\s+(\wbits/sec)', line)
   699:         rate_found = re.search(pattern, line)
   700          if rate_found:

   750  
   751:         rate_found = re.search(pattern, line)
   752          if rate_found:

   895      for line in output_server.splitlines():
   896:         if re.search(r'iperf\s+.+', line):
   897:             output_server_new = re.search(r'(iperf\s+.+)', line)
   898              output_server = output_server_new.group(0)
   899      for line in output_client.splitlines():
   900:         if re.search(r'iperf\s+.+', line):
   901:             output_client_new = re.search(r'(iperf\s+.+)', line)
   902              output_client = output_client_new.group(0)

   927  
   928:         if re.search(r'8\.\d\.\d\.\s+Ethernet\s+Frame\s+Rates', row) or found:
   929              found = True
   930:             if re.search(
   931                      r'\d+\.*\d*\',\s+\'(\d+,*\d*\.*\d*)\',\s+\''
   932                      r'(\d*,*\d+\.*\d*)\'', row):
   933:                 data_new = re.search(
   934                      r'\d+\.*\d*\',\s+\'(\d+,*\d*\.*\d*)\',\s+\''

   941  
   942:         if re.search(r'8\.\d\.\d\.\d\.\sEthernet\s+Frame\s+Rates:\s1', row) \
   943                  and data_count:

  1800      regex = re.compile(r'(\w+)\s*(\d+)/(\d+)')
  1801:     if re.search(regex, untagged):
  1802:         untagged_data = re.search(regex, untagged)
  1803          slot = untagged_data.group(2)

  2250              break
  2251:         if re.search(pattern_loss, line):
  2252:             drop_rate = re.search(pattern_loss, line)
  2253              percent = float(drop_rate.group(1))
  2254              total_percent += percent
  2255:         if re.search(pattern_rate, line):
  2256:             rec_rate = re.search(pattern_rate, line)
  2257              rate_int = float(rec_rate.group(1))

  2316              break
  2317:         if re.search(pattern, line):
  2318              total_checked_count += 1
  2319:             drop_rate = re.search(pattern, line)
  2320              total_bytes = drop_rate.group(1)

  2327              total_percent += percent
  2328:         if re.search(pattern_sum, line):
  2329              sum_count += 1
  2330:             sum_rate = re.search(pattern_sum, line)
  2331              sum_int = float(sum_rate.group(2))

  2354      """
  2355:     rate = re.search(r'-B\s*(\d+)(\w{1,2})', client_opt)
  2356      old_rate = rate.group(1) + rate.group(2)

  2376      """
  2377:     rate = re.search(r'-b\s*(\d+)(\w{1,3})', client_opt)
  2378      old_rate = rate.group(1) + rate.group(2)

  2403      """
  2404:     rate = re.search(r'-b\s*(\d+)', bw_rate)
  2405      client_opt_rate = str(int(rate.group(1)))

  3176  
  3177:         if re.search(pattern, line):
  3178:             found = re.search(pattern, line)
  3179              new_rate = str(float(found.group(1)) * REDUCE_TRAFFIC_80_PERCENT)

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\add_additional_outbound_rules.py:
  75          total_rule_count += 1
  76:         m = re.search(r'Pod(\d+)_vgw_branch(\d+)_obrule(\d+)', rule['name'])
  77          if m:

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\add_additional_trafficpath_rules.py:
  78          total_rule_count += 1
  79:         m = re.search(r'Pod(\d+)_vgw_branch(\d+)_tpr(\d+)', rule['name'])
  80          if m:

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
  46      """
  47:     if (re.search(
  48          r'One or more ports have an IP allocation from this subnet',

  63      # the router UUID first and then deleting the stack
  64:     elif (re.search(
  65            r'it is required by one or more routes', delete_status)):

portfolio-system-tests\new\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\test_system_info_from_scm.py:
  216      for line in f:
  217:         if re.search(r'runsv nginx', line):
  218              process_data = line.split()

  229      for line in f:
  230:         if re.search(r'runsv postgresql', line):
  231              process_data = line.split()

  242      for line in f:
  243:         if re.search(r'runsv redis', line):
  244              process_data = line.split()

  255      for line in f:
  256:         if re.search(r'mojo/Cc.pl\b\s.*hydra.*', line):
  257              process_data = line.split()

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\devices_cli.py:
  185          'ifconfig | grep ' + interface)
  186:     mac_address = re.search("HWaddr {}".format(
  187          mac_pattern), mac_details).group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\syslog.py:
  177      pat = r"prefix=\W+{}\W+".format(prefix)
  178:     match = re.search(pat, conf)
  179      assert match is not None, "prefix {} not found in gw rsyslog config file" \

  342      for line in lines:
  343:         if re.search(msg, line) and re.search(prefix, line) and \
  344:                 re.search("<{}>".format(priority), line) and \
  345:                 re.search(serial, line):
  346              LOGGER.info("LOG message '{}' with prefix '{}', priority '{}',"

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\traffic.py:
  177      ping_result = shell.exec_command('ping {} -c {}'.format(host, count))
  178:     host_ip = re.search(
  179          r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', ping_result).group(0)

  264          cmd, curl_command_result))
  265:     http_status = re.search("HTTP/1.1 ([0-9]{3})", curl_command_result).group(
  266          1)

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler_client.py:
  106      ping_result = shell_default_ns(mgmt_ip, ping)
  107:     loss = re.search('([0-9]{1,3})%', ping_result).group(1)
  108      # Be more sloppy for low ping intervals, since first ping may fail

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\disjoint_wan\test_route_propagation.py:
  104      for line in tunnels:
  105:         match = re.search(r"vti(\d+\_\d+\_\d+).*remote\s"
  106                            r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

  293          # Check learned routes on CGW
  294:         if re.search(r"123\.123\.123\.0", cgw_routes):
  295              criteria += 1

  334          # Check learned routes on CGW
  335:         if re.search(r"123\.123\.123\.0", cgw_routes):
  336              fail_msg += "Route to 123.123.123.0 not retracted from CGW: "

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\disjoint_wan\helpers\utils.py:
  157      for tunnel in tunnels:
  158:         vti = re.search(r'(vti\d+_\d+_\d+)', tunnel)
  159          if vti:

  161  
  162:         remote = re.search(r'remote (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  163                             tunnel)

  167  
  168:         local = re.search(r'local (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  169                            tunnel)

  202          for line in conf:
  203:             if re.search(r"X.*{}".format(vti), line):
  204                  found += 1

  206              if found:
  207:                 check_line = re.search(
  208                      r".*checkip.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

  231      for line in lines:
  232:         top = re.search(
  233              r"^[\*\s][>\s][i\s]" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" +

  237              r"([\d\s]*)i?", line)
  238:         alt = re.search(
  239              r"^[\*\s][>\s][i\s]" + r"\s{17}" +

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_bgp_neighbor.py:
  37      for line in lines:
  38:         top = re.search(
  39              r"^[\*\s][>\s][i\s]\s" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" +

  42              r"([\d\s]*)[i\?]?", line)
  43:         alt = re.search(
  44              r"^[\*\s][>\s][i\s]" + r"\s+" +

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_default_route_originate.py:
   98      list_client = output.split('\n')
   99:     regex = re.search("\Send:\W+(\d+)\W+Recv:\W+(\d+)", list_client[0])  # noqa
  100      if regex:

  109      list_server = output.split('\n')
  110:     regex_server = re.search("Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)", list_server[0])  # noqa
  111      if regex_server:

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_dynamicrouting_bgp_bandwidth_limit.py:
  65      server_log = open(traffic.server_log_file, 'r').read()
  66:     bandwidth = re.search(r'(.\w?) Mbits/sec', server_log).group()
  67      bandwidth = bandwidth.replace('Mbits/sec', '').strip()

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_pqps.py:
  112      list_client = output.split('\n')
  113:     regex = re.search("\Send:\W+(\d+)\W+Recv:\W+(\d+)", list_client[0])  # noqa
  114      if regex:

  123      list_server = output.split('\n')
  124:     regex_server = re.search("Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)", list_server[0])  # noqa
  125      if regex_server:

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_static_routing.py:
  106      list_client = output.split('\n')
  107:     regex = re.search(r"\Send:\W+(\d+)\W+Recv:\W+(\d+)",
  108                        list_client[0])

  118      list_server = output.split('\n')
  119:     regex_server = re.search(r"Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)",
  120                               list_server[0])

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_zebos_config_check_bgp.py:
  44          elif line.strip().startswith('network') and \
  45:                 re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  46              gw_output['networks'].append(line.replace('network', '').strip())

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\conftest.py:
  119              ipPattern = re.compile(r'[0-9]+(?:\.[0-9]+){3}')
  120:             route = re.search(ipPattern, line).group()
  121              if route:

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\test_dynamic_routingwithha_gateway_link_failure.py:
  57      output = gw_shell.exec_command('imish -e "show ip route"')
  58:     if not re.search(zone_ip, output):
  59          pytest.fail("Zone ip is not present on the BGP route")
  60:     match = re.search(r'Total number of prefixes (\d+)', output)
  61      if match and int(match.group(1)) != 1:

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_new_zone_discovery.py:
  154      for element in gw_output.splitlines():
  155:         if re.search(network_ip, element):
  156              return True

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_remove_interface_from_area.py:
  105      for network in networks:
  106:         if re.search("discovered", network.name, re.IGNORECASE):
  107              count += 1

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_route_peering.py:
  46  
  47:             if re.search("Full", element):
  48                  ospf_neighbors.append(ip_address)

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_zebos_config_change.py:
  37          if line.strip().startswith('network') and \
  38:                 re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  39              gw_output['network'].append(re.findall(

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\ospf_multi_lan\test_traffic.py:
   47          for interface in if_op:
   48:             if re.search("192.168.15", if_op[interface]['addr']):
   49                  disabled_ints[router] = interface

  106      for interface in if_op:
  107:         if re.search("192.168.15", if_op[interface]['addr']):
  108              break

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\test_leaf_mode.py:
  97                  for line in chain.split('\n'):
  98:                     route = re.search('set-device ' + vti, line)
  99                      if route:

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\helpers\utils.py:
  31      for tunnel in tunnels:
  32:         vti = re.search(r'(vti\d+_\d+_\d+)', tunnel)
  33          if vti:

  35  
  36:         remote = re.search(r'remote (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  37                             tunnel)

  41  
  42:         local = re.search(r'local (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  43                            tunnel)

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\2gw_sh-1catfish-1gw\test_optimized_path_selection.py:
  175          for custom_app in custom_app_list:
  176:             if re.search("TCP_APP", custom_app.name, flags=re.IGNORECASE):
  177                  resources.org_obj.custom_app_management(

  189      for custom_app in custom_app_list:
  190:         if re.search("TCP_APP", custom_app.name, flags=re.IGNORECASE):
  191              custom_app_obj = custom_app

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\helpers\utils.py:
   138                  m = \
   139:                     re.search(r'(O\>\*|O\s\s)\s'
   140                                r'(\d+\.\d+\.\d+\.\d+\/\d+).*%s' % interface,

   142              else:
   143:                 m = re.search(r'(O\>\*|O\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)',
   144                                line)
   145          elif specific_route.lower() == 'bgp':
   146:             m = re.search(r'(B\>\*|B\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   147          elif specific_route.lower() == 'static':
   148:             m = re.search(r'(S\>\*|S\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   149          elif specific_route.lower() == 'connected':
   150:             m = re.search(r'(C\>\*|C\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   151          else:
   152:             m = re.search(r'(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   153          if m:

   202              if aspath is not None:
   203:                 m = re.search(r'(\d+\s\d+\s\d+)', line)
   204              else:
   205:                 m = re.search(r'(\d{5}\s\d{4})', line)
   206              if m is not None:

   356      for route in route_op.split("OSPF external")[1].split("\n"):
   357:         ips = re.search(r'(\d+\.\d+\.\d+\.\d+\/\d+)', route)
   358          metric_value = re.\
   359              search(r'((\[\d+\]|\[\d+/0\]|\[\d+/\d+\])\s\w+:\s\d+)', route)
   360:         type_route = re.search(r'(E\d)', route)
   361          if ips:

   902      ospf_int_output = container_shell.exec_command(cmd1)
   903:     cost = re.search(r'Cost: (\d+)', ospf_int_output)
   904:     priority = re.search(r'Priority (\d+)', ospf_int_output)
   905:     hello = re.search(r'Hello (\d+)', ospf_int_output)
   906:     dead = re.search(r'Dead (\d+)', ospf_int_output)
   907      return (cost.group(1), priority.group(1), hello.group(1), dead.group(1))

  1126      routes_info = container_shell.exec_command(cmd)
  1127:     routes_ip_info = map(lambda y: re.search(r'\s.(\d*.\d*.\d*.\d*)\s', y).
  1128                           group(0).strip(), routes_info.

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\upgrade\test_upgrade.py:
  125      print(univ_op)
  126:     latest_build_tag = re.search('binary_builds.*browse/(.+)', univ_op).\
  127          group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ospf_bgp_trio\test_ospf_failures.py:
  46      for network in networks:
  47:         if re.search("Discovered", network.name):
  48              count += 1

portfolio-system-tests\new\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ospf_bgp_trio\test_ospf_remove_interface_from_area.py:
  151      for network in networks:
  152:         if re.search("discovered", network.name, re.IGNORECASE):
  153              count += 1

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_hardware_spec_activate.py:
   70                                                          timeout=180)
   71:                     result = re.search(r'Stopped', result)
   72                      if result:

  121                                                      timeout=180)
  122:                 result = re.search(r'Healthy', result)
  123                  if result:

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability_client_sh.py:
  148          # The model extracted is in this form "VCX (VCX10)"
  149:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  150          sh_model_found = sh_model_detected.group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability_server_sh.py:
  158          # The model extracted is in this form "VCX (VCX10)"
  159:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  160          sh_model_found = sh_model_detected.group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability.py:
  189          # The model extracted is in this form "VCX (VCX10)"
  190:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  191          sh_model_found = sh_model_detected.group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_volume_size.py:
  160          # The model extracted is in this form "VCX (VCX10)"
  161:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  162          sh_model_found = sh_model_detected.group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\openstack-tests\openstack_ops.py:
  50              for stack_name in self.stack_name_list:
  51:                 search_string=re.search(r'jenkins-Axel-VSH-CAT-\d+_\w+',stack_name)
  52                  if search_string != None:

portfolio-system-tests\new\portfolio_system_tests\legacy_vsh_tests\provisioning\test_user_data.py:
  360                  if "Model" in line:
  361:                     m = re.search(r"\(([A-Za-z0-9_]+)\)", line)
  362                      print("Found Model: " + m.group(1))

  485      if(not invalid):
  486:         assert re.search(re.escape(expression),show_run)
  487      else:
  488:         assert re.search(re.escape(log_expression),show_rsisinit_log)
  489:         assert not re.search(re.escape(expression),show_run)
  490  

portfolio-system-tests\new\portfolio_system_tests\legacy_webcache_tests\http_server_allocation.py:
  317              cli_result = Model.get(fe).show_info()
  318:             if re.search("Service needs a 'restart'", cli_result.raw, re.I):
  319                  fes_to_restart.append(fe)

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\auditoperations.py:
   53      for line in zfile:
   54:         m = re.search(r"Created key with name='([^']+)' .* operation='Create"
   55                        " root CA", line)

   65      for line in zfile:
   66:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
   67                        "keyvault for user operation='Create root CA for "

   79      for line in zfile:
   80:         m = re.search(r"Create root CA for org=([^\s]+) CN=(.*) completed by "
   81                        "user='([^']*)' with signing key name='([^']+)'", line)

   92      for line in zfile:
   93:         m = re.search("-BEGIN CERTIFICATE-.*", line)
   94          if m:

  107      for line in zfile:
  108:         m = re.search(r"Created key with name='([^']+)' .* operation="
  109                        "'Create and activate root CA", line)

  120      for line in zfile:
  121:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
  122                        "keyvault for user operation='Create and activate root "

  134      for line in zfile:
  135:         m = re.search(r"Create and activate root CA for org=([^\\s]+) CN=(.*)"
  136                        "completed by user='([^']*)' with signing key name="

  148      for line in zfile:
  149:         m = re.search("-BEGIN CERTIFICATE-", line)
  150          if m:

  164      for line in zfile:
  165:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Signed digest='([^']+)' "
  166                        "using key='([^']+)' from keyvault for user operation="

  180      for line in zfile:
  181:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Sign peering cert request for CN="
  182                        "([^']+) from requestor=([^\\s]+) completed", line)

  193      for line in zfile:
  194:         m = re.search("-BEGIN CERTIFICATE-", line)
  195          if m:

  209      for line in zfile:
  210:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Signed digest='([^']+)' using "
  211                        "key='([^']+)' from keyvault for user operation="

  225      for line in zfile:
  226:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Sign proxy cert request for "
  227                        "CN=([^']+) from requestor=([^\\s]+) completed", line)

  238      for line in zfile:
  239:         m = re.search(".*-BEGIN CERTIFICATE-.*", line)
  240          if m:

  253      for line in zfile:
  254:         m = re.search(r"Created key with name='([^']+)' .* operation="
  255                        "'Create intermediate CA CSR", line)

  265      for line in zfile:
  266:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
  267                        "keyvault for user operation='Create intermediate CA "

  279      for line in zfile:
  280:         m = re.search(r"Create intermediate CA CSR for org=([^\s]+) CN=(.*) "
  281                        "completed by user='([^']*)' with signing key name="

  293      for line in zfile:
  294:         m = re.search("-BEGIN CERTIFICATE-", line)
  295          if m:

  308      for line in zfile:
  309:         m = re.search(r".*Retrieved public key with name='([^']+)' .* "
  310                        "operation='Delete CSR", line)

  321      for line in zfile:
  322:         m = re.search(r"Deleted key='([^']+)' from keyvault for user operation"
  323                        "='Delete CSR for org=([^\\s]+) CN=([^']+)", line)

  333      for line in zfile:
  334:         m = re.search(r"Delete CSR for org=([^\s]+) CN=(.*) completed by user="
  335                        "'([^']*)' with signing key name='([^']+)'.*", line)

  350      for line in zfile:
  351:         m = re.search(r"Retrieved public key with name='([^']+)' .* "
  352                        "operation='Delete CA", line)

  363      for line in zfile:
  364:         m = re.search(r"Deleted key='([^']+)' from keyvault for user operation"
  365                        "='Delete CA for org=([^\\s]+) CN=([^']+)", line)

  375      for line in zfile:
  376:         m = re.search(r"Delete CA for org=([^\s]+) CN=(.*) completed by user"
  377                        "='([^']+)' with signing key name '([^']+)'", line)

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\azure_helper.py:
  282          pip_id = nic_params.ip_configurations[0].public_ip_address.id
  283:         pip_name = re.search(r'[^/]*$', pip_id).group(0)
  284          public_ip_address = \

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\conftest.py:
   308          output = automodel.show_peers(online_only=True)
   309:         m = re.search("Connected appliances:\\s+(\\d+)", output.raw)
   310          no_of_peers = int(m.group(1))

   318          zak_serial_no = get_zak_serial_no(scm_actor)
   319:         if (re.search(zak_serial_no, output.raw)):
   320              return 1

   414              azure_helper = AzureHelper()
   415:             zaksh_name = re.search(r'([^\s]+)', zaksh_data).group()
   416              zaksh_nic_ids = azure_helper.get_vm_nic_ids(rg, zaksh_name)
   417:             nic_name = re.search(r'[^/]*$', zaksh_nic_ids[0]).group(0)
   418              pip = azure_helper.get_nic_public_ip(rg, nic_name)

   780          output = zaksh_shell.exec_command(cmd)
   781:         curr_log = re.search(r'(\S+) file', output).group(1)
   782          logger.info(f"Current ZAKSH log level: {curr_log}")

   883          else:
   884:             m = re.search("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*$",
   885                            output)

  1173          output = automodel.show_peers(online_only=True)
  1174:         if (re.search("No connected peer", output.raw)):
  1175              return 1
  1176:         m = re.search("Connected appliances:\\s+(\\d+)", output.raw)
  1177          no_of_peers = int(m.group(1))

  1429                                    allocation=Allocation())
  1430:         zaksh_ip = re.search('(?<=\[)[^]]+(?=\])', zak_sh_data).group()  # noqa
  1431          admin_cidr = ipaddress.ip_interface(str(zaksh_ip + "/0"))

  2013              raise ValueError("There is no application token")
  2014:         app_token = re.search("(^\\S*)", value).group(0)
  2015          return app_token

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\vanautu\test_cfe_lb_none.py:
  28      assert("GLB Secondary Ports" not in output.keys())
  29:     lb_ports = re.search("(\\d+)-(\\d+)", output['load balancer port range'])
  30      port1 = int(lb_ports.group(1))

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\misc_scripts\docker_remove_oldimage.py:
  17  for line in output.splitlines():
  18:     m = re.search("quay.*bamboo.*\\s+(\\S+)\\s+(\\d+)\\s+(hours|days) ago",
  19                    line)

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
   456              try:
   457:                 lb_ip = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',
   458                                    output).group(0)

   491          assert(vm_info is not None)
   492:         output = re.search('{.*}', vm_info)
   493          assert(output)

   642          challenge_str = actor.model.cli_challenge_generate().raw
   643:         token_obj = re.search(r'Generated challenge: (.*)', challenge_str)
   644          if token_obj:

   651          output = local_shell.exec_command(cmd, timeout=TIMEOUT)
   652:         response_obj = re.search(r'cli challenge response (.*)', output)
   653          if response_obj:

   787              app_restrict_flag = \
   788:                 re.search(r'app_restriction_enable=(\S+)', out).group(1)
   789              logger.info(f"Current app restriction: {app_restrict_flag}")

   798              out = ssh_shell.exec_command(cmd)
   799:             curr_log = re.search(r'(\S+) file', out).group(1)
   800              logger.info(f"Current log level: {curr_log}")

   816                  copy_util.copy_from_host(zaksh, "/dumps/", cert_path)
   817:                 cert_file = re.search(r'[^/]*$', cert_path).group(0)
   818                  cmd = (f"sudo cp /dumps/{cert_file} /var/opt/rbt/ssl/ca/; "

  1138              output_expected=True)
  1139:         if re.search(r'active', output):
  1140              return True

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\csh_data_disks_operations.py:
  96      output = perfHelper.execute_shell_cmds_csh(csh, [cmd])
  97:     num_disks = re.search(r"(.*)$", output.decode("utf-8")).group(0)
  98      log.info(f"Number of data disks attached to CSH: {num_disks}")

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\setup_clients_servers.py:
   88          output = shell.exec_command(cmd, output_expected=True)
   89:     version = re.search(r'(\d+.\d+)', output)
   90      if version:

  171          with open('60-static.yaml', 'w') as infile:
  172:             match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}', eth0_ip).group(0)
  173              infile.write(NETPLAN.format(eth0_ip, match))

  176                      str(actor_client.resource.interfaces[f'test{eth}'].cidr.ip)
  177:                 match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}', eth_ip).group(0)
  178                  infile.write(ETH.format(eth, eth_ip, match, eth))

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\zak_cluster.py:
   67      zaksh_ip = \
   68:         re.search(r'(?<=\[)[^]]+(?=\])', zaksh_data).group()
   69      admin_cidr = ipaddress.ip_interface(str(zaksh_ip + "/0"))

  143          zahsh_name = \
  144:             re.search(r'([^\s]+)', zaksh_data).group()
  145          zaksh_resource = create_zaksh_resource(zaksh_data,

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\zaksh_setup\azure_helper.py:
  2685          for vm_nic in vm_nics_list:
  2686:             if re.search('-ul2', vm_nic.name):
  2687                  all_vm_resources["nic_uplink2"] = vm_nic.name

  2691                      all_vm_resources["subnet_uplink2"] = subnet
  2692:             elif re.search('-ul', vm_nic.name):
  2693                  all_vm_resources["nic_uplink"] = vm_nic.name

  2697                      all_vm_resources["subnet_uplink"] = subnet
  2698:             if re.search('-dl', vm_nic.name):
  2699                  all_vm_resources["nic_downlink"] = vm_nic.name

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\shm_tests\shm_helper.py:
   75          cmd_output = self.client_shell.exec_command(cmd)
   76:         status = re.search(search_pattern, cmd_output)
   77          if status:

  155          cmd_output = self.client_shell.exec_command(cmd)
  156:         app_content = re.search(search_pattern, cmd_output, re.DOTALL)
  157          if app_content:

  170              application_map['dest_port'] = int(dest[1])
  171:             application_map['app_id'] = int(re.search(".*snoopy_app="
  172                                                        "(\\d+)", app).group(1)

portfolio-system-tests\new\portfolio_system_tests\legacy_zaksh_tests\tests\zak_sh_troubleshoot\test_zaksh_nic_nw_acceleration.py:
   85              output = zak_sh_shell.exec_command(cmd, output_expected=True)
   86:             ipv4_address = re.search(r'inet \d+.\d+.\d+.\d+', output)
   87              assert(ipv4_address is None)

   91              output = zak_sh_shell.exec_command(cmd, output_expected=True)
   92:             ipv4_address = re.search(r'inet \d+.\d+.\d+.\d+', output)
   93              if (ipv4_address is None):

  107              assert(output is not None)
  108:             maxconn = re.search(r'net.core.somaxconn = \d+', output)
  109              fo.write("\nsomaxconn {} ".format(maxconn.group(0)))
  110:             tcpmem = re.search(r'net.ipv4.tcp_mem = \d+\s+\d+\s+\d+', output)
  111              fo.write("\ntcp_mem {} ".format(tcpmem.group(0)))
  112:             port_range = re.search(r'net.ipv4.ip_local_port_range = \d+\s+\d+',
  113                                     output)

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\configure.py:
  1768              node_name = name.strip()
  1769:             all_match = re.search(r"value: (.*) \((.*)\)", value)
  1770              if not all_match:

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\connectivity.py:
  61                  loss_re = re.compile(r'(\d*)%(?: packet)? loss')
  62:                 tx_search = tx_re.search(line)
  63:                 rx_search = rx_re.search(line)
  64:                 loss_search = loss_re.search(line)
  65                  if tx_search is not None:

  73                      r'(\d*.\d*)/(\d*.\d*)/(\d*.\d*)(?:/\d*.\d*)? ms')
  74:                 rtt_search = rtt_re.search(line)
  75                  if rtt_search is None:

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\exchange_load.py:
  221      client_resource = allocation.resources[client]
  222:     branch_suffix = re.search(r"([-]\d+)", client).group(0)
  223      sh_name = 'steelhead' + branch_suffix

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\sharepoint_load.py:
  186      client_resource = allocation.resources[client]
  187:     branch_suffix = re.search(r"([-]\d+)", client).group(0)
  188      sh_name = 'steelhead' + branch_suffix

  192  
  193:     client_suffix = re.search(r"([-]\d+)+", client)
  194      file_prefix, file_suffix = file_name.split('.')

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\verification.py:
  110          if re.match(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line) and \
  111:            re.search(r'ERR(OR)?\]', line):
  112              # Get time stamp
  113:             split = re.search(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line).group(0)
  114              date = split[1:]

  130      for line in file_contents:
  131:         if re.search(r'ERR(OR)?\]', line):
  132              error_list.append(line)

portfolio-system-tests\new\portfolio_system_tests\spoon_tests\libs\wget_load.py:
  195      else:
  196:         branch_suffix = re.search(r"([-]\d+)", client).group(0)
  197          sh_name = 'steelhead' + branch_suffix

portfolio-system-tests\new\portfolio_system_tests\tiramisu\test_functional_sanity_win.py:
  105  
  106:     match = re.search(r'\((?P<ip>.*?)\) port \d+', output)
  107      if match:

portfolio-system-tests\new\portfolio_system_tests\winsec\conftest.py:
   79      # the lost percentage values.
   80:     results = re.search(r'Lost\s+=\s+(\d+)', ping_results)
   81      if results:

  902      # Matching to 'EncryptData\s+:\s+{True|False}'
  903:     enc_status = re.search(r'EncryptData\s+:\s+(\w+)',
  904                             smb_server._exec_cmd(get_cmd)).group(1)

portfolio-system-tests\portfolio_system_tests\gelato\setup_collector_simulator_pair.py:
  109          res = shell.exec_command('virsh net-dhcp-leases default')
  110:         vm_ip_search = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
  111          if not vm_ip_search:

portfolio-system-tests\portfolio_system_tests\gelato\setup_collector_simulator_stack.py:
  86          res = shell.exec_command('virsh net-dhcp-leases default')
  87:         vm_ip_search = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
  88          if not vm_ip_search:

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\NX_Manufacture\utils.py:
   98      one, two = os.path.split(component)
   99:     build_number = re.search(name + "-(.*?)-(.*?).noarch.rpm", two).group(2)
  100      number = ": " + str(build_number)
  101  
  102:     version = re.search(name + "-(.*?)-(.*?).noarch.rpm", two).group(1)
  103      version = ": " + str(version)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\NX_Manufacture\vm.py:
  100              vm_create_node_image_name = \
  101:                 re.search(r'(.*)\s+:\s+' + vm_product_name,
  102                            line).group(1).strip()

  174      try:
  175:         image_name = re.search(r'\|\s+' + vm_node_name + r"\s+\|\s+(.*?)\|",
  176                                 buf).group(1).strip()

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\setup_upgrade\test_upgrade_scon.py:
  126      print(univ_op)
  127:     latest_build_tag = re.search('binary_builds.*browse/(.+)', univ_op).\
  128          group(1)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_cli.py:
   64      str_pattern = 'challenge generate(.*){}'.format(dut_serialno)
   65:     match = re.search(str_pattern, cmd_op)
   66      if match:

  475                                      replace("rvbd-testuser@", "root@")
  476:                                 match = re.search('ProxyCommand=nc -X '
  477                                                    'connect -x (.*):', val).\

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_connectivity.py:
  185              val = tunnel['ssh_help']
  186:             match = re.search(
  187                  'ProxyCommand=nc -X connect -x (.*):',

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_diverter.py:
  149      dns_output = cvm_shell.exec_command('nslookup ' + remote_host)
  150:     filter_host_ip = re.search('Address: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', # noqa
  151                                 dns_output)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_oa_cdl_update.py:
  747                                                      new_cdl_file)
  748:             match = re.search(error_msg, output.strip())
  749              if not match:

  759                                                      new_cdl_file)
  760:             match = re.search(error_msg, output.strip())
  761              if not match:

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_ssh_tunnel.py:
  86                              val = tunnel['ssh_help']
  87:                             match = re.search('ProxyCommand=nc -X connect '
  88                                                '-x (.*):', val).group(1)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_static_config.py:
  389                  continue
  390:             ipmatch = re.search(r'inet\s(?:addr:)*(\S+)', line)
  391              if ipmatch:

  394  
  395:             maskmatch = re.search(r'Mask:*\s*(\S+)', line, re.IGNORECASE)
  396              if maskmatch:

  405  
  406:             ipv6match = re.search(
  407                  r'inet6\saddr:\s([a-fA-F0-9:]+)/*(\S+)', line)

  413  
  414:             ethmatch = re.search(r'(?:(?:ether)|(?:HWaddr))\s(?:addr:)*(\S+)',
  415                                   line)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_tcpdump_on_cli.py:
  105      if state == 'RUNNING':
  106:         match = re.search(tcpdump_running_exp_str, output)
  107          if match:

  112      else:
  113:         match = re.search(tcpdump_not_running_exp_str, output)
  114          if match:

  208          logger.info("output of tcpdump command: {}".format(tcpdump_output))
  209:         match = re.search(exp_result, tcpdump_output)
  210          tcpdump_file = match.group(0)

  257              tcpdump_output = cli_instance.exec_command(tcpdump_cmd1)
  258:             match = re.search(exp_result, tcpdump_output)
  259              tcpdump_file = match.group(0)

  326          output = cli_instance.exec_command(tcpdump_stop_cmd)
  327:         match = re.search(tcpdump_stop_exp_result, output)
  328          if match:

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_troubleshoot_tool.py:
   92          data = troubleshoot_info.split('\n')
   93:         match = re.search(exp_result, data[-1])
   94          troubleshoot_tar = match.group(0)

  146              data = troubleshoot_info.split('\n')
  147:             match = re.search(exp_result, data[-2])
  148              troubleshoot_tar = match.group(0)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\nodes.py:
  661  
  662:         match = re.search(exp_result, data[-1])
  663          troubleshoot_tar = match.group(0)

portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\site_dns_lib.py:
  248      most_recent_content = lease_file_op.split("lease {")[-1]
  249:     m = re.search("option domain-name-servers (.*);", most_recent_content)
  250      if m:

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_external.py:
  47          for fru in fru_list:
  48:             assert re.search("CXA-00[57]70-B020", fru['Chassis Part Number'])
  49              assert fru['Board Mfg'] == 'Advantech'

  51              assert fru['Product Name'] == 'DTATA'
  52:             assert re.search("FWA-3250-RB0[23]E?", fru['Product Part Number'])
  53      except AssertionError as e:

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_local.py:
  46          for fru in fru_list:
  47:             assert re.search("CXA-00[57]70-B020", fru['Chassis Part Number'])
  48              assert fru['Board Mfg'] == 'Advantech'

  50              assert fru['Product Name'] == 'DTATA'
  51:             assert re.search("FWA-3250-RB0[23]E?", fru['Product Part Number'])
  52      except AssertionError as e:

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_external.py:
   26      try:
   27:         assert re.search(r"\d+", info_dict['Record Count']), \
   28              info_dict['Record Count']
   29:         assert re.search(r"\d+ bytes", info_dict['Free Space']), \
   30              info_dict['Free Space']

   56          for op in status_list:
   57:             if re.search(("fan", op[0].lower()) and
   58                           op[1].lower() != 'no reading'):
   59:                 assert re.search(r"\d+ RPM", op[1]), op
   60      except AssertionError as e:

   70          for op in status_list:
   71:             if re.search(("temp", op[0].lower()) and
   72                           op[1].lower() != 'no reading'):
   73:                 assert re.search(r"\d+ degrees C", op[1]), op
   74      except AssertionError as e:

   84          for op in status_list:
   85:             if re.search(("hdd", op[0].lower()) and
   86                           op[1].lower() != 'no reading'):
   87:                 assert re.search(r"\d+ degrees C", op[1]), op
   88      except AssertionError as e:

   98          for op in status_list:
   99:             if re.search(("cpu_dimm*", op[0].lower()) and
  100                           op[1].lower() != 'no reading'):
  101:                 assert re.search(r"\d+ degrees C", op[1]), op
  102:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  103:                 assert re.search(r"^\d+\.?\d* Volts", op[1]), op
  104      except AssertionError as e:

  114          for op in status_list:
  115:             if re.search("power", op[0].lower()):
  116:                 assert re.search(r"\d+ Watts", op[1]), op
  117      except AssertionError as e:

  142                  assert op[2] == 'ok', op
  143:                 if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  144:                     assert re.search(r"\d+ degrees C", op[4]), op
  145      except AssertionError as e:

  156              assert op[2] == 'ok'
  157:             assert re.search(r"\d+\.\d+ Volts", op[4]), op
  158      except AssertionError as e:

  169              assert op[2] == 'ok'
  170:             assert re.search(r"\d+ RPM", op[4]), op
  171      except AssertionError as e:

  182              assert op[2] == 'ok'
  183:             if re.search(r"PSU\d+ Status", op[0]):
  184                  assert op[4].lower() == 'presence detected'
  185:             elif re.search(r"PSU\d+ Power", op[0]):
  186:                 assert re.search(r"\d+ Watts", op[4])
  187      except AssertionError as e:

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_ipmb.py:
   44      try:
   45:         assert re.search(r'\d+', info_dict['Record Count']), \
   46              info_dict['Record Count']
   47:         assert re.search(r'\d+ bytes', info_dict['Free Space']), \
   48              info_dict['Free Space']

   63          for op in status_list:
   64:             if re.search("fan", op[0].lower()) and op[1] != 'no reading':
   65:                 assert re.search(r'\d+ RPM', op[1]), op
   66      except AssertionError as e:

   79          for op in status_list:
   80:             if re.search("temp", op[0].lower()) and op[1] != 'no reading':
   81:                 assert re.search(r'\d+ degrees C', op[1]), op
   82      except AssertionError as e:

   95          for op in status_list:
   96:             if re.search("hdd", op[0].lower()) and op[1] != 'no reading':
   97:                 assert re.search(r"\d+ degrees C", op[1]), op
   98      except AssertionError as e:

  111          for op in status_list:
  112:             if re.search(("cpu_dimm*", op[0].lower()) and
  113                           op[1].lower() != 'no reading'):
  114:                 assert re.search(r"\d+ degrees C", op[1]), op
  115:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  116:                 assert re.search(r"^\d+\.?\d* Volts", op[1]), op
  117      except AssertionError as e:

  130          for op in status_list:
  131:             if re.search("power", op[0].lower()) and op[1] != 'no reading':
  132:                 assert re.search(r"\d+ Watts", op[1]), op
  133      except AssertionError as e:

  165                      assert op[2] == 'ok', op
  166:                     if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  167:                         assert re.search(r"\d+ degrees C", op[4]), op
  168          except AssertionError as e:

  186                  assert op[2] == 'ok'
  187:                 assert re.search(r"\d+\.\d+ Volts", op[4]), op
  188          except AssertionError as e:

  205                  assert op[2] == 'ok'
  206:                 assert re.search(r"\d+ RPM", op[4]), op
  207          except AssertionError as e:

  224                  assert op[2] == 'ok'
  225:                 if re.search(r"PSU\d+ Status", op[0]):
  226                      assert op[4].lower() == 'presence detected'
  227:                 elif re.search(r"PSU\d+ Power", op[0]):
  228:                     assert re.search(r"\d+ Watts", op[4])
  229          except AssertionError as e:

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_local.py:
   39      try:
   40:         assert re.search(r'\d+', info_dict['Record Count']), \
   41              info_dict['Record Count']
   42:         assert re.search(r'\d+ bytes', info_dict['Free Space']), \
   43              info_dict['Free Space']

   55          for op in status_list:
   56:             if re.search("fan", op[0].lower()) and op[1] != 'no reading':
   57:                 assert re.search(r'\d+ RPM', op[1]), op
   58      except AssertionError as e:

   68          for op in status_list:
   69:             if re.search(("temp", op[0].lower()) and
   70                           op[1].lower() != 'no reading'):
   71:                 assert re.search(r'\d+ degrees C', op[1]), op
   72      except AssertionError as e:

   82          for op in status_list:
   83:             if re.search("hdd", op[0].lower()) and op[1] != 'no reading':
   84:                 assert re.search(r'\d+ degrees C', op[1]), op
   85      except AssertionError as e:

   95          for op in status_list:
   96:             if re.search(("cpu_dimm*", op[0].lower()) and
   97                           op[1].lower() != 'no reading'):
   98:                 assert re.search(r'\d+ degrees C', op[1]), op
   99:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  100:                 assert re.search(r'^\d+\.?\d* Volts', op[1]), op
  101      except AssertionError as e:

  111          for op in status_list:
  112:             if re.search("power", op[0].lower()) and op[1] != 'no reading':
  113:                 assert re.search(r'\d+ Watts', op[1]), op
  114      except AssertionError as e:

  139                  assert op[2] == 'ok', op
  140:                 if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  141:                     assert re.search(r'\d+ degrees C', op[4]), op
  142      except AssertionError as e:

  154                  assert op[2] == 'ok', op
  155:                 assert re.search(r'\d+\.\d+ Volts', op[4]), op
  156      except AssertionError as e:

  167              assert op[2] == 'ok', op
  168:             assert re.search(r'\d+ RPM', op[4]), op
  169      except AssertionError as e:

  180              assert op[2] == 'ok', op
  181:             if re.search(r'PSU\d+ Status', op[0]):
  182                  assert op[4].lower() == 'presence detected'
  183:             elif re.search(r'PSU\d+ Power', op[0]):
  184:                 assert re.search(r'\d+ Watts', op[4])
  185      except AssertionError as e:

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_external.py:
   81          assert sel_info_dict['Entries'] == '3'
   82:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   83              sel_info_dict['Version']
   84:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   85              sel_info_dict['Entries']
   86:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
   87              sel_info_dict['Free Space']
   88:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
   89              sel_info_dict['Percent Used']

  102          assert sel_info_dict['Entries'] == '3'
  103:         assert re.search(r"^1.5", sel_info_dict['Version']), \
  104              sel_info_dict['Version']
  105:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  106              sel_info_dict['Entries']
  107:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  108              sel_info_dict['Free Space']
  109:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  110              sel_info_dict['Percent Used']

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_ipmb.py:
   94          assert sel_info_dict['Entries'] == '3'
   95:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   96              sel_info_dict['Version']
   97:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   98              sel_info_dict['Entries']
   99:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  100              sel_info_dict['Free Space']
  101:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  102              sel_info_dict['Percent Used']

  117          assert sel_info_dict['Entries'] == '3'
  118:         assert re.search(r"^1.5", sel_info_dict['Version']), \
  119              sel_info_dict['Version']
  120:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  121              sel_info_dict['Entries']
  122:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  123              sel_info_dict['Free Space']
  124:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  125              sel_info_dict['Percent Used']

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_local.py:
   90              assert sel_info_dict['Entries'] == '3'
   91:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   92              sel_info_dict['Version']
   93:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   94              sel_info_dict['Entries']
   95:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
   96              sel_info_dict['Free Space']
   97:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
   98              sel_info_dict['Percent Used']

  114              assert sel_info_dict['Entries'] == '4'
  115:         assert re.search("^1.5", sel_info_dict['Version']), \
  116              sel_info_dict['Version']
  117:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  118              sel_info_dict['Entries']
  119:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  120              sel_info_dict['Free Space']
  121:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  122              sel_info_dict['Percent Used']

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_set_ip_source.py:
  100          assert ip_dict['ip_source'] == 'dhcp'
  101:         assert re.search(r"(\d+\.){3}\d+", ip_dict['ip_source']), \
  102              ip_dict['ip_source']
  103:         assert re.search(r"(\d+\.){3}\d+", ip_dict['subnet_mask']), \
  104              ip_dict['subnet_mask']
  105:         assert re.search(r"(\d+\.){3}\d+", ip_dict['gateway']), \
  106              ip_dict['gateway']

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc_stress\test_bmc_stress_rios_power_cycle.py:
  141      proc_ipmi_stats = shell.exec_command(cmd)
  142:     if (re.search(r'sent_ipmb_command_errs:\s+\d{1,3}\s+',
  143                    proc_ipmi_stats) and
  144:             re.search(r'sent_lan_command_errs:\s+\d{1,3}\s+',
  145                        proc_ipmi_stats) and
  146:             re.search(r'retransmitted_lan_commands:\s+\d{1,3}\s+',
  147                        proc_ipmi_stats) and
  148:             re.search(r'timed_out_lan_commands:\s+\d{1,3}\s+',
  149                        proc_ipmi_stats) and
  150:             re.search(r'sent_lan_responses:\s+\d{1,3}\s+',
  151                        proc_ipmi_stats) and
  152:             re.search(r'handled_lan_responses:\s+\d{1,3}\s+',
  153                        proc_ipmi_stats) and
  154:             re.search(r'invalid_lan_responses:\s+\d{1,3}\s+',
  155                        proc_ipmi_stats) and
  156:             re.search(r'unhandled_lan_responses:\s+\d{1,3}\s+',
  157                        proc_ipmi_stats)):

  242          box_type = ipmitool_rios_lan.run("fru list")
  243:         if(re.search("2U", box_type)):
  244              logger.info("##### BLUEFIN-2U #########")

  262                                   "169.254.0.101"]
  263:         elif(re.search("1U", box_type)):
  264              logger.info("##### BLUEFIN-1U #########")

  328          mc_info = ipmitool_rios_lan.run("mc info")
  329:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  330          mc_info_status["rios_aux"][0] = mc_info_status["rios_aux"][0] + 1

  348          mc_info = ipmitool_rios.run("mc info")
  349:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  350          mc_info_status["rios_local"][0] = mc_info_status["rios_local"][0] + 1

  369          mc_info = ipmitool_vsp_lan.run("mc info")
  370:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  371          mc_info_status["vsp_aux"][0] = mc_info_status["vsp_aux"][0] + 1

  389          mc_info = ipmitool_vsp.run("mc info")
  390:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  391          mc_info_status["vsp_ipmb"][0] = mc_info_status["vsp_ipmb"][0] + 1

  412          for op in status_list:
  413:             if (re.search("no reading", op[1]) or
  414:                     re.search("Not Readable", op[1])):
  415                  assert op[2] == "ns", op

  438          for op in status_list:
  439:             if (re.search("no reading", op[1]) or
  440:                     re.search("Not Readable", op[1])):
  441                  assert op[2] == "ns", op

  466          for op in status_list:
  467:             if (re.search("no reading", op[1]) or
  468:                     re.search("Not Readable", op[1])):
  469                  assert op[2] == "ns", op

  494          for op in status_list:
  495:             if (re.search("no reading", op[1]) or
  496:                     re.search("Not Readable", op[1])):
  497                  assert op[2] == "ns", op

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc_stress\test_bmc_stress.py:
  137      proc_ipmi_stats = shell.exec_command(cmd)
  138:     if (re.search(r'sent_ipmb_command_errs:\s+\d{1,3}\s+',
  139                    proc_ipmi_stats) and
  140:             re.search(r'sent_lan_command_errs:\s+\d{1,3}\s+',
  141                        proc_ipmi_stats) and
  142:             re.search(r'retransmitted_lan_commands:\s+\d{1,3}\s+',
  143                        proc_ipmi_stats) and
  144:             re.search(r'timed_out_lan_commands:\s+\d{1,3}\s+',
  145                        proc_ipmi_stats) and
  146:             re.search(r'sent_lan_responses:\s+\d{1,3}\s+',
  147                        proc_ipmi_stats) and
  148:             re.search(r'handled_lan_responses:\s+\d{1,3}\s+',
  149                        proc_ipmi_stats) and
  150:             re.search(r'invalid_lan_responses:\s+\d{1,3}\s+',
  151                        proc_ipmi_stats) and
  152:             re.search(r'unhandled_lan_responses:\s+\d{1,3}\s+',
  153                        proc_ipmi_stats)):

  237          box_type = ipmitool_rios_lan.run("fru list")
  238:         if(re.search("2U", box_type)):
  239              logger.info("##### BLUEFIN-2U #########")

  257                                   "169.254.0.101"]
  258:         elif(re.search("1U", box_type)):
  259              logger.info("##### BLUEFIN-1U #########")

  354              mc_info = ipmitool_rios_lan.run("mc info")
  355:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  356              mc_info_status["rios_aux"][0] = mc_info_status["rios_aux"][0] + 1

  374              mc_info = ipmitool_rios.run("mc info")
  375:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  376              mc_info_status["rios_local"][0] = \

  397              mc_info = ipmitool_vsp_lan.run("mc info")
  398:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  399              mc_info_status["vsp_aux"][0] = mc_info_status["vsp_aux"][0] + 1

  417              mc_info = ipmitool_vsp.run("mc info")
  418:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  419              mc_info_status["vsp_ipmb"][0] = mc_info_status["vsp_ipmb"][0] + 1

  440              for op in status_list:
  441:                 if (re.search("no reading", op[1]) or
  442:                         re.search("Not Readable", op[1])):
  443                      assert op[2] == "ns", op

  466              for op in status_list:
  467:                 if (re.search("no reading", op[1]) or
  468:                         re.search("Not Readable", op[1])):
  469                      assert op[2] == "ns", op

  496              for op in status_list:
  497:                 if (re.search("no reading", op[1]) or
  498:                         re.search("Not Readable", op[1])):
  499                      assert op[2] == "ns", op

  524              for op in status_list:
  525:                 if (re.search("no reading", op[1]) or
  526:                         re.search("Not Readable", op[1])):
  527                      assert op[2] == "ns", op

portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\hwtool\tests_hwtool.py:
  1173          logger.info("Actual Output: [" + actual_output + "]")
  1174:         elements = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)", actual_output)
  1175          # Validating CPU core count

  1265              # Verifying Slots
  1266:             elements = re.search(r"Slot\s+(\d+):\s\.{10}\s([^,]*),\s(.*)",
  1267                                   line)

  1275                  # Verifying Hardware revision
  1276:                 elements = re.search(r"Hardware revision:\s+([\d\D]+)", line)
  1277                  if elements is not None:

  1279                  else:
  1280:                     elements = re.search(r"Mainboard:\s[^,]*,\s(.*)", line)
  1281                      if elements is not None:

  1338              system_section = section
  1339:     elements = re.search(r".*Product\s*:\s*(.*)", system_section)
  1340      actual_motherboard_number = elements.group(1)

  1445          for line in lines:
  1446:             if re.search(r"disk.*", line) is not None:
  1447                  elements = line.split()

  1458          for line in lines:
  1459:             if re.search(r"\w", line):
  1460                  elements = line.split()

portfolio-system-tests\portfolio_system_tests\legacy_exchange_tests\tests\test_allocation_health.py:
   64  
   65:         match = re.search(r'received, (?P<loss>\d+.*)\s*% packet loss,',
   66                            output)

  145                r'\s*% loss\)')
  146:     match = re.search(target, output)
  147      if not match:

portfolio-system-tests\portfolio_system_tests\legacy_exchange_tests\tests\test_smoke_mess.py:
  38      ITEMS_RE = r'ItemsInFolder\s+-------------\s+(?P<items>\d+)'
  39:     match = re.search(ITEMS_RE, output)
  40      return int(match.group('items'))

portfolio-system-tests\portfolio_system_tests\legacy_gluon\libs\__init__.py:
  360      # Example: "hostname":"XNCC58DC4E4D4408",
  361:     sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  362      if not sobj:

portfolio-system-tests\portfolio_system_tests\legacy_gluon\tests\test_firewall_rules_after_failover_vgw.py:
  127      regex = re.escape(str1) + r'\n(.*)$'
  128:     sobj1 = re.search(regex, output, re.MULTILINE | re.DOTALL)
  129      if sobj1:

  182      # Format of uptime: 35d  0h  54m
  183:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  184      if not sobj:

portfolio-system-tests\portfolio_system_tests\legacy_gluon\tests\test_firewall_rules_after_reboot_vgw.py:
  126      regex = re.escape(str1) + r'\n(.*)$'
  127:     sobj1 = re.search(regex, output, re.MULTILINE | re.DOTALL)
  128      if sobj1:

  191          # Example: "hostname":"XNCC58DC4E4D4408",
  192:         sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  193          if not sobj:

  223      # Format of uptime: 35d  0h  54m
  224:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  225      if not sobj:

portfolio-system-tests\portfolio_system_tests\legacy_gluon\tests\test_internet_and_site_to_site.py:
  123      # Example: "hostname":"XNCC58DC4E4D4408",
  124:     sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  125      if not sobj:

  363      # Resolving facebook.com (facebook.com)... 31.13.90.36, 2a03..
  364:     sobj = re.search(r'\(facebook\.com\)\.\.\.\s+(.*),', lines[2])
  365      if sobj:

  407      # Resolving youtube.com (youtube.com)... 216.58.194.206, 2607
  408:     sobj = re.search(r'\(youtube\.com\)\.\.\.\s+(.*),', lines[2])
  409      if sobj:

  450      # Format of uptime: 35d  0h  54m
  451:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  452      if not sobj:

portfolio-system-tests\portfolio_system_tests\legacy_gluon\tests\test_overnight_failover_pingpong.py:
  78  
  79:     match = re.search(r'(?<=\()\S+?(?=\) port \d+)', output)
  80      if match:

portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\conftest.py:
  397  
  398:     if re.search("different_unique_ib_ob", test_case):
  399          logger.info("[INFO]: cleanup after different_unique_ib_ob")

  496          for line in profile_data.raw.split("\n"):
  497:             result = re.search(r"(\*\w+\*)\s+\d+\s+(\d+)\s+(\d+)",
  498                                 profile_data.raw)

  518      """
  519:     if re.search("same_default_ib_ob", test_case):
  520          init_qos_device_configurator.config.manage_sites(7)
  521          init_qos_device_configurator.config.manage_sites(8)
  522:     elif re.search("unique_ib_default_ob", test_case):
  523          init_qos_device_configurator.config.manage_sites(7)
  524:     elif re.search("default_ib_unique_ob", test_case):
  525          init_qos_device_configurator.config.manage_sites(8)
  526:     elif re.search("different_unique_ib_ob", test_case):
  527          init_qos_device_configurator.config.manage_profiles(9)

  549  
  550:     if re.search("same_default|default_ob", test_case):
  551:         if re.search("^.*DSCP_P$", test_case):
  552              init_qos_device_configurator.config.manage_classes(21)
  553  
  554:         if re.search("^.*DSCP_L$", test_case):
  555              init_qos_device_configurator.config.manage_classes(38)
  556  
  557:         if re.search("^.*DSCP_R$", test_case):
  558              init_qos_device_configurator.config.manage_rules(3)
  559  
  560:         if re.search("^.*DSCP_PL$", test_case):
  561              init_qos_device_configurator.config.manage_classes(21)

  563  
  564:         if re.search("^.*DSCP_PR$", test_case):
  565              init_qos_device_configurator.config.manage_classes(21)

  567  
  568:         if re.search("^.*DSCP_LR$", test_case):
  569              init_qos_device_configurator.config.manage_classes(38)

  571  
  572:         if re.search("^.*DSCP_PLR$", test_case):
  573              init_qos_device_configurator.config.manage_classes(21)

  577      else:
  578:         if re.search("^.*DSCP_P$", test_case):
  579              init_qos_device_configurator.config.manage_classes(26)
  580  
  581:         if re.search("^.*DSCP_L$", test_case):
  582              init_qos_device_configurator.config.manage_classes(34)
  583  
  584:         if re.search("^.*DSCP_R$", test_case):
  585              init_qos_device_configurator.config.manage_rules(5)
  586  
  587:         if re.search("^.*DSCP_PL$", test_case):
  588              init_qos_device_configurator.config.manage_classes(26)

  590  
  591:         if re.search("^.*DSCP_PR$", test_case):
  592              init_qos_device_configurator.config.manage_classes(26)

  594  
  595:         if re.search("^.*DSCP_LR$", test_case):
  596              init_qos_device_configurator.config.manage_classes(34)

  598  
  599:         if re.search("^.*DSCP_PLR$", test_case):
  600              init_qos_device_configurator.config.manage_classes(26)

  622  
  623:     if re.search("same_default|default_ob", test_case):
  624:         if re.search("^.*DSCP_P$", test_case):
  625              init_qos_device_configurator.config.manage_classes(25)
  626  
  627:         if re.search("^.*DSCP_L$", test_case):
  628              init_qos_device_configurator.config.manage_classes(39)
  629  
  630:         if re.search("^.*DSCP_R$", test_case):
  631              init_qos_device_configurator.config.manage_rules(4)
  632  
  633:         if re.search("^.*DSCP_PL$", test_case):
  634              init_qos_device_configurator.config.manage_classes(25)

  636  
  637:         if re.search("^.*DSCP_PR$", test_case):
  638              init_qos_device_configurator.config.manage_classes(25)

  640  
  641:         if re.search("^.*DSCP_LR$", test_case):
  642              init_qos_device_configurator.config.manage_classes(39)

  644  
  645:         if re.search("^.*DSCP_PLR$", test_case):
  646              init_qos_device_configurator.config.manage_classes(25)

  650      else:
  651:         if re.search("^.*DSCP_P$", test_case):
  652              init_qos_device_configurator.config.manage_classes(30)
  653  
  654:         if re.search("^.*DSCP_L$", test_case):
  655              init_qos_device_configurator.config.manage_classes(35)
  656  
  657:         if re.search("^.*DSCP_R$", test_case):
  658              init_qos_device_configurator.config.manage_rules(6)
  659  
  660:         if re.search("^.*DSCP_PL$", test_case):
  661              init_qos_device_configurator.config.manage_classes(30)

  663  
  664:         if re.search("^.*DSCP_PR$", test_case):
  665              init_qos_device_configurator.config.manage_classes(30)

  667  
  668:         if re.search("^.*DSCP_LR$", test_case):
  669              init_qos_device_configurator.config.manage_classes(35)

  671  
  672:         if re.search("^.*DSCP_PLR$", test_case):
  673              init_qos_device_configurator.config.manage_classes(30)

portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_inbound_qos_dscp_full_combinations.py:
   89      try:
   90:         if re.search("same_default|default_ob", test_case):
   91              init_qos_device_configurator.config.manage_classes(37)
   92  
   93:             if re.search("unique_ib_default_ob", test_case):
   94                  qos = init_qos_device_configurator.config.\

  119  
  120:             if re.search("^.*DSCP_P$", test_case):
  121                  expected_ob_qos_dscp = 0
  122  
  123:             if re.search("^.*DSCP_L$", test_case):
  124                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  125  
  126:             if re.search("^.*DSCP_R$", test_case):
  127                  expected_ob_qos_dscp = default_outbound_dscp_rule
  128  
  129:             if re.search("^.*DSCP_PL$", test_case):
  130                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  131  
  132:             if re.search("^.*DSCP_PR$", test_case):
  133                  expected_ob_qos_dscp = default_outbound_dscp_rule
  134  
  135:             if re.search("^.*DSCP_LR$", test_case):
  136                  expected_ob_qos_dscp = default_outbound_dscp_rule
  137  
  138:             if re.search("^.*DSCP_PLR$", test_case):
  139                  expected_ob_qos_dscp = default_outbound_dscp_rule

  143  
  144:             if re.search("default_ib_unique_ob", test_case):
  145                  qos = init_qos_device_configurator.config.\

  148  
  149:             elif re.search("different_unique_ib_ob", test_case):
  150                  qos = init_qos_device_configurator.config.\

  175  
  176:             if re.search("^.*DSCP_P$", test_case):
  177                  expected_ob_qos_dscp = 0
  178  
  179:             if re.search("^.*DSCP_L$", test_case):
  180                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  181  
  182:             if re.search("^.*DSCP_R$", test_case):
  183                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  184  
  185:             if re.search("^.*DSCP_PL$", test_case):
  186                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  187  
  188:             if re.search("^.*DSCP_PR$", test_case):
  189                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  190  
  191:             if re.search("^.*DSCP_LR$", test_case):
  192                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  193  
  194:             if re.search("^.*DSCP_PLR$", test_case):
  195                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  281  
  282:         if re.search("same_default|default_ob", test_case):
  283              init_qos_device_configurator.config.manage_rules(7)

portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_outbound_qos_dscp_full_combinations.py:
   89      try:
   90:         if re.search("same_default|default_ob", test_case):
   91              init_qos_device_configurator.config.manage_classes(37)

  113  
  114:             if re.search("^.*DSCP_P$", test_case):
  115                  expected_ob_qos_dscp = 0
  116  
  117:             if re.search("^.*DSCP_L$", test_case):
  118                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  119  
  120:             if re.search("^.*DSCP_R$", test_case):
  121                  expected_ob_qos_dscp = default_outbound_dscp_rule
  122  
  123:             if re.search("^.*DSCP_PL$", test_case):
  124                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  125  
  126:             if re.search("^.*DSCP_PR$", test_case):
  127                  expected_ob_qos_dscp = default_outbound_dscp_rule
  128  
  129:             if re.search("^.*DSCP_LR$", test_case):
  130                  expected_ob_qos_dscp = default_outbound_dscp_rule
  131  
  132:             if re.search("^.*DSCP_PLR$", test_case):
  133                  expected_ob_qos_dscp = default_outbound_dscp_rule

  158  
  159:             if re.search("^.*DSCP_P$", test_case):
  160                  expected_ob_qos_dscp = 0
  161  
  162:             if re.search("^.*DSCP_L$", test_case):
  163                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  164  
  165:             if re.search("^.*DSCP_R$", test_case):
  166                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  167  
  168:             if re.search("^.*DSCP_PL$", test_case):
  169                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  170  
  171:             if re.search("^.*DSCP_PR$", test_case):
  172                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  173  
  174:             if re.search("^.*DSCP_LR$", test_case):
  175                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  176  
  177:             if re.search("^.*DSCP_PLR$", test_case):
  178                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  250  
  251:         if re.search("same_default|default_ob", test_case):
  252              init_qos_device_configurator.config.manage_rules(7)

portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_qos_device_all_classification.py:
  213      """
  214:     if re.search('-sh', test_case):
  215          check_qos_on_IC = 0

  217  
  218:     elif re.search('-ic', test_case):
  219          check_qos_on_IC = 1

  224  
  225:     if re.search('-IN', test_case):
  226          QoS_Flags = 1

  233  
  234:     elif re.search('-OUT', test_case):
  235          QoS_Flags = 0

  242  
  243:     if re.search('-UniqueSite', test_case):
  244          is_UniqueSite = 1

  247  
  248:     elif re.search('-DefaultSite', test_case):
  249          is_UniqueSite = 0

  294      try:
  295:         if re.search('same_unique_ib_ob', test_case):
  296              # The same unique profile is used for Inbound and outbound.

  309  
  310:         elif re.search('same_default_ib_ob', test_case):
  311              # Default profile is used for both Inbound and outbound traffic.

  325  
  326:         elif re.search('default_ib_unique_ob', test_case):
  327              # Default profile is used for inbound and

  342  
  343:         elif re.search('unique_ib_default_ob', test_case):
  344              # Default profile is used for outbound and

  358  
  359:         elif re.search('different_unique_ib_ob', test_case):
  360              # Different unique profiles for outbound and inbound traffic.

  431              # Checking for optimized or passthrough traffic
  432:             if re.search('-noOpt', test_case):
  433                  verify_opt(sh_resource=test_objects.client_sh,

  439  
  440:             elif re.search('-Opt', test_case):
  441                  verify_opt(sh_resource=test_objects.client_sh,

portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_qos_dscp_full_combinations.py:
   88      try:
   89:         if re.search("same_default|default_ob", test_case):
   90              init_qos_device_configurator.config.manage_classes(37)
   91  
   92:             if re.search("unique_ib_default_ob", test_case):
   93                  qos = init_qos_device_configurator.config.\

  123  
  124:             if re.search("^.*DSCP_P$", test_case):
  125                  expected_ob_qos_dscp = 0
  126  
  127:             if re.search("^.*DSCP_L$", test_case):
  128                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  129  
  130:             if re.search("^.*DSCP_R$", test_case):
  131                  expected_ob_qos_dscp = default_outbound_dscp_rule
  132  
  133:             if re.search("^.*DSCP_PL$", test_case):
  134                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  135  
  136:             if re.search("^.*DSCP_PR$", test_case):
  137                  expected_ob_qos_dscp = default_outbound_dscp_rule
  138  
  139:             if re.search("^.*DSCP_LR$", test_case):
  140                  expected_ob_qos_dscp = default_outbound_dscp_rule
  141  
  142:             if re.search("^.*DSCP_PLR$", test_case):
  143                  expected_ob_qos_dscp = default_outbound_dscp_rule

  147  
  148:             if re.search("default_ib_unique_ob", test_case):
  149                  qos = init_qos_device_configurator.config.\

  152  
  153:             elif re.search("different_unique_ib_ob", test_case):
  154                  qos = init_qos_device_configurator.config.\

  184  
  185:             if re.search("^.*DSCP_P$", test_case):
  186                  expected_ob_qos_dscp = 0
  187  
  188:             if re.search("^.*DSCP_L$", test_case):
  189                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  190  
  191:             if re.search("^.*DSCP_R$", test_case):
  192                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  193  
  194:             if re.search("^.*DSCP_PL$", test_case):
  195                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  196  
  197:             if re.search("^.*DSCP_PR$", test_case):
  198                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  199  
  200:             if re.search("^.*DSCP_LR$", test_case):
  201                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  202  
  203:             if re.search("^.*DSCP_PLR$", test_case):
  204                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  300  
  301:         if re.search("same_default|default_ob", test_case):
  302              init_qos_device_configurator.config.manage_rules(7)

portfolio-system-tests\portfolio_system_tests\legacy_netint_tests\tests\legacy\Securetransport\sectp_ms2_nat_integ.py:
  31      """
  32:     m = re.search(r"Runner - Tests planned:\s+(\d+)", log)
  33      planned_tc = m.group(1)
  34:     m = re.search(r"Runner - Tests passed:\s+(\d+)", log)
  35      passed_tc = m.group(1)

  47      """
  48:     match = re.search(r"1 passed in (\d+)", log)
  49      if match:

portfolio-system-tests\portfolio_system_tests\legacy_ns\service_chain_manager\service_chain_manager\test\orclibs\traffic_parser.py:
  51      hwaddr = None
  52:     eth_match = re.search(r'(ether|HWaddr)\s(?:addr:)*(\S+)', output)
  53      if eth_match:

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\ibt\tests\Guest_Zone_Support\test_local_internet_breakout.py:
  79      for line in output_lines:
  80:         maskmatch = re.search(r'\s' + interface, line, re.IGNORECASE)
  81          if maskmatch:

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\cf3\DHCP_DNS\test_DHCP_relay_via_overlay_to_DC.py:
   90      for zone in zones:
   91:         if re.search(site_1['name'], zone.site):
   92              branch_net = zone.networks[0]

  130          for zone in zones:
  131:             if re.search(site_1['name'], zone.site):
  132                  configurator.scm_actor.config.change_network(

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\cf3\QoS\test_aggregate_traffic_with_mixed_traffic_class.py:
  115      for line in output.split("\n"):
  116:         bandwidth = re.search(r'\d+\.\d+mbps', line)
  117          if not bandwidth:

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_add_new_tep_ips_in_dc_uplinks.py:
  205          for dcuplink in dc_old_wan_teps:
  206:             if re.search('Internet', dcuplink):
  207                  public_ipv4 = str(resources.dc_public.cidr.ip)

  266          for dcuplink in dc_old_wan_teps:
  267:             if re.search('Internet', dcuplink):
  268                  public_ipv4 = str(resources.dc_public.cidr.ip)

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_data_ports_poweroff_update.py:
  215      for port in data_ports:
  216:         if re.search('PORT3', port.id, flags=re.IGNORECASE) or \
  217:                 re.search('PORT4', port.id, flags=re.IGNORECASE):
  218              resources.scm_actor.change_port(

  226          for port in data_ports:
  227:             if re.search('PORT3', port.id, flags=re.IGNORECASE) or \
  228:                     re.search('PORT4', port.id, flags=re.IGNORECASE):
  229                  resources.scm_actor.change_port(

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover_CF3.py:
  235      for zone in zone_list:
  236:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  237              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  251      for uplink in uplink_list:
  252:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  253:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  254                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  379          for zone in zones_list:
  380:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  381                  obj_added_zone = zone

  399                  for custom_app in custom_apps:
  400:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  401                                   flags=re.IGNORECASE):

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover.py:
  237      for zone in zone_list:
  238:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  239              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  253      for uplink in uplink_list:
  254:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  255:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  256                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  388          for zone in zones_list:
  389:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  390                  obj_added_zone = zone

  408                  for custom_app in custom_apps:
  409:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  410                                   flags=re.IGNORECASE):

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_leaf_site_checking_in_site_pool.py:
  440      for site in sites_lists:
  441:         if re.search('HQ', site.name):
  442              hq_site_name = site.name

  467          for dc_uplink in dc_uplinks:
  468:             if re.search(INTERNET,
  469                           dc_uplink.wan,

  709          for dc_uplink in dc_uplinks:
  710:             if re.search(INTERNET,
  711                           dc_uplink.wan,

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch_CF3.py:
  135      for zone in zone_list:
  136:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  137              zone_network = scm_actor.get_network(zone.networks[0])

  146      for uplink in uplink_list:
  147:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  148:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  149                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  176          for zone in zones_list:
  177:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  178                  obj_added_zone = zone

  192                  for custom_app in custom_apps:
  193:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  194                                   flags=re.IGNORECASE):

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch.py:
  135      for zone in zone_list:
  136:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  137              zone_network = scm_actor.get_network(zone.networks[0])

  146      for uplink in uplink_list:
  147:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  148:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  149                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  176          for zone in zones_list:
  177:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  178                  obj_added_zone = zone

  192                  for custom_app in custom_apps:
  193:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  194                                   flags=re.IGNORECASE):

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_size_change_for_site_moves.py:
  445      for site in sites_lists:
  446:         if re.search('HQ', site.name):
  447              hq_site_name = site.name

  473          for dc_uplink in dc_uplinks:
  474:             if re.search(INTERNET,
  475                           dc_uplink.wan,

  758          for dc_uplink in dc_uplinks:
  759:             if re.search(INTERNET,
  760                           dc_uplink.wan,

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch_CF3.py:
  264      for zone in zone_list:
  265:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  266              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  280      for uplink in uplink_list:
  281:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  282:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  283                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  402          for zone in zones_list:
  403:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  404                  obj_added_zone = zone

  422                  for custom_app in custom_apps:
  423:                     if re.search('CAT_CUSTOM_UDP',
  424                                   custom_app.name,

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch.py:
  264      for zone in zone_list:
  265:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  266              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  280      for uplink in uplink_list:
  281:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  282:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  283                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  403          for zone in zones_list:
  404:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  405                  obj_added_zone = zone

  423                  for custom_app in custom_apps:
  424:                     if re.search(
  425                          'CAT_CUSTOM_UDP',

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_dc_uplink.py:
  259      for dc_uplink in dc_uplinks:
  260:         if re.search(WAN,
  261                       dc_uplink.wan,

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_wan_CF3.py:
  304      for zone in zone_list:
  305:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  306              zone_obj = copy.copy(zone)

  317      for uplink in uplink_list:
  318:         if re.search(WAN, uplink.wan, flags=re.IGNORECASE):
  319              branch_name = test_objects.scm_actor.get_site(

  457          for wan_data in wans:
  458:             if re.search(WAN, wan_data.name, flags=re.IGNORECASE):
  459                  wan_id = wan_data.id

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_wan.py:
  308      for uplink in uplink_list:
  309:         if re.search(WAN, uplink.wan, flags=re.IGNORECASE):
  310              branch_name = test_objects.scm_actor.get_site(

  440          for wan_data in wans:
  441:             if re.search(WAN, wan_data.name, flags=re.IGNORECASE):
  442                  wan_id = wan_data.id

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone_CF3.py:
  193      output = shell.exec_command("cat /var/last_received_cdl.yaml")
  194:     match = re.search('subnet: ' + ipv4, output, flags=re.IGNORECASE)
  195      if match:

  209          output = shell.exec_command("ip rule list")
  210:         match = re.search(ipv4, output)
  211          if match:

  244      for zone in zone_list:
  245:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  246              # Getting old zone ip

  378          for custom_app in custom_apps:
  379:             if re.search('CAT_CUSTOM_UDP', custom_app.name,
  380                           flags=re.IGNORECASE):

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone.py:
  195      output = shell.exec_command("cat /var/last_received_cdl.yaml")
  196:     match = re.search('subnet: ' + ipv4, output, flags=re.IGNORECASE)
  197      if match:

  209          output = shell.exec_command("ip rule list")
  210:         match = re.search(ipv4, output)
  211          if match:

  245      for zone in zone_list:
  246:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  247              # Getting old zone ip

  379          for custom_app in custom_apps:
  380:             if re.search(
  381                  'CAT_CUSTOM_UDP',

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_uplink_wantype.py:
  357          # Example old_wan_name='Wan1',dc_uplink.wan='wan-Wan1-e63d40e499c3f0ab'
  358:         if re.search(old_wan_name,
  359                       dc_uplink.wan,

  395          # path_rule.path_preference[0]='wan-Wan1-e63d40e499c3f0ab'
  396:         if re.search(wan_name,
  397                       path_rule.path_preference[0],

  439          # Example uplink.name: "Wan1_Uplink"
  440:         if re.search(r'\bWan1_Uplink\b',
  441                       uplink.name,

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_wan_uplink_ipaddress.py:
  284      for uplink in uplink_list:
  285:         if re.search(WAN, uplink.name, flags=re.IGNORECASE):
  286              return uplink.name

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_zone_for_branch.py:
  181              for network_obj in network_list:
  182:                 if re.search(BRANCH, network_obj.site):
  183                      return network_obj

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_change_panther_db_address.py:
  147      for route in ic_ip_routes:
  148:         if re.search(network, route):
  149              flag = True

  161      for route in ic_ip_routes:
  162:         if re.search(network, route):
  163              flag = False

  279      for cluster_obj in clusters:
  280:         if re.search('Cluster1', cluster_obj.name, flags=re.IGNORECASE):
  281              old_proxy_ip = cluster_obj.proxy_ip

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_check_route_table.py:
  115      for route in ic_ip_routes:
  116:         if re.search(network, route):
  117              flag = True

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_int_service_restart.py:
  166      result = ic.show_info().raw
  167:     if re.search(status, str(result), flags=re.IGNORECASE):
  168          flag = True

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_modify_branch_subnet.py:
  207              for network_obj in network_list:
  208:                 if re.search(BRANCH, network_obj.site):
  209                      return network_obj

  225      for route in ic_ip_routes:
  226:         if re.search(network, route):
  227              flag = True

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\services\test_symmetrical_nat_port_dynamic_change.py:
  139      for uplink in uplink_list:
  140:         if re.search(r'\bWan1_Uplink\b',
  141                       uplink.name,

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_as_mismatch.py:
  126              shell.exec_command("grep remote_as /var/last_received_cdl.yaml")
  127:         hold = re.search('remote_as: 200', output)
  128          logger.info(output)

  167      logger.info(output)
  168:     holdtime = re.search('remote_as: 100', output)
  169      assert holdtime

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_nondefaults.py:
  124              "grep hold_time /var/last_received_cdl.yaml")
  125:         hold = re.search('hold_time: 10', output)
  126          logger.info(output)

  129              "grep keepalive_time /var/last_received_cdl.yaml")
  130:         keep = re.search('keepalive_time: 80', output)
  131          assert keep

  171      logger.info(output)
  172:     holdtime = re.search('hold_time: 60', output)
  173      assert holdtime

  175          "grep keepalive_time /var/last_received_cdl.yaml")
  176:     keep = re.search('keepalive_time: 180', output)
  177      assert keep

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_match.py:
  163              "grep password /var/last_received_cdl.yaml")
  164:         pword = re.search('password: thepassword', output)
  165          logger.info(output)

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_mismatch.py:
  139              "grep password /var/last_received_cdl.yaml")
  140:         pword = re.search('password: password', output)
  141          logger.info(output)

  189      logger.info(output)
  190:     pword = re.search('password: null', output)
  191      assert pword

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_ibgp_peering_on_wdr1_fails.py:
  327      for network in networks:
  328:         if not re.search('HQ', network.site):
  329              network_list.append(network.netv4)

  335          for subnet in subnet_splitted_list:
  336:             if not re.search(str(subnet), network, re.IGNORECASE):
  337                  higher_subnet_list.append(str(subnet))

portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_subnet_splitting.py:
  227      for cluster_obj in clusters:
  228:         if re.search('Cluster1', cluster_obj.name, flags=re.IGNORECASE):
  229              cluster_id = cluster_obj.id

  288      for network in networks:
  289:         if not re.search('HQ', network.site):
  290              network_list.append(network.netv4)

  296          for subnet in subnet_splitted_list:
  297:             if not re.search(str(subnet), network, re.IGNORECASE):
  298                  higher_subnet_list.append(str(subnet))

portfolio-system-tests\portfolio_system_tests\legacy_scm_tests\legacy_tests\test_gw_via_rest\test_gw_via_rest.py:
  114      for uplink in uplinks:
  115:         if re.search('Internet', uplink.wan):
  116              continue

  204          uplink = scm_actor.config.get_uplink(uplink_id)
  205:         if re.search('Internet', uplink.wan):
  206              continue

portfolio-system-tests\portfolio_system_tests\legacy_shm_tests\shm_helper.py:
  122              # command output
  123:             app_content = re.search(search_pattern, cmd_output, re.DOTALL) \
  124                  .group(1).strip()

  142                  application_map['dest_port'] = int(dest[1])
  143:                 application_map['app_id'] = int(re.search(".*snoopy_app="
  144                                                  "(\\d+)", app).group(1)

  274              # from command output
  275:             status = re.search(search_pattern, cmd_output) \
  276                  .group(1).strip()

  302              # from command output
  303:             policy = re.search(search_pattern, cmd_output) \
  304                  .group(1).strip()

  379              wait_until_complete(timeout=WAIT_900_SECS)
  380:         result = re.search("\\[PASS\\]:", cmd_output)
  381  

  424          search_pattern = r'{(.*?)}'
  425:         product_code = re.search(search_pattern, cmd_output, re.DOTALL) \
  426              .group(1).strip()

  441          try:
  442:             return re.search(search_pattern, cmd_output, re.DOTALL) \
  443                  .group(1).strip()

portfolio-system-tests\portfolio_system_tests\legacy_shm_tests\zak\tests\conftest.py:
  180          try:
  181:             frmt_op = re.search(r"(.*?)Aliases", output,
  182                                  re.DOTALL).group(1).strip()

  187  
  188:         m = re.search("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*$", output)
  189          return (m.group(1))

portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\portal\test_allsaas_sku.py:
   63          portal_sca.action.add_platform_to_sku(SKU, 'noexist')
   64:     assert re.search("404", str(err404.value)) is not None
   65      with pytest.raises(VerificationError):

   78          portal_sca.action.add_platform_to_sku('noexist', PLATFORM)
   79:     assert re.search("404", str(err404.value)) is not None
   80      with pytest.raises(UnexpectedOutput) as another404:
   81          portal_sca.verification.verify_platforms_sku('noexist', PLATFORM)
   82:     assert re.search("404", str(another404.value)) is not None
   83  

   94          portal_sca.verification.verify_platforms_sku('nonexist', [PLATFORM])
   95:     assert re.search("404", str(err404.value)) is not None
   96  

  107          portal_sca.action.delete_platform_from_sku('noexist', PLATFORM)
  108:     assert re.search("404", str(err404.value)) is not None
  109  

  122              portal_sca.action.delete_platform_from_sku(SKU, valid_platform)
  123:         assert re.search("404", str(err404.value)) is not None
  124  

portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\portal\test_platforms.py:
  243                                         test_params.send_beta_fields)
  244:     assert re.search("400", str(err400.value)) is not None
  245  

  373              test_params.send_beta_fields)
  374:     assert re.search("400", str(err400.value)) is not None
  375  

portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_hostlabel.py:
  228              # Extract class b address from resolved ips
  229:             subnet_extract = re.search(r"(^\d{1,3}\.\d{1,3})*",
  230                                         ip_address)

portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\sepia\conftest.py:
   88      # get the md5 checksum value
   89:     checksum = re.search(r'([0-9a-fA-F]+)\s+', output)
   90      if (not checksum):

   98      # extract the filename from url for checksum
   99:     match_obj = re.search("//.*/(.*)$", url)
  100      server_file = SERVER_FILE_LOCATION + match_obj.group(1)

  136                  # Extract class A address from resolved ips
  137:                 subnet_extract = re.search(r"(^\d{1,3}\.)",
  138                                             ip_address)

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\scripts\connect_to_scc.py:
   61          cmc_version_string = cmc_cli.exec_command('show info')
   62:         cmc_version = re.search(
   63              r'Version:.*',

   65                  'Version:', '').strip(r' \n\r\t')
   66:         steelhead_string = re.search(r'Steelheads.*\n\n\n',
   67                                       output,

   74          for steelhead in steelheads:
   75:             serial = re.search(r'Steelhead \w*', steelhead).\
   76                  group(0).replace('Steelhead ', '')
   77  
   78:             hostname = re.search(
   79                  r'\(.* /', steelhead).group(0).strip(r'(/ \n\t\r')
   80  
   81:             ip_addr = re.search(r'\d+\.\d+\.\d+\.\d+', steelhead).group(0)
   82  
   83:             ver_string = re.search(r'Version:.*', steelhead).\
   84                  group(0).replace('Version:', '').strip(r' \n\t\r')
   85:             version = re.search(r'\d+\.\d+\.\d+', ver_string).group(0)
   86  

   89                  ocs_connectivity = False
   90:                 connectivity = re.search(r'Connected:.*', steelhead).\
   91                      group(0).replace('Connected:', '').strip(r' \n\t\r')

   96                  ocs_connectivity = False
   97:                 connectivity = re.search(
   98                      r'SSH connection:.*', steelhead).group(0).\

  101                      gcl_connectivity = True
  102:                 connectivity = re.search(
  103                      r'HTTPS connection:.*', steelhead).group(0).\

  107  
  108:             build_no = re.search(r'#\d+', ver_string).group(0)
  109  
  110:             model = re.search(r'Model:.*', steelhead).\
  111                  group(0).replace('Model:', '').strip(r' \n\t\r')

  165      output = appl_cli.exec_command("show info")
  166:     serial = re.search(
  167          r'Serial:.*', output).group(0).replace('Serial:', '').strip(r' \n\t\r')

  169      output = appl_cli.exec_command("show cmc")
  170:     line = re.search(r'CMC hostname:.*', output).group(0)
  171      try:
  172:         current_cmc = re.search(r'\d+\.\d+\.\d+\.\d+', line).group(0)
  173      except Exception:

  257          output = appl_cli.exec_command("show cmc")
  258:         managed = re.search(r'Managed by CMC:.*', output).group(0).\
  259              replace('Managed by CMC:', '').strip(r' \n\t\r')
  260:         next_msg = re.search(r'Seconds until next message is sent:.*', output)
  261:         line = re.search(r'CMC hostname:.*', output).group(0)
  262          current_cmc_host = re.sub(

  266  
  267:         current_cmc_ip = re.search(r'\d+\.\d+\.\d+\.\d+',
  268                                     line).group(0).strip(r' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\scripts\install_image.py:
  63      for line in pipe.stdout:
  64:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  65                  is not None):

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\conftest.py:
  169          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  170:         serial = re.search(r'Serial:.*', info_string).group(0).\
  171              replace('Serial:', '').strip(' \n\t\r')

  186          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  187:         serial = re.search(r'Serial:.*', info_string).group(0).\
  188              replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_hostsettings_policy_push.py:
  111      # verifing the primary and secondary dns server
  112:     sh_dns_names = re.search(r'Name server: .*\n.*\n', sh_dns_settings). \
  113          group(0).replace('Name server: ', '').strip(' \n\t\r').split('\n')

  123          model.show_web().raw
  124:     sh_proxy = re.search(r'Network Proxy:.*\n.*\n.*', sh_proxy_settings). \
  125          group(0).replace('Network Proxy:', '').strip(' \n\t\r').split('\n')
  126:     sh_proxy_name = re.search(r'Address:.*', sh_proxy[0]).group(0). \
  127          replace('Address:', '').strip(' \n\t\r')

  129          assert False, " The web proxy is not added in sh "
  130:     sh_port = re.search(r'Port:.*', sh_proxy[1]).group(0). \
  131          replace('Port:', '').strip(' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_inpath_mgmt_policy_push.py:
  123      # Verifying ipv4 inpath settings
  124:     sh_inpath_ip4 = re.search(r'IP address:.*', sh_inpath_settings).group(0).\
  125          replace('IP address:', '').strip(' \n\r\t')

  127          assert False, " IPv4 Address is not added in sh "
  128:     sh_inpath_mask = re.search(r'Netmask:.*', sh_inpath_settings).\
  129          group(0).replace('Netmask:', '').strip(' \n\r\t')

  132      # Verifying ipv6 inpath settings
  133:     sh_inpath_ip6 = re.search(
  134          r'IPv6 address:.*',

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_manage_appliances.py:
  102          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  103:         serial = re.search(r'Serial:.*', info_string).\
  104              group(0).replace('Serial:', '').strip(' \n\t\r')

  276      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  277:     serial = re.search(r'Serial:.*', info_string).\
  278          group(0).replace('Serial:', '').strip(' \n\t\r')

  317              appliance['hostname']].model.show_info().raw
  318:         health = re.search(r'Status:.*', info_text).group(0).\
  319              replace('Status:', '').strip(' \n\t\r')

  339              appliance['hostname']].model.show_info().raw
  340:         health = re.search(r'Status:.*', info_text).group(0).\
  341              replace('Status:', '').strip(' \n\t\r')

  369      info_string_1 = resources.sh_actors[sh1.hostname].model.show_info().raw
  370:     serial_1 = re.search(r'Serial:.*', info_string_1).group(0).\
  371          replace('Serial:', '').strip(' \n\t\r')

  382      info_string_2 = resources.sh_actors[sh2.hostname].model.show_info().raw
  383:     serial_2 = re.search(r'Serial:.*', info_string_2).group(0).\
  384          replace('Serial:', '').strip(' \n\t\r')

  447      info_string = resources.sh_actors[sh1.hostname].model.show_info().raw
  448:     serial = re.search(r'Serial:.*', info_string).group(0).\
  449          replace('Serial:', '').strip(' \n\t\r')

  464      status = resources.scc_actor.model.show_cmc_op_history().raw
  465:     assert 'failed' == re.search(r' *Unlock Vault *\w* *', status).\
  466          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  472      status = resources.scc_actor.model.show_cmc_op_history().raw
  473:     assert 'failed' == re.search(r' *Unlock Vault *\w* *', status).\
  474          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  480      status = resources.scc_actor.model.show_cmc_op_history().raw
  481:     assert 'success' == re.search(r' *Unlock Vault *\w* *', status).\
  482          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  518          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  519:         serial = re.search(r'Serial:.*', info_string).\
  520              group(0).replace('Serial:', '').strip(' \n\t\r')

  557          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  558:         serial = re.search(r'Serial:.*', info_string).\
  559              group(0).replace('Serial:', '').strip(' \n\t\r')

  610      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  611:     serial = re.search(r'Serial:.*', info_string).\
  612          group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_ntp_over_ipv6.py:
  48          req_ntp_servers_parsed = \
  49:             re.search(r'NTP servers:.*\n\n',
  50                        req_ntp_servers,

  76      # Get current scc date from datetme string.
  77:     current_scc_date = re.search(
  78          r'Date: .*', scc_date_time_str).\

  80      # Get current scc time from datetme string.
  81:     current_scc_time = re.search(
  82          r'Time: .*', scc_date_time_str).\

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_ntp_policy_push.py:
  106          model.show_ntp().raw
  107:     sh_ntp_servers = re.search(
  108          r'NTP servers:.*\n.*\n.*\n.*',

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_operation_history.py:
   55      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   56:     serial = re.search(r'Serial:.*', info_string).\
   57          group(0).replace('Serial:', '').strip(' \n\t\r')

  111      op_history = resources.scc_actor.model.show_cmc_op_history().raw
  112:     assert 'rbm_user' in re.search(r'\n\n.*', op_history).\
  113          group(0), 'policy push operation is logged using a different user'

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_policy_push_for_non_admin_connected_appliances.py:
   93      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   94:     serial = re.search(r'Serial:.*', info_string).\
   95          group(0).replace('Serial:', '').strip(' \n\t\r')

  202      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  203:     serial = re.search(r'Serial:.*', info_string).\
  204          group(0).replace('Serial:', '').strip(' \n\t\r')

  312      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  313:     serial = re.search(r'Serial:.*', info_string).\
  314          group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_scc_external_backup.py:
  316      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  317:     serial = re.search(r'Serial:.*', info_string).\
  318          group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_smtp_policy_push.py:
  104          model.show_email().raw
  105:     sh_smtp_name = re.search(r'Mail hub:.*', sh_email_settings).group(0).\
  106          replace('Mail hub:', '').strip(' \n\r\t')

  108          assert False, " smtp server is not added in sh "
  109:     sh_smtp_port = re.search(r'Mail hub port:.*', sh_email_settings).\
  110          group(0).replace('Mail hub port:', '').strip(' \n\r\t')

  114      for item in ['Event emails', 'Failure emails']:
  115:         sh_emails = re.search(r'' + item + '.*\n.*\n.*\n.*\n',
  116                                sh_email_settings).group(0)
  117:         sh_is_enabled = re.search(r'Enabled:.*', sh_emails).\
  118              group(0).replace('Enabled:', '').strip(' \n\r\t')

  120              assert False, sh_emails + " is not enabled "
  121:         sh_recipients = re.search(r'Recipients:.*\n.*', sh_emails).\
  122              group(0).replace('Recipients:', '').strip(' \n\r\t').split(',')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_appliance_backup_restore.py:
  67          result = resources.sh_actors[sh.hostname].model.show_banner().raw
  68:         MOTD = re.search(
  69              r'MOTD:.*', result).group(0).replace('MOTD:', '').strip(' \n\r\t')

  83          result = resources.sh_actors[sh.hostname].model.show_banner().raw
  84:         MOTD = re.search(
  85              r'MOTD:.*', result).group(0).replace('MOTD:', '').strip(' \n\r\t')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_appliance_inventory.py:
   41          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   42:         serial = re.search(r'Serial:.*', info_string).group(0).\
   43              replace('Serial:', '').strip(' \n\t\r')

  123          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  124:         serial = re.search(r'Serial:.*', info_string).\
  125              group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_generic_infrastructure_framework.py:
  125          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  126:         serial = re.search(r'Serial:.*', info_string).\
  127              group(0).replace('Serial:', '').strip(' \n\t\r')

  140          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  141:         serial = re.search(r'Serial:.*', info_string).\
  142              group(0).replace('Serial:', '').strip(' \n\t\r')

  161          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  162:         serial = re.search(r'Serial:.*', info_string).\
  163              group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_kvm_cmc_installation.py:
  178          self.kvm_host.expect(self.kvm_scc_name + r' \(config\) #')
  179:         primary_hw_address = re.search(
  180              r'HW address:.*',

  198          self.kvm_host.expect(self.FOLDER_PROMPT)
  199:         licence1 = re.search(r'\r\n.*\r\n',
  200                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  202          self.kvm_host.expect(self.FOLDER_PROMPT)
  203:         licence2 = re.search(r'\r\n.*\r\n',
  204                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  206          self.kvm_host.expect(self.FOLDER_PROMPT)
  207:         licence3 = re.search(r'\r\n.*\r\n',
  208                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  226          self.kvm_host.expect(self.kvm_scc_name + r' \(config\) #')
  227:         self.aux_ip_address = re.search(
  228              r'IP address:.*',

  233          file.close()
  234:         aux_net_mask = re.search(
  235              r'Netmask:.*',

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_physical_cmc_installation.py:
  62      for line in pipe.stdout:
  63:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  64                  is not None):

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_scc_secure_transport.py:
  182          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  183:         serial = re.search(r'Serial:.*', info_string).\
  184              group(0).replace('Serial:', '').strip(' \n\t\r')

  200          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  201:         serial = re.search(r'Serial:.*', info_string).\
  202              group(0).replace('Serial:', '').strip(' \n\t\r')

  219          resources.client_sh.hostname].model.show_info().raw
  220:     serial = re.search(r'Serial:.*', info_string).\
  221          group(0).replace('Serial:', '').strip(' \n\t\r')

  241      # Get current scc date from datetme string.
  242:     current_scc_date = re.search(
  243          r'Date: .*', current_scc_time_str).\

  245      # Get current scc time from datetme string.
  246:     current_scc_time = re.search(
  247          r'Time: .*', current_scc_time_str).\

  280      # Get current scc date from datetme string.
  281:     current_scc_date = re.search(
  282          r'Date: .*', current_scc_time_str).\

  284      # Get current scc time from datetme string.
  285:     current_scc_time = re.search(
  286          r'Time: .*', current_scc_time_str).group(0).\

  339          resources.client_sh.hostname].model.show_info().raw
  340:     serial = re.search(r'Serial:.*', info_string).\
  341          group(0).replace('Serial:', '').strip(' \n\t\r')

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_stats_operation.py:
   71          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   72:         serial = re.search(r'Serial:.*', info_string).\
   73              group(0).replace('Serial:', '').strip(' \n\t\r')

  117      # Get current scc date from datetme string.
  118:     current_scc_date = re.search(
  119          r'Date: .*', current_scc_time_str).\

  121      # Get current scc time from datetme string.
  122:     current_scc_time = re.search(
  123          r'Time: .*', current_scc_time_str).\

  156      # Get current scc date from datetme string.
  157:     current_scc_date = re.search(
  158          r'Date: .*', current_scc_time_str).\

  160      # Get current scc time from datetme string.
  161:     current_scc_time = re.search(
  162          r'Time: .*', current_scc_time_str).\

  200      # Get current scc date from datetme string.
  201:     current_scc_date = re.search(
  202          r'Date: .*', current_scc_time_str).\

  204      # Get current scc time from datetme string.
  205:     current_scc_time = re.search(
  206          r'Time: .*', current_scc_time_str).\

portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_virtual_cmc_installation.py:
  61      for line in pipe.stdout:
  62:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  63                  is not None):

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_performance\scaleperf_qa\libs\QAPerf.py:
   422                  first_run and not bi_directional:
   423:             if re.search('tx', key):
   424                  interfaces_keys.extend([key])
   425:             elif re.search('rx', key):
   426                  interfaces_keys.extend([key])

   470                              tx_data = re.compile(r'TX\sbytes:(\d+)')
   471:                             if re.search(rx_data, inter):
   472:                                 data1 = re.search(rx_data, inter)
   473                                  interface[ser + '_rx_data'] = data1.group(1)
   474:                             if re.search(tx_data, inter):
   475:                                 data2 = re.search(tx_data, inter)
   476                                  interface[ser + '_tx_data'] = data2.group(1)

   650              location = data_col + str(row)
   651:             temp = re.search(r'(\d+.*\d*)\s+\w', ws[location].value)
   652              record_tput = temp.group(1)

   694              break
   695:         # if not re.search('.+bits/sec', line):
   696          #     continue
   697  
   698:         # rate_found = re.search('Bytes\s+(\d+.*\d*)\s+(\wbits/sec)', line)
   699:         rate_found = re.search(pattern, line)
   700          if rate_found:

   750  
   751:         rate_found = re.search(pattern, line)
   752          if rate_found:

   895      for line in output_server.splitlines():
   896:         if re.search(r'iperf\s+.+', line):
   897:             output_server_new = re.search(r'(iperf\s+.+)', line)
   898              output_server = output_server_new.group(0)
   899      for line in output_client.splitlines():
   900:         if re.search(r'iperf\s+.+', line):
   901:             output_client_new = re.search(r'(iperf\s+.+)', line)
   902              output_client = output_client_new.group(0)

   927  
   928:         if re.search(r'8\.\d\.\d\.\s+Ethernet\s+Frame\s+Rates', row) or found:
   929              found = True
   930:             if re.search(
   931                      r'\d+\.*\d*\',\s+\'(\d+,*\d*\.*\d*)\',\s+\''
   932                      r'(\d*,*\d+\.*\d*)\'', row):
   933:                 data_new = re.search(
   934                      r'\d+\.*\d*\',\s+\'(\d+,*\d*\.*\d*)\',\s+\''

   941  
   942:         if re.search(r'8\.\d\.\d\.\d\.\sEthernet\s+Frame\s+Rates:\s1', row) \
   943                  and data_count:

  1800      regex = re.compile(r'(\w+)\s*(\d+)/(\d+)')
  1801:     if re.search(regex, untagged):
  1802:         untagged_data = re.search(regex, untagged)
  1803          slot = untagged_data.group(2)

  2250              break
  2251:         if re.search(pattern_loss, line):
  2252:             drop_rate = re.search(pattern_loss, line)
  2253              percent = float(drop_rate.group(1))
  2254              total_percent += percent
  2255:         if re.search(pattern_rate, line):
  2256:             rec_rate = re.search(pattern_rate, line)
  2257              rate_int = float(rec_rate.group(1))

  2316              break
  2317:         if re.search(pattern, line):
  2318              total_checked_count += 1
  2319:             drop_rate = re.search(pattern, line)
  2320              total_bytes = drop_rate.group(1)

  2327              total_percent += percent
  2328:         if re.search(pattern_sum, line):
  2329              sum_count += 1
  2330:             sum_rate = re.search(pattern_sum, line)
  2331              sum_int = float(sum_rate.group(2))

  2354      """
  2355:     rate = re.search(r'-B\s*(\d+)(\w{1,2})', client_opt)
  2356      old_rate = rate.group(1) + rate.group(2)

  2376      """
  2377:     rate = re.search(r'-b\s*(\d+)(\w{1,3})', client_opt)
  2378      old_rate = rate.group(1) + rate.group(2)

  2403      """
  2404:     rate = re.search(r'-b\s*(\d+)', bw_rate)
  2405      client_opt_rate = str(int(rate.group(1)))

  3176  
  3177:         if re.search(pattern, line):
  3178:             found = re.search(pattern, line)
  3179              new_rate = str(float(found.group(1)) * REDUCE_TRAFFIC_80_PERCENT)

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\add_additional_outbound_rules.py:
  75          total_rule_count += 1
  76:         m = re.search(r'Pod(\d+)_vgw_branch(\d+)_obrule(\d+)', rule['name'])
  77          if m:

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\add_additional_trafficpath_rules.py:
  78          total_rule_count += 1
  79:         m = re.search(r'Pod(\d+)_vgw_branch(\d+)_tpr(\d+)', rule['name'])
  80          if m:

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
  46      """
  47:     if (re.search(
  48          r'One or more ports have an IP allocation from this subnet',

  63      # the router UUID first and then deleting the stack
  64:     elif (re.search(
  65            r'it is required by one or more routes', delete_status)):

portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\test_system_info_from_scm.py:
  216      for line in f:
  217:         if re.search(r'runsv nginx', line):
  218              process_data = line.split()

  229      for line in f:
  230:         if re.search(r'runsv postgresql', line):
  231              process_data = line.split()

  242      for line in f:
  243:         if re.search(r'runsv redis', line):
  244              process_data = line.split()

  255      for line in f:
  256:         if re.search(r'mojo/Cc.pl\b\s.*hydra.*', line):
  257              process_data = line.split()

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\devices_cli.py:
  185          'ifconfig | grep ' + interface)
  186:     mac_address = re.search("HWaddr {}".format(
  187          mac_pattern), mac_details).group(1)

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\syslog.py:
  177      pat = r"prefix=\W+{}\W+".format(prefix)
  178:     match = re.search(pat, conf)
  179      assert match is not None, "prefix {} not found in gw rsyslog config file" \

  342      for line in lines:
  343:         if re.search(msg, line) and re.search(prefix, line) and \
  344:                 re.search("<{}>".format(priority), line) and \
  345:                 re.search(serial, line):
  346              LOGGER.info("LOG message '{}' with prefix '{}', priority '{}',"

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\traffic.py:
  177      ping_result = shell.exec_command('ping {} -c {}'.format(host, count))
  178:     host_ip = re.search(
  179          r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', ping_result).group(0)

  264          cmd, curl_command_result))
  265:     http_status = re.search("HTTP/1.1 ([0-9]{3})", curl_command_result).group(
  266          1)

portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler_client.py:
  106      ping_result = shell_default_ns(mgmt_ip, ping)
  107:     loss = re.search('([0-9]{1,3})%', ping_result).group(1)
  108      # Be more sloppy for low ping intervals, since first ping may fail

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\disjoint_wan\test_route_propagation.py:
  104      for line in tunnels:
  105:         match = re.search(r"vti(\d+\_\d+\_\d+).*remote\s"
  106                            r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

  293          # Check learned routes on CGW
  294:         if re.search(r"123\.123\.123\.0", cgw_routes):
  295              criteria += 1

  334          # Check learned routes on CGW
  335:         if re.search(r"123\.123\.123\.0", cgw_routes):
  336              fail_msg += "Route to 123.123.123.0 not retracted from CGW: "

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\disjoint_wan\helpers\utils.py:
  157      for tunnel in tunnels:
  158:         vti = re.search(r'(vti\d+_\d+_\d+)', tunnel)
  159          if vti:

  161  
  162:         remote = re.search(r'remote (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  163                             tunnel)

  167  
  168:         local = re.search(r'local (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  169                            tunnel)

  202          for line in conf:
  203:             if re.search(r"X.*{}".format(vti), line):
  204                  found += 1

  206              if found:
  207:                 check_line = re.search(
  208                      r".*checkip.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

  231      for line in lines:
  232:         top = re.search(
  233              r"^[\*\s][>\s][i\s]" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" +

  237              r"([\d\s]*)i?", line)
  238:         alt = re.search(
  239              r"^[\*\s][>\s][i\s]" + r"\s{17}" +

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_bgp_neighbor.py:
  37      for line in lines:
  38:         top = re.search(
  39              r"^[\*\s][>\s][i\s]\s" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" +

  42              r"([\d\s]*)[i\?]?", line)
  43:         alt = re.search(
  44              r"^[\*\s][>\s][i\s]" + r"\s+" +

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_default_route_originate.py:
   98      list_client = output.split('\n')
   99:     regex = re.search("\Send:\W+(\d+)\W+Recv:\W+(\d+)", list_client[0])  # noqa
  100      if regex:

  109      list_server = output.split('\n')
  110:     regex_server = re.search("Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)", list_server[0])  # noqa
  111      if regex_server:

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_dynamicrouting_bgp_bandwidth_limit.py:
  65      server_log = open(traffic.server_log_file, 'r').read()
  66:     bandwidth = re.search(r'(.\w?) Mbits/sec', server_log).group()
  67      bandwidth = bandwidth.replace('Mbits/sec', '').strip()

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_pqps.py:
  112      list_client = output.split('\n')
  113:     regex = re.search("\Send:\W+(\d+)\W+Recv:\W+(\d+)", list_client[0])  # noqa
  114      if regex:

  123      list_server = output.split('\n')
  124:     regex_server = re.search("Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)", list_server[0])  # noqa
  125      if regex_server:

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_static_routing.py:
  106      list_client = output.split('\n')
  107:     regex = re.search(r"\Send:\W+(\d+)\W+Recv:\W+(\d+)",
  108                        list_client[0])

  118      list_server = output.split('\n')
  119:     regex_server = re.search(r"Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)",
  120                               list_server[0])

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_zebos_config_check_bgp.py:
  44          elif line.strip().startswith('network') and \
  45:                 re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  46              gw_output['networks'].append(line.replace('network', '').strip())

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\conftest.py:
  119              ipPattern = re.compile(r'[0-9]+(?:\.[0-9]+){3}')
  120:             route = re.search(ipPattern, line).group()
  121              if route:

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\test_dynamic_routingwithha_gateway_link_failure.py:
  57      output = gw_shell.exec_command('imish -e "show ip route"')
  58:     if not re.search(zone_ip, output):
  59          pytest.fail("Zone ip is not present on the BGP route")
  60:     match = re.search(r'Total number of prefixes (\d+)', output)
  61      if match and int(match.group(1)) != 1:

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_new_zone_discovery.py:
  154      for element in gw_output.splitlines():
  155:         if re.search(network_ip, element):
  156              return True

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_remove_interface_from_area.py:
  105      for network in networks:
  106:         if re.search("discovered", network.name, re.IGNORECASE):
  107              count += 1

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_route_peering.py:
  46  
  47:             if re.search("Full", element):
  48                  ospf_neighbors.append(ip_address)

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_zebos_config_change.py:
  37          if line.strip().startswith('network') and \
  38:                 re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  39              gw_output['network'].append(re.findall(

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\ospf_multi_lan\test_traffic.py:
   47          for interface in if_op:
   48:             if re.search("192.168.15", if_op[interface]['addr']):
   49                  disabled_ints[router] = interface

  106      for interface in if_op:
  107:         if re.search("192.168.15", if_op[interface]['addr']):
  108              break

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\test_leaf_mode.py:
  97                  for line in chain.split('\n'):
  98:                     route = re.search('set-device ' + vti, line)
  99                      if route:

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\helpers\utils.py:
  31      for tunnel in tunnels:
  32:         vti = re.search(r'(vti\d+_\d+_\d+)', tunnel)
  33          if vti:

  35  
  36:         remote = re.search(r'remote (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  37                             tunnel)

  41  
  42:         local = re.search(r'local (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  43                            tunnel)

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\2gw_sh-1catfish-1gw\test_optimized_path_selection.py:
  175          for custom_app in custom_app_list:
  176:             if re.search("TCP_APP", custom_app.name, flags=re.IGNORECASE):
  177                  resources.org_obj.custom_app_management(

  189      for custom_app in custom_app_list:
  190:         if re.search("TCP_APP", custom_app.name, flags=re.IGNORECASE):
  191              custom_app_obj = custom_app

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\helpers\utils.py:
   138                  m = \
   139:                     re.search(r'(O\>\*|O\s\s)\s'
   140                                r'(\d+\.\d+\.\d+\.\d+\/\d+).*%s' % interface,

   142              else:
   143:                 m = re.search(r'(O\>\*|O\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)',
   144                                line)
   145          elif specific_route.lower() == 'bgp':
   146:             m = re.search(r'(B\>\*|B\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   147          elif specific_route.lower() == 'static':
   148:             m = re.search(r'(S\>\*|S\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   149          elif specific_route.lower() == 'connected':
   150:             m = re.search(r'(C\>\*|C\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   151          else:
   152:             m = re.search(r'(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   153          if m:

   202              if aspath is not None:
   203:                 m = re.search(r'(\d+\s\d+\s\d+)', line)
   204              else:
   205:                 m = re.search(r'(\d{5}\s\d{4})', line)
   206              if m is not None:

   356      for route in route_op.split("OSPF external")[1].split("\n"):
   357:         ips = re.search(r'(\d+\.\d+\.\d+\.\d+\/\d+)', route)
   358          metric_value = re.\
   359              search(r'((\[\d+\]|\[\d+/0\]|\[\d+/\d+\])\s\w+:\s\d+)', route)
   360:         type_route = re.search(r'(E\d)', route)
   361          if ips:

   902      ospf_int_output = container_shell.exec_command(cmd1)
   903:     cost = re.search(r'Cost: (\d+)', ospf_int_output)
   904:     priority = re.search(r'Priority (\d+)', ospf_int_output)
   905:     hello = re.search(r'Hello (\d+)', ospf_int_output)
   906:     dead = re.search(r'Dead (\d+)', ospf_int_output)
   907      return (cost.group(1), priority.group(1), hello.group(1), dead.group(1))

  1126      routes_info = container_shell.exec_command(cmd)
  1127:     routes_ip_info = map(lambda y: re.search(r'\s.(\d*.\d*.\d*.\d*)\s', y).
  1128                           group(0).strip(), routes_info.

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\upgrade\test_upgrade.py:
  125      print(univ_op)
  126:     latest_build_tag = re.search('binary_builds.*browse/(.+)', univ_op).\
  127          group(1)

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ospf_bgp_trio\test_ospf_failures.py:
  46      for network in networks:
  47:         if re.search("Discovered", network.name):
  48              count += 1

portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ospf_bgp_trio\test_ospf_remove_interface_from_area.py:
  151      for network in networks:
  152:         if re.search("discovered", network.name, re.IGNORECASE):
  153              count += 1

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_hardware_spec_activate.py:
   70                                                          timeout=180)
   71:                     result = re.search(r'Stopped', result)
   72                      if result:

  121                                                      timeout=180)
  122:                 result = re.search(r'Healthy', result)
  123                  if result:

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability_client_sh.py:
  148          # The model extracted is in this form "VCX (VCX10)"
  149:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  150          sh_model_found = sh_model_detected.group(1)

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability_server_sh.py:
  158          # The model extracted is in this form "VCX (VCX10)"
  159:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  160          sh_model_found = sh_model_detected.group(1)

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability.py:
  189          # The model extracted is in this form "VCX (VCX10)"
  190:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  191          sh_model_found = sh_model_detected.group(1)

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_volume_size.py:
  160          # The model extracted is in this form "VCX (VCX10)"
  161:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  162          sh_model_found = sh_model_detected.group(1)

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\openstack-tests\openstack_ops.py:
  50              for stack_name in self.stack_name_list:
  51:                 search_string=re.search(r'jenkins-Axel-VSH-CAT-\d+_\w+',stack_name)
  52                  if search_string != None:

portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\provisioning\test_user_data.py:
  360                  if "Model" in line:
  361:                     m = re.search(r"\(([A-Za-z0-9_]+)\)", line)
  362                      print("Found Model: " + m.group(1))

  485      if(not invalid):
  486:         assert re.search(re.escape(expression),show_run)
  487      else:
  488:         assert re.search(re.escape(log_expression),show_rsisinit_log)
  489:         assert not re.search(re.escape(expression),show_run)
  490  

portfolio-system-tests\portfolio_system_tests\legacy_webcache_tests\http_server_allocation.py:
  317              cli_result = Model.get(fe).show_info()
  318:             if re.search("Service needs a 'restart'", cli_result.raw, re.I):
  319                  fes_to_restart.append(fe)

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\auditoperations.py:
   53      for line in zfile:
   54:         m = re.search(r"Created key with name='([^']+)' .* operation='Create"
   55                        " root CA", line)

   65      for line in zfile:
   66:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
   67                        "keyvault for user operation='Create root CA for "

   79      for line in zfile:
   80:         m = re.search(r"Create root CA for org=([^\s]+) CN=(.*) completed by "
   81                        "user='([^']*)' with signing key name='([^']+)'", line)

   92      for line in zfile:
   93:         m = re.search("-BEGIN CERTIFICATE-.*", line)
   94          if m:

  107      for line in zfile:
  108:         m = re.search(r"Created key with name='([^']+)' .* operation="
  109                        "'Create and activate root CA", line)

  120      for line in zfile:
  121:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
  122                        "keyvault for user operation='Create and activate root "

  134      for line in zfile:
  135:         m = re.search(r"Create and activate root CA for org=([^\\s]+) CN=(.*)"
  136                        "completed by user='([^']*)' with signing key name="

  148      for line in zfile:
  149:         m = re.search("-BEGIN CERTIFICATE-", line)
  150          if m:

  164      for line in zfile:
  165:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Signed digest='([^']+)' "
  166                        "using key='([^']+)' from keyvault for user operation="

  180      for line in zfile:
  181:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Sign peering cert request for CN="
  182                        "([^']+) from requestor=([^\\s]+) completed", line)

  193      for line in zfile:
  194:         m = re.search("-BEGIN CERTIFICATE-", line)
  195          if m:

  209      for line in zfile:
  210:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Signed digest='([^']+)' using "
  211                        "key='([^']+)' from keyvault for user operation="

  225      for line in zfile:
  226:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Sign proxy cert request for "
  227                        "CN=([^']+) from requestor=([^\\s]+) completed", line)

  238      for line in zfile:
  239:         m = re.search(".*-BEGIN CERTIFICATE-.*", line)
  240          if m:

  253      for line in zfile:
  254:         m = re.search(r"Created key with name='([^']+)' .* operation="
  255                        "'Create intermediate CA CSR", line)

  265      for line in zfile:
  266:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
  267                        "keyvault for user operation='Create intermediate CA "

  279      for line in zfile:
  280:         m = re.search(r"Create intermediate CA CSR for org=([^\s]+) CN=(.*) "
  281                        "completed by user='([^']*)' with signing key name="

  293      for line in zfile:
  294:         m = re.search("-BEGIN CERTIFICATE-", line)
  295          if m:

  308      for line in zfile:
  309:         m = re.search(r".*Retrieved public key with name='([^']+)' .* "
  310                        "operation='Delete CSR", line)

  321      for line in zfile:
  322:         m = re.search(r"Deleted key='([^']+)' from keyvault for user operation"
  323                        "='Delete CSR for org=([^\\s]+) CN=([^']+)", line)

  333      for line in zfile:
  334:         m = re.search(r"Delete CSR for org=([^\s]+) CN=(.*) completed by user="
  335                        "'([^']*)' with signing key name='([^']+)'.*", line)

  350      for line in zfile:
  351:         m = re.search(r"Retrieved public key with name='([^']+)' .* "
  352                        "operation='Delete CA", line)

  363      for line in zfile:
  364:         m = re.search(r"Deleted key='([^']+)' from keyvault for user operation"
  365                        "='Delete CA for org=([^\\s]+) CN=([^']+)", line)

  375      for line in zfile:
  376:         m = re.search(r"Delete CA for org=([^\s]+) CN=(.*) completed by user"
  377                        "='([^']+)' with signing key name '([^']+)'", line)

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\azure_helper.py:
  282          pip_id = nic_params.ip_configurations[0].public_ip_address.id
  283:         pip_name = re.search(r'[^/]*$', pip_id).group(0)
  284          public_ip_address = \

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\conftest.py:
   308          output = automodel.show_peers(online_only=True)
   309:         m = re.search("Connected appliances:\\s+(\\d+)", output.raw)
   310          no_of_peers = int(m.group(1))

   318          zak_serial_no = get_zak_serial_no(scm_actor)
   319:         if (re.search(zak_serial_no, output.raw)):
   320              return 1

   414              azure_helper = AzureHelper()
   415:             zaksh_name = re.search(r'([^\s]+)', zaksh_data).group()
   416              zaksh_nic_ids = azure_helper.get_vm_nic_ids(rg, zaksh_name)
   417:             nic_name = re.search(r'[^/]*$', zaksh_nic_ids[0]).group(0)
   418              pip = azure_helper.get_nic_public_ip(rg, nic_name)

   780          output = zaksh_shell.exec_command(cmd)
   781:         curr_log = re.search(r'(\S+) file', output).group(1)
   782          logger.info(f"Current ZAKSH log level: {curr_log}")

   883          else:
   884:             m = re.search("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*$",
   885                            output)

  1173          output = automodel.show_peers(online_only=True)
  1174:         if (re.search("No connected peer", output.raw)):
  1175              return 1
  1176:         m = re.search("Connected appliances:\\s+(\\d+)", output.raw)
  1177          no_of_peers = int(m.group(1))

  1429                                    allocation=Allocation())
  1430:         zaksh_ip = re.search('(?<=\[)[^]]+(?=\])', zak_sh_data).group()  # noqa
  1431          admin_cidr = ipaddress.ip_interface(str(zaksh_ip + "/0"))

  2013              raise ValueError("There is no application token")
  2014:         app_token = re.search("(^\\S*)", value).group(0)
  2015          return app_token

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\vanautu\test_cfe_lb_none.py:
  28      assert("GLB Secondary Ports" not in output.keys())
  29:     lb_ports = re.search("(\\d+)-(\\d+)", output['load balancer port range'])
  30      port1 = int(lb_ports.group(1))

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\misc_scripts\docker_remove_oldimage.py:
  17  for line in output.splitlines():
  18:     m = re.search("quay.*bamboo.*\\s+(\\S+)\\s+(\\d+)\\s+(hours|days) ago",
  19                    line)

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
   456              try:
   457:                 lb_ip = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',
   458                                    output).group(0)

   491          assert(vm_info is not None)
   492:         output = re.search('{.*}', vm_info)
   493          assert(output)

   642          challenge_str = actor.model.cli_challenge_generate().raw
   643:         token_obj = re.search(r'Generated challenge: (.*)', challenge_str)
   644          if token_obj:

   651          output = local_shell.exec_command(cmd, timeout=TIMEOUT)
   652:         response_obj = re.search(r'cli challenge response (.*)', output)
   653          if response_obj:

   787              app_restrict_flag = \
   788:                 re.search(r'app_restriction_enable=(\S+)', out).group(1)
   789              logger.info(f"Current app restriction: {app_restrict_flag}")

   798              out = ssh_shell.exec_command(cmd)
   799:             curr_log = re.search(r'(\S+) file', out).group(1)
   800              logger.info(f"Current log level: {curr_log}")

   816                  copy_util.copy_from_host(zaksh, "/dumps/", cert_path)
   817:                 cert_file = re.search(r'[^/]*$', cert_path).group(0)
   818                  cmd = (f"sudo cp /dumps/{cert_file} /var/opt/rbt/ssl/ca/; "

  1138              output_expected=True)
  1139:         if re.search(r'active', output):
  1140              return True

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\csh_data_disks_operations.py:
  96      output = perfHelper.execute_shell_cmds_csh(csh, [cmd])
  97:     num_disks = re.search(r"(.*)$", output.decode("utf-8")).group(0)
  98      log.info(f"Number of data disks attached to CSH: {num_disks}")

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\setup_clients_servers.py:
   88          output = shell.exec_command(cmd, output_expected=True)
   89:     version = re.search(r'(\d+.\d+)', output)
   90      if version:

  171          with open('60-static.yaml', 'w') as infile:
  172:             match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}', eth0_ip).group(0)
  173              infile.write(NETPLAN.format(eth0_ip, match))

  176                      str(actor_client.resource.interfaces[f'test{eth}'].cidr.ip)
  177:                 match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}', eth_ip).group(0)
  178                  infile.write(ETH.format(eth, eth_ip, match, eth))

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\zak_cluster.py:
   67      zaksh_ip = \
   68:         re.search(r'(?<=\[)[^]]+(?=\])', zaksh_data).group()
   69      admin_cidr = ipaddress.ip_interface(str(zaksh_ip + "/0"))

  143          zahsh_name = \
  144:             re.search(r'([^\s]+)', zaksh_data).group()
  145          zaksh_resource = create_zaksh_resource(zaksh_data,

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\zaksh_setup\azure_helper.py:
  2685          for vm_nic in vm_nics_list:
  2686:             if re.search('-ul2', vm_nic.name):
  2687                  all_vm_resources["nic_uplink2"] = vm_nic.name

  2691                      all_vm_resources["subnet_uplink2"] = subnet
  2692:             elif re.search('-ul', vm_nic.name):
  2693                  all_vm_resources["nic_uplink"] = vm_nic.name

  2697                      all_vm_resources["subnet_uplink"] = subnet
  2698:             if re.search('-dl', vm_nic.name):
  2699                  all_vm_resources["nic_downlink"] = vm_nic.name

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\shm_tests\shm_helper.py:
   75          cmd_output = self.client_shell.exec_command(cmd)
   76:         status = re.search(search_pattern, cmd_output)
   77          if status:

  155          cmd_output = self.client_shell.exec_command(cmd)
  156:         app_content = re.search(search_pattern, cmd_output, re.DOTALL)
  157          if app_content:

  170              application_map['dest_port'] = int(dest[1])
  171:             application_map['app_id'] = int(re.search(".*snoopy_app="
  172                                                        "(\\d+)", app).group(1)

portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\zak_sh_troubleshoot\test_zaksh_nic_nw_acceleration.py:
   85              output = zak_sh_shell.exec_command(cmd, output_expected=True)
   86:             ipv4_address = re.search(r'inet \d+.\d+.\d+.\d+', output)
   87              assert(ipv4_address is None)

   91              output = zak_sh_shell.exec_command(cmd, output_expected=True)
   92:             ipv4_address = re.search(r'inet \d+.\d+.\d+.\d+', output)
   93              if (ipv4_address is None):

  107              assert(output is not None)
  108:             maxconn = re.search(r'net.core.somaxconn = \d+', output)
  109              fo.write("\nsomaxconn {} ".format(maxconn.group(0)))
  110:             tcpmem = re.search(r'net.ipv4.tcp_mem = \d+\s+\d+\s+\d+', output)
  111              fo.write("\ntcp_mem {} ".format(tcpmem.group(0)))
  112:             port_range = re.search(r'net.ipv4.ip_local_port_range = \d+\s+\d+',
  113                                     output)

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\configure.py:
  1768              node_name = name.strip()
  1769:             all_match = re.search(r"value: (.*) \((.*)\)", value)
  1770              if not all_match:

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\connectivity.py:
  61                  loss_re = re.compile(r'(\d*)%(?: packet)? loss')
  62:                 tx_search = tx_re.search(line)
  63:                 rx_search = rx_re.search(line)
  64:                 loss_search = loss_re.search(line)
  65                  if tx_search is not None:

  73                      r'(\d*.\d*)/(\d*.\d*)/(\d*.\d*)(?:/\d*.\d*)? ms')
  74:                 rtt_search = rtt_re.search(line)
  75                  if rtt_search is None:

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\exchange_load.py:
  221      client_resource = allocation.resources[client]
  222:     branch_suffix = re.search(r"([-]\d+)", client).group(0)
  223      sh_name = 'steelhead' + branch_suffix

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\sharepoint_load.py:
  186      client_resource = allocation.resources[client]
  187:     branch_suffix = re.search(r"([-]\d+)", client).group(0)
  188      sh_name = 'steelhead' + branch_suffix

  192  
  193:     client_suffix = re.search(r"([-]\d+)+", client)
  194      file_prefix, file_suffix = file_name.split('.')

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\verification.py:
  110          if re.match(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line) and \
  111:            re.search(r'ERR(OR)?\]', line):
  112              # Get time stamp
  113:             split = re.search(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line).group(0)
  114              date = split[1:]

  130      for line in file_contents:
  131:         if re.search(r'ERR(OR)?\]', line):
  132              error_list.append(line)

portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\wget_load.py:
  195      else:
  196:         branch_suffix = re.search(r"([-]\d+)", client).group(0)
  197          sh_name = 'steelhead' + branch_suffix

portfolio-system-tests\portfolio_system_tests\tiramisu\test_functional_sanity_win.py:
  105  
  106:     match = re.search(r'\((?P<ip>.*?)\) port \d+', output)
  107      if match:

portfolio-system-tests\portfolio_system_tests\winsec\conftest.py:
   79      # the lost percentage values.
   80:     results = re.search(r'Lost\s+=\s+(\d+)', ping_results)
   81      if results:

  902      # Matching to 'EncryptData\s+:\s+{True|False}'
  903:     enc_status = re.search(r'EncryptData\s+:\s+(\w+)',
  904                             smb_server._exec_cmd(get_cmd)).group(1)

ProjectVee\venv\Lib\site-packages\pip\_internal\wheel_builder.py:
  42      """
  43:     return bool(_egg_info_re.search(s))
  44  

ProjectVee\venv\Lib\site-packages\pip\_internal\index\package_finder.py:
  223  
  224:         match = self._py_version_re.search(version)
  225          if match:

ProjectVee\venv\Lib\site-packages\pip\_internal\models\link.py:
  162          # type: () -> Optional[str]
  163:         match = self._egg_fragment_re.search(self._url)
  164          if not match:

  172          # type: () -> Optional[str]
  173:         match = self._subdirectory_fragment_re.search(self._url)
  174          if not match:

  184          # type: () -> Optional[str]
  185:         match = self._hash_re.search(self._url)
  186          if match:

  192          # type: () -> Optional[str]
  193:         match = self._hash_re.search(self._url)
  194          if match:

ProjectVee\venv\Lib\site-packages\pip\_internal\req\constructors.py:
  332          # Handle relative file URLs
  333:         if link.scheme == 'file' and re.search(r'\.\./', link.url):
  334              link = Link(

ProjectVee\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  356                  # original file is over http
  357:                 if SCHEME_RE.search(filename):
  358                      # do a url join so relative paths work

  360                  # original file and nested file are paths
  361:                 elif not SCHEME_RE.search(req_path):
  362                      # do a join so relative paths work

ProjectVee\venv\Lib\site-packages\pip\_internal\utils\encoding.py:
  33      for line in data.split(b'\n')[:2]:
  34:         if line[0:1] == b'#' and ENCODING_RE.search(line):
  35:             result = ENCODING_RE.search(line)
  36              assert result is not None

ProjectVee\venv\Lib\site-packages\pip\_internal\vcs\subversion.py:
  151          elif data.startswith('<?xml'):
  152:             match = _svn_xml_url_re.search(data)
  153              if not match:

  168                  )
  169:                 url = _svn_info_xml_url_re.search(xml).group(1)
  170                  revs = [

ProjectVee\venv\Lib\site-packages\pip\_vendor\distro.py:
   989              # If there is no version_codename, parse it from the version
   990:             codename = re.search(r'(\(\D+\))|,(\s+)?\D+', props['version'])
   991              if codename:

  1057          props = {}
  1058:         match = re.search(r'^([^\s]+)\s+([\d\.]+)', lines[0].strip())
  1059          if match:

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\manifest.py:
  291          for name in self.allfiles:
  292:             if pattern_re.search(name):
  293                  self.files.add(name)

  311          for f in list(self.files):
  312:             if pattern_re.search(f):
  313                  self.files.remove(f)

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\util.py:
  709  def get_export_entry(specification):
  710:     m = ENTRY_RE.search(specification)
  711      if not m:

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  569                  CFLAGS = _CONFIG_VARS.get('CFLAGS', '')
  570:                 m = re.search(r'-isysroot\s+(\S+)', CFLAGS)
  571                  if m is not None:

  699                  try:
  700:                     m = re.search(r'<key>ProductUserVisibleVersion</key>\s*'
  701                                    r'<string>(.*?)</string>', f.read())

ProjectVee\venv\Lib\site-packages\pip\_vendor\distlib\_backport\tarfile.py:
  1402          # the translation to UTF-8 fails.
  1403:         match = re.search(br"\d+ hdrcharset=([^\n]+)\n", buf)
  1404          if match is not None:

ProjectVee\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  860              if (token["name"] in self.svg_allow_local_href and
  861:                 (namespaces['xlink'], 'href') in attrs and re.search(r'^\s*[^#\s].*',
  862                                                                       attrs[(namespaces['xlink'], 'href')])):

ProjectVee\venv\Lib\site-packages\pip\_vendor\urllib3\connection.py:
  191          """Send a request to the server"""
  192:         match = _CONTAINS_CONTROL_CHAR_RE.search(method)
  193          if match:

ProjectVee\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:
  281              if is_ipv6:
  282:                 match = ZONE_ID_RE.search(host)
  283                  if match:

  356      source_url = url
  357:     if not SCHEME_RE.search(url):
  358          url = "//" + url

ProjectVee\venv\Lib\site-packages\setuptools\package_index.py:
  843                  # Check for a subversion index page
  844:                 if re.search(r'<title>([^- ]+ - )?Revision \d+:', line):
  845                      # it's a subversion index page:

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\filelist.py:
  215          for name in self.allfiles:
  216:             if pattern_re.search(name):
  217                  self.debug_print(" adding " + name)

  235          for i in range(len(self.files)-1, -1, -1):
  236:             if pattern_re.search(self.files[i]):
  237                  self.debug_print(" removing " + self.files[i])

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\msvc9compiler.py:
  722                  r""".*?(?:/>|</assemblyIdentity>)""", re.DOTALL)
  723:             if re.search(pattern, manifest_buf) is None:
  724                  return None

ProjectVee\venv\Lib\site-packages\setuptools\_distutils\unixccompiler.py:
  290              cflags = sysconfig.get_config_var('CFLAGS')
  291:             m = re.search(r'-isysroot\s*(\S+)', cflags)
  292              if m is None:

ProjectVee\venv\Lib\site-packages\setuptools\command\easy_install.py:
  2095          """
  2096:         has_path_sep = re.search(r'[\\/]', name)
  2097          if has_path_sep:

sc\portfolio-system-tests\portfolio_system_tests\gelato\setup_collector_simulator_pair.py:
  109          res = shell.exec_command('virsh net-dhcp-leases default')
  110:         vm_ip_search = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
  111          if not vm_ip_search:

sc\portfolio-system-tests\portfolio_system_tests\gelato\setup_collector_simulator_stack.py:
  85          res = shell.exec_command('virsh net-dhcp-leases default')
  86:         vm_ip_search = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", res)
  87          if not vm_ip_search:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\NX_Manufacture\utils.py:
   98      one, two = os.path.split(component)
   99:     build_number = re.search(name + "-(.*?)-(.*?).noarch.rpm", two).group(2)
  100      number = ": " + str(build_number)
  101  
  102:     version = re.search(name + "-(.*?)-(.*?).noarch.rpm", two).group(1)
  103      version = ": " + str(version)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\NX_Manufacture\vm.py:
  100              vm_create_node_image_name = \
  101:                 re.search(r'(.*)\s+:\s+' + vm_product_name,
  102                            line).group(1).strip()

  174      try:
  175:         image_name = re.search(r'\|\s+' + vm_node_name + r"\s+\|\s+(.*?)\|",
  176                                 buf).group(1).strip()

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\setup_upgrade\test_upgrade_scon.py:
  126      print(univ_op)
  127:     latest_build_tag = re.search('binary_builds.*browse/(.+)', univ_op).\
  128          group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_cli.py:
   64      str_pattern = 'challenge generate(.*){}'.format(dut_serialno)
   65:     match = re.search(str_pattern, cmd_op)
   66      if match:

  475                                      replace("rvbd-testuser@", "root@")
  476:                                 match = re.search('ProxyCommand=nc -X '
  477                                                    'connect -x (.*):', val).\

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_connectivity.py:
  185              val = tunnel['ssh_help']
  186:             match = re.search(
  187                  'ProxyCommand=nc -X connect -x (.*):',

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_diverter.py:
  149      dns_output = cvm_shell.exec_command('nslookup ' + remote_host)
  150:     filter_host_ip = re.search('Address: (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', # noqa
  151                                 dns_output)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_oa_cdl_update.py:
  747                                                      new_cdl_file)
  748:             match = re.search(error_msg, output.strip())
  749              if not match:

  759                                                      new_cdl_file)
  760:             match = re.search(error_msg, output.strip())
  761              if not match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_ssh_tunnel.py:
  86                              val = tunnel['ssh_help']
  87:                             match = re.search('ProxyCommand=nc -X connect '
  88                                                '-x (.*):', val).group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_static_config.py:
  389                  continue
  390:             ipmatch = re.search(r'inet\s(?:addr:)*(\S+)', line)
  391              if ipmatch:

  394  
  395:             maskmatch = re.search(r'Mask:*\s*(\S+)', line, re.IGNORECASE)
  396              if maskmatch:

  405  
  406:             ipv6match = re.search(
  407                  r'inet6\saddr:\s([a-fA-F0-9:]+)/*(\S+)', line)

  413  
  414:             ethmatch = re.search(r'(?:(?:ether)|(?:HWaddr))\s(?:addr:)*(\S+)',
  415                                   line)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_tcpdump_on_cli.py:
  105      if state == 'RUNNING':
  106:         match = re.search(tcpdump_running_exp_str, output)
  107          if match:

  112      else:
  113:         match = re.search(tcpdump_not_running_exp_str, output)
  114          if match:

  208          logger.info("output of tcpdump command: {}".format(tcpdump_output))
  209:         match = re.search(exp_result, tcpdump_output)
  210          tcpdump_file = match.group(0)

  257              tcpdump_output = cli_instance.exec_command(tcpdump_cmd1)
  258:             match = re.search(exp_result, tcpdump_output)
  259              tcpdump_file = match.group(0)

  326          output = cli_instance.exec_command(tcpdump_stop_cmd)
  327:         match = re.search(tcpdump_stop_exp_result, output)
  328          if match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\test_troubleshoot_tool.py:
   92          data = troubleshoot_info.split('\n')
   93:         match = re.search(exp_result, data[-1])
   94          troubleshoot_tar = match.group(0)

  146              data = troubleshoot_info.split('\n')
  147:             match = re.search(exp_result, data[-2])
  148              troubleshoot_tar = match.group(0)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\nodes.py:
  661  
  662:         match = re.search(exp_result, data[-1])
  663          troubleshoot_tar = match.group(0)

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infra_nx\tests\common_lib\site_dns_lib.py:
  248      most_recent_content = lease_file_op.split("lease {")[-1]
  249:     m = re.search("option domain-name-servers (.*);", most_recent_content)
  250      if m:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_external.py:
  47          for fru in fru_list:
  48:             assert re.search("CXA-00[57]70-B020", fru['Chassis Part Number'])
  49              assert fru['Board Mfg'] == 'Advantech'

  51              assert fru['Product Name'] == 'DTATA'
  52:             assert re.search("FWA-3250-RB0[23]E?", fru['Product Part Number'])
  53      except AssertionError as e:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_fru_local.py:
  46          for fru in fru_list:
  47:             assert re.search("CXA-00[57]70-B020", fru['Chassis Part Number'])
  48              assert fru['Board Mfg'] == 'Advantech'

  50              assert fru['Product Name'] == 'DTATA'
  51:             assert re.search("FWA-3250-RB0[23]E?", fru['Product Part Number'])
  52      except AssertionError as e:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_external.py:
   26      try:
   27:         assert re.search(r"\d+", info_dict['Record Count']), \
   28              info_dict['Record Count']
   29:         assert re.search(r"\d+ bytes", info_dict['Free Space']), \
   30              info_dict['Free Space']

   56          for op in status_list:
   57:             if re.search(("fan", op[0].lower()) and
   58                           op[1].lower() != 'no reading'):
   59:                 assert re.search(r"\d+ RPM", op[1]), op
   60      except AssertionError as e:

   70          for op in status_list:
   71:             if re.search(("temp", op[0].lower()) and
   72                           op[1].lower() != 'no reading'):
   73:                 assert re.search(r"\d+ degrees C", op[1]), op
   74      except AssertionError as e:

   84          for op in status_list:
   85:             if re.search(("hdd", op[0].lower()) and
   86                           op[1].lower() != 'no reading'):
   87:                 assert re.search(r"\d+ degrees C", op[1]), op
   88      except AssertionError as e:

   98          for op in status_list:
   99:             if re.search(("cpu_dimm*", op[0].lower()) and
  100                           op[1].lower() != 'no reading'):
  101:                 assert re.search(r"\d+ degrees C", op[1]), op
  102:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  103:                 assert re.search(r"^\d+\.?\d* Volts", op[1]), op
  104      except AssertionError as e:

  114          for op in status_list:
  115:             if re.search("power", op[0].lower()):
  116:                 assert re.search(r"\d+ Watts", op[1]), op
  117      except AssertionError as e:

  142                  assert op[2] == 'ok', op
  143:                 if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  144:                     assert re.search(r"\d+ degrees C", op[4]), op
  145      except AssertionError as e:

  156              assert op[2] == 'ok'
  157:             assert re.search(r"\d+\.\d+ Volts", op[4]), op
  158      except AssertionError as e:

  169              assert op[2] == 'ok'
  170:             assert re.search(r"\d+ RPM", op[4]), op
  171      except AssertionError as e:

  182              assert op[2] == 'ok'
  183:             if re.search(r"PSU\d+ Status", op[0]):
  184                  assert op[4].lower() == 'presence detected'
  185:             elif re.search(r"PSU\d+ Power", op[0]):
  186:                 assert re.search(r"\d+ Watts", op[4])
  187      except AssertionError as e:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_ipmb.py:
   44      try:
   45:         assert re.search(r'\d+', info_dict['Record Count']), \
   46              info_dict['Record Count']
   47:         assert re.search(r'\d+ bytes', info_dict['Free Space']), \
   48              info_dict['Free Space']

   63          for op in status_list:
   64:             if re.search("fan", op[0].lower()) and op[1] != 'no reading':
   65:                 assert re.search(r'\d+ RPM', op[1]), op
   66      except AssertionError as e:

   79          for op in status_list:
   80:             if re.search("temp", op[0].lower()) and op[1] != 'no reading':
   81:                 assert re.search(r'\d+ degrees C', op[1]), op
   82      except AssertionError as e:

   95          for op in status_list:
   96:             if re.search("hdd", op[0].lower()) and op[1] != 'no reading':
   97:                 assert re.search(r"\d+ degrees C", op[1]), op
   98      except AssertionError as e:

  111          for op in status_list:
  112:             if re.search(("cpu_dimm*", op[0].lower()) and
  113                           op[1].lower() != 'no reading'):
  114:                 assert re.search(r"\d+ degrees C", op[1]), op
  115:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  116:                 assert re.search(r"^\d+\.?\d* Volts", op[1]), op
  117      except AssertionError as e:

  130          for op in status_list:
  131:             if re.search("power", op[0].lower()) and op[1] != 'no reading':
  132:                 assert re.search(r"\d+ Watts", op[1]), op
  133      except AssertionError as e:

  165                      assert op[2] == 'ok', op
  166:                     if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  167:                         assert re.search(r"\d+ degrees C", op[4]), op
  168          except AssertionError as e:

  186                  assert op[2] == 'ok'
  187:                 assert re.search(r"\d+\.\d+ Volts", op[4]), op
  188          except AssertionError as e:

  205                  assert op[2] == 'ok'
  206:                 assert re.search(r"\d+ RPM", op[4]), op
  207          except AssertionError as e:

  224                  assert op[2] == 'ok'
  225:                 if re.search(r"PSU\d+ Status", op[0]):
  226                      assert op[4].lower() == 'presence detected'
  227:                 elif re.search(r"PSU\d+ Power", op[0]):
  228:                     assert re.search(r"\d+ Watts", op[4])
  229          except AssertionError as e:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sdr_local.py:
   39      try:
   40:         assert re.search(r'\d+', info_dict['Record Count']), \
   41              info_dict['Record Count']
   42:         assert re.search(r'\d+ bytes', info_dict['Free Space']), \
   43              info_dict['Free Space']

   55          for op in status_list:
   56:             if re.search("fan", op[0].lower()) and op[1] != 'no reading':
   57:                 assert re.search(r'\d+ RPM', op[1]), op
   58      except AssertionError as e:

   68          for op in status_list:
   69:             if re.search(("temp", op[0].lower()) and
   70                           op[1].lower() != 'no reading'):
   71:                 assert re.search(r'\d+ degrees C', op[1]), op
   72      except AssertionError as e:

   82          for op in status_list:
   83:             if re.search("hdd", op[0].lower()) and op[1] != 'no reading':
   84:                 assert re.search(r'\d+ degrees C', op[1]), op
   85      except AssertionError as e:

   95          for op in status_list:
   96:             if re.search(("cpu_dimm*", op[0].lower()) and
   97                           op[1].lower() != 'no reading'):
   98:                 assert re.search(r'\d+ degrees C', op[1]), op
   99:             elif re.search("cpu vcore|cpu memory", op[0].lower()):
  100:                 assert re.search(r'^\d+\.?\d* Volts', op[1]), op
  101      except AssertionError as e:

  111          for op in status_list:
  112:             if re.search("power", op[0].lower()) and op[1] != 'no reading':
  113:                 assert re.search(r'\d+ Watts', op[1]), op
  114      except AssertionError as e:

  139                  assert op[2] == 'ok', op
  140:                 if not re.search(r'CPU\d*_PECI_Value', str(op[0])):
  141:                     assert re.search(r'\d+ degrees C', op[4]), op
  142      except AssertionError as e:

  154                  assert op[2] == 'ok', op
  155:                 assert re.search(r'\d+\.\d+ Volts', op[4]), op
  156      except AssertionError as e:

  167              assert op[2] == 'ok', op
  168:             assert re.search(r'\d+ RPM', op[4]), op
  169      except AssertionError as e:

  180              assert op[2] == 'ok', op
  181:             if re.search(r'PSU\d+ Status', op[0]):
  182                  assert op[4].lower() == 'presence detected'
  183:             elif re.search(r'PSU\d+ Power', op[0]):
  184:                 assert re.search(r'\d+ Watts', op[4])
  185      except AssertionError as e:

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_external.py:
   81          assert sel_info_dict['Entries'] == '3'
   82:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   83              sel_info_dict['Version']
   84:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   85              sel_info_dict['Entries']
   86:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
   87              sel_info_dict['Free Space']
   88:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
   89              sel_info_dict['Percent Used']

  102          assert sel_info_dict['Entries'] == '3'
  103:         assert re.search(r"^1.5", sel_info_dict['Version']), \
  104              sel_info_dict['Version']
  105:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  106              sel_info_dict['Entries']
  107:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  108              sel_info_dict['Free Space']
  109:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  110              sel_info_dict['Percent Used']

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_ipmb.py:
   94          assert sel_info_dict['Entries'] == '3'
   95:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   96              sel_info_dict['Version']
   97:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   98              sel_info_dict['Entries']
   99:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  100              sel_info_dict['Free Space']
  101:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  102              sel_info_dict['Percent Used']

  117          assert sel_info_dict['Entries'] == '3'
  118:         assert re.search(r"^1.5", sel_info_dict['Version']), \
  119              sel_info_dict['Version']
  120:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  121              sel_info_dict['Entries']
  122:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  123              sel_info_dict['Free Space']
  124:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  125              sel_info_dict['Percent Used']

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_sel_local.py:
   90              assert sel_info_dict['Entries'] == '3'
   91:         assert re.search(r"^1.5", sel_info_dict['Version']), \
   92              sel_info_dict['Version']
   93:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
   94              sel_info_dict['Entries']
   95:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
   96              sel_info_dict['Free Space']
   97:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
   98              sel_info_dict['Percent Used']

  114              assert sel_info_dict['Entries'] == '4'
  115:         assert re.search("^1.5", sel_info_dict['Version']), \
  116              sel_info_dict['Version']
  117:         assert re.search(r"^\d+$", sel_info_dict['Entries']), \
  118              sel_info_dict['Entries']
  119:         assert re.search(r"^\d+ bytes$", sel_info_dict['Free Space']), \
  120              sel_info_dict['Free Space']
  121:         assert re.search(r"^\d+\s*%$", sel_info_dict['Percent Used']), \
  122              sel_info_dict['Percent Used']

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc\test_bmc_set_ip_source.py:
  100          assert ip_dict['ip_source'] == 'dhcp'
  101:         assert re.search(r"(\d+\.){3}\d+", ip_dict['ip_source']), \
  102              ip_dict['ip_source']
  103:         assert re.search(r"(\d+\.){3}\d+", ip_dict['subnet_mask']), \
  104              ip_dict['subnet_mask']
  105:         assert re.search(r"(\d+\.){3}\d+", ip_dict['gateway']), \
  106              ip_dict['gateway']

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc_stress\test_bmc_stress_rios_power_cycle.py:
  141      proc_ipmi_stats = shell.exec_command(cmd)
  142:     if (re.search(r'sent_ipmb_command_errs:\s+\d{1,3}\s+',
  143                    proc_ipmi_stats) and
  144:             re.search(r'sent_lan_command_errs:\s+\d{1,3}\s+',
  145                        proc_ipmi_stats) and
  146:             re.search(r'retransmitted_lan_commands:\s+\d{1,3}\s+',
  147                        proc_ipmi_stats) and
  148:             re.search(r'timed_out_lan_commands:\s+\d{1,3}\s+',
  149                        proc_ipmi_stats) and
  150:             re.search(r'sent_lan_responses:\s+\d{1,3}\s+',
  151                        proc_ipmi_stats) and
  152:             re.search(r'handled_lan_responses:\s+\d{1,3}\s+',
  153                        proc_ipmi_stats) and
  154:             re.search(r'invalid_lan_responses:\s+\d{1,3}\s+',
  155                        proc_ipmi_stats) and
  156:             re.search(r'unhandled_lan_responses:\s+\d{1,3}\s+',
  157                        proc_ipmi_stats)):

  242          box_type = ipmitool_rios_lan.run("fru list")
  243:         if(re.search("2U", box_type)):
  244              logger.info("##### BLUEFIN-2U #########")

  262                                   "169.254.0.101"]
  263:         elif(re.search("1U", box_type)):
  264              logger.info("##### BLUEFIN-1U #########")

  328          mc_info = ipmitool_rios_lan.run("mc info")
  329:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  330          mc_info_status["rios_aux"][0] = mc_info_status["rios_aux"][0] + 1

  348          mc_info = ipmitool_rios.run("mc info")
  349:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  350          mc_info_status["rios_local"][0] = mc_info_status["rios_local"][0] + 1

  369          mc_info = ipmitool_vsp_lan.run("mc info")
  370:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  371          mc_info_status["vsp_aux"][0] = mc_info_status["vsp_aux"][0] + 1

  389          mc_info = ipmitool_vsp.run("mc info")
  390:         assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  391          mc_info_status["vsp_ipmb"][0] = mc_info_status["vsp_ipmb"][0] + 1

  412          for op in status_list:
  413:             if (re.search("no reading", op[1]) or
  414:                     re.search("Not Readable", op[1])):
  415                  assert op[2] == "ns", op

  438          for op in status_list:
  439:             if (re.search("no reading", op[1]) or
  440:                     re.search("Not Readable", op[1])):
  441                  assert op[2] == "ns", op

  466          for op in status_list:
  467:             if (re.search("no reading", op[1]) or
  468:                     re.search("Not Readable", op[1])):
  469                  assert op[2] == "ns", op

  494          for op in status_list:
  495:             if (re.search("no reading", op[1]) or
  496:                     re.search("Not Readable", op[1])):
  497                  assert op[2] == "ns", op

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\bmc_stress\test_bmc_stress.py:
  137      proc_ipmi_stats = shell.exec_command(cmd)
  138:     if (re.search(r'sent_ipmb_command_errs:\s+\d{1,3}\s+',
  139                    proc_ipmi_stats) and
  140:             re.search(r'sent_lan_command_errs:\s+\d{1,3}\s+',
  141                        proc_ipmi_stats) and
  142:             re.search(r'retransmitted_lan_commands:\s+\d{1,3}\s+',
  143                        proc_ipmi_stats) and
  144:             re.search(r'timed_out_lan_commands:\s+\d{1,3}\s+',
  145                        proc_ipmi_stats) and
  146:             re.search(r'sent_lan_responses:\s+\d{1,3}\s+',
  147                        proc_ipmi_stats) and
  148:             re.search(r'handled_lan_responses:\s+\d{1,3}\s+',
  149                        proc_ipmi_stats) and
  150:             re.search(r'invalid_lan_responses:\s+\d{1,3}\s+',
  151                        proc_ipmi_stats) and
  152:             re.search(r'unhandled_lan_responses:\s+\d{1,3}\s+',
  153                        proc_ipmi_stats)):

  237          box_type = ipmitool_rios_lan.run("fru list")
  238:         if(re.search("2U", box_type)):
  239              logger.info("##### BLUEFIN-2U #########")

  257                                   "169.254.0.101"]
  258:         elif(re.search("1U", box_type)):
  259              logger.info("##### BLUEFIN-1U #########")

  354              mc_info = ipmitool_rios_lan.run("mc info")
  355:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  356              mc_info_status["rios_aux"][0] = mc_info_status["rios_aux"][0] + 1

  374              mc_info = ipmitool_rios.run("mc info")
  375:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  376              mc_info_status["rios_local"][0] = \

  397              mc_info = ipmitool_vsp_lan.run("mc info")
  398:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  399              mc_info_status["vsp_aux"][0] = mc_info_status["vsp_aux"][0] + 1

  417              mc_info = ipmitool_vsp.run("mc info")
  418:             assert re.search(r'Device Available\s+:\s+yes', mc_info), mc_info
  419              mc_info_status["vsp_ipmb"][0] = mc_info_status["vsp_ipmb"][0] + 1

  440              for op in status_list:
  441:                 if (re.search("no reading", op[1]) or
  442:                         re.search("Not Readable", op[1])):
  443                      assert op[2] == "ns", op

  466              for op in status_list:
  467:                 if (re.search("no reading", op[1]) or
  468:                         re.search("Not Readable", op[1])):
  469                      assert op[2] == "ns", op

  496              for op in status_list:
  497:                 if (re.search("no reading", op[1]) or
  498:                         re.search("Not Readable", op[1])):
  499                      assert op[2] == "ns", op

  524              for op in status_list:
  525:                 if (re.search("no reading", op[1]) or
  526:                         re.search("Not Readable", op[1])):
  527                      assert op[2] == "ns", op

sc\portfolio-system-tests\portfolio_system_tests\legacy_core_infrastructure_qa_tests\tests\hwtool\tests_hwtool.py:
  1173          logger.info("Actual Output: [" + actual_output + "]")
  1174:         elements = re.search(r"(\d+)\s+(\d+)\s+(\d+)\s+(.*)", actual_output)
  1175          # Validating CPU core count

  1265              # Verifying Slots
  1266:             elements = re.search(r"Slot\s+(\d+):\s\.{10}\s([^,]*),\s(.*)",
  1267                                   line)

  1275                  # Verifying Hardware revision
  1276:                 elements = re.search(r"Hardware revision:\s+([\d\D]+)", line)
  1277                  if elements is not None:

  1279                  else:
  1280:                     elements = re.search(r"Mainboard:\s[^,]*,\s(.*)", line)
  1281                      if elements is not None:

  1338              system_section = section
  1339:     elements = re.search(r".*Product\s*:\s*(.*)", system_section)
  1340      actual_motherboard_number = elements.group(1)

  1445          for line in lines:
  1446:             if re.search(r"disk.*", line) is not None:
  1447                  elements = line.split()

  1458          for line in lines:
  1459:             if re.search(r"\w", line):
  1460                  elements = line.split()

sc\portfolio-system-tests\portfolio_system_tests\legacy_exchange_tests\tests\test_allocation_health.py:
   64  
   65:         match = re.search(r'received, (?P<loss>\d+.*)\s*% packet loss,',
   66                            output)

  145                r'\s*% loss\)')
  146:     match = re.search(target, output)
  147      if not match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_exchange_tests\tests\test_smoke_mess.py:
  38      ITEMS_RE = r'ItemsInFolder\s+-------------\s+(?P<items>\d+)'
  39:     match = re.search(ITEMS_RE, output)
  40      return int(match.group('items'))

sc\portfolio-system-tests\portfolio_system_tests\legacy_gluon\libs\__init__.py:
  360      # Example: "hostname":"XNCC58DC4E4D4408",
  361:     sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  362      if not sobj:

sc\portfolio-system-tests\portfolio_system_tests\legacy_gluon\tests\test_firewall_rules_after_failover_vgw.py:
  127      regex = re.escape(str1) + r'\n(.*)$'
  128:     sobj1 = re.search(regex, output, re.MULTILINE | re.DOTALL)
  129      if sobj1:

  182      # Format of uptime: 35d  0h  54m
  183:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  184      if not sobj:

sc\portfolio-system-tests\portfolio_system_tests\legacy_gluon\tests\test_firewall_rules_after_reboot_vgw.py:
  126      regex = re.escape(str1) + r'\n(.*)$'
  127:     sobj1 = re.search(regex, output, re.MULTILINE | re.DOTALL)
  128      if sobj1:

  191          # Example: "hostname":"XNCC58DC4E4D4408",
  192:         sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  193          if not sobj:

  223      # Format of uptime: 35d  0h  54m
  224:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  225      if not sobj:

sc\portfolio-system-tests\portfolio_system_tests\legacy_gluon\tests\test_internet_and_site_to_site.py:
  123      # Example: "hostname":"XNCC58DC4E4D4408",
  124:     sobj = re.search(r'\"hostname\":\"(.*)\",$', res_lines[0])
  125      if not sobj:

  363      # Resolving facebook.com (facebook.com)... 31.13.90.36, 2a03..
  364:     sobj = re.search(r'\(facebook\.com\)\.\.\.\s+(.*),', lines[2])
  365      if sobj:

  407      # Resolving youtube.com (youtube.com)... 216.58.194.206, 2607
  408:     sobj = re.search(r'\(youtube\.com\)\.\.\.\s+(.*),', lines[2])
  409      if sobj:

  450      # Format of uptime: 35d  0h  54m
  451:     sobj = re.search(r'(\d*)d\s+(\d*)h\s+(\d*)m', uptime, re.M | re.I)
  452      if not sobj:

sc\portfolio-system-tests\portfolio_system_tests\legacy_gluon\tests\test_overnight_failover_pingpong.py:
  78  
  79:     match = re.search(r'(?<=\()\S+?(?=\) port \d+)', output)
  80      if match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\conftest.py:
  397  
  398:     if re.search("different_unique_ib_ob", test_case):
  399          logger.info("[INFO]: cleanup after different_unique_ib_ob")

  496          for line in profile_data.raw.split("\n"):
  497:             result = re.search(r"(\*\w+\*)\s+\d+\s+(\d+)\s+(\d+)",
  498                                 profile_data.raw)

  518      """
  519:     if re.search("same_default_ib_ob", test_case):
  520          init_qos_device_configurator.config.manage_sites(7)
  521          init_qos_device_configurator.config.manage_sites(8)
  522:     elif re.search("unique_ib_default_ob", test_case):
  523          init_qos_device_configurator.config.manage_sites(7)
  524:     elif re.search("default_ib_unique_ob", test_case):
  525          init_qos_device_configurator.config.manage_sites(8)
  526:     elif re.search("different_unique_ib_ob", test_case):
  527          init_qos_device_configurator.config.manage_profiles(9)

  549  
  550:     if re.search("same_default|default_ob", test_case):
  551:         if re.search("^.*DSCP_P$", test_case):
  552              init_qos_device_configurator.config.manage_classes(21)
  553  
  554:         if re.search("^.*DSCP_L$", test_case):
  555              init_qos_device_configurator.config.manage_classes(38)
  556  
  557:         if re.search("^.*DSCP_R$", test_case):
  558              init_qos_device_configurator.config.manage_rules(3)
  559  
  560:         if re.search("^.*DSCP_PL$", test_case):
  561              init_qos_device_configurator.config.manage_classes(21)

  563  
  564:         if re.search("^.*DSCP_PR$", test_case):
  565              init_qos_device_configurator.config.manage_classes(21)

  567  
  568:         if re.search("^.*DSCP_LR$", test_case):
  569              init_qos_device_configurator.config.manage_classes(38)

  571  
  572:         if re.search("^.*DSCP_PLR$", test_case):
  573              init_qos_device_configurator.config.manage_classes(21)

  577      else:
  578:         if re.search("^.*DSCP_P$", test_case):
  579              init_qos_device_configurator.config.manage_classes(26)
  580  
  581:         if re.search("^.*DSCP_L$", test_case):
  582              init_qos_device_configurator.config.manage_classes(34)
  583  
  584:         if re.search("^.*DSCP_R$", test_case):
  585              init_qos_device_configurator.config.manage_rules(5)
  586  
  587:         if re.search("^.*DSCP_PL$", test_case):
  588              init_qos_device_configurator.config.manage_classes(26)

  590  
  591:         if re.search("^.*DSCP_PR$", test_case):
  592              init_qos_device_configurator.config.manage_classes(26)

  594  
  595:         if re.search("^.*DSCP_LR$", test_case):
  596              init_qos_device_configurator.config.manage_classes(34)

  598  
  599:         if re.search("^.*DSCP_PLR$", test_case):
  600              init_qos_device_configurator.config.manage_classes(26)

  622  
  623:     if re.search("same_default|default_ob", test_case):
  624:         if re.search("^.*DSCP_P$", test_case):
  625              init_qos_device_configurator.config.manage_classes(25)
  626  
  627:         if re.search("^.*DSCP_L$", test_case):
  628              init_qos_device_configurator.config.manage_classes(39)
  629  
  630:         if re.search("^.*DSCP_R$", test_case):
  631              init_qos_device_configurator.config.manage_rules(4)
  632  
  633:         if re.search("^.*DSCP_PL$", test_case):
  634              init_qos_device_configurator.config.manage_classes(25)

  636  
  637:         if re.search("^.*DSCP_PR$", test_case):
  638              init_qos_device_configurator.config.manage_classes(25)

  640  
  641:         if re.search("^.*DSCP_LR$", test_case):
  642              init_qos_device_configurator.config.manage_classes(39)

  644  
  645:         if re.search("^.*DSCP_PLR$", test_case):
  646              init_qos_device_configurator.config.manage_classes(25)

  650      else:
  651:         if re.search("^.*DSCP_P$", test_case):
  652              init_qos_device_configurator.config.manage_classes(30)
  653  
  654:         if re.search("^.*DSCP_L$", test_case):
  655              init_qos_device_configurator.config.manage_classes(35)
  656  
  657:         if re.search("^.*DSCP_R$", test_case):
  658              init_qos_device_configurator.config.manage_rules(6)
  659  
  660:         if re.search("^.*DSCP_PL$", test_case):
  661              init_qos_device_configurator.config.manage_classes(30)

  663  
  664:         if re.search("^.*DSCP_PR$", test_case):
  665              init_qos_device_configurator.config.manage_classes(30)

  667  
  668:         if re.search("^.*DSCP_LR$", test_case):
  669              init_qos_device_configurator.config.manage_classes(35)

  671  
  672:         if re.search("^.*DSCP_PLR$", test_case):
  673              init_qos_device_configurator.config.manage_classes(30)

sc\portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_inbound_qos_dscp_full_combinations.py:
   89      try:
   90:         if re.search("same_default|default_ob", test_case):
   91              init_qos_device_configurator.config.manage_classes(37)
   92  
   93:             if re.search("unique_ib_default_ob", test_case):
   94                  qos = init_qos_device_configurator.config.\

  119  
  120:             if re.search("^.*DSCP_P$", test_case):
  121                  expected_ob_qos_dscp = 0
  122  
  123:             if re.search("^.*DSCP_L$", test_case):
  124                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  125  
  126:             if re.search("^.*DSCP_R$", test_case):
  127                  expected_ob_qos_dscp = default_outbound_dscp_rule
  128  
  129:             if re.search("^.*DSCP_PL$", test_case):
  130                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  131  
  132:             if re.search("^.*DSCP_PR$", test_case):
  133                  expected_ob_qos_dscp = default_outbound_dscp_rule
  134  
  135:             if re.search("^.*DSCP_LR$", test_case):
  136                  expected_ob_qos_dscp = default_outbound_dscp_rule
  137  
  138:             if re.search("^.*DSCP_PLR$", test_case):
  139                  expected_ob_qos_dscp = default_outbound_dscp_rule

  143  
  144:             if re.search("default_ib_unique_ob", test_case):
  145                  qos = init_qos_device_configurator.config.\

  148  
  149:             elif re.search("different_unique_ib_ob", test_case):
  150                  qos = init_qos_device_configurator.config.\

  175  
  176:             if re.search("^.*DSCP_P$", test_case):
  177                  expected_ob_qos_dscp = 0
  178  
  179:             if re.search("^.*DSCP_L$", test_case):
  180                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  181  
  182:             if re.search("^.*DSCP_R$", test_case):
  183                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  184  
  185:             if re.search("^.*DSCP_PL$", test_case):
  186                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  187  
  188:             if re.search("^.*DSCP_PR$", test_case):
  189                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  190  
  191:             if re.search("^.*DSCP_LR$", test_case):
  192                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  193  
  194:             if re.search("^.*DSCP_PLR$", test_case):
  195                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  281  
  282:         if re.search("same_default|default_ob", test_case):
  283              init_qos_device_configurator.config.manage_rules(7)

sc\portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_outbound_qos_dscp_full_combinations.py:
   89      try:
   90:         if re.search("same_default|default_ob", test_case):
   91              init_qos_device_configurator.config.manage_classes(37)

  113  
  114:             if re.search("^.*DSCP_P$", test_case):
  115                  expected_ob_qos_dscp = 0
  116  
  117:             if re.search("^.*DSCP_L$", test_case):
  118                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  119  
  120:             if re.search("^.*DSCP_R$", test_case):
  121                  expected_ob_qos_dscp = default_outbound_dscp_rule
  122  
  123:             if re.search("^.*DSCP_PL$", test_case):
  124                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  125  
  126:             if re.search("^.*DSCP_PR$", test_case):
  127                  expected_ob_qos_dscp = default_outbound_dscp_rule
  128  
  129:             if re.search("^.*DSCP_LR$", test_case):
  130                  expected_ob_qos_dscp = default_outbound_dscp_rule
  131  
  132:             if re.search("^.*DSCP_PLR$", test_case):
  133                  expected_ob_qos_dscp = default_outbound_dscp_rule

  158  
  159:             if re.search("^.*DSCP_P$", test_case):
  160                  expected_ob_qos_dscp = 0
  161  
  162:             if re.search("^.*DSCP_L$", test_case):
  163                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  164  
  165:             if re.search("^.*DSCP_R$", test_case):
  166                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  167  
  168:             if re.search("^.*DSCP_PL$", test_case):
  169                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  170  
  171:             if re.search("^.*DSCP_PR$", test_case):
  172                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  173  
  174:             if re.search("^.*DSCP_LR$", test_case):
  175                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  176  
  177:             if re.search("^.*DSCP_PLR$", test_case):
  178                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  250  
  251:         if re.search("same_default|default_ob", test_case):
  252              init_qos_device_configurator.config.manage_rules(7)

sc\portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_qos_device_all_classification.py:
  213      """
  214:     if re.search('-sh', test_case):
  215          check_qos_on_IC = 0

  217  
  218:     elif re.search('-ic', test_case):
  219          check_qos_on_IC = 1

  224  
  225:     if re.search('-IN', test_case):
  226          QoS_Flags = 1

  233  
  234:     elif re.search('-OUT', test_case):
  235          QoS_Flags = 0

  242  
  243:     if re.search('-UniqueSite', test_case):
  244          is_UniqueSite = 1

  247  
  248:     elif re.search('-DefaultSite', test_case):
  249          is_UniqueSite = 0

  294      try:
  295:         if re.search('same_unique_ib_ob', test_case):
  296              # The same unique profile is used for Inbound and outbound.

  309  
  310:         elif re.search('same_default_ib_ob', test_case):
  311              # Default profile is used for both Inbound and outbound traffic.

  325  
  326:         elif re.search('default_ib_unique_ob', test_case):
  327              # Default profile is used for inbound and

  342  
  343:         elif re.search('unique_ib_default_ob', test_case):
  344              # Default profile is used for outbound and

  358  
  359:         elif re.search('different_unique_ib_ob', test_case):
  360              # Different unique profiles for outbound and inbound traffic.

  431              # Checking for optimized or passthrough traffic
  432:             if re.search('-noOpt', test_case):
  433                  verify_opt(sh_resource=test_objects.client_sh,

  439  
  440:             elif re.search('-Opt', test_case):
  441                  verify_opt(sh_resource=test_objects.client_sh,

sc\portfolio-system-tests\portfolio_system_tests\legacy_netint_qosez_tests\tests\QoS-SH-IC\test_qos_dscp_full_combinations.py:
   88      try:
   89:         if re.search("same_default|default_ob", test_case):
   90              init_qos_device_configurator.config.manage_classes(37)
   91  
   92:             if re.search("unique_ib_default_ob", test_case):
   93                  qos = init_qos_device_configurator.config.\

  123  
  124:             if re.search("^.*DSCP_P$", test_case):
  125                  expected_ob_qos_dscp = 0
  126  
  127:             if re.search("^.*DSCP_L$", test_case):
  128                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  129  
  130:             if re.search("^.*DSCP_R$", test_case):
  131                  expected_ob_qos_dscp = default_outbound_dscp_rule
  132  
  133:             if re.search("^.*DSCP_PL$", test_case):
  134                  expected_ob_qos_dscp = default_outbound_dscp_leaf
  135  
  136:             if re.search("^.*DSCP_PR$", test_case):
  137                  expected_ob_qos_dscp = default_outbound_dscp_rule
  138  
  139:             if re.search("^.*DSCP_LR$", test_case):
  140                  expected_ob_qos_dscp = default_outbound_dscp_rule
  141  
  142:             if re.search("^.*DSCP_PLR$", test_case):
  143                  expected_ob_qos_dscp = default_outbound_dscp_rule

  147  
  148:             if re.search("default_ib_unique_ob", test_case):
  149                  qos = init_qos_device_configurator.config.\

  152  
  153:             elif re.search("different_unique_ib_ob", test_case):
  154                  qos = init_qos_device_configurator.config.\

  184  
  185:             if re.search("^.*DSCP_P$", test_case):
  186                  expected_ob_qos_dscp = 0
  187  
  188:             if re.search("^.*DSCP_L$", test_case):
  189                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  190  
  191:             if re.search("^.*DSCP_R$", test_case):
  192                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  193  
  194:             if re.search("^.*DSCP_PL$", test_case):
  195                  expected_ob_qos_dscp = unique_outbound_dscp_leaf
  196  
  197:             if re.search("^.*DSCP_PR$", test_case):
  198                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  199  
  200:             if re.search("^.*DSCP_LR$", test_case):
  201                  expected_ob_qos_dscp = unique_outbound_dscp_rule
  202  
  203:             if re.search("^.*DSCP_PLR$", test_case):
  204                  expected_ob_qos_dscp = unique_outbound_dscp_rule

  300  
  301:         if re.search("same_default|default_ob", test_case):
  302              init_qos_device_configurator.config.manage_rules(7)

sc\portfolio-system-tests\portfolio_system_tests\legacy_netint_tests\tests\legacy\Securetransport\sectp_ms2_nat_integ.py:
  31      """
  32:     m = re.search(r"Runner - Tests planned:\s+(\d+)", log)
  33      planned_tc = m.group(1)
  34:     m = re.search(r"Runner - Tests passed:\s+(\d+)", log)
  35      passed_tc = m.group(1)

  47      """
  48:     match = re.search(r"1 passed in (\d+)", log)
  49      if match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns\service_chain_manager\service_chain_manager\test\orclibs\traffic_parser.py:
  51      hwaddr = None
  52:     eth_match = re.search(r'(ether|HWaddr)\s(?:addr:)*(\S+)', output)
  53      if eth_match:

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\ibt\tests\Guest_Zone_Support\test_local_internet_breakout.py:
  79      for line in output_lines:
  80:         maskmatch = re.search(r'\s' + interface, line, re.IGNORECASE)
  81          if maskmatch:

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\cf3\DHCP_DNS\test_DHCP_relay_via_overlay_to_DC.py:
   90      for zone in zones:
   91:         if re.search(site_1['name'], zone.site):
   92              branch_net = zone.networks[0]

  130          for zone in zones:
  131:             if re.search(site_1['name'], zone.site):
  132                  configurator.scm_actor.config.change_network(

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\cf3\QoS\test_aggregate_traffic_with_mixed_traffic_class.py:
  115      for line in output.split("\n"):
  116:         bandwidth = re.search(r'\d+\.\d+mbps', line)
  117          if not bandwidth:

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_add_new_tep_ips_in_dc_uplinks.py:
  205          for dcuplink in dc_old_wan_teps:
  206:             if re.search('Internet', dcuplink):
  207                  public_ipv4 = str(resources.dc_public.cidr.ip)

  266          for dcuplink in dc_old_wan_teps:
  267:             if re.search('Internet', dcuplink):
  268                  public_ipv4 = str(resources.dc_public.cidr.ip)

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_data_ports_poweroff_update.py:
  215      for port in data_ports:
  216:         if re.search('PORT3', port.id, flags=re.IGNORECASE) or \
  217:                 re.search('PORT4', port.id, flags=re.IGNORECASE):
  218              resources.scm_actor.change_port(

  226          for port in data_ports:
  227:             if re.search('PORT3', port.id, flags=re.IGNORECASE) or \
  228:                     re.search('PORT4', port.id, flags=re.IGNORECASE):
  229                  resources.scm_actor.change_port(

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover_CF3.py:
  235      for zone in zone_list:
  236:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  237              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  251      for uplink in uplink_list:
  252:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  253:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  254                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  379          for zone in zones_list:
  380:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  381                  obj_added_zone = zone

  399                  for custom_app in custom_apps:
  400:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  401                                   flags=re.IGNORECASE):

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_flow_rules_recover.py:
  237      for zone in zone_list:
  238:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  239              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  253      for uplink in uplink_list:
  254:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  255:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  256                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  388          for zone in zones_list:
  389:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  390                  obj_added_zone = zone

  408                  for custom_app in custom_apps:
  409:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  410                                   flags=re.IGNORECASE):

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_leaf_site_checking_in_site_pool.py:
  440      for site in sites_lists:
  441:         if re.search('HQ', site.name):
  442              hq_site_name = site.name

  467          for dc_uplink in dc_uplinks:
  468:             if re.search(INTERNET,
  469                           dc_uplink.wan,

  709          for dc_uplink in dc_uplinks:
  710:             if re.search(INTERNET,
  711                           dc_uplink.wan,

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch_CF3.py:
  135      for zone in zone_list:
  136:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  137              zone_network = scm_actor.get_network(zone.networks[0])

  146      for uplink in uplink_list:
  147:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  148:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  149                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  176          for zone in zones_list:
  177:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  178                  obj_added_zone = zone

  192                  for custom_app in custom_apps:
  193:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  194                                   flags=re.IGNORECASE):

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_lpm_delete_existing_branch.py:
  135      for zone in zone_list:
  136:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  137              zone_network = scm_actor.get_network(zone.networks[0])

  146      for uplink in uplink_list:
  147:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  148:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  149                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  176          for zone in zones_list:
  177:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  178                  obj_added_zone = zone

  192                  for custom_app in custom_apps:
  193:                     if re.search('CAT_CUSTOM_UDP', custom_app.name,
  194                                   flags=re.IGNORECASE):

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\cluster\test_size_change_for_site_moves.py:
  445      for site in sites_lists:
  446:         if re.search('HQ', site.name):
  447              hq_site_name = site.name

  473          for dc_uplink in dc_uplinks:
  474:             if re.search(INTERNET,
  475                           dc_uplink.wan,

  758          for dc_uplink in dc_uplinks:
  759:             if re.search(INTERNET,
  760                           dc_uplink.wan,

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch_CF3.py:
  264      for zone in zone_list:
  265:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  266              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  280      for uplink in uplink_list:
  281:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  282:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  283                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  402          for zone in zones_list:
  403:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  404                  obj_added_zone = zone

  422                  for custom_app in custom_apps:
  423:                     if re.search('CAT_CUSTOM_UDP',
  424                                   custom_app.name,

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_branch.py:
  264      for zone in zone_list:
  265:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  266              zone_network = test_objects.scm_actor.get_network(zone.networks[0])

  280      for uplink in uplink_list:
  281:         if re.search(SITE, uplink.site, flags=re.IGNORECASE):
  282:             if re.search('Internet', uplink.wan, flags=re.IGNORECASE):
  283                  dct_variables['internet_static_ipv4'] = uplink.static_ip_v4

  403          for zone in zones_list:
  404:             if re.search(SITE, zone.site, flags=re.IGNORECASE):
  405                  obj_added_zone = zone

  423                  for custom_app in custom_apps:
  424:                     if re.search(
  425                          'CAT_CUSTOM_UDP',

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_dc_uplink.py:
  259      for dc_uplink in dc_uplinks:
  260:         if re.search(WAN,
  261                       dc_uplink.wan,

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_wan_CF3.py:
  304      for zone in zone_list:
  305:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  306              zone_obj = copy.copy(zone)

  317      for uplink in uplink_list:
  318:         if re.search(WAN, uplink.wan, flags=re.IGNORECASE):
  319              branch_name = test_objects.scm_actor.get_site(

  457          for wan_data in wans:
  458:             if re.search(WAN, wan_data.name, flags=re.IGNORECASE):
  459                  wan_id = wan_data.id

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_wan.py:
  308      for uplink in uplink_list:
  309:         if re.search(WAN, uplink.wan, flags=re.IGNORECASE):
  310              branch_name = test_objects.scm_actor.get_site(

  440          for wan_data in wans:
  441:             if re.search(WAN, wan_data.name, flags=re.IGNORECASE):
  442                  wan_id = wan_data.id

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone_CF3.py:
  193      output = shell.exec_command("cat /var/last_received_cdl.yaml")
  194:     match = re.search('subnet: ' + ipv4, output, flags=re.IGNORECASE)
  195      if match:

  209          output = shell.exec_command("ip rule list")
  210:         match = re.search(ipv4, output)
  211          if match:

  244      for zone in zone_list:
  245:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  246              # Getting old zone ip

  378          for custom_app in custom_apps:
  379:             if re.search('CAT_CUSTOM_UDP', custom_app.name,
  380                           flags=re.IGNORECASE):

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_delete_add_zone.py:
  195      output = shell.exec_command("cat /var/last_received_cdl.yaml")
  196:     match = re.search('subnet: ' + ipv4, output, flags=re.IGNORECASE)
  197      if match:

  209          output = shell.exec_command("ip rule list")
  210:         match = re.search(ipv4, output)
  211          if match:

  245      for zone in zone_list:
  246:         if re.search(SITE, zone.site, flags=re.IGNORECASE):
  247              # Getting old zone ip

  379          for custom_app in custom_apps:
  380:             if re.search(
  381                  'CAT_CUSTOM_UDP',

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_uplink_wantype.py:
  357          # Example old_wan_name='Wan1',dc_uplink.wan='wan-Wan1-e63d40e499c3f0ab'
  358:         if re.search(old_wan_name,
  359                       dc_uplink.wan,

  395          # path_rule.path_preference[0]='wan-Wan1-e63d40e499c3f0ab'
  396:         if re.search(wan_name,
  397                       path_rule.path_preference[0],

  439          # Example uplink.name: "Wan1_Uplink"
  440:         if re.search(r'\bWan1_Uplink\b',
  441                       uplink.name,

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_branch_wan_uplink_ipaddress.py:
  284      for uplink in uplink_list:
  285:         if re.search(WAN, uplink.name, flags=re.IGNORECASE):
  286              return uplink.name

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\dynamic_changes\test_modify_zone_for_branch.py:
  181              for network_obj in network_list:
  182:                 if re.search(BRANCH, network_obj.site):
  183                      return network_obj

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_change_panther_db_address.py:
  147      for route in ic_ip_routes:
  148:         if re.search(network, route):
  149              flag = True

  161      for route in ic_ip_routes:
  162:         if re.search(network, route):
  163              flag = False

  279      for cluster_obj in clusters:
  280:         if re.search('Cluster1', cluster_obj.name, flags=re.IGNORECASE):
  281              old_proxy_ip = cluster_obj.proxy_ip

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_check_route_table.py:
  115      for route in ic_ip_routes:
  116:         if re.search(network, route):
  117              flag = True

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_int_service_restart.py:
  166      result = ic.show_info().raw
  167:     if re.search(status, str(result), flags=re.IGNORECASE):
  168          flag = True

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\icplusplus\test_modify_branch_subnet.py:
  207              for network_obj in network_list:
  208:                 if re.search(BRANCH, network_obj.site):
  209                      return network_obj

  225      for route in ic_ip_routes:
  226:         if re.search(network, route):
  227              flag = True

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\services\test_symmetrical_nat_port_dynamic_change.py:
  139      for uplink in uplink_list:
  140:         if re.search(r'\bWan1_Uplink\b',
  141                       uplink.name,

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_as_mismatch.py:
  126              shell.exec_command("grep remote_as /var/last_received_cdl.yaml")
  127:         hold = re.search('remote_as: 200', output)
  128          logger.info(output)

  167      logger.info(output)
  168:     holdtime = re.search('remote_as: 100', output)
  169      assert holdtime

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_nondefaults.py:
  124              "grep hold_time /var/last_received_cdl.yaml")
  125:         hold = re.search('hold_time: 10', output)
  126          logger.info(output)

  129              "grep keepalive_time /var/last_received_cdl.yaml")
  130:         keep = re.search('keepalive_time: 80', output)
  131          assert keep

  171      logger.info(output)
  172:     holdtime = re.search('hold_time: 60', output)
  173      assert holdtime

  175          "grep keepalive_time /var/last_received_cdl.yaml")
  176:     keep = re.search('keepalive_time: 180', output)
  177      assert keep

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_match.py:
  163              "grep password /var/last_received_cdl.yaml")
  164:         pword = re.search('password: thepassword', output)
  165          logger.info(output)

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_bgp_password_mismatch.py:
  139              "grep password /var/last_received_cdl.yaml")
  140:         pword = re.search('password: password', output)
  141          logger.info(output)

  189      logger.info(output)
  190:     pword = re.search('password: null', output)
  191      assert pword

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_ibgp_peering_on_wdr1_fails.py:
  327      for network in networks:
  328:         if not re.search('HQ', network.site):
  329              network_list.append(network.netv4)

  335          for subnet in subnet_splitted_list:
  336:             if not re.search(str(subnet), network, re.IGNORECASE):
  337                  higher_subnet_list.append(str(subnet))

sc\portfolio-system-tests\portfolio_system_tests\legacy_ns_tests\tests\panther\underlay\test_subnet_splitting.py:
  227      for cluster_obj in clusters:
  228:         if re.search('Cluster1', cluster_obj.name, flags=re.IGNORECASE):
  229              cluster_id = cluster_obj.id

  288      for network in networks:
  289:         if not re.search('HQ', network.site):
  290              network_list.append(network.netv4)

  296          for subnet in subnet_splitted_list:
  297:             if not re.search(str(subnet), network, re.IGNORECASE):
  298                  higher_subnet_list.append(str(subnet))

sc\portfolio-system-tests\portfolio_system_tests\legacy_scm_tests\legacy_tests\test_gw_via_rest\test_gw_via_rest.py:
  114      for uplink in uplinks:
  115:         if re.search('Internet', uplink.wan):
  116              continue

  204          uplink = scm_actor.config.get_uplink(uplink_id)
  205:         if re.search('Internet', uplink.wan):
  206              continue

sc\portfolio-system-tests\portfolio_system_tests\legacy_shm_tests\shm_helper.py:
  122              # command output
  123:             app_content = re.search(search_pattern, cmd_output, re.DOTALL) \
  124                  .group(1).strip()

  142                  application_map['dest_port'] = int(dest[1])
  143:                 application_map['app_id'] = int(re.search(".*snoopy_app="
  144                                                  "(\\d+)", app).group(1)

  274              # from command output
  275:             status = re.search(search_pattern, cmd_output) \
  276                  .group(1).strip()

  302              # from command output
  303:             policy = re.search(search_pattern, cmd_output) \
  304                  .group(1).strip()

  379              wait_until_complete(timeout=WAIT_900_SECS)
  380:         result = re.search("\\[PASS\\]:", cmd_output)
  381  

  424          search_pattern = r'{(.*?)}'
  425:         product_code = re.search(search_pattern, cmd_output, re.DOTALL) \
  426              .group(1).strip()

  441          try:
  442:             return re.search(search_pattern, cmd_output, re.DOTALL) \
  443                  .group(1).strip()

sc\portfolio-system-tests\portfolio_system_tests\legacy_shm_tests\zak\tests\conftest.py:
  180          try:
  181:             frmt_op = re.search(r"(.*?)Aliases", output,
  182                                  re.DOTALL).group(1).strip()

  187  
  188:         m = re.search("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*$", output)
  189          return (m.group(1))

sc\portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\portal\test_allsaas_sku.py:
   63          portal_sca.action.add_platform_to_sku(SKU, 'noexist')
   64:     assert re.search("404", str(err404.value)) is not None
   65      with pytest.raises(VerificationError):

   78          portal_sca.action.add_platform_to_sku('noexist', PLATFORM)
   79:     assert re.search("404", str(err404.value)) is not None
   80      with pytest.raises(UnexpectedOutput) as another404:
   81          portal_sca.verification.verify_platforms_sku('noexist', PLATFORM)
   82:     assert re.search("404", str(another404.value)) is not None
   83  

   94          portal_sca.verification.verify_platforms_sku('nonexist', [PLATFORM])
   95:     assert re.search("404", str(err404.value)) is not None
   96  

  107          portal_sca.action.delete_platform_from_sku('noexist', PLATFORM)
  108:     assert re.search("404", str(err404.value)) is not None
  109  

  122              portal_sca.action.delete_platform_from_sku(SKU, valid_platform)
  123:         assert re.search("404", str(err404.value)) is not None
  124  

sc\portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\portal\test_platforms.py:
  243                                         test_params.send_beta_fields)
  244:     assert re.search("400", str(err400.value)) is not None
  245  

  373              test_params.send_beta_fields)
  374:     assert re.search("400", str(err400.value)) is not None
  375  

sc\portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\O365D\inpath_rules\test_add_delete_hostlabel.py:
  228              # Extract class b address from resolved ips
  229:             subnet_extract = re.search(r"(^\d{1,3}\.\d{1,3})*",
  230                                         ip_address)

sc\portfolio-system-tests\portfolio_system_tests\legacy_shsaas_tests\tests\SH\sepia\conftest.py:
   88      # get the md5 checksum value
   89:     checksum = re.search(r'([0-9a-fA-F]+)\s+', output)
   90      if (not checksum):

   98      # extract the filename from url for checksum
   99:     match_obj = re.search("//.*/(.*)$", url)
  100      server_file = SERVER_FILE_LOCATION + match_obj.group(1)

  136                  # Extract class A address from resolved ips
  137:                 subnet_extract = re.search(r"(^\d{1,3}\.)",
  138                                             ip_address)

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\scripts\connect_to_scc.py:
   61          cmc_version_string = cmc_cli.exec_command('show info')
   62:         cmc_version = re.search(
   63              r'Version:.*',

   65                  'Version:', '').strip(r' \n\r\t')
   66:         steelhead_string = re.search(r'Steelheads.*\n\n\n',
   67                                       output,

   74          for steelhead in steelheads:
   75:             serial = re.search(r'Steelhead \w*', steelhead).\
   76                  group(0).replace('Steelhead ', '')
   77  
   78:             hostname = re.search(
   79                  r'\(.* /', steelhead).group(0).strip(r'(/ \n\t\r')
   80  
   81:             ip_addr = re.search(r'\d+\.\d+\.\d+\.\d+', steelhead).group(0)
   82  
   83:             ver_string = re.search(r'Version:.*', steelhead).\
   84                  group(0).replace('Version:', '').strip(r' \n\t\r')
   85:             version = re.search(r'\d+\.\d+\.\d+', ver_string).group(0)
   86  

   89                  ocs_connectivity = False
   90:                 connectivity = re.search(r'Connected:.*', steelhead).\
   91                      group(0).replace('Connected:', '').strip(r' \n\t\r')

   96                  ocs_connectivity = False
   97:                 connectivity = re.search(
   98                      r'SSH connection:.*', steelhead).group(0).\

  101                      gcl_connectivity = True
  102:                 connectivity = re.search(
  103                      r'HTTPS connection:.*', steelhead).group(0).\

  107  
  108:             build_no = re.search(r'#\d+', ver_string).group(0)
  109  
  110:             model = re.search(r'Model:.*', steelhead).\
  111                  group(0).replace('Model:', '').strip(r' \n\t\r')

  165      output = appl_cli.exec_command("show info")
  166:     serial = re.search(
  167          r'Serial:.*', output).group(0).replace('Serial:', '').strip(r' \n\t\r')

  169      output = appl_cli.exec_command("show cmc")
  170:     line = re.search(r'CMC hostname:.*', output).group(0)
  171      try:
  172:         current_cmc = re.search(r'\d+\.\d+\.\d+\.\d+', line).group(0)
  173      except Exception:

  257          output = appl_cli.exec_command("show cmc")
  258:         managed = re.search(r'Managed by CMC:.*', output).group(0).\
  259              replace('Managed by CMC:', '').strip(r' \n\t\r')
  260:         next_msg = re.search(r'Seconds until next message is sent:.*', output)
  261:         line = re.search(r'CMC hostname:.*', output).group(0)
  262          current_cmc_host = re.sub(

  266  
  267:         current_cmc_ip = re.search(r'\d+\.\d+\.\d+\.\d+',
  268                                     line).group(0).strip(r' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\scripts\install_image.py:
  63      for line in pipe.stdout:
  64:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  65                  is not None):

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\conftest.py:
  169          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  170:         serial = re.search(r'Serial:.*', info_string).group(0).\
  171              replace('Serial:', '').strip(' \n\t\r')

  186          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  187:         serial = re.search(r'Serial:.*', info_string).group(0).\
  188              replace('Serial:', '').strip(' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_hostsettings_policy_push.py:
  111      # verifing the primary and secondary dns server
  112:     sh_dns_names = re.search(r'Name server: .*\n.*\n', sh_dns_settings). \
  113          group(0).replace('Name server: ', '').strip(' \n\t\r').split('\n')

  123          model.show_web().raw
  124:     sh_proxy = re.search(r'Network Proxy:.*\n.*\n.*', sh_proxy_settings). \
  125          group(0).replace('Network Proxy:', '').strip(' \n\t\r').split('\n')
  126:     sh_proxy_name = re.search(r'Address:.*', sh_proxy[0]).group(0). \
  127          replace('Address:', '').strip(' \n\t\r')

  129          assert False, " The web proxy is not added in sh "
  130:     sh_port = re.search(r'Port:.*', sh_proxy[1]).group(0). \
  131          replace('Port:', '').strip(' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_inpath_mgmt_policy_push.py:
  123      # Verifying ipv4 inpath settings
  124:     sh_inpath_ip4 = re.search(r'IP address:.*', sh_inpath_settings).group(0).\
  125          replace('IP address:', '').strip(' \n\r\t')

  127          assert False, " IPv4 Address is not added in sh "
  128:     sh_inpath_mask = re.search(r'Netmask:.*', sh_inpath_settings).\
  129          group(0).replace('Netmask:', '').strip(' \n\r\t')

  132      # Verifying ipv6 inpath settings
  133:     sh_inpath_ip6 = re.search(
  134          r'IPv6 address:.*',

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_manage_appliances.py:
  102          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  103:         serial = re.search(r'Serial:.*', info_string).\
  104              group(0).replace('Serial:', '').strip(' \n\t\r')

  276      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  277:     serial = re.search(r'Serial:.*', info_string).\
  278          group(0).replace('Serial:', '').strip(' \n\t\r')

  317              appliance['hostname']].model.show_info().raw
  318:         health = re.search(r'Status:.*', info_text).group(0).\
  319              replace('Status:', '').strip(' \n\t\r')

  339              appliance['hostname']].model.show_info().raw
  340:         health = re.search(r'Status:.*', info_text).group(0).\
  341              replace('Status:', '').strip(' \n\t\r')

  369      info_string_1 = resources.sh_actors[sh1.hostname].model.show_info().raw
  370:     serial_1 = re.search(r'Serial:.*', info_string_1).group(0).\
  371          replace('Serial:', '').strip(' \n\t\r')

  382      info_string_2 = resources.sh_actors[sh2.hostname].model.show_info().raw
  383:     serial_2 = re.search(r'Serial:.*', info_string_2).group(0).\
  384          replace('Serial:', '').strip(' \n\t\r')

  447      info_string = resources.sh_actors[sh1.hostname].model.show_info().raw
  448:     serial = re.search(r'Serial:.*', info_string).group(0).\
  449          replace('Serial:', '').strip(' \n\t\r')

  464      status = resources.scc_actor.model.show_cmc_op_history().raw
  465:     assert 'failed' == re.search(r' *Unlock Vault *\w* *', status).\
  466          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  472      status = resources.scc_actor.model.show_cmc_op_history().raw
  473:     assert 'failed' == re.search(r' *Unlock Vault *\w* *', status).\
  474          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  480      status = resources.scc_actor.model.show_cmc_op_history().raw
  481:     assert 'success' == re.search(r' *Unlock Vault *\w* *', status).\
  482          group(0).replace('Unlock Vault', '').strip(' \n\t\r')

  518          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  519:         serial = re.search(r'Serial:.*', info_string).\
  520              group(0).replace('Serial:', '').strip(' \n\t\r')

  557          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  558:         serial = re.search(r'Serial:.*', info_string).\
  559              group(0).replace('Serial:', '').strip(' \n\t\r')

  610      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  611:     serial = re.search(r'Serial:.*', info_string).\
  612          group(0).replace('Serial:', '').strip(' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_ntp_over_ipv6.py:
  48          req_ntp_servers_parsed = \
  49:             re.search(r'NTP servers:.*\n\n',
  50                        req_ntp_servers,

  76      # Get current scc date from datetme string.
  77:     current_scc_date = re.search(
  78          r'Date: .*', scc_date_time_str).\

  80      # Get current scc time from datetme string.
  81:     current_scc_time = re.search(
  82          r'Time: .*', scc_date_time_str).\

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_ntp_policy_push.py:
  106          model.show_ntp().raw
  107:     sh_ntp_servers = re.search(
  108          r'NTP servers:.*\n.*\n.*\n.*',

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_operation_history.py:
   55      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   56:     serial = re.search(r'Serial:.*', info_string).\
   57          group(0).replace('Serial:', '').strip(' \n\t\r')

  111      op_history = resources.scc_actor.model.show_cmc_op_history().raw
  112:     assert 'rbm_user' in re.search(r'\n\n.*', op_history).\
  113          group(0), 'policy push operation is logged using a different user'

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_policy_push_for_non_admin_connected_appliances.py:
   93      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   94:     serial = re.search(r'Serial:.*', info_string).\
   95          group(0).replace('Serial:', '').strip(' \n\t\r')

  202      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  203:     serial = re.search(r'Serial:.*', info_string).\
  204          group(0).replace('Serial:', '').strip(' \n\t\r')

  312      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  313:     serial = re.search(r'Serial:.*', info_string).\
  314          group(0).replace('Serial:', '').strip(' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_scc_external_backup.py:
  316      info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  317:     serial = re.search(r'Serial:.*', info_string).\
  318          group(0).replace('Serial:', '').strip(' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\hardening_tests\test_smtp_policy_push.py:
  104          model.show_email().raw
  105:     sh_smtp_name = re.search(r'Mail hub:.*', sh_email_settings).group(0).\
  106          replace('Mail hub:', '').strip(' \n\r\t')

  108          assert False, " smtp server is not added in sh "
  109:     sh_smtp_port = re.search(r'Mail hub port:.*', sh_email_settings).\
  110          group(0).replace('Mail hub port:', '').strip(' \n\r\t')

  114      for item in ['Event emails', 'Failure emails']:
  115:         sh_emails = re.search(r'' + item + '.*\n.*\n.*\n.*\n',
  116                                sh_email_settings).group(0)
  117:         sh_is_enabled = re.search(r'Enabled:.*', sh_emails).\
  118              group(0).replace('Enabled:', '').strip(' \n\r\t')

  120              assert False, sh_emails + " is not enabled "
  121:         sh_recipients = re.search(r'Recipients:.*\n.*', sh_emails).\
  122              group(0).replace('Recipients:', '').strip(' \n\r\t').split(',')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_appliance_backup_restore.py:
  67          result = resources.sh_actors[sh.hostname].model.show_banner().raw
  68:         MOTD = re.search(
  69              r'MOTD:.*', result).group(0).replace('MOTD:', '').strip(' \n\r\t')

  83          result = resources.sh_actors[sh.hostname].model.show_banner().raw
  84:         MOTD = re.search(
  85              r'MOTD:.*', result).group(0).replace('MOTD:', '').strip(' \n\r\t')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_appliance_inventory.py:
   41          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   42:         serial = re.search(r'Serial:.*', info_string).group(0).\
   43              replace('Serial:', '').strip(' \n\t\r')

  123          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  124:         serial = re.search(r'Serial:.*', info_string).\
  125              group(0).replace('Serial:', '').strip(' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_generic_infrastructure_framework.py:
  125          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  126:         serial = re.search(r'Serial:.*', info_string).\
  127              group(0).replace('Serial:', '').strip(' \n\t\r')

  140          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  141:         serial = re.search(r'Serial:.*', info_string).\
  142              group(0).replace('Serial:', '').strip(' \n\t\r')

  161          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  162:         serial = re.search(r'Serial:.*', info_string).\
  163              group(0).replace('Serial:', '').strip(' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_kvm_cmc_installation.py:
  178          self.kvm_host.expect(self.kvm_scc_name + r' \(config\) #')
  179:         primary_hw_address = re.search(
  180              r'HW address:.*',

  198          self.kvm_host.expect(self.FOLDER_PROMPT)
  199:         licence1 = re.search(r'\r\n.*\r\n',
  200                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  202          self.kvm_host.expect(self.FOLDER_PROMPT)
  203:         licence2 = re.search(r'\r\n.*\r\n',
  204                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  206          self.kvm_host.expect(self.FOLDER_PROMPT)
  207:         licence3 = re.search(r'\r\n.*\r\n',
  208                               self.kvm_host.before).group(0).strip(r' \n\t\r')

  226          self.kvm_host.expect(self.kvm_scc_name + r' \(config\) #')
  227:         self.aux_ip_address = re.search(
  228              r'IP address:.*',

  233          file.close()
  234:         aux_net_mask = re.search(
  235              r'Netmask:.*',

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_physical_cmc_installation.py:
  62      for line in pipe.stdout:
  63:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  64                  is not None):

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_scc_secure_transport.py:
  182          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  183:         serial = re.search(r'Serial:.*', info_string).\
  184              group(0).replace('Serial:', '').strip(' \n\t\r')

  200          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
  201:         serial = re.search(r'Serial:.*', info_string).\
  202              group(0).replace('Serial:', '').strip(' \n\t\r')

  219          resources.client_sh.hostname].model.show_info().raw
  220:     serial = re.search(r'Serial:.*', info_string).\
  221          group(0).replace('Serial:', '').strip(' \n\t\r')

  241      # Get current scc date from datetme string.
  242:     current_scc_date = re.search(
  243          r'Date: .*', current_scc_time_str).\

  245      # Get current scc time from datetme string.
  246:     current_scc_time = re.search(
  247          r'Time: .*', current_scc_time_str).\

  280      # Get current scc date from datetme string.
  281:     current_scc_date = re.search(
  282          r'Date: .*', current_scc_time_str).\

  284      # Get current scc time from datetme string.
  285:     current_scc_time = re.search(
  286          r'Time: .*', current_scc_time_str).group(0).\

  339          resources.client_sh.hostname].model.show_info().raw
  340:     serial = re.search(r'Serial:.*', info_string).\
  341          group(0).replace('Serial:', '').strip(' \n\t\r')

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_stats_operation.py:
   71          info_string = resources.sh_actors[sh.hostname].model.show_info().raw
   72:         serial = re.search(r'Serial:.*', info_string).\
   73              group(0).replace('Serial:', '').strip(' \n\t\r')

  117      # Get current scc date from datetme string.
  118:     current_scc_date = re.search(
  119          r'Date: .*', current_scc_time_str).\

  121      # Get current scc time from datetme string.
  122:     current_scc_time = re.search(
  123          r'Time: .*', current_scc_time_str).\

  156      # Get current scc date from datetme string.
  157:     current_scc_date = re.search(
  158          r'Date: .*', current_scc_time_str).\

  160      # Get current scc time from datetme string.
  161:     current_scc_time = re.search(
  162          r'Time: .*', current_scc_time_str).\

  200      # Get current scc date from datetme string.
  201:     current_scc_date = re.search(
  202          r'Date: .*', current_scc_time_str).\

  204      # Get current scc time from datetme string.
  205:     current_scc_time = re.search(
  206          r'Time: .*', current_scc_time_str).\

sc\portfolio-system-tests\portfolio_system_tests\legacy_ssi_tests\tests\sanity_tests\test_virtual_cmc_installation.py:
  61      for line in pipe.stdout:
  62:         if (re.search(r'\[PASS\]: Successfully installed.*', line)
  63                  is not None):

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_performance\scaleperf_qa\libs\QAPerf.py:
   422                  first_run and not bi_directional:
   423:             if re.search('tx', key):
   424                  interfaces_keys.extend([key])
   425:             elif re.search('rx', key):
   426                  interfaces_keys.extend([key])

   470                              tx_data = re.compile(r'TX\sbytes:(\d+)')
   471:                             if re.search(rx_data, inter):
   472:                                 data1 = re.search(rx_data, inter)
   473                                  interface[ser + '_rx_data'] = data1.group(1)
   474:                             if re.search(tx_data, inter):
   475:                                 data2 = re.search(tx_data, inter)
   476                                  interface[ser + '_tx_data'] = data2.group(1)

   650              location = data_col + str(row)
   651:             temp = re.search(r'(\d+.*\d*)\s+\w', ws[location].value)
   652              record_tput = temp.group(1)

   694              break
   695:         # if not re.search('.+bits/sec', line):
   696          #     continue
   697  
   698:         # rate_found = re.search('Bytes\s+(\d+.*\d*)\s+(\wbits/sec)', line)
   699:         rate_found = re.search(pattern, line)
   700          if rate_found:

   750  
   751:         rate_found = re.search(pattern, line)
   752          if rate_found:

   895      for line in output_server.splitlines():
   896:         if re.search(r'iperf\s+.+', line):
   897:             output_server_new = re.search(r'(iperf\s+.+)', line)
   898              output_server = output_server_new.group(0)
   899      for line in output_client.splitlines():
   900:         if re.search(r'iperf\s+.+', line):
   901:             output_client_new = re.search(r'(iperf\s+.+)', line)
   902              output_client = output_client_new.group(0)

   927  
   928:         if re.search(r'8\.\d\.\d\.\s+Ethernet\s+Frame\s+Rates', row) or found:
   929              found = True
   930:             if re.search(
   931                      r'\d+\.*\d*\',\s+\'(\d+,*\d*\.*\d*)\',\s+\''
   932                      r'(\d*,*\d+\.*\d*)\'', row):
   933:                 data_new = re.search(
   934                      r'\d+\.*\d*\',\s+\'(\d+,*\d*\.*\d*)\',\s+\''

   941  
   942:         if re.search(r'8\.\d\.\d\.\d\.\sEthernet\s+Frame\s+Rates:\s1', row) \
   943                  and data_count:

  1800      regex = re.compile(r'(\w+)\s*(\d+)/(\d+)')
  1801:     if re.search(regex, untagged):
  1802:         untagged_data = re.search(regex, untagged)
  1803          slot = untagged_data.group(2)

  2250              break
  2251:         if re.search(pattern_loss, line):
  2252:             drop_rate = re.search(pattern_loss, line)
  2253              percent = float(drop_rate.group(1))
  2254              total_percent += percent
  2255:         if re.search(pattern_rate, line):
  2256:             rec_rate = re.search(pattern_rate, line)
  2257              rate_int = float(rec_rate.group(1))

  2316              break
  2317:         if re.search(pattern, line):
  2318              total_checked_count += 1
  2319:             drop_rate = re.search(pattern, line)
  2320              total_bytes = drop_rate.group(1)

  2327              total_percent += percent
  2328:         if re.search(pattern_sum, line):
  2329              sum_count += 1
  2330:             sum_rate = re.search(pattern_sum, line)
  2331              sum_int = float(sum_rate.group(2))

  2354      """
  2355:     rate = re.search(r'-B\s*(\d+)(\w{1,2})', client_opt)
  2356      old_rate = rate.group(1) + rate.group(2)

  2376      """
  2377:     rate = re.search(r'-b\s*(\d+)(\w{1,3})', client_opt)
  2378      old_rate = rate.group(1) + rate.group(2)

  2403      """
  2404:     rate = re.search(r'-b\s*(\d+)', bw_rate)
  2405      client_opt_rate = str(int(rate.group(1)))

  3176  
  3177:         if re.search(pattern, line):
  3178:             found = re.search(pattern, line)
  3179              new_rate = str(float(found.group(1)) * REDUCE_TRAFFIC_80_PERCENT)

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\add_additional_outbound_rules.py:
  75          total_rule_count += 1
  76:         m = re.search(r'Pod(\d+)_vgw_branch(\d+)_obrule(\d+)', rule['name'])
  77          if m:

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\add_additional_trafficpath_rules.py:
  78          total_rule_count += 1
  79:         m = re.search(r'Pod(\d+)_vgw_branch(\d+)_tpr(\d+)', rule['name'])
  80          if m:

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\delete_old_stack.py:
  46      """
  47:     if (re.search(
  48          r'One or more ports have an IP allocation from this subnet',

  63      # the router UUID first and then deleting the stack
  64:     elif (re.search(
  65            r'it is required by one or more routes', delete_status)):

sc\portfolio-system-tests\portfolio_system_tests\legacy_steelconnect_system_tests\solutions_scale\test_system_info_from_scm.py:
  216      for line in f:
  217:         if re.search(r'runsv nginx', line):
  218              process_data = line.split()

  229      for line in f:
  230:         if re.search(r'runsv postgresql', line):
  231              process_data = line.split()

  242      for line in f:
  243:         if re.search(r'runsv redis', line):
  244              process_data = line.split()

  255      for line in f:
  256:         if re.search(r'mojo/Cc.pl\b\s.*hydra.*', line):
  257              process_data = line.split()

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\devices_cli.py:
  185          'ifconfig | grep ' + interface)
  186:     mac_address = re.search("HWaddr {}".format(
  187          mac_pattern), mac_details).group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\syslog.py:
  177      pat = r"prefix=\W+{}\W+".format(prefix)
  178:     match = re.search(pat, conf)
  179      assert match is not None, "prefix {} not found in gw rsyslog config file" \

  342      for line in lines:
  343:         if re.search(msg, line) and re.search(prefix, line) and \
  344:                 re.search("<{}>".format(priority), line) and \
  345:                 re.search(serial, line):
  346              LOGGER.info("LOG message '{}' with prefix '{}', priority '{}',"

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\traffic.py:
  177      ping_result = shell.exec_command('ping {} -c {}'.format(host, count))
  178:     host_ip = re.search(
  179          r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', ping_result).group(0)

  264          cmd, curl_command_result))
  265:     http_status = re.search("HTTP/1.1 ([0-9]{3})", curl_command_result).group(
  266          1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steelbranch\test_steelbranch\zscaler_client.py:
  106      ping_result = shell_default_ns(mgmt_ip, ping)
  107:     loss = re.search('([0-9]{1,3})%', ping_result).group(1)
  108      # Be more sloppy for low ping intervals, since first ping may fail

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\disjoint_wan\test_route_propagation.py:
  104      for line in tunnels:
  105:         match = re.search(r"vti(\d+\_\d+\_\d+).*remote\s"
  106                            r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

  293          # Check learned routes on CGW
  294:         if re.search(r"123\.123\.123\.0", cgw_routes):
  295              criteria += 1

  334          # Check learned routes on CGW
  335:         if re.search(r"123\.123\.123\.0", cgw_routes):
  336              fail_msg += "Route to 123.123.123.0 not retracted from CGW: "

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\disjoint_wan\helpers\utils.py:
  157      for tunnel in tunnels:
  158:         vti = re.search(r'(vti\d+_\d+_\d+)', tunnel)
  159          if vti:

  161  
  162:         remote = re.search(r'remote (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  163                             tunnel)

  167  
  168:         local = re.search(r'local (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  169                            tunnel)

  202          for line in conf:
  203:             if re.search(r"X.*{}".format(vti), line):
  204                  found += 1

  206              if found:
  207:                 check_line = re.search(
  208                      r".*checkip.*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)

  231      for line in lines:
  232:         top = re.search(
  233              r"^[\*\s][>\s][i\s]" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" +

  237              r"([\d\s]*)i?", line)
  238:         alt = re.search(
  239              r"^[\*\s][>\s][i\s]" + r"\s{17}" +

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_bgp_neighbor.py:
  37      for line in lines:
  38:         top = re.search(
  39              r"^[\*\s][>\s][i\s]\s" + r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})" +

  42              r"([\d\s]*)[i\?]?", line)
  43:         alt = re.search(
  44              r"^[\*\s][>\s][i\s]" + r"\s+" +

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_default_route_originate.py:
   98      list_client = output.split('\n')
   99:     regex = re.search("\Send:\W+(\d+)\W+Recv:\W+(\d+)", list_client[0])  # noqa
  100      if regex:

  109      list_server = output.split('\n')
  110:     regex_server = re.search("Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)", list_server[0])  # noqa
  111      if regex_server:

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_dynamicrouting_bgp_bandwidth_limit.py:
  65      server_log = open(traffic.server_log_file, 'r').read()
  66:     bandwidth = re.search(r'(.\w?) Mbits/sec', server_log).group()
  67      bandwidth = bandwidth.replace('Mbits/sec', '').strip()

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_pqps.py:
  112      list_client = output.split('\n')
  113:     regex = re.search("\Send:\W+(\d+)\W+Recv:\W+(\d+)", list_client[0])  # noqa
  114      if regex:

  123      list_server = output.split('\n')
  124:     regex_server = re.search("Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)", list_server[0])  # noqa
  125      if regex_server:

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_static_routing.py:
  106      list_client = output.split('\n')
  107:     regex = re.search(r"\Send:\W+(\d+)\W+Recv:\W+(\d+)",
  108                        list_client[0])

  118      list_server = output.split('\n')
  119:     regex_server = re.search(r"Send:\s+(\d+)\s\(.+\)\s+Recv:\s+(\d+)",
  120                               list_server[0])

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing\test_zebos_config_check_bgp.py:
  44          elif line.strip().startswith('network') and \
  45:                 re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  46              gw_output['networks'].append(line.replace('network', '').strip())

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\conftest.py:
  119              ipPattern = re.compile(r'[0-9]+(?:\.[0-9]+){3}')
  120:             route = re.search(ipPattern, line).group()
  121              if route:

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\dynamic_routing_with_ha\test_dynamic_routingwithha_gateway_link_failure.py:
  57      output = gw_shell.exec_command('imish -e "show ip route"')
  58:     if not re.search(zone_ip, output):
  59          pytest.fail("Zone ip is not present on the BGP route")
  60:     match = re.search(r'Total number of prefixes (\d+)', output)
  61      if match and int(match.group(1)) != 1:

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_new_zone_discovery.py:
  154      for element in gw_output.splitlines():
  155:         if re.search(network_ip, element):
  156              return True

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_remove_interface_from_area.py:
  105      for network in networks:
  106:         if re.search("discovered", network.name, re.IGNORECASE):
  107              count += 1

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_route_peering.py:
  46  
  47:             if re.search("Full", element):
  48                  ospf_neighbors.append(ip_address)

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\novartis\test_ospf_zebos_config_change.py:
  37          if line.strip().startswith('network') and \
  38:                 re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]", line):
  39              gw_output['network'].append(re.findall(

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\ospf_multi_lan\test_traffic.py:
   47          for interface in if_op:
   48:             if re.search("192.168.15", if_op[interface]['addr']):
   49                  disabled_ints[router] = interface

  106      for interface in if_op:
  107:         if re.search("192.168.15", if_op[interface]['addr']):
  108              break

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\test_leaf_mode.py:
  97                  for line in chain.split('\n'):
  98:                     route = re.search('set-device ' + vti, line)
  99                      if route:

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\docker\transit_routing\helpers\utils.py:
  31      for tunnel in tunnels:
  32:         vti = re.search(r'(vti\d+_\d+_\d+)', tunnel)
  33          if vti:

  35  
  36:         remote = re.search(r'remote (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  37                             tunnel)

  41  
  42:         local = re.search(r'local (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
  43                            tunnel)

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\2gw_sh-1catfish-1gw\test_optimized_path_selection.py:
  175          for custom_app in custom_app_list:
  176:             if re.search("TCP_APP", custom_app.name, flags=re.IGNORECASE):
  177                  resources.org_obj.custom_app_management(

  189      for custom_app in custom_app_list:
  190:         if re.search("TCP_APP", custom_app.name, flags=re.IGNORECASE):
  191              custom_app_obj = custom_app

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\helpers\utils.py:
   138                  m = \
   139:                     re.search(r'(O\>\*|O\s\s)\s'
   140                                r'(\d+\.\d+\.\d+\.\d+\/\d+).*%s' % interface,

   142              else:
   143:                 m = re.search(r'(O\>\*|O\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)',
   144                                line)
   145          elif specific_route.lower() == 'bgp':
   146:             m = re.search(r'(B\>\*|B\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   147          elif specific_route.lower() == 'static':
   148:             m = re.search(r'(S\>\*|S\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   149          elif specific_route.lower() == 'connected':
   150:             m = re.search(r'(C\>\*|C\s\s)\s(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   151          else:
   152:             m = re.search(r'(\d+\.\d+\.\d+\.\d+\/\d+)', line)
   153          if m:

   202              if aspath is not None:
   203:                 m = re.search(r'(\d+\s\d+\s\d+)', line)
   204              else:
   205:                 m = re.search(r'(\d{5}\s\d{4})', line)
   206              if m is not None:

   356      for route in route_op.split("OSPF external")[1].split("\n"):
   357:         ips = re.search(r'(\d+\.\d+\.\d+\.\d+\/\d+)', route)
   358          metric_value = re.\
   359              search(r'((\[\d+\]|\[\d+/0\]|\[\d+/\d+\])\s\w+:\s\d+)', route)
   360:         type_route = re.search(r'(E\d)', route)
   361          if ips:

   902      ospf_int_output = container_shell.exec_command(cmd1)
   903:     cost = re.search(r'Cost: (\d+)', ospf_int_output)
   904:     priority = re.search(r'Priority (\d+)', ospf_int_output)
   905:     hello = re.search(r'Hello (\d+)', ospf_int_output)
   906:     dead = re.search(r'Dead (\d+)', ospf_int_output)
   907      return (cost.group(1), priority.group(1), hello.group(1), dead.group(1))

  1126      routes_info = container_shell.exec_command(cmd)
  1127:     routes_ip_info = map(lambda y: re.search(r'\s.(\d*.\d*.\d*.\d*)\s', y).
  1128                           group(0).strip(), routes_info.

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ibt\features\upgrade\test_upgrade.py:
  125      print(univ_op)
  126:     latest_build_tag = re.search('binary_builds.*browse/(.+)', univ_op).\
  127          group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ospf_bgp_trio\test_ospf_failures.py:
  46      for network in networks:
  47:         if re.search("Discovered", network.name):
  48              count += 1

sc\portfolio-system-tests\portfolio_system_tests\legacy_test_steeloc_qa\test_steeloc_qa\openstack\ospf_bgp_trio\test_ospf_remove_interface_from_area.py:
  151      for network in networks:
  152:         if re.search("discovered", network.name, re.IGNORECASE):
  153              count += 1

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_hardware_spec_activate.py:
   70                                                          timeout=180)
   71:                     result = re.search(r'Stopped', result)
   72                      if result:

  121                                                      timeout=180)
  122:                 result = re.search(r'Healthy', result)
  123                  if result:

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability_client_sh.py:
  148          # The model extracted is in this form "VCX (VCX10)"
  149:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  150          sh_model_found = sh_model_detected.group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability_server_sh.py:
  158          # The model extracted is in this form "VCX (VCX10)"
  159:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  160          sh_model_found = sh_model_detected.group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_model_capability.py:
  189          # The model extracted is in this form "VCX (VCX10)"
  190:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  191          sh_model_found = sh_model_detected.group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\test_sh_volume_size.py:
  160          # The model extracted is in this form "VCX (VCX10)"
  161:         sh_model_detected = re.search(r'\((.*)\)', sh_model_detected)
  162          sh_model_found = sh_model_detected.group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\fvsh-openstack\openstack-tests\openstack_ops.py:
  50              for stack_name in self.stack_name_list:
  51:                 search_string=re.search(r'jenkins-Axel-VSH-CAT-\d+_\w+',stack_name)
  52                  if search_string != None:

sc\portfolio-system-tests\portfolio_system_tests\legacy_vsh_tests\provisioning\test_user_data.py:
  360                  if "Model" in line:
  361:                     m = re.search(r"\(([A-Za-z0-9_]+)\)", line)
  362                      print("Found Model: " + m.group(1))

  485      if(not invalid):
  486:         assert re.search(re.escape(expression),show_run)
  487      else:
  488:         assert re.search(re.escape(log_expression),show_rsisinit_log)
  489:         assert not re.search(re.escape(expression),show_run)
  490  

sc\portfolio-system-tests\portfolio_system_tests\legacy_webcache_tests\http_server_allocation.py:
  317              cli_result = Model.get(fe).show_info()
  318:             if re.search("Service needs a 'restart'", cli_result.raw, re.I):
  319                  fes_to_restart.append(fe)

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\auditoperations.py:
   53      for line in zfile:
   54:         m = re.search(r"Created key with name='([^']+)' .* operation='Create"
   55                        " root CA", line)

   65      for line in zfile:
   66:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
   67                        "keyvault for user operation='Create root CA for "

   79      for line in zfile:
   80:         m = re.search(r"Create root CA for org=([^\s]+) CN=(.*) completed by "
   81                        "user='([^']*)' with signing key name='([^']+)'", line)

   92      for line in zfile:
   93:         m = re.search("-BEGIN CERTIFICATE-.*", line)
   94          if m:

  107      for line in zfile:
  108:         m = re.search(r"Created key with name='([^']+)' .* operation="
  109                        "'Create and activate root CA", line)

  120      for line in zfile:
  121:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
  122                        "keyvault for user operation='Create and activate root "

  134      for line in zfile:
  135:         m = re.search(r"Create and activate root CA for org=([^\\s]+) CN=(.*)"
  136                        "completed by user='([^']*)' with signing key name="

  148      for line in zfile:
  149:         m = re.search("-BEGIN CERTIFICATE-", line)
  150          if m:

  164      for line in zfile:
  165:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Signed digest='([^']+)' "
  166                        "using key='([^']+)' from keyvault for user operation="

  180      for line in zfile:
  181:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Sign peering cert request for CN="
  182                        "([^']+) from requestor=([^\\s]+) completed", line)

  193      for line in zfile:
  194:         m = re.search("-BEGIN CERTIFICATE-", line)
  195          if m:

  209      for line in zfile:
  210:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Signed digest='([^']+)' using "
  211                        "key='([^']+)' from keyvault for user operation="

  225      for line in zfile:
  226:         m = re.search(r"([\d\/]+\s[\d\:]+)\s+Sign proxy cert request for "
  227                        "CN=([^']+) from requestor=([^\\s]+) completed", line)

  238      for line in zfile:
  239:         m = re.search(".*-BEGIN CERTIFICATE-.*", line)
  240          if m:

  253      for line in zfile:
  254:         m = re.search(r"Created key with name='([^']+)' .* operation="
  255                        "'Create intermediate CA CSR", line)

  265      for line in zfile:
  266:         m = re.search(r"Signed digest='([^']+)' using key='([^']+)' from "
  267                        "keyvault for user operation='Create intermediate CA "

  279      for line in zfile:
  280:         m = re.search(r"Create intermediate CA CSR for org=([^\s]+) CN=(.*) "
  281                        "completed by user='([^']*)' with signing key name="

  293      for line in zfile:
  294:         m = re.search("-BEGIN CERTIFICATE-", line)
  295          if m:

  308      for line in zfile:
  309:         m = re.search(r".*Retrieved public key with name='([^']+)' .* "
  310                        "operation='Delete CSR", line)

  321      for line in zfile:
  322:         m = re.search(r"Deleted key='([^']+)' from keyvault for user operation"
  323                        "='Delete CSR for org=([^\\s]+) CN=([^']+)", line)

  333      for line in zfile:
  334:         m = re.search(r"Delete CSR for org=([^\s]+) CN=(.*) completed by user="
  335                        "'([^']*)' with signing key name='([^']+)'.*", line)

  350      for line in zfile:
  351:         m = re.search(r"Retrieved public key with name='([^']+)' .* "
  352                        "operation='Delete CA", line)

  363      for line in zfile:
  364:         m = re.search(r"Deleted key='([^']+)' from keyvault for user operation"
  365                        "='Delete CA for org=([^\\s]+) CN=([^']+)", line)

  375      for line in zfile:
  376:         m = re.search(r"Delete CA for org=([^\s]+) CN=(.*) completed by user"
  377                        "='([^']+)' with signing key name '([^']+)'", line)

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\azure_helper.py:
  282          pip_id = nic_params.ip_configurations[0].public_ip_address.id
  283:         pip_name = re.search(r'[^/]*$', pip_id).group(0)
  284          public_ip_address = \

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\conftest.py:
   308          output = automodel.show_peers(online_only=True)
   309:         m = re.search("Connected appliances:\\s+(\\d+)", output.raw)
   310          no_of_peers = int(m.group(1))

   318          zak_serial_no = get_zak_serial_no(scm_actor)
   319:         if (re.search(zak_serial_no, output.raw)):
   320              return 1

   414              azure_helper = AzureHelper()
   415:             zaksh_name = re.search(r'([^\s]+)', zaksh_data).group()
   416              zaksh_nic_ids = azure_helper.get_vm_nic_ids(rg, zaksh_name)
   417:             nic_name = re.search(r'[^/]*$', zaksh_nic_ids[0]).group(0)
   418              pip = azure_helper.get_nic_public_ip(rg, nic_name)

   780          output = zaksh_shell.exec_command(cmd)
   781:         curr_log = re.search(r'(\S+) file', output).group(1)
   782          logger.info(f"Current ZAKSH log level: {curr_log}")

   883          else:
   884:             m = re.search("Address:\\s+(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s*$",
   885                            output)

  1173          output = automodel.show_peers(online_only=True)
  1174:         if (re.search("No connected peer", output.raw)):
  1175              return 1
  1176:         m = re.search("Connected appliances:\\s+(\\d+)", output.raw)
  1177          no_of_peers = int(m.group(1))

  1429                                    allocation=Allocation())
  1430:         zaksh_ip = re.search('(?<=\[)[^]]+(?=\])', zak_sh_data).group()  # noqa
  1431          admin_cidr = ipaddress.ip_interface(str(zaksh_ip + "/0"))

  2013              raise ValueError("There is no application token")
  2014:         app_token = re.search("(^\\S*)", value).group(0)
  2015          return app_token

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\legacy_sh_tests\vanautu\test_cfe_lb_none.py:
  28      assert("GLB Secondary Ports" not in output.keys())
  29:     lb_ports = re.search("(\\d+)-(\\d+)", output['load balancer port range'])
  30      port1 = int(lb_ports.group(1))

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\misc_scripts\docker_remove_oldimage.py:
  17  for line in output.splitlines():
  18:     m = re.search("quay.*bamboo.*\\s+(\\S+)\\s+(\\d+)\\s+(hours|days) ago",
  19                    line)

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\conftest.py:
   456              try:
   457:                 lb_ip = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',
   458                                    output).group(0)

   491          assert(vm_info is not None)
   492:         output = re.search('{.*}', vm_info)
   493          assert(output)

   642          challenge_str = actor.model.cli_challenge_generate().raw
   643:         token_obj = re.search(r'Generated challenge: (.*)', challenge_str)
   644          if token_obj:

   651          output = local_shell.exec_command(cmd, timeout=TIMEOUT)
   652:         response_obj = re.search(r'cli challenge response (.*)', output)
   653          if response_obj:

   787              app_restrict_flag = \
   788:                 re.search(r'app_restriction_enable=(\S+)', out).group(1)
   789              logger.info(f"Current app restriction: {app_restrict_flag}")

   798              out = ssh_shell.exec_command(cmd)
   799:             curr_log = re.search(r'(\S+) file', out).group(1)
   800              logger.info(f"Current log level: {curr_log}")

   816                  copy_util.copy_from_host(zaksh, "/dumps/", cert_path)
   817:                 cert_file = re.search(r'[^/]*$', cert_path).group(0)
   818                  cmd = (f"sudo cp /dumps/{cert_file} /var/opt/rbt/ssl/ca/; "

  1138              output_expected=True)
  1139:         if re.search(r'active', output):
  1140              return True

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\csh_data_disks_operations.py:
  96      output = perfHelper.execute_shell_cmds_csh(csh, [cmd])
  97:     num_disks = re.search(r"(.*)$", output.decode("utf-8")).group(0)
  98      log.info(f"Number of data disks attached to CSH: {num_disks}")

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\setup_clients_servers.py:
   88          output = shell.exec_command(cmd, output_expected=True)
   89:     version = re.search(r'(\d+.\d+)', output)
   90      if version:

  171          with open('60-static.yaml', 'w') as infile:
  172:             match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}', eth0_ip).group(0)
  173              infile.write(NETPLAN.format(eth0_ip, match))

  176                      str(actor_client.resource.interfaces[f'test{eth}'].cidr.ip)
  177:                 match = re.search(r'\d{1,3}.\d{1,3}.\d{1,3}', eth_ip).group(0)
  178                  infile.write(ETH.format(eth, eth_ip, match, eth))

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\zak_cluster.py:
   67      zaksh_ip = \
   68:         re.search(r'(?<=\[)[^]]+(?=\])', zaksh_data).group()
   69      admin_cidr = ipaddress.ip_interface(str(zaksh_ip + "/0"))

  143          zahsh_name = \
  144:             re.search(r'([^\s]+)', zaksh_data).group()
  145          zaksh_resource = create_zaksh_resource(zaksh_data,

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\perf_tests\zaksh_setup\azure_helper.py:
  2685          for vm_nic in vm_nics_list:
  2686:             if re.search('-ul2', vm_nic.name):
  2687                  all_vm_resources["nic_uplink2"] = vm_nic.name

  2691                      all_vm_resources["subnet_uplink2"] = subnet
  2692:             elif re.search('-ul', vm_nic.name):
  2693                  all_vm_resources["nic_uplink"] = vm_nic.name

  2697                      all_vm_resources["subnet_uplink"] = subnet
  2698:             if re.search('-dl', vm_nic.name):
  2699                  all_vm_resources["nic_downlink"] = vm_nic.name

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\shm_tests\shm_helper.py:
   75          cmd_output = self.client_shell.exec_command(cmd)
   76:         status = re.search(search_pattern, cmd_output)
   77          if status:

  155          cmd_output = self.client_shell.exec_command(cmd)
  156:         app_content = re.search(search_pattern, cmd_output, re.DOTALL)
  157          if app_content:

  170              application_map['dest_port'] = int(dest[1])
  171:             application_map['app_id'] = int(re.search(".*snoopy_app="
  172                                                        "(\\d+)", app).group(1)

sc\portfolio-system-tests\portfolio_system_tests\legacy_zaksh_tests\tests\zak_sh_troubleshoot\test_zaksh_nic_nw_acceleration.py:
   85              output = zak_sh_shell.exec_command(cmd, output_expected=True)
   86:             ipv4_address = re.search(r'inet \d+.\d+.\d+.\d+', output)
   87              assert(ipv4_address is None)

   91              output = zak_sh_shell.exec_command(cmd, output_expected=True)
   92:             ipv4_address = re.search(r'inet \d+.\d+.\d+.\d+', output)
   93              if (ipv4_address is None):

  107              assert(output is not None)
  108:             maxconn = re.search(r'net.core.somaxconn = \d+', output)
  109              fo.write("\nsomaxconn {} ".format(maxconn.group(0)))
  110:             tcpmem = re.search(r'net.ipv4.tcp_mem = \d+\s+\d+\s+\d+', output)
  111              fo.write("\ntcp_mem {} ".format(tcpmem.group(0)))
  112:             port_range = re.search(r'net.ipv4.ip_local_port_range = \d+\s+\d+',
  113                                     output)

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\configure.py:
  1768              node_name = name.strip()
  1769:             all_match = re.search(r"value: (.*) \((.*)\)", value)
  1770              if not all_match:

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\connectivity.py:
  61                  loss_re = re.compile(r'(\d*)%(?: packet)? loss')
  62:                 tx_search = tx_re.search(line)
  63:                 rx_search = rx_re.search(line)
  64:                 loss_search = loss_re.search(line)
  65                  if tx_search is not None:

  73                      r'(\d*.\d*)/(\d*.\d*)/(\d*.\d*)(?:/\d*.\d*)? ms')
  74:                 rtt_search = rtt_re.search(line)
  75                  if rtt_search is None:

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\exchange_load.py:
  221      client_resource = allocation.resources[client]
  222:     branch_suffix = re.search(r"([-]\d+)", client).group(0)
  223      sh_name = 'steelhead' + branch_suffix

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\sharepoint_load.py:
  186      client_resource = allocation.resources[client]
  187:     branch_suffix = re.search(r"([-]\d+)", client).group(0)
  188      sh_name = 'steelhead' + branch_suffix

  192  
  193:     client_suffix = re.search(r"([-]\d+)+", client)
  194      file_prefix, file_suffix = file_name.split('.')

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\verification.py:
  110          if re.match(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line) and \
  111:            re.search(r'ERR(OR)?\]', line):
  112              # Get time stamp
  113:             split = re.search(r'^\[\S+ \d+ \d+ \d+:\d+:\d+.\d+', line).group(0)
  114              date = split[1:]

  130      for line in file_contents:
  131:         if re.search(r'ERR(OR)?\]', line):
  132              error_list.append(line)

sc\portfolio-system-tests\portfolio_system_tests\spoon_tests\libs\wget_load.py:
  195      else:
  196:         branch_suffix = re.search(r"([-]\d+)", client).group(0)
  197          sh_name = 'steelhead' + branch_suffix

sc\portfolio-system-tests\portfolio_system_tests\tiramisu\test_functional_sanity_win.py:
  105  
  106:     match = re.search(r'\((?P<ip>.*?)\) port \d+', output)
  107      if match:

sc\portfolio-system-tests\portfolio_system_tests\winsec\conftest.py:
   79      # the lost percentage values.
   80:     results = re.search(r'Lost\s+=\s+(\d+)', ping_results)
   81      if results:

  902      # Matching to 'EncryptData\s+:\s+{True|False}'
  903:     enc_status = re.search(r'EncryptData\s+:\s+(\w+)',
  904                             smb_server._exec_cmd(get_cmd)).group(1)

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\wheel_builder.py:
  44      """
  45:     return bool(_egg_info_re.search(s))
  46  

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\index\package_finder.py:
  223  
  224:         match = self._py_version_re.search(version)
  225          if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\models\link.py:
  153          # type: () -> Optional[str]
  154:         match = self._egg_fragment_re.search(self._url)
  155          if not match:

  163          # type: () -> Optional[str]
  164:         match = self._subdirectory_fragment_re.search(self._url)
  165          if not match:

  175          # type: () -> Optional[str]
  176:         match = self._hash_re.search(self._url)
  177          if match:

  183          # type: () -> Optional[str]
  184:         match = self._hash_re.search(self._url)
  185          if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\req\constructors.py:
  331          # Handle relative file URLs
  332:         if link.scheme == 'file' and re.search(r'\.\./', link.url):
  333              link = Link(

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\req\req_file.py:
  348                  # original file is over http
  349:                 if SCHEME_RE.search(filename):
  350                      # do a url join so relative paths work

  352                  # original file and nested file are paths
  353:                 elif not SCHEME_RE.search(req_path):
  354                      # do a join so relative paths work

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\utils\encoding.py:
  36      for line in data.split(b'\n')[:2]:
  37:         if line[0:1] == b'#' and ENCODING_RE.search(line):
  38:             encoding = ENCODING_RE.search(line).groups()[0].decode('ascii')
  39              return data.decode(encoding)

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_internal\vcs\subversion.py:
  151          elif data.startswith('<?xml'):
  152:             match = _svn_xml_url_re.search(data)
  153              if not match:

  169                  )
  170:                 url = _svn_info_xml_url_re.search(xml).group(1)
  171                  revs = [

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distro.py:
   989              # If there is no version_codename, parse it from the version
   990:             codename = re.search(r'(\(\D+\))|,(\s+)?\D+', props['version'])
   991              if codename:

  1057          props = {}
  1058:         match = re.search(r'^([^\s]+)\s+([\d\.]+)', lines[0].strip())
  1059          if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\manifest.py:
  291          for name in self.allfiles:
  292:             if pattern_re.search(name):
  293                  self.files.add(name)

  311          for f in list(self.files):
  312:             if pattern_re.search(f):
  313                  self.files.remove(f)

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\util.py:
  709  def get_export_entry(specification):
  710:     m = ENTRY_RE.search(specification)
  711      if not m:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\_backport\sysconfig.py:
  569                  CFLAGS = _CONFIG_VARS.get('CFLAGS', '')
  570:                 m = re.search(r'-isysroot\s+(\S+)', CFLAGS)
  571                  if m is not None:

  699                  try:
  700:                     m = re.search(r'<key>ProductUserVisibleVersion</key>\s*'
  701                                    r'<string>(.*?)</string>', f.read())

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\distlib\_backport\tarfile.py:
  1402          # the translation to UTF-8 fails.
  1403:         match = re.search(br"\d+ hdrcharset=([^\n]+)\n", buf)
  1404          if match is not None:

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\html5lib\filters\sanitizer.py:
  840              if (token["name"] in self.svg_allow_local_href and
  841:                 (namespaces['xlink'], 'href') in attrs and re.search(r'^\s*[^#\s].*',
  842                                                                       attrs[(namespaces['xlink'], 'href')])):

VCMGUIAUTO_FF\venv\Lib\site-packages\pip\_vendor\urllib3\util\url.py:
  281              if is_ipv6:
  282:                 match = ZONE_ID_RE.search(host)
  283                  if match:

  356      source_url = url
  357:     if not SCHEME_RE.search(url):
  358          url = "//" + url

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\libraries\BuiltIn.py:
  1162          """
  1163:         res = re.search(pattern, string)
  1164          if res is None:

  1177          """
  1178:         if re.search(pattern, string) is not None:
  1179              raise AssertionError(self._get_string_msg(string, pattern, msg,

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\libraries\DateTime.py:
  566          input_format = self._remove_f_from_format(input_format)
  567:         match = re.search('\d+$', ts)
  568          if not match:

VCMGUIAUTO_FF\venv\Lib\site-packages\robot\parsing\model\statements.py:
  151      def _escaped_or_has_newline(self, line):
  152:         match = re.search(r'(\\+)n?$', line)
  153          return match and len(match.group(1)) % 2 == 1

VCMGUIAUTO_FF\venv\Lib\site-packages\selenium\webdriver\firefox\firefox_profile.py:
  236                  for usr in f:
  237:                     matches = re.search(PREF_RE, usr)
  238                      try:

VCMGUIAUTO_FF\venv\Lib\site-packages\selenium\webdriver\support\expected_conditions.py:
  88          import re
  89:         match = re.search(self.pattern, driver.current_url)
  90  

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\package_index.py:
  843                  # Check for a subversion index page
  844:                 if re.search(r'<title>([^- ]+ - )?Revision \d+:', line):
  845                      # it's a subversion index page:

VCMGUIAUTO_FF\venv\Lib\site-packages\setuptools\command\easy_install.py:
  2128          """
  2129:         has_path_sep = re.search(r'[\\/]', name)
  2130          if has_path_sep:

VCMGUIAUTO_FF\venv\Lib\site-packages\urllib3\connection.py:
  191          """Send a request to the server"""
  192:         match = _CONTAINS_CONTROL_CHAR_RE.search(method)
  193          if match:

VCMGUIAUTO_FF\venv\Lib\site-packages\urllib3\util\url.py:
  281              if is_ipv6:
  282:                 match = ZONE_ID_RE.search(host)
  283                  if match:

  356      source_url = url
  357:     if not SCHEME_RE.search(url):
  358          url = "//" + url
