# SNMP MIB module (CISCO-FIREPOWER-HOSTIMG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-FIREPOWER-HOSTIMG-MIB.mib
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

(CfprHostimgComposition,
 CfprHostimgDistribution,
 CfprHostimgImgType,
 CfprHostimgType,
 CfprPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-FIREPOWER-TC-MIB",
    "CfprHostimgComposition",
    "CfprHostimgDistribution",
    "CfprHostimgImgType",
    "CfprHostimgType",
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

cfprHostimgObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CfprHostimgPolicyTable_Object = MibTable
cfprHostimgPolicyTable = _CfprHostimgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1)
)
if mibBuilder.loadTexts:
    cfprHostimgPolicyTable.setStatus("current")
_CfprHostimgPolicyEntry_Object = MibTableRow
cfprHostimgPolicyEntry = _CfprHostimgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1)
)
cfprHostimgPolicyEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-HOSTIMG-MIB", "cfprHostimgPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cfprHostimgPolicyEntry.setStatus("current")
_CfprHostimgPolicyInstanceId_Type = CfprManagedObjectId
_CfprHostimgPolicyInstanceId_Object = MibTableColumn
cfprHostimgPolicyInstanceId = _CfprHostimgPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 1),
    _CfprHostimgPolicyInstanceId_Type()
)
cfprHostimgPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprHostimgPolicyInstanceId.setStatus("current")
_CfprHostimgPolicyDn_Type = CfprManagedObjectDn
_CfprHostimgPolicyDn_Object = MibTableColumn
cfprHostimgPolicyDn = _CfprHostimgPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 2),
    _CfprHostimgPolicyDn_Type()
)
cfprHostimgPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyDn.setStatus("current")
_CfprHostimgPolicyRn_Type = SnmpAdminString
_CfprHostimgPolicyRn_Object = MibTableColumn
cfprHostimgPolicyRn = _CfprHostimgPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 3),
    _CfprHostimgPolicyRn_Type()
)
cfprHostimgPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyRn.setStatus("current")
_CfprHostimgPolicyComp_Type = CfprHostimgComposition
_CfprHostimgPolicyComp_Object = MibTableColumn
cfprHostimgPolicyComp = _CfprHostimgPolicyComp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 4),
    _CfprHostimgPolicyComp_Type()
)
cfprHostimgPolicyComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyComp.setStatus("current")
_CfprHostimgPolicyConf_Type = SnmpAdminString
_CfprHostimgPolicyConf_Object = MibTableColumn
cfprHostimgPolicyConf = _CfprHostimgPolicyConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 5),
    _CfprHostimgPolicyConf_Type()
)
cfprHostimgPolicyConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyConf.setStatus("current")
_CfprHostimgPolicyDescr_Type = SnmpAdminString
_CfprHostimgPolicyDescr_Object = MibTableColumn
cfprHostimgPolicyDescr = _CfprHostimgPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 6),
    _CfprHostimgPolicyDescr_Type()
)
cfprHostimgPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyDescr.setStatus("current")
_CfprHostimgPolicyDistro_Type = CfprHostimgDistribution
_CfprHostimgPolicyDistro_Object = MibTableColumn
cfprHostimgPolicyDistro = _CfprHostimgPolicyDistro_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 7),
    _CfprHostimgPolicyDistro_Type()
)
cfprHostimgPolicyDistro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyDistro.setStatus("current")
_CfprHostimgPolicyIntId_Type = SnmpAdminString
_CfprHostimgPolicyIntId_Object = MibTableColumn
cfprHostimgPolicyIntId = _CfprHostimgPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 8),
    _CfprHostimgPolicyIntId_Type()
)
cfprHostimgPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyIntId.setStatus("current")
_CfprHostimgPolicyName_Type = SnmpAdminString
_CfprHostimgPolicyName_Object = MibTableColumn
cfprHostimgPolicyName = _CfprHostimgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 9),
    _CfprHostimgPolicyName_Type()
)
cfprHostimgPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyName.setStatus("current")
_CfprHostimgPolicyPolicyLevel_Type = Gauge32
_CfprHostimgPolicyPolicyLevel_Object = MibTableColumn
cfprHostimgPolicyPolicyLevel = _CfprHostimgPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 10),
    _CfprHostimgPolicyPolicyLevel_Type()
)
cfprHostimgPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyPolicyLevel.setStatus("current")
_CfprHostimgPolicyPolicyOwner_Type = CfprPolicyPolicyOwner
_CfprHostimgPolicyPolicyOwner_Object = MibTableColumn
cfprHostimgPolicyPolicyOwner = _CfprHostimgPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 11),
    _CfprHostimgPolicyPolicyOwner_Type()
)
cfprHostimgPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyPolicyOwner.setStatus("current")
_CfprHostimgPolicyType_Type = CfprHostimgImgType
_CfprHostimgPolicyType_Object = MibTableColumn
cfprHostimgPolicyType = _CfprHostimgPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 1, 1, 12),
    _CfprHostimgPolicyType_Type()
)
cfprHostimgPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgPolicyType.setStatus("current")
_CfprHostimgTargetTable_Object = MibTable
cfprHostimgTargetTable = _CfprHostimgTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2)
)
if mibBuilder.loadTexts:
    cfprHostimgTargetTable.setStatus("current")
