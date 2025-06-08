# SNMP MIB module (ACCEDIAN-SKYLIGHT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/accedian_22420/ACCEDIAN-SKYLIGHT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 15:07:59 2025
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

accedian = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22545)
)
if mibBuilder.loadTexts:
    accedian.setRevisions(
        ("2017-02-20 05:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_It_product_line_ObjectIdentity = ObjectIdentity
it_product_line = _It_product_line_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2)
)
_OperationCenter_ObjectIdentity = ObjectIdentity
operationCenter = _OperationCenter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("current")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "ACCEDIAN-SKYLIGHT-MIB", "alarm_sn"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("current")
_Alarm_sn_Type = Integer32
_Alarm_sn_Object = MibTableColumn
alarm_sn = _Alarm_sn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 1),
    _Alarm_sn_Type()
)
alarm_sn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_sn.setStatus("current")
_Alarm_id_Type = DisplayString
_Alarm_id_Object = MibTableColumn
alarm_id = _Alarm_id_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 2),
    _Alarm_id_Type()
)
alarm_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_id.setStatus("current")
_Alarm_name_Type = DisplayString
_Alarm_name_Object = MibTableColumn
alarm_name = _Alarm_name_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 3),
    _Alarm_name_Type()
)
alarm_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_name.setStatus("current")
_Severity_Type = Integer32
_Severity_Object = MibTableColumn
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 4),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_First_report_time_Type = DisplayString
_First_report_time_Object = MibTableColumn
first_report_time = _First_report_time_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 5),
    _First_report_time_Type()
)
first_report_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    first_report_time.setStatus("current")
_Last_report_time_Type = DisplayString
_Last_report_time_Object = MibTableColumn
last_report_time = _Last_report_time_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 6),
    _Last_report_time_Type()
)
last_report_time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    last_report_time.setStatus("current")
_Occur_times_Type = Integer32
_Occur_times_Object = MibTableColumn
occur_times = _Occur_times_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 7),
    _Occur_times_Type()
)
occur_times.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    occur_times.setStatus("current")
_Object_code_Type = DisplayString
_Object_code_Object = MibTableColumn
object_code = _Object_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 8),
    _Object_code_Type()
)
object_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    object_code.setStatus("current")
_Model_Type = DisplayString
_Model_Object = MibTableColumn
model = _Model_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 9),
    _Model_Type()
)
model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    model.setStatus("current")
_Object_name_Type = DisplayString
_Object_name_Object = MibTableColumn
object_name = _Object_name_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 10),
    _Object_name_Type()
)
object_name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    object_name.setStatus("current")
_Object_ciid_Type = DisplayString
_Object_ciid_Object = MibTableColumn
object_ciid = _Object_ciid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 15),
    _Object_ciid_Type()
)
object_ciid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    object_ciid.setStatus("current")
_Zone_code_Type = DisplayString
_Zone_code_Object = MibTableColumn
zone_code = _Zone_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 18),
    _Zone_code_Type()
)
zone_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zone_code.setStatus("current")
_Customer_code_Type = DisplayString
_Customer_code_Object = MibTableColumn
customer_code = _Customer_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 19),
    _Customer_code_Type()
)
customer_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customer_code.setStatus("current")
_Data_center_code_Type = DisplayString
_Data_center_code_Object = MibTableColumn
data_center_code = _Data_center_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 20),
    _Data_center_code_Type()
)
data_center_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    data_center_code.setStatus("current")
_Cluster_code_Type = DisplayString
_Cluster_code_Object = MibTableColumn
cluster_code = _Cluster_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 21),
    _Cluster_code_Type()
)
cluster_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cluster_code.setStatus("current")
_Machine_room_code_Type = DisplayString
_Machine_room_code_Object = MibTableColumn
machine_room_code = _Machine_room_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 22),
    _Machine_room_code_Type()
)
machine_room_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    machine_room_code.setStatus("current")
_Pool_mag_code_Type = DisplayString
_Pool_mag_code_Object = MibTableColumn
pool_mag_code = _Pool_mag_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 23),
    _Pool_mag_code_Type()
)
pool_mag_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pool_mag_code.setStatus("current")
_Alarm_monitor_sys_code_Type = DisplayString
_Alarm_monitor_sys_code_Object = MibTableColumn
alarm_monitor_sys_code = _Alarm_monitor_sys_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 24),
    _Alarm_monitor_sys_code_Type()
)
alarm_monitor_sys_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm_monitor_sys_code.setStatus("current")
_Perf_monitor_sys_code_Type = DisplayString
_Perf_monitor_sys_code_Object = MibTableColumn
perf_monitor_sys_code = _Perf_monitor_sys_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 25),
    _Perf_monitor_sys_code_Type()
)
perf_monitor_sys_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    perf_monitor_sys_code.setStatus("current")
_Service_group_code_Type = DisplayString
_Service_group_code_Object = MibTableColumn
service_group_code = _Service_group_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 26),
    _Service_group_code_Type()
)
service_group_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    service_group_code.setStatus("current")
_User_define_attr1_Type = DisplayString
_User_define_attr1_Object = MibTableColumn
user_define_attr1 = _User_define_attr1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 27),
    _User_define_attr1_Type()
)
user_define_attr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user_define_attr1.setStatus("current")
_User_define_attr2_Type = DisplayString
_User_define_attr2_Object = MibTableColumn
user_define_attr2 = _User_define_attr2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 28),
    _User_define_attr2_Type()
)
user_define_attr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    user_define_attr2.setStatus("current")
_Province_code_Type = DisplayString
_Province_code_Object = MibTableColumn
province_code = _Province_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 29),
    _Province_code_Type()
)
province_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    province_code.setStatus("current")
_Logic_zone_code_Type = DisplayString
_Logic_zone_code_Object = MibTableColumn
logic_zone_code = _Logic_zone_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 31),
    _Logic_zone_code_Type()
)
logic_zone_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logic_zone_code.setStatus("current")
_Phydc_code_Type = DisplayString
_Phydc_code_Object = MibTableColumn
phydc_code = _Phydc_code_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 32),
    _Phydc_code_Type()
)
phydc_code.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    phydc_code.setStatus("current")
_Object_type1_Type = DisplayString
_Object_type1_Object = MibTableColumn
object_type1 = _Object_type1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 34),
    _Object_type1_Type()
)
object_type1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    object_type1.setStatus("current")
_Object_type_Type = DisplayString
_Object_type_Object = MibTableColumn
object_type = _Object_type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 35),
    _Object_type_Type()
)
object_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    object_type.setStatus("current")
_Old_additional_Type = DisplayString
_Old_additional_Object = MibTableColumn
old_additional = _Old_additional_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 36),
    _Old_additional_Type()
)
old_additional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    old_additional.setStatus("current")
_Remark_Type = DisplayString
_Remark_Object = MibTableColumn
remark = _Remark_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 37),
    _Remark_Type()
)
remark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remark.setStatus("current")
_Manufacturer_Type = DisplayString
_Manufacturer_Object = MibTableColumn
manufacturer = _Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 52),
    _Manufacturer_Type()
)
manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    manufacturer.setStatus("current")
_Old_alarm_source_obj_ip_Type = DisplayString
_Old_alarm_source_obj_ip_Object = MibTableColumn
old_alarm_source_obj_ip = _Old_alarm_source_obj_ip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 56),
    _Old_alarm_source_obj_ip_Type()
)
old_alarm_source_obj_ip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    old_alarm_source_obj_ip.setStatus("current")
_Old_alarm_reason_Type = DisplayString
_Old_alarm_reason_Object = MibTableColumn
old_alarm_reason = _Old_alarm_reason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 60),
    _Old_alarm_reason_Type()
)
old_alarm_reason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    old_alarm_reason.setStatus("current")
_Old_reason_located_info_Type = DisplayString
_Old_reason_located_info_Object = MibTableColumn
old_reason_located_info = _Old_reason_located_info_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 61),
    _Old_reason_located_info_Type()
)
old_reason_located_info.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    old_reason_located_info.setStatus("current")
_Type_Type = Integer32
_Type_Object = MibTableColumn
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 62),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("current")
_Old_alarm_id_Type = DisplayString
_Old_alarm_id_Object = MibTableColumn
old_alarm_id = _Old_alarm_id_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 1, 1, 63),
    _Old_alarm_id_Type()
)
old_alarm_id.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    old_alarm_id.setStatus("current")

