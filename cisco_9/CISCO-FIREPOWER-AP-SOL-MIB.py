# SNMP MIB module (CISCO-FIREPOWER-AP-SOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-SOL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:17:27 2025
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

(CfprApManagedObjectDn,
 CfprApManagedObjectId,
 ciscoFirepowerApMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-MIB",
    "CfprApManagedObjectDn",
    "CfprApManagedObjectId",
    "ciscoFirepowerApMIBObjects")

(CfprApPolicyPolicyOwner,
 CfprApSolAdminState,
 CfprApSolSpeed) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApPolicyPolicyOwner",
    "CfprApSolAdminState",
    "CfprApSolSpeed")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cfprApSolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApSolConfigTable_Object = MibTable
cfprApSolConfigTable = _CfprApSolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1)
)
if mibBuilder.loadTexts:
    cfprApSolConfigTable.setStatus("current")
_CfprApSolConfigEntry_Object = MibTableRow
cfprApSolConfigEntry = _CfprApSolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1)
)
cfprApSolConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SOL-MIB", "cfprApSolConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSolConfigEntry.setStatus("current")
_CfprApSolConfigInstanceId_Type = CfprApManagedObjectId
_CfprApSolConfigInstanceId_Object = MibTableColumn
cfprApSolConfigInstanceId = _CfprApSolConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 1),
    _CfprApSolConfigInstanceId_Type()
)
cfprApSolConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSolConfigInstanceId.setStatus("current")
_CfprApSolConfigDn_Type = CfprApManagedObjectDn
_CfprApSolConfigDn_Object = MibTableColumn
cfprApSolConfigDn = _CfprApSolConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 2),
    _CfprApSolConfigDn_Type()
)
cfprApSolConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigDn.setStatus("current")
_CfprApSolConfigRn_Type = SnmpAdminString
_CfprApSolConfigRn_Object = MibTableColumn
cfprApSolConfigRn = _CfprApSolConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 3),
    _CfprApSolConfigRn_Type()
)
cfprApSolConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigRn.setStatus("current")
_CfprApSolConfigAdminState_Type = CfprApSolAdminState
_CfprApSolConfigAdminState_Object = MibTableColumn
cfprApSolConfigAdminState = _CfprApSolConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 4),
    _CfprApSolConfigAdminState_Type()
)
cfprApSolConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigAdminState.setStatus("current")
_CfprApSolConfigDescr_Type = SnmpAdminString
_CfprApSolConfigDescr_Object = MibTableColumn
cfprApSolConfigDescr = _CfprApSolConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 5),
    _CfprApSolConfigDescr_Type()
)
cfprApSolConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigDescr.setStatus("current")
_CfprApSolConfigIntId_Type = SnmpAdminString
_CfprApSolConfigIntId_Object = MibTableColumn
cfprApSolConfigIntId = _CfprApSolConfigIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 6),
    _CfprApSolConfigIntId_Type()
)
cfprApSolConfigIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigIntId.setStatus("current")
_CfprApSolConfigName_Type = SnmpAdminString
_CfprApSolConfigName_Object = MibTableColumn
cfprApSolConfigName = _CfprApSolConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 7),
    _CfprApSolConfigName_Type()
)
cfprApSolConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigName.setStatus("current")
_CfprApSolConfigPolicyLevel_Type = Gauge32
_CfprApSolConfigPolicyLevel_Object = MibTableColumn
cfprApSolConfigPolicyLevel = _CfprApSolConfigPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 8),
    _CfprApSolConfigPolicyLevel_Type()
)
cfprApSolConfigPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigPolicyLevel.setStatus("current")
_CfprApSolConfigPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApSolConfigPolicyOwner_Object = MibTableColumn
cfprApSolConfigPolicyOwner = _CfprApSolConfigPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 9),
    _CfprApSolConfigPolicyOwner_Type()
)
cfprApSolConfigPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigPolicyOwner.setStatus("current")
_CfprApSolConfigSpeed_Type = CfprApSolSpeed
_CfprApSolConfigSpeed_Object = MibTableColumn
cfprApSolConfigSpeed = _CfprApSolConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 1, 1, 10),
    _CfprApSolConfigSpeed_Type()
)
cfprApSolConfigSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolConfigSpeed.setStatus("current")
_CfprApSolIfTable_Object = MibTable
cfprApSolIfTable = _CfprApSolIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2)
)
if mibBuilder.loadTexts:
    cfprApSolIfTable.setStatus("current")
