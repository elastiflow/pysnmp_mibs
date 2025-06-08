# SNMP MIB module (CISCO-FIREPOWER-DPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-DPSEC-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:10 2025
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

(CfprDpsecForgedTransmit,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprDpsecForgedTransmit",
    "CfprPolicyPolicyOwner")

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

cfprDpsecObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprDpsecMacTable_Object = MibTable
cfprDpsecMacTable = _CfprDpsecMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1)
)
if mibBuilder.loadTexts:
    cfprDpsecMacTable.setStatus("current")
_CfprDpsecMacEntry_Object = MibTableRow
cfprDpsecMacEntry = _CfprDpsecMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1)
)
cfprDpsecMacEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-DPSEC-MIB", "cfprDpsecMacInstanceId"),
)
if mibBuilder.loadTexts:
    cfprDpsecMacEntry.setStatus("current")
_CfprDpsecMacInstanceId_Type = CfprManagedObjectId
_CfprDpsecMacInstanceId_Object = MibTableColumn
cfprDpsecMacInstanceId = _CfprDpsecMacInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 1),
    _CfprDpsecMacInstanceId_Type()
)
cfprDpsecMacInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprDpsecMacInstanceId.setStatus("current")
_CfprDpsecMacDn_Type = CfprManagedObjectDn
_CfprDpsecMacDn_Object = MibTableColumn
cfprDpsecMacDn = _CfprDpsecMacDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 2),
    _CfprDpsecMacDn_Type()
)
cfprDpsecMacDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDpsecMacDn.setStatus("current")
_CfprDpsecMacRn_Type = SnmpAdminString
_CfprDpsecMacRn_Object = MibTableColumn
cfprDpsecMacRn = _CfprDpsecMacRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 3),
    _CfprDpsecMacRn_Type()
)
cfprDpsecMacRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDpsecMacRn.setStatus("current")
_CfprDpsecMacDescr_Type = SnmpAdminString
_CfprDpsecMacDescr_Object = MibTableColumn
cfprDpsecMacDescr = _CfprDpsecMacDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 4),
    _CfprDpsecMacDescr_Type()
)
cfprDpsecMacDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDpsecMacDescr.setStatus("current")
_CfprDpsecMacForge_Type = CfprDpsecForgedTransmit
_CfprDpsecMacForge_Object = MibTableColumn
cfprDpsecMacForge = _CfprDpsecMacForge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 5),
    _CfprDpsecMacForge_Type()
)
cfprDpsecMacForge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDpsecMacForge.setStatus("current")
_CfprDpsecMacIntId_Type = SnmpAdminString
_CfprDpsecMacIntId_Object = MibTableColumn
cfprDpsecMacIntId = _CfprDpsecMacIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 6),
    _CfprDpsecMacIntId_Type()
)
cfprDpsecMacIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDpsecMacIntId.setStatus("current")
_CfprDpsecMacName_Type = SnmpAdminString
_CfprDpsecMacName_Object = MibTableColumn
cfprDpsecMacName = _CfprDpsecMacName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 7),
    _CfprDpsecMacName_Type()
)
cfprDpsecMacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDpsecMacName.setStatus("current")
_CfprDpsecMacPolicyLevel_Type = Gauge32
_CfprDpsecMacPolicyLevel_Object = MibTableColumn
cfprDpsecMacPolicyLevel = _CfprDpsecMacPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 8),
    _CfprDpsecMacPolicyLevel_Type()
)
cfprDpsecMacPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDpsecMacPolicyLevel.setStatus("current")
_CfprDpsecMacPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprDpsecMacPolicyOwner_Object = MibTableColumn
cfprDpsecMacPolicyOwner = _CfprDpsecMacPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 18, 1, 1, 9),
    _CfprDpsecMacPolicyOwner_Type()
)
cfprDpsecMacPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprDpsecMacPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-DPSEC-MIB",
    **{"cfprDpsecObjects": cfprDpsecObjects,
       "cfprDpsecMacTable": cfprDpsecMacTable,
       "cfprDpsecMacEntry": cfprDpsecMacEntry,
       "cfprDpsecMacInstanceId": cfprDpsecMacInstanceId,
       "cfprDpsecMacDn": cfprDpsecMacDn,
       "cfprDpsecMacRn": cfprDpsecMacRn,
       "cfprDpsecMacDescr": cfprDpsecMacDescr,
       "cfprDpsecMacForge": cfprDpsecMacForge,
       "cfprDpsecMacIntId": cfprDpsecMacIntId,
       "cfprDpsecMacName": cfprDpsecMacName,
       "cfprDpsecMacPolicyLevel": cfprDpsecMacPolicyLevel,
       "cfprDpsecMacPolicyOwner": cfprDpsecMacPolicyOwner}
)
