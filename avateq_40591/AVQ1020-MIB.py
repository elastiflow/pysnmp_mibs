# SNMP MIB module (AVQ1020-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/avateq_40591/AVQ1020-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:40:05 2025
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

avq = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 40591)
)
if mibBuilder.loadTexts:
    avq.setRevisions(
        ("2014-07-08 10:55",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Receiver_ObjectIdentity = ObjectIdentity
receiver = _Receiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020)
)
_Receiver_1_ObjectIdentity = ObjectIdentity
receiver_1 = _Receiver_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1)
)
_ReceiverTable_Object = MibTable
receiverTable = _ReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1)
)
if mibBuilder.loadTexts:
    receiverTable.setStatus("current")
_AvqTraps_ObjectIdentity = ObjectIdentity
avqTraps = _AvqTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0)
)
_AvqObjs_ObjectIdentity = ObjectIdentity
avqObjs = _AvqObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0)
)


class _AvqSiteId_Type(DisplayString):
    """Custom type avqSiteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvqSiteId_Type.__name__ = "DisplayString"
_AvqSiteId_Object = MibScalar
avqSiteId = _AvqSiteId_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0, 1),
    _AvqSiteId_Type()
)
avqSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avqSiteId.setStatus("current")


class _AvqAlarmGroupId_Type(Integer32):
    """Custom type avqAlarmGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gID-System", 0),
          ("gID-HB", 1),
          ("gID-LB", 2))
    )


_AvqAlarmGroupId_Type.__name__ = "Integer32"
_AvqAlarmGroupId_Object = MibScalar
avqAlarmGroupId = _AvqAlarmGroupId_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0, 2),
    _AvqAlarmGroupId_Type()
)
avqAlarmGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avqAlarmGroupId.setStatus("current")


class _AvqAlarmSeverityLevel_Type(Integer32):
    """Custom type avqAlarmSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("indeterminated", 1),
          ("informational", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_AvqAlarmSeverityLevel_Type.__name__ = "Integer32"
_AvqAlarmSeverityLevel_Object = MibScalar
avqAlarmSeverityLevel = _AvqAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0, 3),
    _AvqAlarmSeverityLevel_Type()
)
avqAlarmSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avqAlarmSeverityLevel.setStatus("current")
_AvqTrapNumber_Type = Integer32
_AvqTrapNumber_Object = MibScalar
avqTrapNumber = _AvqTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0, 4),
    _AvqTrapNumber_Type()
)
avqTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avqTrapNumber.setStatus("current")


class _AvqParameterName_Type(DisplayString):
    """Custom type avqParameterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvqParameterName_Type.__name__ = "DisplayString"
_AvqParameterName_Object = MibScalar
avqParameterName = _AvqParameterName_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0, 5),
    _AvqParameterName_Type()
)
avqParameterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avqParameterName.setStatus("current")


class _AvqParameterOID_Type(DisplayString):
    """Custom type avqParameterOID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvqParameterOID_Type.__name__ = "DisplayString"
_AvqParameterOID_Object = MibScalar
avqParameterOID = _AvqParameterOID_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0, 6),
    _AvqParameterOID_Type()
)
avqParameterOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avqParameterOID.setStatus("current")


class _AvqParameterValue_Type(DisplayString):
    """Custom type avqParameterValue based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvqParameterValue_Type.__name__ = "DisplayString"
_AvqParameterValue_Object = MibScalar
avqParameterValue = _AvqParameterValue_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0, 7),
    _AvqParameterValue_Type()
)
avqParameterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avqParameterValue.setStatus("current")


class _AvqUTCTimestamp_Type(DisplayString):
    """Custom type avqUTCTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvqUTCTimestamp_Type.__name__ = "DisplayString"
_AvqUTCTimestamp_Object = MibScalar
avqUTCTimestamp = _AvqUTCTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 0, 8),
    _AvqUTCTimestamp_Type()
)
avqUTCTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avqUTCTimestamp.setStatus("current")
_AvqTraps_Info_ObjectIdentity = ObjectIdentity
avqTraps_Info = _AvqTraps_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1)
)
_AvqTraps_Traps_ObjectIdentity = ObjectIdentity
avqTraps_Traps = _AvqTraps_Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1)
)
_ReceiverEntry_Object = MibTableRow
receiverEntry = _ReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1)
)
receiverEntry.setIndexNames(
    (0, "AVQ1020-MIB", "x1-Alarm-Entry-Index"),
)
if mibBuilder.loadTexts:
    receiverEntry.setStatus("current")
_Global_Status_Info_ObjectIdentity = ObjectIdentity
global_Status_Info = _Global_Status_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1)
)
_Status_Info_ObjectIdentity = ObjectIdentity
status_Info = _Status_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 1)
)
_Alarms_Info_ObjectIdentity = ObjectIdentity
alarms_Info = _Alarms_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 2)
)
_Standard_and_central_frequency_Info_ObjectIdentity = ObjectIdentity
standard_and_central_frequency_Info = _Standard_and_central_frequency_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 3)
)
_Spectral_Info_ObjectIdentity = ObjectIdentity
spectral_Info = _Spectral_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 4)
)
_Quality_Info_ObjectIdentity = ObjectIdentity
quality_Info = _Quality_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 5)
)
_Options_Info_ObjectIdentity = ObjectIdentity
options_Info = _Options_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 6)
)
_Reference_and_timing_Info_ObjectIdentity = ObjectIdentity
reference_and_timing_Info = _Reference_and_timing_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 7)
)
_Network_Info_ObjectIdentity = ObjectIdentity
network_Info = _Network_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 8)
)
_HW_Status_Info_ObjectIdentity = ObjectIdentity
hW_Status_Info = _HW_Status_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 9)
)
_Versions_and_Serial_Numbers_Info_ObjectIdentity = ObjectIdentity
versions_and_Serial_Numbers_Info = _Versions_and_Serial_Numbers_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 1, 10)
)


class _X1_Alarm_Entry_Index_Type(Integer32):
    """Custom type x1_Alarm_Entry_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_X1_Alarm_Entry_Index_Type.__name__ = "Integer32"
_X1_Alarm_Entry_Index_Object = MibTableColumn
x1_Alarm_Entry_Index = _X1_Alarm_Entry_Index_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 5125),
    _X1_Alarm_Entry_Index_Type()
)
x1_Alarm_Entry_Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x1_Alarm_Entry_Index.setStatus("current")


class _X1_Trap_Notification_on_Alarm_Type(Integer32):
    """Custom type x1_Trap_Notification_on_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 0),
          ("oN", 1))
    )


_X1_Trap_Notification_on_Alarm_Type.__name__ = "Integer32"
_X1_Trap_Notification_on_Alarm_Object = MibTableColumn
x1_Trap_Notification_on_Alarm = _X1_Trap_Notification_on_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 5637),
    _X1_Trap_Notification_on_Alarm_Type()
)
x1_Trap_Notification_on_Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x1_Trap_Notification_on_Alarm.setStatus("current")


class _X1_Email_Notification_on_Alarm_Type(Integer32):
    """Custom type x1_Email_Notification_on_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 0),
          ("oN", 1))
    )