_CfprApSolIfEntry_Object = MibTableRow
cfprApSolIfEntry = _CfprApSolIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1)
)
cfprApSolIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SOL-MIB", "cfprApSolIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSolIfEntry.setStatus("current")
_CfprApSolIfInstanceId_Type = CfprApManagedObjectId
_CfprApSolIfInstanceId_Object = MibTableColumn
cfprApSolIfInstanceId = _CfprApSolIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 1),
    _CfprApSolIfInstanceId_Type()
)
cfprApSolIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSolIfInstanceId.setStatus("current")
_CfprApSolIfDn_Type = CfprApManagedObjectDn
_CfprApSolIfDn_Object = MibTableColumn
cfprApSolIfDn = _CfprApSolIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 2),
    _CfprApSolIfDn_Type()
)
cfprApSolIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfDn.setStatus("current")
_CfprApSolIfRn_Type = SnmpAdminString
_CfprApSolIfRn_Object = MibTableColumn
cfprApSolIfRn = _CfprApSolIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 3),
    _CfprApSolIfRn_Type()
)
cfprApSolIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfRn.setStatus("current")
_CfprApSolIfAdminState_Type = CfprApSolAdminState
_CfprApSolIfAdminState_Object = MibTableColumn
cfprApSolIfAdminState = _CfprApSolIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 4),
    _CfprApSolIfAdminState_Type()
)
cfprApSolIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfAdminState.setStatus("current")
_CfprApSolIfDescr_Type = SnmpAdminString
_CfprApSolIfDescr_Object = MibTableColumn
cfprApSolIfDescr = _CfprApSolIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 5),
    _CfprApSolIfDescr_Type()
)
cfprApSolIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfDescr.setStatus("current")
_CfprApSolIfIntId_Type = SnmpAdminString
_CfprApSolIfIntId_Object = MibTableColumn
cfprApSolIfIntId = _CfprApSolIfIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 6),
    _CfprApSolIfIntId_Type()
)
cfprApSolIfIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfIntId.setStatus("current")
_CfprApSolIfName_Type = SnmpAdminString
_CfprApSolIfName_Object = MibTableColumn
cfprApSolIfName = _CfprApSolIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 7),
    _CfprApSolIfName_Type()
)
cfprApSolIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfName.setStatus("current")
_CfprApSolIfPolicyLevel_Type = Gauge32
_CfprApSolIfPolicyLevel_Object = MibTableColumn
cfprApSolIfPolicyLevel = _CfprApSolIfPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 8),
    _CfprApSolIfPolicyLevel_Type()
)
cfprApSolIfPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfPolicyLevel.setStatus("current")
_CfprApSolIfPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApSolIfPolicyOwner_Object = MibTableColumn
cfprApSolIfPolicyOwner = _CfprApSolIfPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 9),
    _CfprApSolIfPolicyOwner_Type()
)
cfprApSolIfPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfPolicyOwner.setStatus("current")
_CfprApSolIfSpeed_Type = CfprApSolSpeed
_CfprApSolIfSpeed_Object = MibTableColumn
cfprApSolIfSpeed = _CfprApSolIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 2, 1, 10),
    _CfprApSolIfSpeed_Type()
)
cfprApSolIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolIfSpeed.setStatus("current")
_CfprApSolPolicyTable_Object = MibTable
cfprApSolPolicyTable = _CfprApSolPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3)
)
if mibBuilder.loadTexts:
    cfprApSolPolicyTable.setStatus("current")
