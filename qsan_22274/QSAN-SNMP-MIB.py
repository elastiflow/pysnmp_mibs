# SNMP MIB module (QSAN-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/qsan_22274/QSAN-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:29 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Qsan_ObjectIdentity = ObjectIdentity
qsan = _Qsan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274)
)
_Raid_ObjectIdentity = ObjectIdentity
raid = _Raid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1)
)
_System_config_ObjectIdentity = ObjectIdentity
system_config = _System_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1)
)
_System_config_status_ObjectIdentity = ObjectIdentity
system_config_status = _System_config_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 1)
)
_Sys_status_raid_Type = DisplayString
_Sys_status_raid_Object = MibScalar
sys_status_raid = _Sys_status_raid_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 1, 1),
    _Sys_status_raid_Type()
)
sys_status_raid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_status_raid.setStatus("mandatory")
_Sys_status_temp_Type = DisplayString
_Sys_status_temp_Object = MibScalar
sys_status_temp = _Sys_status_temp_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 1, 2),
    _Sys_status_temp_Type()
)
sys_status_temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_status_temp.setStatus("mandatory")
_Sys_status_volt_Type = DisplayString
_Sys_status_volt_Object = MibScalar
sys_status_volt = _Sys_status_volt_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 1, 3),
    _Sys_status_volt_Type()
)
sys_status_volt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_status_volt.setStatus("mandatory")
_Sys_status_ups_Type = DisplayString
_Sys_status_ups_Object = MibScalar
sys_status_ups = _Sys_status_ups_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 1, 4),
    _Sys_status_ups_Type()
)
sys_status_ups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_status_ups.setStatus("mandatory")
_Sys_status_fan_Type = DisplayString
_Sys_status_fan_Object = MibScalar
sys_status_fan = _Sys_status_fan_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 1, 5),
    _Sys_status_fan_Type()
)
sys_status_fan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_status_fan.setStatus("mandatory")
_Sys_status_psu_Type = DisplayString
_Sys_status_psu_Object = MibScalar
sys_status_psu = _Sys_status_psu_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 1, 6),
    _Sys_status_psu_Type()
)
sys_status_psu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_status_psu.setStatus("mandatory")
_Sys_status_dual_Type = DisplayString
_Sys_status_dual_Object = MibScalar
sys_status_dual = _Sys_status_dual_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 1, 7),
    _Sys_status_dual_Type()
)
sys_status_dual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_status_dual.setStatus("mandatory")
_System_config_setting_ObjectIdentity = ObjectIdentity
system_config_setting = _System_config_setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 4)
)
_Sys_name_Type = DisplayString
_Sys_name_Object = MibScalar
sys_name = _Sys_name_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 4, 1),
    _Sys_name_Type()
)
sys_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_name.setStatus("mandatory")
_Sys_current_time_Type = DisplayString
_Sys_current_time_Object = MibScalar
sys_current_time = _Sys_current_time_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 4, 2),
    _Sys_current_time_Type()
)
sys_current_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_current_time.setStatus("mandatory")
_Sys_ntp_server_Type = DisplayString
_Sys_ntp_server_Object = MibScalar
sys_ntp_server = _Sys_ntp_server_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 4, 3),
    _Sys_ntp_server_Type()
)
sys_ntp_server.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_ntp_server.setStatus("mandatory")
_System_config_ip_ObjectIdentity = ObjectIdentity
system_config_ip = _System_config_ip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5)
)
_Sys_mac_Type = DisplayString
_Sys_mac_Object = MibScalar
sys_mac = _Sys_mac_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5, 1),
    _Sys_mac_Type()
)
sys_mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mac.setStatus("mandatory")
_Sys_ip_Type = DisplayString
_Sys_ip_Object = MibScalar
sys_ip = _Sys_ip_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5, 2),
    _Sys_ip_Type()
)
sys_ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_ip.setStatus("mandatory")
_Sys_mask_Type = DisplayString
_Sys_mask_Object = MibScalar
sys_mask = _Sys_mask_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5, 3),
    _Sys_mask_Type()
)
sys_mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mask.setStatus("mandatory")
_Sys_gateway_Type = DisplayString
_Sys_gateway_Object = MibScalar
sys_gateway = _Sys_gateway_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5, 4),
    _Sys_gateway_Type()
)
sys_gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_gateway.setStatus("mandatory")
_Sys_dns_Type = DisplayString
_Sys_dns_Object = MibScalar
sys_dns = _Sys_dns_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5, 5),
    _Sys_dns_Type()
)
sys_dns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_dns.setStatus("mandatory")
_Sys_http_port_Type = DisplayString
_Sys_http_port_Object = MibScalar
sys_http_port = _Sys_http_port_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5, 6),
    _Sys_http_port_Type()
)
sys_http_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_http_port.setStatus("mandatory")
_Sys_https_port_Type = DisplayString
_Sys_https_port_Object = MibScalar
sys_https_port = _Sys_https_port_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5, 7),
    _Sys_https_port_Type()
)
sys_https_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_https_port.setStatus("mandatory")
_Sys_ssh_port_Type = DisplayString
_Sys_ssh_port_Object = MibScalar
sys_ssh_port = _Sys_ssh_port_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 5, 8),
    _Sys_ssh_port_Type()
)
sys_ssh_port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_ssh_port.setStatus("mandatory")
_System_config_mail_ObjectIdentity = ObjectIdentity
system_config_mail = _System_config_mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6)
)
_Sys_mailfrom_Type = DisplayString
_Sys_mailfrom_Object = MibScalar
sys_mailfrom = _Sys_mailfrom_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6, 1),
    _Sys_mailfrom_Type()
)
sys_mailfrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mailfrom.setStatus("mandatory")
_Sys_mailto1_Type = DisplayString
_Sys_mailto1_Object = MibScalar
sys_mailto1 = _Sys_mailto1_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6, 2),
    _Sys_mailto1_Type()
)
sys_mailto1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mailto1.setStatus("mandatory")
_Sys_mailto1_filter_Type = DisplayString
_Sys_mailto1_filter_Object = MibScalar
sys_mailto1_filter = _Sys_mailto1_filter_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6, 3),
    _Sys_mailto1_filter_Type()
)
sys_mailto1_filter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mailto1_filter.setStatus("mandatory")
_Sys_mailto2_Type = DisplayString
_Sys_mailto2_Object = MibScalar
sys_mailto2 = _Sys_mailto2_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6, 4),
    _Sys_mailto2_Type()
)
sys_mailto2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mailto2.setStatus("mandatory")
_Sys_mailto2_filter_Type = DisplayString
_Sys_mailto2_filter_Object = MibScalar
sys_mailto2_filter = _Sys_mailto2_filter_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6, 5),
    _Sys_mailto2_filter_Type()
)
sys_mailto2_filter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mailto2_filter.setStatus("mandatory")
_Sys_mailto3_Type = DisplayString
_Sys_mailto3_Object = MibScalar
sys_mailto3 = _Sys_mailto3_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6, 6),
    _Sys_mailto3_Type()
)
sys_mailto3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mailto3.setStatus("mandatory")
_Sys_mailto3_filter_Type = DisplayString
_Sys_mailto3_filter_Object = MibScalar
sys_mailto3_filter = _Sys_mailto3_filter_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6, 7),
    _Sys_mailto3_filter_Type()
)
sys_mailto3_filter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_mailto3_filter.setStatus("mandatory")
_Sys_smpt_relay_Type = DisplayString
_Sys_smpt_relay_Object = MibScalar
sys_smpt_relay = _Sys_smpt_relay_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 1, 6, 8),
    _Sys_smpt_relay_Type()
)
sys_smpt_relay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sys_smpt_relay.setStatus("mandatory")
_Volume_config_ObjectIdentity = ObjectIdentity
volume_config = _Volume_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2)
)
_Physical_disk_Object = MibTable
physical_disk = _Physical_disk_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1)
)
if mibBuilder.loadTexts:
    physical_disk.setStatus("mandatory")
_Physical_disk_item_Object = MibTableRow
physical_disk_item = _Physical_disk_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1)
)
physical_disk_item.setIndexNames(
    (0, "QSAN-SNMP-MIB", "pd-location"),
)
if mibBuilder.loadTexts:
    physical_disk_item.setStatus("mandatory")
_Pd_location_Type = DisplayString
_Pd_location_Object = MibTableColumn
pd_location = _Pd_location_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 1),
    _Pd_location_Type()
)
pd_location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_location.setStatus("mandatory")
_Pd_idx_Type = DisplayString
_Pd_idx_Object = MibTableColumn
pd_idx = _Pd_idx_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 2),
    _Pd_idx_Type()
)
pd_idx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_idx.setStatus("mandatory")
_Pd_size_Type = DisplayString
_Pd_size_Object = MibTableColumn
pd_size = _Pd_size_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 3),
    _Pd_size_Type()
)
pd_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_size.setStatus("mandatory")
_Pd_RG_Type = DisplayString
_Pd_RG_Object = MibTableColumn
pd_RG = _Pd_RG_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 4),
    _Pd_RG_Type()
)
pd_RG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_RG.setStatus("mandatory")
_Pd_status_Type = DisplayString
_Pd_status_Object = MibTableColumn
pd_status = _Pd_status_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 5),
    _Pd_status_Type()
)
pd_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_status.setStatus("mandatory")
_Pd_status_health_Type = DisplayString
_Pd_status_health_Object = MibTableColumn
pd_status_health = _Pd_status_health_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 6),
    _Pd_status_health_Type()
)
pd_status_health.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_status_health.setStatus("mandatory")
_Pd_status_usage_Type = DisplayString
_Pd_status_usage_Object = MibTableColumn
pd_status_usage = _Pd_status_usage_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 7),
    _Pd_status_usage_Type()
)
pd_status_usage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_status_usage.setStatus("mandatory")
_Pd_vendor_Type = DisplayString
_Pd_vendor_Object = MibTableColumn
pd_vendor = _Pd_vendor_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 8),
    _Pd_vendor_Type()
)
pd_vendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_vendor.setStatus("mandatory")
_Pd_serial_Type = DisplayString
_Pd_serial_Object = MibTableColumn
pd_serial = _Pd_serial_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 9),
    _Pd_serial_Type()
)
pd_serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_serial.setStatus("mandatory")
_Pd_type_Type = DisplayString
_Pd_type_Object = MibTableColumn
pd_type = _Pd_type_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 10),
    _Pd_type_Type()
)
pd_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_type.setStatus("mandatory")
_Pd_write_cache_Type = DisplayString
_Pd_write_cache_Object = MibTableColumn
pd_write_cache = _Pd_write_cache_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 11),
    _Pd_write_cache_Type()
)
pd_write_cache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_write_cache.setStatus("mandatory")
_Pd_standby_Type = DisplayString
_Pd_standby_Object = MibTableColumn
pd_standby = _Pd_standby_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 12),
    _Pd_standby_Type()
)
pd_standby.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_standby.setStatus("mandatory")
_Pd_readahead_Type = DisplayString
_Pd_readahead_Object = MibTableColumn
pd_readahead = _Pd_readahead_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 13),
    _Pd_readahead_Type()
)
pd_readahead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_readahead.setStatus("mandatory")
_Pd_command_queuing_Type = DisplayString
_Pd_command_queuing_Object = MibTableColumn
pd_command_queuing = _Pd_command_queuing_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 14),
    _Pd_command_queuing_Type()
)
pd_command_queuing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_command_queuing.setStatus("mandatory")
_Pd_product_Type = DisplayString
_Pd_product_Object = MibTableColumn
pd_product = _Pd_product_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 15),
    _Pd_product_Type()
)
pd_product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_product.setStatus("mandatory")
_Pd_revision_Type = DisplayString
_Pd_revision_Object = MibTableColumn
pd_revision = _Pd_revision_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 1, 1, 16),
    _Pd_revision_Type()
)
pd_revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pd_revision.setStatus("mandatory")
_Raid_group_Object = MibTable
raid_group = _Raid_group_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2)
)
if mibBuilder.loadTexts:
    raid_group.setStatus("mandatory")
_Raid_group_item_Object = MibTableRow
raid_group_item = _Raid_group_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1)
)
raid_group_item.setIndexNames(
    (0, "QSAN-SNMP-MIB", "rg-name"),
)
if mibBuilder.loadTexts:
    raid_group_item.setStatus("mandatory")
_Rg_name_Type = DisplayString
_Rg_name_Object = MibTableColumn
rg_name = _Rg_name_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 1),
    _Rg_name_Type()
)
rg_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_name.setStatus("mandatory")
_Rg_total_Type = DisplayString
_Rg_total_Object = MibTableColumn
rg_total = _Rg_total_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 2),
    _Rg_total_Type()
)
rg_total.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_total.setStatus("mandatory")
_Rg_free_Type = DisplayString
_Rg_free_Object = MibTableColumn
rg_free = _Rg_free_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 3),
    _Rg_free_Type()
)
rg_free.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_free.setStatus("mandatory")
_Rg_pd_Type = DisplayString
_Rg_pd_Object = MibTableColumn
rg_pd = _Rg_pd_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 4),
    _Rg_pd_Type()
)
rg_pd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_pd.setStatus("mandatory")
_Rg_vd_Type = DisplayString
_Rg_vd_Object = MibTableColumn
rg_vd = _Rg_vd_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 5),
    _Rg_vd_Type()
)
rg_vd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_vd.setStatus("mandatory")
_Rg_status_Type = DisplayString
_Rg_status_Object = MibTableColumn
rg_status = _Rg_status_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 6),
    _Rg_status_Type()
)
rg_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_status.setStatus("mandatory")
_Rg_health_Type = DisplayString
_Rg_health_Object = MibTableColumn
rg_health = _Rg_health_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 7),
    _Rg_health_Type()
)
rg_health.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_health.setStatus("mandatory")
_Rg_raid_Type = DisplayString
_Rg_raid_Object = MibTableColumn
rg_raid = _Rg_raid_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 8),
    _Rg_raid_Type()
)
rg_raid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_raid.setStatus("mandatory")
_Rg_owner_Type = DisplayString
_Rg_owner_Object = MibTableColumn
rg_owner = _Rg_owner_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 9),
    _Rg_owner_Type()
)
rg_owner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_owner.setStatus("mandatory")
_Rg_powner_Type = DisplayString
_Rg_powner_Object = MibTableColumn
rg_powner = _Rg_powner_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 2, 1, 10),
    _Rg_powner_Type()
)
rg_powner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rg_powner.setStatus("mandatory")
_Virtual_disk_Object = MibTable
virtual_disk = _Virtual_disk_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3)
)
if mibBuilder.loadTexts:
    virtual_disk.setStatus("mandatory")