_CfprHostimgTargetEntry_Object = MibTableRow
cfprHostimgTargetEntry = _CfprHostimgTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2, 1)
)
cfprHostimgTargetEntry.setIndexNames(
    (0, "CISCO-FIREPOWER-HOSTIMG-MIB", "cfprHostimgTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cfprHostimgTargetEntry.setStatus("current")
_CfprHostimgTargetInstanceId_Type = CfprManagedObjectId
_CfprHostimgTargetInstanceId_Object = MibTableColumn
cfprHostimgTargetInstanceId = _CfprHostimgTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2, 1, 1),
    _CfprHostimgTargetInstanceId_Type()
)
cfprHostimgTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfprHostimgTargetInstanceId.setStatus("current")
_CfprHostimgTargetDn_Type = CfprManagedObjectDn
_CfprHostimgTargetDn_Object = MibTableColumn
cfprHostimgTargetDn = _CfprHostimgTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2, 1, 2),
    _CfprHostimgTargetDn_Type()
)
cfprHostimgTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgTargetDn.setStatus("current")
_CfprHostimgTargetRn_Type = SnmpAdminString
_CfprHostimgTargetRn_Object = MibTableColumn
cfprHostimgTargetRn = _CfprHostimgTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2, 1, 3),
    _CfprHostimgTargetRn_Type()
)
cfprHostimgTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgTargetRn.setStatus("current")
_CfprHostimgTargetName_Type = SnmpAdminString
_CfprHostimgTargetName_Object = MibTableColumn
cfprHostimgTargetName = _CfprHostimgTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2, 1, 4),
    _CfprHostimgTargetName_Type()
)
cfprHostimgTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgTargetName.setStatus("current")
_CfprHostimgTargetOrder_Type = Gauge32
_CfprHostimgTargetOrder_Object = MibTableColumn
cfprHostimgTargetOrder = _CfprHostimgTargetOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2, 1, 5),
    _CfprHostimgTargetOrder_Type()
)
cfprHostimgTargetOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgTargetOrder.setStatus("current")
_CfprHostimgTargetType_Type = CfprHostimgType
_CfprHostimgTargetType_Object = MibTableColumn
cfprHostimgTargetType = _CfprHostimgTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2, 1, 6),
    _CfprHostimgTargetType_Type()
)
cfprHostimgTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgTargetType.setStatus("current")
_CfprHostimgTargetUri_Type = SnmpAdminString
_CfprHostimgTargetUri_Object = MibTableColumn
cfprHostimgTargetUri = _CfprHostimgTargetUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 826, 1, 35, 2, 1, 7),
    _CfprHostimgTargetUri_Type()
)
cfprHostimgTargetUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfprHostimgTargetUri.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FIREPOWER-HOSTIMG-MIB",
    **{"cfprHostimgObjects": cfprHostimgObjects,
       "cfprHostimgPolicyTable": cfprHostimgPolicyTable,
       "cfprHostimgPolicyEntry": cfprHostimgPolicyEntry,
       "cfprHostimgPolicyInstanceId": cfprHostimgPolicyInstanceId,
       "cfprHostimgPolicyDn": cfprHostimgPolicyDn,
       "cfprHostimgPolicyRn": cfprHostimgPolicyRn,
       "cfprHostimgPolicyComp": cfprHostimgPolicyComp,
       "cfprHostimgPolicyConf": cfprHostimgPolicyConf,
       "cfprHostimgPolicyDescr": cfprHostimgPolicyDescr,
       "cfprHostimgPolicyDistro": cfprHostimgPolicyDistro,
       "cfprHostimgPolicyIntId": cfprHostimgPolicyIntId,
       "cfprHostimgPolicyName": cfprHostimgPolicyName,
       "cfprHostimgPolicyPolicyLevel": cfprHostimgPolicyPolicyLevel,
       "cfprHostimgPolicyPolicyOwner": cfprHostimgPolicyPolicyOwner,
       "cfprHostimgPolicyType": cfprHostimgPolicyType,
       "cfprHostimgTargetTable": cfprHostimgTargetTable,
       "cfprHostimgTargetEntry": cfprHostimgTargetEntry,
       "cfprHostimgTargetInstanceId": cfprHostimgTargetInstanceId,
       "cfprHostimgTargetDn": cfprHostimgTargetDn,
       "cfprHostimgTargetRn": cfprHostimgTargetRn,
       "cfprHostimgTargetName": cfprHostimgTargetName,
       "cfprHostimgTargetOrder": cfprHostimgTargetOrder,
       "cfprHostimgTargetType": cfprHostimgTargetType,
       "cfprHostimgTargetUri": cfprHostimgTargetUri}
)