# Managed Objects groups


# Notification objects

AlarmMOne = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 288, 100)
)
AlarmMOne.setObjects(
      *(("ACCEDIAN-SKYLIGHT-MIB", "alarm_sn"),
        ("ACCEDIAN-SKYLIGHT-MIB", "alarm_id"),
        ("ACCEDIAN-SKYLIGHT-MIB", "alarm_name"),
        ("ACCEDIAN-SKYLIGHT-MIB", "severity"),
        ("ACCEDIAN-SKYLIGHT-MIB", "first_report_time"),
        ("ACCEDIAN-SKYLIGHT-MIB", "last_report_time"),
        ("ACCEDIAN-SKYLIGHT-MIB", "occur_times"),
        ("ACCEDIAN-SKYLIGHT-MIB", "object_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "model"),
        ("ACCEDIAN-SKYLIGHT-MIB", "object_name"),
        ("ACCEDIAN-SKYLIGHT-MIB", "object_ciid"),
        ("ACCEDIAN-SKYLIGHT-MIB", "zone_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "customer_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "data_center_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "cluster_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "machine_room_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "pool_mag_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "alarm_monitor_sys_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "perf_monitor_sys_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "service_group_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "user_define_attr1"),
        ("ACCEDIAN-SKYLIGHT-MIB", "user_define_attr2"),
        ("ACCEDIAN-SKYLIGHT-MIB", "province_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "logic_zone_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "phydc_code"),
        ("ACCEDIAN-SKYLIGHT-MIB", "object_type1"),
        ("ACCEDIAN-SKYLIGHT-MIB", "object_type"),
        ("ACCEDIAN-SKYLIGHT-MIB", "old_additional"),
        ("ACCEDIAN-SKYLIGHT-MIB", "remark"),
        ("ACCEDIAN-SKYLIGHT-MIB", "manufacturer"),
        ("ACCEDIAN-SKYLIGHT-MIB", "old_alarm_source_obj_ip"),
        ("ACCEDIAN-SKYLIGHT-MIB", "old_alarm_reason"),
        ("ACCEDIAN-SKYLIGHT-MIB", "old_reason_located_info"),
        ("ACCEDIAN-SKYLIGHT-MIB", "type"),
        ("ACCEDIAN-SKYLIGHT-MIB", "old_alarm_id"))
)
if mibBuilder.loadTexts:
    AlarmMOne.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACCEDIAN-SKYLIGHT-MIB",
    **{"huawei": huawei,
       "it_product_line": it_product_line,
       "operationCenter": operationCenter,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarm_sn": alarm_sn,
       "alarm_id": alarm_id,
       "alarm_name": alarm_name,
       "severity": severity,
       "first_report_time": first_report_time,
       "last_report_time": last_report_time,
       "occur_times": occur_times,
       "object_code": object_code,
       "model": model,
       "object_name": object_name,
       "object_ciid": object_ciid,
       "zone_code": zone_code,
       "customer_code": customer_code,
       "data_center_code": data_center_code,
       "cluster_code": cluster_code,
       "machine_room_code": machine_room_code,
       "pool_mag_code": pool_mag_code,
       "alarm_monitor_sys_code": alarm_monitor_sys_code,
       "perf_monitor_sys_code": perf_monitor_sys_code,
       "service_group_code": service_group_code,
       "user_define_attr1": user_define_attr1,
       "user_define_attr2": user_define_attr2,
       "province_code": province_code,
       "logic_zone_code": logic_zone_code,
       "phydc_code": phydc_code,
       "object_type1": object_type1,
       "object_type": object_type,
       "old_additional": old_additional,
       "remark": remark,
       "manufacturer": manufacturer,
       "old_alarm_source_obj_ip": old_alarm_source_obj_ip,
       "old_alarm_reason": old_alarm_reason,
       "old_reason_located_info": old_reason_located_info,
       "type": type,
       "old_alarm_id": old_alarm_id,
       "AlarmMOne": AlarmMOne,
       "accedian": accedian}
)