_Virtual_disk_item_Object = MibTableRow
virtual_disk_item = _Virtual_disk_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1)
)
virtual_disk_item.setIndexNames(
    (0, "QSAN-SNMP-MIB", "vd-name"),
)
if mibBuilder.loadTexts:
    virtual_disk_item.setStatus("mandatory")
_Vd_name_Type = DisplayString
_Vd_name_Object = MibTableColumn
vd_name = _Vd_name_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 1),
    _Vd_name_Type()
)
vd_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_name.setStatus("mandatory")
_Vd_size_Type = DisplayString
_Vd_size_Object = MibTableColumn
vd_size = _Vd_size_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 2),
    _Vd_size_Type()
)
vd_size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_size.setStatus("mandatory")
_Vd_right_Type = DisplayString
_Vd_right_Object = MibTableColumn
vd_right = _Vd_right_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 3),
    _Vd_right_Type()
)
vd_right.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_right.setStatus("mandatory")
_Vd_priority_Type = DisplayString
_Vd_priority_Object = MibTableColumn
vd_priority = _Vd_priority_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 4),
    _Vd_priority_Type()
)
vd_priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_priority.setStatus("mandatory")
_Vd_bgrate_Type = DisplayString
_Vd_bgrate_Object = MibTableColumn
vd_bgrate = _Vd_bgrate_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 5),
    _Vd_bgrate_Type()
)
vd_bgrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_bgrate.setStatus("mandatory")
_Vd_status_Type = DisplayString
_Vd_status_Object = MibTableColumn
vd_status = _Vd_status_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 6),
    _Vd_status_Type()
)
vd_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_status.setStatus("mandatory")
_Vd_health_Type = DisplayString
_Vd_health_Object = MibTableColumn
vd_health = _Vd_health_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 7),
    _Vd_health_Type()
)
vd_health.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_health.setStatus("mandatory")
_Vd_progress_Type = DisplayString
_Vd_progress_Object = MibTableColumn
vd_progress = _Vd_progress_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 8),
    _Vd_progress_Type()
)
vd_progress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_progress.setStatus("mandatory")
_Vd_raid_Type = DisplayString
_Vd_raid_Object = MibTableColumn
vd_raid = _Vd_raid_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 9),
    _Vd_raid_Type()
)
vd_raid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_raid.setStatus("mandatory")
_Vd_lun_Type = DisplayString
_Vd_lun_Object = MibTableColumn
vd_lun = _Vd_lun_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 10),
    _Vd_lun_Type()
)
vd_lun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_lun.setStatus("mandatory")
_Vd_snapshot_space_Type = DisplayString
_Vd_snapshot_space_Object = MibTableColumn
vd_snapshot_space = _Vd_snapshot_space_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 11),
    _Vd_snapshot_space_Type()
)
vd_snapshot_space.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_snapshot_space.setStatus("mandatory")
_Vd_snapshot_Type = DisplayString
_Vd_snapshot_Object = MibTableColumn
vd_snapshot = _Vd_snapshot_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 12),
    _Vd_snapshot_Type()
)
vd_snapshot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_snapshot.setStatus("mandatory")
_Vd_rg_Type = DisplayString
_Vd_rg_Object = MibTableColumn
vd_rg = _Vd_rg_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 3, 1, 13),
    _Vd_rg_Type()
)
vd_rg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vd_rg.setStatus("mandatory")
_Logical_unit_Object = MibTable
logical_unit = _Logical_unit_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 4)
)
if mibBuilder.loadTexts:
    logical_unit.setStatus("mandatory")
_Logical_unit_item_Object = MibTableRow
logical_unit_item = _Logical_unit_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 4, 1)
)
logical_unit_item.setIndexNames(
    (0, "QSAN-SNMP-MIB", "lun-index"),
)
if mibBuilder.loadTexts:
    logical_unit_item.setStatus("mandatory")
_Lun_index_Type = DisplayString
_Lun_index_Object = MibTableColumn
lun_index = _Lun_index_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 4, 1, 1),
    _Lun_index_Type()
)
lun_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun_index.setStatus("mandatory")
_Lun_host_Type = DisplayString
_Lun_host_Object = MibTableColumn
lun_host = _Lun_host_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 4, 1, 2),
    _Lun_host_Type()
)
lun_host.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun_host.setStatus("mandatory")
_Lun_target_Type = DisplayString
_Lun_target_Object = MibTableColumn
lun_target = _Lun_target_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 4, 1, 3),
    _Lun_target_Type()
)
lun_target.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun_target.setStatus("mandatory")
_Lun_num_Type = DisplayString
_Lun_num_Object = MibTableColumn
lun_num = _Lun_num_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 4, 1, 4),
    _Lun_num_Type()
)
lun_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun_num.setStatus("mandatory")
_Lun_permission_Type = DisplayString
_Lun_permission_Object = MibTableColumn
lun_permission = _Lun_permission_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 4, 1, 5),
    _Lun_permission_Type()
)
lun_permission.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun_permission.setStatus("mandatory")
_Lun_vd_Type = DisplayString
_Lun_vd_Object = MibTableColumn
lun_vd = _Lun_vd_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 2, 4, 1, 6),
    _Lun_vd_Type()
)
lun_vd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lun_vd.setStatus("mandatory")
_Enclosure_management_ObjectIdentity = ObjectIdentity
enclosure_management = _Enclosure_management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3)
)
_Hardware_monitor_Object = MibTable
hardware_monitor = _Hardware_monitor_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hardware_monitor.setStatus("mandatory")
_Hardware_monitor_item_Object = MibTableRow
hardware_monitor_item = _Hardware_monitor_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 2, 1)
)
hardware_monitor_item.setIndexNames(
    (0, "QSAN-SNMP-MIB", "ems-item"),
)
if mibBuilder.loadTexts:
    hardware_monitor_item.setStatus("mandatory")
_Ems_loc_Type = DisplayString
_Ems_loc_Object = MibTableColumn
ems_loc = _Ems_loc_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 2, 1, 1),
    _Ems_loc_Type()
)
ems_loc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ems_loc.setStatus("mandatory")
_Ems_type_Type = DisplayString
_Ems_type_Object = MibTableColumn
ems_type = _Ems_type_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 2, 1, 2),
    _Ems_type_Type()
)
ems_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ems_type.setStatus("mandatory")
_Ems_item_Type = DisplayString
_Ems_item_Object = MibTableColumn
ems_item = _Ems_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 2, 1, 3),
    _Ems_item_Type()
)
ems_item.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ems_item.setStatus("mandatory")
_Ems_value_Type = DisplayString
_Ems_value_Object = MibTableColumn
ems_value = _Ems_value_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 2, 1, 4),
    _Ems_value_Type()
)
ems_value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ems_value.setStatus("mandatory")
_Ems_status_Type = DisplayString
_Ems_status_Object = MibTableColumn
ems_status = _Ems_status_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 2, 1, 5),
    _Ems_status_Type()
)
ems_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ems_status.setStatus("mandatory")
_Enclosure_management_ses_ObjectIdentity = ObjectIdentity
enclosure_management_ses = _Enclosure_management_ses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 3)
)
_Ems_ses_Type = DisplayString
_Ems_ses_Object = MibScalar
ems_ses = _Ems_ses_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 3, 1),
    _Ems_ses_Type()
)
ems_ses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ems_ses.setStatus("mandatory")
_Hdd_smart_Object = MibTable
hdd_smart = _Hdd_smart_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hdd_smart.setStatus("mandatory")
_Hdd_smart_item_Object = MibTableRow
hdd_smart_item = _Hdd_smart_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 4, 1)
)
hdd_smart_item.setIndexNames(
    (0, "QSAN-SNMP-MIB", "hdd-loc"),
)
if mibBuilder.loadTexts:
    hdd_smart_item.setStatus("mandatory")
_Hdd_loc_Type = DisplayString
_Hdd_loc_Object = MibTableColumn
hdd_loc = _Hdd_loc_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 4, 1, 1),
    _Hdd_loc_Type()
)
hdd_loc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdd_loc.setStatus("mandatory")
_Hdd_type_Type = DisplayString
_Hdd_type_Object = MibTableColumn
hdd_type = _Hdd_type_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 4, 1, 2),
    _Hdd_type_Type()
)
hdd_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdd_type.setStatus("mandatory")
_Hdd_readerror_Type = DisplayString
_Hdd_readerror_Object = MibTableColumn
hdd_readerror = _Hdd_readerror_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 4, 1, 3),
    _Hdd_readerror_Type()
)
hdd_readerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdd_readerror.setStatus("mandatory")
_Hdd_temperature_Type = DisplayString
_Hdd_temperature_Object = MibTableColumn
hdd_temperature = _Hdd_temperature_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 3, 4, 1, 4),
    _Hdd_temperature_Type()
)
hdd_temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdd_temperature.setStatus("mandatory")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4)
)
_Maintenance_info_ObjectIdentity = ObjectIdentity
maintenance_info = _Maintenance_info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4, 1)
)
_Maintenance_info_cpu_Type = DisplayString
_Maintenance_info_cpu_Object = MibScalar
maintenance_info_cpu = _Maintenance_info_cpu_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4, 1, 1),
    _Maintenance_info_cpu_Type()
)
maintenance_info_cpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenance_info_cpu.setStatus("mandatory")
_Maintenance_info_mem_Type = DisplayString
_Maintenance_info_mem_Object = MibScalar
maintenance_info_mem = _Maintenance_info_mem_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4, 1, 2),
    _Maintenance_info_mem_Type()
)
maintenance_info_mem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenance_info_mem.setStatus("mandatory")
_Maintenance_info_fw_Type = DisplayString
_Maintenance_info_fw_Object = MibScalar
maintenance_info_fw = _Maintenance_info_fw_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4, 1, 3),
    _Maintenance_info_fw_Type()
)
maintenance_info_fw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenance_info_fw.setStatus("mandatory")
_Maintenance_info_serial_no_Type = DisplayString
_Maintenance_info_serial_no_Object = MibScalar
maintenance_info_serial_no = _Maintenance_info_serial_no_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4, 1, 4),
    _Maintenance_info_serial_no_Type()
)
maintenance_info_serial_no.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenance_info_serial_no.setStatus("mandatory")
_Maintenance_info_backplane_id_Type = DisplayString
_Maintenance_info_backplane_id_Object = MibScalar
maintenance_info_backplane_id = _Maintenance_info_backplane_id_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4, 1, 5),
    _Maintenance_info_backplane_id_Type()
)
maintenance_info_backplane_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenance_info_backplane_id.setStatus("mandatory")
_Maintenance_info_status_Type = DisplayString
_Maintenance_info_status_Object = MibScalar
maintenance_info_status = _Maintenance_info_status_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4, 1, 6),
    _Maintenance_info_status_Type()
)
maintenance_info_status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenance_info_status.setStatus("mandatory")
_Maintenance_info_message_Type = DisplayString
_Maintenance_info_message_Object = MibScalar
maintenance_info_message = _Maintenance_info_message_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 4, 1, 7),
    _Maintenance_info_message_Type()
)
maintenance_info_message.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintenance_info_message.setStatus("mandatory")
_Iscsi_config_ObjectIdentity = ObjectIdentity
iscsi_config = _Iscsi_config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5)
)
_Iscsi_config_nic_Object = MibTable
iscsi_config_nic = _Iscsi_config_nic_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1)
)
if mibBuilder.loadTexts:
    iscsi_config_nic.setStatus("mandatory")
_Iscsi_nic_item_Object = MibTableRow
iscsi_nic_item = _Iscsi_nic_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1, 1)
)
iscsi_nic_item.setIndexNames(
    (0, "QSAN-SNMP-MIB", "iscsi-nic-id"),
)
if mibBuilder.loadTexts:
    iscsi_nic_item.setStatus("mandatory")
