# SNMP MIB module (BORDA-TECHNOLOGY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/borda_48591/BORDA-TECHNOLOGY-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:58:49 2025
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

bordaSnmp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48591)
)
if mibBuilder.loadTexts:
    bordaSnmp.setRevisions(
        ("2016-09-24 17:15",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RecordID_Type = Integer32
_RecordID_Object = MibScalar
recordID = _RecordID_Object(
    (1, 3, 6, 1, 4, 1, 48591, 1),
    _RecordID_Type()
)
recordID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    recordID.setStatus("current")
_AlarmUniqueID_Type = Integer32
_AlarmUniqueID_Object = MibScalar
alarmUniqueID = _AlarmUniqueID_Object(
    (1, 3, 6, 1, 4, 1, 48591, 2),
    _AlarmUniqueID_Type()
)
alarmUniqueID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmUniqueID.setStatus("current")
_ReaderIP_Type = IpAddress
_ReaderIP_Object = MibScalar
readerIP = _ReaderIP_Object(
    (1, 3, 6, 1, 4, 1, 48591, 3),
    _ReaderIP_Type()
)
readerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readerIP.setStatus("current")
_ReaderSerialNo_Type = Integer32
_ReaderSerialNo_Object = MibScalar
readerSerialNo = _ReaderSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 48591, 4),
    _ReaderSerialNo_Type()
)
readerSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readerSerialNo.setStatus("current")
_ReaderAntennaNo_Type = Integer32
_ReaderAntennaNo_Object = MibScalar
readerAntennaNo = _ReaderAntennaNo_Object(
    (1, 3, 6, 1, 4, 1, 48591, 5),
    _ReaderAntennaNo_Type()
)
readerAntennaNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readerAntennaNo.setStatus("current")
_AlarmNotificationName_Type = OctetString
_AlarmNotificationName_Object = MibScalar
alarmNotificationName = _AlarmNotificationName_Object(
    (1, 3, 6, 1, 4, 1, 48591, 6),
    _AlarmNotificationName_Type()
)
alarmNotificationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNotificationName.setStatus("current")
_AlarmNotificationMessage_Type = OctetString
_AlarmNotificationMessage_Object = MibScalar
alarmNotificationMessage = _AlarmNotificationMessage_Object(
    (1, 3, 6, 1, 4, 1, 48591, 7),
    _AlarmNotificationMessage_Type()
)
alarmNotificationMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmNotificationMessage.setStatus("current")
_Severity_Type = Integer32
_Severity_Object = MibScalar
severity = _Severity_Object(
    (1, 3, 6, 1, 4, 1, 48591, 8),
    _Severity_Type()
)
severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severity.setStatus("current")
_Priority_Type = Integer32
_Priority_Object = MibScalar
priority = _Priority_Object(
    (1, 3, 6, 1, 4, 1, 48591, 9),
    _Priority_Type()
)
priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priority.setStatus("current")
_AlarmStatus_Type = Integer32
_AlarmStatus_Object = MibScalar
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 48591, 10),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("current")

# Managed Objects groups

snmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48591, 11)
)
snmpGroup.setObjects(
      *(("BORDA-TECHNOLOGY-MIB", "recordID"),
        ("BORDA-TECHNOLOGY-MIB", "alarmUniqueID"),
        ("BORDA-TECHNOLOGY-MIB", "readerIP"),
        ("BORDA-TECHNOLOGY-MIB", "readerSerialNo"),
        ("BORDA-TECHNOLOGY-MIB", "readerAntennaNo"),
        ("BORDA-TECHNOLOGY-MIB", "alarmNotificationName"),
        ("BORDA-TECHNOLOGY-MIB", "alarmNotificationMessage"),
        ("BORDA-TECHNOLOGY-MIB", "severity"),
        ("BORDA-TECHNOLOGY-MIB", "priority"),
        ("BORDA-TECHNOLOGY-MIB", "alarmStatus"))
)
if mibBuilder.loadTexts:
    snmpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BORDA-TECHNOLOGY-MIB",
    **{"bordaSnmp": bordaSnmp,
       "recordID": recordID,
       "alarmUniqueID": alarmUniqueID,
       "readerIP": readerIP,
       "readerSerialNo": readerSerialNo,
       "readerAntennaNo": readerAntennaNo,
       "alarmNotificationName": alarmNotificationName,
       "alarmNotificationMessage": alarmNotificationMessage,
       "severity": severity,
       "priority": priority,
       "alarmStatus": alarmStatus,
       "snmpGroup": snmpGroup}
)