_X1_Email_Notification_on_Alarm_Type.__name__ = "Integer32"
_X1_Email_Notification_on_Alarm_Object = MibTableColumn
x1_Email_Notification_on_Alarm = _X1_Email_Notification_on_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 5893),
    _X1_Email_Notification_on_Alarm_Type()
)
x1_Email_Notification_on_Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x1_Email_Notification_on_Alarm.setStatus("current")
_X1_Integration_Time_Type = Integer32
_X1_Integration_Time_Object = MibTableColumn
x1_Integration_Time = _X1_Integration_Time_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 7429),
    _X1_Integration_Time_Type()
)
x1_Integration_Time.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x1_Integration_Time.setStatus("current")


class _X1_Alarm_Severity_Level_Type(Integer32):
    """Custom type x1_Alarm_Severity_Level based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("indetermnated", 1),
          ("informational", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_X1_Alarm_Severity_Level_Type.__name__ = "Integer32"
_X1_Alarm_Severity_Level_Object = MibTableColumn
x1_Alarm_Severity_Level = _X1_Alarm_Severity_Level_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 7685),
    _X1_Alarm_Severity_Level_Type()
)
x1_Alarm_Severity_Level.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x1_Alarm_Severity_Level.setStatus("current")
_Status_Active_Alarms_Type = Integer32
_Status_Active_Alarms_Object = MibScalar
status_Active_Alarms = _Status_Active_Alarms_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 7941),
    _Status_Active_Alarms_Type()
)
status_Active_Alarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Active_Alarms.setStatus("current")


class _X1_Relay1_on_Alarm_Type(Integer32):
    """Custom type x1_Relay1_on_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 0),
          ("oN", 1))
    )


_X1_Relay1_on_Alarm_Type.__name__ = "Integer32"
_X1_Relay1_on_Alarm_Object = MibTableColumn
x1_Relay1_on_Alarm = _X1_Relay1_on_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18445),
    _X1_Relay1_on_Alarm_Type()
)
x1_Relay1_on_Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x1_Relay1_on_Alarm.setStatus("current")


class _X1_Relay2_on_Alarm_Type(Integer32):
    """Custom type x1_Relay2_on_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 0),
          ("oN", 1))
    )


_X1_Relay2_on_Alarm_Type.__name__ = "Integer32"
_X1_Relay2_on_Alarm_Object = MibTableColumn
x1_Relay2_on_Alarm = _X1_Relay2_on_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18701),
    _X1_Relay2_on_Alarm_Type()
)
x1_Relay2_on_Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x1_Relay2_on_Alarm.setStatus("current")
_Status_CPU_Temperature_Current_Type = Integer32
_Status_CPU_Temperature_Current_Object = MibScalar
status_CPU_Temperature_Current = _Status_CPU_Temperature_Current_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18720),
    _Status_CPU_Temperature_Current_Type()
)
status_CPU_Temperature_Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_CPU_Temperature_Current.setStatus("current")
_Status_FPGA_Temperature_Current_Type = Integer32
_Status_FPGA_Temperature_Current_Object = MibScalar
status_FPGA_Temperature_Current = _Status_FPGA_Temperature_Current_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18736),
    _Status_FPGA_Temperature_Current_Type()
)
status_FPGA_Temperature_Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_FPGA_Temperature_Current.setStatus("current")
_Status_Case_Temperature_Current_Type = Integer32
_Status_Case_Temperature_Current_Object = MibScalar
status_Case_Temperature_Current = _Status_Case_Temperature_Current_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18752),
    _Status_Case_Temperature_Current_Type()
)
status_Case_Temperature_Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Case_Temperature_Current.setStatus("current")


class _Status_Temperature_Fault_Type(Integer32):
    """Custom type status_Temperature_Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nO", 0),
          ("yES", 1))
    )


_Status_Temperature_Fault_Type.__name__ = "Integer32"
_Status_Temperature_Fault_Object = MibScalar
status_Temperature_Fault = _Status_Temperature_Fault_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18758),
    _Status_Temperature_Fault_Type()
)
status_Temperature_Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Temperature_Fault.setStatus("current")


class _Status_RF_Board_Fault_Type(Integer32):
    """Custom type status_RF_Board_Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nO", 0),
          ("yES", 1))
    )


_Status_RF_Board_Fault_Type.__name__ = "Integer32"
_Status_RF_Board_Fault_Object = MibScalar
status_RF_Board_Fault = _Status_RF_Board_Fault_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18759),
    _Status_RF_Board_Fault_Type()
)
status_RF_Board_Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_RF_Board_Fault.setStatus("current")


class _Status_HW_Fault_Type(Integer32):
    """Custom type status_HW_Fault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nO", 0),
          ("yES", 1))
    )


_Status_HW_Fault_Type.__name__ = "Integer32"
_Status_HW_Fault_Object = MibScalar
status_HW_Fault = _Status_HW_Fault_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18760),
    _Status_HW_Fault_Type()
)
status_HW_Fault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_HW_Fault.setStatus("current")
_Status_App_Revision_Type = Integer32
_Status_App_Revision_Object = MibScalar
status_App_Revision = _Status_App_Revision_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18813),
    _Status_App_Revision_Type()
)
status_App_Revision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_App_Revision.setStatus("current")
_Status_App_Version_Type = Integer32
_Status_App_Version_Object = MibScalar
status_App_Version = _Status_App_Version_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 18814),
    _Status_App_Version_Type()
)
status_App_Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_App_Version.setStatus("current")
_Status_App_Build_Date_Type = Integer32
_Status_App_Build_Date_Object = MibScalar
status_App_Build_Date = _Status_App_Build_Date_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 20477),
    _Status_App_Build_Date_Type()
)
status_App_Build_Date.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_App_Build_Date.setStatus("current")
_Status_Eth0_IP_Address_Type = Integer32
_Status_Eth0_IP_Address_Object = MibScalar
status_Eth0_IP_Address = _Status_Eth0_IP_Address_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 24581),
    _Status_Eth0_IP_Address_Type()
)
status_Eth0_IP_Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Eth0_IP_Address.setStatus("current")
_Status_Eth0_Gateway_Type = Integer32
_Status_Eth0_Gateway_Object = MibScalar
status_Eth0_Gateway = _Status_Eth0_Gateway_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 25093),
    _Status_Eth0_Gateway_Type()
)
status_Eth0_Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Eth0_Gateway.setStatus("current")
_Status_Eth0_Netmask_Type = Integer32
_Status_Eth0_Netmask_Object = MibScalar
status_Eth0_Netmask = _Status_Eth0_Netmask_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 25605),
    _Status_Eth0_Netmask_Type()
)
status_Eth0_Netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Eth0_Netmask.setStatus("current")
_Status_DNS_Server_Type = Integer32
_Status_DNS_Server_Object = MibScalar
status_DNS_Server = _Status_DNS_Server_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 25606),
    _Status_DNS_Server_Type()
)
status_DNS_Server.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_DNS_Server.setStatus("current")
_Status_Serial_Number_Type = Integer32
_Status_Serial_Number_Object = MibScalar
status_Serial_Number = _Status_Serial_Number_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 32261),
    _Status_Serial_Number_Type()
)
status_Serial_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Serial_Number.setStatus("current")
_Status_Eth0_Mac_Address_Type = Integer32
_Status_Eth0_Mac_Address_Object = MibScalar
status_Eth0_Mac_Address = _Status_Eth0_Mac_Address_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 38917),
    _Status_Eth0_Mac_Address_Type()
)
status_Eth0_Mac_Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Eth0_Mac_Address.setStatus("current")
_Status_OS_kernel_Type = Integer32
_Status_OS_kernel_Object = MibScalar
status_OS_kernel = _Status_OS_kernel_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 49496),
    _Status_OS_kernel_Type()
)
status_OS_kernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_OS_kernel.setStatus("current")
_Status_FPGA_ver_Type = Integer32
_Status_FPGA_ver_Object = MibScalar
status_FPGA_ver = _Status_FPGA_ver_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 49560),
    _Status_FPGA_ver_Type()
)
status_FPGA_ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_FPGA_ver.setStatus("current")
_Status_Firmware_ver_Type = Integer32
_Status_Firmware_ver_Object = MibScalar
status_Firmware_ver = _Status_Firmware_ver_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57352),
    _Status_Firmware_ver_Type()
)
status_Firmware_ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Firmware_ver.setStatus("current")
_Status_Library_ver_Type = Integer32
_Status_Library_ver_Object = MibScalar
status_Library_ver = _Status_Library_ver_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57368),
    _Status_Library_ver_Type()
)
status_Library_ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Library_ver.setStatus("current")