_Iscsi_nic_id_Type = DisplayString
_Iscsi_nic_id_Object = MibTableColumn
iscsi_nic_id = _Iscsi_nic_id_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1, 1, 1),
    _Iscsi_nic_id_Type()
)
iscsi_nic_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_nic_id.setStatus("mandatory")
_Iscsi_nic_ctrl_Type = DisplayString
_Iscsi_nic_ctrl_Object = MibTableColumn
iscsi_nic_ctrl = _Iscsi_nic_ctrl_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1, 1, 2),
    _Iscsi_nic_ctrl_Type()
)
iscsi_nic_ctrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_nic_ctrl.setStatus("mandatory")
_Iscsi_nic_ip_Type = DisplayString
_Iscsi_nic_ip_Object = MibTableColumn
iscsi_nic_ip = _Iscsi_nic_ip_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1, 1, 3),
    _Iscsi_nic_ip_Type()
)
iscsi_nic_ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_nic_ip.setStatus("mandatory")
_Iscsi_nic_mask_Type = DisplayString
_Iscsi_nic_mask_Object = MibTableColumn
iscsi_nic_mask = _Iscsi_nic_mask_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1, 1, 4),
    _Iscsi_nic_mask_Type()
)
iscsi_nic_mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_nic_mask.setStatus("mandatory")
_Iscsi_nic_gw_Type = DisplayString
_Iscsi_nic_gw_Object = MibTableColumn
iscsi_nic_gw = _Iscsi_nic_gw_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1, 1, 5),
    _Iscsi_nic_gw_Type()
)
iscsi_nic_gw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_nic_gw.setStatus("mandatory")
_Iscsi_nic_jumbo_Type = DisplayString
_Iscsi_nic_jumbo_Object = MibTableColumn
iscsi_nic_jumbo = _Iscsi_nic_jumbo_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1, 1, 6),
    _Iscsi_nic_jumbo_Type()
)
iscsi_nic_jumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_nic_jumbo.setStatus("mandatory")
_Iscsi_nic_mac_Type = DisplayString
_Iscsi_nic_mac_Object = MibTableColumn
iscsi_nic_mac = _Iscsi_nic_mac_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 1, 1, 7),
    _Iscsi_nic_mac_Type()
)
iscsi_nic_mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_nic_mac.setStatus("mandatory")
_Iscsi_config_entity_ObjectIdentity = ObjectIdentity
iscsi_config_entity = _Iscsi_config_entity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 2)
)
_Iscsi_config_entity_item_Type = DisplayString
_Iscsi_config_entity_item_Object = MibScalar
iscsi_config_entity_item = _Iscsi_config_entity_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 2, 1),
    _Iscsi_config_entity_item_Type()
)
iscsi_config_entity_item.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_config_entity_item.setStatus("mandatory")
_Iscsi_config_isns_item_Type = DisplayString
_Iscsi_config_isns_item_Object = MibScalar
iscsi_config_isns_item = _Iscsi_config_isns_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 2, 2),
    _Iscsi_config_isns_item_Type()
)
iscsi_config_isns_item.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_config_isns_item.setStatus("mandatory")
_Iscsi_config_node_Object = MibTable
iscsi_config_node = _Iscsi_config_node_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 3)
)
if mibBuilder.loadTexts:
    iscsi_config_node.setStatus("mandatory")
_Iscsi_node_item_Object = MibTableRow
iscsi_node_item = _Iscsi_node_item_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 3, 1)
)
iscsi_node_item.setIndexNames(
    (0, "QSAN-SNMP-MIB", "iscsi-node-id"),
)
if mibBuilder.loadTexts:
    iscsi_node_item.setStatus("mandatory")
_Iscsi_node_id_Type = DisplayString
_Iscsi_node_id_Object = MibTableColumn
iscsi_node_id = _Iscsi_node_id_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 3, 1, 1),
    _Iscsi_node_id_Type()
)
iscsi_node_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_node_id.setStatus("mandatory")
_Iscsi_node_ctrl_Type = DisplayString
_Iscsi_node_ctrl_Object = MibTableColumn
iscsi_node_ctrl = _Iscsi_node_ctrl_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 3, 1, 2),
    _Iscsi_node_ctrl_Type()
)
iscsi_node_ctrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_node_ctrl.setStatus("mandatory")
_Iscsi_node_auth_Type = DisplayString
_Iscsi_node_auth_Object = MibTableColumn
iscsi_node_auth = _Iscsi_node_auth_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 3, 1, 3),
    _Iscsi_node_auth_Type()
)
iscsi_node_auth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_node_auth.setStatus("mandatory")
_Iscsi_node_name_Type = DisplayString
_Iscsi_node_name_Object = MibTableColumn
iscsi_node_name = _Iscsi_node_name_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 3, 1, 4),
    _Iscsi_node_name_Type()
)
iscsi_node_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_node_name.setStatus("mandatory")
_Iscsi_node_portal_Type = DisplayString
_Iscsi_node_portal_Object = MibTableColumn
iscsi_node_portal = _Iscsi_node_portal_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 5, 3, 1, 5),
    _Iscsi_node_portal_Type()
)
iscsi_node_portal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsi_node_portal.setStatus("mandatory")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000)
)
_EventString_Type = DisplayString
_EventString_Object = MibScalar
eventString = _EventString_Object(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8001),
    _EventString_Type()
)
eventString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

evtid_test = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 0)
)
evtid_test.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_test.setStatus(
        ""
    )

evtid_ecc_single = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 1)
)
evtid_ecc_single.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_ecc_single.setStatus(
        ""
    )

evtid_ecc_multiple = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 2)
)
evtid_ecc_multiple.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_ecc_multiple.setStatus(
        ""
    )

evtid_ecc_dimm = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 3)
)
evtid_ecc_dimm.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_ecc_dimm.setStatus(
        ""
    )

evtid_ecc_none = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 4)
)
evtid_ecc_none.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_ecc_none.setStatus(
        ""
    )

evtid_bbm_start_syncing = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 5)
)
evtid_bbm_start_syncing.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_start_syncing.setStatus(
        ""
    )

evtid_bbm_stop_syncing = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 6)
)
evtid_bbm_stop_syncing.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_stop_syncing.setStatus(
        ""
    )

evtid_bbm_installed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 7)
)
evtid_bbm_installed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_installed.setStatus(
        ""
    )

evtid_bbm_sts_good = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 8)
)
evtid_bbm_sts_good.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_sts_good.setStatus(
        ""
    )

evtid_bbm_sts_charging = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 9)
)
evtid_bbm_sts_charging.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_sts_charging.setStatus(
        ""
    )

evtid_bbm_sts_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 10)
)
evtid_bbm_sts_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_sts_fail.setStatus(
        ""
    )

evtid_bbm_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 11)
)
evtid_bbm_enabled.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_enabled.setStatus(
        ""
    )

evtid_bbm_inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 12)
)
evtid_bbm_inserted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_inserted.setStatus(
        ""
    )

evtid_bbm_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 13)
)
evtid_bbm_removed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_removed.setStatus(
        ""
    )

evtid_bbm_warning_temperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 14)
)
evtid_bbm_warning_temperature.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_bbm_warning_temperature.setStatus(
        ""
    )

evtid_qcopy_job_info = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 15)
)
evtid_qcopy_job_info.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_qcopy_job_info.setStatus(
        ""
    )

evtid_qcopy_job_restart = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 16)
)
evtid_qcopy_job_restart.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_qcopy_job_restart.setStatus(
        ""
    )

evtid_qcopy_job_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 17)
)
evtid_qcopy_job_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_qcopy_job_fail.setStatus(
        ""
    )

evtid_qcopy_job_abort = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 18)
)
evtid_qcopy_job_abort.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_qcopy_job_abort.setStatus(
        ""
    )

evtid_qcopy_job_abort_lba_size = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 19)
)
evtid_qcopy_job_abort_lba_size.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_qcopy_job_abort_lba_size.setStatus(
        ""
    )

evtid_scsi_busreset = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 20)
)
evtid_scsi_busreset.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_scsi_busreset.setStatus(
        ""
    )

evtid_scsi_host_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 21)
)
evtid_scsi_host_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_scsi_host_error.setStatus(
        ""
    )

evtid_sas_port_reply_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 22)
)
evtid_sas_port_reply_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sas_port_reply_error.setStatus(
        ""
    )

evtid_sas_unknown_port_reply_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 23)
)
evtid_sas_unknown_port_reply_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sas_unknown_port_reply_error.setStatus(
        ""
    )

evtid_fc_port_reply_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 24)
)
evtid_fc_port_reply_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_fc_port_reply_error.setStatus(
        ""
    )

evtid_fc_unknown_port_reply_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 25)
)
evtid_fc_unknown_port_reply_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_fc_unknown_port_reply_error.setStatus(
        ""
    )

evtid_fc_port_linkup = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 26)
)
evtid_fc_port_linkup.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_fc_port_linkup.setStatus(
        ""
    )

evtid_fc_port_linkdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 27)
)
evtid_fc_port_linkdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_fc_port_linkdown.setStatus(
        ""
    )

evtid_iscsi_login_accepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 28)
)
evtid_iscsi_login_accepted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_iscsi_login_accepted.setStatus(
        ""
    )

evtid_iscsi_login_rejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 29)
)
evtid_iscsi_login_rejected.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_iscsi_login_rejected.setStatus(
        ""
    )

evtid_iscsi_logout_recvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 30)
)
evtid_iscsi_logout_recvd.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_iscsi_logout_recvd.setStatus(
        ""
    )

evtid_sata_enable_dev_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 31)
)
evtid_sata_enable_dev_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_enable_dev_fail.setStatus(
        ""
    )

evtid_sata_edma_mem_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 32)
)
evtid_sata_edma_mem_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_edma_mem_fail.setStatus(
        ""
    )

evtid_sata_remap_mem_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 33)
)
evtid_sata_remap_mem_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_remap_mem_fail.setStatus(
        ""
    )

evtid_sata_prd_mem_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 34)
)
evtid_sata_prd_mem_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_prd_mem_fail.setStatus(
        ""
    )

evtid_sata_revision_id_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 35)
)
evtid_sata_revision_id_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_revision_id_fail.setStatus(
        ""
    )

evtid_sata_set_reg_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 36)
)
evtid_sata_set_reg_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_set_reg_fail.setStatus(
        ""
    )

evtid_sata_init_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 37)
)
evtid_sata_init_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_init_fail.setStatus(
        ""
    )

evtid_sata_diag_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 38)
)
evtid_sata_diag_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_diag_fail.setStatus(
        ""
    )

evtid_mode_id_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 39)
)
evtid_mode_id_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_mode_id_fail.setStatus(
        ""
    )

evtid_sata_chip_count_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 40)
)
evtid_sata_chip_count_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sata_chip_count_error.setStatus(
        ""
    )

evtid_disk_upgrade_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 41)
)
evtid_disk_upgrade_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_disk_upgrade_started.setStatus(
        ""
    )

evtid_disk_upgrade_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 42)
)
evtid_disk_upgrade_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_disk_upgrade_finished.setStatus(
        ""
    )

evtid_disk_upgrade_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 43)
)
evtid_disk_upgrade_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_disk_upgrade_failed.setStatus(
        ""
    )

evtid_jbod_disk_upgrade_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 44)
)
evtid_jbod_disk_upgrade_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_disk_upgrade_started.setStatus(
        ""
    )

evtid_jbod_disk_upgrade_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 45)
)
evtid_jbod_disk_upgrade_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_disk_upgrade_finished.setStatus(
        ""
    )

evtid_jbod_disk_upgrade_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 46)
)
evtid_jbod_disk_upgrade_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_disk_upgrade_failed.setStatus(
        ""
    )

evtid_pd_inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 47)
)
evtid_pd_inserted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_pd_inserted.setStatus(
        ""
    )

evtid_pd_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 48)
)
evtid_pd_removed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_pd_removed.setStatus(
        ""
    )

evtid_hdd_readerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 49)
)
evtid_hdd_readerr.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hdd_readerr.setStatus(
        ""
    )

evtid_hdd_writeerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 50)
)
evtid_hdd_writeerr.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hdd_writeerr.setStatus(
        ""
    )

evtid_hdd_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 51)
)
evtid_hdd_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hdd_error.setStatus(
        ""
    )

evtid_hdd_io_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 52)
)
evtid_hdd_io_timeout.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hdd_io_timeout.setStatus(
        ""
    )

evtid_hdd_temp_warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 53)
)
evtid_hdd_temp_warning.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hdd_temp_warning.setStatus(
        ""
    )

evtid_env_power_install = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 54)
)
evtid_env_power_install.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_power_install.setStatus(
        ""
    )

evtid_env_power_absent = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 55)
)
evtid_env_power_absent.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_power_absent.setStatus(
        ""
    )

evtid_env_power_rst = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 56)
)
evtid_env_power_rst.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_power_rst.setStatus(
        ""
    )

evtid_env_power_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 57)
)
evtid_env_power_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_power_fail.setStatus(
        ""
    )

evtid_env_power_sig_vol = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 58)
)
evtid_env_power_sig_vol.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_power_sig_vol.setStatus(
        ""
    )

evtid_env_fan_rst = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 59)
)
evtid_env_fan_rst.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_fan_rst.setStatus(
        ""
    )

evtid_env_fan_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 60)
)
evtid_env_fan_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_fan_fail.setStatus(
        ""
    )

evtid_env_fan_pr = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 61)
)
evtid_env_fan_pr.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_fan_pr.setStatus(
        ""
    )

evtid_env_fan_not_pr = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 62)
)
evtid_env_fan_not_pr.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_fan_not_pr.setStatus(
        ""
    )

evtid_env_fan_over_speed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 63)
)
evtid_env_fan_over_speed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_fan_over_speed.setStatus(
        ""
    )

evtid_env_fan_track = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 64)
)
evtid_env_fan_track.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_fan_track.setStatus(
        ""
    )

evtid_env_therm_level_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 65)
)
evtid_env_therm_level_1.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_therm_level_1.setStatus(
        ""
    )

evtid_env_therm_level_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 66)
)
evtid_env_therm_level_2.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_therm_level_2.setStatus(
        ""
    )

evtid_env_therm_level_2_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 67)
)
evtid_env_therm_level_2_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_therm_level_2_shutdown.setStatus(
        ""
    )

