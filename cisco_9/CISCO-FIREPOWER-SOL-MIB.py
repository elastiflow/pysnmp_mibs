# SNMP MIB module (CISCO-FIREPOWER-SOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-SOL-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:12 2025
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

(CfprManagedObjectDn,
 CfprManagedObjectId,
 ciscoFirepowerMIBObjects) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-MIB",
    "CfprManagedObjectDn",
    "CfprManagedObjectId",
    "ciscoFirepowerMIBObjects")

(CfprPolicyPolicyOwner,
 CfprSolAdminState,
 CfprSolSpeed) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprPolicyPolicyOwner",
    "CfprSolAdminState",
    "CfprSolSpeed")

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

cfprSolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprSolConfigTable_Object = MibTable
cfprSolConfigTable = _CfprSolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1)
)
if mibBuilder.loadTexts:
    cfprSolConfigTable.setStatus("current")
_CfprSolConfigEntry_Object = MibTableRow
cfprSolConfigEntry = _CfprSolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1)
)
cfprSolConfigEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SOL-MIB", "cfprSolConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSolConfigEntry.setStatus("current")
_CfprSolConfigInstanceId_Type = CfprManagedObjectId
_CfprSolConfigInstanceId_Object = MibTableColumn
cfprSolConfigInstanceId = _CfprSolConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 1),
    _CfprSolConfigInstanceId_Type()
)
cfprSolConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSolConfigInstanceId.setStatus("current")
_CfprSolConfigDn_Type = CfprManagedObjectDn
_CfprSolConfigDn_Object = MibTableColumn
cfprSolConfigDn = _CfprSolConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 2),
    _CfprSolConfigDn_Type()
)
cfprSolConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigDn.setStatus("current")
_CfprSolConfigRn_Type = SnmpAdminString
_CfprSolConfigRn_Object = MibTableColumn
cfprSolConfigRn = _CfprSolConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 3),
    _CfprSolConfigRn_Type()
)
cfprSolConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigRn.setStatus("current")
_CfprSolConfigAdminState_Type = CfprSolAdminState
_CfprSolConfigAdminState_Object = MibTableColumn
cfprSolConfigAdminState = _CfprSolConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 4),
    _CfprSolConfigAdminState_Type()
)
cfprSolConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigAdminState.setStatus("current")
_CfprSolConfigDescr_Type = SnmpAdminString
_CfprSolConfigDescr_Object = MibTableColumn
cfprSolConfigDescr = _CfprSolConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 5),
    _CfprSolConfigDescr_Type()
)
cfprSolConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigDescr.setStatus("current")
_CfprSolConfigIntId_Type = SnmpAdminString
_CfprSolConfigIntId_Object = MibTableColumn
cfprSolConfigIntId = _CfprSolConfigIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 6),
    _CfprSolConfigIntId_Type()
)
cfprSolConfigIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigIntId.setStatus("current")
_CfprSolConfigName_Type = SnmpAdminString
_CfprSolConfigName_Object = MibTableColumn
cfprSolConfigName = _CfprSolConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 7),
    _CfprSolConfigName_Type()
)
cfprSolConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigName.setStatus("current")
_CfprSolConfigPolicyLevel_Type = Gauge32
_CfprSolConfigPolicyLevel_Object = MibTableColumn
cfprSolConfigPolicyLevel = _CfprSolConfigPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 8),
    _CfprSolConfigPolicyLevel_Type()
)
cfprSolConfigPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigPolicyLevel.setStatus("current")
_CfprSolConfigPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprSolConfigPolicyOwner_Object = MibTableColumn
cfprSolConfigPolicyOwner = _CfprSolConfigPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 9),
    _CfprSolConfigPolicyOwner_Type()
)
cfprSolConfigPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigPolicyOwner.setStatus("current")
_CfprSolConfigSpeed_Type = CfprSolSpeed
_CfprSolConfigSpeed_Object = MibTableColumn
cfprSolConfigSpeed = _CfprSolConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 1, 1, 10),
    _CfprSolConfigSpeed_Type()
)
cfprSolConfigSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolConfigSpeed.setStatus("current")
_CfprSolIfTable_Object = MibTable
cfprSolIfTable = _CfprSolIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2)
)
if mibBuilder.loadTexts:
    cfprSolIfTable.setStatus("current")