class _Status_Standard_Type(Integer32):
    """Custom type status_Standard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("dVB-TH", 1),
          ("aTSC", 2),
          ("dAB", 3),
          ("dTMB", 4),
          ("iSDB-T", 5),
          ("cMMB", 6),
          ("dVB-T2", 7),
          ("dVB-S-S2", 8),
          ("aTSC3-0", 9))
    )


_Status_Standard_Type.__name__ = "Integer32"
_Status_Standard_Object = MibScalar
status_Standard = _Status_Standard_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57384),
    _Status_Standard_Type()
)
status_Standard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Standard.setStatus("current")
_Status_Central_Freq_Hz_Type = Integer32
_Status_Central_Freq_Hz_Object = MibScalar
status_Central_Freq_Hz = _Status_Central_Freq_Hz_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57416),
    _Status_Central_Freq_Hz_Type()
)
status_Central_Freq_Hz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Central_Freq_Hz.setStatus("current")


class _Status_Status_Type(Integer32):
    """Custom type status_Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("not-Initialized", 0),
          ("not-Ready", 1),
          ("idle", 2),
          ("processing", 3),
          ("cancelling", 4),
          ("invalid", 5))
    )


_Status_Status_Type.__name__ = "Integer32"
_Status_Status_Object = MibScalar
status_Status = _Status_Status_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57464),
    _Status_Status_Type()
)
status_Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Status.setStatus("current")


class _Status_Last_error_Type(Integer32):
    """Custom type status_Last_error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("no-errors", 0),
          ("generic-error", 1),
          ("not-supported", 2),
          ("not-available", 3),
          ("invalid-param", 4),
          ("no-lock", 5),
          ("out-of-memory", 6),
          ("not-licensed", 7),
          ("low-input-level", 8),
          ("no-valid-signal", 9),
          ("no-valid-MER", 10),
          ("no-1PPS", 11),
          ("no-10MHz", 12),
          ("no-sampling-freq", 13),
          ("cap-timeout", 14),
          ("does-not-exist", 15),
          ("is-not-supported", 16),
          ("msg-format-error", 17),
          ("msg-CS-error", 18),
          ("numerous-errors", 19),
          ("capturing-hardware-error", 20))
    )


_Status_Last_error_Type.__name__ = "Integer32"
_Status_Last_error_Object = MibScalar
status_Last_error = _Status_Last_error_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57480),
    _Status_Last_error_Type()
)
status_Last_error.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Last_error.setStatus("current")
_Status_PAPR_dB_Type = Integer32
_Status_PAPR_dB_Object = MibScalar
status_PAPR_dB = _Status_PAPR_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57512),
    _Status_PAPR_dB_Type()
)
status_PAPR_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_PAPR_dB.setStatus("current")
_Status_Frequency_Shift_Hz_Type = Integer32
_Status_Frequency_Shift_Hz_Object = MibScalar
status_Frequency_Shift_Hz = _Status_Frequency_Shift_Hz_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57544),
    _Status_Frequency_Shift_Hz_Type()
)
status_Frequency_Shift_Hz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Frequency_Shift_Hz.setStatus("current")
_Status_Left_Shoulder_dB_Type = Integer32
_Status_Left_Shoulder_dB_Object = MibScalar
status_Left_Shoulder_dB = _Status_Left_Shoulder_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57560),
    _Status_Left_Shoulder_dB_Type()
)
status_Left_Shoulder_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Left_Shoulder_dB.setStatus("current")
_Status_Right_Shoulder_dB_Type = Integer32
_Status_Right_Shoulder_dB_Object = MibScalar
status_Right_Shoulder_dB = _Status_Right_Shoulder_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57576),
    _Status_Right_Shoulder_dB_Type()
)
status_Right_Shoulder_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Right_Shoulder_dB.setStatus("current")
_Status_Amplitude_Error_dB_Type = Integer32
_Status_Amplitude_Error_dB_Object = MibScalar
status_Amplitude_Error_dB = _Status_Amplitude_Error_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57592),
    _Status_Amplitude_Error_dB_Type()
)
status_Amplitude_Error_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Amplitude_Error_dB.setStatus("current")
_Status_Phase_Error_degree_Type = Integer32
_Status_Phase_Error_degree_Object = MibScalar
status_Phase_Error_degree = _Status_Phase_Error_degree_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57608),
    _Status_Phase_Error_degree_Type()
)
status_Phase_Error_degree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Phase_Error_degree.setStatus("current")
_Status_MER_dB_Type = Integer32
_Status_MER_dB_Object = MibScalar
status_MER_dB = _Status_MER_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57624),
    _Status_MER_dB_Type()
)
status_MER_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_MER_dB.setStatus("current")


class _Status_SFN_Sync_Status_Type(Integer32):
    """Custom type status_SFN_Sync_Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Status_SFN_Sync_Status_Type.__name__ = "Integer32"
_Status_SFN_Sync_Status_Object = MibScalar
status_SFN_Sync_Status = _Status_SFN_Sync_Status_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 57883),
    _Status_SFN_Sync_Status_Type()
)
status_SFN_Sync_Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_SFN_Sync_Status.setStatus("current")
_Status_Residual_GD_Type = Integer32
_Status_Residual_GD_Object = MibScalar
status_Residual_GD = _Status_Residual_GD_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 58456),
    _Status_Residual_GD_Type()
)
status_Residual_GD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Residual_GD.setStatus("current")
_Status_Spectrum_inversion_Type = Integer32
_Status_Spectrum_inversion_Object = MibScalar
status_Spectrum_inversion = _Status_Spectrum_inversion_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 58888),
    _Status_Spectrum_inversion_Type()
)
status_Spectrum_inversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Spectrum_inversion.setStatus("current")