evtid_env_therm_l2_ctr_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 68)
)
evtid_env_therm_l2_ctr_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_therm_l2_ctr_shutdown.setStatus(
        ""
    )

evtid_env_therm_ignore_value = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 69)
)
evtid_env_therm_ignore_value.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_therm_ignore_value.setStatus(
        ""
    )

evtid_env_therm_track = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 70)
)
evtid_env_therm_track.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_therm_track.setStatus(
        ""
    )

evtid_env_vol_level_1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 71)
)
evtid_env_vol_level_1.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_vol_level_1.setStatus(
        ""
    )

evtid_env_vol_level_2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 72)
)
evtid_env_vol_level_2.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_vol_level_2.setStatus(
        ""
    )

evtid_env_vol_level_2_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 73)
)
evtid_env_vol_level_2_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_vol_level_2_shutdown.setStatus(
        ""
    )

evtid_env_vol_l2_ctr_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 74)
)
evtid_env_vol_l2_ctr_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_vol_l2_ctr_shutdown.setStatus(
        ""
    )

evtid_env_vol_level_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 75)
)
evtid_env_vol_level_3.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_vol_level_3.setStatus(
        ""
    )

evtid_env_vol_track = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 76)
)
evtid_env_vol_track.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_vol_track.setStatus(
        ""
    )

evtid_env_ups_ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 77)
)
evtid_env_ups_ok.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_ups_ok.setStatus(
        ""
    )

evtid_env_ups_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 78)
)
evtid_env_ups_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_ups_fail.setStatus(
        ""
    )

evtid_env_ups_ac_loss = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 79)
)
evtid_env_ups_ac_loss.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_ups_ac_loss.setStatus(
        ""
    )

evtid_env_ups_power_low = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 80)
)
evtid_env_ups_power_low.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_env_ups_power_low.setStatus(
        ""
    )

evtid_smart_tec = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 81)
)
evtid_smart_tec.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_smart_tec.setStatus(
        ""
    )

evtid_smart_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 82)
)
evtid_smart_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_smart_fail.setStatus(
        ""
    )

evtid_rb_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 83)
)
evtid_rb_failover.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_rb_failover.setStatus(
        ""
    )

evtid_wdt_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 84)
)
evtid_wdt_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_wdt_shutdown.setStatus(
        ""
    )

evtid_wdt_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 85)
)
evtid_wdt_reset.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_wdt_reset.setStatus(
        ""
    )

evtid_jbod_pd_inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 86)
)
evtid_jbod_pd_inserted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_pd_inserted.setStatus(
        ""
    )

evtid_jbod_pd_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 87)
)
evtid_jbod_pd_removed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_pd_removed.setStatus(
        ""
    )

evtid_jbod_hdd_readerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 88)
)
evtid_jbod_hdd_readerr.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_hdd_readerr.setStatus(
        ""
    )

evtid_jbod_hdd_writeerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 89)
)
evtid_jbod_hdd_writeerr.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_hdd_writeerr.setStatus(
        ""
    )

evtid_jbod_hdd_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 90)
)
evtid_jbod_hdd_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_hdd_error.setStatus(
        ""
    )

evtid_jbod_hdd_io_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 91)
)
evtid_jbod_hdd_io_timeout.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_hdd_io_timeout.setStatus(
        ""
    )

evtid_jbod_inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 92)
)
evtid_jbod_inserted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_inserted.setStatus(
        ""
    )

evtid_jbod_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 93)
)
evtid_jbod_removed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_removed.setStatus(
        ""
    )

evtid_jbod_ctr_inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 94)
)
evtid_jbod_ctr_inserted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_ctr_inserted.setStatus(
        ""
    )

evtid_jbod_ctr_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 95)
)
evtid_jbod_ctr_removed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_ctr_removed.setStatus(
        ""
    )

evtid_jbod_smart_tec = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 96)
)
evtid_jbod_smart_tec.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_smart_tec.setStatus(
        ""
    )

evtid_jbod_smart_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 97)
)
evtid_jbod_smart_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_smart_fail.setStatus(
        ""
    )

evtid_jbod_degraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 98)
)
evtid_jbod_degraded.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_degraded.setStatus(
        ""
    )

evtid_enc_ps_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 99)
)
evtid_enc_ps_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_ps_fail.setStatus(
        ""
    )

evtid_enc_ps_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 100)
)
evtid_enc_ps_normal.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_ps_normal.setStatus(
        ""
    )

evtid_enc_fan_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 101)
)
evtid_enc_fan_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_fan_fail.setStatus(
        ""
    )

evtid_enc_fan_normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 102)
)
evtid_enc_fan_normal.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_fan_normal.setStatus(
        ""
    )

evtid_enc_volt_warn_ov = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 103)
)
evtid_enc_volt_warn_ov.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_volt_warn_ov.setStatus(
        ""
    )

evtid_enc_volt_warn_uv = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 104)
)
evtid_enc_volt_warn_uv.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_volt_warn_uv.setStatus(
        ""
    )

evtid_enc_volt_crit_ov = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 105)
)
evtid_enc_volt_crit_ov.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_volt_crit_ov.setStatus(
        ""
    )

evtid_enc_volt_crit_uv = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 106)
)
evtid_enc_volt_crit_uv.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_volt_crit_uv.setStatus(
        ""
    )

evtid_enc_volt_recovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 107)
)
evtid_enc_volt_recovery.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_volt_recovery.setStatus(
        ""
    )

evtid_enc_therm_warn_ot = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 108)
)
evtid_enc_therm_warn_ot.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_therm_warn_ot.setStatus(
        ""
    )

evtid_enc_therm_warn_ut = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 109)
)
evtid_enc_therm_warn_ut.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_therm_warn_ut.setStatus(
        ""
    )

evtid_enc_therm_fail_ot = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 110)
)
evtid_enc_therm_fail_ot.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_therm_fail_ot.setStatus(
        ""
    )

evtid_enc_therm_fail_ut = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 111)
)
evtid_enc_therm_fail_ut.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_therm_fail_ut.setStatus(
        ""
    )

evtid_enc_therm_recovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 112)
)
evtid_enc_therm_recovery.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_enc_therm_recovery.setStatus(
        ""
    )

evtid_lvm_vg_create_ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 113)
)
evtid_lvm_vg_create_ok.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_create_ok.setStatus(
        ""
    )

evtid_lvm_vg_create_ok_smi = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 114)
)
evtid_lvm_vg_create_ok_smi.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_create_ok_smi.setStatus(
        ""
    )

evtid_lvm_vg_create_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 115)
)
evtid_lvm_vg_create_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_create_fail.setStatus(
        ""
    )

evtid_lvm_vg_delete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 116)
)
evtid_lvm_vg_delete.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_delete.setStatus(
        ""
    )

evtid_lvm_vg_delete_smi = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 117)
)
evtid_lvm_vg_delete_smi.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_delete_smi.setStatus(
        ""
    )

evtid_lvm_vg_rename = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 118)
)
evtid_lvm_vg_rename.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_rename.setStatus(
        ""
    )

evtid_lvm_udv_create_ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 119)
)
evtid_lvm_udv_create_ok.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_create_ok.setStatus(
        ""
    )

evtid_lvm_udv_create_ok_smi = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 120)
)
evtid_lvm_udv_create_ok_smi.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_create_ok_smi.setStatus(
        ""
    )

evtid_lvm_udv_create_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 121)
)
evtid_lvm_udv_create_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_create_fail.setStatus(
        ""
    )

evtid_lvm_udv_delete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 122)
)
evtid_lvm_udv_delete.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_delete.setStatus(
        ""
    )

evtid_lvm_udv_delete_smi = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 123)
)
evtid_lvm_udv_delete_smi.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_delete_smi.setStatus(
        ""
    )

evtid_lvm_udv_rename = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 124)
)
evtid_lvm_udv_rename.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_rename.setStatus(
        ""
    )

evtid_lvm_udv_readonly = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 125)
)
evtid_lvm_udv_readonly.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_readonly.setStatus(
        ""
    )

evtid_lvm_udv_wr_back = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 126)
)
evtid_lvm_udv_wr_back.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_wr_back.setStatus(
        ""
    )

evtid_lvm_udv_wr_thru = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 127)
)
evtid_lvm_udv_wr_thru.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_wr_thru.setStatus(
        ""
    )

evtid_lvm_udv_extend = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 128)
)
evtid_lvm_udv_extend.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_extend.setStatus(
        ""
    )

evtid_lvm_udv_attach_lun_ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 129)
)
evtid_lvm_udv_attach_lun_ok.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_attach_lun_ok.setStatus(
        ""
    )

evtid_lvm_udv_attach_lun_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 130)
)
evtid_lvm_udv_attach_lun_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_attach_lun_fail.setStatus(
        ""
    )

evtid_lvm_udv_detach_lun_ok = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 131)
)
evtid_lvm_udv_detach_lun_ok.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_detach_lun_ok.setStatus(
        ""
    )

evtid_lvm_udv_detach_lun_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 132)
)
evtid_lvm_udv_detach_lun_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_detach_lun_fail.setStatus(
        ""
    )

evtid_lvm_udv_init_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 133)
)
evtid_lvm_udv_init_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_init_started.setStatus(
        ""
    )

evtid_lvm_udv_init_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 134)
)
evtid_lvm_udv_init_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_init_finished.setStatus(
        ""
    )

evtid_lvm_udv_init_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 135)
)
evtid_lvm_udv_init_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_init_failed.setStatus(
        ""
    )

evtid_lvm_udv_rebuild_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 136)
)
evtid_lvm_udv_rebuild_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_rebuild_started.setStatus(
        ""
    )

evtid_lvm_udv_rebuild_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 137)
)
evtid_lvm_udv_rebuild_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_rebuild_finished.setStatus(
        ""
    )

evtid_lvm_udv_rebuild_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 138)
)
evtid_lvm_udv_rebuild_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_rebuild_failed.setStatus(
        ""
    )

evtid_lvm_udv_migrate_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 139)
)
evtid_lvm_udv_migrate_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_migrate_started.setStatus(
        ""
    )

evtid_lvm_udv_migrate_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 140)
)
evtid_lvm_udv_migrate_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_migrate_finished.setStatus(
        ""
    )

evtid_lvm_udv_migrate_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 141)
)
evtid_lvm_udv_migrate_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_migrate_failed.setStatus(
        ""
    )

evtid_lvm_udv_scrub_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 142)
)
evtid_lvm_udv_scrub_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_scrub_started.setStatus(
        ""
    )

evtid_lvm_udv_scrub_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 143)
)
evtid_lvm_udv_scrub_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_scrub_finished.setStatus(
        ""
    )

evtid_lvm_vg_migrate_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 144)
)
evtid_lvm_vg_migrate_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_migrate_started.setStatus(
        ""
    )

evtid_lvm_vg_migrate_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 145)
)
evtid_lvm_vg_migrate_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_migrate_finished.setStatus(
        ""
    )

evtid_lvm_vg_move_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 146)
)
evtid_lvm_vg_move_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_move_started.setStatus(
        ""
    )

evtid_lvm_vg_move_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 147)
)
evtid_lvm_vg_move_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_move_finished.setStatus(
        ""
    )

evtid_lvm_udv_move_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 148)
)
evtid_lvm_udv_move_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_move_started.setStatus(
        ""
    )

evtid_lvm_udv_move_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 149)
)
evtid_lvm_udv_move_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_move_finished.setStatus(
        ""
    )

evtid_lvm_udv_move_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 150)
)
evtid_lvm_udv_move_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_move_failed.setStatus(
        ""
    )

evtid_lvm_udv_attach_lun = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 151)
)
evtid_lvm_udv_attach_lun.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_attach_lun.setStatus(
        ""
    )

evtid_lvm_udv_detach_lun = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 152)
)
evtid_lvm_udv_detach_lun.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_detach_lun.setStatus(
        ""
    )

evtid_lvm_vg_activated = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 153)
)
evtid_lvm_vg_activated.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_activated.setStatus(
        ""
    )

evtid_lvm_vg_deactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 154)
)
evtid_lvm_vg_deactivated.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_deactivated.setStatus(
        ""
    )

evtid_lvm_udv_rewrite_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 155)
)
evtid_lvm_udv_rewrite_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_rewrite_started.setStatus(
        ""
    )

evtid_lvm_udv_rewrite_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 156)
)
evtid_lvm_udv_rewrite_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_rewrite_finished.setStatus(
        ""
    )

evtid_lvm_udv_rewrite_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 157)
)
evtid_lvm_udv_rewrite_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_rewrite_failed.setStatus(
        ""
    )

evtid_lvm_vg_degraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 158)
)
evtid_lvm_vg_degraded.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_degraded.setStatus(
        ""
    )

evtid_lvm_udv_degraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 159)
)
evtid_lvm_udv_degraded.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_degraded.setStatus(
        ""
    )

evtid_lvm_vg_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 160)
)
evtid_lvm_vg_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_failed.setStatus(
        ""
    )

evtid_lvm_udv_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 161)
)
evtid_lvm_udv_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_failed.setStatus(
        ""
    )

evtid_lvm_udv_io_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 162)
)
evtid_lvm_udv_io_fault.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_io_fault.setStatus(
        ""
    )

evtid_lvm_recoverable_read_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 163)
)
evtid_lvm_recoverable_read_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_recoverable_read_error.setStatus(
        ""
    )

evtid_lvm_recoverable_write_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 164)
)
evtid_lvm_recoverable_write_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_recoverable_write_error.setStatus(
        ""
    )

