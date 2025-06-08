# SNMP MIB module (CISCO-FIREPOWER-IMGPROV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-IMGPROV-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:24:11 2025
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

(CfprPolicyPolicyOwner,) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
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

cfprImgprovObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprImgprovPolicyTable_Object = MibTable
cfprImgprovPolicyTable = _CfprImgprovPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1)
)
if mibBuilder.loadTexts:
    cfprImgprovPolicyTable.setStatus("current")
_CfprImgprovPolicyEntry_Object = MibTableRow
cfprImgprovPolicyEntry = _CfprImgprovPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1)
)
cfprImgprovPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IMGPROV-MIB", "cfprImgprovPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprImgprovPolicyEntry.setStatus("current")
_CfprImgprovPolicyInstanceId_Type = CfprManagedObjectId
_CfprImgprovPolicyInstanceId_Object = MibTableColumn
cfprImgprovPolicyInstanceId = _CfprImgprovPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1, 1),
    _CfprImgprovPolicyInstanceId_Type()
)
cfprImgprovPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprImgprovPolicyInstanceId.setStatus("current")
_CfprImgprovPolicyDn_Type = CfprManagedObjectDn
_CfprImgprovPolicyDn_Object = MibTableColumn
cfprImgprovPolicyDn = _CfprImgprovPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1, 2),
    _CfprImgprovPolicyDn_Type()
)
cfprImgprovPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovPolicyDn.setStatus("current")
_CfprImgprovPolicyRn_Type = SnmpAdminString
_CfprImgprovPolicyRn_Object = MibTableColumn
cfprImgprovPolicyRn = _CfprImgprovPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1, 3),
    _CfprImgprovPolicyRn_Type()
)
cfprImgprovPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovPolicyRn.setStatus("current")
_CfprImgprovPolicyDescr_Type = SnmpAdminString
_CfprImgprovPolicyDescr_Object = MibTableColumn
cfprImgprovPolicyDescr = _CfprImgprovPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1, 4),
    _CfprImgprovPolicyDescr_Type()
)
cfprImgprovPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovPolicyDescr.setStatus("current")
_CfprImgprovPolicyIntId_Type = SnmpAdminString
_CfprImgprovPolicyIntId_Object = MibTableColumn
cfprImgprovPolicyIntId = _CfprImgprovPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1, 5),
    _CfprImgprovPolicyIntId_Type()
)
cfprImgprovPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovPolicyIntId.setStatus("current")
_CfprImgprovPolicyName_Type = SnmpAdminString
_CfprImgprovPolicyName_Object = MibTableColumn
cfprImgprovPolicyName = _CfprImgprovPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1, 6),
    _CfprImgprovPolicyName_Type()
)
cfprImgprovPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovPolicyName.setStatus("current")
_CfprImgprovPolicyPolicyLevel_Type = Gauge32
_CfprImgprovPolicyPolicyLevel_Object = MibTableColumn
cfprImgprovPolicyPolicyLevel = _CfprImgprovPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1, 7),
    _CfprImgprovPolicyPolicyLevel_Type()
)
cfprImgprovPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovPolicyPolicyLevel.setStatus("current")
_CfprImgprovPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprImgprovPolicyPolicyOwner_Object = MibTableColumn
cfprImgprovPolicyPolicyOwner = _CfprImgprovPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 1, 1, 8),
    _CfprImgprovPolicyPolicyOwner_Type()
)
cfprImgprovPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovPolicyPolicyOwner.setStatus("current")
_CfprImgprovTargetTable_Object = MibTable
cfprImgprovTargetTable = _CfprImgprovTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 2)
)
if mibBuilder.loadTexts:
    cfprImgprovTargetTable.setStatus("current")
_CfprImgprovTargetEntry_Object = MibTableRow
cfprImgprovTargetEntry = _CfprImgprovTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 2, 1)
)
cfprImgprovTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-IMGPROV-MIB", "cfprImgprovTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprImgprovTargetEntry.setStatus("current")
_CfprImgprovTargetInstanceId_Type = CfprManagedObjectId
_CfprImgprovTargetInstanceId_Object = MibTableColumn
cfprImgprovTargetInstanceId = _CfprImgprovTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 2, 1, 1),
    _CfprImgprovTargetInstanceId_Type()
)
cfprImgprovTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprImgprovTargetInstanceId.setStatus("current")
_CfprImgprovTargetDn_Type = CfprManagedObjectDn
_CfprImgprovTargetDn_Object = MibTableColumn
cfprImgprovTargetDn = _CfprImgprovTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 2, 1, 2),
    _CfprImgprovTargetDn_Type()
)
cfprImgprovTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovTargetDn.setStatus("current")
_CfprImgprovTargetRn_Type = SnmpAdminString
_CfprImgprovTargetRn_Object = MibTableColumn
cfprImgprovTargetRn = _CfprImgprovTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 2, 1, 3),
    _CfprImgprovTargetRn_Type()
)
cfprImgprovTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovTargetRn.setStatus("current")
_CfprImgprovTargetName_Type = SnmpAdminString
_CfprImgprovTargetName_Object = MibTableColumn
cfprImgprovTargetName = _CfprImgprovTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 37, 2, 1, 4),
    _CfprImgprovTargetName_Type()
)
cfprImgprovTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprImgprovTargetName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-IMGPROV-MIB",
    **{"cfprImgprovObjects": cfprImgprovObjects,
       "cfprImgprovPolicyTable": cfprImgprovPolicyTable,
       "cfprImgprovPolicyEntry": cfprImgprovPolicyEntry,
       "cfprImgprovPolicyInstanceId": cfprImgprovPolicyInstanceId,
       "cfprImgprovPolicyDn": cfprImgprovPolicyDn,
       "cfprImgprovPolicyRn": cfprImgprovPolicyRn,
       "cfprImgprovPolicyDescr": cfprImgprovPolicyDescr,
       "cfprImgprovPolicyIntId": cfprImgprovPolicyIntId,
       "cfprImgprovPolicyName": cfprImgprovPolicyName,
       "cfprImgprovPolicyPolicyLevel": cfprImgprovPolicyPolicyLevel,
       "cfprImgprovPolicyPolicyOwner": cfprImgprovPolicyPolicyOwner,
       "cfprImgprovTargetTable": cfprImgprovTargetTable,
       "cfprImgprovTargetEntry": cfprImgprovTargetEntry,
       "cfprImgprovTargetInstanceId": cfprImgprovTargetInstanceId,
       "cfprImgprovTargetDn": cfprImgprovTargetDn,
       "cfprImgprovTargetRn": cfprImgprovTargetRn,
       "cfprImgprovTargetName": cfprImgprovTargetName}
)