class _Status_Ten_MHz_Reference_Source_Type(Integer32):
    """Custom type status_Ten_MHz_Reference_Source based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("external", 1))
    )


_Status_Ten_MHz_Reference_Source_Type.__name__ = "Integer32"
_Status_Ten_MHz_Reference_Source_Object = MibScalar
status_Ten_MHz_Reference_Source = _Status_Ten_MHz_Reference_Source_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 58904),
    _Status_Ten_MHz_Reference_Source_Type()
)
status_Ten_MHz_Reference_Source.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Ten_MHz_Reference_Source.setStatus("current")
_Status_ADC_Signal_Scale_Percent_Type = Integer32
_Status_ADC_Signal_Scale_Percent_Object = MibScalar
status_ADC_Signal_Scale_Percent = _Status_ADC_Signal_Scale_Percent_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 58937),
    _Status_ADC_Signal_Scale_Percent_Type()
)
status_ADC_Signal_Scale_Percent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_ADC_Signal_Scale_Percent.setStatus("current")
_Status_ADC_clock_error_Hz_Type = Integer32
_Status_ADC_clock_error_Hz_Object = MibScalar
status_ADC_clock_error_Hz = _Status_ADC_clock_error_Hz_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 58938),
    _Status_ADC_clock_error_Hz_Type()
)
status_ADC_clock_error_Hz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_ADC_clock_error_Hz.setStatus("current")
_Status_Sample_Rate_Shift_Hz_Type = Integer32
_Status_Sample_Rate_Shift_Hz_Object = MibScalar
status_Sample_Rate_Shift_Hz = _Status_Sample_Rate_Shift_Hz_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 59032),
    _Status_Sample_Rate_Shift_Hz_Type()
)
status_Sample_Rate_Shift_Hz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Sample_Rate_Shift_Hz.setStatus("current")
_Status_RF_board_firmware_ver_Type = Integer32
_Status_RF_board_firmware_ver_Object = MibScalar
status_RF_board_firmware_ver = _Status_RF_board_firmware_ver_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 60472),
    _Status_RF_board_firmware_ver_Type()
)
status_RF_board_firmware_ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_RF_board_firmware_ver.setStatus("current")
_Status_RF_board_serial_num_Type = Integer32
_Status_RF_board_serial_num_Object = MibScalar
status_RF_board_serial_num = _Status_RF_board_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 60488),
    _Status_RF_board_serial_num_Type()
)
status_RF_board_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_RF_board_serial_num.setStatus("current")
_Status_RF_transceiver_RTOS_ver_Type = Integer32
_Status_RF_transceiver_RTOS_ver_Object = MibScalar
status_RF_transceiver_RTOS_ver = _Status_RF_transceiver_RTOS_ver_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 60504),
    _Status_RF_transceiver_RTOS_ver_Type()
)
status_RF_transceiver_RTOS_ver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_RF_transceiver_RTOS_ver.setStatus("current")
_Status_Input_RF_power_dBm_Type = Integer32
_Status_Input_RF_power_dBm_Object = MibScalar
status_Input_RF_power_dBm = _Status_Input_RF_power_dBm_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 1, 65400),
    _Status_Input_RF_power_dBm_Type()
)
status_Input_RF_power_dBm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status_Input_RF_power_dBm.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2)
)
_Settings_ObjectIdentity = ObjectIdentity
settings = _Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 1)
)
_Site_Info_ObjectIdentity = ObjectIdentity
site_Info = _Site_Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 12)
)
_System_Description_Type = Integer32
_System_Description_Object = MibScalar
system_Description = _System_Description_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 517),
    _System_Description_Type()
)
system_Description.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    system_Description.setStatus("current")
_Contact_Information_Type = Integer32
_Contact_Information_Object = MibScalar
contact_Information = _Contact_Information_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 773),
    _Contact_Information_Type()
)
contact_Information.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact_Information.setStatus("current")
_System_Location_Type = Integer32
_System_Location_Object = MibScalar
system_Location = _System_Location_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 1029),
    _System_Location_Type()
)
system_Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    system_Location.setStatus("current")
_Site_Address_Line_1_Type = Integer32
_Site_Address_Line_1_Object = MibScalar
site_Address_Line_1 = _Site_Address_Line_1_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 1541),
    _Site_Address_Line_1_Type()
)
site_Address_Line_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    site_Address_Line_1.setStatus("current")
_Site_Address_Line_2_Type = Integer32
_Site_Address_Line_2_Object = MibScalar
site_Address_Line_2 = _Site_Address_Line_2_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 1797),
    _Site_Address_Line_2_Type()
)
site_Address_Line_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    site_Address_Line_2.setStatus("current")
_Site_Address_Line_3_Type = Integer32
_Site_Address_Line_3_Object = MibScalar
site_Address_Line_3 = _Site_Address_Line_3_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 2053),
    _Site_Address_Line_3_Type()
)
site_Address_Line_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    site_Address_Line_3.setStatus("current")
_Site_Address_Line_4_Type = Integer32
_Site_Address_Line_4_Object = MibScalar
site_Address_Line_4 = _Site_Address_Line_4_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 2309),
    _Site_Address_Line_4_Type()
)
site_Address_Line_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    site_Address_Line_4.setStatus("current")
_Site_Notes_Type = Integer32
_Site_Notes_Object = MibScalar
site_Notes = _Site_Notes_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 2565),
    _Site_Notes_Type()
)
site_Notes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    site_Notes.setStatus("current")
_Central_Freq_Hz_Type = Integer32
_Central_Freq_Hz_Object = MibScalar
central_Freq_Hz = _Central_Freq_Hz_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 57416),
    _Central_Freq_Hz_Type()
)
central_Freq_Hz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    central_Freq_Hz.setStatus("current")


class _Command_Type(Integer32):
    """Custom type command based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("run", 1),
          ("reset", 2))
    )


_Command_Type.__name__ = "Integer32"
_Command_Object = MibScalar
command = _Command_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 57448),
    _Command_Type()
)
command.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    command.setStatus("current")


class _Equalizer_Type(Integer32):
    """Custom type equalizer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Equalizer_Type.__name__ = "Integer32"
_Equalizer_Object = MibScalar
equalizer = _Equalizer_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 57800),
    _Equalizer_Type()
)
equalizer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    equalizer.setStatus("current")


class _Channel_Filter_Type(Integer32):
    """Custom type channel_Filter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Channel_Filter_Type.__name__ = "Integer32"
_Channel_Filter_Object = MibScalar
channel_Filter = _Channel_Filter_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 57816),
    _Channel_Filter_Type()
)
channel_Filter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel_Filter.setStatus("current")


class _SFN_Sync_Type(Integer32):
    """Custom type sFN_Sync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SFN_Sync_Type.__name__ = "Integer32"
_SFN_Sync_Object = MibScalar
sFN_Sync = _SFN_Sync_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 57882),
    _SFN_Sync_Type()
)
sFN_Sync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sFN_Sync.setStatus("current")


class _Active_Input_Type(Integer32):
    """Custom type active_Input based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rFin1", 0),
          ("rFin2", 1))
    )