evtid_lvm_unrecoverable_read_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 165)
)
evtid_lvm_unrecoverable_read_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_unrecoverable_read_error.setStatus(
        ""
    )

evtid_lvm_unrecoverable_write_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 166)
)
evtid_lvm_unrecoverable_write_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_unrecoverable_write_error.setStatus(
        ""
    )

evtid_lvm_config_read_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 167)
)
evtid_lvm_config_read_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_config_read_fail.setStatus(
        ""
    )

evtid_lvm_config_write_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 168)
)
evtid_lvm_config_write_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_config_write_fail.setStatus(
        ""
    )

evtid_lvm_cv_boot_error_adjust_global = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 169)
)
evtid_lvm_cv_boot_error_adjust_global.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_cv_boot_error_adjust_global.setStatus(
        ""
    )

evtid_lvm_cv_boot_global = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 170)
)
evtid_lvm_cv_boot_global.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_cv_boot_global.setStatus(
        ""
    )

evtid_lvm_cv_boot_error_create_global = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 171)
)
evtid_lvm_cv_boot_error_create_global.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_cv_boot_error_create_global.setStatus(
        ""
    )

evtid_lvm_pd_dedicated_spare = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 172)
)
evtid_lvm_pd_dedicated_spare.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_dedicated_spare.setStatus(
        ""
    )

evtid_lvm_pd_global_spare = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 173)
)
evtid_lvm_pd_global_spare.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_global_spare.setStatus(
        ""
    )

evtid_lvm_pd_read_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 174)
)
evtid_lvm_pd_read_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_read_error.setStatus(
        ""
    )

evtid_lvm_pd_write_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 175)
)
evtid_lvm_pd_write_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_write_error.setStatus(
        ""
    )

evtid_lvm_snap_mem = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 176)
)
evtid_lvm_snap_mem.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_mem.setStatus(
        ""
    )

evtid_lvm_snap_space_overflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 177)
)
evtid_lvm_snap_space_overflow.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_space_overflow.setStatus(
        ""
    )

evtid_lvm_snap_threshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 178)
)
evtid_lvm_snap_threshold.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_threshold.setStatus(
        ""
    )

evtid_lvm_snap_delete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 179)
)
evtid_lvm_snap_delete.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_delete.setStatus(
        ""
    )

evtid_lvm_snap_auto_delete = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 180)
)
evtid_lvm_snap_auto_delete.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_auto_delete.setStatus(
        ""
    )

evtid_lvm_snap_take = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 181)
)
evtid_lvm_snap_take.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_take.setStatus(
        ""
    )

evtid_lvm_snap_set_space = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 182)
)
evtid_lvm_snap_set_space.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_set_space.setStatus(
        ""
    )

evtid_lvm_snap_rollback_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 183)
)
evtid_lvm_snap_rollback_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_rollback_started.setStatus(
        ""
    )

evtid_lvm_snap_rollback_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 184)
)
evtid_lvm_snap_rollback_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_rollback_finished.setStatus(
        ""
    )

evtid_lvm_snap_quota_reached = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 185)
)
evtid_lvm_snap_quota_reached.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_quota_reached.setStatus(
        ""
    )

evtid_lvm_scrub_wrong_parity = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 186)
)
evtid_lvm_scrub_wrong_parity.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_scrub_wrong_parity.setStatus(
        ""
    )

evtid_lvm_scrub_data_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 187)
)
evtid_lvm_scrub_data_recovered.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_scrub_data_recovered.setStatus(
        ""
    )

evtid_lvm_pd_freed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 188)
)
evtid_lvm_pd_freed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_freed.setStatus(
        ""
    )

evtid_jbod_lvm_pd_freed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 189)
)
evtid_jbod_lvm_pd_freed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_freed.setStatus(
        ""
    )

evtid_lvm_vg_imported = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 190)
)
evtid_lvm_vg_imported.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_imported.setStatus(
        ""
    )

evtid_lvm_vg_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 191)
)
evtid_lvm_vg_restored.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_restored.setStatus(
        ""
    )

evtid_lvm_udv_restored = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 192)
)
evtid_lvm_udv_restored.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_restored.setStatus(
        ""
    )

evtid_jbod_lvm_pd_dedicated_spare = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 193)
)
evtid_jbod_lvm_pd_dedicated_spare.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_dedicated_spare.setStatus(
        ""
    )

evtid_jbod_lvm_pd_global_spare = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 194)
)
evtid_jbod_lvm_pd_global_spare.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_global_spare.setStatus(
        ""
    )

evtid_jbod_lvm_config_read_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 195)
)
evtid_jbod_lvm_config_read_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_config_read_fail.setStatus(
        ""
    )

evtid_jbod_lvm_config_write_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 196)
)
evtid_jbod_lvm_config_write_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_config_write_fail.setStatus(
        ""
    )

evtid_jbod_lvm_pd_read_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 197)
)
evtid_jbod_lvm_pd_read_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_read_error.setStatus(
        ""
    )

evtid_jbod_lvm_pd_write_error = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 198)
)
evtid_jbod_lvm_pd_write_error.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_write_error.setStatus(
        ""
    )

evtid_lvm_rg_owner_changed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 199)
)
evtid_lvm_rg_owner_changed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_rg_owner_changed.setStatus(
        ""
    )

evtid_lvm_force_ctr_write_thru = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 200)
)
evtid_lvm_force_ctr_write_thru.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_force_ctr_write_thru.setStatus(
        ""
    )

evtid_lvm_restore_ctr_cache_mode = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 201)
)
evtid_lvm_restore_ctr_cache_mode.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_restore_ctr_cache_mode.setStatus(
        ""
    )

evtid_lvm_failover_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 202)
)
evtid_lvm_failover_completed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_failover_completed.setStatus(
        ""
    )

evtid_lvm_failback_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 203)
)
evtid_lvm_failback_completed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_failback_completed.setStatus(
        ""
    )

evtid_lvm_pd_scrub_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 204)
)
evtid_lvm_pd_scrub_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_scrub_started.setStatus(
        ""
    )

evtid_lvm_pd_scrub_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 205)
)
evtid_lvm_pd_scrub_completed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_scrub_completed.setStatus(
        ""
    )

evtid_jbod_lvm_pd_scrub_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 206)
)
evtid_jbod_lvm_pd_scrub_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_scrub_started.setStatus(
        ""
    )

evtid_jbod_lvm_pd_scrub_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 207)
)
evtid_jbod_lvm_pd_scrub_completed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_scrub_completed.setStatus(
        ""
    )

evtid_lvm_pd_check_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 208)
)
evtid_lvm_pd_check_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_check_started.setStatus(
        ""
    )

evtid_lvm_pd_check_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 209)
)
evtid_lvm_pd_check_completed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_check_completed.setStatus(
        ""
    )

evtid_lvm_pd_check_term = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 210)
)
evtid_lvm_pd_check_term.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_check_term.setStatus(
        ""
    )

evtid_jbod_lvm_pd_check_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 211)
)
evtid_jbod_lvm_pd_check_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_check_started.setStatus(
        ""
    )

evtid_jbod_lvm_pd_check_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 212)
)
evtid_jbod_lvm_pd_check_completed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_check_completed.setStatus(
        ""
    )

evtid_jbod_lvm_pd_check_term = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 213)
)
evtid_jbod_lvm_pd_check_term.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_jbod_lvm_pd_check_term.setStatus(
        ""
    )

evtid_lvm_scrub_recovered_data = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 214)
)
evtid_lvm_scrub_recovered_data.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_scrub_recovered_data.setStatus(
        ""
    )

evtid_lvm_scrub_parity_recovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 215)
)
evtid_lvm_scrub_parity_recovered.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_scrub_parity_recovered.setStatus(
        ""
    )

evtid_lvm_udv_scrub_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 216)
)
evtid_lvm_udv_scrub_aborted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_scrub_aborted.setStatus(
        ""
    )

evtid_lvm_snap_clear_space = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 217)
)
evtid_lvm_snap_clear_space.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_snap_clear_space.setStatus(
        ""
    )

evtid_lvm_large_vg_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 218)
)
evtid_lvm_large_vg_created.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_large_vg_created.setStatus(
        ""
    )

evtid_lvm_weak_vg_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 219)
)
evtid_lvm_weak_vg_created.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_weak_vg_created.setStatus(
        ""
    )

evtid_lvm_vg_size_shrunk = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 220)
)
evtid_lvm_vg_size_shrunk.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_size_shrunk.setStatus(
        ""
    )

evtid_lvm_udv_clone_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 221)
)
evtid_lvm_udv_clone_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_clone_started.setStatus(
        ""
    )

evtid_lvm_udv_clone_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 222)
)
evtid_lvm_udv_clone_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_clone_finished.setStatus(
        ""
    )

evtid_lvm_udv_clone_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 223)
)
evtid_lvm_udv_clone_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_clone_failed.setStatus(
        ""
    )

evtid_lvm_udv_clone_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 224)
)
evtid_lvm_udv_clone_aborted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_clone_aborted.setStatus(
        ""
    )

evtid_lvm_udv_replicate_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 225)
)
evtid_lvm_udv_replicate_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_replicate_started.setStatus(
        ""
    )

evtid_lvm_udv_replicate_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 226)
)
evtid_lvm_udv_replicate_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_replicate_finished.setStatus(
        ""
    )

evtid_lvm_udv_replicate_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 227)
)
evtid_lvm_udv_replicate_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_replicate_failed.setStatus(
        ""
    )

evtid_lvm_udv_replicate_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 228)
)
evtid_lvm_udv_replicate_aborted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_replicate_aborted.setStatus(
        ""
    )

evtid_lvm_udv_erase_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 229)
)
evtid_lvm_udv_erase_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_erase_finished.setStatus(
        ""
    )

evtid_lvm_udv_erase_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 230)
)
evtid_lvm_udv_erase_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_erase_failed.setStatus(
        ""
    )

evtid_lvm_udv_erase_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 231)
)
evtid_lvm_udv_erase_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_erase_started.setStatus(
        ""
    )

evtid_lvm_udv_set_as_replica = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 232)
)
evtid_lvm_udv_set_as_replica.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_set_as_replica.setStatus(
        ""
    )

evtid_lvm_udv_set_as_raid = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 233)
)
evtid_lvm_udv_set_as_raid.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_set_as_raid.setStatus(
        ""
    )

evtid_lvm_udv_replica_set = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 234)
)
evtid_lvm_udv_replica_set.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_replica_set.setStatus(
        ""
    )

evtid_lvm_udv_replica_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 235)
)
evtid_lvm_udv_replica_reset.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_replica_reset.setStatus(
        ""
    )

evtid_lvm_udv_clone_set = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 236)
)
evtid_lvm_udv_clone_set.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_clone_set.setStatus(
        ""
    )

evtid_lvm_udv_clone_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 237)
)
evtid_lvm_udv_clone_reset.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_clone_reset.setStatus(
        ""
    )

evtid_lvm_src_replicate_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 238)
)
evtid_lvm_src_replicate_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_src_replicate_started.setStatus(
        ""
    )

evtid_lvm_src_replicate_finished = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 239)
)
evtid_lvm_src_replicate_finished.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_src_replicate_finished.setStatus(
        ""
    )

evtid_lvm_src_replicate_failed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 240)
)
evtid_lvm_src_replicate_failed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_src_replicate_failed.setStatus(
        ""
    )

evtid_lvm_src_replicate_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 241)
)
evtid_lvm_src_replicate_aborted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_src_replicate_aborted.setStatus(
        ""
    )

evtid_lvm_vg_disk_missing = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 242)
)
evtid_lvm_vg_disk_missing.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_disk_missing.setStatus(
        ""
    )

evtid_lvm_pd_rps_started_l2l = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 243)
)
evtid_lvm_pd_rps_started_l2l.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_started_l2l.setStatus(
        ""
    )

evtid_lvm_pd_rps_started_l2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 244)
)
evtid_lvm_pd_rps_started_l2f.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_started_l2f.setStatus(
        ""
    )

evtid_lvm_pd_rps_started_f2l = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 245)
)
evtid_lvm_pd_rps_started_f2l.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_started_f2l.setStatus(
        ""
    )

evtid_lvm_pd_rps_started_f2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 246)
)
evtid_lvm_pd_rps_started_f2f.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_started_f2f.setStatus(
        ""
    )

evtid_lvm_pd_rps_finished_l2l = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 247)
)
evtid_lvm_pd_rps_finished_l2l.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_finished_l2l.setStatus(
        ""
    )

evtid_lvm_pd_rps_finished_l2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 248)
)
evtid_lvm_pd_rps_finished_l2f.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_finished_l2f.setStatus(
        ""
    )

evtid_lvm_pd_rps_finished_f2l = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 249)
)
evtid_lvm_pd_rps_finished_f2l.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_finished_f2l.setStatus(
        ""
    )

evtid_lvm_pd_rps_finished_f2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 250)
)
evtid_lvm_pd_rps_finished_f2f.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_finished_f2f.setStatus(
        ""
    )

evtid_lvm_pd_rps_failed_l2l = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 251)
)
evtid_lvm_pd_rps_failed_l2l.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_failed_l2l.setStatus(
        ""
    )

evtid_lvm_pd_rps_failed_l2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 252)
)
evtid_lvm_pd_rps_failed_l2f.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_failed_l2f.setStatus(
        ""
    )

evtid_lvm_pd_rps_failed_f2l = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 253)
)
evtid_lvm_pd_rps_failed_f2l.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_failed_f2l.setStatus(
        ""
    )

evtid_lvm_pd_rps_failed_f2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 254)
)
evtid_lvm_pd_rps_failed_f2f.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_rps_failed_f2f.setStatus(
        ""
    )