_CfprApSolPolicyEntry_Object = MibTableRow
cfprApSolPolicyEntry = _CfprApSolPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1)
)
cfprApSolPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-SOL-MIB", "cfprApSolPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApSolPolicyEntry.setStatus("current")
_CfprApSolPolicyInstanceId_Type = CfprApManagedObjectId
_CfprApSolPolicyInstanceId_Object = MibTableColumn
cfprApSolPolicyInstanceId = _CfprApSolPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 1),
    _CfprApSolPolicyInstanceId_Type()
)
cfprApSolPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApSolPolicyInstanceId.setStatus("current")
_CfprApSolPolicyDn_Type = CfprApManagedObjectDn
_CfprApSolPolicyDn_Object = MibTableColumn
cfprApSolPolicyDn = _CfprApSolPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 2),
    _CfprApSolPolicyDn_Type()
)
cfprApSolPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicyDn.setStatus("current")
_CfprApSolPolicyRn_Type = SnmpAdminString
_CfprApSolPolicyRn_Object = MibTableColumn
cfprApSolPolicyRn = _CfprApSolPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 3),
    _CfprApSolPolicyRn_Type()
)
cfprApSolPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicyRn.setStatus("current")
_CfprApSolPolicyAdminState_Type = CfprApSolAdminState
_CfprApSolPolicyAdminState_Object = MibTableColumn
cfprApSolPolicyAdminState = _CfprApSolPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 4),
    _CfprApSolPolicyAdminState_Type()
)
cfprApSolPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicyAdminState.setStatus("current")
_CfprApSolPolicyDescr_Type = SnmpAdminString
_CfprApSolPolicyDescr_Object = MibTableColumn
cfprApSolPolicyDescr = _CfprApSolPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 5),
    _CfprApSolPolicyDescr_Type()
)
cfprApSolPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicyDescr.setStatus("current")
_CfprApSolPolicyIntId_Type = SnmpAdminString
_CfprApSolPolicyIntId_Object = MibTableColumn
cfprApSolPolicyIntId = _CfprApSolPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 6),
    _CfprApSolPolicyIntId_Type()
)
cfprApSolPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicyIntId.setStatus("current")
_CfprApSolPolicyName_Type = SnmpAdminString
_CfprApSolPolicyName_Object = MibTableColumn
cfprApSolPolicyName = _CfprApSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 7),
    _CfprApSolPolicyName_Type()
)
cfprApSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicyName.setStatus("current")
_CfprApSolPolicyPolicyLevel_Type = Gauge32
_CfprApSolPolicyPolicyLevel_Object = MibTableColumn
cfprApSolPolicyPolicyLevel = _CfprApSolPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 8),
    _CfprApSolPolicyPolicyLevel_Type()
)
cfprApSolPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicyPolicyLevel.setStatus("current")
_CfprApSolPolicyPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApSolPolicyPolicyOwner_Object = MibTableColumn
cfprApSolPolicyPolicyOwner = _CfprApSolPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 9),
    _CfprApSolPolicyPolicyOwner_Type()
)
cfprApSolPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicyPolicyOwner.setStatus("current")
_CfprApSolPolicySpeed_Type = CfprApSolSpeed
_CfprApSolPolicySpeed_Object = MibTableColumn
cfprApSolPolicySpeed = _CfprApSolPolicySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 72, 3, 1, 10),
    _CfprApSolPolicySpeed_Type()
)
cfprApSolPolicySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApSolPolicySpeed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-SOL-MIB",
    **{"cfprApSolObjects": cfprApSolObjects,
       "cfprApSolConfigTable": cfprApSolConfigTable,
       "cfprApSolConfigEntry": cfprApSolConfigEntry,
       "cfprApSolConfigInstanceId": cfprApSolConfigInstanceId,
       "cfprApSolConfigDn": cfprApSolConfigDn,
       "cfprApSolConfigRn": cfprApSolConfigRn,
       "cfprApSolConfigAdminState": cfprApSolConfigAdminState,
       "cfprApSolConfigDescr": cfprApSolConfigDescr,
       "cfprApSolConfigIntId": cfprApSolConfigIntId,
       "cfprApSolConfigName": cfprApSolConfigName,
       "cfprApSolConfigPolicyLevel": cfprApSolConfigPolicyLevel,
       "cfprApSolConfigPolicyOwner": cfprApSolConfigPolicyOwner,
       "cfprApSolConfigSpeed": cfprApSolConfigSpeed,
       "cfprApSolIfTable": cfprApSolIfTable,
       "cfprApSolIfEntry": cfprApSolIfEntry,
       "cfprApSolIfInstanceId": cfprApSolIfInstanceId,
       "cfprApSolIfDn": cfprApSolIfDn,
       "cfprApSolIfRn": cfprApSolIfRn,
       "cfprApSolIfAdminState": cfprApSolIfAdminState,
       "cfprApSolIfDescr": cfprApSolIfDescr,
       "cfprApSolIfIntId": cfprApSolIfIntId,
       "cfprApSolIfName": cfprApSolIfName,
       "cfprApSolIfPolicyLevel": cfprApSolIfPolicyLevel,
       "cfprApSolIfPolicyOwner": cfprApSolIfPolicyOwner,
       "cfprApSolIfSpeed": cfprApSolIfSpeed,
       "cfprApSolPolicyTable": cfprApSolPolicyTable,
       "cfprApSolPolicyEntry": cfprApSolPolicyEntry,
       "cfprApSolPolicyInstanceId": cfprApSolPolicyInstanceId,
       "cfprApSolPolicyDn": cfprApSolPolicyDn,
       "cfprApSolPolicyRn": cfprApSolPolicyRn,
       "cfprApSolPolicyAdminState": cfprApSolPolicyAdminState,
       "cfprApSolPolicyDescr": cfprApSolPolicyDescr,
       "cfprApSolPolicyIntId": cfprApSolPolicyIntId,
       "cfprApSolPolicyName": cfprApSolPolicyName,
       "cfprApSolPolicyPolicyLevel": cfprApSolPolicyPolicyLevel,
       "cfprApSolPolicyPolicyOwner": cfprApSolPolicyPolicyOwner,
       "cfprApSolPolicySpeed": cfprApSolPolicySpeed}
)