_Active_Input_Type.__name__ = "Integer32"
_Active_Input_Object = MibScalar
active_Input = _Active_Input_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 58792),
    _Active_Input_Type()
)
active_Input.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    active_Input.setStatus("current")


class _One_PPS_Source_Type(Integer32):
    """Custom type one_PPS_Source based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("external", 1))
    )


_One_PPS_Source_Type.__name__ = "Integer32"
_One_PPS_Source_Object = MibScalar
one_PPS_Source = _One_PPS_Source_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 58936),
    _One_PPS_Source_Type()
)
one_PPS_Source.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    one_PPS_Source.setStatus("current")
_Result_Update_Rate_Reduction_Type = Integer32
_Result_Update_Rate_Reduction_Object = MibScalar
result_Update_Rate_Reduction = _Result_Update_Rate_Reduction_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 61462),
    _Result_Update_Rate_Reduction_Type()
)
result_Update_Rate_Reduction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    result_Update_Rate_Reduction.setStatus("current")


class _Spectral_Only_Type(Integer32):
    """Custom type spectral_Only based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Spectral_Only_Type.__name__ = "Integer32"
_Spectral_Only_Object = MibScalar
spectral_Only = _Spectral_Only_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 61463),
    _Spectral_Only_Type()
)
spectral_Only.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spectral_Only.setStatus("current")


class _Rx_gain_dB_Type(Integer32):
    """Custom type rx_gain_dB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aGC", 0),
          ("minus-18", 1),
          ("minus-12", 2),
          ("minus-6", 3),
          ("zero", 4),
          ("plus-20", 5),
          ("plus-40", 6),
          ("plus-60", 7))
    )


_Rx_gain_dB_Type.__name__ = "Integer32"
_Rx_gain_dB_Object = MibScalar
rx_gain_dB = _Rx_gain_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 2, 61476),
    _Rx_gain_dB_Type()
)
rx_gain_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rx_gain_dB.setStatus("current")
_Alarms_ObjectIdentity = ObjectIdentity
alarms = _Alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3)
)
_Alarm_Properties_ObjectIdentity = ObjectIdentity
alarm_Properties = _Alarm_Properties_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 1)
)
_Thresholds_ObjectIdentity = ObjectIdentity
thresholds = _Thresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 2)
)
_Alarm_Email_Settings_ObjectIdentity = ObjectIdentity
alarm_Email_Settings = _Alarm_Email_Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 17)
)
_SMTP_Server_Host_Type = Integer32
_SMTP_Server_Host_Object = MibScalar
sMTP_Server_Host = _SMTP_Server_Host_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 5894),
    _SMTP_Server_Host_Type()
)
sMTP_Server_Host.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTP_Server_Host.setStatus("current")
_SMTP_Server_Port_Type = Integer32
_SMTP_Server_Port_Object = MibScalar
sMTP_Server_Port = _SMTP_Server_Port_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 5895),
    _SMTP_Server_Port_Type()
)
sMTP_Server_Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTP_Server_Port.setStatus("current")
_Email_From_Type = Integer32
_Email_From_Object = MibScalar
email_From = _Email_From_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 5896),
    _Email_From_Type()
)
email_From.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    email_From.setStatus("current")
_SMTP_Server_Password_Type = Integer32
_SMTP_Server_Password_Object = MibScalar
sMTP_Server_Password = _SMTP_Server_Password_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 5897),
    _SMTP_Server_Password_Type()
)
sMTP_Server_Password.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTP_Server_Password.setStatus("current")
_Email_To_Type = Integer32
_Email_To_Object = MibScalar
email_To = _Email_To_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 5898),
    _Email_To_Type()
)
email_To.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    email_To.setStatus("current")
_SMTP_Server_User_Name_Type = Integer32
_SMTP_Server_User_Name_Object = MibScalar
sMTP_Server_User_Name = _SMTP_Server_User_Name_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 5899),
    _SMTP_Server_User_Name_Type()
)
sMTP_Server_User_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sMTP_Server_User_Name.setStatus("current")


class _Use_SSL_TLS_Type(Integer32):
    """Custom type use_SSL_TLS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nO", 0),
          ("yES", 1))
    )