evtid_lvm_l_pd_udv_rewr_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 255)
)
evtid_lvm_l_pd_udv_rewr_fault.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_l_pd_udv_rewr_fault.setStatus(
        ""
    )

evtid_lvm_f_pd_udv_rewr_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 256)
)
evtid_lvm_f_pd_udv_rewr_fault.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_f_pd_udv_rewr_fault.setStatus(
        ""
    )

evtid_lvm_l_pd_io_retry_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 257)
)
evtid_lvm_l_pd_io_retry_fault.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_l_pd_io_retry_fault.setStatus(
        ""
    )

evtid_lvm_f_pd_io_retry_fault = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 258)
)
evtid_lvm_f_pd_io_retry_fault.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_f_pd_io_retry_fault.setStatus(
        ""
    )

evtid_lvm_pd_substitute_l2l = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 259)
)
evtid_lvm_pd_substitute_l2l.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_substitute_l2l.setStatus(
        ""
    )

evtid_lvm_pd_substitute_l2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 260)
)
evtid_lvm_pd_substitute_l2f.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_substitute_l2f.setStatus(
        ""
    )

evtid_lvm_pd_substitute_f2l = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 261)
)
evtid_lvm_pd_substitute_f2l.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_substitute_f2l.setStatus(
        ""
    )

evtid_lvm_pd_substitute_f2f = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 262)
)
evtid_lvm_pd_substitute_f2f.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_pd_substitute_f2f.setStatus(
        ""
    )

evtid_lvm_vg_threshold_hit = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 263)
)
evtid_lvm_vg_threshold_hit.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_vg_threshold_hit.setStatus(
        ""
    )

evtid_lvm_raid_set_created = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 264)
)
evtid_lvm_raid_set_created.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_raid_set_created.setStatus(
        ""
    )

evtid_lvm_raid_set_deleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 265)
)
evtid_lvm_raid_set_deleted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_raid_set_deleted.setStatus(
        ""
    )

evtid_lvm_udv_reclaim_started = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 266)
)
evtid_lvm_udv_reclaim_started.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_reclaim_started.setStatus(
        ""
    )

evtid_lvm_udv_reclaim_completed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 267)
)
evtid_lvm_udv_reclaim_completed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_reclaim_completed.setStatus(
        ""
    )

evtid_lvm_udv_reclaim_aborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 268)
)
evtid_lvm_udv_reclaim_aborted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_lvm_udv_reclaim_aborted.setStatus(
        ""
    )

evtid_hac_ctr_inserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 269)
)
evtid_hac_ctr_inserted.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_inserted.setStatus(
        ""
    )

evtid_hac_ctr_removed = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 270)
)
evtid_hac_ctr_removed.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_removed.setStatus(
        ""
    )

evtid_hac_ctr_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 271)
)
evtid_hac_ctr_timeout.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_timeout.setStatus(
        ""
    )

evtid_hac_ctr_lockdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 272)
)
evtid_hac_ctr_lockdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_lockdown.setStatus(
        ""
    )

evtid_hac_ctr_failover = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 273)
)
evtid_hac_ctr_failover.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_failover.setStatus(
        ""
    )

evtid_hac_ctr_reset = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 274)
)
evtid_hac_ctr_reset.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_reset.setStatus(
        ""
    )

evtid_hac_ctr_memory_ng = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 275)
)
evtid_hac_ctr_memory_ng.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_memory_ng.setStatus(
        ""
    )

evtid_hac_ctr_firmware_ng = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 276)
)
evtid_hac_ctr_firmware_ng.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_firmware_ng.setStatus(
        ""
    )

evtid_hac_ctr_lowspeed_ng = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 277)
)
evtid_hac_ctr_lowspeed_ng.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_lowspeed_ng.setStatus(
        ""
    )

evtid_hac_ctr_highspeed_ng = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 278)
)
evtid_hac_ctr_highspeed_ng.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_highspeed_ng.setStatus(
        ""
    )

evtid_hac_ctr_be_ng = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 279)
)
evtid_hac_ctr_be_ng.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_be_ng.setStatus(
        ""
    )

evtid_hac_ctr_fe_ng = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 280)
)
evtid_hac_ctr_fe_ng.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_ctr_fe_ng.setStatus(
        ""
    )

evtid_hac_jbod_hdd_path_ng = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 281)
)
evtid_hac_jbod_hdd_path_ng.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_hac_jbod_hdd_path_ng.setStatus(
        ""
    )

evtid_rms_console_login = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 282)
)
evtid_rms_console_login.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_rms_console_login.setStatus(
        ""
    )

evtid_rms_console_logout = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 283)
)
evtid_rms_console_logout.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_rms_console_logout.setStatus(
        ""
    )

evtid_rms_web_login = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 284)
)
evtid_rms_web_login.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_rms_web_login.setStatus(
        ""
    )

evtid_rms_web_logout = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 285)
)
evtid_rms_web_logout.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_rms_web_logout.setStatus(
        ""
    )

evtid_rms_log_clear = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 286)
)
evtid_rms_log_clear.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_rms_log_clear.setStatus(
        ""
    )

evtid_sys_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 287)
)
evtid_sys_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_shutdown.setStatus(
        ""
    )

evtid_sys_reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 288)
)
evtid_sys_reboot.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_reboot.setStatus(
        ""
    )

evtid_fw_upgrade_start = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 289)
)
evtid_fw_upgrade_start.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_fw_upgrade_start.setStatus(
        ""
    )

evtid_fw_upgrade_success = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 290)
)
evtid_fw_upgrade_success.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_fw_upgrade_success.setStatus(
        ""
    )

evtid_fw_upgrade_failure = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 291)
)
evtid_fw_upgrade_failure.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_fw_upgrade_failure.setStatus(
        ""
    )

evtid_ipc_fw_upgrade_timeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 292)
)
evtid_ipc_fw_upgrade_timeout.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_ipc_fw_upgrade_timeout.setStatus(
        ""
    )

evtid_sys_console_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 293)
)
evtid_sys_console_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_console_shutdown.setStatus(
        ""
    )

evtid_sys_web_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 294)
)
evtid_sys_web_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_web_shutdown.setStatus(
        ""
    )

evtid_sys_btn_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 295)
)
evtid_sys_btn_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_btn_shutdown.setStatus(
        ""
    )

evtid_sys_console_reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 296)
)
evtid_sys_console_reboot.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_console_reboot.setStatus(
        ""
    )

evtid_sys_web_reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 297)
)
evtid_sys_web_reboot.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_web_reboot.setStatus(
        ""
    )

evtid_sys_lcm_shutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 298)
)
evtid_sys_lcm_shutdown.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_lcm_shutdown.setStatus(
        ""
    )

evtid_sys_lcm_reboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 299)
)
evtid_sys_lcm_reboot.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_sys_lcm_reboot.setStatus(
        ""
    )

evtid_ctr_reboot_fwsync = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 300)
)
evtid_ctr_reboot_fwsync.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_ctr_reboot_fwsync.setStatus(
        ""
    )

evtid_auto_qrep_not_enable = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 301)
)
evtid_auto_qrep_not_enable.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_auto_qrep_not_enable.setStatus(
        ""
    )

evtid_auto_qrep_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 302)
)
evtid_auto_qrep_err.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_auto_qrep_err.setStatus(
        ""
    )

evtid_auto_qrep_no_snap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 303)
)
evtid_auto_qrep_no_snap.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_auto_qrep_no_snap.setStatus(
        ""
    )

evtid_auto_clone_err = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 304)
)
evtid_auto_clone_err.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_auto_clone_err.setStatus(
        ""
    )

evtid_auto_clone_no_snap = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 305)
)
evtid_auto_clone_no_snap.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_auto_clone_no_snap.setStatus(
        ""
    )

evtid_qrep_portal_enabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 306)
)
evtid_qrep_portal_enabled.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_qrep_portal_enabled.setStatus(
        ""
    )

evtid_qrep_portal_disabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 307)
)
evtid_qrep_portal_disabled.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_qrep_portal_disabled.setStatus(
        ""
    )

evtid_send_mail_fail = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 308)
)
evtid_send_mail_fail.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_send_mail_fail.setStatus(
        ""
    )

