# SNMP MIB module (CISCO-FIREPOWER-AP-DPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-AP-DPSEC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:15:14 2025
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

(CfprApDpsecForgedTransmit,
 CfprApPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-AP-TC-MIB",
    "CfprApDpsecForgedTransmit",
    "CfprApPolicyPolicyOwner")

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

cfprApDpsecObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprApDpsecMacTable_Object = MibTable
cfprApDpsecMacTable = _CfprApDpsecMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    cfprApDpsecMacTable.setStatus("current")
_CfprApDpsecMacEntry_Object = MibTableRow
cfprApDpsecMacEntry = _CfprApDpsecMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1)
)
cfprApDpsecMacEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-AP-DPSEC-MIB", "cfprApDpsecMacInstanceId"),
)
if mibBuilder.loadTexts:
    cfprApDpsecMacEntry.setStatus("current")
_CfprApDpsecMacInstanceId_Type = CfprApManagedObjectId
_CfprApDpsecMacInstanceId_Object = MibTableColumn
cfprApDpsecMacInstanceId = _CfprApDpsecMacInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 1),
    _CfprApDpsecMacInstanceId_Type()
)
cfprApDpsecMacInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprApDpsecMacInstanceId.setStatus("current")
_CfprApDpsecMacDn_Type = CfprApManagedObjectDn
_CfprApDpsecMacDn_Object = MibTableColumn
cfprApDpsecMacDn = _CfprApDpsecMacDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 2),
    _CfprApDpsecMacDn_Type()
)
cfprApDpsecMacDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDpsecMacDn.setStatus("current")
_CfprApDpsecMacRn_Type = SnmpAdminString
_CfprApDpsecMacRn_Object = MibTableColumn
cfprApDpsecMacRn = _CfprApDpsecMacRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 3),
    _CfprApDpsecMacRn_Type()
)
cfprApDpsecMacRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDpsecMacRn.setStatus("current")
_CfprApDpsecMacDescr_Type = SnmpAdminString
_CfprApDpsecMacDescr_Object = MibTableColumn
cfprApDpsecMacDescr = _CfprApDpsecMacDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 4),
    _CfprApDpsecMacDescr_Type()
)
cfprApDpsecMacDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDpsecMacDescr.setStatus("current")
_CfprApDpsecMacForge_Type = CfprApDpsecForgedTransmit
_CfprApDpsecMacForge_Object = MibTableColumn
cfprApDpsecMacForge = _CfprApDpsecMacForge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 5),
    _CfprApDpsecMacForge_Type()
)
cfprApDpsecMacForge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDpsecMacForge.setStatus("current")
_CfprApDpsecMacIntId_Type = SnmpAdminString
_CfprApDpsecMacIntId_Object = MibTableColumn
cfprApDpsecMacIntId = _CfprApDpsecMacIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 6),
    _CfprApDpsecMacIntId_Type()
)
cfprApDpsecMacIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDpsecMacIntId.setStatus("current")
_CfprApDpsecMacName_Type = SnmpAdminString
_CfprApDpsecMacName_Object = MibTableColumn
cfprApDpsecMacName = _CfprApDpsecMacName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 7),
    _CfprApDpsecMacName_Type()
)
cfprApDpsecMacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDpsecMacName.setStatus("current")
_CfprApDpsecMacPolicyLevel_Type = Gauge32
_CfprApDpsecMacPolicyLevel_Object = MibTableColumn
cfprApDpsecMacPolicyLevel = _CfprApDpsecMacPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 8),
    _CfprApDpsecMacPolicyLevel_Type()
)
cfprApDpsecMacPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDpsecMacPolicyLevel.setStatus("current")
_CfprApDpsecMacPolicyOwner_Type = CfprApPolicyPolicyOwner
_CfprApDpsecMacPolicyOwner_Object = MibTableColumn
cfprApDpsecMacPolicyOwner = _CfprApDpsecMacPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 2, 1, 18, 1, 1, 9),
    _CfprApDpsecMacPolicyOwner_Type()
)
cfprApDpsecMacPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprApDpsecMacPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-AP-DPSEC-MIB",
    **{"cfprApDpsecObjects": cfprApDpsecObjects,
       "cfprApDpsecMacTable": cfprApDpsecMacTable,
       "cfprApDpsecMacEntry": cfprApDpsecMacEntry,
       "cfprApDpsecMacInstanceId": cfprApDpsecMacInstanceId,
       "cfprApDpsecMacDn": cfprApDpsecMacDn,
       "cfprApDpsecMacRn": cfprApDpsecMacRn,
       "cfprApDpsecMacDescr": cfprApDpsecMacDescr,
       "cfprApDpsecMacForge": cfprApDpsecMacForge,
       "cfprApDpsecMacIntId": cfprApDpsecMacIntId,
       "cfprApDpsecMacName": cfprApDpsecMacName,
       "cfprApDpsecMacPolicyLevel": cfprApDpsecMacPolicyLevel,
       "cfprApDpsecMacPolicyOwner": cfprApDpsecMacPolicyOwner}
)