_Use_SSL_TLS_Type.__name__ = "Integer32"
_Use_SSL_TLS_Object = MibScalar
use_SSL_TLS = _Use_SSL_TLS_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 5900),
    _Use_SSL_TLS_Type()
)
use_SSL_TLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    use_SSL_TLS.setStatus("current")
_Frequency_Shift_Threshold_High_Hz_Type = Integer32
_Frequency_Shift_Threshold_High_Hz_Object = MibScalar
frequency_Shift_Threshold_High_Hz = _Frequency_Shift_Threshold_High_Hz_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 57896),
    _Frequency_Shift_Threshold_High_Hz_Type()
)
frequency_Shift_Threshold_High_Hz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequency_Shift_Threshold_High_Hz.setStatus("current")
_Frequency_Shift_Threshold_Low_Hz_Type = Integer32
_Frequency_Shift_Threshold_Low_Hz_Object = MibScalar
frequency_Shift_Threshold_Low_Hz = _Frequency_Shift_Threshold_Low_Hz_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 57912),
    _Frequency_Shift_Threshold_Low_Hz_Type()
)
frequency_Shift_Threshold_Low_Hz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frequency_Shift_Threshold_Low_Hz.setStatus("current")
_Lower_Shoulder_Threshold_Low_dB_Type = Integer32
_Lower_Shoulder_Threshold_Low_dB_Object = MibScalar
lower_Shoulder_Threshold_Low_dB = _Lower_Shoulder_Threshold_Low_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 57928),
    _Lower_Shoulder_Threshold_Low_dB_Type()
)
lower_Shoulder_Threshold_Low_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lower_Shoulder_Threshold_Low_dB.setStatus("current")
_Lower_Shoulder_Threshold_High_dB_Type = Integer32
_Lower_Shoulder_Threshold_High_dB_Object = MibScalar
lower_Shoulder_Threshold_High_dB = _Lower_Shoulder_Threshold_High_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 57944),
    _Lower_Shoulder_Threshold_High_dB_Type()
)
lower_Shoulder_Threshold_High_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lower_Shoulder_Threshold_High_dB.setStatus("current")
_Upper_Shoulder_Threshold_Low_dB_Type = Integer32
_Upper_Shoulder_Threshold_Low_dB_Object = MibScalar
upper_Shoulder_Threshold_Low_dB = _Upper_Shoulder_Threshold_Low_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 57960),
    _Upper_Shoulder_Threshold_Low_dB_Type()
)
upper_Shoulder_Threshold_Low_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upper_Shoulder_Threshold_Low_dB.setStatus("current")
_Upper_Shoulder_Threshold_High_dB_Type = Integer32
_Upper_Shoulder_Threshold_High_dB_Object = MibScalar
upper_Shoulder_Threshold_High_dB = _Upper_Shoulder_Threshold_High_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 57976),
    _Upper_Shoulder_Threshold_High_dB_Type()
)
upper_Shoulder_Threshold_High_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upper_Shoulder_Threshold_High_dB.setStatus("current")
_MER_Threshold_High_dB_Type = Integer32
_MER_Threshold_High_dB_Object = MibScalar
mER_Threshold_High_dB = _MER_Threshold_High_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 57992),
    _MER_Threshold_High_dB_Type()
)
mER_Threshold_High_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mER_Threshold_High_dB.setStatus("current")
_MER_Threshold_Low_dB_Type = Integer32
_MER_Threshold_Low_dB_Object = MibScalar
mER_Threshold_Low_dB = _MER_Threshold_Low_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 58008),
    _MER_Threshold_Low_dB_Type()
)
mER_Threshold_Low_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mER_Threshold_Low_dB.setStatus("current")
_SNR_Threshold_High_dB_Type = Integer32
_SNR_Threshold_High_dB_Object = MibScalar
sNR_Threshold_High_dB = _SNR_Threshold_High_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 58024),
    _SNR_Threshold_High_dB_Type()
)
sNR_Threshold_High_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNR_Threshold_High_dB.setStatus("current")
_SNR_Threshold_Low_dB_Type = Integer32
_SNR_Threshold_Low_dB_Object = MibScalar
sNR_Threshold_Low_dB = _SNR_Threshold_Low_dB_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 58040),
    _SNR_Threshold_Low_dB_Type()
)
sNR_Threshold_Low_dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNR_Threshold_Low_dB.setStatus("current")
_Scale_Threshold_High_Type = Integer32
_Scale_Threshold_High_Object = MibScalar
scale_Threshold_High = _Scale_Threshold_High_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 58056),
    _Scale_Threshold_High_Type()
)
scale_Threshold_High.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scale_Threshold_High.setStatus("current")
_Scale_Threshold_Low_Type = Integer32
_Scale_Threshold_Low_Object = MibScalar
scale_Threshold_Low = _Scale_Threshold_Low_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 58072),
    _Scale_Threshold_Low_Type()
)
scale_Threshold_Low.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scale_Threshold_Low.setStatus("current")
_Echo_time_offset_Allowed_Threshold_usec_Type = Integer32
_Echo_time_offset_Allowed_Threshold_usec_Object = MibScalar
echo_time_offset_Allowed_Threshold_usec = _Echo_time_offset_Allowed_Threshold_usec_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 58105),
    _Echo_time_offset_Allowed_Threshold_usec_Type()
)
echo_time_offset_Allowed_Threshold_usec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echo_time_offset_Allowed_Threshold_usec.setStatus("current")
_Echo_Amplitude_Allowed_Threshold_db_Type = Integer32
_Echo_Amplitude_Allowed_Threshold_db_Object = MibScalar
echo_Amplitude_Allowed_Threshold_db = _Echo_Amplitude_Allowed_Threshold_db_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 3, 58106),
    _Echo_Amplitude_Allowed_Threshold_db_Type()
)
echo_Amplitude_Allowed_Threshold_db.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    echo_Amplitude_Allowed_Threshold_db.setStatus("current")
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4)
)
_Site_ObjectIdentity = ObjectIdentity
site = _Site_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 1)
)
_SNMP_ObjectIdentity = ObjectIdentity
sNMP = _SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 4)
)
_Site_Name_Type = Integer32
_Site_Name_Object = MibScalar
site_Name = _Site_Name_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 5),
    _Site_Name_Type()
)
site_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    site_Name.setStatus("current")
_RTC_ObjectIdentity = ObjectIdentity
rTC = _RTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 9)
)
_Heartbeat_ObjectIdentity = ObjectIdentity
heartbeat = _Heartbeat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 16)
)
_Licensed_Standards_ObjectIdentity = ObjectIdentity
licensed_Standards = _Licensed_Standards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 20)
)
_Reset_parameters_to_default_ObjectIdentity = ObjectIdentity
reset_parameters_to_default = _Reset_parameters_to_default_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 22)
)
_Restart_System_ObjectIdentity = ObjectIdentity
restart_System = _Restart_System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 24)
)
_Site_ID_Type = Integer32
_Site_ID_Object = MibScalar
site_ID = _Site_ID_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 261),
    _Site_ID_Type()
)
site_ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    site_ID.setStatus("current")
_SNMP_Trap_Server_IP_Address_Type = Integer32
_SNMP_Trap_Server_IP_Address_Object = MibScalar
sNMP_Trap_Server_IP_Address = _SNMP_Trap_Server_IP_Address_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 26885),
    _SNMP_Trap_Server_IP_Address_Type()
)
sNMP_Trap_Server_IP_Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMP_Trap_Server_IP_Address.setStatus("current")


class _SNMP_Notification_Type_Type(Integer32):
    """Custom type sNMP_Notification_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trap", 0),
          ("inform", 1))
    )


_SNMP_Notification_Type_Type.__name__ = "Integer32"
_SNMP_Notification_Type_Object = MibScalar
sNMP_Notification_Type = _SNMP_Notification_Type_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 29445),
    _SNMP_Notification_Type_Type()
)
sNMP_Notification_Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMP_Notification_Type.setStatus("current")


class _SNMP_Traps_On_Off_Type(Integer32):
    """Custom type sNMP_Traps_On_Off based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 0),
          ("oN", 1))
    )


_SNMP_Traps_On_Off_Type.__name__ = "Integer32"
_SNMP_Traps_On_Off_Object = MibScalar
sNMP_Traps_On_Off = _SNMP_Traps_On_Off_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 29701),
    _SNMP_Traps_On_Off_Type()
)
sNMP_Traps_On_Off.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sNMP_Traps_On_Off.setStatus("current")


class _System_Restart_Type(Integer32):
    """Custom type system_Restart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 0),
          ("oN", 1))
    )


_System_Restart_Type.__name__ = "Integer32"
_System_Restart_Object = MibScalar
system_Restart = _System_Restart_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 32517),
    _System_Restart_Type()
)
system_Restart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    system_Restart.setStatus("current")


class _Restore_default_parameters_Type(Integer32):
    """Custom type restore_default_parameters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 0),
          ("oN", 1))
    )