_CfprSolIfEntry_Object = MibTableRow
cfprSolIfEntry = _CfprSolIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1)
)
cfprSolIfEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SOL-MIB", "cfprSolIfInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSolIfEntry.setStatus("current")
_CfprSolIfInstanceId_Type = CfprManagedObjectId
_CfprSolIfInstanceId_Object = MibTableColumn
cfprSolIfInstanceId = _CfprSolIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 1),
    _CfprSolIfInstanceId_Type()
)
cfprSolIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSolIfInstanceId.setStatus("current")
_CfprSolIfDn_Type = CfprManagedObjectDn
_CfprSolIfDn_Object = MibTableColumn
cfprSolIfDn = _CfprSolIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 2),
    _CfprSolIfDn_Type()
)
cfprSolIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfDn.setStatus("current")
_CfprSolIfRn_Type = SnmpAdminString
_CfprSolIfRn_Object = MibTableColumn
cfprSolIfRn = _CfprSolIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 3),
    _CfprSolIfRn_Type()
)
cfprSolIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfRn.setStatus("current")
_CfprSolIfAdminState_Type = CfprSolAdminState
_CfprSolIfAdminState_Object = MibTableColumn
cfprSolIfAdminState = _CfprSolIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 4),
    _CfprSolIfAdminState_Type()
)
cfprSolIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfAdminState.setStatus("current")
_CfprSolIfDescr_Type = SnmpAdminString
_CfprSolIfDescr_Object = MibTableColumn
cfprSolIfDescr = _CfprSolIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 5),
    _CfprSolIfDescr_Type()
)
cfprSolIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfDescr.setStatus("current")
_CfprSolIfIntId_Type = SnmpAdminString
_CfprSolIfIntId_Object = MibTableColumn
cfprSolIfIntId = _CfprSolIfIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 6),
    _CfprSolIfIntId_Type()
)
cfprSolIfIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfIntId.setStatus("current")
_CfprSolIfName_Type = SnmpAdminString
_CfprSolIfName_Object = MibTableColumn
cfprSolIfName = _CfprSolIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 7),
    _CfprSolIfName_Type()
)
cfprSolIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfName.setStatus("current")
_CfprSolIfPolicyLevel_Type = Gauge32
_CfprSolIfPolicyLevel_Object = MibTableColumn
cfprSolIfPolicyLevel = _CfprSolIfPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 8),
    _CfprSolIfPolicyLevel_Type()
)
cfprSolIfPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfPolicyLevel.setStatus("current")
_CfprSolIfPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprSolIfPolicyOwner_Object = MibTableColumn
cfprSolIfPolicyOwner = _CfprSolIfPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 9),
    _CfprSolIfPolicyOwner_Type()
)
cfprSolIfPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfPolicyOwner.setStatus("current")
_CfprSolIfSpeed_Type = CfprSolSpeed
_CfprSolIfSpeed_Object = MibTableColumn
cfprSolIfSpeed = _CfprSolIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 2, 1, 10),
    _CfprSolIfSpeed_Type()
)
cfprSolIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolIfSpeed.setStatus("current")
_CfprSolPolicyTable_Object = MibTable
cfprSolPolicyTable = _CfprSolPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3)
)
if mibBuilder.loadTexts:
    cfprSolPolicyTable.setStatus("current")