evtid_config_imported = NotificationType(
    (1, 3, 6, 1, 4, 1, 22274, 1, 8000, 0, 309)
)
evtid_config_imported.setObjects(
    ("QSAN-SNMP-MIB", "eventString")
)
if mibBuilder.loadTexts:
    evtid_config_imported.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QSAN-SNMP-MIB",
    **{"internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "qsan": qsan,
       "raid": raid,
       "system-config": system_config,
       "system-config-status": system_config_status,
       "sys-status-raid": sys_status_raid,
       "sys-status-temp": sys_status_temp,
       "sys-status-volt": sys_status_volt,
       "sys-status-ups": sys_status_ups,
       "sys-status-fan": sys_status_fan,
       "sys-status-psu": sys_status_psu,
       "sys-status-dual": sys_status_dual,
       "system-config-setting": system_config_setting,
       "sys-name": sys_name,
       "sys-current-time": sys_current_time,
       "sys-ntp-server": sys_ntp_server,
       "system-config-ip": system_config_ip,
       "sys-mac": sys_mac,
       "sys-ip": sys_ip,
       "sys-mask": sys_mask,
       "sys-gateway": sys_gateway,
       "sys-dns": sys_dns,
       "sys-http-port": sys_http_port,
       "sys-https-port": sys_https_port,
       "sys-ssh-port": sys_ssh_port,
       "system-config-mail": system_config_mail,
       "sys-mailfrom": sys_mailfrom,
       "sys-mailto1": sys_mailto1,
       "sys-mailto1-filter": sys_mailto1_filter,
       "sys-mailto2": sys_mailto2,
       "sys-mailto2-filter": sys_mailto2_filter,
       "sys-mailto3": sys_mailto3,
       "sys-mailto3-filter": sys_mailto3_filter,
       "sys-smpt-relay": sys_smpt_relay,
       "volume-config": volume_config,
       "physical-disk": physical_disk,
       "physical-disk-item": physical_disk_item,
       "pd-location": pd_location,
       "pd-idx": pd_idx,
       "pd-size": pd_size,
       "pd-RG": pd_RG,
       "pd-status": pd_status,
       "pd-status-health": pd_status_health,
       "pd-status-usage": pd_status_usage,
       "pd-vendor": pd_vendor,
       "pd-serial": pd_serial,
       "pd-type": pd_type,
       "pd-write-cache": pd_write_cache,
       "pd-standby": pd_standby,
       "pd-readahead": pd_readahead,
       "pd-command-queuing": pd_command_queuing,
       "pd-product": pd_product,
       "pd-revision": pd_revision,
       "raid-group": raid_group,
       "raid-group-item": raid_group_item,
       "rg-name": rg_name,
       "rg-total": rg_total,
       "rg-free": rg_free,
       "rg-pd": rg_pd,
       "rg-vd": rg_vd,
       "rg-status": rg_status,
       "rg-health": rg_health,
       "rg-raid": rg_raid,
       "rg-owner": rg_owner,
       "rg-powner": rg_powner,
       "virtual-disk": virtual_disk,
       "virtual-disk-item": virtual_disk_item,
       "vd-name": vd_name,
       "vd-size": vd_size,
       "vd-right": vd_right,
       "vd-priority": vd_priority,
       "vd-bgrate": vd_bgrate,
       "vd-status": vd_status,
       "vd-health": vd_health,
       "vd-progress": vd_progress,
       "vd-raid": vd_raid,
       "vd-lun": vd_lun,
       "vd-snapshot-space": vd_snapshot_space,
       "vd-snapshot": vd_snapshot,
       "vd-rg": vd_rg,
       "logical-unit": logical_unit,
       "logical-unit-item": logical_unit_item,
       "lun-index": lun_index,
       "lun-host": lun_host,
       "lun-target": lun_target,
       "lun-num": lun_num,
       "lun-permission": lun_permission,
       "lun-vd": lun_vd,
       "enclosure-management": enclosure_management,
       "hardware-monitor": hardware_monitor,
       "hardware-monitor-item": hardware_monitor_item,
       "ems-loc": ems_loc,
       "ems-type": ems_type,
       "ems-item": ems_item,
       "ems-value": ems_value,
       "ems-status": ems_status,
       "enclosure-management-ses": enclosure_management_ses,
       "ems-ses": ems_ses,
       "hdd-smart": hdd_smart,
       "hdd-smart-item": hdd_smart_item,
       "hdd-loc": hdd_loc,
       "hdd-type": hdd_type,
       "hdd-readerror": hdd_readerror,
       "hdd-temperature": hdd_temperature,
       "maintenance": maintenance,
       "maintenance-info": maintenance_info,
       "maintenance-info-cpu": maintenance_info_cpu,
       "maintenance-info-mem": maintenance_info_mem,
       "maintenance-info-fw": maintenance_info_fw,
       "maintenance-info-serial-no": maintenance_info_serial_no,
       "maintenance-info-backplane-id": maintenance_info_backplane_id,
       "maintenance-info-status": maintenance_info_status,
       "maintenance-info-message": maintenance_info_message,
       "iscsi-config": iscsi_config,
       "iscsi-config-nic": iscsi_config_nic,
       "iscsi-nic-item": iscsi_nic_item,
       "iscsi-nic-id": iscsi_nic_id,
       "iscsi-nic-ctrl": iscsi_nic_ctrl,
       "iscsi-nic-ip": iscsi_nic_ip,
       "iscsi-nic-mask": iscsi_nic_mask,
       "iscsi-nic-gw": iscsi_nic_gw,
       "iscsi-nic-jumbo": iscsi_nic_jumbo,
       "iscsi-nic-mac": iscsi_nic_mac,
       "iscsi-config-entity": iscsi_config_entity,
       "iscsi-config-entity-item": iscsi_config_entity_item,
       "iscsi-config-isns-item": iscsi_config_isns_item,
       "iscsi-config-node": iscsi_config_node,
       "iscsi-node-item": iscsi_node_item,
       "iscsi-node-id": iscsi_node_id,
       "iscsi-node-ctrl": iscsi_node_ctrl,
       "iscsi-node-auth": iscsi_node_auth,
       "iscsi-node-name": iscsi_node_name,
       "iscsi-node-portal": iscsi_node_portal,
       "event": event,
       "evtid-test": evtid_test,
       "evtid-ecc-single": evtid_ecc_single,
       "evtid-ecc-multiple": evtid_ecc_multiple,
       "evtid-ecc-dimm": evtid_ecc_dimm,
       "evtid-ecc-none": evtid_ecc_none,
       "evtid-bbm-start-syncing": evtid_bbm_start_syncing,
       "evtid-bbm-stop-syncing": evtid_bbm_stop_syncing,
       "evtid-bbm-installed": evtid_bbm_installed,
       "evtid-bbm-sts-good": evtid_bbm_sts_good,
       "evtid-bbm-sts-charging": evtid_bbm_sts_charging,
       "evtid-bbm-sts-fail": evtid_bbm_sts_fail,
       "evtid-bbm-enabled": evtid_bbm_enabled,
       "evtid-bbm-inserted": evtid_bbm_inserted,
       "evtid-bbm-removed": evtid_bbm_removed,
       "evtid-bbm-warning-temperature": evtid_bbm_warning_temperature,
       "evtid-qcopy-job-info": evtid_qcopy_job_info,
       "evtid-qcopy-job-restart": evtid_qcopy_job_restart,
       "evtid-qcopy-job-fail": evtid_qcopy_job_fail,
       "evtid-qcopy-job-abort": evtid_qcopy_job_abort,
       "evtid-qcopy-job-abort-lba-size": evtid_qcopy_job_abort_lba_size,
       "evtid-scsi-busreset": evtid_scsi_busreset,
       "evtid-scsi-host-error": evtid_scsi_host_error,
       "evtid-sas-port-reply-error": evtid_sas_port_reply_error,
       "evtid-sas-unknown-port-reply-error": evtid_sas_unknown_port_reply_error,
       "evtid-fc-port-reply-error": evtid_fc_port_reply_error,
       "evtid-fc-unknown-port-reply-error": evtid_fc_unknown_port_reply_error,
       "evtid-fc-port-linkup": evtid_fc_port_linkup,
       "evtid-fc-port-linkdown": evtid_fc_port_linkdown,
       "evtid-iscsi-login-accepted": evtid_iscsi_login_accepted,
       "evtid-iscsi-login-rejected": evtid_iscsi_login_rejected,
       "evtid-iscsi-logout-recvd": evtid_iscsi_logout_recvd,
       "evtid-sata-enable-dev-fail": evtid_sata_enable_dev_fail,
       "evtid-sata-edma-mem-fail": evtid_sata_edma_mem_fail,
       "evtid-sata-remap-mem-fail": evtid_sata_remap_mem_fail,
       "evtid-sata-prd-mem-fail": evtid_sata_prd_mem_fail,
       "evtid-sata-revision-id-fail": evtid_sata_revision_id_fail,
       "evtid-sata-set-reg-fail": evtid_sata_set_reg_fail,
       "evtid-sata-init-fail": evtid_sata_init_fail,
       "evtid-sata-diag-fail": evtid_sata_diag_fail,
       "evtid-mode-id-fail": evtid_mode_id_fail,
       "evtid-sata-chip-count-error": evtid_sata_chip_count_error,
       "evtid-disk-upgrade-started": evtid_disk_upgrade_started,
       "evtid-disk-upgrade-finished": evtid_disk_upgrade_finished,
       "evtid-disk-upgrade-failed": evtid_disk_upgrade_failed,
       "evtid-jbod-disk-upgrade-started": evtid_jbod_disk_upgrade_started,
       "evtid-jbod-disk-upgrade-finished": evtid_jbod_disk_upgrade_finished,
       "evtid-jbod-disk-upgrade-failed": evtid_jbod_disk_upgrade_failed,
       "evtid-pd-inserted": evtid_pd_inserted,
       "evtid-pd-removed": evtid_pd_removed,
       "evtid-hdd-readerr": evtid_hdd_readerr,
       "evtid-hdd-writeerr": evtid_hdd_writeerr,
       "evtid-hdd-error": evtid_hdd_error,
       "evtid-hdd-io-timeout": evtid_hdd_io_timeout,
       "evtid-hdd-temp-warning": evtid_hdd_temp_warning,
       "evtid-env-power-install": evtid_env_power_install,
       "evtid-env-power-absent": evtid_env_power_absent,
       "evtid-env-power-rst": evtid_env_power_rst,
       "evtid-env-power-fail": evtid_env_power_fail,
       "evtid-env-power-sig-vol": evtid_env_power_sig_vol,
       "evtid-env-fan-rst": evtid_env_fan_rst,
       "evtid-env-fan-fail": evtid_env_fan_fail,
       "evtid-env-fan-pr": evtid_env_fan_pr,
       "evtid-env-fan-not-pr": evtid_env_fan_not_pr,
       "evtid-env-fan-over-speed": evtid_env_fan_over_speed,
       "evtid-env-fan-track": evtid_env_fan_track,
       "evtid-env-therm-level-1": evtid_env_therm_level_1,
       "evtid-env-therm-level-2": evtid_env_therm_level_2,
       "evtid-env-therm-level-2-shutdown": evtid_env_therm_level_2_shutdown,
       "evtid-env-therm-l2-ctr-shutdown": evtid_env_therm_l2_ctr_shutdown,
       "evtid-env-therm-ignore-value": evtid_env_therm_ignore_value,
       "evtid-env-therm-track": evtid_env_therm_track,
       "evtid-env-vol-level-1": evtid_env_vol_level_1,
       "evtid-env-vol-level-2": evtid_env_vol_level_2,
       "evtid-env-vol-level-2-shutdown": evtid_env_vol_level_2_shutdown,
       "evtid-env-vol-l2-ctr-shutdown": evtid_env_vol_l2_ctr_shutdown,
       "evtid-env-vol-level-3": evtid_env_vol_level_3,
       "evtid-env-vol-track": evtid_env_vol_track,
       "evtid-env-ups-ok": evtid_env_ups_ok,
       "evtid-env-ups-fail": evtid_env_ups_fail,
       "evtid-env-ups-ac-loss": evtid_env_ups_ac_loss,
       "evtid-env-ups-power-low": evtid_env_ups_power_low,
       "evtid-smart-tec": evtid_smart_tec,
       "evtid-smart-fail": evtid_smart_fail,
       "evtid-rb-failover": evtid_rb_failover,
       "evtid-wdt-shutdown": evtid_wdt_shutdown,
       "evtid-wdt-reset": evtid_wdt_reset,
       "evtid-jbod-pd-inserted": evtid_jbod_pd_inserted,
       "evtid-jbod-pd-removed": evtid_jbod_pd_removed,
       "evtid-jbod-hdd-readerr": evtid_jbod_hdd_readerr,
       "evtid-jbod-hdd-writeerr": evtid_jbod_hdd_writeerr,
       "evtid-jbod-hdd-error": evtid_jbod_hdd_error,
       "evtid-jbod-hdd-io-timeout": evtid_jbod_hdd_io_timeout,
       "evtid-jbod-inserted": evtid_jbod_inserted,
       "evtid-jbod-removed": evtid_jbod_removed,
       "evtid-jbod-ctr-inserted": evtid_jbod_ctr_inserted,
       "evtid-jbod-ctr-removed": evtid_jbod_ctr_removed,
       "evtid-jbod-smart-tec": evtid_jbod_smart_tec,
       "evtid-jbod-smart-fail": evtid_jbod_smart_fail,
       "evtid-jbod-degraded": evtid_jbod_degraded,
       "evtid-enc-ps-fail": evtid_enc_ps_fail,
       "evtid-enc-ps-normal": evtid_enc_ps_normal,
       "evtid-enc-fan-fail": evtid_enc_fan_fail,
       "evtid-enc-fan-normal": evtid_enc_fan_normal,
       "evtid-enc-volt-warn-ov": evtid_enc_volt_warn_ov,
       "evtid-enc-volt-warn-uv": evtid_enc_volt_warn_uv,
       "evtid-enc-volt-crit-ov": evtid_enc_volt_crit_ov,
       "evtid-enc-volt-crit-uv": evtid_enc_volt_crit_uv,
       "evtid-enc-volt-recovery": evtid_enc_volt_recovery,
       "evtid-enc-therm-warn-ot": evtid_enc_therm_warn_ot,
       "evtid-enc-therm-warn-ut": evtid_enc_therm_warn_ut,
       "evtid-enc-therm-fail-ot": evtid_enc_therm_fail_ot,
       "evtid-enc-therm-fail-ut": evtid_enc_therm_fail_ut,
       "evtid-enc-therm-recovery": evtid_enc_therm_recovery,
       "evtid-lvm-vg-create-ok": evtid_lvm_vg_create_ok,
       "evtid-lvm-vg-create-ok-smi": evtid_lvm_vg_create_ok_smi,
       "evtid-lvm-vg-create-fail": evtid_lvm_vg_create_fail,
       "evtid-lvm-vg-delete": evtid_lvm_vg_delete,
       "evtid-lvm-vg-delete-smi": evtid_lvm_vg_delete_smi,
       "evtid-lvm-vg-rename": evtid_lvm_vg_rename,
       "evtid-lvm-udv-create-ok": evtid_lvm_udv_create_ok,
       "evtid-lvm-udv-create-ok-smi": evtid_lvm_udv_create_ok_smi,
       "evtid-lvm-udv-create-fail": evtid_lvm_udv_create_fail,
       "evtid-lvm-udv-delete": evtid_lvm_udv_delete,
       "evtid-lvm-udv-delete-smi": evtid_lvm_udv_delete_smi,
       "evtid-lvm-udv-rename": evtid_lvm_udv_rename,
       "evtid-lvm-udv-readonly": evtid_lvm_udv_readonly,
       "evtid-lvm-udv-wr-back": evtid_lvm_udv_wr_back,
       "evtid-lvm-udv-wr-thru": evtid_lvm_udv_wr_thru,
       "evtid-lvm-udv-extend": evtid_lvm_udv_extend,
       "evtid-lvm-udv-attach-lun-ok": evtid_lvm_udv_attach_lun_ok,
       "evtid-lvm-udv-attach-lun-fail": evtid_lvm_udv_attach_lun_fail,
       "evtid-lvm-udv-detach-lun-ok": evtid_lvm_udv_detach_lun_ok,
       "evtid-lvm-udv-detach-lun-fail": evtid_lvm_udv_detach_lun_fail,
       "evtid-lvm-udv-init-started": evtid_lvm_udv_init_started,
       "evtid-lvm-udv-init-finished": evtid_lvm_udv_init_finished,
       "evtid-lvm-udv-init-failed": evtid_lvm_udv_init_failed,
       "evtid-lvm-udv-rebuild-started": evtid_lvm_udv_rebuild_started,
       "evtid-lvm-udv-rebuild-finished": evtid_lvm_udv_rebuild_finished,
       "evtid-lvm-udv-rebuild-failed": evtid_lvm_udv_rebuild_failed,
       "evtid-lvm-udv-migrate-started": evtid_lvm_udv_migrate_started,
       "evtid-lvm-udv-migrate-finished": evtid_lvm_udv_migrate_finished,
       "evtid-lvm-udv-migrate-failed": evtid_lvm_udv_migrate_failed,
       "evtid-lvm-udv-scrub-started": evtid_lvm_udv_scrub_started,
       "evtid-lvm-udv-scrub-finished": evtid_lvm_udv_scrub_finished,
       "evtid-lvm-vg-migrate-started": evtid_lvm_vg_migrate_started,
       "evtid-lvm-vg-migrate-finished": evtid_lvm_vg_migrate_finished,
       "evtid-lvm-vg-move-started": evtid_lvm_vg_move_started,
       "evtid-lvm-vg-move-finished": evtid_lvm_vg_move_finished,
       "evtid-lvm-udv-move-started": evtid_lvm_udv_move_started,
       "evtid-lvm-udv-move-finished": evtid_lvm_udv_move_finished,
       "evtid-lvm-udv-move-failed": evtid_lvm_udv_move_failed,
       "evtid-lvm-udv-attach-lun": evtid_lvm_udv_attach_lun,
       "evtid-lvm-udv-detach-lun": evtid_lvm_udv_detach_lun,
       "evtid-lvm-vg-activated": evtid_lvm_vg_activated,
       "evtid-lvm-vg-deactivated": evtid_lvm_vg_deactivated,
       "evtid-lvm-udv-rewrite-started": evtid_lvm_udv_rewrite_started,
       "evtid-lvm-udv-rewrite-finished": evtid_lvm_udv_rewrite_finished,
       "evtid-lvm-udv-rewrite-failed": evtid_lvm_udv_rewrite_failed,
       "evtid-lvm-vg-degraded": evtid_lvm_vg_degraded,
       "evtid-lvm-udv-degraded": evtid_lvm_udv_degraded,
       "evtid-lvm-vg-failed": evtid_lvm_vg_failed,
       "evtid-lvm-udv-failed": evtid_lvm_udv_failed,
       "evtid-lvm-udv-io-fault": evtid_lvm_udv_io_fault,
       "evtid-lvm-recoverable-read-error": evtid_lvm_recoverable_read_error,
       "evtid-lvm-recoverable-write-error": evtid_lvm_recoverable_write_error,
       "evtid-lvm-unrecoverable-read-error": evtid_lvm_unrecoverable_read_error,
       "evtid-lvm-unrecoverable-write-error": evtid_lvm_unrecoverable_write_error,
       "evtid-lvm-config-read-fail": evtid_lvm_config_read_fail,
       "evtid-lvm-config-write-fail": evtid_lvm_config_write_fail,
       "evtid-lvm-cv-boot-error-adjust-global": evtid_lvm_cv_boot_error_adjust_global,
       "evtid-lvm-cv-boot-global": evtid_lvm_cv_boot_global,
       "evtid-lvm-cv-boot-error-create-global": evtid_lvm_cv_boot_error_create_global,
       "evtid-lvm-pd-dedicated-spare": evtid_lvm_pd_dedicated_spare,
       "evtid-lvm-pd-global-spare": evtid_lvm_pd_global_spare,
       "evtid-lvm-pd-read-error": evtid_lvm_pd_read_error,
       "evtid-lvm-pd-write-error": evtid_lvm_pd_write_error,
       "evtid-lvm-snap-mem": evtid_lvm_snap_mem,
       "evtid-lvm-snap-space-overflow": evtid_lvm_snap_space_overflow,
       "evtid-lvm-snap-threshold": evtid_lvm_snap_threshold,
       "evtid-lvm-snap-delete": evtid_lvm_snap_delete,
       "evtid-lvm-snap-auto-delete": evtid_lvm_snap_auto_delete,
       "evtid-lvm-snap-take": evtid_lvm_snap_take,
       "evtid-lvm-snap-set-space": evtid_lvm_snap_set_space,
       "evtid-lvm-snap-rollback-started": evtid_lvm_snap_rollback_started,
       "evtid-lvm-snap-rollback-finished": evtid_lvm_snap_rollback_finished,
       "evtid-lvm-snap-quota-reached": evtid_lvm_snap_quota_reached,
       "evtid-lvm-scrub-wrong-parity": evtid_lvm_scrub_wrong_parity,
       "evtid-lvm-scrub-data-recovered": evtid_lvm_scrub_data_recovered,
       "evtid-lvm-pd-freed": evtid_lvm_pd_freed,
       "evtid-jbod-lvm-pd-freed": evtid_jbod_lvm_pd_freed,
       "evtid-lvm-vg-imported": evtid_lvm_vg_imported,
       "evtid-lvm-vg-restored": evtid_lvm_vg_restored,
       "evtid-lvm-udv-restored": evtid_lvm_udv_restored,
       "evtid-jbod-lvm-pd-dedicated-spare": evtid_jbod_lvm_pd_dedicated_spare,
       "evtid-jbod-lvm-pd-global-spare": evtid_jbod_lvm_pd_global_spare,
       "evtid-jbod-lvm-config-read-fail": evtid_jbod_lvm_config_read_fail,
       "evtid-jbod-lvm-config-write-fail": evtid_jbod_lvm_config_write_fail,
       "evtid-jbod-lvm-pd-read-error": evtid_jbod_lvm_pd_read_error,
       "evtid-jbod-lvm-pd-write-error": evtid_jbod_lvm_pd_write_error,
       "evtid-lvm-rg-owner-changed": evtid_lvm_rg_owner_changed,
       "evtid-lvm-force-ctr-write-thru": evtid_lvm_force_ctr_write_thru,
       "evtid-lvm-restore-ctr-cache-mode": evtid_lvm_restore_ctr_cache_mode,
       "evtid-lvm-failover-completed": evtid_lvm_failover_completed,
       "evtid-lvm-failback-completed": evtid_lvm_failback_completed,
       "evtid-lvm-pd-scrub-started": evtid_lvm_pd_scrub_started,
       "evtid-lvm-pd-scrub-completed": evtid_lvm_pd_scrub_completed,
       "evtid-jbod-lvm-pd-scrub-started": evtid_jbod_lvm_pd_scrub_started,
       "evtid-jbod-lvm-pd-scrub-completed": evtid_jbod_lvm_pd_scrub_completed,
       "evtid-lvm-pd-check-started": evtid_lvm_pd_check_started,
       "evtid-lvm-pd-check-completed": evtid_lvm_pd_check_completed,
       "evtid-lvm-pd-check-term": evtid_lvm_pd_check_term,
       "evtid-jbod-lvm-pd-check-started": evtid_jbod_lvm_pd_check_started,
       "evtid-jbod-lvm-pd-check-completed": evtid_jbod_lvm_pd_check_completed,
       "evtid-jbod-lvm-pd-check-term": evtid_jbod_lvm_pd_check_term,
       "evtid-lvm-scrub-recovered-data": evtid_lvm_scrub_recovered_data,
       "evtid-lvm-scrub-parity-recovered": evtid_lvm_scrub_parity_recovered,
       "evtid-lvm-udv-scrub-aborted": evtid_lvm_udv_scrub_aborted,
       "evtid-lvm-snap-clear-space": evtid_lvm_snap_clear_space,
       "evtid-lvm-large-vg-created": evtid_lvm_large_vg_created,
       "evtid-lvm-weak-vg-created": evtid_lvm_weak_vg_created,
       "evtid-lvm-vg-size-shrunk": evtid_lvm_vg_size_shrunk,
       "evtid-lvm-udv-clone-started": evtid_lvm_udv_clone_started,
       "evtid-lvm-udv-clone-finished": evtid_lvm_udv_clone_finished,
       "evtid-lvm-udv-clone-failed": evtid_lvm_udv_clone_failed,
       "evtid-lvm-udv-clone-aborted": evtid_lvm_udv_clone_aborted,
       "evtid-lvm-udv-replicate-started": evtid_lvm_udv_replicate_started,
       "evtid-lvm-udv-replicate-finished": evtid_lvm_udv_replicate_finished,
       "evtid-lvm-udv-replicate-failed": evtid_lvm_udv_replicate_failed,
       "evtid-lvm-udv-replicate-aborted": evtid_lvm_udv_replicate_aborted,
       "evtid-lvm-udv-erase-finished": evtid_lvm_udv_erase_finished,
       "evtid-lvm-udv-erase-failed": evtid_lvm_udv_erase_failed,
       "evtid-lvm-udv-erase-started": evtid_lvm_udv_erase_started,
       "evtid-lvm-udv-set-as-replica": evtid_lvm_udv_set_as_replica,
       "evtid-lvm-udv-set-as-raid": evtid_lvm_udv_set_as_raid,
       "evtid-lvm-udv-replica-set": evtid_lvm_udv_replica_set,
       "evtid-lvm-udv-replica-reset": evtid_lvm_udv_replica_reset,
       "evtid-lvm-udv-clone-set": evtid_lvm_udv_clone_set,
       "evtid-lvm-udv-clone-reset": evtid_lvm_udv_clone_reset,
       "evtid-lvm-src-replicate-started": evtid_lvm_src_replicate_started,
       "evtid-lvm-src-replicate-finished": evtid_lvm_src_replicate_finished,
       "evtid-lvm-src-replicate-failed": evtid_lvm_src_replicate_failed,
       "evtid-lvm-src-replicate-aborted": evtid_lvm_src_replicate_aborted,
       "evtid-lvm-vg-disk-missing": evtid_lvm_vg_disk_missing,
       "evtid-lvm-pd-rps-started-l2l": evtid_lvm_pd_rps_started_l2l,
       "evtid-lvm-pd-rps-started-l2f": evtid_lvm_pd_rps_started_l2f,
       "evtid-lvm-pd-rps-started-f2l": evtid_lvm_pd_rps_started_f2l,
       "evtid-lvm-pd-rps-started-f2f": evtid_lvm_pd_rps_started_f2f,
       "evtid-lvm-pd-rps-finished-l2l": evtid_lvm_pd_rps_finished_l2l,
       "evtid-lvm-pd-rps-finished-l2f": evtid_lvm_pd_rps_finished_l2f,
       "evtid-lvm-pd-rps-finished-f2l": evtid_lvm_pd_rps_finished_f2l,
       "evtid-lvm-pd-rps-finished-f2f": evtid_lvm_pd_rps_finished_f2f,
       "evtid-lvm-pd-rps-failed-l2l": evtid_lvm_pd_rps_failed_l2l,
       "evtid-lvm-pd-rps-failed-l2f": evtid_lvm_pd_rps_failed_l2f,
       "evtid-lvm-pd-rps-failed-f2l": evtid_lvm_pd_rps_failed_f2l,
       "evtid-lvm-pd-rps-failed-f2f": evtid_lvm_pd_rps_failed_f2f,
       "evtid-lvm-l-pd-udv-rewr-fault": evtid_lvm_l_pd_udv_rewr_fault,
       "evtid-lvm-f-pd-udv-rewr-fault": evtid_lvm_f_pd_udv_rewr_fault,
       "evtid-lvm-l-pd-io-retry-fault": evtid_lvm_l_pd_io_retry_fault,
       "evtid-lvm-f-pd-io-retry-fault": evtid_lvm_f_pd_io_retry_fault,
       "evtid-lvm-pd-substitute-l2l": evtid_lvm_pd_substitute_l2l,
       "evtid-lvm-pd-substitute-l2f": evtid_lvm_pd_substitute_l2f,
       "evtid-lvm-pd-substitute-f2l": evtid_lvm_pd_substitute_f2l,
       "evtid-lvm-pd-substitute-f2f": evtid_lvm_pd_substitute_f2f,
       "evtid-lvm-vg-threshold-hit": evtid_lvm_vg_threshold_hit,
       "evtid-lvm-raid-set-created": evtid_lvm_raid_set_created,
       "evtid-lvm-raid-set-deleted": evtid_lvm_raid_set_deleted,
       "evtid-lvm-udv-reclaim-started": evtid_lvm_udv_reclaim_started,
       "evtid-lvm-udv-reclaim-completed": evtid_lvm_udv_reclaim_completed,
       "evtid-lvm-udv-reclaim-aborted": evtid_lvm_udv_reclaim_aborted,
       "evtid-hac-ctr-inserted": evtid_hac_ctr_inserted,
       "evtid-hac-ctr-removed": evtid_hac_ctr_removed,
       "evtid-hac-ctr-timeout": evtid_hac_ctr_timeout,
       "evtid-hac-ctr-lockdown": evtid_hac_ctr_lockdown,
       "evtid-hac-ctr-failover": evtid_hac_ctr_failover,
       "evtid-hac-ctr-reset": evtid_hac_ctr_reset,
       "evtid-hac-ctr-memory-ng": evtid_hac_ctr_memory_ng,
       "evtid-hac-ctr-firmware-ng": evtid_hac_ctr_firmware_ng,
       "evtid-hac-ctr-lowspeed-ng": evtid_hac_ctr_lowspeed_ng,
       "evtid-hac-ctr-highspeed-ng": evtid_hac_ctr_highspeed_ng,
       "evtid-hac-ctr-be-ng": evtid_hac_ctr_be_ng,
       "evtid-hac-ctr-fe-ng": evtid_hac_ctr_fe_ng,
       "evtid-hac-jbod-hdd-path-ng": evtid_hac_jbod_hdd_path_ng,
       "evtid-rms-console-login": evtid_rms_console_login,
       "evtid-rms-console-logout": evtid_rms_console_logout,
       "evtid-rms-web-login": evtid_rms_web_login,
       "evtid-rms-web-logout": evtid_rms_web_logout,
       "evtid-rms-log-clear": evtid_rms_log_clear,
       "evtid-sys-shutdown": evtid_sys_shutdown,
       "evtid-sys-reboot": evtid_sys_reboot,
       "evtid-fw-upgrade-start": evtid_fw_upgrade_start,
       "evtid-fw-upgrade-success": evtid_fw_upgrade_success,
       "evtid-fw-upgrade-failure": evtid_fw_upgrade_failure,
       "evtid-ipc-fw-upgrade-timeout": evtid_ipc_fw_upgrade_timeout,
       "evtid-sys-console-shutdown": evtid_sys_console_shutdown,
       "evtid-sys-web-shutdown": evtid_sys_web_shutdown,
       "evtid-sys-btn-shutdown": evtid_sys_btn_shutdown,
       "evtid-sys-console-reboot": evtid_sys_console_reboot,
       "evtid-sys-web-reboot": evtid_sys_web_reboot,
       "evtid-sys-lcm-shutdown": evtid_sys_lcm_shutdown,
       "evtid-sys-lcm-reboot": evtid_sys_lcm_reboot,
       "evtid-ctr-reboot-fwsync": evtid_ctr_reboot_fwsync,
       "evtid-auto-qrep-not-enable": evtid_auto_qrep_not_enable,
       "evtid-auto-qrep-err": evtid_auto_qrep_err,
       "evtid-auto-qrep-no-snap": evtid_auto_qrep_no_snap,
       "evtid-auto-clone-err": evtid_auto_clone_err,
       "evtid-auto-clone-no-snap": evtid_auto_clone_no_snap,
       "evtid-qrep-portal-enabled": evtid_qrep_portal_enabled,
       "evtid-qrep-portal-disabled": evtid_qrep_portal_disabled,
       "evtid-send-mail-fail": evtid_send_mail_fail,
       "evtid-config-imported": evtid_config_imported,
       "eventString": eventString}
)