_Restore_default_parameters_Type.__name__ = "Integer32"
_Restore_default_parameters_Object = MibScalar
restore_default_parameters = _Restore_default_parameters_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 32518),
    _Restore_default_parameters_Type()
)
restore_default_parameters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    restore_default_parameters.setStatus("current")
_Year_Type = Integer32
_Year_Object = MibScalar
year = _Year_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 36101),
    _Year_Type()
)
year.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    year.setStatus("current")
_Month_Type = Integer32
_Month_Object = MibScalar
month = _Month_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 36357),
    _Month_Type()
)
month.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    month.setStatus("current")
_Day_Type = Integer32
_Day_Object = MibScalar
day = _Day_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 36613),
    _Day_Type()
)
day.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    day.setStatus("current")
_Hour_Type = Integer32
_Hour_Object = MibScalar
hour = _Hour_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 36869),
    _Hour_Type()
)
hour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hour.setStatus("current")
_Minute_Type = Integer32
_Minute_Object = MibScalar
minute = _Minute_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 37125),
    _Minute_Type()
)
minute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    minute.setStatus("current")
_Second_Type = Integer32
_Second_Object = MibScalar
second = _Second_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 37381),
    _Second_Type()
)
second.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    second.setStatus("current")
_Heartbeat_Hour_Start_Type = Integer32
_Heartbeat_Hour_Start_Object = MibScalar
heartbeat_Hour_Start = _Heartbeat_Hour_Start_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 37637),
    _Heartbeat_Hour_Start_Type()
)
heartbeat_Hour_Start.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartbeat_Hour_Start.setStatus("current")
_Heartbeat_Minute_Start_Type = Integer32
_Heartbeat_Minute_Start_Object = MibScalar
heartbeat_Minute_Start = _Heartbeat_Minute_Start_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 37893),
    _Heartbeat_Minute_Start_Type()
)
heartbeat_Minute_Start.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartbeat_Minute_Start.setStatus("current")
_Heartbeat_Pace_Type = Integer32
_Heartbeat_Pace_Object = MibScalar
heartbeat_Pace = _Heartbeat_Pace_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 38149),
    _Heartbeat_Pace_Type()
)
heartbeat_Pace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartbeat_Pace.setStatus("current")


class _Set_Test_Alarm_Type(Integer32):
    """Custom type set_Test_Alarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("oFF", 0),
          ("oN", 1))
    )


_Set_Test_Alarm_Type.__name__ = "Integer32"
_Set_Test_Alarm_Object = MibScalar
set_Test_Alarm = _Set_Test_Alarm_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 44549),
    _Set_Test_Alarm_Type()
)
set_Test_Alarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    set_Test_Alarm.setStatus("current")


class _Standard_Type(Integer32):
    """Custom type standard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("dVB-TH", 1),
          ("aTSC", 2),
          ("dAB", 3),
          ("dTMB", 4),
          ("iSDB-T", 5),
          ("cMMB", 6),
          ("dVB-T2", 7),
          ("dVB-S-S2", 8),
          ("aTSC3-0", 9))
    )


_Standard_Type.__name__ = "Integer32"
_Standard_Object = MibScalar
standard = _Standard_Object(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 4, 57384),
    _Standard_Type()
)
standard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    standard.setStatus("current")

# Managed Objects groups


# Notification objects

avqSystem_Restarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 1)
)
avqSystem_Restarted.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqSystem_Restarted.setStatus(
        "current"
    )

avqSignal_scale_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 2)
)
avqSignal_scale_out_of_range.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqSignal_scale_out_of_range.setStatus(
        "current"
    )

avqLeft_Shoulder_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 3)
)
avqLeft_Shoulder_out_of_range.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqLeft_Shoulder_out_of_range.setStatus(
        "current"
    )

avqRight_Shoulder_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 4)
)
avqRight_Shoulder_out_of_range.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqRight_Shoulder_out_of_range.setStatus(
        "current"
    )

avqFrequency_Shift_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 5)
)
avqFrequency_Shift_out_of_range.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqFrequency_Shift_out_of_range.setStatus(
        "current"
    )

avqSNR_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 6)
)
avqSNR_out_of_range.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqSNR_out_of_range.setStatus(
        "current"
    )

avqMER_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 7)
)
avqMER_out_of_range.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqMER_out_of_range.setStatus(
        "current"
    )

avqSFN_Drift_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 8)
)
avqSFN_Drift_out_of_range.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqSFN_Drift_out_of_range.setStatus(
        "current"
    )

avqEcho_profile_out_of_range = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 9)
)
avqEcho_profile_out_of_range.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqEcho_profile_out_of_range.setStatus(
        "current"
    )

avqRF_Board_alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 10)
)
avqRF_Board_alarm.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqRF_Board_alarm.setStatus(
        "current"
    )

avqGPS_no_fix = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 11)
)
avqGPS_no_fix.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqGPS_no_fix.setStatus(
        "current"
    )