_CfprSolPolicyEntry_Object = MibTableRow
cfprSolPolicyEntry = _CfprSolPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1)
)
cfprSolPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-SOL-MIB", "cfprSolPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprSolPolicyEntry.setStatus("current")
_CfprSolPolicyInstanceId_Type = CfprManagedObjectId
_CfprSolPolicyInstanceId_Object = MibTableColumn
cfprSolPolicyInstanceId = _CfprSolPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 1),
    _CfprSolPolicyInstanceId_Type()
)
cfprSolPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprSolPolicyInstanceId.setStatus("current")
_CfprSolPolicyDn_Type = CfprManagedObjectDn
_CfprSolPolicyDn_Object = MibTableColumn
cfprSolPolicyDn = _CfprSolPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 2),
    _CfprSolPolicyDn_Type()
)
cfprSolPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicyDn.setStatus("current")
_CfprSolPolicyRn_Type = SnmpAdminString
_CfprSolPolicyRn_Object = MibTableColumn
cfprSolPolicyRn = _CfprSolPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 3),
    _CfprSolPolicyRn_Type()
)
cfprSolPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicyRn.setStatus("current")
_CfprSolPolicyAdminState_Type = CfprSolAdminState
_CfprSolPolicyAdminState_Object = MibTableColumn
cfprSolPolicyAdminState = _CfprSolPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 4),
    _CfprSolPolicyAdminState_Type()
)
cfprSolPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicyAdminState.setStatus("current")
_CfprSolPolicyDescr_Type = SnmpAdminString
_CfprSolPolicyDescr_Object = MibTableColumn
cfprSolPolicyDescr = _CfprSolPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 5),
    _CfprSolPolicyDescr_Type()
)
cfprSolPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicyDescr.setStatus("current")
_CfprSolPolicyIntId_Type = SnmpAdminString
_CfprSolPolicyIntId_Object = MibTableColumn
cfprSolPolicyIntId = _CfprSolPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 6),
    _CfprSolPolicyIntId_Type()
)
cfprSolPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicyIntId.setStatus("current")
_CfprSolPolicyName_Type = SnmpAdminString
_CfprSolPolicyName_Object = MibTableColumn
cfprSolPolicyName = _CfprSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 7),
    _CfprSolPolicyName_Type()
)
cfprSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicyName.setStatus("current")
_CfprSolPolicyPolicyLevel_Type = Gauge32
_CfprSolPolicyPolicyLevel_Object = MibTableColumn
cfprSolPolicyPolicyLevel = _CfprSolPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 8),
    _CfprSolPolicyPolicyLevel_Type()
)
cfprSolPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicyPolicyLevel.setStatus("current")
_CfprSolPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprSolPolicyPolicyOwner_Object = MibTableColumn
cfprSolPolicyPolicyOwner = _CfprSolPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 9),
    _CfprSolPolicyPolicyOwner_Type()
)
cfprSolPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicyPolicyOwner.setStatus("current")
_CfprSolPolicySpeed_Type = CfprSolSpeed
_CfprSolPolicySpeed_Object = MibTableColumn
cfprSolPolicySpeed = _CfprSolPolicySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 72, 3, 1, 10),
    _CfprSolPolicySpeed_Type()
)
cfprSolPolicySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprSolPolicySpeed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-SOL-MIB",
    **{"cfprSolObjects": cfprSolObjects,
       "cfprSolConfigTable": cfprSolConfigTable,
       "cfprSolConfigEntry": cfprSolConfigEntry,
       "cfprSolConfigInstanceId": cfprSolConfigInstanceId,
       "cfprSolConfigDn": cfprSolConfigDn,
       "cfprSolConfigRn": cfprSolConfigRn,
       "cfprSolConfigAdminState": cfprSolConfigAdminState,
       "cfprSolConfigDescr": cfprSolConfigDescr,
       "cfprSolConfigIntId": cfprSolConfigIntId,
       "cfprSolConfigName": cfprSolConfigName,
       "cfprSolConfigPolicyLevel": cfprSolConfigPolicyLevel,
       "cfprSolConfigPolicyOwner": cfprSolConfigPolicyOwner,
       "cfprSolConfigSpeed": cfprSolConfigSpeed,
       "cfprSolIfTable": cfprSolIfTable,
       "cfprSolIfEntry": cfprSolIfEntry,
       "cfprSolIfInstanceId": cfprSolIfInstanceId,
       "cfprSolIfDn": cfprSolIfDn,
       "cfprSolIfRn": cfprSolIfRn,
       "cfprSolIfAdminState": cfprSolIfAdminState,
       "cfprSolIfDescr": cfprSolIfDescr,
       "cfprSolIfIntId": cfprSolIfIntId,
       "cfprSolIfName": cfprSolIfName,
       "cfprSolIfPolicyLevel": cfprSolIfPolicyLevel,
       "cfprSolIfPolicyOwner": cfprSolIfPolicyOwner,
       "cfprSolIfSpeed": cfprSolIfSpeed,
       "cfprSolPolicyTable": cfprSolPolicyTable,
       "cfprSolPolicyEntry": cfprSolPolicyEntry,
       "cfprSolPolicyInstanceId": cfprSolPolicyInstanceId,
       "cfprSolPolicyDn": cfprSolPolicyDn,
       "cfprSolPolicyRn": cfprSolPolicyRn,
       "cfprSolPolicyAdminState": cfprSolPolicyAdminState,
       "cfprSolPolicyDescr": cfprSolPolicyDescr,
       "cfprSolPolicyIntId": cfprSolPolicyIntId,
       "cfprSolPolicyName": cfprSolPolicyName,
       "cfprSolPolicyPolicyLevel": cfprSolPolicyPolicyLevel,
       "cfprSolPolicyPolicyOwner": cfprSolPolicyPolicyOwner,
       "cfprSolPolicySpeed": cfprSolPolicySpeed}
)