avqTest_Alarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 40591, 1020, 1, 0, 1, 0, 12)
)
avqTest_Alarm.setObjects(
      *(("AVQ1020-MIB", "avqSiteId"),
        ("AVQ1020-MIB", "avqAlarmGroupId"),
        ("AVQ1020-MIB", "avqAlarmSeverityLevel"),
        ("AVQ1020-MIB", "avqTrapNumber"),
        ("AVQ1020-MIB", "avqParameterName"),
        ("AVQ1020-MIB", "avqParameterOID"),
        ("AVQ1020-MIB", "avqParameterValue"),
        ("AVQ1020-MIB", "avqUTCTimestamp"))
)
if mibBuilder.loadTexts:
    avqTest_Alarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVQ1020-MIB",
    **{"avq": avq,
       "receiver": receiver,
       "receiver-1": receiver_1,
       "receiverTable": receiverTable,
       "avqTraps": avqTraps,
       "avqObjs": avqObjs,
       "avqSiteId": avqSiteId,
       "avqAlarmGroupId": avqAlarmGroupId,
       "avqAlarmSeverityLevel": avqAlarmSeverityLevel,
       "avqTrapNumber": avqTrapNumber,
       "avqParameterName": avqParameterName,
       "avqParameterOID": avqParameterOID,
       "avqParameterValue": avqParameterValue,
       "avqUTCTimestamp": avqUTCTimestamp,
       "avqTraps-Info": avqTraps_Info,
       "avqTraps-Traps": avqTraps_Traps,
       "avqSystem-Restarted": avqSystem_Restarted,
       "avqSignal-scale-out-of-range": avqSignal_scale_out_of_range,
       "avqLeft-Shoulder-out-of-range": avqLeft_Shoulder_out_of_range,
       "avqRight-Shoulder-out-of-range": avqRight_Shoulder_out_of_range,
       "avqFrequency-Shift-out-of-range": avqFrequency_Shift_out_of_range,
       "avqSNR-out-of-range": avqSNR_out_of_range,
       "avqMER-out-of-range": avqMER_out_of_range,
       "avqSFN-Drift-out-of-range": avqSFN_Drift_out_of_range,
       "avqEcho-profile-out-of-range": avqEcho_profile_out_of_range,
       "avqRF-Board-alarm": avqRF_Board_alarm,
       "avqGPS-no-fix": avqGPS_no_fix,
       "avqTest-Alarm": avqTest_Alarm,
       "status": status,
       "receiverEntry": receiverEntry,
       "global-Status-Info": global_Status_Info,
       "status-Info": status_Info,
       "alarms-Info": alarms_Info,
       "standard-and-central-frequency-Info": standard_and_central_frequency_Info,
       "spectral-Info": spectral_Info,
       "quality-Info": quality_Info,
       "options-Info": options_Info,
       "reference-and-timing-Info": reference_and_timing_Info,
       "network-Info": network_Info,
       "hW-Status-Info": hW_Status_Info,
       "versions-and-Serial-Numbers-Info": versions_and_Serial_Numbers_Info,
       "x1-Alarm-Entry-Index": x1_Alarm_Entry_Index,
       "x1-Trap-Notification-on-Alarm": x1_Trap_Notification_on_Alarm,
       "x1-Email-Notification-on-Alarm": x1_Email_Notification_on_Alarm,
       "x1-Integration-Time": x1_Integration_Time,
       "x1-Alarm-Severity-Level": x1_Alarm_Severity_Level,
       "status-Active-Alarms": status_Active_Alarms,
       "x1-Relay1-on-Alarm": x1_Relay1_on_Alarm,
       "x1-Relay2-on-Alarm": x1_Relay2_on_Alarm,
       "status-CPU-Temperature-Current": status_CPU_Temperature_Current,
       "status-FPGA-Temperature-Current": status_FPGA_Temperature_Current,
       "status-Case-Temperature-Current": status_Case_Temperature_Current,
       "status-Temperature-Fault": status_Temperature_Fault,
       "status-RF-Board-Fault": status_RF_Board_Fault,
       "status-HW-Fault": status_HW_Fault,
       "status-App-Revision": status_App_Revision,
       "status-App-Version": status_App_Version,
       "status-App-Build-Date": status_App_Build_Date,
       "status-Eth0-IP-Address": status_Eth0_IP_Address,
       "status-Eth0-Gateway": status_Eth0_Gateway,
       "status-Eth0-Netmask": status_Eth0_Netmask,
       "status-DNS-Server": status_DNS_Server,
       "status-Serial-Number": status_Serial_Number,
       "status-Eth0-Mac-Address": status_Eth0_Mac_Address,
       "status-OS-kernel": status_OS_kernel,
       "status-FPGA-ver": status_FPGA_ver,
       "status-Firmware-ver": status_Firmware_ver,
       "status-Library-ver": status_Library_ver,
       "status-Standard": status_Standard,
       "status-Central-Freq-Hz": status_Central_Freq_Hz,
       "status-Status": status_Status,
       "status-Last-error": status_Last_error,
       "status-PAPR-dB": status_PAPR_dB,
       "status-Frequency-Shift-Hz": status_Frequency_Shift_Hz,
       "status-Left-Shoulder-dB": status_Left_Shoulder_dB,
       "status-Right-Shoulder-dB": status_Right_Shoulder_dB,
       "status-Amplitude-Error-dB": status_Amplitude_Error_dB,
       "status-Phase-Error-degree": status_Phase_Error_degree,
       "status-MER-dB": status_MER_dB,
       "status-SFN-Sync-Status": status_SFN_Sync_Status,
       "status-Residual-GD": status_Residual_GD,
       "status-Spectrum-inversion": status_Spectrum_inversion,
       "status-Ten-MHz-Reference-Source": status_Ten_MHz_Reference_Source,
       "status-ADC-Signal-Scale-Percent": status_ADC_Signal_Scale_Percent,
       "status-ADC-clock-error-Hz": status_ADC_clock_error_Hz,
       "status-Sample-Rate-Shift-Hz": status_Sample_Rate_Shift_Hz,
       "status-RF-board-firmware-ver": status_RF_board_firmware_ver,
       "status-RF-board-serial-num": status_RF_board_serial_num,
       "status-RF-transceiver-RTOS-ver": status_RF_transceiver_RTOS_ver,
       "status-Input-RF-power-dBm": status_Input_RF_power_dBm,
       "configuration": configuration,
       "settings": settings,
       "site-Info": site_Info,
       "system-Description": system_Description,
       "contact-Information": contact_Information,
       "system-Location": system_Location,
       "site-Address-Line-1": site_Address_Line_1,
       "site-Address-Line-2": site_Address_Line_2,
       "site-Address-Line-3": site_Address_Line_3,
       "site-Address-Line-4": site_Address_Line_4,
       "site-Notes": site_Notes,
       "central-Freq-Hz": central_Freq_Hz,
       "command": command,
       "equalizer": equalizer,
       "channel-Filter": channel_Filter,
       "sFN-Sync": sFN_Sync,
       "active-Input": active_Input,
       "one-PPS-Source": one_PPS_Source,
       "result-Update-Rate-Reduction": result_Update_Rate_Reduction,
       "spectral-Only": spectral_Only,
       "rx-gain-dB": rx_gain_dB,
       "alarms": alarms,
       "alarm-Properties": alarm_Properties,
       "thresholds": thresholds,
       "alarm-Email-Settings": alarm_Email_Settings,
       "sMTP-Server-Host": sMTP_Server_Host,
       "sMTP-Server-Port": sMTP_Server_Port,
       "email-From": email_From,
       "sMTP-Server-Password": sMTP_Server_Password,
       "email-To": email_To,
       "sMTP-Server-User-Name": sMTP_Server_User_Name,
       "use-SSL-TLS": use_SSL_TLS,
       "frequency-Shift-Threshold-High-Hz": frequency_Shift_Threshold_High_Hz,
       "frequency-Shift-Threshold-Low-Hz": frequency_Shift_Threshold_Low_Hz,
       "lower-Shoulder-Threshold-Low-dB": lower_Shoulder_Threshold_Low_dB,
       "lower-Shoulder-Threshold-High-dB": lower_Shoulder_Threshold_High_dB,
       "upper-Shoulder-Threshold-Low-dB": upper_Shoulder_Threshold_Low_dB,
       "upper-Shoulder-Threshold-High-dB": upper_Shoulder_Threshold_High_dB,
       "mER-Threshold-High-dB": mER_Threshold_High_dB,
       "mER-Threshold-Low-dB": mER_Threshold_Low_dB,
       "sNR-Threshold-High-dB": sNR_Threshold_High_dB,
       "sNR-Threshold-Low-dB": sNR_Threshold_Low_dB,
       "scale-Threshold-High": scale_Threshold_High,
       "scale-Threshold-Low": scale_Threshold_Low,
       "echo-time-offset-Allowed-Threshold-usec": echo_time_offset_Allowed_Threshold_usec,
       "echo-Amplitude-Allowed-Threshold-db": echo_Amplitude_Allowed_Threshold_db,
       "system": system,
       "site": site,
       "sNMP": sNMP,
       "site-Name": site_Name,
       "rTC": rTC,
       "heartbeat": heartbeat,
       "licensed-Standards": licensed_Standards,
       "reset-parameters-to-default": reset_parameters_to_default,
       "restart-System": restart_System,
       "site-ID": site_ID,
       "sNMP-Trap-Server-IP-Address": sNMP_Trap_Server_IP_Address,
       "sNMP-Notification-Type": sNMP_Notification_Type,
       "sNMP-Traps-On-Off": sNMP_Traps_On_Off,
       "system-Restart": system_Restart,
       "restore-default-parameters": restore_default_parameters,
       "year": year,
       "month": month,
       "day": day,
       "hour": hour,
       "minute": minute,
       "second": second,
       "heartbeat-Hour-Start": heartbeat_Hour_Start,
       "heartbeat-Minute-Start": heartbeat_Minute_Start,
       "heartbeat-Pace": heartbeat_Pace,
       "set-Test-Alarm": set_Test_Alarm,
       "standard": standard}
)
